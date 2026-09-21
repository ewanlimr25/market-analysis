"""DESIGN/70 §6: `make daily` grades `ledger/name/` rows on their `post` session — option rows
intrinsic at the close, share rows by the next-open ±1R walk — write-once, bars injectable."""
from __future__ import annotations

from datetime import date

import pandas as pd
import pytest

from engine import ledger as L
from engine.name import grading as GR
from engine.name import ledger_rows as LR

pytestmark = pytest.mark.unit

D = date(2026, 9, 18)
POST = date(2026, 10, 16)
IB = {"family": "IB", "expiry": POST.isoformat(), "mark": 7.0, "max_loss": 800.0, "cost": 30.0, "mark_source": "s",
      "legs": [{"right": "P", "strike": 85.0, "side": 1, "mark": 1.0}, {"right": "P", "strike": 100.0, "side": -1, "mark": 4.5},
               {"right": "C", "strike": 100.0, "side": -1, "mark": 4.5}, {"right": "C", "strike": 115.0, "side": 1, "mark": 1.0}]}
SHARES = {"family": "SHARES", "entry": 100.0, "stop": 90.0, "target": 120.0, "max_loss": 10.0, "cost": 0.1, "n": 50,
          "mark_source": "s"}


def _bars(rows):
    return pd.DataFrame(rows, columns=["date", "open", "high", "low", "close"])


def _ledger(tmp_path, rows):
    L.emit(str(tmp_path), LR.frame(rows), D)
    return str(tmp_path)


def test_option_row_grades_intrinsic_at_the_post_close(tmp_path):
    row = LR.sheet_row("X", D, {"can_price": True}, {"x1": False, "sc": {"pass": True}}, [IB])
    ld = _ledger(tmp_path, [row])
    bars = _bars([(POST, 100, 101, 99, 103.0)])
    out = GR.grade_due(POST, ld, bars_for=lambda t, d: bars)
    assert out == {"due": 1, "graded": 1, "skipped": 0, "dropped": 0, "dropped_reasons": []}
    g = L.read_ledger(ld).iloc[0]
    assert g["close_post"] == 103.0 and g["pnl_per_share"] == pytest.approx(7.0 - 3.0)
    assert g["ror"] == pytest.approx(4.0 / 8.0) and g["outcome"] == "EXPIRED"


def test_option_row_without_a_close_is_left_pending(tmp_path):
    row = LR.sheet_row("X", D, {"can_price": True}, {"x1": False, "sc": {"pass": True}}, [IB])
    ld = _ledger(tmp_path, [row])
    out = GR.grade_due(POST, ld, bars_for=lambda t, d: _bars([(date(2026, 10, 15), 1, 1, 1, 1.0)]))
    assert out["graded"] == 0 and out["dropped"] == 1 and "no close" in out["dropped_reasons"][0]
    assert L.read_ledger(ld).empty and len(L.pending(ld, POST)) == 1


def test_share_row_walks_from_the_next_open_and_scores_the_target(tmp_path):
    rows = LR.disc_rows("X", D, "long", [SHARES], "none")
    ld = _ledger(tmp_path, rows)
    post = date.fromisoformat(rows[0]["post"])
    bars = _bars([(date(2026, 9, 21), 102.0, 104, 101, 103), (date(2026, 9, 22), 103, 125.0, 102, 124), (post, 124, 125, 123, 124)])
    out = GR.grade_due(post, ld, bars_for=lambda t, d: bars)
    assert out["graded"] == 1
    g = L.read_ledger(ld).iloc[0]
    # next_open fill at 102 shifts stop/target by +2: target 122 hit on 09-22 -> r = 20/10 = +2
    assert g["outcome"] == "WIN" and g["r_share"] == pytest.approx(2.0) and str(g["fill_date"])[:10] == "2026-09-21"


def test_grading_is_write_once(tmp_path):
    row = LR.sheet_row("X", D, {"can_price": True}, {"x1": False, "sc": {"pass": True}}, [IB])
    ld = _ledger(tmp_path, [row])
    bars = _bars([(POST, 100, 101, 99, 100.0)])
    GR.grade_due(POST, ld, bars_for=lambda t, d: bars)
    again = GR.grade_due(POST, ld, bars_for=lambda t, d: bars)
    assert again["due"] == 0 and len(L.read_ledger(ld)) == 1


def test_nothing_due_is_a_no_op(tmp_path):
    assert GR.grade_due(POST, str(tmp_path), bars_for=lambda t, d: _bars([]))["due"] == 0
