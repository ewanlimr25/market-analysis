"""S-C structures, pricing, max and stress loss, sizing and caps (DESIGN/90 §3, §4; R2 of §10).
Pure functions over one `sc_filters.evaluate_name` result, the name's `daily_contract` rows in the
chosen expiry, and a `MarkResolver` for the wings. Legs, contracts and records reuse `sa_structures`.

SS: sell the F8 call and put at `late` on the entry session (tier 1 by F8's own size clause).
IB: SS plus a long call at `round_to_strike(S + 2 σ_hold)` and a long put at `round_to_strike(S − 2 σ_hold)`,
marked through the resolver (a wing may mark at tier 2; a tier-3 wing carries the 5% spread floor).
Costs: half of each leg's spread plus commission at entry; nothing at expiry (§3). Settlement is
tier-4 intrinsic at the expiry close; where the close comes from is R3's job (`settle_source`).
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass, field
from datetime import date
from typing import Any, Iterable, Mapping

import pandas as pd

from engine import marking as M
from engine.config import SC_PARAMS, SC_SIZING, SCParams, SCSizing
from engine.strategies import sa_filters as SAF
from engine.strategies import sa_structures as ST
from engine.strategies import sc_filters as F

STRUCTURE_SS, STRUCTURE_IB = "SS", "IB"
STRUCTURES = (STRUCTURE_SS, STRUCTURE_IB)
ATM_LEGS = (("call", "call"), ("put", "put"))
WING_LEGS = (("wing_call", "call"), ("wing_put", "put"))
REASON_UNMARKABLE_ATM = "unmarkable_entry"
REASON_UNMARKABLE_WING = "unmarkable_wing_entry"
REASON_DEGENERATE = "degenerate_wings"
CAP_NEW_WEEK, CAP_OPEN, CAP_SECTOR, CAP_BUDGET = "cap_new_week", "cap_open", "cap_sector", "cap_budget"


@dataclass(frozen=True)
class BuildResult:
    structures: dict[str, dict] = field(default_factory=dict)     # structure -> row
    dropped: list[dict] = field(default_factory=list)


# ---- geometry ------------------------------------------------------------------------------------

def strike_grid(rows_in_expiry: pd.DataFrame) -> SAF.StrikeGrid:
    return SAF.strike_grid(rows_in_expiry)


def wing_strikes(close: float, sigma: float, grid: SAF.StrikeGrid, params: SCParams = SC_PARAMS) -> tuple[float, float]:
    """§3 IB wings: S ± wing_sigma × σ_hold, rounded to the expiry's grid (unprinted strikes allowed)."""
    up, dn = F.wing_targets(close, sigma, params)
    return SAF.round_to_strike(up, grid), SAF.round_to_strike(dn, grid)


# ---- risk and size -------------------------------------------------------------------------------

def ss_stress_loss_usd(close: float, k: float, sigma: float, credit: float, params: SCParams = SC_PARAMS) -> float:
    """§4: per-contract loss at expiry after a stress_sigma × σ_hold move, the worse side."""
    move = params.stress_sigma * sigma
    intrinsic = max(abs(close + move - k), abs(close - move - k))
    return max((intrinsic - credit) * M.CONTRACT_MULTIPLIER, ST.MIN_RISK_USD)


def ib_max_loss_usd(k: float, k_up: float, k_dn: float, credit: float) -> float:
    return ST.ic_max_loss_usd(k, k_up, k_dn, credit)


def size(structure: str, risk_per_contract: float, sizing: SCSizing = SC_SIZING) -> int:
    """§4: IB n = floor(0.005 E / max loss), SS n = floor(0.010 E / stress loss); min 1."""
    frac = sizing.ib_max_loss_frac if structure == STRUCTURE_IB else sizing.ss_stress_frac
    return max(1, math.floor(frac * sizing.equity / risk_per_contract))


# ---- legs ----------------------------------------------------------------------------------------

def _atm_legs(ticker: str, expiry: date, pair: F.AtmPair) -> list[ST.Leg] | None:
    legs = []
    for name, typ in ATM_LEGS:
        mark = M.print_mark(getattr(pair, name), M.WHEN_LATE)
        if mark is None:
            return None
        legs.append(ST.Leg(name, ST.make_contract(ticker, expiry, typ, pair.strike), ST.SHORT, mark, None))
    return legs


def _wing_legs(ticker: str, expiry: date, entry: date, strikes: Mapping[str, float], resolver) -> list[ST.Leg] | None:
    legs = []
    for name, typ in WING_LEGS:
        contract = ST.make_contract(ticker, expiry, typ, strikes[name])
        mark = resolver.mark(contract, entry, M.WHEN_LATE)
        if mark is None:
            return None
        legs.append(ST.Leg(name, contract, ST.LONG, mark, None))
    return legs


def entry_cost_usd(legs: list[ST.Leg], n: int) -> float:
    return sum(M.leg_cost(leg.entry, n) for leg in legs)


def _row(ev: Mapping[str, Any], structure: str, legs: list[ST.Leg], risk_name: str, risk: float,
         sizing: SCSizing, wings: tuple[float, float] | None) -> dict:
    n = size(structure, risk, sizing)
    return {"ticker": ev["ticker"], "entry": ev["entry"], "expiry": ev["expiry"], "dte_cal": ev["dte_cal"],
            "sector": ev.get("sector"), "structure": structure, "close": float(ev["close"]),
            "sigma_hold": float(ev["sigma_hold"]), "mean_spread": ev.get("mean_spread"), "k": ev["pair"].strike,
            "k_up": wings[0] if wings else None, "k_dn": wings[1] if wings else None, "contracts": n,
            "credit_entry": ST.credit_per_share(legs, "entry"), "entry_cost_usd": entry_cost_usd(legs, n),
            risk_name: risk, "risk_usd": risk * n,
            "entry_tier_max": max(l.entry.tier for l in legs), "model_entry": any(l.entry.tier == 3 for l in legs),
            "legs_json": json.dumps([ST.leg_record(l) for l in legs])}


