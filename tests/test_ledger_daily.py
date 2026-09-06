"""P6: forward ledger (idempotent emit / grade), templated report, and the daily grading step."""
from __future__ import annotations

import json
from datetime import date

import pandas as pd
import pytest

from engine import ledger as L
from engine import report as R
from engine import daily as D
from engine import marking as M
from engine.strategies import sa_structures as ST

pytestmark = pytest.mark.unit

PRE, POST = date(2026, 10, 14), date(2026, 10, 15)


def _signal(ticker="XYZ", variant="A1", structure="SS", legs=None, **kw):
    legs = legs or [
        {"name": "call", "option_chain_id": f"{ticker}261016C00100000", "option_type": "call", "strike": 100.0,
         "expiry": "2026-10-16", "side": -1, "entry_price": 4.0, "entry_spread": 0.06, "entry_tier": 1, "entry_source": "print_vwap"},
        {"name": "put", "option_chain_id": f"{ticker}261016P00100000", "option_type": "put", "strike": 100.0,
         "expiry": "2026-10-16", "side": -1, "entry_price": 3.6, "entry_spread": 0.07, "entry_tier": 1, "entry_source": "print_vwap"},
    ]
    row = {"ticker": ticker, "E": POST, "pre": PRE, "post": POST, "variant": variant, "structure": structure,
           "n": 1, "notional_usd": 10_000.0, "spot": 100.0, "implied": 0.08, "credit_entry": 7.6,
           "entry_cost_usd": 25.9, "stress_loss_usd": 1640.0, "max_loss_usd": None, "risk_usd": 1640.0,
           "credit_net_pct": 0.07341, "cap_pass": True, "cap_rank": 1, "sector": "Industrials",
           "season": "S3", "month": "2026-10", "legs_json": json.dumps(legs), "expiry": date(2026, 10, 16), "k": 100.0}
    row.update(kw)
    return row


# ---- ledger ------------------------------------------------------------------------------------

def test_emit_is_idempotent_on_the_key(tmp_path):
    cands = pd.DataFrame([_signal(), _signal(structure="IC"), _signal(ticker="ABC")])
    n_new, n_skip = L.emit(str(tmp_path), cands, emitted_on=PRE)
    assert (n_new, n_skip) == (3, 0)
    again = pd.DataFrame([_signal(credit_entry=99.0), _signal(ticker="NEW")])
    n_new, n_skip = L.emit(str(tmp_path), again, emitted_on=PRE)
    assert (n_new, n_skip) == (1, 1)
    sig = L.read_signals(str(tmp_path))
    assert len(sig) == 4 and sig[sig.ticker == "XYZ"].credit_entry.iloc[0] == 7.6   # never re-derived
    assert (sig.emitted_at == PRE.isoformat()).all()


def test_pending_lists_signals_with_post_today_and_no_grade_yet(tmp_path):
    L.emit(str(tmp_path), pd.DataFrame([_signal(), _signal(ticker="ABC"), _signal(ticker="LATER", post=date(2026, 10, 16))]), PRE)
    pend = L.pending(str(tmp_path), POST)
    assert set(pend.ticker) == {"XYZ", "ABC"}
    graded = pend[pend.ticker == "XYZ"].assign(net_usd=100.0, net_pct=0.01, exit_tier_max=1, model_exit=False)
    assert L.grade(str(tmp_path), graded, graded_on=POST) == (1, 0)
    assert set(L.pending(str(tmp_path), POST).ticker) == {"ABC"}
    assert L.grade(str(tmp_path), graded, graded_on=POST) == (0, 1)     # a graded row is never rewritten
    led = L.read_ledger(str(tmp_path))
    assert len(led) == 1 and led.graded_at.iloc[0] == POST.isoformat()


def test_read_missing_files_gives_empty_frames(tmp_path):
    assert L.read_signals(str(tmp_path)).empty and L.read_ledger(str(tmp_path)).empty
    assert L.pending(str(tmp_path), POST).empty


# ---- grading from the stored legs ----------------------------------------------------------------

def _post_rows():
    return {
        ("XYZ261016C00100000", POST): {"vwap_early": 1.2, "size_early": 20, "early_rel_spread": 0.05,
                                        "early_last_bid": 1.15, "early_last_ask": 1.25, "last_nbbo_bid": 1.1, "last_nbbo_ask": 1.3},
        ("XYZ261016P00100000", POST): {"vwap_early": 1.0, "size_early": 15, "early_rel_spread": 0.05,
                                        "early_last_bid": 0.95, "early_last_ask": 1.05, "last_nbbo_bid": 0.9, "last_nbbo_ask": 1.1},
    }


