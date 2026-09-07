"""Pure technical indicators for the watch basket (`DESIGN/110-watch-basket.md` §2).

Every function here takes plain sequences or a bars DataFrame (columns at least `date`, `high`,
`low`, `close`, `volume`) and returns numbers, `None`, or small dicts/lists of dicts -- no I/O, no
mart access, so each is directly hand-computable in a test. Callers (`conditions.py`, `retro.py`)
are responsible for passing an already point-in-time-safe slice (`bars.bars_as_of`).
"""
from __future__ import annotations

import math
from datetime import date

import numpy as np
import pandas as pd

RSI_PERIOD = 14
ATR_PERIOD = 14
ZIGZAG_REVERSAL_MULT = 2.0          # DESIGN/110 §2 C-SWING/C-SWING-LOSS
VOLUME_PROFILE_WINDOW = 60          # sessions, DESIGN/110 §2 C-POC/C-POC-LOSS
VOLUME_PROFILE_BINS = 50
VALUE_AREA_FRACTION = 0.70
AVWAP_LOOKBACK_SESSIONS = 5         # DESIGN/110 §2 C-AVWAP/C-AVWAP-LOSS "within the last 5 sessions"
DIVERGENCE_LOOKBACK_WEEKS = 8       # DESIGN/110 §2 C-DIV
DIVERGENCE_LOOKBACK_DAYS = 20       # DESIGN/110 §2 C-DIV-D


def _nan(x) -> bool:
    return x is None or (isinstance(x, float) and math.isnan(x))


# =============================================================================================
# RSI (Wilder), ATR (Wilder)
# =============================================================================================


def rsi_from_state(avg_gain: float, avg_loss: float) -> float:
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return 100.0 - 100.0 / (1.0 + rs)


def wilder_state_series(closes: list[float], n: int = RSI_PERIOD) -> list[tuple[float, float] | None]:
    """One `(avg_gain, avg_loss)` Wilder smoothing state per close, index-aligned; `None` before
    there are `n` deltas. Exposed (not just `wilder_rsi_series`) so a caller with a fixed
    completed-history prefix and a single new observation (`series.py`'s point-in-time weekly
    evaluation) can apply one more incremental step without recomputing the whole series --
    Wilder's recursion depends only on the running state and the next delta, never on the future."""
    out: list[tuple[float, float] | None] = [None] * len(closes)
    if len(closes) <= n:
        return out
    gains = [max(closes[i] - closes[i - 1], 0.0) for i in range(1, len(closes))]
    losses = [max(closes[i - 1] - closes[i], 0.0) for i in range(1, len(closes))]
    avg_gain = sum(gains[:n]) / n
    avg_loss = sum(losses[:n]) / n
    out[n] = (avg_gain, avg_loss)
    for i in range(n, len(gains)):
        avg_gain = (avg_gain * (n - 1) + gains[i]) / n
        avg_loss = (avg_loss * (n - 1) + losses[i]) / n
        out[i + 1] = (avg_gain, avg_loss)
    return out


def wilder_rsi_series(closes: list[float], n: int = RSI_PERIOD) -> list[float | None]:
    """One Wilder RSI value per close, index-aligned; `None` before there are `n` deltas (i.e.
    fewer than `n + 1` closes). Matches `scripts/chart.py:rsi14`'s formula on the last value."""
    return [rsi_from_state(*s) if s is not None else None for s in wilder_state_series(closes, n)]


def wilder_atr_series(highs: list[float], lows: list[float], closes: list[float],
                       n: int = ATR_PERIOD) -> list[float | None]:
    """One Wilder ATR value per bar, index-aligned; `None` for the first `n` bars (need `n` true
    ranges, and a true range needs a previous close, so the first true range is at index 1)."""
    m = len(closes)
    out: list[float | None] = [None] * m
    if m <= n:
        return out
    trs = [max(highs[i] - lows[i], abs(highs[i] - closes[i - 1]), abs(lows[i] - closes[i - 1]))
           for i in range(1, m)]
    atr = sum(trs[:n]) / n
    out[n] = atr
    for i in range(n, len(trs)):
        atr = (atr * (n - 1) + trs[i]) / n
        out[i + 1] = atr
    return out


# =============================================================================================
# ATR zigzag pivots (2x ATR reversal)
# =============================================================================================


