"""engine.calendar: the hard-coded NYSE calendar must agree with the price panel (Yahoo grid)."""
from __future__ import annotations

import os
from datetime import date

import pytest

from engine import calendar as cal
from engine.config import PRICES

pytestmark = pytest.mark.unit


def test_holidays_are_not_trading_days():
    assert not cal.is_trading_day(date(2026, 4, 3))    # Good Friday
    assert not cal.is_trading_day(date(2026, 7, 3))    # Independence Day observed
    assert not cal.is_trading_day(date(2026, 9, 7))    # Labor Day
    assert not cal.is_trading_day(date(2026, 9, 5))    # Saturday


def test_next_and_prev_session_skip_weekends_and_holidays():
    assert cal.next_session(date(2026, 7, 2)) == date(2026, 7, 6)
    assert cal.prev_session(date(2026, 7, 6)) == date(2026, 7, 2)
    assert cal.next_session(date(2026, 9, 4)) == date(2026, 9, 8)
    assert cal.next_session(date(2026, 9, 5)) == date(2026, 9, 8)   # from a Saturday
    assert cal.prev_session(date(2026, 9, 6)) == date(2026, 9, 4)   # from a Sunday
    assert cal.next_session(date(2026, 9, 4), 2) == date(2026, 9, 9)


def test_trading_days_between_counts_the_expiry_day_not_the_observation_day():
    assert cal.trading_days_between(date(2026, 7, 29), date(2026, 7, 31)) == 2
    assert cal.trading_days_between(date(2026, 7, 2), date(2026, 7, 6)) == 1
    assert cal.trading_days_between(date(2026, 7, 29), date(2026, 7, 29)) == 0


def test_trading_days_range():
    days = cal.trading_days(date(2026, 6, 29), date(2026, 7, 7))
    assert days == [date(2026, 6, 29), date(2026, 6, 30), date(2026, 7, 1), date(2026, 7, 2),
                    date(2026, 7, 6), date(2026, 7, 7)]


@pytest.mark.skipif(not os.path.exists(PRICES), reason="price panel not on disk")
def test_calendar_matches_price_panel_grid():
    import duckdb
    spy = [r[0] for r in duckdb.connect().execute(
        f"SELECT DISTINCT date FROM read_parquet('{PRICES}') WHERE ticker='SPY' ORDER BY date").fetchall()]
    ours = cal.trading_days(spy[0], spy[-1])
    assert ours == spy
