"""The marked S-B layer (DESIGN/80 §3, §5.2): entry candidates from an underlying's
`daily_contract` rows on an entry session, grading at expiry from the close, and the
chronological run over the panel. Pure functions; the proxy shares `position_row`.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import date
from typing import Any, Callable, Mapping

import pandas as pd

from engine import calendar as cal
from engine import marking as M
from engine import policy as POL
from engine.mart import index_vol as IV
from engine.config import SB_PARAMS, SB_POLICY_ID, SB_SIZING, SB_STRUCTURES, SB_UNDERLYINGS, SB_VOL_INDEX, SBParams, SBSizing
from engine.strategies import sb_gate as G
from engine.strategies import sb_proxy as P
from engine.strategies import sb_structures as SB
from engine.strategies import sa_structures as ST
from engine.strategies import sa_filters as F

VARIANT_B1 = "B1"
# The exploration book (DESIGN/100 §6): one contract, whatever the equity; the sizing floor is 1.
EXPLORATION_SIZING = SBSizing(equity=0.0, max_loss_frac=SB_SIZING.max_loss_frac, max_open_per_sleeve=SB_SIZING.max_open_per_sleeve)
REASON_NO_PRINTS, REASON_NO_EXPIRY, REASON_NO_SPOT, REASON_NO_INDEX = "no_prints", "no_expiry", "no_spot", "no_index_vol"
IsSession = Callable[[date], bool]


@dataclass
class EntryResult:
    trades: list[dict] = field(default_factory=list)
    skipped: list[dict] = field(default_factory=list)


def spot_from_rows(rows: pd.DataFrame) -> float | None:
    """The underlying price on the session's last print."""
    if rows is None or rows.empty or "underlying_last" not in rows.columns:
        return None
    sub = rows.dropna(subset=["underlying_last"])
    if sub.empty:
        return None
    if "last_ts" in sub.columns and sub["last_ts"].notna().any():
        sub = sub.sort_values("last_ts", kind="mergesort")
    return float(sub["underlying_last"].iloc[-1])


def _skip(underlying: str, entry: date, structure: str, reason: str, state: G.GateState) -> dict:
    return {"ticker": underlying, "underlying": underlying, "entry": entry, "E": entry, "variant": VARIANT_B1,
            "structure": structure, "reason": reason, "gate_reason": state.reason}


def _leg_columns(legs: list[ST.Leg]) -> dict:
    out = {}
    for leg in legs:
        out[f"{leg.name}_id"] = leg.contract.option_chain_id
        out[f"{leg.name}_entry"] = leg.entry.price
        out[f"{leg.name}_entry_tier"] = leg.entry.tier
        out[f"{leg.name}_entry_spread"] = leg.entry.rel_spread
        out[f"{leg.name}_exit"] = leg.exit.price if leg.exit else None
        out[f"{leg.name}_exit_tier"] = leg.exit.tier if leg.exit else None
    return out


def _select_strikes(rows_in_expiry: pd.DataFrame, spot: float, m: float, params: SBParams) -> tuple[dict[str, float], dict[str, dict]]:
    band_abs = params.strike_band_sigma * m * spot
    strikes, picked = {}, {}
    for leg, target in SB.target_strikes(spot, m, params).items():
        row = SB.select_leg_row(rows_in_expiry, SB.LEG_TYPE[leg], target, band_abs, spot, params.leg_size_min)
        if row is not None:
            strikes[leg] = float(row["strike"])
            picked[leg] = row
    return strikes, picked


def _first_short_spread_fail(picked: Mapping[str, dict], structure: str, params: SBParams) -> str | None:
    for leg in SB.STRUCTURE_LEGS[structure]:
        if leg not in SB.SHORT_LEGS:
            continue
        spread = picked[leg].get("late_rel_spread")
        if spread is None or pd.isna(spread) or float(spread) > params.short_spread_max:
            return f"spread_{leg}"
    return None


