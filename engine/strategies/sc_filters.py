"""S-C pre-registered filters F1..F10, the C2 variant, expiry and ATM selection, and the σ unit
(DESIGN/90 §2 and §3; R1 of §10). Pure functions over a screener row and the underlying's
`daily_contract` rows on the entry session; no I/O. Nothing here may be tuned before the read.

Order of evaluation, and what each needs:

    F1 F2 F3 F4 F6      the screener row alone                      `screener_filters`
    F7                  the contracts that printed on `t`            `select_expiry`
    F5                  F7's expiry and `next_earnings_date`         `earnings_ok` (null fails closed)
    F8 F9               the contracts in that expiry                 `select_atm_pair`, `spreads_ok`
    F10                 every name that passed F1..F9                `select_top` (10 lowest mean ATM spread)
    C2                  F10 with `sector != Technology`              `c2_ok`

`evaluate_name` runs F1..F9 for one name and reports every verdict plus the first failing filter,
so the funnel table (§10 acceptance c) is a count over its output.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import date
from typing import Any, Callable, Iterable, Mapping

import pandas as pd

from engine.config import ISSUE_TYPES, SC_PARAMS, SCParams
from engine.strategies.sa_filters import _num, to_date
from engine.strategies.sb_structures import DAYS_PER_YEAR, is_friday_expiry

FILTER_ORDER = ("F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9")
SCREENER_FILTERS = ("F1", "F2", "F3", "F4", "F6")
F10 = "F10"
C2_FILTER = "C2_sector"
VARIANT_C1, VARIANT_C2 = "C1", "C2"
CALL, PUT = "call", "put"


# ---- F1 F2 F3 F4 F6 ------------------------------------------------------------------------------

def screener_filters(row: Mapping[str, Any], params: SCParams = SC_PARAMS) -> dict[str, bool]:
    """The five filters the screener row answers alone. A missing number fails."""
    close, mcap, adv, iv = (_num(row.get(k)) for k in ("close", "marketcap", "adv_usd_20d", "iv30d"))
    is_index = row.get("is_index")
    return {
        "F1": row.get("issue_type") in ISSUE_TYPES and not (is_index is True or is_index == 1),
        "F2": close is not None and close >= params.price_min,
        "F3": mcap is not None and params.mcap_min <= mcap <= params.mcap_max,
        "F4": adv is not None and adv >= params.adv_min,
        "F6": iv is not None and params.iv30d_min <= iv <= params.iv30d_max,
    }


# ---- F7 ------------------------------------------------------------------------------------------

def select_expiry(printed_expiries: Iterable[date], entry: date, is_session: Callable[[date], bool],
                  params: SCParams = SC_PARAMS) -> date | None:
    """F7: among the expiries that printed on `entry`, the Friday-type one (Friday, or the Thursday
    before a holiday Friday) with calendar DTE in [dte_cal_min, dte_cal_max] nearest `entry +
    target_dte_cal`; ties go earlier. None when nothing qualifies."""
    ok = [e for e in {to_date(x) for x in printed_expiries if x is not None}
          if params.dte_cal_min <= (e - entry).days <= params.dte_cal_max and is_friday_expiry(e, is_session)]
    if not ok:
        return None
    return min(ok, key=lambda e: (abs((e - entry).days - params.target_dte_cal), e))


# ---- F5 ------------------------------------------------------------------------------------------

def earnings_ok(next_earnings_date: Any, expiry: date) -> bool:
    """F5: the next earnings date is known and strictly after the expiry session. A null date, an
    unparseable date, or a print on or before expiry fails (closed)."""
    if next_earnings_date is None or (isinstance(next_earnings_date, float) and math.isnan(next_earnings_date)):
        return False
    try:
        d = to_date(next_earnings_date)
    except (TypeError, ValueError):
        return False
    if pd.isna(d):
        return False
    return d > expiry


# ---- F8 F9 ---------------------------------------------------------------------------------------

@dataclass(frozen=True)
class AtmPair:
    strike: float
    call: dict
    put: dict

    @property
    def mean_spread(self) -> float:
        """Mean late relative spread of the two legs; NaN when either is unknown."""
        spreads = [_num(self.call.get("late_rel_spread")), _num(self.put.get("late_rel_spread"))]
        return float("nan") if any(s is None for s in spreads) else sum(spreads) / 2.0


def _qualifying(rows: pd.DataFrame, option_type: str, min_size: int) -> dict[float, dict]:
    sub = rows[(rows["option_type"] == option_type) & (rows["size_late"].fillna(0) >= min_size)]
    return {float(r["strike"]): r for r in sub.to_dict("records")}


def select_atm_pair(rows_in_expiry: pd.DataFrame, close: float, params: SCParams = SC_PARAMS) -> AtmPair | None:
    """F8: the strike nearest `close` with |K/S − 1| <= atm_band whose call AND put each printed
    leg_size_min+ contracts in the late window. Ties go to the lower strike."""
    if rows_in_expiry is None or rows_in_expiry.empty or not close or close <= 0:
        return None
    calls = _qualifying(rows_in_expiry, CALL, params.leg_size_min)
    puts = _qualifying(rows_in_expiry, PUT, params.leg_size_min)
    candidates = [k for k in calls.keys() & puts.keys() if abs(k / close - 1) <= params.atm_band]
    if not candidates:
        return None
    k = min(candidates, key=lambda x: (abs(x - close), x))
    return AtmPair(k, calls[k], puts[k])


def spreads_ok(pair: AtmPair, params: SCParams = SC_PARAMS) -> bool:
    """F9: late relative NBBO spread <= spread_max on both ATM legs; an unknown spread fails."""
    spreads = [_num(pair.call.get("late_rel_spread")), _num(pair.put.get("late_rel_spread"))]
    return all(s is not None and s <= params.spread_max for s in spreads)


# ---- C2, σ unit, wings ---------------------------------------------------------------------------

def c2_ok(sector: Any, params: SCParams = SC_PARAMS) -> bool:
    return sector not in params.c2_excluded_sectors


def sigma_hold(close: float, iv30d: float, dte_cal: int) -> float:
    """§3: σ_hold = close × iv30d × sqrt(DTE_cal / 365), in dollars of underlying."""
    return close * iv30d * math.sqrt(dte_cal / DAYS_PER_YEAR)


def wing_targets(close: float, sigma: float, params: SCParams = SC_PARAMS) -> tuple[float, float]:
    """§3 IB wings before rounding to the expiry's strike grid: (S + 2σ, S − 2σ)."""
    return close + params.wing_sigma * sigma, close - params.wing_sigma * sigma


