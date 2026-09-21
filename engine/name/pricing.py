"""R4 of the ticker sheet, part 1 (findings/stock-deep-dive DESIGN/70 §5): how one leg is marked,
what a structure costs, what it can lose, where it breaks even, the probabilities printed beside
it, and how a set of legs becomes one §7 line. `engine/name/structures.py` decides which expiry,
which strikes and which families; nothing here knows what a butterfly is.

**Marking a leg** (the brief's rule, shared with R2's L6). The live `cboe_chain` partition for the
sheet date is the first source: mark = the quoted mid, `half_spread = (ask - bid) / 2`,
`mark_source = "<chain source> <date>"`. When the stored chain is older than the sheet date, or the
leg is not in it, the name's `daily_contract` row for that contract is marked by the engine's own
tier 1/2 rule (`marking.print_mark(row, "late")`) and `half_spread = rel_spread x mark / 2`. A leg
that neither source prices is `unpriced`, and the structure that holds it is not sized.

**Sign convention.** A leg's `side` is +1 long / -1 short, as `name/grade.py` defines it, so
`entry_cost = sum(side x mark)` is positive for a net debit. The sheet prints the opposite sign --
`mark` on a structure is the net **credit** per share, positive for a short straddle and negative
for a debit vertical -- so `net_credit` is simply `-entry_cost`. `max_loss` is read off the payoff
curve by `grade.grade_vertical`, the same function that grades the row at expiry, so the sheet and
the ledger can never disagree about what a structure could lose.

**Probabilities** are context, never a size (§5): a driftless lognormal to expiry at the trailing
63-session close-to-close sigma -- deliberately not the IV the sheet is judging -- with
`P(touch) = 2 x P(beyond)` by reflection. Every one of them is None when the bar history is short.

**One line.** `blank_line` is the §7 shape with every number null (an unpriced or impossible line
still prints, with its reason); `defined_line` and `straddle_line` fill it in from a leg set, a
`Ctx` (the session, its close, the live chain, the trailing sigma) and the sizing rule -- both
family-agnostic, since a butterfly, a condor and a vertical are one arithmetic over different legs.
Pure functions over dicts and frames; no I/O, no mutation of any input.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy.stats import norm

from engine import marking as M
from engine.config import (COMMISSION_PER_CONTRACT, CONTRACT_MULTIPLIER, MODEL_SPREAD_FLOOR,
                           NameParams, NameSizing)
from engine.name.grade import grade_vertical
from engine.strategies.sa_filters import _num, to_date

RIGHT_CALL, RIGHT_PUT, RIGHT_SHARES = "C", "P", "S"
RIGHT_TO_TYPE = {RIGHT_CALL: "call", RIGHT_PUT: "put"}
SIDE_LONG, SIDE_SHORT = 1, -1
STRIKE_TOL = 1e-6
PAYOFF_TOL = 1e-9
BREAKEVEN_DP = 6
DAYS_PER_YEAR = 365.0
SESSIONS_PER_YEAR = 252.0
MIN_BARS_FOR_SIGMA = 40          # "null when bars are short": fewer sessions than this, no sigma
TOUCH_ENTRY, TOUCH_ROUND_TRIP = 1, 2
UNIT_CONTRACT, UNIT_SHARE = "contract", "share"
NOTE_JOIN = " · "
NOTE_NO_SIZE = "max loss exceeds 0.5% of E at one contract"
NOTE_MEASUREMENT = "ALLOW_UNDEFINED=0: measurement only"


# --- marking one leg -----------------------------------------------------------------------------

def chain_source(inputs) -> str | None:
    """`"<source> <date>"` when `inputs.chain` is a chain of the sheet date itself, else None.

    A stored chain older than the sheet date is not a live quote and is not used: the
    `daily_contract` tier 1/2 mark of the session is the honest price for that leg.
    """
    meta = inputs.chain_meta or {}
    if inputs.chain is None or inputs.chain.empty:
        return None
    source, carried = meta.get("source"), meta.get("date")
    if not source or carried != inputs.date.isoformat():
        return None
    return f"{source} {carried}"


def _row_at(frame: pd.DataFrame, expiry, strike: float, right_column: str, right_value: str):
    """The one row of `frame` for (expiry, strike, right), or None. Never raises on a thin frame."""
    if frame is None or frame.empty:
        return None
    needed = {"expiry", "strike", right_column}
    if not needed.issubset(frame.columns):
        return None
    match = ((frame[right_column] == right_value)
             & (frame["expiry"].map(to_date) == expiry)
             & ((pd.to_numeric(frame["strike"], errors="coerce") - strike).abs() <= STRIKE_TOL))
    hit = frame[match.fillna(False)]
    return None if hit.empty else hit.iloc[0].to_dict()


def _quote_mark(row: dict, source: str) -> dict | None:
    """Mid and quoted half-spread from a chain row; None when the NBBO is not a usable quote."""
    bid, ask = _num(row.get("bid")), _num(row.get("ask"))
    if bid is None or ask is None or bid < 0 or ask <= 0 or ask < bid:
        return None
    mid = _num(row.get("mid"))
    if mid is None or mid <= 0:
        mid = (bid + ask) / 2.0
    if mid <= 0:
        return None
    return {"mark": float(mid), "half_spread": float((ask - bid) / 2.0), "mark_source": source}


def _print_leg_mark(row: dict) -> dict | None:
    """The engine's tier 1/2 `daily_contract` mark; `half_spread = rel_spread x mark / 2`."""
    mark = M.print_mark(row, M.WHEN_LATE)
    if mark is None or mark.price is None or mark.price <= 0:
        return None
    rel = mark.rel_spread if not math.isnan(mark.rel_spread) else MODEL_SPREAD_FLOOR
    return {"mark": float(mark.price), "half_spread": float(rel * mark.price / 2.0),
            "mark_source": f"daily_contract tier {mark.tier}"}


