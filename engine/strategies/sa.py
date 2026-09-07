"""S-A: earnings short-vol on mid-caps, as a pure function from tables to a trade list.

`evaluate_event` applies F1..F8 (and A2's sector cut) to one event, selects the nearest expiry
after `post` and the ATM pair, marks both structures at `late` on `pre` and `early` on `post`,
sizes them, and returns trade rows, suppressed rows (first failing filter) and dropped rows
(unmarkable legs). `run` maps it over the event table. No parameter here may be tuned before the
Season 3 read (DESIGN/70 §0).
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import date
from typing import Any, Mapping

import pandas as pd

from engine import calendar as cal
from engine import policy as POL
from engine.config import SA_POLICY_ID
from engine import marking as M
from engine.config import CONTRACT_MULTIPLIER, SAParams, SizingParams
from engine.strategies import sa_filters as F
from engine.strategies import sa_structures as ST

VARIANT_A1, VARIANT_A2 = "A1", "A2"
VARIANTS = (VARIANT_A1, VARIANT_A2)
MCAP_MID_MAX = 10e9


@dataclass(frozen=True)
class Selection:
    expiry: date
    pair: F.AtmPair
    grid: F.StrikeGrid
    k_up: float
    k_dn: float


@dataclass
class EventResult:
    trades: list[dict] = field(default_factory=list)
    suppressed: list[dict] = field(default_factory=list)
    dropped: list[dict] = field(default_factory=list)
    flags: dict = field(default_factory=dict)


@dataclass
class RunResult:
    trades: pd.DataFrame
    suppressed: pd.DataFrame
    dropped: pd.DataFrame


def select_legs(event: Mapping[str, Any], pre_rows: pd.DataFrame, params: SAParams) -> tuple[Selection | None, dict]:
    """F5/F6 evaluation plus the leg selection; returns (selection or None, {F5, F6})."""
    post, spot = F.to_date(event["post"]), float(event["spot_pre"])
    expiry = F.select_expiry(pre_rows, post)
    if expiry is None:
        return None, {"F5": False, "F6": None}
    rows = pre_rows[pre_rows["expiry"].map(F.to_date) == expiry]
    pair = F.select_atm_pair(rows, spot, params)
    if pair is None:
        return None, {"F5": False, "F6": None}
    grid = F.strike_grid(rows)
    k_up, k_dn = F.wing_strikes(spot, float(event["implied_move_perc"]), grid, params)
    return Selection(expiry, pair, grid, k_up, k_dn), {"F5": True, "F6": F.spreads_ok(pair, params)}


def first_failing(flags: Mapping[str, bool | None], variant: str, a2_ok: bool) -> str | None:
    for f in F.FILTER_ORDER:
        if flags.get(f) is False:
            return f
    if variant == VARIANT_A2 and not a2_ok:
        return F.A2_FILTER
    return None


def _event_keys(event: Mapping[str, Any]) -> dict:
    return {k: event.get(k) for k in ("ticker", "E", "pre", "post")}


def _strata(event: Mapping[str, Any]) -> dict:
    mcap = float(event.get("marketcap") or 0)
    return {"sector": event.get("sector"), "mcap_bucket": "2-10B" if mcap < MCAP_MID_MAX else "10-50B",
            "timing": event.get("timing"), "how": event.get("how"), "regime_pre": event.get("regime_pre"),
            "vix_pre": event.get("vix_pre"), "month": event.get("month"), "season": event.get("season"),
            "implied": float(event["implied_move_perc"]), "spot": float(event["spot_pre"]),
            "realized_move": event.get("realized_move"), "gap_signed": event.get("gap_signed"),
            "iv30d_pre": event.get("iv30d_pre"), "iv30d_post": event.get("iv30d_post")}


def _leg(name: str, contract: M.Contract, side: int, entry: M.Mark | None, exit_: M.Mark | None,
         with_exit: bool) -> ST.Leg | None:
    if entry is None or (with_exit and exit_ is None):
        return None
    return ST.Leg(name, contract, side, entry, exit_ if with_exit else None)


def _atm_legs(event, sel: Selection, resolver: M.MarkResolver, with_exit: bool = True) -> tuple[list[ST.Leg] | None, str | None]:
    sym, post = event["ticker"], F.to_date(event["post"])
    legs = []
    for name, row in (("call", sel.pair.call), ("put", sel.pair.put)):
        contract = ST.make_contract(sym, sel.expiry, name, sel.pair.strike)
        entry = M.print_mark(row, M.WHEN_LATE)
        exit_ = resolver.mark(contract, post, M.WHEN_EARLY) if with_exit else None
        leg = _leg(name, contract, ST.SHORT, entry, exit_, with_exit)
        if leg is None:
            return None, "unmarkable_entry" if entry is None else "unmarkable_exit"
        legs.append(leg)
    return legs, None


def _wing_legs(event, sel: Selection, resolver: M.MarkResolver, with_exit: bool = True) -> tuple[list[ST.Leg] | None, str | None]:
    sym, pre, post = event["ticker"], F.to_date(event["pre"]), F.to_date(event["post"])
    if not (sel.k_up > sel.pair.strike > sel.k_dn):
        return None, "degenerate_wings"
    legs = []
    for name, typ, k in (("wing_call", "call", sel.k_up), ("wing_put", "put", sel.k_dn)):
        contract = ST.make_contract(sym, sel.expiry, typ, k)
        entry = resolver.mark(contract, pre, M.WHEN_LATE)
        exit_ = resolver.mark(contract, post, M.WHEN_EARLY) if with_exit else None
        leg = _leg(name, contract, ST.LONG, entry, exit_, with_exit)
        if leg is None:
            return None, "unmarkable_wing_entry" if entry is None else "unmarkable_wing_exit"
        legs.append(leg)
    return legs, None


def _leg_columns(legs: list[ST.Leg]) -> dict:
    out = {}
    for leg in legs:
        out[f"{leg.name}_id"] = leg.contract.option_chain_id
        out[f"{leg.name}_entry"] = leg.entry.price
        out[f"{leg.name}_entry_tier"] = leg.entry.tier
        out[f"{leg.name}_entry_spread"] = leg.entry.rel_spread
        out[f"{leg.name}_exit"] = leg.exit.price if leg.exit else None
        out[f"{leg.name}_exit_tier"] = leg.exit.tier if leg.exit else None
        out[f"{leg.name}_exit_spread"] = leg.exit.rel_spread if leg.exit else None
    return out


def _trade_row(event, sel: Selection, structure: str, legs: list[ST.Leg], n: int, risk_usd: float,
               risk_name: str, cost_mult: float) -> dict:
    priced = ST.price_legs(legs, n, cost_mult)
    graded = ST.has_exits(legs)
    spot = float(event["spot_pre"])
    notional = spot * CONTRACT_MULTIPLIER * n
    atm_credit = sum(-l.side * l.entry.price for l in legs if l.name in ("call", "put"))
    row = {**_event_keys(event), "structure": structure, "expiry": sel.expiry, "k": sel.pair.strike,
           "k_up": sel.k_up if structure == ST.STRUCTURE_IC else None,
           "k_dn": sel.k_dn if structure == ST.STRUCTURE_IC else None,
           "contracts": n, "notional_usd": notional, **priced,
           "gross_pct": priced["gross_usd"] / notional, "cost_pct": priced["cost_usd"] / notional,
           "net_pct": priced["net_usd"] / notional,
           "credit_net_pct": (priced["credit_entry"] * CONTRACT_MULTIPLIER * n - priced["entry_cost_usd"]) / notional,
           risk_name: risk_usd, "risk_usd": risk_usd * n,
           "straddle_over_implied": (atm_credit / spot) / float(event["implied_move_perc"]),
           "exit_tier_max": max(l.exit.tier for l in legs) if graded else None,
           "entry_tier_max": max(l.entry.tier for l in legs),
           "model_exit": any(l.exit.tier == 3 for l in legs) if graded else None,
           "model_entry": any(l.entry.tier == 3 for l in legs),
           "dte": cal.trading_days_between(F.to_date(event["pre"]), sel.expiry),
           "legs_json": json.dumps([ST.leg_record(l) for l in legs]),
           **_leg_columns(legs), **_strata(event)}
    return POL.stamp(row, SA_POLICY_ID, POL.ROLE_CHAMPION, POL.SA_GATE_PASS)


def _build_structures(event, sel: Selection, resolver: M.MarkResolver, sizing: SizingParams,
                      cost_mult: float, with_exit: bool = True) -> tuple[list[dict], list[dict]]:
    atm, reason = _atm_legs(event, sel, resolver, with_exit)
    if atm is None:
        return [], [{**_event_keys(event), "structure": "both", "reason": reason}]
    spot, implied = float(event["spot_pre"]), float(event["implied_move_perc"])
    credit_ss = ST.credit_per_share(atm, "entry")
    stress = ST.ss_stress_loss_usd(spot, implied, credit_ss, sizing.ss_stress_move_mult)
    rows = [_trade_row(event, sel, ST.STRUCTURE_SS, atm, ST.size_ss(stress, sizing), stress, "stress_loss_usd", cost_mult)]
    wings, reason = _wing_legs(event, sel, resolver, with_exit)
    if wings is None:
        return rows, [{**_event_keys(event), "structure": ST.STRUCTURE_IC, "reason": reason}]
    ic_legs = atm + wings
    max_loss = ST.ic_max_loss_usd(sel.pair.strike, sel.k_up, sel.k_dn, ST.credit_per_share(ic_legs, "entry"))
    rows.append(_trade_row(event, sel, ST.STRUCTURE_IC, ic_legs, ST.size_ic(max_loss, sizing), max_loss, "max_loss_usd", cost_mult))
    return rows, []


def evaluate_event(event: Mapping[str, Any], pre_rows: pd.DataFrame, resolver: M.MarkResolver,
                   params: SAParams, sizing: SizingParams, cost_mult: float = 1.0,
                   with_exit: bool = True) -> EventResult:
    """Filters, selection, marks and sizing for one event. `with_exit=False` produces the
    entry-only candidate rows `make daily` emits on the pre-print night."""
    flags = F.cheap_filters(event, params)
    sel = None
    if all(flags[f] for f in ("F1", "F2", "F3", "F4")):
        sel, f56 = select_legs(event, pre_rows, params)
        flags = {**flags, **f56}
    else:
        flags = {**flags, "F5": None, "F6": None}
    a2_ok = F.a2_sector_ok(event, params)
    res = EventResult(flags=flags)
    fails = {v: first_failing(flags, v, a2_ok) for v in VARIANTS}
    for v, ff in fails.items():
        if ff is not None:
            res.suppressed.append({**_event_keys(event), "variant": v, "first_fail": ff, **_strata(event)})
    passing = [v for v, ff in fails.items() if ff is None]
    if not passing or sel is None:
        return res
    rows, dropped = _build_structures(event, sel, resolver, sizing, cost_mult, with_exit)
    res.dropped.extend(dropped)
    res.trades.extend({**r, "variant": v} for v in passing for r in rows)
    return res


def run(events: pd.DataFrame, pre_rows: pd.DataFrame, resolver: M.MarkResolver, params: SAParams,
        sizing: SizingParams, cost_mult: float = 1.0, with_exit: bool = True) -> RunResult:
    """Evaluate every event; returns trades / suppressed / dropped frames (deterministic order)."""
    groups = {k: g for k, g in pre_rows.groupby(["underlying_symbol", "date"], sort=False)} if len(pre_rows) else {}
    empty = pre_rows.iloc[0:0]
    trades, suppressed, dropped = [], [], []
    for event in events.sort_values(["pre", "ticker", "E"]).to_dict("records"):
        rows = groups.get((event["ticker"], F.to_date(event["pre"])), empty)
        r = evaluate_event(event, rows, resolver, params, sizing, cost_mult, with_exit)
        trades.extend(r.trades)
        suppressed.extend(r.suppressed)
        dropped.extend(r.dropped)
    return RunResult(pd.DataFrame(trades), pd.DataFrame(suppressed), pd.DataFrame(dropped))
