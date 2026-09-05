"""S-A structures, pricing and sizing (DESIGN/70 §3.2, §3.3).

SS: short 1 ATM call + 1 ATM put. IC: SS plus long wings at ~2x the implied move.
Legs are priced at `late` on `pre` and `early` on `post`; costs at every touch per marking.leg_cost.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import date

from engine.config import CONTRACT_MULTIPLIER, SizingParams
from engine.marking import Contract, Mark, leg_cost

STRUCTURE_SS, STRUCTURE_IC = "SS", "IC"
STRUCTURES = (STRUCTURE_SS, STRUCTURE_IC)
SHORT, LONG = -1, +1
MIN_RISK_USD = 1.0


@dataclass(frozen=True)
class Leg:
    name: str                 # call | put | wing_call | wing_put
    contract: Contract
    side: int                 # SHORT (-1) or LONG (+1)
    entry: Mark
    exit: Mark | None       # None for a signal that has not been graded yet


def osi_id(symbol: str, expiry: date, option_type: str, strike: float) -> str:
    cp = "C" if option_type == "call" else "P"
    return f"{symbol}{expiry.strftime('%y%m%d')}{cp}{int(round(strike * 1000)):08d}"


def make_contract(symbol: str, expiry: date, option_type: str, strike: float) -> Contract:
    return Contract(osi_id(symbol, expiry, option_type, strike), symbol, option_type, float(strike), expiry)


def credit_per_share(legs: list[Leg], attr: str) -> float:
    """Net premium received per share at entry (attr='entry') or paid to close (attr='exit')."""
    return sum(-leg.side * getattr(leg, attr).price for leg in legs)


def has_exits(legs: list[Leg]) -> bool:
    return all(leg.exit is not None for leg in legs)


def price_legs(legs: list[Leg], n: int, cost_mult: float = 1.0) -> dict:
    """Entry credit, exit debit, gross and cost in dollars; exit fields NaN for ungraded legs."""
    credit_entry = credit_per_share(legs, "entry")
    entry_cost = sum(leg_cost(leg.entry, n, cost_mult) for leg in legs)
    if not has_exits(legs):
        return {"credit_entry": credit_entry, "debit_exit": math.nan, "gross_usd": math.nan,
                "entry_cost_usd": entry_cost, "exit_cost_usd": math.nan, "cost_usd": math.nan,
                "net_usd": math.nan, "n_touches": 2 * len(legs)}
    debit_exit = credit_per_share(legs, "exit")
    gross = (credit_entry - debit_exit) * CONTRACT_MULTIPLIER * n
    exit_cost = sum(leg_cost(leg.exit, n, cost_mult) for leg in legs)
    return {"credit_entry": credit_entry, "debit_exit": debit_exit, "gross_usd": gross,
            "entry_cost_usd": entry_cost, "exit_cost_usd": exit_cost, "cost_usd": entry_cost + exit_cost,
            "net_usd": gross - entry_cost - exit_cost, "n_touches": 2 * len(legs)}


def leg_record(leg: Leg) -> dict:
    """JSON-able description of a leg so a signal can be graded later from the ledger alone."""
    return {"name": leg.name, "option_chain_id": leg.contract.option_chain_id, "option_type": leg.contract.option_type,
            "strike": leg.contract.strike, "expiry": leg.contract.expiry.isoformat(), "side": leg.side,
            "entry_price": leg.entry.price, "entry_spread": leg.entry.rel_spread, "entry_tier": leg.entry.tier,
            "entry_source": leg.entry.source}


def leg_from_record(rec: dict, symbol: str, exit_mark: Mark | None) -> Leg:
    contract = Contract(rec["option_chain_id"], symbol, rec["option_type"], float(rec["strike"]),
                        date.fromisoformat(rec["expiry"]))
    entry = Mark(float(rec["entry_price"]), float(rec["entry_spread"]), int(rec["entry_tier"]), rec["entry_source"])
    return Leg(rec["name"], contract, int(rec["side"]), entry, exit_mark)


def ss_stress_loss_usd(spot: float, implied: float, credit_entry: float, move_mult: float) -> float:
    """Per-contract loss if the underlying moves `move_mult` x implied against the straddle."""
    return max((move_mult * implied * spot - credit_entry) * CONTRACT_MULTIPLIER, MIN_RISK_USD)


def ic_max_loss_usd(k: float, k_up: float, k_dn: float, credit_entry: float) -> float:
    width = max(k_up - k, k - k_dn)
    return max((width - credit_entry) * CONTRACT_MULTIPLIER, MIN_RISK_USD)


def size_ss(stress_loss_usd: float, sizing: SizingParams) -> int:
    return max(1, math.floor(sizing.ss_stress_frac * sizing.equity / stress_loss_usd))


def size_ic(max_loss_usd: float, sizing: SizingParams) -> int:
    return max(1, math.floor(sizing.ic_max_loss_frac * sizing.equity / max_loss_usd))