def leg_mark(inputs, expiry, strike: float, right: str, *, live_source: str | None) -> dict | None:
    """`{mark, half_spread, mark_source}` for one contract, or None when nothing prices it."""
    if live_source is not None:
        row = _row_at(inputs.chain, expiry, strike, "right", right)
        priced = _quote_mark(row, live_source) if row is not None else None
        if priced is not None:
            return priced
    row = _row_at(inputs.contracts_today, expiry, strike, "option_type", RIGHT_TO_TYPE[right])
    return _print_leg_mark(row) if row is not None else None


def make_leg(inputs, expiry, strike: float, right: str, side: int, *,
             live_source: str | None) -> dict:
    """A §7 leg dict. `mark` is None when the leg is unpriced -- a null is a value, never a raise."""
    priced = leg_mark(inputs, expiry, strike, right, live_source=live_source) or {}
    return {"right": right, "strike": float(strike), "side": int(side),
            "mark": priced.get("mark"), "half_spread": priced.get("half_spread"),
            "mark_source": priced.get("mark_source"), "expiry": expiry.isoformat()}


def share_leg(close: float, side: int, source: str) -> dict:
    """The one-leg SHARES line: no strike, no expiry, marked at the session close."""
    return {"right": RIGHT_SHARES, "strike": None, "side": int(side), "mark": float(close),
            "half_spread": None, "mark_source": source, "expiry": None}


def is_priced(legs: list[dict]) -> bool:
    return bool(legs) and all(leg.get("mark") is not None for leg in legs)


def unpriced_leg_label(legs: list[dict]) -> str:
    """`"<expiry> <strike><right>"` for the first leg nothing could price."""
    leg = next(leg for leg in legs if leg.get("mark") is None)
    return f"{leg['expiry']} {leg['strike']:g}{leg['right']}"


def mark_sources(legs: list[dict]) -> str | None:
    """The distinct sources behind a structure, in leg order: one name when they agree."""
    seen = [leg["mark_source"] for leg in legs if leg.get("mark_source")]
    ordered = list(dict.fromkeys(seen))
    return " + ".join(ordered) if ordered else None


# --- the payoff: credit, max loss, breakevens, the stress point -----------------------------------

