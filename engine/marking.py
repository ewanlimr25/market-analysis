"""The marking engine: `mark(contract, date, when) -> Mark` with the four-tier fallback of
DESIGN/70 §2, plus the per-touch cost rule.

| tier | condition                                   | mark                             | source        |
| 1    | daily_contract row, size_<when> >= 5        | vwap_<when>, window spread       | print_vwap    |
| 2    | row exists, window thin (< 5)               | NBBO mid of last print in window | print_nbbo    |
| 3    | no print that day                           | Black-Scholes, spread floored 5% | model         |
| 4    | date == expiry and when == close            | intrinsic vs underlying close    | intrinsic     |

Costs at every leg touch: half the tier's relative spread x mark (a marketable order crosses to
the NBBO) plus $0.65 per contract, multiplier 100. No fills inside the spread.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import date
from typing import Any, Callable, Mapping

from engine import bs
from engine.config import (COMMISSION_PER_CONTRACT, CONTRACT_MULTIPLIER, MODEL_SPREAD_FLOOR,
                           RISK_FREE_RATE, TIER1_MIN_SIZE)

WHEN_LATE, WHEN_EARLY, WHEN_CLOSE = "late", "early", "close"
SOURCE_PRINT_VWAP, SOURCE_PRINT_NBBO, SOURCE_MODEL, SOURCE_INTRINSIC = "print_vwap", "print_nbbo", "model", "intrinsic"
DAYS_PER_YEAR = 365.0
MODEL_IV_RATIO_MIN, MODEL_IV_RATIO_MAX = 0.5, 3.0


@dataclass(frozen=True)
class Mark:
    price: float
    rel_spread: float      # (ask - bid) / mid; NaN when no valid NBBO was available
    tier: int
    source: str


@dataclass(frozen=True)
class Contract:
    option_chain_id: str
    underlying: str
    option_type: str
    strike: float
    expiry: date


@dataclass(frozen=True)
class ModelInputs:
    """What tier 3 needs: the underlying's price for the window, the IV to use, the name's spread."""
    spot: float | None
    iv: float | None
    rel_spread: float | None


def _num(v) -> float | None:
    if v is None:
        return None
    try:
        f = float(v)
    except (TypeError, ValueError):
        return None
    return None if math.isnan(f) else f


def rel_spread_from_nbbo(bid, ask) -> float:
    b, a = _num(bid), _num(ask)
    if b is None or a is None or b <= 0 or a < b:
        return float("nan")
    return (a - b) / ((a + b) / 2)


def _window_fields(when: str) -> tuple[str, str, str, str, str]:
    if when == WHEN_LATE:
        return "vwap_late", "size_late", "late_rel_spread", "late_last_bid", "late_last_ask"
    if when == WHEN_EARLY:
        return "vwap_early", "size_early", "early_rel_spread", "early_last_bid", "early_last_ask"
    raise ValueError(f"when must be late/early/close, got {when!r}")


def _first_spread(*candidates: float) -> float:
    for c in candidates:
        if c is not None and not math.isnan(c):
            return c
    return float("nan")


def _close_mark(row: Mapping[str, Any], tier1_min_size: int) -> Mark | None:
    last = _num(row.get("last_price"))
    if last is None:
        return None
    spread = rel_spread_from_nbbo(row.get("last_nbbo_bid"), row.get("last_nbbo_ask"))
    n = _num(row.get("n_prints")) or 0
    tier = 1 if n >= tier1_min_size else 2
    return Mark(last, spread, tier, SOURCE_PRINT_VWAP if tier == 1 else SOURCE_PRINT_NBBO)


def print_mark(row: Mapping[str, Any], when: str, tier1_min_size: int = TIER1_MIN_SIZE) -> Mark | None:
    """Tiers 1 and 2 from a `daily_contract` row. None when the window has no prints."""
    if when == WHEN_CLOSE:
        return _close_mark(row, tier1_min_size)
    vwap_col, size_col, spread_col, bid_col, ask_col = _window_fields(when)
    vwap, size = _num(row.get(vwap_col)), _num(row.get(size_col)) or 0.0
    if vwap is None or size <= 0:
        return None
    last_spread = rel_spread_from_nbbo(row.get(bid_col), row.get(ask_col))
    session_spread = rel_spread_from_nbbo(row.get("last_nbbo_bid"), row.get("last_nbbo_ask"))
    if size >= tier1_min_size:
        spread = _first_spread(_num(row.get(spread_col)), last_spread, session_spread)
        return Mark(vwap, spread, 1, SOURCE_PRINT_VWAP)
    bid, ask = _num(row.get(bid_col)), _num(row.get(ask_col))
    if not math.isnan(last_spread):
        return Mark((bid + ask) / 2, last_spread, 2, SOURCE_PRINT_NBBO)
    return Mark(vwap, _first_spread(_num(row.get(spread_col)), session_spread), 2, SOURCE_PRINT_NBBO)


def model_iv(iv30d_today, iv_vwap_last, iv30d_last) -> float | None:
    """Tier-3 IV: today's screener iv30d, scaled by the contract's last (iv_vwap / iv30d) ratio
    when a print exists within the lookback, so the smile/term shape survives the crush."""
    today = _num(iv30d_today)
    if today is None or today <= 0:
        return None
    last_c, last_n = _num(iv_vwap_last), _num(iv30d_last)
    if last_c is None or last_n is None or last_c <= 0 or last_n <= 0:
        return today
    ratio = min(max(last_c / last_n, MODEL_IV_RATIO_MIN), MODEL_IV_RATIO_MAX)
    return today * ratio


def model_mark(spot, strike, dte_cal: int, iv, option_type: str, rel_spread,
               r: float = RISK_FREE_RATE) -> Mark | None:
    """Tier 3: Black-Scholes from the underlying, strike, calendar DTE and IV; spread floored."""
    s, k, v = _num(spot), _num(strike), _num(iv)
    if s is None or k is None or v is None or s <= 0 or k <= 0 or v <= 0:
        return None
    price = bs.price(s, k, max(dte_cal, 0) / DAYS_PER_YEAR, r, v, option_type)
    spread = _num(rel_spread)
    spread = MODEL_SPREAD_FLOOR if spread is None else max(spread, MODEL_SPREAD_FLOOR)
    return Mark(float(price), spread, 3, SOURCE_MODEL)


def intrinsic_mark(spot, strike, option_type: str) -> Mark | None:
    """Tier 4: intrinsic against the underlying close on expiry; spread 0."""
    s, k = _num(spot), _num(strike)
    if s is None or k is None:
        return None
    sign = 1.0 if option_type == "call" else -1.0
    return Mark(max(sign * (s - k), 0.0), 0.0, 4, SOURCE_INTRINSIC)


def leg_cost(mark: Mark, n_contracts: int, cost_mult: float = 1.0) -> float:
    """Dollars charged at one touch: half-spread crossing on n contracts plus commission."""
    spread = mark.rel_spread if not math.isnan(mark.rel_spread) else MODEL_SPREAD_FLOOR
    half_spread_dollars = 0.5 * spread * mark.price * CONTRACT_MULTIPLIER
    return cost_mult * (half_spread_dollars + COMMISSION_PER_CONTRACT) * n_contracts


ModelInputsFn = Callable[[Contract, date, str], ModelInputs | None]


class MarkResolver:
    """Falls through the tiers for (contract, date, when).

    `rows` maps (option_chain_id, date) to a daily_contract row (tiers 1-2); `model_inputs`
    supplies spot / iv / spread for tiers 3-4 and may return None when nothing is known.
    """

    def __init__(self, rows: Mapping[tuple[str, date], Mapping[str, Any]], model_inputs: ModelInputsFn,
                 tier1_min_size: int = TIER1_MIN_SIZE):
        self._rows = rows
        self._model_inputs = model_inputs
        self._tier1_min_size = tier1_min_size

    def mark(self, contract: Contract, d: date, when: str) -> Mark | None:
        row = self._rows.get((contract.option_chain_id, d))
        if row is not None:
            m = print_mark(row, when, self._tier1_min_size)
            if m is not None:
                return m
        inputs = self._model_inputs(contract, d, when)
        if inputs is None:
            return None
        if when == WHEN_CLOSE and d == contract.expiry:
            return intrinsic_mark(inputs.spot, contract.strike, contract.option_type)
        return model_mark(inputs.spot, contract.strike, (contract.expiry - d).days, inputs.iv,
                          contract.option_type, inputs.rel_spread)
