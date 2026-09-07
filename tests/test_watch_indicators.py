"""engine.watch.indicators: RSI (Wilder), ATR (Wilder), ATR-zigzag pivots, swing structure,
anchored VWAP, crossed-within, 60-session volume profile, RSI bullish divergence
(DESIGN/110-watch-basket.md §2). Every case here is worked by hand in the test body or docstring."""
from __future__ import annotations

from datetime import date

import pandas as pd
import pytest

from engine.watch import indicators as I

pytestmark = pytest.mark.unit


# =============================================================================================
# RSI (Wilder)
# =============================================================================================


def test_wilder_rsi_series_too_short_is_all_none():
    assert I.wilder_rsi_series([1.0, 2.0], n=14) == [None, None]


def test_wilder_rsi_series_hand_computed_with_n_2():
    # gains=[1,0,2] losses=[0,1,0]; avg_gain0=(1+0)/2=.5 avg_loss0=(0+1)/2=.5 -> RSI=50
    # avg_gain1=(.5*1+2)/2=1.25 avg_loss1=(.5*1+0)/2=.25 -> RS=5 -> RSI=100-100/6=83.3333...
    out = I.wilder_rsi_series([10.0, 11.0, 10.0, 12.0], n=2)
    assert out[0] is None and out[1] is None
    assert out[2] == pytest.approx(50.0)
    assert out[3] == pytest.approx(83.33333333, abs=1e-6)


def test_wilder_rsi_series_all_gains_is_100():
    closes = [float(x) for x in range(1, 16)]  # monotone increasing, n=14
    out = I.wilder_rsi_series(closes, n=14)
    assert out[14] == pytest.approx(100.0)


# =============================================================================================
# ATR (Wilder)
# =============================================================================================


def test_wilder_atr_series_hand_computed_with_n_1():
    highs = [10, 12, 11]
    lows = [8, 9, 9]
    closes = [9, 11, 10]
    # tr[1] = max(12-9=3, |12-9|=3, |9-9|=0) = 3 -> atr[1] = 3
    # tr[2] = max(11-9=2, |11-11|=0, |9-11|=2) = 2 -> atr[2] = (3*0+2)/1 = 2
    out = I.wilder_atr_series(highs, lows, closes, n=1)
    assert out == [None, pytest.approx(3.0), pytest.approx(2.0)]


def test_wilder_atr_series_too_short_is_all_none():
    assert I.wilder_atr_series([1, 2], [1, 2], [1, 2], n=14) == [None, None]


# =============================================================================================
# ATR zigzag pivots + swing structure
# =============================================================================================


def _dates(n):
    return [date(2026, 1, 1 + i) for i in range(n)]


def test_zigzag_pivots_hand_computed_two_pivots():
    dates = _dates(6)
    highs = [10, 10, 10, 15, 15, 8]
    lows = [10, 10, 10, 10, 10, 8]
    atr_series = [None, 1, 1, 1, 1, 1]  # threshold = 2*ATR = 2 throughout
    pivots = I.zigzag_pivots(dates, highs, lows, atr_series, reversal_mult=2.0)
    assert [(p["type"], p["index"], p["price"]) for p in pivots] == [
        ("L", 1, 10.0), ("H", 3, 15.0),
    ]


def test_zigzag_pivots_no_atr_data_is_empty():
    dates = _dates(3)
    assert I.zigzag_pivots(dates, [1, 2, 3], [1, 2, 3], [None, None, None]) == []


def test_swing_structure_higher_low_higher_high_higher_low_is_true():
    pivots = [{"type": "L", "price": 10}, {"type": "H", "price": 20}, {"type": "L", "price": 12}]
    assert I.swing_structure(pivots) is True


def test_swing_structure_lower_second_low_is_false():
    pivots = [{"type": "L", "price": 10}, {"type": "H", "price": 20}, {"type": "L", "price": 8}]
    assert I.swing_structure(pivots) is False


def test_swing_structure_wrong_type_pattern_is_false():
    pivots = [{"type": "H", "price": 20}, {"type": "L", "price": 10}, {"type": "H", "price": 25}]
    assert I.swing_structure(pivots) is False


def test_swing_structure_fewer_than_three_pivots_is_none():
    assert I.swing_structure([{"type": "L", "price": 10}]) is None


