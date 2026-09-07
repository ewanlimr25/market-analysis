"""G4/G5 exploration row generator (RESEARCH/47 §2; DESIGN/100 §2-3): policy stamping, key
uniqueness, direction/sign convention, and grading, all on synthetic factor tables (no I/O)."""
from __future__ import annotations

from datetime import date

import numpy as np
import pandas as pd
import pytest

from engine import policy as POL
from engine.strategies import xs as XS

pytestmark = pytest.mark.unit


def _week(n=24, factor_cols=("iv_spread", "put_skew")) -> pd.DataFrame:
    rng = np.random.default_rng(1)
    data = {"ticker": [f"T{i:02d}" for i in range(n)], "formation_date": [date(2026, 8, 21)] * n}
    for c in factor_cols:
        data[c] = rng.normal(size=n)
    return pd.DataFrame(data)


def test_build_rows_stamps_policy_role_and_gate_verdict():
    rows = XS.build_rows(_week(), factors=("iv_spread",))
    assert (rows["policy_id"] == XS.POLICY_ID).all()
    assert (rows["role"] == POL.ROLE_EXPLORATION).all()
    assert set(rows["gate_verdict"]) == {"iv_spread:top", "iv_spread:bottom"}
    POL.require_policy_columns(rows)     # raises on any violation


def test_build_rows_ten_names_a_side_equal_weight():
    rows = XS.build_rows(_week(n=40), factors=("iv_spread",))
    top = rows[(rows.factor == "iv_spread") & (rows.side == "top")]
    bottom = rows[(rows.factor == "iv_spread") & (rows.side == "bottom")]
    assert len(top) == XS.N_PER_SIDE and len(bottom) == XS.N_PER_SIDE
    assert np.allclose(rows["weight"].to_numpy(), 1.0 / XS.N_PER_SIDE)
    assert set(top["ticker"]).isdisjoint(set(bottom["ticker"]))


def test_build_rows_shrinks_both_sides_when_universe_is_small_and_never_overlaps():
    rows = XS.build_rows(_week(n=7), factors=("iv_spread",))   # 7 // 2 = 3 a side
    top = rows[rows.side == "top"]
    bottom = rows[rows.side == "bottom"]
    assert len(top) == 3 and len(bottom) == 3
    assert set(top["ticker"]).isdisjoint(set(bottom["ticker"]))


def test_build_rows_empty_universe_is_empty_frame():
    rows = XS.build_rows(pd.DataFrame(columns=["ticker", "formation_date", "iv_spread"]),
                          formation_date=date(2026, 8, 21), factors=("iv_spread",))
    assert rows.empty


def test_top_decile_ranks_the_highest_factor_values_first():
    week = pd.DataFrame({"ticker": ["A", "B", "C", "D"], "formation_date": [date(2026, 8, 21)] * 4,
                          "iv_spread": [0.05, -0.02, 0.09, 0.01]})
    rows = XS.build_rows(week, factors=("iv_spread",))
    top = rows[rows.side == "top"].sort_values("rank")
    assert top["ticker"].tolist() == ["C", "A"]      # 2-a-side (4 // 2), descending by factor_value


def test_direction_matches_the_pre_registered_hypothesis_sign():
    week = _week(n=8, factor_cols=("iv_spread", "put_skew", "os_ratio", "d_iv_spread"))
    rows = XS.build_rows(week, factors=tuple(week.columns[2:]))
    for factor, sign in XS.FACTOR_SIGN.items():
        top_dir = rows[(rows.factor == factor) & (rows.side == "top")]["direction"].unique()
        bottom_dir = rows[(rows.factor == factor) & (rows.side == "bottom")]["direction"].unique()
        expected_top = XS.DIRECTION_LONG if sign > 0 else XS.DIRECTION_SHORT
        expected_bottom = XS.DIRECTION_SHORT if sign > 0 else XS.DIRECTION_LONG
        assert list(top_dir) == [expected_top]
        assert list(bottom_dir) == [expected_bottom]


def test_check_key_unique_true_for_generator_output_false_on_a_forced_duplicate():
    rows = XS.build_rows(_week(), factors=("iv_spread", "put_skew"))
    assert XS.check_key_unique(rows)
    duped = pd.concat([rows, rows.iloc[[0]]], ignore_index=True)
    assert not XS.check_key_unique(duped)


def test_key_uniqueness_holds_across_multiple_formation_weeks():
    week1 = XS.build_rows(_week(factor_cols=("iv_spread",)), factors=("iv_spread",))
    week2_df = _week(factor_cols=("iv_spread",))
    week2_df["formation_date"] = date(2026, 8, 28)
    week2 = XS.build_rows(week2_df, factors=("iv_spread",))
    combined = pd.concat([week1, week2], ignore_index=True)
    assert XS.check_key_unique(combined)


def test_grade_rows_flips_sign_for_short_direction():
    week = pd.DataFrame({"ticker": ["A", "B"], "formation_date": [date(2026, 8, 21)] * 2,
                          "put_skew": [0.05, -0.05]})       # A top(short), B bottom(long) w/ n=1/side
    rows = XS.build_rows(week, factors=("put_skew",))
    outcomes = {("A", date(2026, 8, 21)): 0.02, ("B", date(2026, 8, 21)): -0.03}
    graded = XS.grade_rows(rows, lambda ticker, d: outcomes.get((ticker, d)))
    a = graded[graded.ticker == "A"].iloc[0]
    b = graded[graded.ticker == "B"].iloc[0]
    assert a["direction"] == "short" and a["realized_excess"] == pytest.approx(-0.02)
    assert b["direction"] == "long" and b["realized_excess"] == pytest.approx(-0.03)


def test_grade_rows_empty_input():
    out = XS.grade_rows(pd.DataFrame(columns=XS.ROW_COLUMNS), lambda t, d: None)
    assert out.empty
    assert "realized_excess" in out.columns
