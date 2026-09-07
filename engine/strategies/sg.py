"""S-G: pre-earnings ramp, long ATM straddle from day −3 (or −5) to the last close before the
release, as a pure function from tables to a trade list (DESIGN/91).

`evaluate_event` applies F1..F8 for one (event, entry offset): F1..F4, F7, F8 are event-level and
reused unchanged from `sa_filters.cheap_filters`; F5/F6 are reused from `sa_filters.select_expiry`
/ `select_atm_pair` / `spreads_ok` but evaluated on the entry day's `daily_contract` rows instead
of `pre`. On a pass it prices the LS (long straddle) and LG (long strangle, one strike out)
structures at `late` on the entry day and `late` on `pre` (the exit day), sizes them by premium
paid, and runs the gross ramp decomposition (`sg_decomposition`). `run` maps it over the event
table for both pre-registered entry offsets (DESIGN/91 §1: −3 and −5). No parameter here may be
tuned after this backtest is reported (DESIGN/91 §0).
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass, field
from datetime import date
from typing import Any, Mapping

import numpy as np
import pandas as pd

from engine import calendar as cal
from engine import marking as M
from engine.config import CONTRACT_MULTIPLIER, RISK_FREE_RATE, SA_PARAMS, SG_EQUITY, SGParams
from engine.strategies import sa_filters as F
from engine.strategies import sa_structures as ST
from engine.strategies import sg_decomposition as D
from engine.strategies import sg_filters as SGF
from engine.strategies import sg_structures as SGS

MCAP_MID_MAX = 10e9
REASON_NO_EXPIRY_OR_PAIR = "no_atm_pair"


@dataclass(frozen=True)
class Selection:
    expiry: date
    pair: F.AtmPair
    grid: F.StrikeGrid
    spot_entry: float


@dataclass
class EventResult:
    trades: list[dict] = field(default_factory=list)
    suppressed: list[dict] = field(default_factory=list)
    dropped: list[dict] = field(default_factory=list)


@dataclass
class RunResult:
    trades: pd.DataFrame
    suppressed: pd.DataFrame
    dropped: pd.DataFrame


def _event_keys(event: Mapping[str, Any], offset: int, entry_day: date) -> dict:
    return {"ticker": event.get("ticker"), "E": event.get("E"), "pre": event.get("pre"),
            "post": event.get("post"), "offset": offset, "entry_day": entry_day,
            "variant": f"G3_{offset}"}


def _strata(event: Mapping[str, Any], spot_entry: float | None) -> dict:
    mcap = float(event.get("marketcap") or 0)
    return {"sector": event.get("sector"), "mcap_bucket": "2-10B" if mcap < MCAP_MID_MAX else "10-50B",
            "timing": event.get("timing"), "regime_pre": event.get("regime_pre"),
            "vix_pre": event.get("vix_pre"), "month": event.get("month"), "season": event.get("season"),
            "implied": float(event["implied_move_perc"]), "spot_entry": spot_entry,
            "spot_exit": float(event["spot_pre"]), "realized_move": event.get("realized_move"),
            "gap_signed": event.get("gap_signed"), "iv30d_pre": event.get("iv30d_pre"),
            "iv30d_post": event.get("iv30d_post")}


def first_failing(flags: Mapping[str, bool | None]) -> str | None:
    for f in F.FILTER_ORDER:
        if flags.get(f) is False:
            return f
    return None


def select_legs(event: Mapping[str, Any], entry_rows: pd.DataFrame, spot_entry: float | None
                ) -> tuple[Selection | None, dict]:
    """F5/F6 at the entry day (DESIGN/91 §1): reuses `sa_filters.select_expiry` / `select_atm_pair`
    / `spreads_ok` unchanged, on `entry_rows` instead of S-A's `pre_rows`."""
    if spot_entry is None:
        return None, {"F5": False, "F6": None}
    post = F.to_date(event["post"])
    expiry = F.select_expiry(entry_rows, post)
    if expiry is None:
        return None, {"F5": False, "F6": None}
    rows = entry_rows[entry_rows["expiry"].map(F.to_date) == expiry]
    pair = F.select_atm_pair(rows, spot_entry, SA_PARAMS)
    if pair is None:
        return None, {"F5": False, "F6": None}
    grid = F.strike_grid(rows)
    return Selection(expiry, pair, grid, spot_entry), {"F5": True, "F6": F.spreads_ok(pair, SA_PARAMS)}


