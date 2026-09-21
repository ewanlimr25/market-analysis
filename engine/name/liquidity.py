"""R2 §2 of the ticker sheet: the liquidity floor, the one section that can stop the sheet.

`CAN_PRICE` requires all six floors of `findings/stock-deep-dive DESIGN/70 §2` on the sheet date:

    L1  issue_type in Common Stock / ADR / ETF and not an index   (S-C F1, extended to ETFs)
    L2  close >= price_min                                        (S-C F2)
    L3  distinct contracts printed on DATE >= contracts_min       (RESEARCH/20 §1.2)
    L4  >= hot_chain_min_contracts hot-chain contracts on >= hot_chain_min_days of the window
    L5  20-day dollar ADV >= adv_min                              (S-C F4)
    L6  the premium expiry (S-C's F7 rule, else the front expiry >= 7 DTE; B1) has an ATM pair whose two legs
        both mark at tier <= atm_tier_max with late_rel_spread <= atm_spread_max  (S-C F8/F9)

Every floor is measured whether or not an earlier one failed -- the sheet prints the numbers, and
a reader is never shown a label alone -- but `failing` names the **first** floor that failed in
L1..L6 order, and `can_price` is true only when all six pass. A floor whose input is missing fails
closed and says why in `nulls`: a null is a value here, never an exception (DESIGN/70 §1).

L6 reuses S-C's own selection (`sc_filters.select_atm_pair` / `spreads_ok`) rather than a second
copy of it; `_AtmShim` only renames the three thresholds, which `NameParams` spells differently
because the sheet's minimum leg size is the marking engine's tier-1 minimum (D26 option 1), not
S-C's 20 lots.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Any

import pandas as pd

from engine import calendar as cal
from engine import marking
from engine.config import SC_PARAMS, NAME_ISSUE_TYPES, NAME_PARAMS, NameParams
from engine.name.data import NameInputs
from engine.strategies import sc_filters
from engine.strategies.sa_filters import _num, to_date

FLOOR_ORDER = ("L1", "L2", "L3", "L4", "L5", "L6")
LATE = marking.WHEN_LATE
CHAIN_ID = "option_chain_id"


@dataclass(frozen=True)
class _AtmShim:
    """The three thresholds `sc_filters.select_atm_pair` / `spreads_ok` read, under S-C's names."""
    atm_band: float
    leg_size_min: int
    spread_max: float


def _shim(params: NameParams) -> _AtmShim:
    return _AtmShim(params.atm_band, params.atm_leg_size_min, params.atm_spread_max)


def evaluate(inputs: NameInputs, params: NameParams = NAME_PARAMS) -> dict:
    """The DESIGN/70 §2 floor for one name as the `liquidity` section of `ticker.json`.

    Returns `{can_price, failing, contracts, hot_chain_days, adv_usd, atm_spread, tier,
    atm_strike, atm_expiry, verdicts{L1..L6}, source, nulls}`. Pure: `inputs` is never mutated.
    """
    nulls: list[dict] = []
    screener = inputs.screener or {}
    if inputs.screener is None:
        nulls.append({"field": "liquidity.screener",
                      "reason": f"no screener row for {inputs.ticker} on {inputs.date.isoformat()}"})
    verdicts: dict[str, bool] = {}
    verdicts["L1"] = _l1(screener)
    verdicts["L2"] = _l2(screener, params)
    contracts, verdicts["L3"] = _l3(inputs, params, nulls)
    hot_days, verdicts["L4"] = _l4(inputs, params, nulls)
    adv, verdicts["L5"] = _l5(inputs, params, nulls)
    atm, verdicts["L6"] = _l6(inputs, params, nulls)
    failing = next((f for f in FLOOR_ORDER if not verdicts[f]), None)
    return {"can_price": failing is None, "failing": failing, "contracts": contracts,
            "hot_chain_days": hot_days, "adv_usd": adv, "atm_spread": atm["atm_spread"],
            "tier": atm["tier"], "atm_strike": atm["atm_strike"], "atm_expiry": atm["atm_expiry"],
            "verdicts": verdicts, "source": _source(inputs, params), "nulls": nulls}


# --- L1, L2: the screener row alone ---------------------------------------------------------------

def _l1(screener: dict) -> bool:
    """Common Stock / ADR / ETF and not an index; a missing row or a null issue type fails."""
    is_index = screener.get("is_index")
    return screener.get("issue_type") in NAME_ISSUE_TYPES and not (is_index is True or is_index == 1)


def _l2(screener: dict, params: NameParams) -> bool:
    close = _num(screener.get("close"))
    return close is not None and close >= params.price_min


# --- L3, L4, L5: the counts the marts answer -------------------------------------------------------

def _l3(inputs: NameInputs, params: NameParams, nulls: list[dict]) -> tuple[int | None, bool]:
    """Distinct `option_chain_id` values that printed on the sheet date."""
    rows = inputs.contracts_today
    if rows is None or rows.empty or CHAIN_ID not in rows.columns:
        nulls.append({"field": "liquidity.contracts",
                      "reason": f"no daily_contract rows for {inputs.ticker} on {inputs.date.isoformat()}"})
        return None, False
    contracts = int(rows[CHAIN_ID].nunique())
    return contracts, contracts >= params.contracts_min


