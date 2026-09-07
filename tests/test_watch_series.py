"""engine.watch.series: point-in-time bar-derived conditions. The weekly RSI/divergence path is
an incremental optimisation over the naive "truncate then resample then recompute" approach
(`series.py`'s own docstring claims exact equivalence) -- these tests hold it to that claim by
comparing against a from-scratch reference at many `asof` dates, including mid-week ones where a
lookahead bug would show up first.
"""
from __future__ import annotations

import math
from datetime import date

import pandas as pd
import pytest

from engine.watch import bars as B
from engine.watch import indicators as I
from engine.watch import series as S
from engine.watch.series import _poc_anchored_flags

pytestmark = pytest.mark.unit


def _synthetic_daily(n_days: int = 220, start: str = "2024-01-01") -> pd.DataFrame:
    dates = pd.bdate_range(start, periods=n_days)
    closes = [100.0 + 12.0 * math.sin(i * 0.22) + (i % 9) * 0.6 for i in range(n_days)]
    highs = [c + 1.0 for c in closes]
    lows = [c - 1.0 for c in closes]
    opens = closes
    vols = [1_000.0 + (i % 13) * 25.0 for i in range(n_days)]
    return pd.DataFrame({"date": [d.date() for d in dates], "open": opens, "high": highs,
                          "low": lows, "close": closes, "adj": closes, "volume": vols})


def _naive_weekly_rsi_div(daily: pd.DataFrame, asof: date):
    trunc = B.bars_as_of(daily, asof)
    if trunc.empty:
        return None, None
    wk = B.weekly_bars(trunc)
    closes = list(wk["close"])
    rsi_series = I.wilder_rsi_series(closes, n=I.RSI_PERIOD)
    rsi_last = rsi_series[-1] if rsi_series else None
    div = I.bullish_divergence(closes, rsi_series, lookback=I.DIVERGENCE_LOOKBACK_WEEKS) if closes else None
    return rsi_last, div


def test_build_ticker_series_none_on_empty_bars():
    assert S.build_ticker_series("X", daily=B._empty_bars()) is None


def test_evaluate_bar_conditions_all_none_when_series_is_none():
    out = S.evaluate_bar_conditions(None, date(2026, 1, 1))
    assert all(v is None for v in out.values())


def test_evaluate_bar_conditions_all_none_when_asof_has_no_bar():
    daily = _synthetic_daily(60)
    ts = S.build_ticker_series("X", daily=daily)
    out = S.evaluate_bar_conditions(ts, date(2099, 1, 1))
    assert all(v is None for v in out.values())


@pytest.mark.parametrize("offset", [0, 1, 2, 3, 4, 10, 30])
def test_weekly_rsi_matches_naive_truncate_and_recompute_at_many_asof_points(offset):
    daily = _synthetic_daily(220)
    # pick an asof well into the series, at a few different weekday offsets from a Monday
    base_idx = 150 + offset
    asof = daily["date"].iloc[base_idx]
    ts = S.build_ticker_series("X", daily=daily)
    got_rsi, got_div = S.evaluate_bar_conditions(ts, asof)["rsi_last"], S.evaluate_bar_conditions(ts, asof)["div_flag"]
    want_rsi, want_div = _naive_weekly_rsi_div(daily, asof)
    if want_rsi is None:
        assert got_rsi is None
    else:
        assert got_rsi == pytest.approx(want_rsi, abs=1e-9)
    assert got_div == want_div


