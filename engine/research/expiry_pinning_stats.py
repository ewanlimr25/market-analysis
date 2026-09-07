"""G6 aggregation: rate tables, baseline comparisons, splits and the pre-registered kill rule
(RESEARCH/47 §2 G6), consuming a `g6_pins`-shaped frame (one row per name x expiry, distance
columns in fraction-of-close units). Pure functions; no file I/O.
"""
from __future__ import annotations

from datetime import date

import numpy as np
import pandas as pd

from engine.research.expiry_pinning import PRIMARY_TOLERANCE, TOLERANCES, npp_diagnostic
from engine.validation import stats as S


def tolerance_rate(dist: pd.Series, tol: float) -> tuple[int, int, float]:
    """(successes, n, rate) of `dist <= tol`, dropping NaN. rate is NaN when n == 0."""
    d = dist.dropna()
    n = len(d)
    succ = int((d <= tol).sum())
    return succ, n, (succ / n if n else float("nan"))


def rate_table(pins: pd.DataFrame, dist_col: str, tolerances: tuple[float, ...] = TOLERANCES) -> dict:
    """{tolerance: {successes, n, rate}} for one distance column, no baseline comparison."""
    out = {}
    for tol in tolerances:
        succ, n, rate = tolerance_rate(pins[dist_col], tol)
        out[tol] = {"successes": succ, "n": n, "rate": rate}
    return out


def compare_to_baseline(pins: pd.DataFrame, target_dist_col: str, baseline_dist_col: str,
                        tolerances: tuple[float, ...] = TOLERANCES) -> dict:
    """Per tolerance: target and baseline rates on the paired (non-NaN in both) rows, the
    point-difference, a two-sided binomial test of the target's successes against the
    baseline's pooled rate as the null, and the paired McNemar test on the same rows
    (b = target hit & baseline miss, c = target miss & baseline hit)."""
    out = {}
    for tol in tolerances:
        paired = pins[[target_dist_col, baseline_dist_col]].dropna()
        n = len(paired)
        if n == 0:
            out[tol] = {"n": 0, "rate_target": float("nan"), "rate_baseline": float("nan"),
                       "point_diff": float("nan"), "binomial_p": float("nan"),
                       "mcnemar_p": float("nan"), "mcnemar_b": 0, "mcnemar_c": 0}
            continue
        t_hit = paired[target_dist_col] <= tol
        b_hit = paired[baseline_dist_col] <= tol
        succ_t = int(t_hit.sum())
        rate_t = succ_t / n
        rate_b = float(b_hit.mean())
        b_count = int((t_hit & ~b_hit).sum())
        c_count = int((~t_hit & b_hit).sum())
        binom = S.binomial_test(succ_t, n, rate_b)
        mc = S.mcnemar_test(b_count, c_count)
        out[tol] = {"n": n, "rate_target": rate_t, "rate_baseline": rate_b,
                   "point_diff": (rate_t - rate_b) * 100, "binomial_p": binom["p"],
                   "mcnemar_p": mc["p"], "mcnemar_b": b_count, "mcnemar_c": c_count}
    return out


def assign_halves(pins: pd.DataFrame, date_col: str = "expiry") -> pd.DataFrame:
    """Split by unique expiry DATES (not rows), so a monthly expiry's larger name count does
    not skew the split: the first half of the sorted dates (extra date on H1 if odd) is 'H1'."""
    dates = sorted(pins[date_col].unique())
    mid = len(dates) // 2 + len(dates) % 2
    first_half = set(dates[:mid])
    return pins.assign(half=pins[date_col].map(lambda d: "H1" if d in first_half else "H2"))


def kill_rule_verdict(halves: dict[str, dict], weekly_cell: dict,
                      tol: float = PRIMARY_TOLERANCE, margin_points: float = 5.0,
                      alpha: float = 0.05) -> dict:
    """RESEARCH/47 §2 G6 kill rule: the pin-vs-prior-Friday point difference at `tol` must be
    >= `margin_points` with binomial p < `alpha` in BOTH halves, and the same must hold at
    weekly expiries (what a strategy would need for N)."""
    h1, h2 = halves.get("H1", {}).get(tol, {}), halves.get("H2", {}).get(tol, {})

    def _passes(cell: dict) -> bool:
        diff, p = cell.get("point_diff"), cell.get("binomial_p")
        if diff is None or p is None or (isinstance(diff, float) and np.isnan(diff)):
            return False
        return diff >= margin_points and p < alpha

    both_halves_pass = _passes(h1) and _passes(h2)
    weekly_present = _passes(weekly_cell)
    return {"passed": both_halves_pass and weekly_present, "both_halves_pass": both_halves_pass,
           "weekly_present": weekly_present, "h1": h1, "h2": h2, "weekly": weekly_cell,
           "tol": tol, "margin_points": margin_points, "alpha": alpha}


def build_full_report(pins: pd.DataFrame, n_fridays_total: int, excluded_expiries: list[date]) -> dict:
    """Assemble every table RESEARCH/47 §2 G6 pre-registers: universe counts, pin/max-pain rates
    against both baselines at all three tolerances, the monthly-vs-weekly and half-vs-half
    splits, the NPP any-strike diagnostic, and the kill-rule verdict."""
    pins = assign_halves(pins)
    monthly_dates = set(pins.loc[pins["is_monthly"], "expiry"].unique())
    weekly_dates = set(pins.loc[~pins["is_monthly"], "expiry"].unique())
    universe = {
        "n_rows": int(len(pins)), "n_unique_names": int(pins["underlying"].nunique()),
        "n_fridays_total": int(n_fridays_total), "n_expiries_usable": int(pins["expiry"].nunique()),
        "n_expiries_excluded": len(excluded_expiries),
        "excluded_expiries": [d.isoformat() for d in sorted(excluded_expiries)],
        "n_monthly_usable": len(monthly_dates), "n_weekly_usable": len(weekly_dates),
    }
    monthly, weekly = pins[pins["is_monthly"]], pins[~pins["is_monthly"]]
    monthly_vs_weekly = {
        "monthly": compare_to_baseline(monthly, "dist_pin_expiry", "dist_pin_prior_friday"),
        "weekly": compare_to_baseline(weekly, "dist_pin_expiry", "dist_pin_prior_friday"),
    }
    halves = {
        "H1": compare_to_baseline(pins[pins["half"] == "H1"], "dist_pin_expiry", "dist_pin_prior_friday"),
        "H2": compare_to_baseline(pins[pins["half"] == "H2"], "dist_pin_expiry", "dist_pin_prior_friday"),
    }
    npp = npp_diagnostic(pins["nearest_any_strike_dist_expiry"], pins["nearest_any_strike_dist_prior_friday"])
    verdict = kill_rule_verdict(halves, monthly_vs_weekly["weekly"][PRIMARY_TOLERANCE])
    return {
        "universe": universe,
        "pin_vs_prior_friday": compare_to_baseline(pins, "dist_pin_expiry", "dist_pin_prior_friday"),
        "pin_vs_placebo_second": compare_to_baseline(pins, "dist_pin_expiry", "dist_placebo_second_expiry"),
        "pin_vs_placebo_nearest": compare_to_baseline(pins, "dist_pin_expiry", "dist_placebo_nearest_expiry"),
        "maxpain_vs_prior_friday": compare_to_baseline(pins, "dist_maxpain_expiry", "dist_maxpain_prior_friday"),
        "monthly_vs_weekly": monthly_vs_weekly,
        "halves": halves,
        "npp_diagnostic": npp,
        "kill_rule": verdict,
    }
