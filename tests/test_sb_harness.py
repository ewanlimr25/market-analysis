"""Q6: Newey-West t, the S-B sleeve tables, the month rule, the overlap check and go/no-go
(DESIGN/80 §6) on synthetic position frames."""
from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd
import pytest

from engine.validation import stats as S
from engine.validation import sb_harness as H

pytestmark = pytest.mark.unit


def test_nw_t_with_lag_zero_is_the_classical_t_and_positive_autocorrelation_widens_the_se():
    rng = np.random.default_rng(0)
    x = rng.normal(0.5, 1.0, 200)
    nw0 = S.nw_t(x, 0)
    classical = x.mean() / (x.std(ddof=1) / np.sqrt(len(x)))
    assert nw0["t"] == pytest.approx(classical, rel=0.01)          # NW uses 1/n, classical 1/(n-1)
    ar = np.cumsum(rng.normal(0, 1, 400))[::1]
    ar = np.diff(ar) + 0.2
    smooth = pd.Series(ar).rolling(3).mean().dropna().to_numpy()     # induces positive autocorrelation
    assert S.nw_t(smooth, 2)["se"] > S.nw_t(smooth, 0)["se"]
    assert S.nw_t([1.0, 2.0], 2)["t"] != S.nw_t([1.0, 2.0], 2)["t"]   # NaN for n < 3


def _positions(sleeve_rors: dict, start=date(2024, 1, 5), n=60, risk=2500.0):
    rows = []
    for (u, s), rors in sleeve_rors.items():
        for i in range(n):
            entry = start + timedelta(days=7 * i)
            expiry = entry + timedelta(days=21)
            ror = rors[i % len(rors)]
            rows.append({"underlying": u, "structure": s, "entry": entry, "expiry": expiry, "ror": ror,
                         "net_usd": ror * risk, "risk_usd": risk, "max_loss_usd": risk, "n": 1,
                         "cost_usd": 20.0, "credit_entry": 2.0, "width": 30.0, "credit_over_width": 2 / 30,
                         "cost_over_credit": 0.1, "x": 18.0, "window": "P1" if entry < date(2024, 9, 6) else "P2",
                         "month": expiry.strftime("%Y-%m"), "gate_mode": "both", "gate_reason": "ON"})
    return pd.DataFrame(rows)


def test_sleeve_table_reports_nw_and_clustered_t_per_window_and_pooled():
    df = _positions({("SPY", "PS"): [0.05, 0.06, 0.04], ("SPY", "IC"): [0.03, -0.9, 0.05]})
    tab = H.sleeve_table(df)
    assert set(tab.window) == {"P1", "P2", "pooled"} and set(zip(tab.underlying, tab.structure)) == {("SPY", "PS"), ("SPY", "IC")}
    ps = tab[(tab.structure == "PS") & (tab.window == "pooled")].iloc[0]
    assert ps.n == 60 and ps.mean_ror == pytest.approx(0.05) and ps.nw_t > 2 and ps.cl_t > 2 and ps.hit == 1.0
    ic = tab[(tab.structure == "IC") & (tab.window == "pooled")].iloc[0]
    assert ic.mean_ror < 0 and ic.nw_t < 0


def test_month_rule_passes_when_the_worst_month_is_within_three_median_months():
    df = _positions({("SPY", "PS"): [0.05] * 12 + [-0.2]})
    tab = H.monthly_table(df)
    row = tab.iloc[0]
    assert row.n_months > 6 and row.median_month_usd > 0 and row.worst_month_usd < row.median_month_usd
    assert bool(row.month_rule_pass) == bool(row.worst_month_usd >= -3.0 * row.median_month_usd)
    bad = _positions({("SPY", "PS"): [0.05] * 6 + [-1.0]})
    assert not H.monthly_table(bad).iloc[0].month_rule_pass
    flat = _positions({("SPY", "PS"): [-0.01]})
    assert not H.monthly_table(flat).iloc[0].month_rule_pass          # non-positive median fails


def test_overlap_check_compares_marked_and_proxy_on_the_same_positions():
    proxy = _positions({("SPY", "PS"): [0.05]}, n=10)
    marked = _positions({("SPY", "PS"): [0.045]}, n=10).assign(cost_usd=25.0)   # 1% of risk in cost
    tab = H.overlap_table(marked, proxy)
    row = tab.iloc[0]
    assert row.n_overlap == 10 and row.gap_ror == pytest.approx(0.005) and row.marked_cost_ror == pytest.approx(0.01)
    assert bool(row.overlap_pass)
    far = _positions({("SPY", "PS"): [0.0]}, n=10).assign(cost_usd=25.0)
    assert not H.overlap_table(far, proxy).iloc[0].overlap_pass
    assert H.overlap_table(marked.iloc[0:0], proxy).iloc[0].n_overlap == 0


def test_go_no_go_applies_the_five_criteria_per_sleeve():
    good = [0.06, 0.05, 0.07, 0.04, 0.05, 0.06, -0.05]
    proxy = _positions({("SPY", "PS"): good, ("SPY", "IC"): [0.05, -0.06], ("QQQ", "PS"): good, ("QQQ", "IC"): [0.04, -0.05]}, n=150)
    proxy = proxy.assign(window=proxy.entry.map(lambda d: "P1" if d < date(2024, 9, 6) else ("P2" if d < date(2025, 9, 5) else "P3")))
    marked = _positions({("SPY", "PS"): [0.05], ("SPY", "IC"): [-0.1], ("QQQ", "PS"): [-0.01], ("QQQ", "IC"): [0.01]}, n=8,
                        start=date(2026, 3, 13)).assign(cost_usd=25.0)
    forward = _positions({("SPY", "PS"): [0.04]}, n=3, start=date(2026, 9, 11))
    verdict = H.go_no_go(proxy, marked, forward)
    by = {(r.underlying, r.structure): r for r in verdict.itertuples()}
    spy_ps = by[("SPY", "PS")]
    assert spy_ps.c1_proxy and spy_ps.c2_marked and spy_ps.c3_month and spy_ps.c4_dsr
    assert spy_ps.verdict == "GO-MIN" and spy_ps.forward_n == 3 and not spy_ps.c5_scale
    assert by[("SPY", "IC")].verdict == "NO-GO" and by[("QQQ", "PS")].verdict == "NO-GO"       # marked mean < 0
    assert "c2_marked" in by[("QQQ", "PS")].note


def test_dsr_table_carries_both_benchmarks_and_the_null_one_uses_the_smallest_sleeve():
    df = _positions({("SPY", "PS"): [0.05, 0.06, 0.04, -0.02], ("SPY", "IC"): [0.03, -0.2], ("QQQ", "PS"): [0.060, 0.061], ("QQQ", "IC"): [0.02, -0.05]}, n=40)
    tab = H.dsr_table(df)
    assert {"sr_star", "deflated_sr", "sr_star_null", "deflated_sr_null"} <= set(tab.columns)
    assert tab.var_null.iloc[0] == pytest.approx(1 / 40)
    qqq = tab[tab.sleeve == "QQQ-PS"].iloc[0]
    assert qqq.sr > 5 and tab.sr_star.iloc[0] > tab.sr_star_null.iloc[0]      # the loss-free sleeve inflates the empirical charge
    spy = tab[tab.sleeve == "SPY-PS"].iloc[0]
    assert spy.deflated_sr_null > 0 and spy.deflated_sr < 0
