"""engine.research.intraday_flow_cells: outcome join, cell stats, BH + sign-stability, and the
OPENING/CLOSING/MIXED descriptive table (G2, RESEARCH/47-edge-gaps.md §2). All synthetic; no panel
or DuckDB dependency.
"""
from __future__ import annotations

from datetime import date, datetime, timedelta

import numpy as np
import pandas as pd
import pytest

from engine.research import intraday_flow_cells as cells

pytestmark = pytest.mark.unit

D = date(2026, 7, 29)


def wall(hh: int, mm: int, ss: int = 0, d: date = D) -> pd.Timestamp:
    return pd.Timestamp(datetime(d.year, d.month, d.day, hh, mm, ss))


def path_row(underlying: str, hh: int, mm: int, price: float, n: int = 5) -> dict:
    ts = wall(hh, mm)
    return {"date": D, "underlying_symbol": underlying, "bucket_ts": ts.floor("5min"),
            "last_price": price, "last_ts": ts, "n_prints": n}


# ----------------------------------------------------------------------------- join_outcomes


def make_event(et: pd.Timestamp, underlying: str, entry_price: float, direction: str) -> dict:
    return {"date": D, "underlying_symbol": underlying, "option_chain_id": f"{underlying}-X",
            "et": et, "entry_underlying_price": entry_price, "direction": direction,
            "size_bucket": "250k_1m", "dte_bucket": "0_7", "tod_bucket": "09:35-11:00",
            "classification_oi": "OPENING", "opening_proxy_volume": True}


def test_join_outcomes_computes_signed_excess_over_spy():
    events = pd.DataFrame([make_event(wall(10, 0), "AAA", 100.0, "bullish")])
    path = pd.DataFrame([
        path_row("AAA", 10, 0, 100.0), path_row("AAA", 10, 30, 102.0),   # +2% at +30min
        path_row("SPY", 10, 0, 500.0), path_row("SPY", 10, 30, 501.0),   # +0.2% at +30min
    ])
    out = cells.join_outcomes(events, path, horizons=(30,), tolerance_min=10)
    row = out.iloc[0]
    expected_raw = np.log(102.0 / 100.0)
    expected_spy = np.log(501.0 / 500.0)
    assert row["excess"] == pytest.approx(expected_raw - expected_spy)
    assert not row["outcome_dropped"]


def test_join_outcomes_flips_sign_for_bearish_direction():
    events = pd.DataFrame([make_event(wall(10, 0), "AAA", 100.0, "bearish")])
    path = pd.DataFrame([
        path_row("AAA", 10, 0, 100.0), path_row("AAA", 10, 30, 102.0),
        path_row("SPY", 10, 0, 500.0), path_row("SPY", 10, 30, 500.0),
    ])
    out = cells.join_outcomes(events, path, horizons=(30,), tolerance_min=10)
    expected_raw = np.log(102.0 / 100.0)
    assert out.iloc[0]["excess"] == pytest.approx(-1.0 * expected_raw)


def test_join_outcomes_drops_when_no_observation_within_tolerance():
    events = pd.DataFrame([make_event(wall(10, 0), "AAA", 100.0, "bullish")])
    # nearest AAA observation to the +30min target (10:30) is at 10:15 -- 15 minutes away
    path = pd.DataFrame([
        path_row("AAA", 10, 0, 100.0), path_row("AAA", 10, 15, 101.0),
        path_row("SPY", 10, 0, 500.0), path_row("SPY", 10, 30, 500.0),
    ])
    out = cells.join_outcomes(events, path, horizons=(30,), tolerance_min=10)
    assert out.iloc[0]["outcome_dropped"]
    assert np.isnan(out.iloc[0]["excess"])


def test_join_outcomes_excluded_direction_has_no_excess_but_is_present():
    events = pd.DataFrame([make_event(wall(10, 0), "AAA", 100.0, "excluded")])
    path = pd.DataFrame([
        path_row("AAA", 10, 0, 100.0), path_row("AAA", 10, 30, 102.0),
        path_row("SPY", 10, 0, 500.0), path_row("SPY", 10, 30, 501.0),
    ])
    out = cells.join_outcomes(events, path, horizons=(30,), tolerance_min=10)
    assert len(out) == 1 and out.iloc[0]["outcome_dropped"] and np.isnan(out.iloc[0]["excess"])


