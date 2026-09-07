"""G6: expiration-day pinning on single names (RESEARCH/47 §2 G6; Ni-Pearson-Poteshman 2005).

Pure-function tests only: the expiry calendar, OI-snapshot parsing, pin/max-pain/placebo
strike selection, outcome distance/tolerance, the universe filter, and the NPP diagnostic.
No panel I/O here; see tests/test_expiry_pinning_data.py for the loader.
"""
from __future__ import annotations

from datetime import date

import numpy as np
import pandas as pd
import pytest

from engine.research import expiry_pinning as ep

pytestmark = pytest.mark.unit


# ------------------------------------------------------------------------------- expiry calendar

def test_build_expiry_calendar_covers_every_friday_and_flags_monthly():
    weeks = ep.build_expiry_calendar(date(2026, 3, 13), date(2026, 4, 24))
    fridays = [w.friday for w in weeks]
    assert fridays == [date(2026, 3, 13), date(2026, 3, 20), date(2026, 3, 27),
                       date(2026, 4, 3), date(2026, 4, 10), date(2026, 4, 17), date(2026, 4, 24)]
    monthly = {w.friday for w in weeks if w.is_monthly}
    # third Friday of March is 2026-03-20, of April is 2026-04-17
    assert monthly == {date(2026, 3, 20), date(2026, 4, 17)}


def test_holiday_friday_shifts_expiry_to_thursday():
    # 2026-04-03 is Good Friday, an NYSE holiday
    weeks = ep.build_expiry_calendar(date(2026, 4, 3), date(2026, 4, 3))
    assert len(weeks) == 1
    w = weeks[0]
    assert w.friday == date(2026, 4, 3)
    assert w.expiry == date(2026, 4, 2)          # Thursday
    assert w.day_minus_1 == date(2026, 4, 1)      # Wednesday


def test_non_holiday_friday_expiry_equals_friday_and_day_minus_1_is_thursday():
    weeks = ep.build_expiry_calendar(date(2026, 3, 13), date(2026, 3, 13))
    w = weeks[0]
    assert w.expiry == date(2026, 3, 13)
    assert w.day_minus_1 == date(2026, 3, 12)


def test_prior_friday_is_seven_calendar_days_earlier_adjusted_for_holidays():
    weeks = ep.build_expiry_calendar(date(2026, 3, 20), date(2026, 3, 20))
    assert weeks[0].prior_friday == date(2026, 3, 13)
    # the week after Good Friday: prior_friday should shift to the Thursday, 2026-04-02
    weeks2 = ep.build_expiry_calendar(date(2026, 4, 10), date(2026, 4, 10))
    assert weeks2[0].prior_friday == date(2026, 4, 2)


# ------------------------------------------------------------------------------- OI snapshot parsing

def test_parse_oi_snapshot_extracts_option_type_and_expiry():
    raw = pd.DataFrame({
        "option_symbol": ["AAPL260918C00150000", "AAPL260918P00150000", "MSTU2260918C00001000"],
        "underlying_symbol": ["AAPL", "AAPL", "MSTU2"],
        "strike": [150.0, 150.0, 1.0],
        "curr_oi": [100, 200, 50],
    })
    out = ep.parse_oi_snapshot(raw)
    assert list(out["option_type"]) == ["call", "put", "call"]
    assert list(out["expiry"]) == [date(2026, 9, 18)] * 3
    assert list(out["strike"]) == [150.0, 150.0, 1.0]


def test_parse_oi_snapshot_drops_unparseable_rows():
    raw = pd.DataFrame({
        "option_symbol": ["AAPL260918C00150000", "GARBAGE"],
        "underlying_symbol": ["AAPL", "GARBAGE"],
        "strike": [150.0, 1.0],
        "curr_oi": [100, 50],
    })
    out = ep.parse_oi_snapshot(raw)
    assert len(out) == 1
    assert out.iloc[0]["option_symbol"] == "AAPL260918C00150000"


# ------------------------------------------------------------------------------- strike selection

def _oi_df(rows: list[tuple[str, float, int]]) -> pd.DataFrame:
    return pd.DataFrame(rows, columns=["option_type", "strike", "curr_oi"])


def test_combined_oi_by_strike_sums_calls_and_puts():
    df = _oi_df([("call", 100.0, 500), ("put", 100.0, 300), ("call", 105.0, 200)])
    out = ep.combined_oi_by_strike(df)
    assert dict(zip(out.strike, out.oi)) == {100.0: 800, 105.0: 200}


def test_pin_strike_picks_the_largest_combined_oi():
    df = _oi_df([("call", 100.0, 500), ("put", 100.0, 300),
                ("call", 105.0, 2000), ("put", 105.0, 100)])
    strike_oi = ep.combined_oi_by_strike(df)
    assert ep.pin_strike(strike_oi, ref_close=103.0) == 105.0