def zigzag_pivots(dates: list, highs: list[float], lows: list[float],
                   atr_series: list[float | None],
                   reversal_mult: float = ZIGZAG_REVERSAL_MULT) -> list[dict]:
    """Single-pass ATR-trailing zigzag. Each bar extends the running extreme in the current
    direction; a pivot confirms once price retraces `reversal_mult * ATR[i]` from that extreme,
    and the direction flips. Returns confirmed pivots only (the always-alternating tail is never
    speculative) as `[{"index": i, "date": d, "type": "H"|"L", "price": p}, ...]`, oldest first.

    The initial direction is undetermined until the first `reversal_mult * ATR` swing from the
    first usable bar; that first swing yields the first pivot (the *other* end of the swing, i.e.
    the un-moved side), matching the same trailing-extreme logic used for every later pivot.
    """
    n = len(highs)
    start = next((i for i, a in enumerate(atr_series) if a is not None), None)
    if start is None or start >= n - 1:
        return []

    pivots: list[dict] = []
    anchor_idx, anchor_price = start, (highs[start] + lows[start]) / 2.0
    run_max, run_max_idx = highs[start], start
    run_min, run_min_idx = lows[start], start
    direction = 0  # 0 undetermined, 1 up (extreme is a running high), -1 down (extreme is a low)
    ext_idx, ext_price = start, anchor_price

    for i in range(start + 1, n):
        atr = atr_series[i]
        if atr is None:
            continue
        threshold = reversal_mult * atr
        if highs[i] > run_max:
            run_max, run_max_idx = highs[i], i
        if lows[i] < run_min:
            run_min, run_min_idx = lows[i], i

        if direction == 0:
            if run_max - anchor_price >= threshold and run_max_idx > anchor_idx:
                pivots.append({"index": anchor_idx, "date": dates[anchor_idx], "type": "L",
                                "price": anchor_price})
                direction, ext_idx, ext_price = 1, run_max_idx, run_max
                run_min, run_min_idx = run_max, run_max_idx
            elif anchor_price - run_min >= threshold and run_min_idx > anchor_idx:
                pivots.append({"index": anchor_idx, "date": dates[anchor_idx], "type": "H",
                                "price": anchor_price})
                direction, ext_idx, ext_price = -1, run_min_idx, run_min
                run_max, run_max_idx = run_min, run_min_idx
        elif direction == 1:
            if highs[i] > ext_price:
                ext_price, ext_idx = highs[i], i
            elif ext_price - lows[i] >= threshold:
                pivots.append({"index": ext_idx, "date": dates[ext_idx], "type": "H", "price": ext_price})
                direction, ext_idx, ext_price = -1, i, lows[i]
        elif direction == -1:
            if lows[i] < ext_price:
                ext_price, ext_idx = lows[i], i
            elif highs[i] - ext_price >= threshold:
                pivots.append({"index": ext_idx, "date": dates[ext_idx], "type": "L", "price": ext_price})
                direction, ext_idx, ext_price = 1, i, highs[i]
    return pivots


def swing_structure(pivots: list[dict]) -> bool | None:
    """`True` when the last three confirmed pivots are Low, High, Low with the second Low priced
    above the first (a "higher low ... higher high ... higher low" improving structure,
    DESIGN/110 §2 C-SWING). `False` when three pivots exist but do not show that pattern (either
    the alternating type sequence is H, L, H, or the closing low is not higher). `None` when
    fewer than three pivots are confirmed yet -- not enough structure to judge."""
    if len(pivots) < 3:
        return None
    p1, p2, p3 = pivots[-3], pivots[-2], pivots[-1]
    if p1["type"] == "L" and p2["type"] == "H" and p3["type"] == "L":
        return bool(p3["price"] > p1["price"])
    return False


def swing_structure_loss(pivots: list[dict]) -> bool | None:
    """Mirror of `swing_structure`: last three pivots High, Low, High with the second High priced
    below the first (DESIGN/110 §2 C-SWING-LOSS)."""
    if len(pivots) < 3:
        return None
    p1, p2, p3 = pivots[-3], pivots[-2], pivots[-1]
    if p1["type"] == "H" and p2["type"] == "L" and p3["type"] == "H":
        return bool(p3["price"] < p1["price"])
    return False


# =============================================================================================
# Anchored VWAP
# =============================================================================================


def anchored_vwap_series(bars_from_anchor: pd.DataFrame) -> pd.Series:
    """Cumulative volume-weighted average of the typical price `(H+L+C)/3`, from the first row of
    `bars_from_anchor` (the anchor session, inclusive) through its last. Index-aligned to
    `bars_from_anchor`'s row order; `NaN` where cumulative volume is zero."""
    if bars_from_anchor.empty:
        return pd.Series([], dtype="float64")
    typical = (bars_from_anchor["high"] + bars_from_anchor["low"] + bars_from_anchor["close"]) / 3.0
    cum_pv = (typical * bars_from_anchor["volume"]).cumsum()
    cum_v = bars_from_anchor["volume"].cumsum()
    return cum_pv / cum_v.replace(0, np.nan)


def crossed_within(above: list[bool], lookback: int = AVWAP_LOOKBACK_SESSIONS) -> bool | None:
    """`above`: whether each session (oldest first, last element = "as of" session) closed above
    (or, for the mirror condition, below) its reference line. `True` when the last element is
    `True` and the most recent `False` session (the last time it was NOT above) sits within
    `lookback` sessions of the end -- i.e. the cross happened recently, not merely persisted from
    before the visible window. `None` when there is no data at all."""
    if not above:
        return None
    if not above[-1]:
        return False
    last_below = next((i for i in range(len(above) - 2, -1, -1) if not above[i]), None)
    if last_below is None:
        return False  # above for the whole visible window: no recent crossing event to point to
    sessions_since = (len(above) - 1) - last_below
    return sessions_since <= lookback


