"""G4/G5 cross-section: delta matching/interpolation, factor formulas, residualisation, IC/decile
computation, BH q-values, and `build_week_factors`'s eligibility + merge logic on injected data
(RESEARCH/47 §2 G4/G5)."""
from __future__ import annotations

from datetime import date

import numpy as np
import pandas as pd
import pytest

from engine.research import cross_section as CS
from engine.research import xs_factors as XF
from engine.research import xs_stats as XS

pytestmark = pytest.mark.unit


# ---- xs_factors: delta matching -------------------------------------------------------------

def test_match_iv_at_delta_exact_hit():
    contracts = pd.DataFrame({"delta": [0.3, 0.5, 0.7], "iv": [0.25, 0.30, 0.35]})
    m = XF.match_iv_at_delta(contracts, 0.5)
    assert m.method == XF.METHOD_EXACT
    assert m.iv == pytest.approx(0.30)


def test_match_iv_at_delta_interpolates_when_bracketed():
    contracts = pd.DataFrame({"delta": [0.40, 0.60], "iv": [0.20, 0.30]})
    m = XF.match_iv_at_delta(contracts, 0.50)
    assert m.method == XF.METHOD_INTERP
    assert m.iv == pytest.approx(0.25)          # midpoint of delta -> midpoint of iv (linear)
    assert m.delta_lo == pytest.approx(0.40) and m.delta_hi == pytest.approx(0.60)


def test_match_iv_at_delta_interpolation_is_weighted_not_just_averaged():
    contracts = pd.DataFrame({"delta": [0.40, 0.60], "iv": [0.20, 0.30]})
    m = XF.match_iv_at_delta(contracts, 0.45)    # 25% of the way from 0.40 to 0.60
    assert m.iv == pytest.approx(0.225)


def test_match_iv_at_delta_falls_back_to_nearest_outside_the_range():
    contracts = pd.DataFrame({"delta": [0.55, 0.60, 0.65]}).assign(iv=[0.31, 0.32, 0.33])
    m = XF.match_iv_at_delta(contracts, 0.10)    # target below every observed delta: no bracket
    assert m.method == XF.METHOD_NEAREST
    assert m.iv == pytest.approx(0.31) and m.delta_used == pytest.approx(0.55)


def test_match_iv_at_delta_empty_pool_is_none():
    m = XF.match_iv_at_delta(pd.DataFrame(columns=["delta", "iv"]), 0.5)
    assert m.iv is None and m.method is None and m.n_points == 0


def test_clean_deltas_drops_wrong_sign_and_non_finite_iv():
    calls = pd.DataFrame({"delta": [0.3, -0.2, 0.6, np.nan], "iv": [0.2, 0.3, np.inf, 0.4]})
    cleaned = XF.clean_deltas(calls, sign=+1)
    assert cleaned["delta"].tolist() == [0.3]   # -0.2 wrong sign, 0.6 non-finite iv, nan delta dropped
    puts = pd.DataFrame({"delta": [-0.25, 0.4, -0.5], "iv": [0.3, 0.2, 0.0]})
    cleaned_p = XF.clean_deltas(puts, sign=-1)
    assert cleaned_p["delta"].tolist() == [-0.25]   # 0.4 wrong sign, -0.5 has iv <= 0


def test_nearest_expiry_picks_closest_to_target_ties_broken_by_smaller_date():
    df = pd.DataFrame({"expiry": [date(2026, 9, 1), date(2026, 9, 20), date(2026, 10, 10)],
                        "dte_cal": [5, 25, 35]})
    assert XF.nearest_expiry(df, target_days=30) == date(2026, 9, 20)      # |25-30|=5 closest
    tied = pd.DataFrame({"expiry": [date(2026, 9, 10), date(2026, 9, 30)], "dte_cal": [20, 40]})
    assert XF.nearest_expiry(tied, target_days=30) == date(2026, 9, 10)    # both dist 10, smaller wins


def test_nearest_expiry_empty_is_none():
    assert XF.nearest_expiry(pd.DataFrame(columns=["expiry", "dte_cal"])) is None


