"""Trading-calendar helpers, shared by the harness / lanes / gate scripts.

Single source of truth for "where does an h-day horizon actually end?".

Outcomes in `returns.parquet` are measured over N *trading* days (the Yahoo grid, see
`truthset/build_returns.py`). Any gate written in CALENDAR days is therefore short of the
real window -- ~4 days at h10, ~2 at h5 -- which is exactly the hole the 2026-07-24
calibration audit found in all five harness lanes and in the live S2/S4 lanes.

Stdlib + duckdb only.
"""
from __future__ import annotations

import os
from datetime import date as _date, timedelta as _timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
PX = os.path.join(DATA, "prices.parquet")

_days: list[_date] | None = None


def trading_days() -> list[_date]:
    """Ascending trading dates from the truth-set price panel (SPY as the calendar)."""
    global _days
    if _days is None:
        import duckdb
        _days = [r[0] for r in duckdb.connect().execute(
            f"SELECT DISTINCT date FROM read_parquet('{PX}') WHERE ticker='SPY' ORDER BY date"
        ).fetchall()]
    return _days


def panel_edge() -> _date | None:
    """Last trading date the price panel covers (None if the panel is unreadable)."""
    d = trading_days()
    return d[-1] if d else None


def hz_end(T, h: int) -> str:
    """Date `h` trading days after `T`, as an ISO string.

    If the panel does not reach that far -- always true for a LIVE date at the panel
    edge -- extrapolate on a 5-day week instead of clamping to `T`. Clamping would
    collapse a gate to `> T` and let every upcoming earnings through: a gate must fail
    CLOSED. The extrapolation rounds outward for the same reason, so the window is a
    day long rather than a day short.
    """
    t = _date.fromisoformat(T) if isinstance(T, str) else T
    fut = [d for d in trading_days() if d > t]
    if len(fut) >= h:
        return fut[h - 1].isoformat()
    return (t + _timedelta(days=round(h * 7 / 5) + 1)).isoformat()


def horizon_window(T, h: int) -> tuple[str, str]:
    """(first, last) trading day of the h-day window opening after T, ISO strings."""
    t = _date.fromisoformat(T) if isinstance(T, str) else T
    fut = [d for d in trading_days() if d > t]
    first = fut[0].isoformat() if fut else (t + _timedelta(days=1)).isoformat()
    return first, hz_end(T, h)
