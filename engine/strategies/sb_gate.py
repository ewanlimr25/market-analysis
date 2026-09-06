"""The S-B gate (DESIGN/80 §2), read at the prior session's close.

G1  term structure in contango:      VIX3M[t-1] > VIX[t-1]
G2  level above its 20-session median: X[t-1] > median(X[t-21 .. t-2]), X = VIX (SPY) or VXN (QQQ)

ON iff G1 and G2. Any missing input makes the gate UNKNOWN, which fails closed in every mode.
`is_on(state, mode)` serves the descriptive tables (`both`, `g1`, `g2`, `off`; §6.6).
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import date

import pandas as pd

from engine.config import SBParams

GATE_ON = "ON"
GATE_MODES = ("both", "g1", "g2", "off")


@dataclass(frozen=True)
class GateState:
    date: date                     # the entry session t
    asof: date | None              # the session whose closes were used (t - 1)
    vix: float | None
    vix3m: float | None
    x: float | None                # the level series for the underlying at asof
    x_median: float | None         # median of the 20 sessions before asof
    contango: bool | None
    level_ok: bool | None
    on: bool
    known: bool
    reason: str


def _unknown(t: date, why: str, asof: date | None = None) -> GateState:
    return GateState(t, asof, None, None, None, None, None, None, False, False, f"UNKNOWN:{why}")


def _finite(v) -> float | None:
    try:
        f = float(v)
    except (TypeError, ValueError):
        return None
    return None if math.isnan(f) else f


def gate(index_vol: pd.DataFrame, t: date, prev: date, x_col: str, params: SBParams) -> GateState:
    """Evaluate the gate for entry session `t` from the row at `prev` (its prior session)."""
    if index_vol is None or index_vol.empty:
        return _unknown(t, "no index-vol data")
    if prev >= t:
        return _unknown(t, "prev is not before t", prev)
    if x_col not in index_vol.columns:
        return _unknown(t, f"no column {x_col}", prev)
    dates = index_vol["date"].tolist()
    try:
        i = dates.index(prev)
    except ValueError:
        return _unknown(t, f"no row for {prev}", prev)
    window = index_vol.iloc[max(0, i - params.median_window):i]
    if len(window) < params.median_window:
        return _unknown(t, f"window has {len(window)} of {params.median_window} sessions", prev)
    row = index_vol.iloc[i]
    vix, vix3m, x = _finite(row["vix"]), _finite(row["vix3m"]), _finite(row[x_col])
    if vix is None or vix3m is None or x is None:
        return _unknown(t, f"null input at {prev}", prev)
    win = pd.to_numeric(window[x_col], errors="coerce")
    if win.isna().any():
        return _unknown(t, "null in the median window", prev)
    x_median = float(win.median())
    contango, level_ok = vix3m > vix, x > x_median
    on = contango and level_ok
    failed = [name for name, ok in (("G1", contango), ("G2", level_ok)) if not ok]
    reason = GATE_ON if on else "OFF:" + ",".join(failed)
    return GateState(t, prev, vix, vix3m, x, x_median, contango, level_ok, on, True, reason)


def is_on(state: GateState, mode: str = "both") -> bool:
    """Whether an entry is allowed under the given mode; UNKNOWN is never allowed."""
    if mode not in GATE_MODES:
        raise ValueError(f"mode must be one of {GATE_MODES}, got {mode!r}")
    if not state.known:
        return False
    if mode == "both":
        return state.on
    if mode == "g1":
        return bool(state.contango)
    if mode == "g2":
        return bool(state.level_ok)
    return True