def test_join_outcomes_asof_never_matches_a_later_observation():
    # backward-only: a later, closer-looking price must not be used as the +30min exit
    events = pd.DataFrame([make_event(wall(10, 0), "AAA", 100.0, "bullish")])
    path = pd.DataFrame([
        path_row("AAA", 10, 0, 100.0), path_row("AAA", 10, 25, 103.0),   # at-or-before 10:30
        path_row("AAA", 10, 35, 999.0),                                  # after target, ignored
        path_row("SPY", 10, 0, 500.0), path_row("SPY", 10, 30, 500.0),
    ])
    out = cells.join_outcomes(events, path, horizons=(30,), tolerance_min=10)
    assert out.iloc[0]["excess"] == pytest.approx(np.log(103.0 / 100.0))


def test_join_outcomes_produces_one_row_per_event_per_horizon():
    events = pd.DataFrame([make_event(wall(10, 0), "AAA", 100.0, "bullish")])
    base = wall(10, 0)
    offsets = range(0, 130, 5)
    aaa = [{**path_row("AAA", 10, 0, 0.0), "last_ts": base + timedelta(minutes=m),
           "bucket_ts": (base + timedelta(minutes=m)).floor("5min"), "last_price": 100.0 + m * 0.01}
          for m in offsets]
    spy = [{**path_row("SPY", 10, 0, 0.0), "last_ts": base + timedelta(minutes=m),
           "bucket_ts": (base + timedelta(minutes=m)).floor("5min"), "last_price": 500.0}
          for m in offsets]
    path = pd.DataFrame(aaa + spy)
    out = cells.join_outcomes(events, path, horizons=(30, 60, 120), tolerance_min=10)
    assert sorted(out["horizon"].unique()) == [30, 60, 120]
    assert len(out) == 3


# ----------------------------------------------------------------------------- cell_stats


def _long_row(**over) -> dict:
    base = {"date": D, "underlying_symbol": "AAA", "option_chain_id": "X", "direction": "bullish",
            "size_bucket": "250k_1m", "dte_bucket": "0_7", "tod_bucket": "09:35-11:00",
            "classification_oi": "OPENING", "opening_proxy_volume": True, "horizon": 30,
            "raw_ret": 0.01, "spy_ret": 0.0, "excess": 0.01, "outcome_dropped": False}
    base.update(over)
    return base


def test_cell_stats_groups_by_all_six_dims_and_computes_clustered_t():
    rng = np.random.default_rng(1)
    rows = []
    for i in range(30):
        rows.append(_long_row(underlying_symbol=f"U{i % 5}", date=D if i % 2 == 0 else
                              date(2026, 7, 30), excess=float(rng.normal(0.005, 0.01))))
    long_df = pd.DataFrame(rows)
    out = cells.cell_stats(long_df)
    assert len(out) == 1
    row = out.iloc[0]
    assert row["n"] == 30
    assert row["mean"] == pytest.approx(long_df["excess"].mean())
    assert row["Ga"] == 5   # 5 distinct underlyings
    assert row["Gb"] == 2   # 2 distinct dates


def test_cell_stats_excludes_non_directional_and_dropped_rows():
    long_df = pd.DataFrame([
        _long_row(direction="bullish", excess=0.01),
        _long_row(direction="excluded", excess=np.nan, outcome_dropped=True),
        _long_row(direction="bullish", excess=np.nan, outcome_dropped=True),
    ])
    out = cells.cell_stats(long_df)
    assert len(out) == 1 and out.iloc[0]["n"] == 1


def test_cell_stats_empty_input_returns_empty_frame_with_expected_columns():
    out = cells.cell_stats(pd.DataFrame(columns=list(cells.OUTCOME_COLUMNS)))
    assert out.empty
    assert "t" in out.columns and "p" in out.columns


# ----------------------------------------------------------------------------- BH + stability