def test_grade_rows_recomputes_pnl_from_legs_json():
    resolver = M.MarkResolver(_post_rows(), lambda *a: None)
    sig = pd.DataFrame([_signal()])
    graded, dropped = D.grade_rows(sig, resolver)
    assert dropped.empty and len(graded) == 1
    g = graded.iloc[0]
    assert g.debit_exit == pytest.approx(2.2) and g.gross_usd == pytest.approx(540.0)
    expected_cost = (0.5 * 0.06 * 4.0 * 100 + 0.65) + (0.5 * 0.07 * 3.6 * 100 + 0.65) \
        + (0.5 * 0.05 * 1.2 * 100 + 0.65) + (0.5 * 0.05 * 1.0 * 100 + 0.65)
    assert g.net_usd == pytest.approx(540.0 - expected_cost)
    assert g.net_pct == pytest.approx((540.0 - expected_cost) / 10_000)
    assert g.exit_tier_max == 1 and bool(g.model_exit) is False


def test_grade_rows_drops_unmarkable_exits_with_reason():
    resolver = M.MarkResolver({}, lambda *a: None)
    graded, dropped = D.grade_rows(pd.DataFrame([_signal()]), resolver)
    assert graded.empty and dropped.iloc[0].reason == "unmarkable_exit"


def test_season_running_summarises_the_ledger():
    led = pd.DataFrame([{"variant": "A1", "structure": "SS", "season": "S3", "pre": PRE, "net_pct": 0.02, "net_usd": 200.0},
                        {"variant": "A1", "structure": "SS", "season": "S3", "pre": date(2026, 10, 20), "net_pct": -0.01, "net_usd": -100.0},
                        {"variant": "A2", "structure": "IC", "season": "S3", "pre": PRE, "net_pct": 0.005, "net_usd": 20.0}])
    run = D.season_running(led, "S3")
    a1 = [r for r in run if r["variant"] == "A1" and r["structure"] == "SS"][0]
    assert a1["n"] == 2 and a1["dates"] == 2 and a1["mean_net_pct"] == pytest.approx(0.005) and a1["net_usd_total"] == 100.0
    assert D.season_running(pd.DataFrame(), "S3") == []


# ---- report ---------------------------------------------------------------------------------------

def test_report_renders_candidates_suppressed_and_graded():
    signals = {"date": PRE.isoformat(), "season": "S3", "preflight": {"ok": True, "warnings": []},
               "candidates": [{**_signal(), "expiry": "2026-10-16", "E": POST.isoformat(), "pre": PRE.isoformat(), "post": POST.isoformat()}],
               "suppressed": [{"ticker": "BIG", "variant": "A1", "first_fail": "F3", "marketcap": 90e9}],
               "graded": [{"ticker": "OLD", "variant": "A1", "structure": "IC", "net_pct": 0.012, "net_usd": 120.0, "exit_tier_max": 1}],
               "season_running": [{"variant": "A1", "structure": "SS", "n": 2, "dates": 2, "mean_net_pct": 0.005,
                                   "t": 0.4, "net_usd_total": 100.0}],
               "ledger": {"emitted": 2, "skipped": 0, "graded": 1, "ledger_open": True},
               "sb_state": None}
    md = R.render(signals)
    assert md.startswith("# S-A daily") and "2026-10-14" in md
    assert "XYZ" in md and "BIG" in md and "F3" in md and "OLD" in md
    assert "A1" in md and "## S-B state" in md                      # S-B section (DESIGN/80 §7)


def test_report_says_so_when_no_event_clears():
    signals = {"date": PRE.isoformat(), "season": "S3", "preflight": {"ok": True, "warnings": []}, "candidates": [],
               "suppressed": [], "graded": [], "season_running": [], "ledger": {"emitted": 0, "skipped": 0, "graded": 0, "ledger_open": True},
               "sb_state": None}
    assert "no event tonight clears the filters" in R.render(signals)


def test_ledger_open_rule():
    assert D.ledger_open(date(2026, 10, 1)) and not D.ledger_open(date(2026, 9, 30))
