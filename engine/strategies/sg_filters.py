"""S-G entry/exit day arithmetic and the one-strike-out strangle selection (DESIGN/91 §1, §2).

F1..F4, F7, F8 are event-level and day-independent: they are reused unchanged from
`sa_filters.cheap_filters`. F5 (ATM pair availability) and F6 (spread) are reused from
`sa_filters.select_expiry` / `select_atm_pair` / `spreads_ok`, but evaluated on `daily_contract`
rows dated the entry day instead of `pre` (DESIGN/91 §1's one stated deviation from S-A's funnel).
Nothing in `sa_filters` is edited; everything here is new pure functions plus imports.
"""
from __future__ import annotations

from datetime import date
from typing import Any, Mapping

import pandas as pd

from engine import calendar as cal
from engine.strategies import sa_filters as F


def entry_day(E: date, offset: int) -> date:
    """Trading sessions strictly before the release date `E` (DESIGN/91 §1). Uniform across
    AMC/BMO timing because it is anchored on `E`, not on `pre`."""
    return cal.prev_session(E, offset)


def exit_day(event: Mapping[str, Any]) -> date:
    """`earnings_events.pre` already is "the last close before the release" for both AMC and BMO
    (DESIGN/91 §1); reused directly."""
    return F.to_date(event["pre"])


def one_strike_out(pair_strike: float, grid: F.StrikeGrid) -> tuple[float | None, float | None]:
    """The listed strike immediately above and immediately below `pair_strike` on the expiry's
    strike grid (DESIGN/91 §2, the LG alternate structure). None on either side when `pair_strike`
    is the top or bottom of the printed grid that day."""
    strikes = grid.strikes
    if pair_strike not in strikes:
        return None, None
    i = strikes.index(pair_strike)
    k_up = strikes[i + 1] if i + 1 < len(strikes) else None
    k_dn = strikes[i - 1] if i > 0 else None
    return k_up, k_dn


def leg_row(rows_in_expiry: pd.DataFrame, option_type: str, strike: float, min_size: int) -> dict | None:
    """The row for (option_type, strike) if it printed `min_size`+ contracts late, else None."""
    sub = rows_in_expiry[(rows_in_expiry["option_type"] == option_type)
                         & (rows_in_expiry["strike"].astype(float) == float(strike))
                         & (rows_in_expiry["size_late"].fillna(0) >= min_size)]
    return sub.iloc[0].to_dict() if len(sub) else None