def _trade_row(underlying: str, entry: date, expiry: date, spot: float, x_t: float, strikes: dict, legs: list[ST.Leg],
               structure: str, state: G.GateState, sizing: SBSizing) -> dict:
    base = P.position_row(underlying, structure, entry, expiry, spot, x_t, strikes, legs, sizing, 1.0)
    return POL.stamp({"ticker": underlying, "E": entry, "variant": VARIANT_B1, "pre": entry, "post": expiry, **base,
            "entry_tier_max": max(l.entry.tier for l in legs), "graded": False, "settle_close": None, "settle_source": None,
            "legs_json": json.dumps([ST.leg_record(l) for l in legs]), **_leg_columns(legs), **P._gate_fields(state, "both")},
                     SB_POLICY_ID, POL.ROLE_CHAMPION, state.reason)


def entry_candidates(underlying: str, entry: date, rows: pd.DataFrame, state: G.GateState, x_t: float | None,
                     params: SBParams, sizing: SBSizing, is_session: IsSession,
                     structures: tuple[str, ...] = SB_STRUCTURES) -> EntryResult:
    """Entry-only positions for one underlying on one entry session (no exits yet)."""
    res = EntryResult()
    if not G.is_on(state, "both"):
        res.skipped = [_skip(underlying, entry, s, state.reason, state) for s in structures]
        return res
    if x_t is None:
        res.skipped = [_skip(underlying, entry, s, REASON_NO_INDEX, state) for s in structures]
        return res
    if rows is None or rows.empty:
        res.skipped = [_skip(underlying, entry, s, REASON_NO_PRINTS, state) for s in structures]
        return res
    expiry = SB.select_expiry([F.to_date(e) for e in rows["expiry"].dropna().unique()], entry, is_session, params)
    if expiry is None:
        res.skipped = [_skip(underlying, entry, s, REASON_NO_EXPIRY, state) for s in structures]
        return res
    spot = spot_from_rows(rows)
    if spot is None:
        res.skipped = [_skip(underlying, entry, s, REASON_NO_SPOT, state) for s in structures]
        return res
    in_exp = rows[rows["expiry"].map(F.to_date) == expiry]
    m = SB.sigma_unit(x_t, (expiry - entry).days)
    strikes, picked = _select_strikes(in_exp, spot, m, params)
    for structure in structures:
        missing = [leg for leg in SB.STRUCTURE_LEGS[structure] if leg not in strikes]
        if missing:
            res.skipped.append(_skip(underlying, entry, structure, f"no_tier1_{missing[0]}", state))
            continue
        fail = _first_short_spread_fail(picked, structure, params)
        if fail:
            res.skipped.append(_skip(underlying, entry, structure, fail, state))
            continue
        sub = {leg: strikes[leg] for leg in SB.STRUCTURE_LEGS[structure]}
        if not SB.strikes_ordered(sub, spot, structure):
            res.skipped.append(_skip(underlying, entry, structure, "degenerate_strikes", state))
            continue
        marks = {leg: M.print_mark(picked[leg], M.WHEN_LATE) for leg in sub}
        if any(mk is None for mk in marks.values()):
            res.skipped.append(_skip(underlying, entry, structure, "unmarkable_entry", state))
            continue
        legs = SB.build_legs(underlying, expiry, sub, marks, None, structure)
        res.trades.append(_trade_row(underlying, entry, expiry, spot, x_t, sub, legs, structure, state, sizing))
    return res


def _forced_on(state: G.GateState) -> G.GateState:
    """The same inputs and reason string with the verdict forced ON; UNKNOWN stays UNKNOWN."""
    if not state.known:
        return state
    return G.GateState(state.date, state.asof, state.vix, state.vix3m, state.x, state.x_median, state.contango,
                       state.level_ok, True, True, state.reason)