def _intrinsic(right: str, strike: float, spot: float) -> float:
    return max(spot - strike, 0.0) if right == RIGHT_CALL else max(strike - spot, 0.0)


def payoff_value(legs: list[dict], spot: float) -> float:
    """Intrinsic value per share of the leg set at `spot` (the grader's `_value`)."""
    return sum(leg["side"] * _intrinsic(leg["right"], float(leg["strike"]), spot) for leg in legs)


def entry_cost(legs: list[dict]) -> float:
    """`sum(side x mark)`: positive for a net debit, negative for a net credit."""
    return sum(leg["side"] * leg["mark"] for leg in legs)


def net_credit(legs: list[dict]) -> float:
    """What the sheet prints as `mark`: credit per share > 0, debit < 0."""
    return -entry_cost(legs)


def max_loss_usd(legs: list[dict], spot: float) -> float | None:
    """Max loss per contract in dollars, read off the payoff curve by the R5 grader.

    The grader is the single source of truth so the sheet and the ledger row cannot disagree.
    None when the leg count is not one the grader defines (a short straddle is unbounded and is
    stressed instead, `stress_loss_usd`).
    """
    try:
        graded = grade_vertical(legs, spot)
    except ValueError:
        return None
    loss = graded["max_loss_per_share"]
    return float(loss * CONTRACT_MULTIPLIER) if loss > 0 else None


def breakevens(legs: list[dict]) -> list[float]:
    """Every zero of the expiry payoff, ascending. Piecewise linear with kinks at the strikes, so
    probing 0, each strike and a point above the top strike finds them all."""
    if not is_priced(legs):
        return []
    strikes = sorted(float(leg["strike"]) for leg in legs)
    probes = [0.0, *strikes, 2 * strikes[-1] + 1.0]
    cost = entry_cost(legs)
    roots: set[float] = set()
    for low, high in zip(probes, probes[1:]):
        f_low, f_high = payoff_value(legs, low) - cost, payoff_value(legs, high) - cost
        for point, value in ((low, f_low), (high, f_high)):
            if abs(value) <= PAYOFF_TOL:
                roots.add(round(point, BREAKEVEN_DP))
        if f_low * f_high < 0:
            roots.add(round(low + (high - low) * f_low / (f_low - f_high), BREAKEVEN_DP))
    return sorted(roots)


def stress_loss_usd(legs: list[dict], spot: float, sigma_hold: float, stress_sigma: float) -> float | None:
    """The undefined-risk line's §5 stress: the loss per contract at `spot +/- stress x sigma_hold`,
    worse side. None (not zero) when the structure cannot lose at either point."""
    if sigma_hold is None or sigma_hold <= 0:
        return None
    cost = entry_cost(legs)
    move = stress_sigma * sigma_hold
    worst = min(payoff_value(legs, spot + sign * move) - cost for sign in (1.0, -1.0))
    return float(-worst * CONTRACT_MULTIPLIER) if worst < 0 else None


# --- the cost model (§5: Muravyev-Pearson effective/quoted + $0.65 a contract) --------------------

def option_cost_usd(legs: list[dict], params: NameParams, touches: int) -> float | None:
    """Dollars per contract: `0.584 x half_spread x 100 + 0.65` per leg, once for a premium
    structure held to expiry and twice for a vertical closed at the horizon."""
    spreads = [leg.get("half_spread") for leg in legs]
    if any(s is None for s in spreads):
        return None
    per_leg = sum(params.cost_spread_mult * s * CONTRACT_MULTIPLIER + COMMISSION_PER_CONTRACT
                  for s in spreads)
    return float(touches * per_leg)


def share_cost_usd(entry: float, params: NameParams) -> float | None:
    """Round-trip cost per **share**: `share_cost_bp` a side (§5). The SHARES line reports every
    dollar figure per share, and its `n` is a share count -- `unit` on the line says so."""
    if entry is None or entry <= 0:
        return None
    return float(params.share_cost_bp * 1e-4 * entry * 2)


# --- probabilities (§5; context only, never a size) ----------------------------------------------

