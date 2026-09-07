"""engine.improve.basket_read: the wb-1.0 read (DESIGN/110-watch-basket.md §6, R3). Every test
uses a synthetic ledger frame or monkeypatched `universe_base_h21`/`live.load_closes` -- nothing
here touches the real ledger, the mart, or the network."""
from __future__ import annotations

import os
from datetime import date

import pandas as pd
import pytest

from engine.improve import basket_read as BR

pytestmark = pytest.mark.unit


def _row(ticker, d, basket, episode=True, excess_h21=None):
    return {"ticker": ticker, "date": d, "basket": basket, "episode": episode, "excess_h21": excess_h21}


# ---- episode_rows ---------------------------------------------------------------------------------

def test_episode_rows_keeps_only_episode_true_and_resolved_h21():
    ledger = pd.DataFrame([
        _row("A", date(2026, 6, 1), "LONG", episode=True, excess_h21=0.01),
        _row("B", date(2026, 6, 2), "LONG", episode=False, excess_h21=0.02),   # continuation, excluded
        _row("C", date(2026, 6, 3), "LONG", episode=True, excess_h21=None),    # unresolved, excluded
        _row("D", date(2026, 6, 4), "SHORT", episode=True, excess_h21=-0.01),  # wrong basket, excluded
    ])
    out = BR.episode_rows(ledger, "LONG")
    assert sorted(out["ticker"]) == ["A"]


def test_episode_rows_empty_ledger_is_empty():
    assert BR.episode_rows(pd.DataFrame(), "LONG").empty


# ---- projected_date ---------------------------------------------------------------------------------

def test_projected_date_returns_as_of_when_already_met():
    assert BR.projected_date([], date(2026, 6, 1), n_have=100) == "2026-06-01"


def test_projected_date_none_without_recent_episodes():
    old_dates = [date(2026, 1, 5)]           # long before the trailing window
    assert BR.projected_date(old_dates, date(2026, 6, 1), n_have=1) is None


def test_projected_date_none_without_any_episodes():
    assert BR.projected_date([], date(2026, 6, 1), n_have=0) is None


def test_projected_date_projects_forward_at_the_trailing_rate():
    from engine import calendar as cal
    as_of = date(2026, 6, 1)
    # 10 episodes in the trailing 30 sessions before as_of -> rate 1/3 per session
    recent = [cal.prev_session(as_of, k) for k in range(1, 11)]
    proj = BR.projected_date(recent, as_of, n_have=10, n_required=100)
    assert proj is not None
    # remaining 90 at rate 10/30 -> 270 sessions needed
    expected = cal.next_session(as_of, 270).isoformat()
    assert proj == expected


# ---- universe_base_h21 --------------------------------------------------------------------------------

def test_universe_base_h21_empty_nights_is_empty():
    out = BR.universe_base_h21([])
    assert out["n"] == 0 and out["hit_rate"] != out["hit_rate"] and out["mean_excess"] != out["mean_excess"]


def test_universe_base_h21_computes_hit_rate_and_mean(monkeypatch):
    d0 = date(2026, 6, 1)
    d1 = date(2026, 7, 1)      # stand-in "h21 later" date

    def fake_build_universe(dates):
        return pd.DataFrame({"ticker": ["A", "B"], "date": [d0, d0]})

    def fake_next_session(d, n):
        return d1

    closes = {("A", d0): 100.0, ("A", d1): 110.0, ("B", d0): 50.0, ("B", d1): 45.0,
              ("SPY", d0): 500.0, ("SPY", d1): 510.0}

    monkeypatch.setattr(BR.U, "build_universe", fake_build_universe)
    monkeypatch.setattr(BR.cal, "next_session", fake_next_session)
    monkeypatch.setattr(BR.LV, "load_closes", lambda tickers, dates, stocks_dir=None: closes)

    out = BR.universe_base_h21([d0])
    spy_ret = 510.0 / 500.0 - 1
    a_excess = 110.0 / 100.0 - 1 - spy_ret
    b_excess = 45.0 / 50.0 - 1 - spy_ret
    assert out["n"] == 2
    assert out["hit_rate"] == pytest.approx(0.5)          # A positive, B negative
    assert out["mean_excess"] == pytest.approx((a_excess + b_excess) / 2)


# ---- verdict -------------------------------------------------------------------------------------------

def _episodes(excesses, tickers=None):
    tickers = tickers or [f"T{i}" for i in range(len(excesses))]
    return pd.DataFrame({"ticker": tickers, "excess_h21": excesses})


def test_verdict_clears_when_hit_rate_and_t_clear_the_bar():
    # 20 episodes, 16 positive (80% hit) vs a 50% base -> +30pt, comfortably clears
    excesses = [0.05] * 16 + [-0.02] * 4
    v, reason, stats = BR.verdict(_episodes(excesses), {"n": 500, "hit_rate": 0.50, "mean_excess": 0.0})
    assert v == BR.CLEARS
    assert stats["n_episodes"] == 20 and stats["hit_rate"] == pytest.approx(0.8)
    assert "CLEARS" not in reason  # reason is a plain sentence, not the verdict word itself
    assert stats["clustered_t"] >= BR.MEAN_EXCESS_MIN_T