def test_has_delta_band():
    contracts = pd.DataFrame({"delta": [0.1, 0.3, 0.55]})
    assert XF.has_delta_band(contracts, XF.ELIGIBLE_CALL_DELTA_BAND)
    assert not XF.has_delta_band(pd.DataFrame({"delta": [0.1, 0.65]}), XF.ELIGIBLE_CALL_DELTA_BAND)
    assert not XF.has_delta_band(pd.DataFrame(columns=["delta"]), XF.ELIGIBLE_CALL_DELTA_BAND)


# ---- xs_factors: factor formulas --------------------------------------------------------------

def test_iv_spread_and_put_skew_formulas():
    call = XF.DeltaMatch(0.30, "exact", 0.5, None, None, 3)
    put = XF.DeltaMatch(0.25, "exact", -0.5, None, None, 3)
    put25 = XF.DeltaMatch(0.35, "exact", -0.25, None, None, 3)
    assert XF.iv_spread(call, put) == pytest.approx(0.05)
    assert XF.put_skew(put25, call) == pytest.approx(0.05)


def test_iv_spread_and_put_skew_none_when_either_side_missing():
    missing = XF.DeltaMatch(None, None, None, None, None, 0)
    call = XF.DeltaMatch(0.30, "exact", 0.5, None, None, 3)
    assert XF.iv_spread(call, missing) is None
    assert XF.put_skew(missing, call) is None


def test_os_ratio_uses_total_volume_then_falls_back_to_avg30():
    ratio, source = XF.os_ratio(call_volume=1000, put_volume=500, total_volume=100_000, avg30_volume=50_000)
    assert source == "total_volume"
    assert ratio == pytest.approx(1500 * 100 / 100_000)
    ratio2, source2 = XF.os_ratio(1000, 500, total_volume=0, avg30_volume=50_000)
    assert source2 == "avg30_volume"
    assert ratio2 == pytest.approx(1500 * 100 / 50_000)
    ratio3, source3 = XF.os_ratio(1000, 500, total_volume=None, avg30_volume=None)
    assert ratio3 is None and source3 is None


# ---- xs_stats: residualisation, IC, decile spread, BH -----------------------------------------

def test_residualize_week_removes_an_exact_linear_relationship():
    rng = np.random.default_rng(0)
    n = 30
    control = rng.normal(size=n)
    df = pd.DataFrame({"factor": 2.0 * control + 1.0, "control": control})
    resid = XS.residualize_week(df, "factor", ["control"])
    assert resid.abs().max() < 1e-8          # exact linear relation, no noise: residual ~ 0


def test_residualize_week_returns_nan_when_too_few_complete_rows():
    df = pd.DataFrame({"factor": [1.0, 2.0], "c1": [1.0, 2.0], "c2": [1.0, np.nan]})
    resid = XS.residualize_week(df, "factor", ["c1", "c2"])
    assert resid.isna().all()


def test_rank_ic_perfect_monotone_relationship():
    df = pd.DataFrame({"f": range(10), "y": range(10)})
    ic, n = XS.rank_ic(df, "f", "y")
    assert ic == pytest.approx(1.0) and n == 10


def test_rank_ic_nan_below_min_week_n():
    df = pd.DataFrame({"f": [1, 2], "y": [1, 2]})
    ic, n = XS.rank_ic(df, "f", "y")
    assert np.isnan(ic) and n == 2


def test_decile_spread_top_minus_bottom():
    n = 40
    df = pd.DataFrame({"f": range(n), "y": [float(i) for i in range(n)]})
    ds, n_used = XS.decile_spread(df, "f", "y")
    assert ds > 0 and n_used == n


def test_decile_spread_nan_when_universe_too_small():
    df = pd.DataFrame({"f": range(5), "y": range(5)})
    ds, n_used = XS.decile_spread(df, "f", "y")
    assert np.isnan(ds)


def test_bh_qvalues_matches_hand_worked_example():
    # p-values 0.01, 0.02, 0.03, 0.5 -> BH q = p*m/rank, monotone from the top
    q = XS.bh_qvalues([0.01, 0.02, 0.03, 0.5])
    assert q[0] == pytest.approx(0.04)          # min(0.01*4/1, ...) after monotonicity enforcement
    assert q[3] == pytest.approx(0.5)
    assert all(0.0 <= x <= 1.0 for x in q)


def test_bh_qvalues_empty():
    assert XS.bh_qvalues([]) == []


