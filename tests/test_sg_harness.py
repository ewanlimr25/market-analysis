"""S-G validation harness (DESIGN/91 §4): clustered t by entry day, the spread-half split, the
gross ramp decomposition summary, and the go/no-go bar."""
from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd
import pytest

from engine import calendar as cal
from engine.config import SG_DSR_TRIALS
from engine.validation import sg_harness as SH

pytestmark = pytest.mark.unit


def _trades(n_dates=30, per_date=4, start=date(2026, 4, 6), mean=0.05, sd=0.05, seed=0,
           season="S1", low_spread_bonus=0.0):
    rng = np.random.default_rng(seed)
    days = cal.trading_days(start, start + timedelta(days=120))[:n_dates]
    rows = []
    for d in days:
        for i in range(per_date):
            base = rng.normal(mean, sd)
            spread = 0.03 if i % 2 == 0 else 0.12                # half low, half wide
            adj = low_spread_bonus if spread > 0.05 else 0.0     # bonus applies to the wide-spread half
            for v in ("G3_3", "G3_5"):
                for s in ("LS", "LG"):
                    pnl = base + adj + (0.0 if s == "LS" else -0.01)
                    rows.append({"ticker": f"T{i}", "E": d, "pre": d, "post": cal.next_session(d),
                                "entry_day": cal.prev_session(d, 3), "offset": 3 if v == "G3_3" else 5,
                                "variant": v, "structure": s, "net_pct": pnl, "gross_pct": pnl + 0.01,
                                "cost_pct": 0.01, "gross_usd": (pnl + 0.01) * 5000, "cost_usd": 50.0,
                                "net_usd": pnl * 5000, "contracts": 1, "notional_usd": 5000.0,
                                "atm_spread_entry": spread, "season": season,
                                "net_pct_prem": pnl * 8, "unhedged_pnl_pct": pnl + 0.01, "delta_pnl_pct": 0.002,
                                "delta_hedged_pnl_pct": pnl + 0.008, "vega_pnl_pct": pnl + 0.005,
                                "residual_pnl_pct": 0.003})
    return pd.DataFrame(rows)


def test_primary_table_clusters_by_entry_day_not_pre():
    t = _trades()
    tab = SH.primary_table(t)
    row = tab[(tab.variant == "G3_3") & (tab.structure == "LS") & (tab.season == "S1")].iloc[0]
    sub = t[(t.variant == "G3_3") & (t.structure == "LS") & (t.season == "S1")]
    assert row.dates == sub.entry_day.nunique()
    assert row.n == len(sub)


def test_dsr_table_uses_ten_trial_charge():
    tab = SH.dsr_table(_trades(mean=0.05, sd=0.02), "S1")
    assert len(tab) == 4
    assert (tab.n_trials == SG_DSR_TRIALS).all()


def test_spread_median_and_half_table():
    t = _trades(mean=0.02, sd=0.01)
    median = SH.spread_median(t)
    assert median == pytest.approx(0.075)  # bimodal 0.03/0.12 input, even split -> midpoint
    halves = SH.spread_half_table(t, median)
    assert set(halves.half) == {"low", "wide"}
    assert len(halves) == 2 * len(SH.SG_PAIRS)


def test_decomposition_summary_groups_by_season():
    t = pd.concat([_trades(season="S1", mean=0.03), _trades(season="S2", mean=0.04, start=date(2026, 7, 6))])
    summary = SH.decomposition_summary(t, ("season",))
    assert set(summary.season) == {"S1", "S2"}
    for col in ("unhedged_pnl_pct", "delta_pnl_pct", "delta_hedged_pnl_pct", "vega_pnl_pct", "residual_pnl_pct"):
        assert col in summary.columns


def test_go_no_go_pass_when_both_seasons_positive_t_above_bar_and_low_spread_positive():
    t = pd.concat([_trades(season="S1", mean=0.05, sd=0.02, start=date(2026, 4, 6)),
                  _trades(season="S2", mean=0.05, sd=0.02, start=date(2026, 7, 6))])
    verdict = SH.go_no_go(t)
    row = verdict[(verdict.variant == "G3_3") & (verdict.structure == "LS")].iloc[0]
    assert row.verdict == "PASS"


def test_go_no_go_killed_when_a_season_is_non_positive():
    t = pd.concat([_trades(season="S1", mean=-0.01, sd=0.02, start=date(2026, 4, 6)),
                  _trades(season="S2", mean=0.05, sd=0.02, start=date(2026, 7, 6))])
    verdict = SH.go_no_go(t)
    row = verdict[(verdict.variant == "G3_3") & (verdict.structure == "LS")].iloc[0]
    assert row.verdict == "KILLED"
    assert "Season" in row.note or "season" in row.note


def test_go_no_go_killed_when_positive_only_in_wide_spread_half():
    # both seasons positive overall and t clears the bar, but only via the wide-spread rows
    t = pd.concat([
        _trades(season="S1", mean=-0.06, sd=0.005, start=date(2026, 4, 6), low_spread_bonus=0.20),
        _trades(season="S2", mean=-0.06, sd=0.005, start=date(2026, 7, 6), low_spread_bonus=0.20),
    ])
    verdict = SH.go_no_go(t)
    row = verdict[(verdict.variant == "G3_3") & (verdict.structure == "LS")].iloc[0]
    assert row.mean_low_spread <= 0 < row.mean_wide_spread
    if row.mean_s1 > 0 and row.mean_s2 > 0 and row.t_pooled >= 2.0:
        assert row.verdict == "KILLED"
        assert "wide" in row.note