def _leg(name: str, contract: M.Contract, entry: M.Mark | None, exit_: M.Mark | None) -> ST.Leg | None:
    if entry is None or exit_ is None:
        return None
    return ST.Leg(name, contract, ST.LONG, entry, exit_)


def _ls_legs(event: Mapping[str, Any], sel: Selection, resolver: M.MarkResolver, exit_day: date
            ) -> tuple[list[ST.Leg] | None, str | None]:
    sym = event["ticker"]
    legs = []
    for name, row in (("call", sel.pair.call), ("put", sel.pair.put)):
        contract = ST.make_contract(sym, sel.expiry, name, sel.pair.strike)
        entry = M.print_mark(row, M.WHEN_LATE)
        exit_ = resolver.mark(contract, exit_day, M.WHEN_LATE)
        leg = _leg(name, contract, entry, exit_)
        if leg is None:
            return None, "unmarkable_entry" if entry is None else "unmarkable_exit"
        legs.append(leg)
    return legs, None


def _lg_legs(event: Mapping[str, Any], sel: Selection, rows_in_expiry: pd.DataFrame,
            resolver: M.MarkResolver, exit_day: date, sg_params: SGParams
            ) -> tuple[list[ST.Leg] | None, str | None]:
    sym = event["ticker"]
    k_up, k_dn = SGF.one_strike_out(sel.pair.strike, sel.grid)
    if k_up is None or k_dn is None:
        return None, "no_strike_out"
    call_row = SGF.leg_row(rows_in_expiry, "call", k_up, sg_params.leg_size_min)
    put_row = SGF.leg_row(rows_in_expiry, "put", k_dn, sg_params.leg_size_min)
    if call_row is None or put_row is None:
        return None, "illiquid_strangle_leg"
    legs = []
    for name, typ, k, row in (("strangle_call", "call", k_up, call_row), ("strangle_put", "put", k_dn, put_row)):
        contract = ST.make_contract(sym, sel.expiry, typ, k)
        entry = M.print_mark(row, M.WHEN_LATE)
        exit_ = resolver.mark(contract, exit_day, M.WHEN_LATE)
        leg = _leg(name, contract, entry, exit_)
        if leg is None:
            return None, "unmarkable_entry" if entry is None else "unmarkable_exit"
        legs.append(leg)
    return legs, None


def _leg_iv(leg: ST.Leg, d: date, rows_dict: Mapping[tuple[str, date], Mapping], model_inputs_fn) -> float | None:
    row = rows_dict.get((leg.contract.option_chain_id, d))
    if row is not None:
        iv = row.get("iv_vwap")
        if iv is not None and not (isinstance(iv, float) and math.isnan(iv)):
            return float(iv)
    inputs = model_inputs_fn(leg.contract, d, M.WHEN_LATE)
    return inputs.iv if inputs is not None else None


