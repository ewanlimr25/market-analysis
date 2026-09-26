"""S-C R5 (DESIGN/90 §7, §10): the nightly step -- Friday entries and the exploration book into
`ledger/sc/`, grading at expiry (and the night after when the close was missing), a second grade writes
0 rows, the ledger closed before its open date, `sc_state` valid against the signals schema."""
from __future__ import annotations

from datetime import date

import jsonschema
import pandas as pd
import pytest

from engine import ledger as L
from engine import report as R
from engine import sc_daily as SCD
from engine import schema as SCH
from sc_fixtures import week

pytestmark = pytest.mark.unit

FRI = date(2026, 10, 2)                  # the ledger's first entry Friday
THU = date(2026, 10, 1)
EXP = date(2026, 10, 30)                 # 28 days later, a Friday
MON_AFTER = date(2026, 11, 2)


def _weeks(con, d):
    return week(d, EXP) if d == FRI else None


def _settle(closes: dict):
    return lambda con, tickers, start, d: (closes, {}, max(k[1] for k in closes) if closes else None)


CLOSES = {(t, FRI): 50.0 for t in ("AAA", "BBB", "CCC")} | {(t, EXP): 51.0 for t in ("AAA", "BBB", "CCC")}


def _run(tmp_path, d, closes=CLOSES, **kw):
    return SCD.run(None, d, str(tmp_path / "sc"), str(tmp_path / "sb"), week_loader=_weeks, settle_loader=_settle(closes), **kw)


def test_friday_writes_champion_and_exploration_rows(tmp_path):
    st = _run(tmp_path, FRI)
    sig = L.read_signals(str(tmp_path / "sc"))
    champ, expl = sig[sig.role == "champion"], sig[sig.role == "exploration"]
    assert st["is_entry_day"] and st["ledger"]["emitted"] == len(champ) == 6
    assert len(expl) == 6 and set(expl.gate_verdict) == {"PASS", "F3"}
    assert st["funnel"]["F3"] == 1 and st["funnel"]["F8"] == 1 and st["funnel"]["C1:selected"] == 2
    assert st["exploration"] == {"names": 3, "by_verdict": {"PASS": 2, "F3": 1}, "graded": 0}
    assert {s["pair"]: s["positions"] for s in st["open_book"]["sleeves"]} == {"C1-SS": 2, "C1-IB": 2, "C2-SS": 1, "C2-IB": 1}


def test_not_an_entry_day_and_the_closed_ledger_write_nothing(tmp_path):
    assert not _run(tmp_path, THU)["is_entry_day"]
    closed = SCD.run(None, date(2026, 9, 25), str(tmp_path / "sc2"), str(tmp_path / "sb"), week_loader=lambda c, d: week(d, EXP),
                     settle_loader=_settle(CLOSES))
    assert not closed["ledger_open"] and L.read_signals(str(tmp_path / "sc2")).empty
    assert closed["candidates"]                                               # still shown in the report


def test_emit_grade_round_trip_and_a_second_grade_writes_nothing(tmp_path):
    _run(tmp_path, FRI)
    st = _run(tmp_path, EXP)
    assert st["ledger"]["graded"] == 12 and len(st["graded"]) == 6 and st["exploration"]["graded"] == 6
    led = L.read_ledger(str(tmp_path / "sc"))
    assert set(led.settle_source) == {"prices"} and led["ror"].notna().all()
    again = _run(tmp_path, EXP)
    assert again["ledger"]["graded"] == 0 and len(L.read_ledger(str(tmp_path / "sc"))) == 12
    assert {p["pair"]: p["forward_weeks"] for p in again["progress"]} == {"C1-SS": 1, "C1-IB": 1, "C2-SS": 1, "C2-IB": 1}
    assert all(s["positions"] == 0 for s in again["open_book"]["sleeves"])


def test_a_missing_close_is_unsettled_then_graded_the_next_night(tmp_path):
    _run(tmp_path, FRI)
    no_close = {k: v for k, v in CLOSES.items() if k[1] == FRI}
    st = _run(tmp_path, EXP, closes=no_close)
    assert st["ledger"]["graded"] == 0 and len(st["unsettled"]) == 12
    later = _run(tmp_path, MON_AFTER)
    assert later["ledger"]["graded"] == 12


def test_the_book_budget_reads_the_sb_ledger(tmp_path):
    sb = pd.DataFrame([{"ticker": "SPY", "E": FRI, "post": EXP, "variant": "B1", "structure": "PS",
                        "policy_id": "sb-1.0", "role": "champion", "gate_verdict": "ON"}])
    L.emit(str(tmp_path / "sb"), sb, FRI)
    st = _run(tmp_path, FRI)
    assert st["open_book"]["sb_open"] and st["open_book"]["sleeves"][1]["budget_usd"] == pytest.approx(4000.0)


def test_sc_state_matches_the_schema_and_renders(tmp_path):
    for d in (FRI, EXP):
        st = SCH.clean(_run(tmp_path, d))
        schema = SCH.load_schema()
        jsonschema.validate(st, {**schema["$defs"]["sc_state"], "$defs": schema["$defs"]})
        text = R.render_sc(st)
        assert "graded entry-weeks" in text
    err = SCH.clean({"date": FRI.isoformat(), "error": "S-C step failed: boom", "candidates": [], "graded": []})
    jsonschema.validate(err, {**schema["$defs"]["sc_state"], "$defs": schema["$defs"]})
    assert "failed" in R.render_sc(err)