def test_sign_consistency_and_half_split():
    ic = pd.Series([0.02, 0.03, -0.01, 0.04, 0.05, 0.06])
    assert XS.sign_consistency(ic) == pytest.approx(5 / 6)
    halves = XS.half_split(ic)
    assert halves["first_half_n"] == 3 and halves["second_half_n"] == 3
    assert halves["sign_stable_across_halves"] is True


def test_summarize_ic_reports_nw_t_and_sign_consistency():
    ic = pd.Series([0.02, 0.03, 0.01, 0.04], index=[date(2026, 1, 2), date(2026, 1, 9),
                                                     date(2026, 1, 16), date(2026, 1, 23)])
    out = XS.summarize_ic(ic)
    assert out["mean_ic"] == pytest.approx(ic.mean())
    assert out["sign_consistency"] == pytest.approx(1.0)
    assert out["n_formations"] == 4


# ---- cross_section: build_week_factors on injected data (no mart / screener I/O) --------------

def _hot_row(ticker, option_type, strike, expiry, dte_cal, delta, iv):
    return {"underlying_symbol": ticker, "option_type": option_type, "strike": strike,
            "expiry": expiry, "dte_cal": dte_cal, "delta_last": delta, "iv": iv}


def _synthetic_hot_chain(d: date) -> pd.DataFrame:
    exp = date(2026, 10, 2)                     # ~ 28 calendar days out from d = 2026-09-04
    rows = [
        # AAA: eligible both sides, clean 0.50/0.25 matches
        _hot_row("AAA", "call", 100, exp, 28, 0.50, 0.20),
        _hot_row("AAA", "call", 105, exp, 28, 0.30, 0.18),
        _hot_row("AAA", "put", 95, exp, 28, -0.50, 0.22),
        _hot_row("AAA", "put", 90, exp, 28, -0.25, 0.28),
        # BBB: no put in the eligible band -> ineligible
        _hot_row("BBB", "call", 50, exp, 28, 0.45, 0.30),
        # CCC: eligible, used to check the merge drops sub-$1B names
        _hot_row("CCC", "call", 20, exp, 28, 0.55, 0.40),
        _hot_row("CCC", "put", 18, exp, 28, -0.30, 0.45),
    ]
    return pd.DataFrame(rows)


def _synthetic_screener(d: date) -> pd.DataFrame:
    return pd.DataFrame({
        "ticker": ["AAA", "CCC"], "marketcap": [5e9, 5e8], "log_mcap": [np.log(5e9), np.log(5e8)],
        "sector": ["Technology", "Energy"], "total_volume": [1_000_000, 200_000],
        "avg30_volume": [900_000, 180_000], "call_volume": [5000, 100], "put_volume": [3000, 50],
    })


def _stub_short_side(spine: pd.DataFrame) -> pd.DataFrame:
    return spine.assign(short_interest=1_000_000.0, days_to_cover=2.0,
                         si_change_pct=0.0, borrow_fee=0.01)


def test_build_week_factors_eligibility_and_marketcap_filter():
    d = date(2026, 9, 4)
    week = CS.build_week_factors(d, hot=_synthetic_hot_chain(d), screener=_synthetic_screener(d),
                                  join_short_side_fn=_stub_short_side)
    # BBB has no eligible put -> excluded regardless of screener presence.
    # CCC clears the delta bands but is sub-$1B -> excluded by the marketcap leg.
    assert week["ticker"].tolist() == ["AAA"]
    row = week.iloc[0]
    assert row["atm_call_iv"] == pytest.approx(0.20) and row["atm_call_method"] == XF.METHOD_EXACT
    assert row["atm_put_iv"] == pytest.approx(0.22)
    assert row["put25_iv"] == pytest.approx(0.28)
    assert row["iv_spread"] == pytest.approx(0.20 - 0.22)
    assert row["put_skew"] == pytest.approx(0.28 - 0.20)
    assert row["os_source"] == "total_volume"
    assert row["short_interest"] == pytest.approx(1_000_000.0)
    assert row["formation_date"] == d


def test_build_week_factors_empty_hot_chain_returns_empty_frame():
    d = date(2026, 9, 4)
    out = CS.build_week_factors(d, hot=pd.DataFrame(columns=["underlying_symbol", "option_type",
                                                              "expiry", "dte_cal", "delta_last", "iv"]),
                                 screener=_synthetic_screener(d))
    assert out.empty