def exploration_candidates(underlying: str, entry: date, rows: pd.DataFrame, state: G.GateState, x_t: float | None,
                           params: SBParams, is_session: IsSession, structures: tuple[str, ...] = SB_STRUCTURES) -> EntryResult:
    """The exploration book (DESIGN/100 §6): the champion's entry rules with the gate ignored, one
    contract per structure, `role = exploration`, the real gate verdict kept on the row. A gate that is
    UNKNOWN (missing CBOE data) still fails closed: that is a data failure, not a gate verdict."""
    res = entry_candidates(underlying, entry, rows, _forced_on(state), x_t, params, EXPLORATION_SIZING, is_session, structures)
    res.trades = [POL.stamp(t, SB_POLICY_ID, POL.ROLE_EXPLORATION, state.reason) for t in res.trades]
    return res


def grade_position(sig: Mapping[str, Any], settle_close: float, settle_source: str) -> dict:
    """Re-price a stored signal with tier-4 intrinsic exits at the given close."""
    records = json.loads(sig["legs_json"])
    strikes = {rec["name"]: float(rec["strike"]) for rec in records}
    exits = SB.settle_marks(strikes, sig["structure"], settle_close)
    legs = [ST.leg_from_record(rec, sig["underlying"], exits[rec["name"]]) for rec in records]
    n = int(sig["contracts"])
    priced = ST.price_legs(legs, n)
    risk = float(sig["max_loss_usd"]) * n
    credit = priced["credit_entry"]
    ratios = {"cost_over_credit": priced["cost_usd"] / (credit * M.CONTRACT_MULTIPLIER * n) if credit > 0 else float("nan")}
    return {**sig, **priced, **ratios, "ror": priced["net_usd"] / risk, "graded": True, "settle_close": settle_close,
            "settle_source": settle_source, "exit_tier_max": max(l.exit.tier for l in legs), **_leg_columns(legs)}


def run_marked(entry_rows: Mapping[date, pd.DataFrame], index_vol: pd.DataFrame, closes: Mapping[tuple[str, date], float],
               sessions: list[date], params: SBParams = SB_PARAMS, sizing: SBSizing = SB_SIZING, gate_mode: str = "both",
               is_session: IsSession = cal.is_trading_day, underlyings: tuple[str, ...] = SB_UNDERLYINGS) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Chronological marked run over the panel: entries on the last session of each week, the
    per-sleeve open cap, grading wherever the settlement close is known."""
    entries = P.entry_sessions(sessions, sessions[0], sessions[-1]) if sessions else []
    index = {d: i for i, d in enumerate(sessions)}
    index_vol = IV.on_sessions(index_vol, is_session)
    trades, skipped = [], []
    for t in entries:
        i = index[t]
        if i == 0:
            continue
        rows_all = entry_rows.get(t)
        for u in underlyings:
            x_col = SB_VOL_INDEX[u]
            state = G.gate(index_vol, t, sessions[i - 1], x_col, params)
            if gate_mode != "both":
                state = G.GateState(state.date, state.asof, state.vix, state.vix3m, state.x, state.x_median, state.contango,
                                    state.level_ok, G.is_on(state, gate_mode), state.known, state.reason)
            rows_u = rows_all[rows_all["underlying_symbol"] == u] if rows_all is not None and len(rows_all) else pd.DataFrame()
            res = entry_candidates(u, t, rows_u, state, P._x_on(index_vol, t, x_col), params, sizing, is_session)
            trades.extend(res.trades)
            skipped.extend(res.skipped)
    entered, capped = SB.cap_open_positions(trades, sizing.max_open_per_sleeve)
    skipped.extend({k: c[k] for k in ("ticker", "underlying", "entry", "E", "variant", "structure", "gate_reason")} | {"reason": "cap_open"} for c in capped)
    graded = []
    for row in entered:
        close = closes.get((row["underlying"], row["expiry"]))
        graded.append(grade_position(row, close, "prices") if close is not None else row)
    trades_df = pd.DataFrame(graded)
    if len(trades_df):
        trades_df = trades_df.sort_values(["entry", "underlying", "structure"], kind="mergesort").reset_index(drop=True)
    return trades_df, pd.DataFrame(skipped)
