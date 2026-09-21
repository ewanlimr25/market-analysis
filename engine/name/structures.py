"""R4 of the ticker sheet (findings/stock-deep-dive DESIGN/70 §4 X1..X6, §5, §7 `structures[]`):
the section-G menu for one name on one session, as a list of plain dicts.

`build(...)` is pure. It reads `NameInputs` (R1) and the finished R2/R3 sections as dicts, takes
only the keys it needs, and returns the §5 menu:

    IB   S-C's iron butterfly: short straddle at the strike nearest the close, wings at
         `round_to_listed_strike(S +/- x6_wing_sigma x sigma_hold)` on that expiry's grid  (X6)
    IC   a one-sigma iron condor: shorts at +/- 1 sigma_hold, longs one step further at +/- 2
    SS   the short straddle alone -- a measurement line unless `ALLOW_UNDEFINED=1`   (D5, D11)
    SHARES / DEBIT_VERTICAL / CREDIT_VERTICAL   only when the owner passed a DIRECTION

**§2 is the one stop.** A `CANNOT_PRICE` sheet writes no structure: `build` returns `[]` when
`liquidity["can_price"]` is false (and when the session has no close at all). Sections B, E and F
still write -- that is R6's business, not this module's. X3 therefore never appears on a line.

**Nothing else drops a line.** An expiry that does not exist, a leg nothing can price, a strike
grid too coarse for the wings, an earnings print inside the expiry, a top-decile borrow fee: each
of those produces the line anyway, with `excluded_by` or `note` saying why and `n = 0`. An excluded
line keeps its mark, its max loss and its breakevens -- the reader is shown the price and the
reason, and the R5 ledger still writes the exploration row that grades S-C's own filter.

**Units.** Option lines are per contract (`unit = "contract"`): `mark` is the net credit per share
(credit > 0, so a short straddle is positive and a debit vertical negative), `max_loss`, `cost` and
`usd_at_risk` are dollars per contract, `n` is contracts. The SHARES line is per share
(`unit = "share"`): `max_loss` and `cost` are dollars per share and `n` is a share count.

Marking, the payoff arithmetic, the cost model, the probabilities, the sizing and the generic
legs-to-line shape all live in `engine/name/pricing.py`; `max_loss` is read off the payoff curve by
`grade.grade_vertical`, the same function that grades the row at expiry, so the sheet and the
ledger can never disagree about what a structure could lose.
"""
from __future__ import annotations

from datetime import date, timedelta

import pandas as pd

from engine import calendar as cal
from engine.config import NAME_PARAMS, NAME_SIZING, SC_PARAMS, NameParams, NameSizing
from engine.name import pricing as P
from engine.strategies.sa_filters import StrikeGrid, _num, round_to_strike, strike_grid, to_date
from engine.strategies.sc_filters import select_expiry, sigma_hold

FAMILY_IB, FAMILY_IC, FAMILY_SS = "IB", "IC", "SS"
FAMILY_SHARES, FAMILY_DEBIT, FAMILY_CREDIT = "SHARES", "DEBIT_VERTICAL", "CREDIT_VERTICAL"
PREMIUM_FAMILIES = (FAMILY_IB, FAMILY_IC, FAMILY_SS)
DIRECTIONS = ("long", "short")
EXCLUDED_X1, EXCLUDED_X2 = "X1", "X2"

NOTE_DEFINED_RISK = "defined-risk preferred"
NOTE_X2 = ("short shares excluded by X2 (borrow fee in the top decile, or fewer than 100,000 "
           "shares available); the debit put vertical on this menu is the put-side spread")
NOTE_NO_ATR = "no ATR(14): the X4 stop cannot be placed"
NOTE_NO_SIGMA = "no iv30d: sigma_hold cannot be placed on the strike grid"
NOTE_NO_GRID = "no listed strike grid at that expiry"
NOTE_DEGENERATE = "the strike grid is too coarse for the sigma_hold wings"
NOTE_NO_PREMIUM_EXPIRY = (f"no listed Friday-type expiry with calendar DTE in "
                          f"[{SC_PARAMS.dte_cal_min}, {SC_PARAMS.dte_cal_max}]")


# --- the session's close, its listed expiries and their strike grids ------------------------------

