"""`scripts/g1_remark.py`: the pure helpers around building fresh exit marks.

Regression coverage for a bug caught in the first real run: DuckDB's `DATE` columns round-trip
into pandas as `Timestamp`, while `trades.parquet`'s `post` column is a plain python `date`
(parquet round-trip of the original `datetime.date` values). Without normalizing, every
`window_lookup(...).get((option_chain_id, post_date))` misses silently and every leg falls
through to the tier-3 model fallback — which made the `b1` and `b2` treatments produce identical
results in the first run (both windows' "no print found" path collapsed to the same model spot).
"""
from __future__ import annotations

from datetime import date

import pandas as pd
import pytest

from scripts import g1_remark as GR

pytestmark = pytest.mark.unit


def _window_df() -> pd.DataFrame:
    # mirrors build_window_rows' output: DuckDB DATE -> pandas Timestamp, not python date
    return pd.DataFrame({
        "option_chain_id": ["XYZ260821C00100000", "XYZ260821P00100000"],
        "date": pd.to_datetime(["2026-08-14", "2026-08-14"]),
        "vwap": [2.00, 2.05], "size_win": [12, 3], "last_bid": [1.95, 2.00], "last_ask": [2.05, 2.10],
    })


def test_window_lookup_keys_match_plain_python_dates():
    win = _window_df()
    lookup = GR.window_lookup(win)
    key = ("XYZ260821C00100000", date(2026, 8, 14))
    assert key in lookup
    assert lookup[key].vwap == pytest.approx(2.00)


def test_window_lookup_distinguishes_dates_that_would_collide_as_timestamps():
    win = _window_df()
    lookup = GR.window_lookup(win)
    assert ("XYZ260821C00100000", date(2026, 8, 15)) not in lookup


def test_window_lookup_empty_frame():
    empty = pd.DataFrame(columns=["option_chain_id", "date", "vwap", "size_win", "last_bid", "last_ask"])
    assert GR.window_lookup(empty) == {}


def test_window_lookup_result_usable_with_row_from_window():
    win = _window_df()
    lookup = GR.window_lookup(win)
    row = lookup[("XYZ260821C00100000", date(2026, 8, 14))]
    shaped = GR._row_from_window(row)
    assert shaped["vwap_late"] == pytest.approx(2.00)
    assert shaped["size_late"] == 12
    assert shaped["late_last_bid"] == pytest.approx(1.95)
