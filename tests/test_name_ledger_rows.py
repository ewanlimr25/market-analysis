"""DESIGN/70 §6: one `sheet-1.0` row per CAN_PRICE sheet (champion on PASS, exploration on X1 or a
failing S-C filter), two `disc-1.0` rows per owner call, all stamped with policy columns."""
from __future__ import annotations

from datetime import date

import pandas as pd
import pytest

from engine import ledger as L
from engine import policy as POL
from engine.name import ledger_rows as LR

pytestmark = pytest.mark.unit

D = date(2026, 9, 18)
IB = {"family": "IB", "expiry": "2026-10-16", "mark": 7.40, "max_loss": 710.0, "cost": 31.0, "mark_source": "cboe_chain 2026-09-18",
      "legs": [{"right": "P", "strike": 208.0, "side": 1, "mark": 1.1}, {"right": "P", "strike": 222.5, "side": -1, "mark": 4.9},
               {"right": "C", "strike": 222.5, "side": -1, "mark": 5.0}, {"right": "C", "strike": 237.0, "side": 1, "mark": 1.4}]}
SHARES = {"family": "SHARES", "entry": 222.27, "stop": 211.9, "target": 243.0, "max_loss": 10.37, "cost": 0.22, "n": 48,
          "mark_source": "screener 2026-09-18"}
DV = {"family": "DEBIT_VERTICAL", "expiry": "2026-10-16", "mark": -4.2, "max_loss": 420.0, "cost": 2.0, "mark_source": "cboe_chain 2026-09-18",
      "legs": [{"right": "C", "strike": 222.5, "side": 1, "mark": 8.0}, {"right": "C", "strike": 235.0, "side": -1, "mark": 3.8}]}
LIQ_OK = {"can_price": True}
LIQ_NO = {"can_price": False}


def test_champion_when_sc_passes_and_no_x1():
    row = LR.sheet_row("OKLO", D, LIQ_OK, {"x1": False, "sc": {"pass": True, "failing": None}}, [IB])
    assert row["policy_id"] == "sheet-1.0" and row["role"] == POL.ROLE_CHAMPION and row["gate_verdict"] == "PASS"
    assert row["variant"] == "sheet" and row["structure"] == "IB" and row["post"] == "2026-10-16"
    assert row["unit_id"] == "OKLO:2026-10-16" and row["n"] == 1 and row["credit"] == 7.40
    assert (row["k1"], row["k2"], row["k3"], row["k4"]) == (208.0, 222.5, 222.5, 237.0)
    assert (row["r1"], row["r2"], row["r3"], row["r4"]) == ("P", "P", "C", "C")


def test_exploration_with_the_failing_filter_as_gate():
    row = LR.sheet_row("NVDA", D, LIQ_OK, {"x1": False, "sc": {"pass": False, "failing": "F3"}}, [IB])
    assert row["role"] == POL.ROLE_EXPLORATION and row["gate_verdict"] == "F3"


def test_x1_wins_over_a_filter_failure():
    row = LR.sheet_row("NVDA", D, LIQ_OK, {"x1": True, "sc": {"pass": False, "failing": "F3"}}, [IB])
    assert row["role"] == POL.ROLE_EXPLORATION and row["gate_verdict"] == "X1"


def test_cannot_price_writes_no_sheet_row():
    assert LR.sheet_row("BL", D, LIQ_NO, {"x1": False, "sc": {"pass": True}}, [IB]) is None


def test_unpriced_ib_writes_no_sheet_row():
    assert LR.sheet_row("X", D, LIQ_OK, {"x1": False, "sc": {"pass": True}}, [{**IB, "mark": None}]) is None
    assert LR.sheet_row("X", D, LIQ_OK, {"x1": False, "sc": {"pass": True}}, []) is None


def test_disc_rows_are_shares_and_the_debit_vertical_with_the_context_tag():
    rows = LR.disc_rows("NVDA", D, "long", [SHARES, DV, IB], context_read="sheet_only")
    assert [r["structure"] for r in rows] == ["SHARES", "DEBIT_VERTICAL"]
    assert all(r["policy_id"] == "disc-1.0" and r["role"] == POL.ROLE_EXPLORATION and r["variant"] == "long" for r in rows)
    assert all(r["context_read"] == "sheet_only" for r in rows)
    sh = rows[0]
    assert sh["post"] == "2026-10-19" and sh["entry"] == 222.27 and sh["stop"] == 211.9 and sh["target"] == 243.0
    assert rows[1]["post"] == "2026-10-16" and rows[1]["k1"] == 222.5 and rows[1]["s1"] == 1


def test_disc_rows_skip_what_is_not_priced():
    assert LR.disc_rows("X", D, "short", [{**SHARES, "entry": None}], "none") == []
    assert [r["structure"] for r in LR.disc_rows("X", D, "short", [SHARES, {**DV, "mark": None}], "none")] == ["SHARES"]


def test_rows_pass_the_ledger_writer_and_are_write_once(tmp_path):
    rows = [LR.sheet_row("NVDA", D, LIQ_OK, {"x1": False, "sc": {"pass": False, "failing": "F3"}}, [IB])]
    rows += LR.disc_rows("NVDA", D, "long", [SHARES, DV], "none")
    df = LR.frame(rows)
    assert L.emit(str(tmp_path), df, D) == (3, 0)
    assert L.emit(str(tmp_path), df, D) == (0, 3)
    existing = L.read_signals(str(tmp_path))
    assert LR.already_present(existing, rows[0]) and not LR.already_present(pd.DataFrame(), rows[0])
    s = LR.summary(rows, [True, False, False])
    assert s[0]["written"] is False and s[0]["reason"] and s[1]["written"] is True