def _close(inputs) -> tuple[float | None, str]:
    """The close the menu marks against, and the source that carries it."""
    screener = inputs.screener or {}
    value = _num(screener.get("close"))
    if value is not None and value > 0:
        return value, f"screener {inputs.date.isoformat()}"
    chain = inputs.chain
    if chain is not None and not chain.empty and "underlying_price" in chain.columns:
        quoted = chain["underlying_price"].dropna()
        value = _num(quoted.iloc[0]) if not quoted.empty else None
        if value is not None and value > 0:
            return value, P.chain_source(inputs) or "chain"
    bars = inputs.bars
    if bars is not None and not bars.empty and "close" in bars.columns:
        value = _num(bars["close"].iloc[-1])
        if value is not None and value > 0:
            return value, f"bars {inputs.date.isoformat()}"
    return None, "none"


def _expiry_frame(inputs, live_source: str | None) -> pd.DataFrame | None:
    """The frame the listed expiries and the strike grid come from: the live chain when there is
    one (it lists every expiry, not only the ones that printed), else `daily_contract`."""
    frame = inputs.chain if live_source else inputs.contracts_today
    if frame is None or frame.empty or "expiry" not in frame.columns:
        return None
    return frame


def listed_expiries(inputs, live_source: str | None) -> list[date]:
    """Every expiry the chain lists, plus every expiry that printed on the session (a contract that
    printed is listed even when the stored chain is partial); each leg is still priced per leg."""
    out: set[date] = set()
    for frame in (inputs.chain if live_source else None, inputs.contracts_today):
        if frame is not None and not frame.empty and "expiry" in frame.columns:
            out |= {to_date(x) for x in frame["expiry"].dropna().unique()}
    return sorted(out)


def _quoted(rows: pd.DataFrame) -> pd.DataFrame:
    """Chain rows with a usable quote (`ask > 0`). A stored snapshot lists strikes the market makers
    had pulled by the time it was taken (0/0 on the 2.5-spaced NVDA monthlies on a weekend), and a
    strike nothing quotes or prints cannot anchor a structure."""
    if "ask" not in rows.columns:
        return rows
    return rows[pd.to_numeric(rows["ask"], errors="coerce").fillna(0) > 0]


def strike_grid_at(inputs, expiry: date, live_source: str | None) -> StrikeGrid | None:
    """That expiry's grid: the strikes the live chain quotes, plus the strikes that printed on the
    session (a stored chain trimmed to the near expiries still prices the far ones by print)."""
    frames = []
    for frame, is_chain in ((inputs.chain if live_source else None, True), (inputs.contracts_today, False)):
        if frame is None or frame.empty or "expiry" not in frame.columns:
            continue
        rows = frame[frame["expiry"].map(to_date) == expiry]
        rows = _quoted(rows) if is_chain else rows
        if not rows.empty:
            frames.append(rows[["strike"]])
    if not frames:
        return None
    grid = strike_grid(pd.concat(frames, ignore_index=True))
    return grid if grid.strikes else None


def round_to_listed_strike(x: float, grid: StrikeGrid) -> float:
    """X6's rounding, restricted to strikes that actually exist at that expiry.

    `sa_filters.round_to_strike` may return an unprinted strike on the grid's inferred increment
    (the minimum gap), which is right for S-A's model-marked wings but wrong here: a strike the
    chain does not list cannot be marked or traded, and the leg would come back `unpriced`. The
    common case is a name quoted every 0.5 near the money and every 1.0 in the wings.
    """
    rounded = round_to_strike(x, grid)
    if any(abs(rounded - listed) <= P.STRIKE_TOL for listed in grid.strikes):
        return rounded
    return min(grid.strikes, key=lambda listed: (abs(listed - x), listed))


# --- §5 expiry rule ------------------------------------------------------------------------------

def premium_expiry(inputs, premium: dict, live_source: str | None) -> tuple[date | None, float | None]:
    """S-C's own expiry when F7 found one, else the listed Friday-type expiry with calendar DTE in
    S-C's band nearest `t + 28` (`sc_filters.select_expiry`). Returns `(expiry, sigma_hold)`;
    `sigma_hold` is S-C's when it came with the expiry, else None for the caller to compute."""
    sc = (premium or {}).get("sc") or {}
    if sc.get("expiry"):
        return to_date(sc["expiry"]), _num(sc.get("sigma_hold"))
    chosen = select_expiry(listed_expiries(inputs, live_source), inputs.date,
                           cal.is_trading_day, SC_PARAMS)
    return chosen, None


def directional_expiry(inputs, params: NameParams, live_source: str | None) -> date | None:
    """The nearest listed expiry on or after `t + dir_target_dte_cal` (the 1-4 week horizon)."""
    target = inputs.date + timedelta(days=params.dir_target_dte_cal)
    later = [e for e in listed_expiries(inputs, live_source) if e >= target]
    return later[0] if later else None