def build(ev: Mapping[str, Any], rows_in_expiry: pd.DataFrame, resolver, sizing: SCSizing = SC_SIZING,
          params: SCParams = SC_PARAMS) -> BuildResult:
    """SS and IB for one name that passed F1..F9. `ev` is `evaluate_name`'s output plus `close`."""
    if ev.get("reason") is not None or ev.get("pair") is None:
        raise ValueError(f"{ev.get('ticker')}: S-C structures need a name that passed F1..F9 (reason {ev.get('reason')!r})")
    keys = {"ticker": ev["ticker"], "entry": ev["entry"]}
    atm = _atm_legs(ev["ticker"], ev["expiry"], ev["pair"])
    if atm is None:
        return BuildResult({}, [{**keys, "structure": "both", "reason": REASON_UNMARKABLE_ATM}])
    close, k, sigma = float(ev["close"]), ev["pair"].strike, float(ev["sigma_hold"])
    credit = ST.credit_per_share(atm, "entry")
    out = {STRUCTURE_SS: _row(ev, STRUCTURE_SS, atm, "stress_loss_usd",
                              ss_stress_loss_usd(close, k, sigma, credit, params), sizing, None)}
    k_up, k_dn = wing_strikes(close, sigma, strike_grid(rows_in_expiry), params)
    if not (k_up > k > k_dn):
        return BuildResult(out, [{**keys, "structure": STRUCTURE_IB, "reason": REASON_DEGENERATE}])
    wings = _wing_legs(ev["ticker"], ev["expiry"], ev["entry"], {"wing_call": k_up, "wing_put": k_dn}, resolver)
    if wings is None:
        return BuildResult(out, [{**keys, "structure": STRUCTURE_IB, "reason": REASON_UNMARKABLE_WING}])
    legs = atm + wings
    max_loss = ib_max_loss_usd(k, k_up, k_dn, ST.credit_per_share(legs, "entry"))
    out[STRUCTURE_IB] = _row(ev, STRUCTURE_IB, legs, "max_loss_usd", max_loss, sizing, (k_up, k_dn))
    return BuildResult(out, [])


# ---- settlement ----------------------------------------------------------------------------------

def settle(row: Mapping[str, Any], close: float) -> dict:
    """Tier-4 intrinsic exits at the expiry close; the exit costs nothing (§3)."""
    n = int(row["contracts"])
    legs = [ST.leg_from_record(rec, row["ticker"], M.intrinsic_mark(close, rec["strike"], rec["option_type"]))
            for rec in json.loads(row["legs_json"])]
    credit, debit = ST.credit_per_share(legs, "entry"), ST.credit_per_share(legs, "exit")
    gross = (credit - debit) * M.CONTRACT_MULTIPLIER * n
    entry_cost = entry_cost_usd(legs, n)
    return {"credit_entry": credit, "debit_exit": debit, "gross_usd": gross, "entry_cost_usd": entry_cost,
            "exit_cost_usd": 0.0, "cost_usd": entry_cost, "net_usd": gross - entry_cost,
            "exit_tier_max": max(l.exit.tier for l in legs)}


# ---- caps (§4) -----------------------------------------------------------------------------------

def book_budget_usd(structure: str, sizing: SCSizing = SC_SIZING) -> float:
    """§4's "40% of the book's risk budget", read as S-A reads its night budget (`portfolio.py`):
    book_budget_frac × max_open_per_variant × the per-trade risk fraction × E."""
    per_trade = sizing.ib_max_loss_frac if structure == STRUCTURE_IB else sizing.ss_stress_frac
    return sizing.book_budget_frac * sizing.max_open_per_variant * per_trade * sizing.equity


def _cap_reason(c: Mapping[str, Any], taken: list[dict], open_: list[dict], sizing: SCSizing, sb_open: bool) -> str | None:
    book = open_ + taken
    if len(taken) >= sizing.max_new_per_week:
        return CAP_NEW_WEEK
    if len(book) >= sizing.max_open_per_variant:
        return CAP_OPEN
    if sum(1 for r in book if r.get("sector") == c.get("sector")) >= sizing.max_open_per_sector:
        return CAP_SECTOR
    if sb_open and sum(float(r["risk_usd"]) for r in book) + float(c["risk_usd"]) > book_budget_usd(c["structure"], sizing):
        return CAP_BUDGET
    return None


def apply_caps(candidates: Iterable[Mapping[str, Any]], open_positions: Iterable[Mapping[str, Any]],
               sizing: SCSizing = SC_SIZING, *, sb_open: bool) -> list[dict]:
    """§4 caps for one entry week, per (variant, structure) sleeve, in F10 rank order. `open_positions`
    are the sleeve's rows still open on the entry session. Returns new rows with `cap_pass` and
    `cap_reason`; the input order is not assumed."""
    open_list = [dict(r) for r in open_positions]
    out, taken = [], {}
    for c in sorted((dict(c) for c in candidates), key=lambda r: (r["variant"], r["structure"], r["rank"])):
        sleeve = (c["variant"], c["structure"])
        sleeve_open = [r for r in open_list if (r["variant"], r["structure"]) == sleeve]
        reason = _cap_reason(c, taken.get(sleeve, []), sleeve_open, sizing, sb_open)
        if reason is None:
            taken[sleeve] = taken.get(sleeve, []) + [c]
        out.append({**c, "cap_pass": reason is None, "cap_reason": reason})
    return out
