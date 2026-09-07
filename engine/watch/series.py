"""Point-in-time bar-derived conditions -- RSI, divergence, anchored VWAP, volume profile
acceptance, swing structure (`DESIGN/110-watch-basket.md` §2) -- built once per ticker over its
full cached daily-bar history and evaluated cheaply at every panel night that ticker qualifies
for.

Every daily technique here is "online": a Wilder ATR state or a confirmed zigzag pivot at index
`i` depends only on `bars[0..i]`, never on bars after `i` (see `indicators.py`'s own docstrings),
so computing each series ONCE over the full history and reading off a point-in-time slice gives
the exact same answer as truncating the bars and recomputing from scratch at every one of a
ticker's ~100 nights -- for a fraction of the cost.

The weekly series (RSI, divergence) is the one place that needs care: naively resampling the full
history would let the in-progress week's bar see days after `asof`. `TickerSeries.weekly_*` holds
only fully-completed weeks; `evaluate_bar_conditions` splices in a single synthetic "partial
current week" (its close is just `asof`'s own daily close) on top of the last completed week's
saved Wilder state, which is exactly one more incremental step -- never a lookahead.

The daily divergence (C-DIV-D, DESIGN/110 §2) needs no such splicing: `TickerSeries.daily_rsi` is
already a full-history, index-aligned Wilder RSI-14 on the daily closes themselves (online by
construction, like `atr_series`), so `_daily_divergence` just slices the trailing window up to
`idx` and calls the same `indicators.bullish_divergence` C-DIV uses.
"""
from __future__ import annotations

import bisect
from dataclasses import dataclass
from datetime import date

import pandas as pd

from engine.watch import bars as B
from engine.watch import conditions as C
from engine.watch import indicators as I

LOOKBACK_52W_SESSIONS = 252   # trading sessions, ~1 year (chart.py's own w52() uses a 1y range)


def _iso_week_id(d: date) -> tuple[int, int]:
    y, w, _ = d.isocalendar()
    return (y, w)


@dataclass(frozen=True)
class TickerSeries:
    ticker: str
    dates: list                                    # daily, ascending
    highs: list[float]
    lows: list[float]
    closes: list[float]
    volumes: list[float]
    atr_series: list[float | None]                  # daily Wilder ATR-14
    daily_rsi: list[float | None]                    # daily Wilder RSI-14, C-DIV-D
    pivots: list[dict]                               # full-history zigzag pivots
    weekly_week_ids: list[tuple[int, int]]           # COMPLETED weeks only, ascending
    weekly_closes: list[float]
    weekly_states: list[tuple[float, float] | None]  # Wilder (avg_gain, avg_loss) per completed week
    weekly_rsi: list[float | None]


def build_ticker_series(ticker: str, daily: pd.DataFrame | None = None) -> TickerSeries | None:
    """`None` when the ticker has no cached/fetchable bars at all (`bars.load_daily_bars` failed
    soft) -- every bar-derived condition is then `None` for that ticker on every night."""
    daily = B.load_daily_bars(ticker) if daily is None else daily
    if daily is None or daily.empty:
        return None
    dates = list(daily["date"])
    highs = [float(x) for x in daily["high"]]
    lows = [float(x) for x in daily["low"]]
    closes = [float(x) for x in daily["close"]]
    volumes = [float(x) for x in daily["volume"]]
    atr_series = I.wilder_atr_series(highs, lows, closes, n=I.ATR_PERIOD)
    daily_rsi = I.wilder_rsi_series(closes, n=I.RSI_PERIOD)
    pivots = I.zigzag_pivots(dates, highs, lows, atr_series, reversal_mult=I.ZIGZAG_REVERSAL_MULT)

    weekly = B.weekly_bars(daily)
    weekly_week_ids = [_iso_week_id(d) for d in weekly["week_end"]]
    weekly_closes = [float(x) for x in weekly["close"]]
    weekly_states = I.wilder_state_series(weekly_closes, n=I.RSI_PERIOD)
    weekly_rsi = [I.rsi_from_state(*s) if s is not None else None for s in weekly_states]

    return TickerSeries(ticker=ticker, dates=dates, highs=highs, lows=lows, closes=closes,
                         volumes=volumes, atr_series=atr_series, daily_rsi=daily_rsi, pivots=pivots,
                         weekly_week_ids=weekly_week_ids, weekly_closes=weekly_closes,
                         weekly_states=weekly_states, weekly_rsi=weekly_rsi)


def _avwap_flag(ts: TickerSeries, anchor_idx: int, idx: int, want_above: bool) -> bool | None:
    sub = pd.DataFrame({
        "high": ts.highs[anchor_idx:idx + 1], "low": ts.lows[anchor_idx:idx + 1],
        "close": ts.closes[anchor_idx:idx + 1], "volume": ts.volumes[anchor_idx:idx + 1],
    })
    vwap = I.anchored_vwap_series(sub)
    side = []
    for c, v in zip(sub["close"], vwap):
        if v != v:  # NaN AVWAP (zero cumulative volume so far) -- can't classify this session
            side.append(False)
            continue
        side.append(bool(c > v) if want_above else bool(c < v))
    return I.crossed_within(side, lookback=C.C_AVWAP_LOOKBACK_SESSIONS)


