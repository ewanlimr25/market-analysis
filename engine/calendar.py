"""NYSE trading calendar for the engine.

`scripts/_calendar.py` derives its calendar from `data/prices.parquet` and extrapolates past
the panel edge on a 5-day week (its fail-open branch, DESIGN/60 §7). Option expiries sit past
the edge on every date, so the engine needs a real holiday calendar instead. The holiday list is
hard-coded for 2026 and 2027 and cross-checked against the price panel in
`tests/test_engine_calendar.py`.
"""
from __future__ import annotations

from datetime import date, timedelta
from functools import lru_cache

import numpy as np

NYSE_HOLIDAYS: tuple[date, ...] = (
    # 2026
    date(2026, 1, 1), date(2026, 1, 19), date(2026, 2, 16), date(2026, 4, 3), date(2026, 5, 25),
    date(2026, 6, 19), date(2026, 7, 3), date(2026, 9, 7), date(2026, 11, 26), date(2026, 12, 25),
    # 2027
    date(2027, 1, 1), date(2027, 1, 18), date(2027, 2, 15), date(2027, 3, 26), date(2027, 5, 31),
    date(2027, 6, 18), date(2027, 7, 5), date(2027, 9, 6), date(2027, 11, 25), date(2027, 12, 24),
)
EARLY_CLOSES: tuple[date, ...] = (date(2026, 7, 2), date(2026, 11, 27), date(2026, 12, 24))
CALENDAR_START = date(2025, 1, 1)
CALENDAR_END = date(2027, 12, 31)


@lru_cache(maxsize=1)
def _busday_calendar() -> np.busdaycalendar:
    return np.busdaycalendar(holidays=[np.datetime64(h) for h in NYSE_HOLIDAYS])


def is_trading_day(d: date) -> bool:
    return bool(np.is_busday(np.datetime64(d), busdaycal=_busday_calendar()))


def trading_days(start: date, end: date) -> list[date]:
    """Ascending NYSE trading days in [start, end]."""
    if end < start:
        return []
    days = np.arange(np.datetime64(start), np.datetime64(end) + np.timedelta64(1, "D"))
    mask = np.is_busday(days, busdaycal=_busday_calendar())
    return [d.astype("datetime64[D]").astype(date) for d in days[mask]]


def next_session(d: date, n: int = 1) -> date:
    """The n-th trading day strictly after d (d itself need not be a trading day)."""
    start = np.datetime64(d) + np.timedelta64(1, "D")
    out = np.busday_offset(start, n - 1, roll="forward", busdaycal=_busday_calendar())
    return out.astype("datetime64[D]").astype(date)


def prev_session(d: date, n: int = 1) -> date:
    """The n-th trading day strictly before d (d itself need not be a trading day)."""
    start = np.datetime64(d) - np.timedelta64(1, "D")
    out = np.busday_offset(start, -(n - 1), roll="backward", busdaycal=_busday_calendar())
    return out.astype("datetime64[D]").astype(date)


def trading_days_between(d0: date, d1: date) -> int:
    """Trading days in (d0, d1]: the engine's `dte` for a contract observed on d0 expiring d1."""
    if d1 <= d0:
        return 0
    return int(np.busday_count(np.datetime64(d0) + np.timedelta64(1, "D"),
                               np.datetime64(d1) + np.timedelta64(1, "D"),
                               busdaycal=_busday_calendar()))


def calendar_days_between(d0: date, d1: date) -> int:
    return (d1 - d0).days


def session_index(days: list[date]) -> dict[date, int]:
    return {d: i for i, d in enumerate(days)}


def month_of(d: date) -> str:
    return d.strftime("%Y-%m")


def parse_date(s: str | date) -> date:
    return s if isinstance(s, date) else date.fromisoformat(s)


def shift_days(d: date, n: int) -> date:
    return d + timedelta(days=n)