def sigma_c2c(bars: pd.DataFrame, params: NameParams) -> float | None:
    """Annualised close-to-close vol over the trailing `sigma_c2c_window` sessions of `bars`.
    None when fewer than `MIN_BARS_FOR_SIGMA` sessions are stored: a short history is a null."""
    if bars is None or len(bars) < MIN_BARS_FOR_SIGMA or "close" not in bars.columns:
        return None
    closes = pd.to_numeric(bars["close"], errors="coerce").dropna().to_numpy(dtype=float)
    if len(closes) < MIN_BARS_FOR_SIGMA or (closes <= 0).any():
        return None
    returns = np.diff(np.log(closes))[-params.sigma_c2c_window:]
    if len(returns) < 2:
        return None
    sigma = float(np.std(returns, ddof=1) * math.sqrt(SESSIONS_PER_YEAR))
    return sigma if sigma > 0 else None


def _d(spot: float, strike: float, sigma: float, t: float) -> float:
    """`ln(K/S)` shifted by the driftless lognormal's median, in standard deviations."""
    return (math.log(strike / spot) + 0.5 * sigma ** 2 * t) / (sigma * math.sqrt(t))


def _usable(spot, strike, sigma, t) -> bool:
    return all(v is not None for v in (spot, strike, sigma, t)) and spot > 0 and strike > 0 \
        and sigma > 0 and t > 0


def prob_below(spot: float, strike: float, sigma: float | None, t: float) -> float | None:
    """P(S_T <= K) under a driftless lognormal (E[S_T] = S)."""
    if not _usable(spot, strike, sigma, t):
        return None
    return float(norm.cdf(_d(spot, strike, sigma, t)))


def p_inside(spot: float, low: float, high: float, sigma: float | None, t: float) -> float | None:
    """P(the breakevens hold at expiry). None when either bound or sigma is null."""
    below_high, below_low = prob_below(spot, high, sigma, t), prob_below(spot, low, sigma, t)
    if below_high is None or below_low is None:
        return None
    return float(max(0.0, below_high - below_low))


def p_touch(spot: float, strike: float, sigma: float | None, t: float, *, above: bool) -> float | None:
    """`2 x P(beyond)` by reflection, capped at 1 (§5)."""
    below = prob_below(spot, strike, sigma, t)
    if below is None:
        return None
    beyond = (1.0 - below) if above else below
    return float(min(1.0, 2.0 * beyond))


# --- sizing (D5: risk units at a stated maximum loss) ---------------------------------------------

def size_at_risk(risk_per_unit: float | None, frac: float, sizing: NameSizing) -> int:
    """`floor(frac x E / risk)`; 0 for a null or non-positive risk, never a raise."""
    if risk_per_unit is None or risk_per_unit <= 0:
        return 0
    return int(math.floor(frac * sizing.equity / risk_per_unit))


# --- legs -> one §7 line (generic: nothing here knows what a butterfly is) -------------------------

@dataclass(frozen=True)
class Ctx:
    """What every line needs: the session, the close it marks against, the chain that is live for
    it, and the sigma the probabilities use. Frozen, like everything the sheet passes around."""
    inputs: object
    params: NameParams
    sizing: NameSizing
    close: float
    close_source: str
    live_source: str | None
    sigma63: float | None


def note(parts) -> str | None:
    """The line's `note`: the reasons that apply, in order, or None when there are none."""
    kept = [p for p in parts if p]
    return NOTE_JOIN.join(kept) if kept else None


def leg_of(ctx: Ctx, expiry, strike: float, right: str, side: int) -> dict:
    return make_leg(ctx.inputs, expiry, strike, right, side, live_source=ctx.live_source)


def blank_line(family: str, expiry, legs: list[dict], *, unit: str = UNIT_CONTRACT,
               excluded_by: str | None = None, reason: str | None = None, sheet_date=None) -> dict:
    """A §7 structure with every number null: what an unpriced or impossible line looks like."""
    dte_cal = (expiry - sheet_date).days if (expiry and sheet_date) else None
    return {"family": family, "legs": legs, "expiry": expiry.isoformat() if expiry else None,
            "dte_cal": dte_cal, "mark": None, "mark_source": mark_sources(legs),
            "max_loss": None, "credit_debit": None, "breakevens": [],
            "p_inside": None, "p_touch": None, "cost": None, "n": 0, "usd_at_risk": None,
            "excluded_by": excluded_by, "note": reason, "unit": unit}


