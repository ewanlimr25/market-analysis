"""G1 step 2 (`engine/improve/g1_remark.py`): the re-marking treatments, on small synthetic
frames shaped like `data/backtest/trades.parquet`."""
from __future__ import annotations

import math
from datetime import date

import pandas as pd
import pytest

from engine import marking as M
from engine.config import COMMISSION_PER_CONTRACT, CONTRACT_MULTIPLIER, MODEL_SPREAD_FLOOR
from engine.improve import fills as G
from engine.improve import g1_remark as R

pytestmark = pytest.mark.unit


def _ss_row(**kw) -> dict:
    base = dict(ticker="XYZ", expiry=date(2026, 8, 21), k=100.0, k_up=None, k_dn=None, contracts=2,
                notional_usd=100.0 * CONTRACT_MULTIPLIER * 2,
                call_id="XYZ260821C00100000", call_entry=2.00, call_entry_spread=0.04, call_entry_tier=1,
                call_exit=1.00, call_exit_spread=0.10, call_exit_tier=1,
                put_id="XYZ260821P00100000", put_entry=2.00, put_entry_spread=0.04, put_entry_tier=1,
                put_exit=1.00, put_exit_spread=0.10, put_exit_tier=1,
                wing_call_id=None, wing_put_id=None)
    base.update(kw)
    return base


def _ic_row(**kw) -> dict:
    base = _ss_row(k_up=110.0, k_dn=90.0,
                   wing_call_id="XYZ260821C00110000", wing_call_entry=0.30, wing_call_entry_spread=0.20,
                   wing_call_entry_tier=3, wing_call_exit=0.05, wing_call_exit_spread=0.20, wing_call_exit_tier=3,
                   wing_put_id="XYZ260821P00090000", wing_put_entry=0.30, wing_put_entry_spread=0.20,
                   wing_put_entry_tier=3, wing_put_exit=0.05, wing_put_exit_spread=0.20, wing_put_exit_tier=3)
    base.update(kw)
    return base


# ----------------------------------------------------------------------------- present_legs / build_legs

def test_present_legs_ss_vs_ic():
    assert R.present_legs(_ss_row()) == ["call", "put"]
    assert R.present_legs(_ic_row()) == ["call", "put", "wing_call", "wing_put"]


def test_build_legs_default_uses_original_marks():
    row = _ss_row()
    legs = R.build_legs(row)
    assert len(legs) == 2
    call = next(l for l in legs if l.name == "call")
    assert call.side == R.ST.SHORT
    assert call.entry.price == 2.00 and call.exit.price == 1.00
    assert call.contract.option_type == "call" and call.contract.strike == 100.0


def test_build_legs_wing_side_is_long():
    row = _ic_row()
    legs = R.build_legs(row)
    wing_call = next(l for l in legs if l.name == "wing_call")
    assert wing_call.side == R.ST.LONG
    assert wing_call.contract.strike == 110.0


def test_build_legs_excludes_leg_with_no_new_mark():
    row = _ss_row()
    legs = R.build_legs(row, exit_marks={"call": M.Mark(0.9, 0.1, 1, "x"), "put": None})
    assert [l.name for l in legs] == ["call"]


# ----------------------------------------------------------------------------- mid-share lookup

def test_build_mid_share_lookup():
    fills_window = pd.DataFrame([
        {"tier": 1, "dim2": "early", "class": G.CLASS_AT_OR_BETTER_MID, "volume": 60.0, "premium": 600.0},
        {"tier": 1, "dim2": "early", "class": G.CLASS_AT_TOUCH, "volume": 40.0, "premium": 400.0},
        {"tier": 1, "dim2": "late", "class": G.CLASS_AT_OR_BETTER_MID, "volume": 10.0, "premium": 100.0},
        {"tier": 1, "dim2": "late", "class": G.CLASS_AT_TOUCH, "volume": 90.0, "premium": 900.0},
    ])
    lookup = R.build_mid_share_lookup(fills_window)
    assert lookup[(1, "early")] == pytest.approx(0.6)
    assert lookup[(1, "late")] == pytest.approx(0.1)


def test_qualifies_for_mid_fill():
    lookup = {(1, "early"): 0.6, (2, "early"): 0.4}
    assert R.qualifies_for_mid_fill(1, "early", lookup)
    assert not R.qualifies_for_mid_fill(2, "early", lookup)
    assert not R.qualifies_for_mid_fill(3, "early", lookup)          # tier 3 never qualifies
    assert not R.qualifies_for_mid_fill(1, "b1", lookup)             # cell absent -> no


# ----------------------------------------------------------------------------- leg_touch_cost