def _sigma_hold(ctx: P.Ctx, premium: dict, expiry: date | None, given: float | None) -> float | None:
    if given is not None and given > 0:
        return given
    iv30d = _num((premium or {}).get("iv30d"))
    if expiry is None or iv30d is None or iv30d <= 0:
        return None
    dte_cal = (expiry - ctx.inputs.date).days
    return sigma_hold(ctx.close, iv30d, dte_cal) if dte_cal > 0 else None


# --- §4 X1: no premium structure that straddles the next earnings session -------------------------

def x1_window_end(events: dict, sheet_date: date, params: NameParams) -> date | None:
    """The date from which X1 blocks a premium expiry: the events section's own window end, else
    the earnings session, else `t + 45` (a null earnings date is a print tomorrow, X1)."""
    raw = (events or {}).get("x1_window_end")
    if raw:
        return to_date(raw)
    earnings = ((events or {}).get("earnings") or {}).get("date")
    if earnings:
        return to_date(earnings)
    return sheet_date + timedelta(days=params.x1_unknown_earnings_days)


def x1_blocked(premium: dict, events: dict, expiry: date | None, sheet_date: date,
               params: NameParams) -> bool:
    if (premium or {}).get("x1"):
        return True
    end = x1_window_end(events, sheet_date, params)
    return expiry is not None and end is not None and expiry >= end


# --- the premium block (IB, IC, SS): X6 geometry on the chosen expiry's grid ----------------------

def _premium_lines(ctx: P.Ctx, premium: dict, events: dict) -> list[dict]:
    expiry, sc_sigma = premium_expiry(ctx.inputs, premium, ctx.live_source)
    sigma = _sigma_hold(ctx, premium, expiry, sc_sigma)
    blocked = EXCLUDED_X1 if x1_blocked(premium, events, expiry, ctx.inputs.date, ctx.params) else None
    grid = strike_grid_at(ctx.inputs, expiry, ctx.live_source) if expiry else None
    reason = (NOTE_NO_PREMIUM_EXPIRY if expiry is None
              else NOTE_NO_SIGMA if sigma is None else NOTE_NO_GRID if grid is None else None)
    if reason is not None:
        return [P.blank_line(family, expiry, [], excluded_by=blocked, reason=reason,
                             sheet_date=ctx.inputs.date) for family in PREMIUM_FAMILIES]
    wing, condor = ctx.params.x6_wing_sigma * sigma, ctx.params.x6_condor_sigma * sigma
    k_mid = round_to_listed_strike(ctx.close, grid)
    k_lo = round_to_listed_strike(ctx.close - wing, grid)
    k_hi = round_to_listed_strike(ctx.close + wing, grid)
    k_ps = round_to_listed_strike(ctx.close - condor, grid)
    k_cs = round_to_listed_strike(ctx.close + condor, grid)
    return [_butterfly(ctx, expiry, k_lo, k_mid, k_hi, blocked),
            _condor(ctx, expiry, k_lo, k_ps, k_cs, k_hi, blocked),
            _straddle(ctx, expiry, k_mid, sigma, blocked)]


def _degenerate(ctx: P.Ctx, family: str, expiry: date, blocked: str | None) -> dict:
    return P.blank_line(family, expiry, [], excluded_by=blocked, reason=NOTE_DEGENERATE,
                        sheet_date=ctx.inputs.date)


def _butterfly(ctx: P.Ctx, expiry: date, k_lo: float, k_mid: float, k_hi: float,
               blocked: str | None) -> dict:
    if not k_lo < k_mid < k_hi:
        return _degenerate(ctx, FAMILY_IB, expiry, blocked)
    legs = [P.leg_of(ctx, expiry, k_lo, P.RIGHT_PUT, P.SIDE_LONG),
            P.leg_of(ctx, expiry, k_mid, P.RIGHT_PUT, P.SIDE_SHORT),
            P.leg_of(ctx, expiry, k_mid, P.RIGHT_CALL, P.SIDE_SHORT),
            P.leg_of(ctx, expiry, k_hi, P.RIGHT_CALL, P.SIDE_LONG)]
    return P.defined_line(ctx, FAMILY_IB, expiry, legs, touches=P.TOUCH_ENTRY, excluded_by=blocked)