def test_weekly_rsi_never_leaks_a_future_session_within_the_current_week():
    # Two series identical through a Wednesday, diverging only on the following Thursday/Friday.
    daily_a = _synthetic_daily(120)
    daily_b = daily_a.copy()
    # flip the sign of the last two closes (Thu/Fri of the final week) to prove they cannot affect
    # an asof of the Wednesday before them
    wed_idx = 112  # chosen so index 113, 114 are Thu/Fri of the same week in this synthetic calendar
    if daily_a["date"].iloc[wed_idx].weekday() != 2:  # pragma: no cover - synthetic calendar guard
        pytest.skip("synthetic calendar shifted; index no longer lands on a Wednesday")
    daily_b.loc[wed_idx + 1:, "close"] = daily_b.loc[wed_idx + 1:, "close"] * 3.0
    asof = daily_a["date"].iloc[wed_idx]
    ts_a = S.build_ticker_series("A", daily=daily_a)
    ts_b = S.build_ticker_series("B", daily=daily_b)
    out_a = S.evaluate_bar_conditions(ts_a, asof)
    out_b = S.evaluate_bar_conditions(ts_b, asof)
    assert out_a["rsi_last"] == pytest.approx(out_b["rsi_last"], abs=1e-9)
    assert out_a["div_flag"] == out_b["div_flag"]


# =============================================================================================
# C-DIV-D: daily RSI bullish divergence, last 20 daily bars (DESIGN/110 §2)
# =============================================================================================


def _naive_daily_div(daily: pd.DataFrame, asof: date):
    trunc = B.bars_as_of(daily, asof)
    if trunc.empty:
        return None
    closes = list(trunc["close"])
    rsi_series = I.wilder_rsi_series(closes, n=I.RSI_PERIOD)
    return I.bullish_divergence(closes, rsi_series, lookback=I.DIVERGENCE_LOOKBACK_DAYS)


@pytest.mark.parametrize("offset", [0, 1, 2, 3, 4, 10, 30])
def test_daily_divergence_matches_naive_truncate_and_recompute_at_many_asof_points(offset):
    daily = _synthetic_daily(220)
    base_idx = 150 + offset
    asof = daily["date"].iloc[base_idx]
    ts = S.build_ticker_series("X", daily=daily)
    got = S.evaluate_bar_conditions(ts, asof)["div_d_flag"]
    want = _naive_daily_div(daily, asof)
    assert got == want


def test_daily_divergence_none_before_rsi_has_warmed_up():
    daily = _synthetic_daily(10)   # fewer than RSI_PERIOD+1 closes -> no daily RSI at all yet
    ts = S.build_ticker_series("X", daily=daily)
    out = S.evaluate_bar_conditions(ts, daily["date"].iloc[-1])
    assert out["div_d_flag"] is None


def test_daily_divergence_never_leaks_a_bar_after_asof():
    daily_a = _synthetic_daily(120)
    daily_b = daily_a.copy()
    idx = 100
    # flip the sign of everything after idx -- must not affect a div_d_flag computed at idx
    daily_b.loc[idx + 1:, "close"] = daily_b.loc[idx + 1:, "close"] * 3.0
    asof = daily_a["date"].iloc[idx]
    ts_a = S.build_ticker_series("A", daily=daily_a)
    ts_b = S.build_ticker_series("B", daily=daily_b)
    out_a = S.evaluate_bar_conditions(ts_a, asof)
    out_b = S.evaluate_bar_conditions(ts_b, asof)
    assert out_a["div_d_flag"] == out_b["div_d_flag"]


def test_swing_pivots_are_point_in_time_and_do_not_use_bars_after_asof():
    # A long, deliberately choppy daily series where later data would otherwise create an
    # additional pivot; check that asof in the middle only sees pivots confirmed by then.
    daily = _synthetic_daily(200)
    ts = S.build_ticker_series("X", daily=daily)
    early_asof = daily["date"].iloc[60]
    idx = 60
    out = S.evaluate_bar_conditions(ts, early_asof)
    active_pivots_direct = [p for p in ts.pivots if p["index"] <= idx]
    # whatever evaluate_bar_conditions computed for swing_up must equal recomputing directly from
    # only the pivots confirmed by index 60 -- i.e. it must not have used a pivot confirmed later
    assert out["swing_up"] == I.swing_structure(active_pivots_direct)
    assert out["swing_down"] == I.swing_structure_loss(active_pivots_direct)


