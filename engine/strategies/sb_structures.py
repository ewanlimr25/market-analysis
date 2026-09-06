"""S-B expiry rule, sigma unit, targets, strike selection, structures, max loss, sizing and the
open-position cap (DESIGN/80 §3 to §4). Legs, pricing and records reuse `sa_structures`.

Legs: p1 short put at S(1 - m), p2 long put at S(1 - 2m), c1 short call at S(1 + m), c2 long call
at S(1 + 2m), with m = X/100 * sqrt(DTE_cal / 365). PS = (p1, p2); IC = (p1, p2, c1, c2).
"""
from __future__ import annotations

import math
from datetime import date, timedelta
from typing import Any, Callable, Iterable, Mapping

import pandas as pd

from engine import marking as M
from engine.config import SBParams, SBSizing
from engine.strategies import sa_structures as ST

LEG_P1, LEG_P2, LEG_C1, LEG_C2 = "p1", "p2", "c1", "c2"
STRUCTURE_PS, STRUCTURE_IC = "PS", "IC"
STRUCTURE_LEGS = {STRUCTURE_PS: (LEG_P1, LEG_P2), STRUCTURE_IC: (LEG_P1, LEG_P2, LEG_C1, LEG_C2)}
LEG_TYPE = {LEG_P1: "put", LEG_P2: "put", LEG_C1: "call", LEG_C2: "call"}
LEG_SIDE = {LEG_P1: ST.SHORT, LEG_P2: ST.LONG, LEG_C1: ST.SHORT, LEG_C2: ST.LONG}
SHORT_LEGS = (LEG_P1, LEG_C1)
FRIDAY, THURSDAY = 4, 3
DAYS_PER_YEAR = 365.0
STRIKE_TOL = 1e-9


def sigma_unit(x_index: float, dte_cal: int) -> float:
    """m = X/100 * sqrt(DTE_cal / 365): the index-implied move to expiry as a fraction of spot."""
    return x_index / 100.0 * math.sqrt(dte_cal / DAYS_PER_YEAR)


def leg_sigmas(params: SBParams) -> dict[str, float]:
    return {LEG_P1: -params.short_sigma, LEG_P2: -params.wing_sigma,
            LEG_C1: params.short_sigma, LEG_C2: params.wing_sigma}


def target_strikes(spot: float, m: float, params: SBParams) -> dict[str, float]:
    return {leg: spot * (1.0 + s * m) for leg, s in leg_sigmas(params).items()}


def is_friday_expiry(expiry: date, is_session: Callable[[date], bool]) -> bool:
    """A Friday, or the Thursday before a Friday that is not a session (a holiday)."""
    if expiry.weekday() == FRIDAY:
        return True
    return expiry.weekday() == THURSDAY and not is_session(expiry + timedelta(days=1))


def select_expiry(candidates: Iterable[date], entry: date, is_session: Callable[[date], bool],
                  params: SBParams) -> date | None:
    """The Friday-type expiry with calendar DTE in [min, max] nearest the target; ties go earlier."""
    ok = [e for e in set(candidates)
          if params.dte_cal_min <= (e - entry).days <= params.dte_cal_max and is_friday_expiry(e, is_session)]
    if not ok:
        return None
    return min(ok, key=lambda e: (abs((e - entry).days - params.target_dte_cal), e))


def proxy_expiry(entry: date, sessions: list[date], params: SBParams) -> date | None:
    """entry + target days when that is a session, else the last session before it; None when the
    target lies beyond the session list (the settlement is not observable yet)."""
    if not sessions:
        return None
    target = entry + timedelta(days=params.target_dte_cal)
    if target > sessions[-1]:
        return None
    prior = [s for s in sessions if s <= target]
    if not prior:
        return None
    expiry = prior[-1]
    if expiry <= entry or not (params.dte_cal_min <= (expiry - entry).days <= params.dte_cal_max):
        return None
    return expiry


def round_to_step(x: float, step: float) -> float:
    return float(round(x / step) * step)


def select_leg_row(rows: pd.DataFrame, option_type: str, target: float, band_abs: float, spot: float,
                   min_size: int) -> dict | None:
    """The tier-1 strike (size_late >= min_size) nearest `target` within `band_abs`; ties go to
    the strike nearer the money."""
    if rows is None or rows.empty:
        return None
    sub = rows[(rows["option_type"] == option_type) & (rows["size_late"].fillna(0) >= min_size)]
    sub = sub[(sub["strike"].astype(float) - target).abs() <= band_abs + STRIKE_TOL]
    if sub.empty:
        return None
    records = sub.to_dict("records")
    return min(records, key=lambda r: (abs(float(r["strike"]) - target), abs(float(r["strike"]) - spot)))


def strikes_ordered(strikes: Mapping[str, float], spot: float, structure: str) -> bool:
    p1, p2 = strikes.get(LEG_P1), strikes.get(LEG_P2)
    if p1 is None or p2 is None or not (p2 < p1 < spot):
        return False
    if structure == STRUCTURE_PS:
        return True
    c1, c2 = strikes.get(LEG_C1), strikes.get(LEG_C2)
    return c1 is not None and c2 is not None and spot < c1 < c2


def width(strikes: Mapping[str, float], structure: str) -> float:
    put_width = strikes[LEG_P1] - strikes[LEG_P2]
    if structure == STRUCTURE_PS:
        return put_width
    return max(put_width, strikes[LEG_C2] - strikes[LEG_C1])


def max_loss_per_contract(strikes: Mapping[str, float], structure: str, credit_per_share: float) -> float:
    return max((width(strikes, structure) - credit_per_share) * M.CONTRACT_MULTIPLIER, ST.MIN_RISK_USD)


def size_position(max_loss_usd: float, sizing: SBSizing) -> int:
    return max(1, math.floor(sizing.max_loss_frac * sizing.equity / max_loss_usd))


def settle_marks(strikes: Mapping[str, float], structure: str, close: float) -> dict[str, M.Mark]:
    """Tier-4 intrinsic marks for every leg of the structure at the expiry close."""
    return {leg: M.intrinsic_mark(close, strikes[leg], LEG_TYPE[leg]) for leg in STRUCTURE_LEGS[structure]}


def build_legs(underlying: str, expiry: date, strikes: Mapping[str, float], entry_marks: Mapping[str, M.Mark],
               exit_marks: Mapping[str, M.Mark] | None, structure: str) -> list[ST.Leg]:
    legs = []
    for leg in STRUCTURE_LEGS[structure]:
        contract = ST.make_contract(underlying, expiry, LEG_TYPE[leg], float(strikes[leg]))
        legs.append(ST.Leg(leg, contract, LEG_SIDE[leg], entry_marks[leg], exit_marks[leg] if exit_marks else None))
    return legs


def cap_open_positions(rows: list[dict], max_open: int) -> tuple[list[dict], list[dict]]:
    """Chronological open-position cap per (underlying, structure): a position is open from its
    entry until its expiry (exclusive). Returns (entered, capped); input order is preserved."""
    ordered = sorted(rows, key=lambda r: (r["entry"], r["underlying"], r["structure"]))
    open_by_sleeve: dict[tuple[str, str], list[date]] = {}
    entered, capped = [], []
    for row in ordered:
        key = (row["underlying"], row["structure"])
        still_open = [e for e in open_by_sleeve.get(key, []) if e > row["entry"]]
        if len(still_open) >= max_open:
            capped.append({**row, "reason": "cap_open"})
            open_by_sleeve[key] = still_open
            continue
        entered.append(row)
        open_by_sleeve[key] = still_open + [row["expiry"]]
    return entered, capped