def test_swing_structure_loss_mirrors_swing_structure():
    down = [{"type": "H", "price": 20}, {"type": "L", "price": 10}, {"type": "H", "price": 15}]
    assert I.swing_structure_loss(down) is True
    up_pattern_not_down = [{"type": "H", "price": 20}, {"type": "L", "price": 10}, {"type": "H", "price": 25}]
    assert I.swing_structure_loss(up_pattern_not_down) is False
    assert I.swing_structure_loss([{"type": "H", "price": 20}]) is None


# =============================================================================================
# Anchored VWAP + crossed-within
# =============================================================================================


def test_anchored_vwap_series_hand_computed():
    df = pd.DataFrame({"high": [10.0, 12.0], "low": [8.0, 10.0], "close": [9.0, 11.0],
                        "volume": [100.0, 200.0]})
    # typical = [9.0, 11.0]; cum_pv = [900, 900+2200=3100]; cum_v=[100,300]
    out = I.anchored_vwap_series(df)
    assert out.iloc[0] == pytest.approx(9.0)
    assert out.iloc[1] == pytest.approx(3100.0 / 300.0)


def test_anchored_vwap_series_empty():
    assert I.anchored_vwap_series(pd.DataFrame({"high": [], "low": [], "close": [], "volume": []})).empty


def test_crossed_within_recent_cross_is_true():
    assert I.crossed_within([False, False, True, True], lookback=5) is True


def test_crossed_within_currently_below_is_false():
    assert I.crossed_within([True, True, False], lookback=5) is False


def test_crossed_within_always_above_visible_window_is_false():
    assert I.crossed_within([True, True, True], lookback=5) is False


def test_crossed_within_cross_too_long_ago_is_false():
    above = [False, True, True, True, True, True, True]  # last False at index 0, 6 sessions ago
    assert I.crossed_within(above, lookback=5) is False


def test_crossed_within_no_data_is_none():
    assert I.crossed_within([]) is None


# =============================================================================================
# 60-session volume profile
# =============================================================================================


def test_volume_profile_hand_computed_two_bins():
    window = pd.DataFrame({
        "high": [10.0, 20.0], "low": [0.0, 10.0], "close": [5.0, 15.0], "volume": [100.0, 50.0],
    })
    out = I.volume_profile(window, n_bins=2, value_area_fraction=0.70)
    assert out["poc"] == pytest.approx(5.0)          # center of bin [0,10], the heavier bin
    assert out["value_area_low"] == pytest.approx(0.0)
    assert out["value_area_high"] == pytest.approx(20.0)  # 100/150=66.7% < 70%, must expand to both bins
    assert out["range_low"] == 0.0 and out["range_high"] == 20.0


def test_volume_profile_empty_or_zero_range_is_none():
    assert I.volume_profile(pd.DataFrame({"high": [], "low": [], "close": [], "volume": []})) is None
    flat = pd.DataFrame({"high": [5.0, 5.0], "low": [5.0, 5.0], "close": [5.0, 5.0], "volume": [10.0, 10.0]})
    assert I.volume_profile(flat) is None


# =============================================================================================
# RSI bullish divergence
# =============================================================================================


def test_bullish_divergence_true():
    closes = [10, 9, 8, 9, 10, 11, 7, 12]
    rsi = [50, 40, 30, 45, 55, 60, 42, 65]
    assert I.bullish_divergence(closes, rsi, lookback=8) is True


def test_bullish_divergence_false_when_rsi_also_makes_a_lower_low():
    closes = [10, 9, 8, 9, 10, 11, 7, 12]
    rsi = [50, 40, 20, 45, 55, 60, 10, 65]
    assert I.bullish_divergence(closes, rsi, lookback=8) is False


def test_bullish_divergence_false_when_price_does_not_make_a_lower_low():
    closes = [10, 9, 8, 9, 10, 11, 9, 12]
    rsi = [50, 40, 30, 45, 55, 60, 42, 65]
    assert I.bullish_divergence(closes, rsi, lookback=8) is False


def test_bullish_divergence_insufficient_bars_is_none():
    assert I.bullish_divergence([10, 9, 8], [50, 40, 30], lookback=8) is None


def test_bullish_divergence_missing_rsi_is_none():
    closes = [10, 9, 8, 9, 10, 11, 7, 12]
    rsi = [50, 40, None, 45, 55, 60, 42, 65]
    assert I.bullish_divergence(closes, rsi, lookback=8) is None