def test_poc_and_avwap_are_none_with_too_little_history():
    daily = _synthetic_daily(10)
    ts = S.build_ticker_series("X", daily=daily)
    out = S.evaluate_bar_conditions(ts, daily["date"].iloc[-1])
    assert out["poc_accept"] is None and out["poc_loss"] is None
    assert out["poc_a_accept"] is None and out["poc_a_loss"] is None  # too little history for even a zigzag pivot


def test_evaluate_bar_conditions_wires_poc_a_flags_through():
    daily = _synthetic_daily(200)
    ts = S.build_ticker_series("X", daily=daily)
    idx = 150
    asof = daily["date"].iloc[idx]
    out = S.evaluate_bar_conditions(ts, asof)
    want_accept, want_loss = _poc_anchored_flags(ts, idx)
    assert out["poc_a_accept"] == want_accept
    assert out["poc_a_loss"] == want_loss


def test_avwap_reclaim_true_after_a_clean_recovery_above_the_low_anchor():
    # 60 sessions: padding, then a long decline into the 52-week low (each new close stays at or
    # below the cumulative AVWAP by construction, since the sequence is non-increasing), then a
    # sharp, sustained rally in only the last 5 sessions that crosses cleanly above it.
    n = 60
    dates = [d.date() for d in pd.bdate_range("2024-01-01", periods=n)]
    padding = [100.0] * 10
    decline = list(pd.Series([99.0 - i * 1.5 for i in range(45)]))   # 99.0 down to ~33.5, the 52w low
    rally = [400.0, 420.0, 440.0, 460.0, 480.0]
    closes = padding + decline + rally
    assert len(closes) == n
    highs = [c + 0.5 for c in closes]
    lows = [c - 0.5 for c in closes]
    vols = [1000.0] * n
    daily = pd.DataFrame({"date": dates, "open": closes, "high": highs, "low": lows,
                           "close": closes, "adj": closes, "volume": vols})
    ts = S.build_ticker_series("X", daily=daily)
    out = S.evaluate_bar_conditions(ts, dates[-1])
    assert out["avwap_reclaim"] is True


# =============================================================================================
# C-POC-A / C-POC-A-LOSS: anchored volume profile, most recent confirmed pivot L / H
# (DESIGN/110 §2). `_poc_anchored_flags` is exercised directly against a hand-built `TickerSeries`
# (bypassing `build_ticker_series`/`zigzag_pivots`) so the confirmed pivot and the bar data are
# both fully controlled -- the only two inputs the function reads.
# =============================================================================================


def _ticker_series(highs, lows, closes, volumes, pivots) -> S.TickerSeries:
    n = len(closes)
    dates = [d.date() for d in pd.bdate_range("2024-01-01", periods=n)]
    return S.TickerSeries(
        ticker="X", dates=dates, highs=highs, lows=lows, closes=closes, volumes=volumes,
        atr_series=[None] * n, daily_rsi=[None] * n, pivots=pivots,
        weekly_week_ids=[], weekly_closes=[], weekly_states=[], weekly_rsi=[],
    )