def _poc_flags(ts: TickerSeries, idx: int) -> tuple[bool | None, bool | None]:
    window_n = I.VOLUME_PROFILE_WINDOW
    if idx < window_n - 1:
        return None, None
    start = idx - window_n + 1
    window = pd.DataFrame({"high": ts.highs[start:idx + 1], "low": ts.lows[start:idx + 1],
                            "close": ts.closes[start:idx + 1], "volume": ts.volumes[start:idx + 1]})
    profile = I.volume_profile(window, n_bins=I.VOLUME_PROFILE_BINS,
                                value_area_fraction=I.VALUE_AREA_FRACTION)
    if profile is None:
        return None, None
    close_now = ts.closes[idx]
    if not close_now:
        return None, None
    range_frac = (profile["range_high"] - profile["range_low"]) / close_now
    range_ok = range_frac <= C.C_POC_MAX_RANGE_FRACTION
    n_accept = C.C_POC_ACCEPTANCE_SESSIONS
    if idx - n_accept + 1 < 0:
        return None, None
    recent = ts.closes[idx - n_accept + 1: idx + 1]
    above = all(c > profile["value_area_high"] for c in recent)
    below = all(c < profile["value_area_low"] for c in recent)
    return bool(range_ok and above), bool(range_ok and below)


def _weekly_rsi_and_divergence(ts: TickerSeries, idx: int, asof: date) -> tuple[float | None, bool | None]:
    week_id = _iso_week_id(asof)
    prev_idx = bisect.bisect_left(ts.weekly_week_ids, week_id) - 1  # last COMPLETED week before asof's week
    if prev_idx < 0 or ts.weekly_states[prev_idx] is None:
        return None, None
    prev_close = ts.weekly_closes[prev_idx]
    partial_close = ts.closes[idx]
    avg_gain, avg_loss = ts.weekly_states[prev_idx]
    n = I.RSI_PERIOD
    gain, loss = max(partial_close - prev_close, 0.0), max(prev_close - partial_close, 0.0)
    new_avg_gain = (avg_gain * (n - 1) + gain) / n
    new_avg_loss = (avg_loss * (n - 1) + loss) / n
    rsi_asof = I.rsi_from_state(new_avg_gain, new_avg_loss)

    lookback = I.DIVERGENCE_LOOKBACK_WEEKS
    start = max(0, prev_idx - (lookback - 2))
    closes_seq = ts.weekly_closes[start:prev_idx + 1] + [partial_close]
    rsi_seq = ts.weekly_rsi[start:prev_idx + 1] + [rsi_asof]
    div_flag = I.bullish_divergence(closes_seq, rsi_seq, lookback=lookback)
    return rsi_asof, div_flag


def _daily_divergence(ts: TickerSeries, idx: int) -> bool | None:
    """C-DIV-D (DESIGN/110 §2): the same `bullish_divergence` rule as C-DIV, but directly on the
    daily closes/RSI already carried by `ts` -- unlike the weekly path, daily Wilder RSI at index
    `idx` already depends only on `bars[0..idx]` (no in-progress-bar splicing needed), so this is
    just a bounded, point-in-time-safe slice of the two full-history series already computed once
    in `build_ticker_series`."""
    lookback = I.DIVERGENCE_LOOKBACK_DAYS
    start = max(0, idx - lookback + 1)
    closes_seq = ts.closes[start:idx + 1]
    rsi_seq = ts.daily_rsi[start:idx + 1]
    return I.bullish_divergence(closes_seq, rsi_seq, lookback=lookback)


def evaluate_bar_conditions(ts: TickerSeries | None, asof: date) -> dict:
    """`{rsi_last, div_flag, div_d_flag, avwap_reclaim, avwap_loss, poc_accept, poc_loss, swing_up,
    swing_down}`, every value `None` when `ts` is `None` or has no bar exactly on `asof`."""
    out = {"rsi_last": None, "div_flag": None, "div_d_flag": None, "avwap_reclaim": None,
           "avwap_loss": None, "poc_accept": None, "poc_loss": None, "swing_up": None,
           "swing_down": None}
    if ts is None:
        return out
    idx = bisect.bisect_left(ts.dates, asof)
    if idx >= len(ts.dates) or ts.dates[idx] != asof:
        return out

    active_pivots = [p for p in ts.pivots if p["index"] <= idx]
    out["swing_up"] = I.swing_structure(active_pivots)
    out["swing_down"] = I.swing_structure_loss(active_pivots)

    win_start = max(0, idx - LOOKBACK_52W_SESSIONS + 1)
    lo_slice, hi_slice = ts.lows[win_start:idx + 1], ts.highs[win_start:idx + 1]
    low_anchor = win_start + min(range(len(lo_slice)), key=lambda i: lo_slice[i])
    high_anchor = win_start + max(range(len(hi_slice)), key=lambda i: hi_slice[i])
    out["avwap_reclaim"] = _avwap_flag(ts, low_anchor, idx, want_above=True)
    out["avwap_loss"] = _avwap_flag(ts, high_anchor, idx, want_above=False)

    out["poc_accept"], out["poc_loss"] = _poc_flags(ts, idx)
    out["rsi_last"], out["div_flag"] = _weekly_rsi_and_divergence(ts, idx, asof)
    out["div_d_flag"] = _daily_divergence(ts, idx)
    return out
