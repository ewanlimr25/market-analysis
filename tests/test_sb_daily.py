"""Q7: the S-B nightly step (DESIGN/80 §7): gate lines, emit on an entry day, grade at expiry
through ledger/sb/, idempotency, the report section. Loaders are injected; no panel, no network."""
from __future__ import annotations

from datetime import date

import pandas as pd
import pytest

from engine import calendar as cal
from engine import ledger as L
from engine import report as R
from engine import sb_daily as SD
from engine.strategies import sb_structures as SB
from test_sb_strategy import _rows, _index_vol, ENTRY, EXP

pytestmark = pytest.mark.unit


def _loaders(closes=None):
    def rows_loader(con, underlyings, d):
        return _rows().assign(underlying_symbol="SPY") if d == ENTRY else pd.DataFrame()
    def close_loader(con, ticker, d):
        return (closes or {}).get((ticker, d))
    return rows_loader, close_loader


def test_thursday_previews_fridays_gate_and_emits_nothing(tmp_path):
    rows_loader, close_loader = _loaders()
    state = SD.run(None, date(2026, 7, 9), str(tmp_path), _index_vol(), rows_loader, close_loader, force_ledger=True)
    assert state["is_entry_day"] is False and state["gate"]["SPY"]["reason"] in ("ON", "OFF:G2")
    assert state["gate_next"]["SPY"]["date"] == "2026-07-10"
    assert state["candidates"] == [] and state["ledger"]["emitted"] == 0
    assert L.read_signals(str(tmp_path)).empty


def test_friday_emits_both_structures_once_and_grades_them_at_expiry(tmp_path):
    rows_loader, close_loader = _loaders({("SPY", EXP): 92.0})
    iv = _index_vol()
    state = SD.run(None, ENTRY, str(tmp_path), iv, rows_loader, close_loader, force_ledger=True)
    assert state["is_entry_day"] is True and state["gate"]["SPY"]["reason"] == "ON"
    assert [c["structure"] for c in state["candidates"]] == ["PS", "IC"]
    assert state["ledger"] == {"emitted": 2, "skipped": 0, "graded": 0, "ledger_open": True, "exploration_emitted": 2, "exploration_skipped": 0}
    again = SD.run(None, ENTRY, str(tmp_path), iv, rows_loader, close_loader, force_ledger=True)
    assert again["ledger"]["emitted"] == 0 and again["ledger"]["skipped"] == 2
    assert state["open_positions"] == {"SPY-PS": 1, "SPY-IC": 1} or again["open_positions"] == {"SPY-PS": 1, "SPY-IC": 1}
    # a fourth position in a sleeve would be capped: seed three open signals and re-run on a later Friday
    graded = SD.run(None, EXP, str(tmp_path), iv, rows_loader, close_loader, force_ledger=True)
    assert graded["ledger"]["graded"] == 4 and [g["structure"] for g in graded["graded"] if g["role"] == "champion"] == ["PS", "IC"]
    led = L.read_ledger(str(tmp_path))
    assert len(led) == 4 and (led.settle_close == 92.0).all() and led.graded_at.eq(EXP.isoformat()).all()
    assert led.groupby("role").size().to_dict() == {"champion": 2, "exploration": 2}
    assert SD.run(None, EXP, str(tmp_path), iv, rows_loader, close_loader, force_ledger=True)["ledger"]["graded"] == 0
    running = [r for r in graded["running"] if r["role"] == "champion"]
    assert {r["sleeve"] for r in running} == {"SPY-PS", "SPY-IC"} and all(r["n"] == 1 for r in running)


def test_ledger_stays_closed_before_2026_09_11_unless_forced(tmp_path):
    rows_loader, close_loader = _loaders()
    state = SD.run(None, ENTRY, str(tmp_path), _index_vol(), rows_loader, close_loader, force_ledger=False)
    assert state["ledger"]["ledger_open"] is False and state["ledger"]["emitted"] == 0 and len(state["candidates"]) == 2
    assert L.read_signals(str(tmp_path)).empty


def test_unknown_gate_fails_closed_and_the_report_says_so(tmp_path):
    rows_loader, close_loader = _loaders()
    state = SD.run(None, ENTRY, str(tmp_path), pd.DataFrame(), rows_loader, close_loader, force_ledger=True)
    assert state["gate"]["SPY"]["reason"].startswith("UNKNOWN") and state["candidates"] == []
    text = R.render({"date": ENTRY.isoformat(), "season": "off", "preflight": {"ok": True}, "candidates": [], "suppressed": [],
                     "graded": [], "season_running": [], "ledger": {}, "sb_state": state})
    assert "## S-B state" in text and "UNKNOWN" in text and "SPY" in text
    assert "not implemented" not in text


# ---- DESIGN/100 P2: the exploration book -----------------------------------------------------------

def _off():
    from engine.strategies import sb_gate as G
    return G.GateState(ENTRY, date(2026, 7, 9), 18.0, 20.0, 15.0, 16.0, True, False, False, True, "OFF:G2")


def test_exploration_candidates_enter_one_contract_per_structure_when_the_gate_is_off():
    from engine.strategies import sb
    from engine.config import SB_PARAMS, SB_SIZING
    from test_sb_strategy import X
    res = sb.exploration_candidates("SPY", ENTRY, _rows(), _off(), X, SB_PARAMS, cal.is_trading_day)
    assert [t["structure"] for t in res.trades] == ["PS", "IC"] and res.skipped == []
    for t in res.trades:
        assert t["role"] == "exploration" and t["policy_id"] == "sb-1.0" and t["contracts"] == 1
        assert t["gate_verdict"] == "OFF:G2" and t["gate_reason"] == "OFF:G2"
        assert t["risk_usd"] == pytest.approx(t["max_loss_usd"])
    champion = sb.entry_candidates("SPY", ENTRY, _rows(), _off(), X, SB_PARAMS, SB_SIZING, cal.is_trading_day)
    assert champion.trades == [] and [s["reason"] for s in champion.skipped] == ["OFF:G2", "OFF:G2"]