def _condor(ctx: P.Ctx, expiry: date, k_lo: float, k_ps: float, k_cs: float, k_hi: float,
            blocked: str | None) -> dict:
    if not k_lo < k_ps < k_cs < k_hi:
        return _degenerate(ctx, FAMILY_IC, expiry, blocked)
    legs = [P.leg_of(ctx, expiry, k_lo, P.RIGHT_PUT, P.SIDE_LONG),
            P.leg_of(ctx, expiry, k_ps, P.RIGHT_PUT, P.SIDE_SHORT),
            P.leg_of(ctx, expiry, k_cs, P.RIGHT_CALL, P.SIDE_SHORT),
            P.leg_of(ctx, expiry, k_hi, P.RIGHT_CALL, P.SIDE_LONG)]
    return P.defined_line(ctx, FAMILY_IC, expiry, legs, touches=P.TOUCH_ENTRY, excluded_by=blocked)


def _straddle(ctx: P.Ctx, expiry: date, k_mid: float, sigma: float, blocked: str | None) -> dict:
    legs = [P.leg_of(ctx, expiry, k_mid, P.RIGHT_PUT, P.SIDE_SHORT),
            P.leg_of(ctx, expiry, k_mid, P.RIGHT_CALL, P.SIDE_SHORT)]
    return P.straddle_line(ctx, FAMILY_SS, expiry, legs, sigma, blocked)


# --- the directional block (SHARES, the two verticals): X2, X4, X5 --------------------------------

def _vertical_strikes(ctx: P.Ctx, direction: str, sigma: float, grid: StrikeGrid) -> dict:
    """Debit: long ATM, short one sigma with the move. Credit: short one sigma against the move,
    long two sigma. Every strike on that expiry's own grid (X6's rounding)."""
    k_atm = round_to_listed_strike(ctx.close, grid)
    one, two = ctx.params.x6_condor_sigma * sigma, ctx.params.x6_wing_sigma * sigma
    up_one, dn_one = round_to_listed_strike(ctx.close + one, grid), round_to_listed_strike(ctx.close - one, grid)
    up_two, dn_two = round_to_listed_strike(ctx.close + two, grid), round_to_listed_strike(ctx.close - two, grid)
    if direction == "long":
        return {"right_debit": P.RIGHT_CALL, "debit_short": up_one, "right_credit": P.RIGHT_PUT,
                "credit_short": dn_one, "credit_long": dn_two, "atm": k_atm,
                "debit_above": True, "credit_above": False}
    return {"right_debit": P.RIGHT_PUT, "debit_short": dn_one, "right_credit": P.RIGHT_CALL,
            "credit_short": up_one, "credit_long": up_two, "atm": k_atm,
            "debit_above": False, "credit_above": True}


def _vertical_lines(ctx: P.Ctx, direction: str, premium: dict) -> list[dict]:
    expiry = directional_expiry(ctx.inputs, ctx.params, ctx.live_source)
    sigma = _sigma_hold(ctx, premium, expiry, None)
    grid = strike_grid_at(ctx.inputs, expiry, ctx.live_source) if expiry else None
    reason = (f"no listed expiry on or after t + {ctx.params.dir_target_dte_cal} calendar days"
              if expiry is None else NOTE_NO_SIGMA if sigma is None else
              NOTE_NO_GRID if grid is None else None)
    if reason is not None:
        return [P.blank_line(family, expiry, [], reason=reason, sheet_date=ctx.inputs.date)
                for family in (FAMILY_DEBIT, FAMILY_CREDIT)]
    k = _vertical_strikes(ctx, direction, sigma, grid)
    debit = ([P.leg_of(ctx, expiry, k["atm"], k["right_debit"], P.SIDE_LONG),
              P.leg_of(ctx, expiry, k["debit_short"], k["right_debit"], P.SIDE_SHORT)]
             if k["atm"] != k["debit_short"] else None)
    credit = ([P.leg_of(ctx, expiry, k["credit_short"], k["right_credit"], P.SIDE_SHORT),
               P.leg_of(ctx, expiry, k["credit_long"], k["right_credit"], P.SIDE_LONG)]
              if k["credit_short"] != k["credit_long"] else None)
    return [
        _degenerate(ctx, FAMILY_DEBIT, expiry, None) if debit is None else
        P.defined_line(ctx, FAMILY_DEBIT, expiry, debit, touches=P.TOUCH_ROUND_TRIP,
                      short_strike=k["debit_short"], above=k["debit_above"]),
        _degenerate(ctx, FAMILY_CREDIT, expiry, None) if credit is None else
        P.defined_line(ctx, FAMILY_CREDIT, expiry, credit, touches=P.TOUCH_ROUND_TRIP,
                      short_strike=k["credit_short"], above=k["credit_above"]),
    ]


