"""S-C R4 (DESIGN/90 §6, §10): entry-week aggregation, NW lag 4, BH across the four pairs, the
six-trial DSR, PBO, the month rule, the tail, strata, the count-trigger status and the go / no-go,
each criterion on synthetic frames."""
from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd
import pytest

from engine.config import SC_NW_LAG
from engine.validation import sc_harness as H
from engine.validation import stats as ST

pytestmark = pytest.mark.unit

MON0 = date(2026, 1, 2)


def _frame(weeks: int, ror_fn, pairs=H.PAIRS, per_week: int = 2, start: date = MON0, risk: float = 500.0,
           cost_ror: float = 0.02) -> pd.DataFrame:
    rows = []
    for w in range(weeks):
        entry = start + timedelta(days=7 * w)
        for v, s in pairs:
            for k in range(per_week):
                r = float(ror_fn(w, k, v, s))
                rows.append({"variant": v, "structure": s, "entry": entry, "expiry": entry + timedelta(days=28),
                             "ticker": f"N{k}", "ror": r, "net_usd": r * risk, "risk_usd": risk,
                             "entry_cost_usd": cost_ror * risk, "cost_usd": cost_ror * risk, "graded": True,
                             "close": 50.0, "settle_close": 50.0 + (20.0 if r < -0.9 else 1.0), "sigma_hold": 5.0,
                             "marketcap": 2e9 * (1 + k), "iv30d": 0.35 + 0.1 * k, "sector": "Energy" if k else "Tech"})
    return pd.DataFrame(rows)


def _noisy(mean: float, sd: float = 0.05, seed: int = 7):
    rng = np.random.default_rng(seed)
    cache: dict = {}

    def f(w, k, v, s):
        key = (w, k, v, s)
        if key not in cache:
            cache[key] = mean + sd * rng.standard_normal()
        return cache[key]
    return f


# ---- the unit: entry week ------------------------------------------------------------------------

def test_weekly_series_averages_within_week_first():
    df = _frame(3, lambda w, k, v, s: [0.10, -0.02][k] + 0.01 * w, pairs=[("C1", "IB")])
    wk = H.weekly(df, "C1", "IB")
    assert list(wk.round(4)) == [0.04, 0.05, 0.06] and len(wk) == 3


def test_pair_block_uses_nw_lag_4_on_the_weekly_series():
    df = _frame(30, _noisy(0.03), pairs=[("C1", "SS")])
    b = H.pair_block(df, "C1", "SS", "M")
    ref = ST.nw_t(H.weekly(df, "C1", "SS").to_numpy(), SC_NW_LAG)
    assert b["weeks"] == 30 and b["n"] == 60 and b["nw_t"] == pytest.approx(ref["t"])
    assert b["mean_ror"] == pytest.approx(ref["mean"]) and b["mean_cost_ror"] == pytest.approx(0.02)


def test_bh_across_the_four_pairs():
    strong, null = _noisy(0.05, 0.02, 1), _noisy(0.0, 0.05, 2)
    df = _frame(40, lambda w, k, v, s: strong(w, k, v, s) if v == "C1" else null(w, k, v, s))
    bh = H.bh_table(df)
    assert list(bh["pair"]) == ["C1-SS", "C1-IB", "C2-SS", "C2-IB"]
    assert bh.set_index("pair").loc[["C1-SS", "C1-IB"], "bh_pass"].all()
    assert not bh.set_index("pair").loc[["C2-SS", "C2-IB"], "bh_pass"].any()


def test_dsr_reports_both_benchmarks_at_six_trials():
    d = H.dsr_table(_frame(30, _noisy(0.03)))
    assert set(d["n_trials"]) == {6} and {"deflated_sr", "deflated_sr_null"} <= set(d.columns)


def test_pbo_over_entry_blocks():
    rep = H.pbo_report(_frame(32, _noisy(0.01)))
    assert 0.0 <= rep["pbo"] <= 1.0 and rep["n_blocks"] == 8
    assert np.isnan(H.pbo_report(_frame(4, _noisy(0.01)))["pbo"])


# ---- month rule ----------------------------------------------------------------------------------