def test_poc_a_accept_true_after_a_tight_base_above_a_confirmed_pivot_low():
    # index 0: the confirmed pivot LOW (price 95.0, bar range [95.0, 96.0]). Indices 1-19: 19
    # identical "base" bars ([99.5, 100.5], volume 100 each) -- 20 sessions total, exactly
    # POC_ANCHOR_MIN_SESSIONS. Anchor's own volume (10) is negligible next to the base's 1,900, so
    # the profile's POC/value-area sit inside the tight base band: hand-computed (`I.volume_profile`
    # on this exact window) value_area_high = 100.28; the last two closes (100.45) clear it and the
    # range (100.5-95.0)/100.45 = 5.5% is well under the 25% cap.
    highs = [96.0] + [100.5] * 19
    lows = [95.0] + [99.5] * 19
    closes = [95.5] + [100.0] * 17 + [100.45, 100.45]
    vols = [10.0] + [100.0] * 19
    idx = len(closes) - 1
    pivots = [{"index": 0, "date": None, "type": "L", "price": 95.0}]
    ts = _ticker_series(highs, lows, closes, vols, pivots)

    profile = I.volume_profile(pd.DataFrame({"high": highs, "low": lows, "close": closes, "volume": vols}),
                                n_bins=I.VOLUME_PROFILE_BINS, value_area_fraction=I.VALUE_AREA_FRACTION)
    assert profile["value_area_high"] == pytest.approx(100.28, abs=0.01)
    assert all(c > profile["value_area_high"] for c in closes[-2:])
    assert (profile["range_high"] - profile["range_low"]) / closes[-1] <= 0.25

    accept, loss = _poc_anchored_flags(ts, idx)
    assert accept is True
    assert loss is None    # no confirmed pivot H at all


def test_poc_a_loss_true_after_a_tight_base_below_a_confirmed_pivot_high():
    # Mirror: index 0 is the confirmed pivot HIGH (price 104.5), 19 base bars below it, and the
    # last two closes (99.45) fall below the hand-computed value_area_low (99.5).
    highs = [105.0] + [100.5] * 19
    lows = [104.0] + [99.5] * 19
    closes = [104.5] + [100.0] * 17 + [99.45, 99.45]
    vols = [10.0] + [100.0] * 19
    idx = len(closes) - 1
    pivots = [{"index": 0, "date": None, "type": "H", "price": 104.5}]
    ts = _ticker_series(highs, lows, closes, vols, pivots)

    profile = I.volume_profile(pd.DataFrame({"high": highs, "low": lows, "close": closes, "volume": vols}),
                                n_bins=I.VOLUME_PROFILE_BINS, value_area_fraction=I.VALUE_AREA_FRACTION)
    assert profile["value_area_low"] == pytest.approx(99.5, abs=0.01)
    assert all(c < profile["value_area_low"] for c in closes[-2:])

    accept, loss = _poc_anchored_flags(ts, idx)
    assert accept is None   # no confirmed pivot L at all
    assert loss is True


def test_poc_a_none_when_no_confirmed_pivot_of_either_type_exists():
    n = 30
    highs, lows, closes, vols = [100.0] * n, [99.0] * n, [99.5] * n, [10.0] * n
    ts = _ticker_series(highs, lows, closes, vols, pivots=[])
    accept, loss = _poc_anchored_flags(ts, n - 1)
    assert accept is None and loss is None


def test_poc_a_none_when_the_anchored_window_is_shorter_than_the_minimum():
    # 25 bars; the confirmed pivot L sits at index 19 -> window through idx 24 is only 6 sessions,
    # short of POC_ANCHOR_MIN_SESSIONS (20).
    n = 25
    highs, lows, closes, vols = [100.0] * n, [99.0] * n, [99.5] * n, [10.0] * n
    pivots = [{"index": 19, "date": None, "type": "L", "price": 99.0}]
    ts = _ticker_series(highs, lows, closes, vols, pivots)
    accept, loss = _poc_anchored_flags(ts, n - 1)
    assert accept is None


def test_poc_a_none_when_the_anchored_window_is_longer_than_the_maximum():
    # 300 bars; the only confirmed pivot L is at index 0 -> window through the last bar is 300
    # sessions, past POC_ANCHOR_MAX_SESSIONS (252).
    n = 300
    highs, lows, closes, vols = [100.0] * n, [99.0] * n, [99.5] * n, [10.0] * n
    pivots = [{"index": 0, "date": None, "type": "L", "price": 99.0}]
    ts = _ticker_series(highs, lows, closes, vols, pivots)
    accept, loss = _poc_anchored_flags(ts, n - 1)
    assert accept is None


