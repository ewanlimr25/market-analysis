#!/usr/bin/env python3
"""Liquidity floor + market-excess win-rate gate for the conviction sizer.

Stdlib-only (no pip installs; runs under the already-allowed ``Bash(python3:*)``).
Two responsibilities, shared by improvement-criteria-register criteria **C12** and **C2**
(``analyses/audit/2026-05-25/improvement_criteria.md``):

  C12 — :func:`apply_liquidity_floor` drops candidates below a 20-day dollar-ADV / price
        floor BEFORE they enter the candidate funnel or the win-rate denominator.
  C2  — :func:`n_conditional_cap` (tightened so ``n < 10`` caps below the full-size line) +
        :func:`market_excess` + :func:`size_decision` turn a raw backtest win-rate into a
        pre-risk size that beta-in-an-up-tape cannot clear.

Why this exists: the UW ``historical_signal_backtest`` tool has no liquidity floor and no
regime control. A ``volume_spike`` probe on 2026-05-20 returned GIF/BLCN/PEX/IGLD/UTHY/ESGE —
micro-ETFs the desk cannot fill at size, which also poison the win-rate denominator. A
``bullish_flow`` probe returned a 100% win-rate over 8 signals dated 05-19/05-20, in an
UPTREND where SPY itself was one of the "signals" — i.e. beta, not edge. This module is the
deterministic, auditable floor + excess gate that catches both.

Academic basis: Barbon & Buraschi (gamma/flow effects strongest in the least-liquid names —
exactly where a flow-follower is least able to exit); Bollerslev-Tauchen-Zhou and
López de Prado (an unconditional, multiply-tested win-rate blends regimes and inflates edge).

The agent populates ``price`` and ``adv_usd`` from yahoo ``get_historical_stock_prices``
(or a screener field) and ``benchmark_win_rate`` from the same-window SPY directional
outcome. This module does the arithmetic so the decision is reproducible and testable.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

# ----- C12 liquidity floor thresholds ---------------------------------------
MIN_ADV_USD = 50_000_000.0  # 20-day average *dollar* volume floor ($50M notional)
MIN_PRICE = 5.0             # sub-$5 / penny floor


@dataclass(frozen=True)
class Candidate:
    """One screened name. ``price``/``adv_usd`` come from yahoo or a screener field.

    ``won`` (when graded) feeds the win-rate denominator; ``None`` means ungraded.
    """

    ticker: str
    price: float | None = None
    adv_usd: float | None = None  # 20-day average dollar volume
    won: bool | None = None       # graded directional outcome, optional


def passes_liquidity_floor(
    c: Candidate, min_adv: float = MIN_ADV_USD, min_price: float = MIN_PRICE
) -> bool:
    """True iff the name clears BOTH the dollar-ADV and price floors.

    Fail-closed: a name whose ``price`` or ``adv_usd`` could not be measured FAILS the
    floor. The desk cannot size what it cannot measure, and an unverifiable name must not
    inflate the win-rate denominator. Legit large-caps always have this data via yahoo, so
    fail-closed only removes names the agent could not confirm are tradable.
    """
    if c.price is None or c.adv_usd is None:
        return False
    return c.price >= min_price and c.adv_usd >= min_adv


def apply_liquidity_floor(
    candidates: list[Candidate],
    min_adv: float = MIN_ADV_USD,
    min_price: float = MIN_PRICE,
) -> tuple[list[Candidate], list[Candidate]]:
    """Split candidates into (kept, excluded) by the liquidity floor.

    Used in two places: (1) the Step-0 funnel, so junk never reaches the agents; and
    (2) the win-rate denominator, so a class is not credited for un-tradable names.
    """
    kept: list[Candidate] = []
    excluded: list[Candidate] = []
    for c in candidates:
        (kept if passes_liquidity_floor(c, min_adv, min_price) else excluded).append(c)
    return kept, excluded


def compute_win_rate(candidates: list[Candidate]) -> tuple[int, int, float | None]:
    """Win-rate over GRADED candidates only. Returns (wins, n_graded, win_rate|None)."""
    graded = [c for c in candidates if c.won is not None]
    wins = sum(1 for c in graded if c.won)
    n = len(graded)
    return wins, n, (wins / n if n else None)


# ----- C2 market-excess + tightened N-conditional cap -----------------------
#
# The sizing ladder (calibrated on RAW win-rate by the 2026-05-15 audit) is preserved:
#   >= 0.70 -> full | 0.50-0.70 -> half | < 0.50 -> starter/skip.
# C2 adds two guards ON TOP of that ladder, neither of which recalibrates the thresholds:
#   1. A TIGHTER N-conditional cap: n < 10 caps at 0.69 (one notch BELOW the 0.70 full line),
#      so an 8-signal up-week class can size at most half. (Was 0.75, which still cleared full.)
#   2. A MARKET-EXCESS gate: if a signal does not beat the same-direction SPY bet over the same
#      windows (excess <= 0), it is beta not edge -> cap at half; materially negative -> starter.
#      The gate can only DOWNGRADE; it never upgrades.
MATERIALLY_NEGATIVE_EXCESS = -0.10  # signal underperforms the market by >= 10pp -> starter

# 2026-05-30 register P1.2 absolute reliability ceiling, enforced here since the
# 2026-06-06 audit P0.1: no class earns a >0.80 quote at ANY sample size (the >=0.90
# claimed bucket realised 51-53%, the 0.80-0.90 bucket 55-62%, across both audits).
ABSOLUTE_WR_CEILING = 0.80

_SIZE_RANK = {"skip": 0, "starter": 1, "half": 2, "full": 3}


def n_conditional_cap(win_rate: float, n: int) -> float:
    """Cap the quoted win-rate by backtest sample size (2026-05-15 audit, C2-tightened;
    synced to the live 0.80 ceiling by the 2026-06-06 audit P0.1 — was stale at 0.85/0.90).

    n < 10  -> 0.69  (TIGHTENED from 0.75: keeps a single-regime small-N class below the
                      0.70 full-size line so it cannot full-size on an up-week alone)
    n >= 10 -> 0.80  (ABSOLUTE_WR_CEILING — 2026-05-30 register P1.2. The prior
                      0.85 (10<=n<20) / 0.90 (n>=20) tiers silently re-permitted the
                      quotes the ceiling bans; realized 2026-06-06 audit P0.1, where 11
                      post-register vol-lane rows quoted 0.837-0.933 raw backtest rates
                      and the decided ones went 0-for-3.)
    """
    cap = 0.69 if n < 10 else ABSOLUTE_WR_CEILING
    return min(win_rate, cap)


# ----- 2026-06-20 audit P1 #2: ceiling + clean-source emission guard -----------
# Sizing-eligible win_rate sources. The 2026-06-12 P0.3 quarantine RETIRED
# ``backtest`` / ``fallback_proxy`` as sizing sources (substrate-contaminated): the
# 2026-06-20 audit measured 30 pre-freeze envelopes that quoted >=0.80 off exactly
# these sources (earnings_vol 0.86->0.38, high_iv_rank 0.84->0.38, both BH-surviving).
SIZING_ELIGIBLE_SOURCES = frozenset({"backtest_clean", "NA(substrate)", "NA", None})
RETIRED_SUBSTRATE_SOURCES = frozenset({"backtest", "fallback_proxy"})


def sizing_eligible_quote(win_rate: float | None, win_rate_source: str | None) -> dict:
    """C2 / 2026-06-20 P1 #2 emission guard: bind the 0.80 ceiling AND the clean-source
    requirement at serialization, mirroring the sub-0.50 pre-emit floor in the agent.

    Returns an audit dict:
      ``sizing_eligible`` — False when the quote carries a RETIRED substrate source; such a
                            quote must NOT drive ``pre_risk_size`` (size at the NA(substrate)
                            tier-default-capped-at-half and mark advisory/non-sizing).
      ``capped_win_rate``  — ``win_rate`` clamped to ABSOLUTE_WR_CEILING (None if input None).
      ``ceiling_ok``       — was the input already <= 0.80 (a serialized >0.80 is an envelope bug).
      ``reason``           — human-readable audit string.
    """
    eligible = win_rate_source in SIZING_ELIGIBLE_SOURCES
    capped = None if win_rate is None else round(min(win_rate, ABSOLUTE_WR_CEILING), 4)
    ceiling_ok = win_rate is None or win_rate <= ABSOLUTE_WR_CEILING
    if not eligible:
        reason = (
            f"win_rate_source={win_rate_source!r} is RETIRED substrate (2026-06-12 P0.3) -> "
            f"NON-SIZING; size at NA(substrate) tier-default capped half"
        )
    elif not ceiling_ok:
        reason = f"win_rate {win_rate} > {ABSOLUTE_WR_CEILING} ceiling -> clamped to {capped} (envelope bug if serialized raw)"
    else:
        reason = f"win_rate {win_rate} (source {win_rate_source}) <= {ABSOLUTE_WR_CEILING} ceiling -> sizing-eligible"
    return {
        "sizing_eligible": eligible,
        "capped_win_rate": capped,
        "ceiling_ok": ceiling_ok,
        "reason": reason,
    }


def market_excess(signal_win_rate: float, benchmark_win_rate: float) -> float:
    """Market-excess win-rate = signal WR - benchmark WR.

    ``benchmark_win_rate`` MUST be the SAME-DIRECTION bet on SPY over the SAME signal
    windows (long signal -> fraction of windows SPY rose; short signal -> fraction SPY
    fell). This subtracts the beta a signal earns just by agreeing with the tape, so an
    up-tape 100% bullish class (benchmark ~1.0) reads as ~0 excess, not edge.

    Both arguments are the RAW (uncapped) win-rate — apples-to-apples. The N-cap is a
    separate humility guard on the *quoted* win-rate and is deliberately NOT applied here.

    WINDOW-MATCHING RULE (2026-06-12 audit P2.6 — the caller's responsibility, not
    enforced here). ``benchmark_win_rate`` must be computed over **exactly the kept
    windows of the signal side** — i.e. the P0.3 clean-query complete-forward-window set
    (signal_date has >= lookback_days of data after it), NOT whatever windows the caller
    can conveniently build. Two failure modes this rule exists to stop: (1) computing SPY
    over the FULL calendar while the signal side dropped clamped (too-recent) windows ->
    apples-to-oranges excess, sign-flippable near the 0 boundary where the gate is binary;
    (2) reusing SPY's appearance INSIDE the signal class's own backtest set as the
    benchmark -> conflates the signal with its reference. The matched window set is NOT
    reconstructible from ``uw historical signal-backtest`` output alone (it returns per-row
    signal_date but the SPY-side fractions must be rebuilt over those same dates via a
    dedicated SPY ``uw historical trend``); the caller (signal-confluence-quant, under the
    P0.3 protocol) owns that reconstruction and must record the date set in audit_trail.
    """
    return round(signal_win_rate - benchmark_win_rate, 4)


def size_from_winrate(win_rate: float | None) -> str:
    """Map a (capped) win-rate to the calibrated pre-risk size ladder."""
    if win_rate is None:
        return "starter"  # newly covered / no history
    if win_rate >= 0.70:
        return "full"
    if win_rate >= 0.50:
        return "half"
    return "starter"


def _min_size(a: str, b: str) -> str:
    return a if _SIZE_RANK[a] <= _SIZE_RANK[b] else b


def size_decision(
    signal_win_rate: float | None,
    n: int,
    benchmark_win_rate: float | None = None,
    *,
    liquidity_ok: bool = True,
) -> dict:
    """Full C2 sizing decision: liquidity floor -> N-cap -> ladder -> market-excess gate.

    Returns an audit dict. The market-excess gate can only downgrade the ladder size.
    """
    if not liquidity_ok:
        return {
            "capped_win_rate": None, "excess": None, "base_size": "skip",
            "final_size": "skip", "excess_gate": "below_liquidity_floor",
            "reason": "below liquidity floor (price < $5 or 20d $ADV < $50M or unverifiable)",
        }

    capped = None if signal_win_rate is None else round(n_conditional_cap(signal_win_rate, n), 4)
    base = size_from_winrate(capped)
    final = base
    excess = None
    gate = "no_benchmark"

    if benchmark_win_rate is not None and signal_win_rate is not None:
        excess = market_excess(signal_win_rate, benchmark_win_rate)
        # Branch order matters: the more-negative threshold MUST be checked first, else
        # excess=-0.15 would satisfy `<= 0` and only cap to half instead of starter.
        if excess <= MATERIALLY_NEGATIVE_EXCESS:
            final = _min_size(base, "starter")
            gate = f"excess {excess:+.2f} <= {MATERIALLY_NEGATIVE_EXCESS:+.2f} -> starter (beta, underperforms market)"
        elif excess <= 0:
            final = _min_size(base, "half")
            gate = f"excess {excess:+.2f} <= 0 -> capped half (no edge over same-direction SPY)"
        else:
            gate = f"excess {excess:+.2f} > 0 -> edge confirmed, no excess penalty"

    reason = (
        f"raw {signal_win_rate} n={n} -> N-cap {capped} -> ladder {base}"
        + (f"; market-excess gate: {gate} -> {final}" if benchmark_win_rate is not None else "")
    )
    return {
        "capped_win_rate": capped, "excess": excess, "base_size": base,
        "final_size": final, "excess_gate": gate, "reason": reason,
    }


# ----- CLI ------------------------------------------------------------------


def _candidates_from_json(payload: dict) -> list[Candidate]:
    return [
        Candidate(
            ticker=row.get("ticker", "?"),
            price=row.get("price"),
            adv_usd=row.get("adv_usd"),  # DOLLAR volume (shares x close), NOT a share count
            won=row.get("won"),
        )
        for row in payload.get("candidates", [])
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description="Liquidity-floor a candidate set (C12).")
    parser.add_argument("--file", help="JSON file with {'candidates': [{ticker, price, adv_usd, won?}]}")
    parser.add_argument("--min-adv", type=float, default=MIN_ADV_USD)
    parser.add_argument("--min-price", type=float, default=MIN_PRICE)
    args = parser.parse_args()

    if not args.file:
        parser.error("--file is required")
    payload = json.loads(Path(args.file).read_text(encoding="utf-8"))
    cands = _candidates_from_json(payload)
    kept, excluded = apply_liquidity_floor(cands, args.min_adv, args.min_price)
    print(json.dumps({
        "kept": [c.ticker for c in kept],
        "excluded": [c.ticker for c in excluded],
        "min_adv_usd": args.min_adv,
        "min_price": args.min_price,
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
