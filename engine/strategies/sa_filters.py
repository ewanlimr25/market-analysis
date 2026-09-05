"""S-A pre-registered filters F1..F8 and the contract selection they need (DESIGN/70 §3.1).

F1..F4, F7, F8 read the event row alone (`cheap_filters`). F5 and F6 need the pre-session
`daily_contract` rows of the underlying (`select_expiry`, `select_atm_pair`, `spreads_ok`).
The strike grid helpers serve the iron-condor wings (§3.2). Nothing here may be tuned before
the Season 3 read.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import date, datetime
from typing import Any, Mapping

import pandas as pd

from engine.config import ISSUE_TYPES, SAParams

FILTER_ORDER = ("F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8")
A2_FILTER = "A2_sector"
RESOLVED_TIMINGS = ("postmarket", "premarket")
UNRESOLVED_HOW = "2-session"
GRID_TOL = 1e-6


def _num(v) -> float | None:
    if v is None:
        return None
    try:
        f = float(v)
    except (TypeError, ValueError):
        return None
    return None if math.isnan(f) else f


def to_date(v) -> date:
    """Coerce a date / datetime / pandas Timestamp / ISO string to a python date."""
    if isinstance(v, datetime):          # pandas Timestamp and datetime are both date subclasses
        return v.date()
    if isinstance(v, date):
        return v
    return pd.Timestamp(v).date()


def cheap_filters(event: Mapping[str, Any], params: SAParams) -> dict[str, bool]:
    """F1, F2, F3, F4, F7, F8 from the event row alone."""
    spot, mcap, adv, imp = (_num(event.get(k)) for k in ("spot_pre", "marketcap", "adv_usd_20d", "implied_move_perc"))
    return {
        "F1": event.get("issue_type") in ISSUE_TYPES,
        "F2": spot is not None and spot >= params.price_min,
        "F3": mcap is not None and params.mcap_min <= mcap <= params.mcap_max,
        "F4": adv is not None and adv >= params.adv_min,
        "F7": imp is not None and params.implied_min <= imp <= params.implied_max,
        "F8": event.get("timing") in RESOLVED_TIMINGS and event.get("how") != UNRESOLVED_HOW,
    }


def a2_sector_ok(event: Mapping[str, Any], params: SAParams) -> bool:
    return event.get("sector") not in params.a2_excluded_sectors


def select_expiry(rows: pd.DataFrame, post: date) -> date | None:
    """The nearest expiry strictly after `post` among the contracts that printed on `pre`."""
    if rows.empty:
        return None
    exps = sorted({to_date(e) for e in rows["expiry"].dropna().unique()})
    later = [e for e in exps if e > post]
    return later[0] if later else None


@dataclass(frozen=True)
class AtmPair:
    strike: float
    call: dict
    put: dict


def _qualifying(rows: pd.DataFrame, option_type: str, min_size: int) -> dict[float, dict]:
    sub = rows[(rows["option_type"] == option_type) & (rows["size_late"].fillna(0) >= min_size)]
    return {float(r["strike"]): r for r in sub.to_dict("records")}


def select_atm_pair(rows_in_expiry: pd.DataFrame, spot: float, params: SAParams) -> AtmPair | None:
    """F5: the strike nearest `spot` inside the ATM band whose call AND put both printed
    `leg_size_min`+ contracts in the late window. Ties go to the lower strike."""
    calls = _qualifying(rows_in_expiry, "call", params.leg_size_min)
    puts = _qualifying(rows_in_expiry, "put", params.leg_size_min)
    candidates = [k for k in calls.keys() & puts.keys() if abs(k / spot - 1) <= params.atm_band]
    if not candidates:
        return None
    k = min(candidates, key=lambda x: (abs(x - spot), x))
    return AtmPair(k, calls[k], puts[k])


def spreads_ok(pair: AtmPair, params: SAParams) -> bool:
    """F6: late relative NBBO spread on both legs <= spread_max (an unknown spread fails)."""
    spreads = [_num(pair.call.get("late_rel_spread")), _num(pair.put.get("late_rel_spread"))]
    return all(s is not None and s <= params.spread_max for s in spreads)


@dataclass(frozen=True)
class StrikeGrid:
    strikes: tuple[float, ...]
    increment: float          # 0 when it cannot be inferred (single printed strike)


def strike_grid(rows_in_expiry: pd.DataFrame) -> StrikeGrid:
    strikes = tuple(sorted({float(k) for k in rows_in_expiry["strike"].dropna().unique()}))
    diffs = [b - a for a, b in zip(strikes, strikes[1:]) if b - a > GRID_TOL]
    return StrikeGrid(strikes, min(diffs) if diffs else 0.0)


def round_to_strike(x: float, grid: StrikeGrid) -> float:
    """Nearest listed strike, allowing unprinted strikes on the inferred increment; ties go lower."""
    candidates = set(grid.strikes)
    if grid.increment > 0 and grid.strikes:
        base = grid.strikes[0]
        candidates.add(base + round((x - base) / grid.increment) * grid.increment)
    return min(candidates, key=lambda k: (abs(k - x), k))


def wing_strikes(spot: float, implied: float, grid: StrikeGrid, params: SAParams) -> tuple[float, float]:
    """IC wings at S x (1 +/- wing_mult x implied), rounded to the expiry's strike grid."""
    k_up = round_to_strike(spot * (1 + params.wing_mult * implied), grid)
    k_dn = round_to_strike(spot * (1 - params.wing_mult * implied), grid)
    return k_up, k_dn