def test_pin_strike_ties_broken_by_nearest_to_ref_close():
    df = _oi_df([("call", 100.0, 1000), ("call", 110.0, 1000)])
    strike_oi = ep.combined_oi_by_strike(df)
    assert ep.pin_strike(strike_oi, ref_close=101.0) == 100.0
    assert ep.pin_strike(strike_oi, ref_close=109.0) == 110.0


def test_pin_strike_empty_returns_none():
    strike_oi = ep.combined_oi_by_strike(_oi_df([]))
    assert ep.pin_strike(strike_oi, ref_close=100.0) is None


def test_max_pain_strike_minimizes_total_itm_payout():
    # single strike each side: max pain trivially sits where the smaller-OI side's payout wins
    df = _oi_df([("call", 95.0, 100), ("call", 100.0, 100), ("call", 105.0, 100),
                ("put", 95.0, 100), ("put", 100.0, 100), ("put", 105.0, 1000)])
    # at S=105: calls ITM payout = 100*(105-95)+100*(105-100)+0 = 1000+500=1500; puts ITM = 0
    # at S=100: calls ITM = 100*5=500; puts ITM = 1000*5=5000 -> total 5500
    # at S=95:  calls ITM = 0; puts ITM = 100*5+100*10+1000*(-10 clipped 0)... compute properly below
    out = ep.max_pain_strike(df, ref_close=100.0)
    assert out == 105.0


def test_max_pain_strike_ties_broken_by_nearest_to_ref_close():
    df = _oi_df([("call", 100.0, 0), ("put", 100.0, 0),
                ("call", 105.0, 0), ("put", 105.0, 0)])
    # zero OI everywhere -> every strike has zero payout -> tie broken by ref_close
    out = ep.max_pain_strike(df, ref_close=104.0)
    assert out == 105.0


def test_second_largest_oi_strike_excludes_the_pin():
    df = _oi_df([("call", 100.0, 500), ("call", 105.0, 2000), ("call", 110.0, 800)])
    strike_oi = ep.combined_oi_by_strike(df)
    pin = ep.pin_strike(strike_oi, ref_close=105.0)
    assert pin == 105.0
    second = ep.second_largest_oi_strike(strike_oi, exclude_strike=pin, ref_close=105.0)
    assert second == 110.0


def test_nearest_strike_to_close():
    strikes = pd.Series([90.0, 100.0, 110.0])
    assert ep.nearest_strike_to_close(strikes, ref_close=101.0) == 100.0
    assert ep.nearest_strike_to_close(strikes, ref_close=106.0) == 110.0


def test_nearest_strike_distance_uses_all_strikes_regardless_of_type():
    strikes = pd.Series([90.0, 100.0, 110.0])
    assert ep.nearest_strike_distance(strikes, close=101.0) == pytest.approx(1.0 / 101.0)


# ------------------------------------------------------------------------------- outcome metrics

def test_distance_frac():
    assert ep.distance_frac(close=100.0, strike=100.5) == pytest.approx(0.005)
    assert ep.distance_frac(close=100.0, strike=99.0) == pytest.approx(0.01)


@pytest.mark.parametrize("close,strike,tol,expected", [
    (100.0, 100.25, 0.0025, True),
    (100.0, 100.26, 0.0025, False),
    (100.0, 100.5, 0.005, True),
    (100.0, 101.0, 0.01, True),
    (100.0, 101.01, 0.01, False),
])
def test_within_tolerance(close, strike, tol, expected):
    assert ep.within_tolerance(close, strike, tol) is expected


# ------------------------------------------------------------------------------- universe filter

@pytest.mark.parametrize("issue_type,mcap,total_oi,expected", [
    ("Common Stock", 3e9, 6000, True),
    ("ADR", 2e9, 5000, True),
    ("ETF", 3e9, 6000, False),      # excluded issue type
    ("Common Stock", 1.9e9, 6000, False),   # below mcap floor
    ("Common Stock", 3e9, 4999, False),     # below OI floor
    ("Common Stock", None, 6000, False),
    ("Common Stock", 3e9, None, False),
])
def test_passes_universe(issue_type, mcap, total_oi, expected):
    assert ep.passes_universe(issue_type, mcap, total_oi) is expected


# ------------------------------------------------------------------------------- NPP diagnostic

def test_npp_diagnostic_reports_paired_distance_stats():
    expiry_dist = np.array([0.001, 0.002, 0.02, 0.03])
    prior_dist = np.array([0.01, 0.015, 0.018, 0.04])
    out = ep.npp_diagnostic(expiry_dist, prior_dist)
    assert out["n"] == 4
    assert out["mean_expiry"] == pytest.approx(expiry_dist.mean())
    assert out["mean_prior"] == pytest.approx(prior_dist.mean())
    assert "wilcoxon_p" in out and "ttest_p" in out


def test_npp_diagnostic_drops_nan_pairs():
    expiry_dist = np.array([0.001, np.nan, 0.02])
    prior_dist = np.array([0.01, 0.015, np.nan])
    out = ep.npp_diagnostic(expiry_dist, prior_dist)
    assert out["n"] == 1