# =============================================================================================
# 60-session volume profile: POC and the 70% value area
# =============================================================================================


def volume_profile(window: pd.DataFrame, n_bins: int = VOLUME_PROFILE_BINS,
                    value_area_fraction: float = VALUE_AREA_FRACTION) -> dict | None:
    """`window`: the trailing bars (columns `high`, `low`, `close`, `volume`) the profile is built
    over. Each bar's volume is spread uniformly across the price bins its `[low, high]` range
    overlaps (a degenerate zero-range or zero-volume bar dumps its volume in the bin containing
    its close). Returns `None` when the window is empty or has zero price range.

    `poc`: the bin center with the most volume. `value_area_low/high`: expand outward from the
    POC bin, always adding whichever adjacent bin carries more volume next, until at least
    `value_area_fraction` of total volume is covered.
    """
    if window.empty:
        return None
    lo, hi = float(window["low"].min()), float(window["high"].max())
    if not (hi > lo):
        return None
    edges = np.linspace(lo, hi, n_bins + 1)
    bin_vol = np.zeros(n_bins)
    for h, l, c, v in zip(window["high"], window["low"], window["close"], window["volume"]):
        v = float(v) if v == v else 0.0
        if v <= 0:
            continue
        if not (h > l):
            idx = min(max(int((c - lo) / (hi - lo) * n_bins), 0), n_bins - 1)
            bin_vol[idx] += v
            continue
        first_bin = max(int(np.floor((l - lo) / (hi - lo) * n_bins)), 0)
        last_bin = min(int(np.floor((h - lo) / (hi - lo) * n_bins - 1e-12)), n_bins - 1)
        for b in range(first_bin, last_bin + 1):
            overlap = max(0.0, min(h, edges[b + 1]) - max(l, edges[b]))
            bin_vol[b] += v * (overlap / (h - l))

    total = bin_vol.sum()
    if total <= 0:
        return None
    poc_bin = int(np.argmax(bin_vol))
    lo_i = hi_i = poc_bin
    covered = bin_vol[poc_bin]
    target = value_area_fraction * total
    while covered < target and (lo_i > 0 or hi_i < n_bins - 1):
        left = bin_vol[lo_i - 1] if lo_i > 0 else -1.0
        right = bin_vol[hi_i + 1] if hi_i < n_bins - 1 else -1.0
        if right >= left:
            hi_i += 1
            covered += bin_vol[hi_i]
        else:
            lo_i -= 1
            covered += bin_vol[lo_i]
    return {
        "poc": float((edges[poc_bin] + edges[poc_bin + 1]) / 2.0),
        "value_area_low": float(edges[lo_i]),
        "value_area_high": float(edges[hi_i + 1]),
        "range_low": lo, "range_high": hi,
    }


# =============================================================================================
# RSI bullish divergence (weekly, last 8 bars; also reused daily, last 20 bars, for C-DIV-D)
# =============================================================================================


def bullish_divergence(closes: list[float], rsi_values: list[float | None],
                        lookback: int = DIVERGENCE_LOOKBACK_WEEKS) -> bool | None:
    """DESIGN/110 §2 C-DIV: "over the last 8 weekly bars: a lower low in close with a higher low
    in RSI" -- and, with `lookback=DIVERGENCE_LOOKBACK_DAYS` on daily closes and daily RSI(14),
    C-DIV-D's "same halves rule ... over the last 20 daily bars" (same function, no new algorithm).
    Operationalised as: split the trailing `lookback` bars into an earlier and a later
    half (later half gets the extra bar on an odd split); `low1` = the earlier half's minimum
    close, `low2` = the later half's minimum close. Divergence is `close[low2] < close[low1]`
    (price makes a lower low) AND `rsi[low2] > rsi[low1]` (RSI makes a higher low). `None` when
    fewer than 4 bars are available (too few to split into two comparable halves) or any of the
    four values needed is missing (an RSI series that has not warmed up yet)."""
    n = min(lookback, len(closes))
    if n < 4:
        return None
    c = closes[-n:]
    r = rsi_values[-n:]
    half = n // 2
    first_c, first_r = c[:half], r[:half]
    second_c, second_r = c[half:], r[half:]
    if any(_nan(x) for x in first_r) or any(_nan(x) for x in second_r):
        return None
    i1 = min(range(half), key=lambda i: first_c[i])
    i2 = min(range(len(second_c)), key=lambda i: second_c[i])
    low1_close, low1_rsi = first_c[i1], first_r[i1]
    low2_close, low2_rsi = second_c[i2], second_r[i2]
    return bool(low2_close < low1_close and low2_rsi > low1_rsi)