def test_leg_touch_cost_mid_fill_is_commission_only():
    lookup = {(1, "early"): 0.6}
    cost = R.leg_touch_cost(1.00, 0.10, 1, "early", 3, lookup)
    assert cost == pytest.approx(COMMISSION_PER_CONTRACT * 3)


def test_leg_touch_cost_no_mid_fill_is_half_spread_plus_commission():
    lookup = {(1, "early"): 0.4}
    cost = R.leg_touch_cost(1.00, 0.10, 1, "early", 3, lookup)
    expected = (0.5 * 0.10 * 1.00 * CONTRACT_MULTIPLIER + COMMISSION_PER_CONTRACT) * 3
    assert cost == pytest.approx(expected)


def test_leg_touch_cost_nan_spread_uses_floor():
    lookup = {(1, "early"): 0.4}
    cost = R.leg_touch_cost(1.00, float("nan"), 1, "early", 1, lookup)
    expected = 0.5 * MODEL_SPREAD_FLOOR * 1.00 * CONTRACT_MULTIPLIER + COMMISSION_PER_CONTRACT
    assert cost == pytest.approx(expected)


def test_leg_touch_cost_tier3_always_half_spread_even_if_cell_qualifies():
    lookup = {(3, "early"): 0.9}   # would never actually occur (build_mid_share_lookup never keys tier 3)
    cost = R.leg_touch_cost(1.00, 0.10, 3, "early", 1, lookup)
    expected = 0.5 * 0.10 * 1.00 * CONTRACT_MULTIPLIER + COMMISSION_PER_CONTRACT
    assert cost == pytest.approx(expected)


# ----------------------------------------------------------------------------- price_with_treatment_a / apply_treatment

def test_treatment_a_reduces_cost_when_both_legs_qualify():
    row = _ss_row()
    lookup_all_qualify = {(1, "late"): 0.9, (1, "early"): 0.9}
    lookup_none_qualify = {(1, "late"): 0.1, (1, "early"): 0.1}
    r_a = R.price_with_treatment_a(row, lookup_all_qualify, exit_window="early")
    r_orig = R.price_with_treatment_a(row, lookup_none_qualify, exit_window="early")
    assert r_a["gross_usd"] == pytest.approx(r_orig["gross_usd"])   # gross unchanged
    assert r_a["cost_usd"] < r_orig["cost_usd"]
    assert r_a["net_usd"] > r_orig["net_usd"]


def test_treatment_a_no_qualifying_cells_reproduces_original_leg_cost():
    row = _ss_row()
    lookup_none = {}
    r = R.price_with_treatment_a(row, lookup_none, exit_window="early")
    legs = R.build_legs(row)
    expected_cost = sum(M.leg_cost(l.entry, row["contracts"]) + M.leg_cost(l.exit, row["contracts"]) for l in legs)
    assert r["cost_usd"] == pytest.approx(expected_cost)


def test_apply_treatment_b_only_new_exit_marks_changes_gross():
    trades = pd.DataFrame([_ss_row()])
    new_marks = {0: {"call": M.Mark(0.50, 0.06, 1, "new"), "put": M.Mark(0.50, 0.06, 1, "new")}}
    out = R.apply_treatment(trades, "b1", lookup=None, exit_window="b1", exit_marks_by_row=new_marks, apply_a=False)
    assert "net_pct_b1" in out.columns
    assert not math.isnan(out.loc[0, "net_usd_b1"])
    # cheaper exit (0.50 vs original 1.00) improves the short straddle's gross
    orig = pd.DataFrame([_ss_row()])
    orig_out = R.apply_treatment(orig, "orig_via_b_path", lookup=None, exit_window="early", apply_a=False)
    assert out.loc[0, "gross_usd_b1"] > orig_out.loc[0, "gross_usd_orig_via_b_path"]


def test_apply_treatment_missing_leg_mark_yields_nan_row():
    trades = pd.DataFrame([_ss_row()])
    new_marks = {0: {"call": M.Mark(0.50, 0.06, 1, "new"), "put": None}}
    out = R.apply_treatment(trades, "b1", lookup=None, exit_window="b1", exit_marks_by_row=new_marks, apply_a=False)
    assert math.isnan(out.loc[0, "net_usd_b1"])
    assert out.loc[0, "n_legs_b1"] == 1


def test_apply_treatment_a_alone_reproduces_original_gross_on_ic():
    """With exit_marks=None, build_legs uses the row's own frozen marks, so gross must match a
    fresh price_legs call on those same marks exactly."""
    row = _ic_row()
    trades = pd.DataFrame([row])
    out = R.apply_treatment(trades, "a", lookup={}, exit_window="early", apply_a=True)
    legs = R.build_legs(row)
    priced = R.ST.price_legs(legs, row["contracts"])
    assert out.loc[0, "gross_usd_a"] == pytest.approx(priced["gross_usd"])
