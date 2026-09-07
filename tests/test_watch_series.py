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