def test_exploration_fails_closed_when_the_gate_is_unknown():
    from engine.strategies import sb, sb_gate as G
    from engine.config import SB_PARAMS
    from test_sb_strategy import X
    unknown = G.GateState(ENTRY, None, None, None, None, None, None, None, False, False, "UNKNOWN:no index-vol data")
    res = sb.exploration_candidates("SPY", ENTRY, _rows(), unknown, X, SB_PARAMS, cal.is_trading_day)
    assert res.trades == [] and all(s["reason"].startswith("UNKNOWN") for s in res.skipped)


def _gate_off_index_vol():
    """The strategy-test index-vol series with the entry-day level pushed below its median (gate OFF:G2)."""
    iv = _index_vol().copy()
    prev = date(2026, 7, 9)
    iv.loc[iv["date"] == prev, ["vix", "vxn"]] = 5.0
    return iv


def test_gate_off_friday_writes_exploration_rows_and_no_champion_rows(tmp_path):
    rows_loader, close_loader = _loaders({("SPY", EXP): 92.0})
    iv = _gate_off_index_vol()
    state = SD.run(None, ENTRY, str(tmp_path), iv, rows_loader, close_loader, force_ledger=True)
    assert state["gate"]["SPY"]["reason"] == "OFF:G2" and state["candidates"] == []
    assert [x["structure"] for x in state["exploration"]] == ["PS", "IC"]
    assert all(x["role"] == "exploration" and x["contracts"] == 1 and x["gate_verdict"] == "OFF:G2" for x in state["exploration"])
    assert state["ledger"] == {"emitted": 0, "skipped": 0, "graded": 0, "ledger_open": True, "exploration_emitted": 2, "exploration_skipped": 0}
    assert state["open_positions"] == {}                                  # the cap counts champion rows only
    sig = L.read_signals(str(tmp_path))
    assert len(sig) == 2 and set(sig.role) == {"exploration"} and set(sig.policy_id) == {"sb-1.0"}
    again = SD.run(None, ENTRY, str(tmp_path), iv, rows_loader, close_loader, force_ledger=True)
    assert again["ledger"]["exploration_emitted"] == 0 and again["ledger"]["exploration_skipped"] == 2
    graded = SD.run(None, EXP, str(tmp_path), iv, rows_loader, close_loader, force_ledger=True)
    assert graded["ledger"]["graded"] == 2 and all(g["role"] == "exploration" for g in graded["graded"])
    running = graded["running"]
    assert {(r["role"], r["sleeve"]) for r in running} == {("exploration", "SPY-PS"), ("exploration", "SPY-IC")}
    text = R.render({"date": ENTRY.isoformat(), "season": "off", "preflight": {"ok": True}, "candidates": [], "suppressed": [],
                     "graded": [], "season_running": [], "ledger": {}, "sb_state": state})
    assert "exploration" in text.lower() and "OFF:G2" in text


def test_gate_on_friday_writes_both_series_under_distinct_keys(tmp_path):
    rows_loader, close_loader = _loaders()
    state = SD.run(None, ENTRY, str(tmp_path), _index_vol(), rows_loader, close_loader, force_ledger=True)
    assert state["gate"]["SPY"]["reason"] == "ON"
    assert [c["role"] for c in state["candidates"]] == ["champion", "champion"]
    assert [x["role"] for x in state["exploration"]] == ["exploration", "exploration"]
    assert state["ledger"]["emitted"] == 2 and state["ledger"]["exploration_emitted"] == 2
    sig = L.read_signals(str(tmp_path))
    assert len(sig) == 4 and sig.groupby("role").size().to_dict() == {"champion": 2, "exploration": 2}
    assert (sig[sig.role == "exploration"].contracts == 1).all()
    assert state["open_positions"] == {"SPY-PS": 1, "SPY-IC": 1}


def test_exploration_does_not_write_before_the_ledger_opens(tmp_path):
    rows_loader, close_loader = _loaders()
    state = SD.run(None, ENTRY, str(tmp_path), _gate_off_index_vol(), rows_loader, close_loader, force_ledger=False)
    assert len(state["exploration"]) == 2 and state["ledger"]["exploration_emitted"] == 0
    assert L.read_signals(str(tmp_path)).empty


def test_nightly_honours_the_ledger_dir_argument(tmp_path, monkeypatch):
    """`make daily --ledger-dir X --force-ledger` must write S-B rows under X/sb, never the repo ledger."""
    from engine import daily as D
    from engine.config import LEDGER_DIR, LEDGER_SB_DIR
    from engine.mart import index_vol as IV
    rows_loader, close_loader = _loaders()
    monkeypatch.setattr(SD, "refresh_index_vol", lambda: {"ok": False, "error": "offline test"})
    monkeypatch.setattr(IV, "load_index_vol", lambda: _index_vol())
    monkeypatch.setattr(SD.sb_data, "load_entry_rows", rows_loader)
    monkeypatch.setattr(SD, "_default_close_loader", close_loader)
    assert D.sb_ledger_dir(LEDGER_DIR) == LEDGER_SB_DIR
    target = D.sb_ledger_dir(str(tmp_path))
    state = SD.nightly(None, ENTRY, True, target)
    assert state["ledger"]["emitted"] == 2 and state["ledger"]["exploration_emitted"] == 2 and state["refresh"]["ok"] is False
    assert len(L.read_signals(target)) == 4
    assert not (tmp_path / "forward_signals.parquet").exists()
