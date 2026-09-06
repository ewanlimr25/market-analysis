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
    assert state["ledger"] == {"emitted": 2, "skipped": 0, "graded": 0, "ledger_open": True}
    again = SD.run(None, ENTRY, str(tmp_path), iv, rows_loader, close_loader, force_ledger=True)
    assert again["ledger"]["emitted"] == 0 and again["ledger"]["skipped"] == 2
    assert state["open_positions"] == {"SPY-PS": 1, "SPY-IC": 1} or again["open_positions"] == {"SPY-PS": 1, "SPY-IC": 1}
    # a fourth position in a sleeve would be capped: seed three open signals and re-run on a later Friday
    graded = SD.run(None, EXP, str(tmp_path), iv, rows_loader, close_loader, force_ledger=True)
    assert graded["ledger"]["graded"] == 2 and [g["structure"] for g in graded["graded"]] == ["PS", "IC"]
    led = L.read_ledger(str(tmp_path))
    assert len(led) == 2 and (led.settle_close == 92.0).all() and led.graded_at.eq(EXP.isoformat()).all()
    assert SD.run(None, EXP, str(tmp_path), iv, rows_loader, close_loader, force_ledger=True)["ledger"]["graded"] == 0
    running = graded["running"]
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