def test_poc_a_window_boundaries_are_inclusive_at_20_and_252_sessions():
    # Exactly POC_ANCHOR_MIN_SESSIONS (20) must NOT be rejected as "too short".
    n = 20
    highs, lows, closes, vols = [96.0] + [100.5] * (n - 1), [95.0] + [99.5] * (n - 1), \
        [95.5] + [100.0] * (n - 2) + [100.45], [10.0] + [100.0] * (n - 1)
    pivots = [{"index": 0, "date": None, "type": "L", "price": 95.0}]
    ts = _ticker_series(highs, lows, closes, vols, pivots)
    accept, _ = _poc_anchored_flags(ts, n - 1)
    assert accept is not None      # not rejected purely on window length

    # Exactly POC_ANCHOR_MAX_SESSIONS (252) must NOT be rejected as "too long" either.
    n2 = 252
    highs2 = [96.0] + [100.5] * (n2 - 1)
    lows2 = [95.0] + [99.5] * (n2 - 1)
    closes2 = [95.5] + [100.0] * (n2 - 2) + [100.45]
    vols2 = [10.0] + [100.0] * (n2 - 1)
    pivots2 = [{"index": 0, "date": None, "type": "L", "price": 95.0}]
    ts2 = _ticker_series(highs2, lows2, closes2, vols2, pivots2)
    accept2, _ = _poc_anchored_flags(ts2, n2 - 1)
    assert accept2 is not None

    # One session past the ceiling (253) must fall back to None.
    n3 = 253
    highs3 = [96.0] + [100.5] * (n3 - 1)
    lows3 = [95.0] + [99.5] * (n3 - 1)
    closes3 = [95.5] + [100.0] * (n3 - 2) + [100.45]
    vols3 = [10.0] + [100.0] * (n3 - 1)
    pivots3 = [{"index": 0, "date": None, "type": "L", "price": 95.0}]
    ts3 = _ticker_series(highs3, lows3, closes3, vols3, pivots3)
    accept3, _ = _poc_anchored_flags(ts3, n3 - 1)
    assert accept3 is None


def test_poc_a_picks_the_most_recent_confirmed_pivot_of_each_type():
    # Two confirmed L pivots and one H pivot; the anchor must be the LAST L (index 15), not the
    # first (index 0) -- proven by a window-length check: anchoring at index 0 would give a
    # 30-session window, anchoring at index 15 gives 15 (too short, so accept must be None here).
    n = 30
    highs, lows, closes, vols = [100.0] * n, [99.0] * n, [99.5] * n, [10.0] * n
    pivots = [
        {"index": 0, "date": None, "type": "L", "price": 90.0},
        {"index": 8, "date": None, "type": "H", "price": 110.0},
        {"index": 15, "date": None, "type": "L", "price": 95.0},
    ]
    ts = _ticker_series(highs, lows, closes, vols, pivots)
    accept, _ = _poc_anchored_flags(ts, n - 1)
    assert accept is None   # anchored at index 15 (the most recent L): window is 15 sessions, < 20


def test_poc_a_ignores_pivots_not_yet_confirmed_at_idx():
    # A confirmed L at index 0 and a LATER L at index 25 that has not happened yet as of idx=19 --
    # evaluate_bar_conditions/​_poc_anchored_flags must only see pivots with index <= idx.
    n = 30
    highs = [96.0] + [100.5] * 19 + [100.0] * 10
    lows = [95.0] + [99.5] * 19 + [99.0] * 10
    closes = [95.5] + [100.0] * 17 + [100.45, 100.45] + [99.5] * 10
    vols = [10.0] * n
    pivots = [
        {"index": 0, "date": None, "type": "L", "price": 95.0},
        {"index": 25, "date": None, "type": "L", "price": 50.0},
    ]
    ts = _ticker_series(highs, lows, closes, vols, pivots)
    idx = 19  # before index 25's pivot is confirmed
    accept, _ = _poc_anchored_flags(ts, idx)
    assert accept is True   # anchored at index 0 (the only pivot visible at idx=19), window 20
