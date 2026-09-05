"""P5: the validation harness on synthetic trade rows (DESIGN/70 §4)."""
from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd
import pytest

from engine import calendar as cal
from engine.config import GO_MIN_EVENTS
from engine.validation import harness as H

pytestmark = pytest.mark.unit


def _trades(n_dates=40, per_date=3, start=date(2026, 7, 6), mean=0.01, sd=0.03, seed=0, season="S2"):
    rng = np.random.default_rng(seed)
    days = cal.trading_days(start, start + timedelta(days=200))[:n_dates]
    rows = []
    for d in days:
        for i in range(per_date):
            base = rng.normal(mean, sd)
            for v in ("A1", "A2"):
                if v == "A2" and i == 0:
                    continue                      # A2 is a subset of A1
                for s, adj in (("SS", 0.0), ("IC", -0.004)):
                    rows.append({"ticker": f"T{i}", "E": d, "pre": d, "post": cal.next_session(d), "variant": v,
                                 "structure": s, "net_pct": base + adj, "gross_pct": base + adj + 0.006,
                                 "cost_pct": 0.006, "gross_usd": (base + adj + 0.006) * 5000, "cost_usd": 30.0,
                                 "net_usd": (base + adj) * 5000, "n": 1, "notional_usd": 5000.0,
                                 "stress_loss_usd": 900.0, "max_loss_usd": 400.0, "model_exit": i == 2,
                                 "sector": "Energy" if i else "Technology", "mcap_bucket": "2-10B",
                                 "timing": "postmarket", "regime_pre": "CHOP", "month": d.strftime("%Y-%m"),
                                 "season": season, "straddle_over_implied": 1.2, "implied": 0.08,
                                 "cap_pass": True})
    return pd.DataFrame(rows)


def test_season_labels():
    assert H.season_of(date(2026, 4, 1)) == "S1" and H.season_of(date(2026, 6, 15)) == "S1"
    assert H.season_of(date(2026, 7, 1)) == "S2" and H.season_of(date(2026, 9, 4)) == "S2"
    assert H.season_of(date(2026, 10, 1)) == "S3" and H.season_of(date(2026, 6, 20)) == "off"


def test_primary_table_has_pairs_by_season_and_pooled():
    t = _trades()
    tab = H.primary_table(t)
    assert set(tab.season) == {"S2", "pooled"}
    row = tab[(tab.variant == "A1") & (tab.structure == "SS") & (tab.season == "S2")].iloc[0]
    sub = t[(t.variant == "A1") & (t.structure == "SS")]
    assert row.n == len(sub) and row.dates == sub.pre.nunique()
    assert row.mean_net_pct == pytest.approx(sub.net_pct.mean())
    assert {"t", "p", "hit", "median_net_pct", "mean_gross_pct", "mean_cost_pct"} <= set(tab.columns)


def test_bh_table_marks_the_four_primary_tests():
    tab = H.bh_table(_trades(mean=0.02, sd=0.02), "S2")
    assert len(tab) == 4 and tab.bh_pass.all()
    flat = _trades()
    flat = flat.assign(net_pct=np.where(flat.pre.rank(method="dense") % 2 == 0, 0.01, -0.01))  # mean 0, t 0
    null = H.bh_table(flat, "S2")
    assert len(null) == 4 and not null.bh_pass.any()


def test_dsr_table_reports_sharpe_deflation_for_each_pair():
    tab = H.dsr_table(_trades(mean=0.02, sd=0.02), "S2")
    assert len(tab) == 4
    assert {"sr", "sr_star", "deflated_sr", "dsr_prob", "skew", "kurt", "n_trials"} <= set(tab.columns)
    assert (tab.n_trials == H.DSR_TRIALS).all() and (tab.deflated_sr > 0).all()


def test_pbo_on_daily_config_pnl():
    rep = H.pbo_report(_trades(n_dates=64, mean=0.0, sd=0.05, seed=2), "S2", n_blocks=8)
    assert 0.0 <= rep["pbo"] <= 1.0 and rep["n_configs"] == 4


def test_tail_report_fields_and_arithmetic():
    t = _trades()
    rep = H.tail_report(t, "A1", "SS", "S2")
    sub = t[(t.variant == "A1") & (t.structure == "SS")]
    assert len(rep["worst_10"]) == 10
    assert rep["worst_event_pct"] == pytest.approx(sub.net_pct.min())
    assert rep["mean_without_worst_1pct"] > rep["mean_net_pct"] > rep["mean_without_best_1pct"]
    assert 0 <= rep["worst_decile_share_of_loss"] <= 1
    assert "stress_breaches" in rep and rep["mean_win_pct"] > 0


def test_robustness_recomputes_costs_and_filters_model_exits():
    t = _trades()
    rep = H.robustness_table(t, "S2", rerun=None)
    kinds = set(rep.sensitivity)
    assert {"base", "no_model_exit", "costs_x2"} <= kinds
    base = rep[(rep.sensitivity == "base") & (rep.variant == "A1") & (rep.structure == "SS")].iloc[0]
    x2 = rep[(rep.sensitivity == "costs_x2") & (rep.variant == "A1") & (rep.structure == "SS")].iloc[0]
    assert x2.mean_net_pct == pytest.approx(base.mean_net_pct - base.mean_cost_pct)
    nme = rep[(rep.sensitivity == "no_model_exit") & (rep.variant == "A1") & (rep.structure == "SS")].iloc[0]
    assert nme.n < base.n


def test_go_no_go_verdicts():
    good = _trades(n_dates=30, per_date=3, mean=0.03, sd=0.02, start=date(2026, 10, 1), season="S3")
    prior = pd.concat([_trades(mean=0.01, start=date(2026, 4, 6), season="S1"), _trades(mean=0.01, season="S2")])
    verdict = H.go_no_go(pd.concat([prior, good]))
    a1ss = verdict[(verdict.variant == "A1") & (verdict.structure == "SS")].iloc[0]
    assert a1ss.n_s3 >= GO_MIN_EVENTS and a1ss.verdict == "GO"
    small = _trades(n_dates=10, per_date=2, mean=0.03, sd=0.02, start=date(2026, 10, 1), season="S3")
    v2 = H.go_no_go(pd.concat([prior, small]))
    assert (v2.verdict == "PROVISIONAL").any() and "N >= 60" in v2.iloc[0].note
    bad = _trades(n_dates=30, per_date=3, mean=-0.02, sd=0.02, start=date(2026, 10, 1), season="S3")
    assert (H.go_no_go(pd.concat([prior, bad])).verdict == "NO-GO").all()
    assert (H.go_no_go(prior).verdict == "NOT YET").all()


def test_reproduce_e1_compares_to_reference():
    ev = pd.DataFrame({"proxy_pnl": [0.02, 0.01, 0.03, -0.01], "pre": [date(2026, 5, 1)] * 2 + [date(2026, 5, 4)] * 2})
    rep = H.reproduce_e1(ev, reference={"n": 4, "mean": 0.0125, "t": 1.0})
    assert rep["n"] == 4 and rep["mean"] == pytest.approx(0.0125) and rep["n_match"] and rep["mean_match"]
    assert not H.reproduce_e1(ev, reference={"n": 5, "mean": 0.0125, "t": 1.0})["n_match"]


def test_md_table_renders():
    tab = H.primary_table(_trades())
    md = H.md(tab)
    assert md.startswith("|") and "A1" in md