def _shares_line(ctx: P.Ctx, direction: str, range_: dict, flags: dict, dte_cal: int) -> dict:
    """Shares with the X4 stop (`entry -/+ 2 x ATR(14)`) and the disc-1.0 target at 2R. Every
    figure on this line is per share; `n` is a share count and `unit` says so."""
    params, sign = ctx.params, (P.SIDE_LONG if direction == "long" else P.SIDE_SHORT)
    legs = [P.share_leg(ctx.close, sign, ctx.close_source)]
    excluded_by = EXCLUDED_X2 if (direction == "short" and (flags or {}).get("x2")) else None
    notes = [NOTE_DEFINED_RISK if (flags or {}).get("x5") else None,
             NOTE_X2 if excluded_by else None]
    base = {**P.blank_line(FAMILY_SHARES, None, legs, unit=P.UNIT_SHARE, excluded_by=excluded_by),
            "mark": float(ctx.close), "breakevens": [float(ctx.close)],
            "cost": P.share_cost_usd(ctx.close, params)}
    atr14 = _num((range_ or {}).get("atr14"))
    if atr14 is None or atr14 <= 0:
        return {**base, "entry": float(ctx.close), "stop": None, "target": None,
                "direction": direction, "note": P.note([*notes, NOTE_NO_ATR])}
    stop = ctx.close - sign * params.x4_atr_mult * atr14
    risk = abs(ctx.close - stop)
    target = ctx.close + sign * params.disc_target_mult * risk
    n = 0 if excluded_by else P.size_at_risk(risk, params.risk_frac, ctx.sizing)
    return {**base, "entry": float(ctx.close), "stop": float(stop), "target": float(target),
            "direction": direction, "max_loss": float(risk), "n": n,
            "usd_at_risk": float(n * risk),
            "p_touch": P.p_touch(ctx.close, stop, ctx.sigma63, dte_cal / P.DAYS_PER_YEAR,
                                 above=sign == P.SIDE_SHORT),
            "note": P.note([*notes, None if (excluded_by or n) else P.NOTE_NO_SIZE])}


def _directional_lines(ctx: P.Ctx, direction: str, premium: dict, range_: dict,
                       flags: dict) -> list[dict]:
    """X5: when the short float clears 25%, the menu lists the defined-risk verticals first."""
    expiry = directional_expiry(ctx.inputs, ctx.params, ctx.live_source)
    dte_cal = (expiry - ctx.inputs.date).days if expiry else ctx.params.dir_target_dte_cal
    shares = _shares_line(ctx, direction, range_, flags, dte_cal)
    verticals = _vertical_lines(ctx, direction, premium)
    return [*verticals, shares] if (flags or {}).get("x5") else [shares, *verticals]


# --- the entry point -----------------------------------------------------------------------------

def build(inputs, params: NameParams = NAME_PARAMS, sizing: NameSizing = NAME_SIZING, *,
          liquidity: dict, events: dict, premium: dict, range_: dict, flags: dict,
          direction: str | None) -> list[dict]:
    """The DESIGN/70 §5 menu for one name, as §7 `structures[]` dicts in reading order.

    `[]` when the §2 liquidity floor fails -- "a CANNOT_PRICE sheet still writes sections B, E and
    F and no structure" -- and when the session has no usable close. Otherwise three premium lines
    (IB, IC, SS) always, plus SHARES and the two verticals when `direction` is given; each line
    carries `rank`, its 1-based place in this list, so the report can print the X5 order without
    re-deriving it.

    The sections are read, never written: `liquidity.can_price`, `events.x1_window_end` /
    `events.earnings.date`, `premium.iv30d` / `premium.x1` / `premium.sc.{expiry, sigma_hold}`,
    `range_.atr14`, `flags.x2` / `flags.x5`. Nothing else on the sheet may change a number (§4).
    """
    if direction is not None and direction not in DIRECTIONS:
        raise ValueError(f"direction must be one of {DIRECTIONS} or None, got {direction!r}")
    if not (liquidity or {}).get("can_price"):
        return []
    close, close_source = _close(inputs)
    if close is None:
        return []
    ctx = P.Ctx(inputs=inputs, params=params, sizing=sizing, close=close,
                close_source=close_source, live_source=P.chain_source(inputs),
                sigma63=P.sigma_c2c(inputs.bars, params))
    lines = _premium_lines(ctx, premium, events)
    if direction is not None:
        lines = [*lines, *_directional_lines(ctx, direction, premium, range_, flags)]
    return [{**line, "rank": i + 1} for i, line in enumerate(lines)]