def test_month_rule_pass_fail_and_a_non_positive_median_fails():
    good = _frame(12, lambda w, k, v, s: 0.05, pairs=[("C1", "IB")])
    assert H.month_table(good).set_index("pair").loc["C1-IB", "month_rule_pass"]
    bad = _frame(12, lambda w, k, v, s: -0.9 if w == 5 else 0.02, pairs=[("C1", "IB")])
    row = H.month_table(bad).set_index("pair").loc["C1-IB"]
    assert not row["month_rule_pass"] and row["worst_over_median"] > 3
    flat = _frame(12, lambda w, k, v, s: -0.01, pairs=[("C1", "IB")])
    assert not H.month_table(flat).set_index("pair").loc["C1-IB", "month_rule_pass"]


# ---- tail ----------------------------------------------------------------------------------------

def test_tail_counts_realized_stress_on_ss_and_trims_the_worst_percent():
    df = _frame(50, lambda w, k, v, s: -1.2 if (w, k) == (3, 0) else 0.03, pairs=[("C1", "SS")])
    t = H.tail_report(df, "C1", "SS")
    assert t["realized_stress"] == 1 and t["worst_ror"] == pytest.approx(-1.2)
    assert t["mean_without_worst_1pct"] == pytest.approx(0.03) and len(t["worst_10"]) == 10
    assert t["worst_decile_share_of_loss"] == pytest.approx(1.0)


# ---- strata --------------------------------------------------------------------------------------

def test_strata_are_descriptive_terciles_and_categories():
    df = _frame(9, lambda w, k, v, s: 0.01 * (k + 1), pairs=[("C1", "IB")], per_week=3)
    by_cap = H.strata_table(df, "cap_tercile")
    assert list(by_cap["stratum"]) == ["T1", "T2", "T3"] and by_cap["n"].tolist() == [9, 9, 9]
    by_sector = H.strata_table(df, "sector")
    assert set(by_sector["stratum"]) == {"Tech", "Energy"}


# ---- count trigger and the bar ---------------------------------------------------------------------

def test_count_status_is_per_pair_graded_forward_weeks():
    fwd = _frame(39, _noisy(0.03))
    st = H.count_status(fwd).set_index("pair")
    assert (st["forward_weeks"] == 39).all() and (st["status"] == H.NOT_DUE).all() and (st["required"] == 40).all()
    st = H.count_status(_frame(40, _noisy(0.03))).set_index("pair")
    assert (st["status"] == H.DUE).all()


def test_go_no_go_is_not_due_before_the_trigger():
    ins, fwd = _frame(25, _noisy(0.03)), _frame(10, _noisy(0.03), start=date(2026, 10, 2))
    g = H.go_no_go(ins, fwd)
    assert (g["verdict"] == H.NOT_DUE).all() and (g["forward_weeks"] == 10).all()


def test_go_min_when_one_to_four_clear_and_scale_at_eighty():
    ins = _frame(25, _noisy(0.04, 0.02, 3))
    fwd = _frame(40, _noisy(0.04, 0.02, 4), start=date(2026, 10, 2))
    g = H.go_no_go(ins, fwd).set_index("pair")
    assert (g["verdict"] == H.GO_MIN).all(), g[["c1_forward", "c2_pooled", "c3_month", "c4_dsr"]]
    fwd80 = _frame(80, _noisy(0.04, 0.02, 5), start=date(2026, 10, 2))
    assert (H.go_no_go(ins, fwd80)["verdict"] == H.GO_SCALE).all()


def test_drift_beyond_one_round_trip_cost_fails_criterion_two():
    ins = _frame(25, _noisy(0.20, 0.02, 3))                                   # in-sample far richer
    fwd = _frame(40, _noisy(0.04, 0.02, 4), start=date(2026, 10, 2))
    g = H.go_no_go(ins, fwd).set_index("pair")
    assert not g["c2_pooled"].any() and (g["verdict"] == H.NO_GO).all()
    assert all("c2_pooled" in n for n in g["note"])


def test_a_forward_mean_without_t_fails_criterion_one():
    ins = _frame(25, _noisy(0.03, 0.02, 3))
    fwd = _frame(40, _noisy(0.002, 0.08, 9), start=date(2026, 10, 2))
    g = H.go_no_go(ins, fwd).set_index("pair")
    assert not g["c1_forward"].any()