# ---- one name end to end -------------------------------------------------------------------------

def evaluate_name(row: Mapping[str, Any], contract_rows: pd.DataFrame, entry: date,
                  is_session: Callable[[date], bool], params: SCParams = SC_PARAMS) -> dict:
    """F1..F9 for one name on `entry`. Returns every verdict (a filter after the first failure is
    None: not evaluated), the chosen expiry / ATM pair when reached, `mean_spread` for F10, the
    C2 flag, and `reason` = the first failing filter or None."""
    out: dict[str, Any] = {"ticker": row.get("ticker"), "entry": entry, "sector": row.get("sector"),
                           **{f: None for f in FILTER_ORDER}, "expiry": None, "dte_cal": None,
                           "pair": None, "mean_spread": float("nan"), "sigma_hold": None,
                           "c2": c2_ok(row.get("sector"), params), "reason": None}
    out.update(screener_filters(row, params))
    for f in ("F1", "F2", "F3", "F4"):
        if not out[f]:
            return _fail(out, f)
    rows = contract_rows if contract_rows is not None else pd.DataFrame()
    expiry = select_expiry(rows["expiry"].dropna().unique() if len(rows) else [], entry, is_session, params)
    out["F7"] = expiry is not None
    if expiry is None:
        return _fail(out, "F7")
    out["expiry"], out["dte_cal"] = expiry, (expiry - entry).days
    out["F5"] = earnings_ok(row.get("next_earnings_date"), expiry)
    if not out["F5"]:
        return _fail(out, "F5")
    if not out["F6"]:
        return _fail(out, "F6")
    close = _num(row.get("close"))
    in_expiry = rows[rows["expiry"].map(to_date) == expiry]
    pair = select_atm_pair(in_expiry, close, params)
    out["F8"] = pair is not None
    if pair is None:
        return _fail(out, "F8")
    out["pair"], out["mean_spread"] = pair, pair.mean_spread
    out["F9"] = spreads_ok(pair, params)
    if not out["F9"]:
        return _fail(out, "F9")
    out["sigma_hold"] = sigma_hold(close, _num(row.get("iv30d")), out["dte_cal"])
    return out


def _fail(out: dict, f: str) -> dict:
    return {**out, "reason": f}


# ---- F10 -----------------------------------------------------------------------------------------

def passed_all(ev: Mapping[str, Any]) -> bool:
    return ev.get("reason") is None and all(ev.get(f) for f in FILTER_ORDER)


def select_top(evaluations: Iterable[Mapping[str, Any]], variant: str = VARIANT_C1,
               params: SCParams = SC_PARAMS) -> list[dict]:
    """F10: among the names that passed F1..F9 (and C2 for the C2 variant), the `select_n` with the
    lowest mean ATM late spread; ties by ticker so the selection is deterministic."""
    if variant not in (VARIANT_C1, VARIANT_C2):
        raise ValueError(f"unknown S-C variant {variant!r}")
    pool = [dict(e) for e in evaluations if passed_all(e) and (variant == VARIANT_C1 or e.get("c2"))]
    pool.sort(key=lambda e: (e["mean_spread"], str(e.get("ticker"))))
    return [{**e, "variant": variant, "rank": i + 1} for i, e in enumerate(pool[:params.select_n])]


def funnel_counts(evaluations: Iterable[Mapping[str, Any]], params: SCParams = SC_PARAMS) -> dict[str, int]:
    """Names surviving each filter cumulatively, in evaluation order, then F10 per variant."""
    evs = list(evaluations)
    order = ("F1", "F2", "F3", "F4", "F7", "F5", "F6", "F8", "F9")
    counts = {"names": len(evs)}
    alive = evs
    for f in order:
        alive = [e for e in alive if e.get(f)]
        counts[f] = len(alive)
    counts["C1"] = len(select_top(evs, VARIANT_C1, params))
    counts["C2"] = len(select_top(evs, VARIANT_C2, params))
    return counts