def test_add_bh_and_stability_marks_a_pooled_significant_sign_stable_cell_a_survivor():
    early_dates = [date(2026, 3, d) for d in (13, 16, 17, 18, 19)]
    late_dates = [date(2026, 8, d) for d in (1, 2, 3, 4, 5)]
    rows = []
    for i in range(40):
        d = early_dates[i % 5] if i < 20 else late_dates[i % 5]
        rows.append(_long_row(underlying_symbol=f"U{i}", date=d, excess=0.02 + 0.001 * (i % 3)))
    long_df = pd.DataFrame(rows)
    cell_df = cells.cell_stats(long_df)
    out = cells.add_bh_and_stability(cell_df, long_df, fdr=0.05)
    assert out.iloc[0]["tested"]
    assert out.iloc[0]["bh_reject"]
    assert out.iloc[0]["sign_stable"]
    assert out.iloc[0]["survivor"]


def test_add_bh_and_stability_rejects_a_sign_flipping_cell():
    d1, d2 = date(2026, 3, 13), date(2026, 8, 1)
    rows = []
    for i in range(40):
        d = d1 if i < 20 else d2
        sign = 1.0 if d == d1 else -1.0
        rows.append(_long_row(underlying_symbol=f"U{i}", date=d, excess=sign * 0.02))
    long_df = pd.DataFrame(rows)
    cell_df = cells.cell_stats(long_df)
    out = cells.add_bh_and_stability(cell_df, long_df, fdr=0.05)
    assert not out.iloc[0]["sign_stable"]
    assert not out.iloc[0]["survivor"]


def test_add_bh_and_stability_marks_undefined_p_cells_untested_and_never_bh_rejected():
    long_df = pd.DataFrame([_long_row(excess=0.01)])   # a single observation: se undefined
    cell_df = cells.cell_stats(long_df)
    out = cells.add_bh_and_stability(cell_df, long_df, fdr=0.05)
    assert not out.iloc[0]["tested"]
    assert not out.iloc[0]["bh_reject"]
    assert not out.iloc[0]["survivor"]


def test_add_bh_and_stability_gates_on_minimum_cluster_count_per_dimension():
    # 5 underlyings, but every one of them trades on only one of two days -> Gb=2, and the
    # (underlying, day) intersection is collinear with the underlying dimension in this cell.
    # Two-way clustering can manufacture a tiny SE (and hence a huge |t|) in exactly this shape;
    # the cell must still come out untested because Gb < MIN_CLUSTERS_PER_DIM.
    d1, d2 = date(2026, 3, 13), date(2026, 3, 16)
    rows = []
    for i, u in enumerate(["A", "B", "C", "D", "E"]):
        d = d1 if u == "A" else d2
        n = 2 if u == "A" else 60
        for _ in range(n):
            rows.append(_long_row(underlying_symbol=u, date=d, excess=-0.0005 + 0.00001 * i))
    long_df = pd.DataFrame(rows)
    cell_df = cells.cell_stats(long_df)
    out = cells.add_bh_and_stability(cell_df, long_df, fdr=0.05)
    row = out.iloc[0]
    assert row["Ga"] == 5 and row["Gb"] == 2
    assert not row["tested"]
    assert not row["bh_reject"]
    assert not row["survivor"]


# ----------------------------------------------------------------------------- descriptive table


def test_descriptive_oi_share_sums_to_one_within_a_tod_and_side_group():
    events = pd.DataFrame([
        {"tod_bucket": "09:35-11:00", "direction": "bullish", "classification_oi": "OPENING", "premium": 300_000.0},
        {"tod_bucket": "09:35-11:00", "direction": "bullish", "classification_oi": "MIXED", "premium": 700_000.0},
        {"tod_bucket": "09:35-11:00", "direction": "bearish", "classification_oi": "CLOSING", "premium": 500_000.0},
    ])
    out = cells.descriptive_oi_share(events)
    bullish_total = out[(out["tod_bucket"] == "09:35-11:00") & (out["direction"] == "bullish")]
    assert bullish_total["premium_share"].sum() == pytest.approx(1.0)
    opening_row = bullish_total[bullish_total["classification_oi"] == "OPENING"].iloc[0]
    assert opening_row["premium_share"] == pytest.approx(0.3)


def test_descriptive_oi_share_empty_input():
    out = cells.descriptive_oi_share(pd.DataFrame(columns=["tod_bucket", "direction",
                                                            "classification_oi", "premium"]))
    assert out.empty
