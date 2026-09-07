"""engine.watch.retro: the pure/logic pieces of the panel assembly (cross-sectional deciles,
null helpers, condition evaluation wiring, stacks/baskets attachment). The I/O-heavy pieces
(`build_universe`, `attach_short_side`, `attach_tier1`, `attach_leap_dp`, `warm_bars_cache`) are
exercised end-to-end by `make watch-retro` against the real panel, not here."""
from __future__ import annotations

from datetime import date

import pandas as pd
import pytest

from engine.watch import conditions as C
from engine.watch import retro as R
from engine.watch import series as S

pytestmark = pytest.mark.unit


def test_decile_flag_top_decile_and_null_safety():
    s = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, None])
    flag = R._decile_flag(s)
    assert flag.iloc[8] is True or flag.iloc[8] == True  # 9.0 is the top value among 9 non-null -> top decile
    assert flag.iloc[0] is False or flag.iloc[0] == False
    assert flag.iloc[9] is None


def test_add_cross_sectional_deciles_is_computed_per_night():
    d1, d2 = date(2026, 1, 5), date(2026, 1, 6)
    df = pd.DataFrame({
        "ticker": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"] * 2,
        "date": [d1] * 10 + [d2] * 10,
        "oi_net_5d": list(range(10)) + [None] * 10,
        "netprem_mcap": [None] * 10 + list(range(10)),
    })
    out = R.add_cross_sectional_deciles(df)
    night1 = out[out.date == d1]
    assert night1[night1.ticker == "J"]["c_oibuild_raw"].iloc[0] is True   # value 9, the max
    assert night1["c_crowd_raw"].isna().all() or (night1["c_crowd_raw"] == None).all()  # noqa: E711
    night2 = out[out.date == d2]
    assert night2[night2.ticker == "J"]["c_crowd_raw"].iloc[0] is True


def test_is_missing_and_dp_flag():
    assert R._is_missing(None) is True
    assert R._is_missing(pd.NA) is True
    assert R._is_missing(float("nan")) is True
    assert R._is_missing(0.0) is False
    assert R._dp_flag(None) is None
    assert R._dp_flag(6_000_000.0) is True
    assert R._dp_flag(1_000_000.0) is False


def test_to_bool_or_none():
    assert R._to_bool_or_none(True) is True
    assert R._to_bool_or_none(False) is False
    assert R._to_bool_or_none(None) is None
    assert R._to_bool_or_none(pd.NA) is None


def test_evaluate_conditions_wires_inputs_through_to_the_right_condition(monkeypatch):
    d = date(2026, 6, 9)
    universe = pd.DataFrame([{
        "ticker": "X", "date": d, "pct_52w_range": 0.9, "days_to_cover": None,
        "borrow_fee_pct": None, "c_oibuild_raw": True, "c_crowd_raw": False,
        "ivrank_chg_5d": 15.0, "iv30d": 0.5, "marketcap": 5e9, "has_tier1_atm_pair": True,
        "next_earnings_date": None, "c_leap_raw": True, "dp_prem": 6_000_000.0,
    }])
    # no bars for X -> every bar-derived condition must be None
    out = R.evaluate_conditions(universe, series_map={})
    row = out.to_dict("records")[0]      # to_dict, like the production pipeline, native Python types
    assert row["C-HIGH"] is True         # pct_52w_range 0.9 >= 0.85
    assert row["C-LOW"] is False
    assert row["C-SHORT"] is None        # both short inputs missing
    assert row["C-OIBUILD"] is True
    assert row["C-CROWD"] is False
    assert row["C-IVUP"] is True
    assert row["C-VOL"] is None          # earnings date unknown, everything else passes
    assert row["C-RSI"] is None
    assert row["C-LEAP"] is True
    assert row["C-DP"] is True


def test_add_stacks_and_baskets_end_to_end():
    row = {cid: False for cid in C.ALL_CONDITIONS}
    row["C-HIGH"] = True
    row["C-IVUP"] = True
    row["C-DIV"] = True   # bull=3
    cond_df = pd.DataFrame([{"ticker": "X", "date": date(2026, 6, 9), **row}])
    out = R.add_stacks_and_baskets(cond_df)
    assert out.iloc[0]["bull"] == 3
    assert out.iloc[0]["bear"] == 0
    assert bool(out.iloc[0]["LONG"]) is True