def decompose_trade(legs: list[ST.Leg], entry_day: date, exit_day: date, spot_entry: float,
                    spot_exit: float, rows_dict: Mapping, model_inputs_fn) -> D.Decomposition:
    """DESIGN/91 §4's gross ramp decomposition for one straddle/strangle."""
    entry_ivs, exit_ivs, net_delta, net_vega = [], [], 0.0, 0.0
    for leg in legs:
        iv_e = _leg_iv(leg, entry_day, rows_dict, model_inputs_fn)
        iv_x = _leg_iv(leg, exit_day, rows_dict, model_inputs_fn)
        if iv_e is not None:
            entry_ivs.append(iv_e)
            t_years = max((leg.contract.expiry - entry_day).days, 0) / 365.0
            g = D.LegGreekInputs(spot_entry, leg.contract.strike, t_years, iv_e, leg.contract.option_type)
            net_delta += leg.side * D.numeric_delta(g, RISK_FREE_RATE)
            net_vega += leg.side * D.numeric_vega(g, RISK_FREE_RATE)
        if iv_x is not None:
            exit_ivs.append(iv_x)
    iv_entry_mean = float(np.mean(entry_ivs)) if entry_ivs else None
    iv_exit_mean = float(np.mean(exit_ivs)) if exit_ivs else None
    entry_sum = sum(l.entry.price for l in legs)
    exit_sum = sum(l.exit.price for l in legs)
    return D.decompose(entry_sum, exit_sum, spot_entry, spot_exit, net_delta, net_vega,
                       iv_entry_mean, iv_exit_mean)


def _leg_record(leg: ST.Leg) -> dict:
    return {"name": leg.name, "option_chain_id": leg.contract.option_chain_id, "option_type": leg.contract.option_type,
            "strike": leg.contract.strike, "expiry": leg.contract.expiry.isoformat(),
            "entry_price": leg.entry.price, "entry_tier": leg.entry.tier, "entry_spread": leg.entry.rel_spread,
            "exit_price": leg.exit.price if leg.exit else None, "exit_tier": leg.exit.tier if leg.exit else None}


def _trade_row(event: Mapping[str, Any], sel: Selection, structure: str, legs: list[ST.Leg], offset: int,
               entry_day: date, exit_day: date, sg_params: SGParams, cost_mult: float,
               atm_spread_entry: float | None, rows_dict: Mapping, model_inputs_fn) -> dict:
    n = SGS.size_long(SGS.premium_paid_usd(legs, 1), SG_EQUITY, sg_params)
    priced = ST.price_legs(legs, n, cost_mult)
    spot_entry = sel.spot_entry
    notional = spot_entry * CONTRACT_MULTIPLIER * n
    premium_paid = SGS.premium_paid_usd(legs, n)
    decomp = decompose_trade(legs, entry_day, exit_day, spot_entry, float(event["spot_pre"]), rows_dict, model_inputs_fn)
    is_lg = structure == SGS.STRUCTURE_LG
    row = {**_event_keys(event, offset, entry_day), "structure": structure, "expiry": sel.expiry,
           "k": sel.pair.strike, "k_up": legs[0].contract.strike if is_lg else None,
           "k_dn": legs[1].contract.strike if is_lg else None,
           "contracts": n, "notional_usd": notional, "premium_paid_usd": premium_paid, **priced,
           "gross_pct": priced["gross_usd"] / notional, "cost_pct": priced["cost_usd"] / notional,
           "net_pct": priced["net_usd"] / notional,
           "gross_pct_prem": priced["gross_usd"] / premium_paid, "cost_pct_prem": priced["cost_usd"] / premium_paid,
           "net_pct_prem": priced["net_usd"] / premium_paid,
           "entry_tier_max": max(l.entry.tier for l in legs), "exit_tier_max": max(l.exit.tier for l in legs),
           "model_entry": any(l.entry.tier == 3 for l in legs), "model_exit": any(l.exit.tier == 3 for l in legs),
           "atm_spread_entry": atm_spread_entry,
           "unhedged_pnl_pct": decomp.unhedged_pnl_pct, "delta_pnl_pct": decomp.delta_pnl_pct,
           "delta_hedged_pnl_pct": decomp.delta_hedged_pnl_pct, "vega_pnl_pct": decomp.vega_pnl_pct,
           "residual_pnl_pct": decomp.residual_pnl_pct, "net_delta": decomp.net_delta, "net_vega": decomp.net_vega,
           "iv_entry_mean": decomp.iv_entry_mean, "iv_exit_mean": decomp.iv_exit_mean,
           "dte": cal.trading_days_between(entry_day, sel.expiry),
           "legs_json": json.dumps([_leg_record(l) for l in legs]),
           **_strata(event, spot_entry)}
    return row