def _l4(inputs: NameInputs, params: NameParams, nulls: list[dict]) -> tuple[int | None, bool]:
    """Sessions in the trailing window carrying at least `hot_chain_min_contracts` hot contracts."""
    rows = inputs.contract_sessions
    if rows is None or rows.empty or "n_hot" not in rows.columns:
        nulls.append({"field": "liquidity.hot_chain_days",
                      "reason": f"no contract sessions in the trailing {params.hot_chain_window}"})
        return None, False
    hot = pd.to_numeric(rows["n_hot"], errors="coerce").fillna(0)
    days = int((hot >= params.hot_chain_min_contracts).sum())
    return days, days >= params.hot_chain_min_days


def _l5(inputs: NameInputs, params: NameParams, nulls: list[dict]) -> tuple[float | None, bool]:
    adv = _num(inputs.adv_usd_20d)
    if adv is None:
        nulls.append({"field": "liquidity.adv_usd", "reason": "20-day dollar ADV is null"})
        return None, False
    return adv, adv >= params.adv_min


# --- L6: the ATM pair at the premium expiry (B1) -----------------------------------------------------------------

_NO_ATM = {"atm_spread": None, "tier": None, "atm_strike": None, "atm_expiry": None}


def front_expiry(rows: pd.DataFrame, d: date, min_dte_cal: int) -> date | None:
    """The first listed expiry at least `min_dte_cal` calendar days out among the day's prints."""
    if rows is None or rows.empty or "expiry" not in rows.columns:
        return None
    listed = sorted({to_date(e) for e in rows["expiry"].dropna().unique()})
    return next((e for e in listed if (e - d).days >= min_dte_cal), None)


def premium_expiry(rows: pd.DataFrame, d: date, min_dte_cal: int) -> date | None:
    """The expiry the sheet prices its premium structures at: S-C's F7 rule (a Friday-type expiry
    with calendar DTE in [21, 35] nearest `d + 28`) among the day's prints, else the front expiry
    at least `min_dte_cal` out. Build-time amendment B1 (findings/stock-deep-dive DESIGN/70 §12):
    the spec's "front expiry" made L6 fail on a weekly's spread for names S-C itself passes at the
    monthly (ENPH, 2026-09-18), so the floor is measured where the structures are priced."""
    if rows is None or rows.empty or "expiry" not in rows.columns:
        return None
    listed = {to_date(e) for e in rows["expiry"].dropna().unique()}
    sc_expiry = sc_filters.select_expiry(listed, d, cal.is_trading_day, SC_PARAMS)
    return sc_expiry or front_expiry(rows, d, min_dte_cal)


def _l6(inputs: NameInputs, params: NameParams, nulls: list[dict]) -> tuple[dict, bool]:
    """S-C F8/F9 at the sheet's own leg size, on the expiry the sheet prices (`premium_expiry`)."""
    close = _num((inputs.screener or {}).get("close"))
    rows = inputs.contracts_today
    expiry = premium_expiry(rows, inputs.date, params.slope_min_dte_cal)
    if close is None or expiry is None:
        nulls.append({"field": "liquidity.atm_spread",
                      "reason": "no close" if close is None
                                else f"no listed expiry {params.slope_min_dte_cal}+ calendar days out"})
        return dict(_NO_ATM), False
    pair = sc_filters.select_atm_pair(rows[rows["expiry"].map(to_date) == expiry], close, _shim(params))
    if pair is None:
        nulls.append({"field": "liquidity.atm_spread",
                      "reason": f"no ATM pair within {params.atm_band:.1%} of {close} at {expiry.isoformat()} "
                                f"with {params.atm_leg_size_min}+ lots on both legs"})
        return {**_NO_ATM, "atm_expiry": expiry.isoformat()}, False
    out = {"atm_spread": _clean_spread(pair.mean_spread), "tier": _pair_tier(pair, nulls, expiry),
           "atm_strike": float(pair.strike), "atm_expiry": expiry.isoformat()}
    ok = (out["tier"] is not None and out["tier"] <= params.atm_tier_max
          and sc_filters.spreads_ok(pair, _shim(params)))
    return out, ok


def _pair_tier(pair: Any, nulls: list[dict], expiry: date) -> int | None:
    """The worse of the two legs' marking tiers; None (and a reason) when a leg cannot be marked."""
    marks = [marking.print_mark(pair.call, LATE), marking.print_mark(pair.put, LATE)]
    if any(m is None for m in marks):
        nulls.append({"field": "liquidity.tier",
                      "reason": f"an ATM leg at {pair.strike} {expiry.isoformat()} has no late print to mark"})
        return None
    return int(max(m.tier for m in marks))


def _clean_spread(value: float) -> float | None:
    return _num(value)


# --- sources ---------------------------------------------------------------------------------------

def _source(inputs: NameInputs, params: NameParams) -> dict:
    day, known = inputs.date.isoformat(), inputs.sources or {}
    return {
        "issue_type": known.get("screener", f"screener {day}"),
        "close": known.get("screener", f"screener {day}"),
        "contracts": known.get("contracts_today", f"daily_contract {day}"),
        "hot_chain_days": known.get("contract_sessions",
                                    f"daily_contract {params.hot_chain_window} sessions to {day}"),
        "adv_usd": known.get("adv_usd_20d", f"prices.parquet 20 sessions to {day}"),
        "atm_spread": f"daily_contract late window {day}",
        "tier": f"engine.marking.print_mark late, daily_contract {day}",
    }
