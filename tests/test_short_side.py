"""engine.features.short_side: the point-in-time short-interest / borrow-fee join onto a screener
spine (RESEARCH/47 §2 G4/G9)."""
from __future__ import annotations

from datetime import date

import pandas as pd
import pytest

from engine.features import short_side as SS

pytestmark = pytest.mark.unit


def _si_loader(table: dict):
    """table: {as_of_date: DataFrame(symbol, current_short_position, days_to_cover, change_percent)}"""
    def load(as_of):
        return table.get(as_of, pd.DataFrame(columns=["symbol", "current_short_position",
                                                       "days_to_cover", "change_percent"]))
    return load


def _borrow_loader(table: dict):
    """table: {date: DataFrame(symbol, fee_rate)}"""
    def load(d):
        if d not in table:
            return {"available": False, "reason": "no snapshot", "data": pd.DataFrame(columns=["symbol", "fee_rate"])}
        return {"available": True, "reason": None, "data": table[d]}
    return load


def test_join_attaches_all_four_columns_by_ticker_and_date():
    d = date(2026, 9, 4)
    spine = pd.DataFrame({"ticker": ["AAPL", "MSFT"], "date": [d, d]})
    si = _si_loader({d: pd.DataFrame({"symbol": ["AAPL"], "current_short_position": [116327753.0],
                                       "days_to_cover": [2.53], "change_percent": [-17.85]})})
    borrow = _borrow_loader({d: pd.DataFrame({"symbol": ["AAPL"], "fee_rate": [0.3648]})})
    out = SS.join_short_side(spine, load_short_interest=si, load_borrow=borrow)
    assert list(out.columns) == ["ticker", "date"] + list(SS.ATTACHED_COLUMNS) + [SS.BORROW_ASOF_COLUMN]
    aapl = out[out.ticker == "AAPL"].iloc[0]
    assert aapl.short_interest == 116327753.0
    assert aapl.days_to_cover == pytest.approx(2.53)
    assert aapl.si_change_pct == pytest.approx(-17.85)
    assert aapl.borrow_fee == pytest.approx(0.3648)


def test_join_is_nullable_when_ticker_absent_from_either_source():
    d = date(2026, 9, 4)
    spine = pd.DataFrame({"ticker": ["ZZZZ"], "date": [d]})
    si = _si_loader({d: pd.DataFrame({"symbol": ["AAPL"], "current_short_position": [1.0],
                                       "days_to_cover": [1.0], "change_percent": [1.0]})})
    borrow = _borrow_loader({})
    out = SS.join_short_side(spine, load_short_interest=si, load_borrow=borrow)
    row = out.iloc[0]
    assert pd.isna(row.short_interest) and pd.isna(row.days_to_cover)
    assert pd.isna(row.si_change_pct) and pd.isna(row.borrow_fee)


def test_join_preserves_row_count_and_order_across_multiple_dates():
    d1, d2 = date(2026, 9, 3), date(2026, 9, 4)
    spine = pd.DataFrame({"ticker": ["MSFT", "AAPL", "AAPL"], "date": [d2, d1, d2]})
    si = _si_loader({
        d1: pd.DataFrame({"symbol": ["AAPL"], "current_short_position": [10.0], "days_to_cover": [1.0], "change_percent": [1.0]}),
        d2: pd.DataFrame({"symbol": ["AAPL"], "current_short_position": [20.0], "days_to_cover": [2.0], "change_percent": [2.0]}),
    })
    borrow = _borrow_loader({})
    out = SS.join_short_side(spine, load_short_interest=si, load_borrow=borrow)
    assert len(out) == 3
    assert out.ticker.tolist() == ["MSFT", "AAPL", "AAPL"]
    assert out.date.tolist() == [d2, d1, d2]
    assert pd.isna(out.iloc[0].short_interest)                # MSFT, not in either date's table
    assert out.iloc[1].short_interest == 10.0                 # AAPL on d1
    assert out.iloc[2].short_interest == 20.0                 # AAPL on d2 -- point-in-time, not d1's row


def test_join_uses_the_row_own_date_not_a_single_shared_as_of():
    """Two rows for the same ticker on different dates must each see their own point-in-time value,
    proving the join calls the loader per date rather than once for the whole spine."""
    d1, d2 = date(2026, 8, 1), date(2026, 9, 1)
    spine = pd.DataFrame({"ticker": ["AAPL", "AAPL"], "date": [d1, d2]})
    calls = []

    def si(as_of):
        calls.append(as_of)
        val = 10.0 if as_of == d1 else 20.0
        return pd.DataFrame({"symbol": ["AAPL"], "current_short_position": [val],
                              "days_to_cover": [1.0], "change_percent": [1.0]})

    borrow = _borrow_loader({})
    out = SS.join_short_side(spine, load_short_interest=si, load_borrow=borrow)
    assert sorted(calls) == [d1, d2]
    assert out[out.date == d1].iloc[0].short_interest == 10.0
    assert out[out.date == d2].iloc[0].short_interest == 20.0


def test_join_raises_on_a_spine_missing_required_columns():
    with pytest.raises(ValueError):
        SS.join_short_side(pd.DataFrame({"ticker": ["AAPL"]}))


def test_join_empty_spine_returns_empty_frame_with_the_right_columns():
    out = SS.join_short_side(pd.DataFrame(columns=["ticker", "date"]))
    assert out.empty
    assert list(out.columns) == ["ticker", "date"] + list(SS.ATTACHED_COLUMNS) + [SS.BORROW_ASOF_COLUMN]


def _borrow_loader_asof(table: dict, max_stale_days: int = 7):
    """Mimics `borrow.load_borrow_asof`: exact day, else the latest prior snapshot inside the window."""
    def load(d):
        prior = [x for x in table if d - pd.Timedelta(days=max_stale_days).to_pytimedelta() <= x <= d]
        if not prior:
            return {"available": False, "reason": "none", "asof": None, "stale_days": None,
                    "data": pd.DataFrame(columns=["symbol", "fee_rate"])}
        asof = max(prior)
        return {"available": True, "reason": None, "asof": asof, "stale_days": (d - asof).days, "data": table[asof]}
    return load


def test_join_records_the_borrow_snapshot_date_each_row_came_from():
    spine = pd.DataFrame({"ticker": ["GME", "AMC", "XYZ"], "date": [date(2026, 9, 11)] * 3})
    borrow = {date(2026, 9, 10): pd.DataFrame({"symbol": ["GME", "AMC"], "fee_rate": [12.5, 3.0]})}
    out = SS.join_short_side(spine, _si_loader({}), _borrow_loader_asof(borrow))
    assert out["borrow_fee"].tolist()[:2] == [12.5, 3.0] and pd.isna(out["borrow_fee"].iloc[2])
    assert out[SS.BORROW_ASOF_COLUMN].tolist() == [date(2026, 9, 10), date(2026, 9, 10), None]


def test_join_with_the_exact_day_loader_keeps_borrow_null_and_asof_none_when_the_day_is_missing():
    spine = pd.DataFrame({"ticker": ["GME"], "date": [date(2026, 9, 11)]})
    borrow = {date(2026, 9, 10): pd.DataFrame({"symbol": ["GME"], "fee_rate": [12.5]})}
    out = SS.join_short_side(spine, _si_loader({}), _borrow_loader(borrow))
    assert pd.isna(out["borrow_fee"].iloc[0]) and out[SS.BORROW_ASOF_COLUMN].iloc[0] is None