def unpriced_line(ctx: Ctx, family: str, expiry, legs: list[dict], *, excluded_by: str | None,
                  notes) -> dict:
    label = f"unpriced: {unpriced_leg_label(legs)}" if legs else None
    return blank_line(family, expiry, legs, excluded_by=excluded_by, sheet_date=ctx.inputs.date,
                      reason=note([*notes, label]))


def _credit_side(credit: float) -> str:
    return "credit" if credit > 0 else "debit"


def defined_line(ctx: Ctx, family: str, expiry, legs: list[dict], *, touches: int,
                 excluded_by: str | None = None, notes=(), short_strike: float | None = None,
                 above: bool | None = None) -> dict:
    """A defined-risk line: credit, max loss off the payoff curve, breakevens, the probability
    (inside the breakevens, or a touch of `short_strike`), cost and size. An excluded line keeps
    every price it has and is sized at zero."""
    if not is_priced(legs):
        return unpriced_line(ctx, family, expiry, legs, excluded_by=excluded_by, notes=list(notes))
    base = blank_line(family, expiry, legs, excluded_by=excluded_by, sheet_date=ctx.inputs.date)
    t = (expiry - ctx.inputs.date).days / DAYS_PER_YEAR
    credit, max_loss = net_credit(legs), max_loss_usd(legs, ctx.close)
    points = breakevens(legs)
    n = 0 if excluded_by else size_at_risk(max_loss, ctx.params.risk_frac, ctx.sizing)
    inside = _inside(ctx, points, t) if short_strike is None else None
    touch = None if short_strike is None else p_touch(ctx.close, short_strike, ctx.sigma63, t,
                                                      above=bool(above))
    return {**base, "mark": float(credit), "credit_debit": _credit_side(credit),
            "max_loss": max_loss, "breakevens": points, "p_inside": inside, "p_touch": touch,
            "cost": option_cost_usd(legs, ctx.params, touches), "n": n,
            "usd_at_risk": float(n * max_loss) if max_loss is not None else None,
            "note": note([*notes, None if (excluded_by or n) else NOTE_NO_SIZE])}


def _inside(ctx: Ctx, points: list[float], t: float) -> float | None:
    return p_inside(ctx.close, points[0], points[-1], ctx.sigma63, t) if len(points) >= 2 else None


def straddle_line(ctx: Ctx, family: str, expiry, legs: list[dict], sigma: float | None,
                  excluded_by: str | None) -> dict:
    """The undefined-risk line: no max loss, a 3-sigma stress instead, and no size at all unless
    `ALLOW_UNDEFINED=1` (D11's default is off, so this line is a measurement)."""
    if not is_priced(legs):
        return unpriced_line(ctx, family, expiry, legs, excluded_by=excluded_by, notes=[])
    base = blank_line(family, expiry, legs, excluded_by=excluded_by, sheet_date=ctx.inputs.date)
    t = (expiry - ctx.inputs.date).days / DAYS_PER_YEAR
    credit = net_credit(legs)
    stress = stress_loss_usd(legs, ctx.close, sigma, ctx.params.stress_sigma)
    points = breakevens(legs)
    if excluded_by or not ctx.sizing.allow_undefined:
        n, reason = 0, (None if excluded_by else NOTE_MEASUREMENT)
    else:
        n = size_at_risk(stress, ctx.params.undefined_risk_frac, ctx.sizing)
        reason = None if n else NOTE_NO_SIZE
    return {**base, "mark": float(credit), "credit_debit": _credit_side(credit),
            "max_loss": None, "stress_loss_3s": stress, "breakevens": points,
            "p_inside": _inside(ctx, points, t),
            "cost": option_cost_usd(legs, ctx.params, TOUCH_ENTRY), "n": n,
            "usd_at_risk": float(n * stress) if stress is not None else None, "note": reason}