def evaluate_event(event: Mapping[str, Any], entry_rows: pd.DataFrame, offset: int, entry_day: date,
                   exit_day: date, resolver: M.MarkResolver, prices: Mapping, sg_params: SGParams,
                   cost_mult: float, rows_dict: Mapping, model_inputs_fn) -> EventResult:
    """F1..F8 for one (event, offset); on a pass, prices LS and (if liquid) LG."""
    res = EventResult()
    spot_entry = prices.get((event["ticker"], entry_day))
    spot_entry = spot_entry[1] if spot_entry is not None else None
    flags = F.cheap_filters(event, SA_PARAMS)
    sel = None
    if all(flags[k] for k in ("F1", "F2", "F3", "F4")):
        sel, f56 = select_legs(event, entry_rows, spot_entry)
        flags = {**flags, **f56}
    else:
        flags = {**flags, "F5": None, "F6": None}
    ff = first_failing(flags)
    if ff is not None:
        res.suppressed.append({**_event_keys(event, offset, entry_day), "first_fail": ff})
        return res
    if sel is None:
        res.suppressed.append({**_event_keys(event, offset, entry_day), "first_fail": "F5"})
        return res
    ls_legs, reason = _ls_legs(event, sel, resolver, exit_day)
    if ls_legs is None:
        res.dropped.append({**_event_keys(event, offset, entry_day), "structure": SGS.STRUCTURE_LS, "reason": reason})
        return res
    atm_spread_entry = float(np.mean([ls_legs[0].entry.rel_spread, ls_legs[1].entry.rel_spread]))
    res.trades.append(_trade_row(event, sel, SGS.STRUCTURE_LS, ls_legs, offset, entry_day, exit_day,
                                 sg_params, cost_mult, atm_spread_entry, rows_dict, model_inputs_fn))
    rows_in_expiry = entry_rows[entry_rows["expiry"].map(F.to_date) == sel.expiry]
    lg_legs, reason = _lg_legs(event, sel, rows_in_expiry, resolver, exit_day, sg_params)
    if lg_legs is None:
        res.dropped.append({**_event_keys(event, offset, entry_day), "structure": SGS.STRUCTURE_LG, "reason": reason})
        return res
    res.trades.append(_trade_row(event, sel, SGS.STRUCTURE_LG, lg_legs, offset, entry_day, exit_day,
                                 sg_params, cost_mult, atm_spread_entry, rows_dict, model_inputs_fn))
    return res


def run(events: pd.DataFrame, entry_rows_by_offset: Mapping[int, pd.DataFrame], resolver: M.MarkResolver,
       prices: Mapping, model_inputs_fn, offsets: tuple[int, ...], sg_params: SGParams,
       cost_mult: float = 1.0, rows_dict: Mapping | None = None) -> RunResult:
    """Evaluate every (event, offset); returns trades / suppressed / dropped frames."""
    rows_dict = rows_dict or {}
    trades, suppressed, dropped = [], [], []
    for offset in offsets:
        entry_rows = entry_rows_by_offset[offset]
        groups = ({k: g for k, g in entry_rows.groupby(["underlying_symbol", "date"], sort=False)}
                  if len(entry_rows) else {})
        empty = entry_rows.iloc[0:0]
        for event in events.sort_values(["pre", "ticker", "E"]).to_dict("records"):
            entry_day = SGF.entry_day(F.to_date(event["E"]), offset)
            exit_day = SGF.exit_day(event)
            rows = groups.get((event["ticker"], entry_day), empty)
            r = evaluate_event(event, rows, offset, entry_day, exit_day, resolver, prices, sg_params,
                               cost_mult, rows_dict, model_inputs_fn)
            trades.extend(r.trades)
            suppressed.extend(r.suppressed)
            dropped.extend(r.dropped)
    return RunResult(pd.DataFrame(trades), pd.DataFrame(suppressed), pd.DataFrame(dropped))