def test_verdict_fails_when_hit_rate_margin_not_met():
    excesses = [0.01] * 11 + [-0.01] * 9    # 55% hit vs 50% base: only +5pt, below the 10pt margin
    v, reason, stats = BR.verdict(_episodes(excesses), {"n": 500, "hit_rate": 0.50, "mean_excess": 0.0})
    assert v == BR.FAILS


def test_verdict_fails_when_mean_excess_not_positive():
    excesses = [0.05] * 16 + [-0.20] * 4    # 80% hit but the losses dominate the mean
    v, reason, stats = BR.verdict(_episodes(excesses), {"n": 500, "hit_rate": 0.50, "mean_excess": 0.0})
    assert stats["mean_excess"] < 0 or v == BR.FAILS


def test_verdict_fails_when_base_is_nan():
    excesses = [0.05] * 16 + [-0.02] * 4
    v, reason, stats = BR.verdict(_episodes(excesses), {"n": 0, "hit_rate": float("nan"), "mean_excess": float("nan")})
    assert v == BR.FAILS
    assert stats["binomial_p"] != stats["binomial_p"]      # NaN


def test_verdict_fails_on_empty_episodes():
    v, reason, stats = BR.verdict(_episodes([]), {"n": 500, "hit_rate": 0.5, "mean_excess": 0.0})
    assert v == BR.FAILS and stats["n_episodes"] == 0


# ---- read ----------------------------------------------------------------------------------------------

def _ledger_with_episodes(n: int, basket: str, excess: float = 0.05, start=date(2026, 1, 5)):
    from engine import calendar as cal
    rows = []
    for i in range(n):
        d = cal.next_session(start, i)
        rows.append(_row(f"T{i}", d, basket, episode=True, excess_h21=excess))
    return pd.DataFrame(rows)


def test_read_rejects_an_unknown_basket():
    with pytest.raises(ValueError, match="basket must be one of"):
        BR.read(pd.DataFrame(), "CONFLICT", date(2026, 12, 1))


def test_read_not_due_before_2026_12_01_even_with_100_episodes():
    ledger = _ledger_with_episodes(100, "LONG")
    out = BR.read(ledger, "LONG", date(2026, 11, 30))
    assert out["verdict"] == BR.NOT_DUE and out["n_episodes"] == 100
    assert "2026-12-01" in out["reason"]


def test_read_not_due_after_2026_12_01_without_100_episodes():
    ledger = _ledger_with_episodes(5, "LONG")
    out = BR.read(ledger, "LONG", date(2026, 12, 15))
    assert out["verdict"] == BR.NOT_DUE and out["n_episodes"] == 5


def test_read_due_computes_a_verdict_once_both_conditions_are_met(monkeypatch):
    ledger = _ledger_with_episodes(100, "LONG", excess=0.05)
    monkeypatch.setattr(BR, "universe_base_h21", lambda nights: {"n": 1000, "hit_rate": 0.40, "mean_excess": 0.0})
    out = BR.read(ledger, "LONG", date(2026, 12, 1))
    assert out["verdict"] == BR.CLEARS
    assert out["stats"]["n_episodes"] == 100


def test_read_projected_date_present_when_not_due():
    ledger = _ledger_with_episodes(10, "SHORT")
    out = BR.read(ledger, "SHORT", date(2026, 3, 1))
    assert out["verdict"] == BR.NOT_DUE
    assert "projected_date" in out


# ---- the write-once contract (DESIGN/110 §6 / §5's "refuses to run twice") -------------------------

def test_verdict_is_written_once_to_wb_1_0_basket_json_and_refuses_a_second_write(tmp_path, monkeypatch):
    from engine.improve import adjudicate as A
    ledger = _ledger_with_episodes(100, "LONG", excess=0.05)
    monkeypatch.setattr(BR, "universe_base_h21", lambda nights: {"n": 1000, "hit_rate": 0.40, "mean_excess": 0.0})
    out = BR.read(ledger, "LONG", date(2026, 12, 1))
    assert out["verdict"] in (BR.CLEARS, BR.FAILS)
    payload = {"policy_id": "wb-1.0", "kind": "basket", "basket": "LONG", **out}
    path = A.write_adjudication(str(tmp_path), "wb-1.0-LONG", payload)
    assert os.path.basename(path) == "wb-1.0-LONG.json" and os.path.exists(path)
    log = (tmp_path / "adjudications" / "LOG.md").read_text()
    assert "wb-1.0-LONG" in log and out["verdict"] in log
    with pytest.raises(FileExistsError):
        A.write_adjudication(str(tmp_path), "wb-1.0-LONG", payload)
