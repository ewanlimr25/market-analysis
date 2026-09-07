"""G6 aggregation layer: rate tables, baseline comparisons (binomial + McNemar), halves/monthly
split, and the kill-rule verdict, on small synthetic `g6_pins`-shaped frames."""
from __future__ import annotations

from datetime import date

import numpy as np
import pandas as pd
import pytest

from engine.research import expiry_pinning_stats as S

pytestmark = pytest.mark.unit


def test_tolerance_rate_counts_hits_and_drops_nan():
    dist = pd.Series([0.001, 0.003, 0.006, np.nan, 0.02])
    succ, n, rate = S.tolerance_rate(dist, tol=0.005)
    assert (succ, n) == (2, 4)
    assert rate == pytest.approx(0.5)


def test_tolerance_rate_empty_is_nan():
    succ, n, rate = S.tolerance_rate(pd.Series([], dtype=float), tol=0.005)
    assert (succ, n) == (0, 0) and np.isnan(rate)


def _pins(n_hit_target: int, n_miss_target: int, n_hit_baseline_only: int, n_miss_both: int,
         tol: float = 0.005) -> pd.DataFrame:
    """Rows with dist just inside/outside `tol` for target and baseline, in four buckets:
    both hit, target-only hit, baseline-only hit, neither hit."""
    rows = []
    inside, outside = tol * 0.5, tol * 2.0
    for _ in range(n_hit_target):
        rows.append({"dist_t": inside, "dist_b": inside})
    for _ in range(n_miss_target):
        rows.append({"dist_t": outside, "dist_b": outside})
    for _ in range(n_hit_baseline_only):
        rows.append({"dist_t": outside, "dist_b": inside})
    for _ in range(n_miss_both):
        rows.append({"dist_t": inside, "dist_b": outside})
    return pd.DataFrame(rows)


def test_compare_to_baseline_matches_manual_binomial_and_mcnemar():
    # 40 both-hit, 30 both-miss, 10 target-only-hit, 20 baseline-only-hit -> n=100
    pins = _pins(n_hit_target=40, n_miss_target=30, n_hit_baseline_only=20, n_miss_both=10)
    out = S.compare_to_baseline(pins, "dist_t", "dist_b", tolerances=(0.005,))
    cell = out[0.005]
    assert cell["n"] == 100
    assert cell["rate_target"] == pytest.approx(0.50)     # 40 + 10 miss_both counted as target hit
    assert cell["rate_baseline"] == pytest.approx(0.60)   # 40 + 20 baseline-only
    assert cell["point_diff"] == pytest.approx(-10.0)
    assert cell["mcnemar_b"] == 10 and cell["mcnemar_c"] == 20
    from engine.validation import stats as VS
    ref_mc = VS.mcnemar_test(10, 20)
    assert cell["mcnemar_p"] == pytest.approx(ref_mc["p"])
    ref_binom = VS.binomial_test(50, 100, 0.60)
    assert cell["binomial_p"] == pytest.approx(ref_binom["p"])


def test_compare_to_baseline_handles_nan_rows_by_dropping_the_pair():
    pins = pd.DataFrame({"dist_t": [0.001, np.nan, 0.001], "dist_b": [0.001, 0.001, np.nan]})
    out = S.compare_to_baseline(pins, "dist_t", "dist_b", tolerances=(0.005,))
    assert out[0.005]["n"] == 1


def test_assign_halves_splits_on_unique_expiry_dates_not_row_count():
    # a monthly expiry with many names must not pull the split toward its half
    rows = []
    for i, d in enumerate([date(2026, 3, 20), date(2026, 3, 27), date(2026, 4, 3)]):
        n_names = 20 if i == 0 else 2
        for _ in range(n_names):
            rows.append({"expiry": d})
    pins = pd.DataFrame(rows)
    out = S.assign_halves(pins)
    # 3 unique dates -> first 2 dates = H1, last = H2 (ceil split favors H1)
    assert set(out.loc[out.expiry == date(2026, 3, 20), "half"]) == {"H1"}
    assert set(out.loc[out.expiry == date(2026, 3, 27), "half"]) == {"H1"}
    assert set(out.loc[out.expiry == date(2026, 4, 3), "half"]) == {"H2"}


def test_kill_rule_verdict_requires_both_halves_and_weekly():
    passing_cell = {"point_diff": 6.0, "binomial_p": 0.01}
    failing_cell = {"point_diff": 3.0, "binomial_p": 0.01}
    halves_pass = {"H1": {0.005: passing_cell}, "H2": {0.005: passing_cell}}
    halves_fail = {"H1": {0.005: passing_cell}, "H2": {0.005: failing_cell}}
    v = S.kill_rule_verdict(halves_pass, passing_cell)
    assert v["passed"] is True
    v2 = S.kill_rule_verdict(halves_fail, passing_cell)
    assert v2["passed"] is False and v2["both_halves_pass"] is False
    v3 = S.kill_rule_verdict(halves_pass, failing_cell)
    assert v3["passed"] is False and v3["weekly_present"] is False


def test_kill_rule_verdict_rejects_high_p_even_with_margin():
    cell = {"point_diff": 10.0, "binomial_p": 0.20}
    halves = {"H1": {0.005: cell}, "H2": {0.005: cell}}
    v = S.kill_rule_verdict(halves, cell)
    assert v["passed"] is False


def _synthetic_pins(n: int, seed: int = 0) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    dates = [date(2026, 3, 20), date(2026, 3, 27), date(2026, 4, 17), date(2026, 8, 21)]
    rows = []
    for i in range(n):
        d = dates[i % len(dates)]
        rows.append({
            "underlying": f"T{i}", "expiry": d, "is_monthly": d.day in (20, 17, 21),
            "dist_pin_expiry": abs(rng.normal(0, 0.01)),
            "dist_pin_prior_friday": abs(rng.normal(0, 0.02)),
            "dist_maxpain_expiry": abs(rng.normal(0, 0.01)),
            "dist_maxpain_prior_friday": abs(rng.normal(0, 0.02)),
            "dist_placebo_second_expiry": abs(rng.normal(0, 0.015)),
            "dist_placebo_nearest_expiry": abs(rng.normal(0, 0.01)),
            "nearest_any_strike_dist_expiry": abs(rng.normal(0, 0.008)),
            "nearest_any_strike_dist_prior_friday": abs(rng.normal(0, 0.012)),
        })
    return pd.DataFrame(rows)


def test_build_full_report_has_every_pre_registered_table():
    pins = _synthetic_pins(40)
    report = S.build_full_report(pins, n_fridays_total=26, excluded_expiries=[date(2026, 4, 3)])
    assert report["universe"]["n_rows"] == 40
    assert report["universe"]["n_expiries_excluded"] == 1
    assert report["universe"]["excluded_expiries"] == ["2026-04-03"]
    for key in ("pin_vs_prior_friday", "pin_vs_placebo_second", "pin_vs_placebo_nearest",
               "maxpain_vs_prior_friday"):
        assert set(report[key].keys()) == set(S.TOLERANCES)
    assert set(report["monthly_vs_weekly"].keys()) == {"monthly", "weekly"}
    assert set(report["halves"].keys()) == {"H1", "H2"}
    assert "wilcoxon_p" in report["npp_diagnostic"]
    assert "passed" in report["kill_rule"]
