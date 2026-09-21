"""R5 grader (findings/stock-deep-dive DESIGN/70 §6): how a `disc-1.0` share line and a defined-risk
option structure are scored, and the rule the 62-decision / 9-plan corpus was graded under.

The share walk is the port of `artifacts/outcomes/15_trade_plans.py::mtm` and `11_path_r.py::walk`,
which are the corrected versions of the old skill's `trade-plan-eval/lib/mark_to_market.py`:

  * a bar that touches both the stop and the target scores LOSS (the old code scored WIN);
  * `fill="limit"` requires the entry price to trade before the position exists (the old code
    assumed a fill at the plan's entry on the first session, which is `fill="instant"` here);
  * `fill="next_open"` opens at the next session's open and shifts the stop and the target by the
    same amount, so the R distance the plan chose is preserved.

`r` on a WIN is the plan's own reward |target − entry| / |entry − stop|, not +1R; on a LOSS it is
−1; on an OPEN row it is the signed close in R units. An OPEN row is not a graded row: the caller
decides whether the horizon has elapsed before writing it to the ledger.

**Window.** The walk sees the sessions strictly after `entry_after`, capped at `horizon_sessions`
and, when `through` is given, at that date. The two bounds compose: the corpus reproduction uses
`horizon_sessions=NO_HORIZON` with `through=<review date>` (a date-bounded window, which is what
the old `mtm` took), the sheet uses `horizon_sessions=21` with `through=None`.

Pure functions over a `[date, open, high, low, close]` frame in ascending date order; nothing here
reads a mart, a file or the network, and no input frame is mutated.
"""
from __future__ import annotations

from datetime import date

import pandas as pd

BAR_COLUMNS = ("date", "open", "high", "low", "close")
DIRECTIONS = ("long", "short")
FILLS = ("limit", "next_open", "instant")
OUTCOMES = ("WIN", "LOSS", "OPEN", "NO_FILL", "NO_DATA")
RIGHTS = ("C", "P")
SIDES = (1, -1)
NO_HORIZON = 10_000          # "every session in the window"; bound it with `through` instead
LEG_COUNTS = (2, 4)          # a vertical or a four-leg butterfly / condor
TOL = 1e-9


def _empty(outcome: str, sessions: int, last_close: float | None) -> dict:
    return {"outcome": outcome, "r": None, "fill_date": None, "event_date": None, "sessions": sessions,
            "mfe_r": None, "mae_r": None, "last_close": last_close}


def window(bars: pd.DataFrame, entry_after: date, horizon_sessions: int, through: date | None = None) -> pd.DataFrame:
    """The sessions strictly after `entry_after`, capped at `horizon_sessions` and at `through`."""
    missing = [c for c in BAR_COLUMNS if c not in bars.columns]
    if missing:
        raise ValueError(f"bars must carry {list(BAR_COLUMNS)}; missing {missing}")
    if horizon_sessions < 1:
        raise ValueError(f"horizon_sessions must be >= 1, got {horizon_sessions}")
    if len(bars) == 0:
        return bars
    days = pd.to_datetime(bars["date"])
    keep = days > pd.Timestamp(entry_after)
    if through is not None:
        keep &= days <= pd.Timestamp(through)
    return bars[keep].head(horizon_sessions).reset_index(drop=True)


def _first_fill(w: pd.DataFrame, entry: float) -> int | None:
    """The first session whose low..high spans `entry` (the limit rule), or None."""
    spans = (w["low"] <= entry) & (entry <= w["high"])
    hits = spans.to_numpy().nonzero()[0]
    return int(hits[0]) if len(hits) else None


