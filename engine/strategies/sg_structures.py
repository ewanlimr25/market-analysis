"""S-G structures and sizing (DESIGN/91 §2, §3).

LS (long ATM straddle) and LG (long strangle, one strike out) are built from
`engine.strategies.sa_structures.Leg` / `Contract` with `side = LONG`; `price_legs` is
sign-agnostic (DESIGN/91 §2) and reused unmodified, so no new pricing math is written here, only
leg construction and the defined-risk sizing rule (max loss = premium paid, unlike S-A's
undefined-risk short straddle).
"""
from __future__ import annotations

import math

from engine.config import CONTRACT_MULTIPLIER, SGParams
from engine.strategies.sa_structures import LONG, Leg, credit_per_share, make_contract, osi_id  # noqa: F401

STRUCTURE_LS, STRUCTURE_LG = "LS", "LG"
STRUCTURES = (STRUCTURE_LS, STRUCTURE_LG)
MIN_PREMIUM_USD = 1.0


def premium_paid_usd(legs: list[Leg], n: int) -> float:
    """Debit paid per the position (positive dollars): -credit_entry * mult * n."""
    credit_entry = credit_per_share(legs, "entry")
    return max(-credit_entry * CONTRACT_MULTIPLIER * n, MIN_PREMIUM_USD)


def size_long(premium_paid_per_contract: float, equity: float, params: SGParams) -> int:
    """n = floor(risk_frac * equity / premium_paid_per_contract), minimum 1 (DESIGN/91 §3)."""
    if premium_paid_per_contract <= 0:
        return 1
    return max(1, math.floor(params.risk_frac * equity / premium_paid_per_contract))
