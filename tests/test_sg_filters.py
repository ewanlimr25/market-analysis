"""S-G entry/exit day arithmetic and the one-strike-out strangle selection (DESIGN/91 §1, §2)."""
from __future__ import annotations

from datetime import date

import pandas as pd
import pytest

from engine.strategies import sa_filters as F
from engine.strategies import sg_filters as G

pytestmark = pytest.mark.unit


def test_entry_day_amc_counts_back_from_release_date():
    # AMC: release date E is 2026-08-06 (Thursday); day -3 and -5 count trading sessions before it.
    e = date(2026, 8, 6)
    assert G.entry_day(e, 3) == date(2026, 8, 3)
    assert G.entry_day(e, 5) == date(2026, 7, 30)


def test_entry_day_is_the_same_for_amc_and_bmo_same_release_date():
    # DESIGN/91 §1: entry_day is anchored on E, uniform across AMC/BMO timing.
    e = date(2026, 8, 6)
    assert G.entry_day(e, 3) == G.entry_day(e, 3)


def test_exit_day_is_earnings_events_pre_field():
    amc = {"pre": date(2026, 8, 6), "E": date(2026, 8, 6), "timing": "postmarket"}
    bmo = {"pre": date(2026, 8, 5), "E": date(2026, 8, 6), "timing": "premarket"}
    assert G.exit_day(amc) == date(2026, 8, 6)
    assert G.exit_day(bmo) == date(2026, 8, 5)


def test_amc_and_bmo_share_entry_day_but_differ_by_one_session_on_exit_day():
    e = date(2026, 8, 6)
    amc = {"pre": e, "E": e, "timing": "postmarket"}
    bmo = {"pre": date(2026, 8, 5), "E": e, "timing": "premarket"}
    assert G.entry_day(e, 3) == G.entry_day(e, 3)
    assert G.exit_day(amc) != G.exit_day(bmo)
    assert F.to_date(G.exit_day(amc)) == date(2026, 8, 6)
    assert F.to_date(G.exit_day(bmo)) == date(2026, 8, 5)


def _grid(strikes):
    return F.StrikeGrid(tuple(sorted(strikes)), 5.0)


def test_one_strike_out_picks_adjacent_listed_strikes():
    grid = _grid([90, 95, 100, 105, 110])
    assert G.one_strike_out(100, grid) == (105, 95)


def test_one_strike_out_none_at_grid_boundary():
    grid = _grid([90, 95, 100])
    assert G.one_strike_out(100, grid) == (None, 95)
    assert G.one_strike_out(90, grid) == (95, None)


def test_one_strike_out_none_when_strike_not_on_grid():
    grid = _grid([90, 95, 105])
    assert G.one_strike_out(100, grid) == (None, None)


def test_leg_row_requires_min_size():
    rows = pd.DataFrame([
        {"option_type": "call", "strike": 100.0, "size_late": 12},
        {"option_type": "call", "strike": 105.0, "size_late": 3},
        {"option_type": "put", "strike": 95.0, "size_late": 20},
    ])
    assert G.leg_row(rows, "call", 100.0, 10) is not None
    assert G.leg_row(rows, "call", 105.0, 10) is None
    assert G.leg_row(rows, "put", 95.0, 10)["strike"] == 95.0
    assert G.leg_row(rows, "put", 999.0, 10) is None