def walk_shares(bars: pd.DataFrame, *, entry_after: date, direction: str, entry: float, stop: float,
                target: float, horizon_sessions: int, fill: str = "limit",
                through: date | None = None) -> dict:
    """Mark one share line to market on daily highs and lows.

    Returns `{outcome, r, fill_date, event_date, sessions, mfe_r, mae_r, last_close}`; every value
    but `outcome` and `sessions` is None where the branch does not define it.
    """
    if direction not in DIRECTIONS:
        raise ValueError(f"direction must be one of {DIRECTIONS}, got {direction!r}")
    if fill not in FILLS:
        raise ValueError(f"fill must be one of {FILLS}, got {fill!r}")
    w = window(bars, entry_after, horizon_sessions, through)
    if len(w) == 0:
        return _empty("NO_DATA", 0, None)
    sessions, last_close = len(w), float(w["close"].iloc[-1])

    if fill == "next_open":
        shift = float(w["open"].iloc[0]) - entry
        entry, stop, target, start = entry + shift, stop + shift, target + shift, 0
    elif fill == "instant":
        start = 0
    else:
        hit = _first_fill(w, entry)
        if hit is None:
            return _empty("NO_FILL", sessions, last_close)
        start = hit

    risk = abs(entry - stop)
    if risk <= 0:
        raise ValueError(f"the stop must differ from the entry; got entry {entry} stop {stop}")
    is_long, fill_date = direction == "long", w["date"].iloc[start]
    mfe = mae = 0.0
    for i in range(start, sessions):
        high, low = float(w["high"].iloc[i]), float(w["low"].iloc[i])
        favourable = (high - entry) if is_long else (entry - low)
        adverse = (entry - low) if is_long else (high - entry)
        mfe, mae = max(mfe, favourable), max(mae, adverse)
        stop_hit = (low <= stop) if is_long else (high >= stop)
        target_hit = (high >= target) if is_long else (low <= target)
        if stop_hit or target_hit:                       # a bar touching both is conservative: LOSS
            outcome = "LOSS" if stop_hit else "WIN"
            r = -1.0 if stop_hit else abs(target - entry) / risk
            return {"outcome": outcome, "r": r, "fill_date": fill_date, "event_date": w["date"].iloc[i],
                    "sessions": sessions, "mfe_r": mfe / risk, "mae_r": mae / risk, "last_close": last_close}
    signed = (last_close - entry) if is_long else (entry - last_close)
    return {"outcome": "OPEN", "r": signed / risk, "fill_date": fill_date, "event_date": None,
            "sessions": sessions, "mfe_r": mfe / risk, "mae_r": mae / risk, "last_close": last_close}


def _intrinsic(leg: dict, spot: float) -> float:
    return max(spot - leg["strike"], 0.0) if leg["right"] == "C" else max(leg["strike"] - spot, 0.0)


def _value(legs: list[dict], spot: float) -> float:
    return sum(leg["side"] * _intrinsic(leg, spot) for leg in legs)


def _check_legs(legs: list[dict]) -> None:
    if len(legs) not in LEG_COUNTS:
        raise ValueError(f"a defined-risk structure has {LEG_COUNTS} legs, got {len(legs)}")
    for leg in legs:
        missing = [k for k in ("right", "strike", "side", "mark") if k not in leg]
        if missing:
            raise ValueError(f"leg {leg} is missing {missing}")
        if leg["right"] not in RIGHTS:
            raise ValueError(f"right must be one of {RIGHTS}, got {leg['right']!r}")
        if int(leg["side"]) not in SIDES:
            raise ValueError(f"side must be +1 (long) or -1 (short), got {leg['side']!r}")


def grade_vertical(legs: list[dict], close_at_expiry: float) -> dict:
    """Intrinsic P&L per share at expiry for a 2-leg vertical or a 4-leg butterfly / condor.

    An iron butterfly and an iron condor are four legs of this same arithmetic, so they grade
    through this function; there is no separate `grade_iron_butterfly`.

    `legs`: `[{right: "C"|"P", strike, side: +1 long / -1 short, mark}]`, `mark` the entry mark per
    share. Only the net of the marks enters the payoff. `max_loss_per_share` is read off the payoff
    curve at 0, at every strike and above the top strike, so it needs no per-family formula;
    `ror = payoff / max_loss`, None when the structure cannot lose.
    """
    _check_legs(legs)
    entry_cost = sum(leg["side"] * leg["mark"] for leg in legs)      # > 0 a net debit, < 0 a net credit
    value = _value(legs, close_at_expiry)
    payoff = value - entry_cost
    strikes = sorted(float(leg["strike"]) for leg in legs)
    probes = [0.0, *strikes, 2 * strikes[-1] + 1.0]
    max_loss = max(0.0, -min(_value(legs, s) - entry_cost for s in probes))
    return {"payoff_per_share": payoff,
            "ror": (payoff / max_loss) if max_loss > 0 else None,
            "max_loss_per_share": max_loss,
            "full_credit": bool(entry_cost < 0 and abs(value) < TOL),
            "at_max_loss": bool(max_loss > 0 and payoff <= -max_loss + TOL)}
