"""engine.watch.conditions: the 17 watch-basket rules and their thresholds
(DESIGN/110-watch-basket.md §2). Each threshold is checked at its boundary and null-safety is
checked explicitly: a missing input must return `None`, never `False`."""
from __future__ import annotations

import math

import pytest

from engine.watch import conditions as C

pytestmark = pytest.mark.unit


def test_all_conditions_registered_exactly_17():
    assert len(C.ALL_CONDITIONS) == 17
    assert len(set(C.ALL_CONDITIONS)) == 17
    assert set(C.CONDITION_FUNCS) == set(C.ALL_CONDITIONS)


def test_sign_groups_partition_all_17_with_no_overlap():
    groups = [C.SIGN_PLUS, C.SIGN_MINUS, C.SIGN_VOL, C.SIGN_LOGGED]
    assert sum(len(g) for g in groups) == 17
    seen = set()
    for g in groups:
        assert not (seen & set(g))
        seen |= set(g)
    assert seen == set(C.ALL_CONDITIONS)


# --- kleene logic -------------------------------------------------------------------------


def test_kleene_and():
    assert C.kleene_and([True, True]) is True
    assert C.kleene_and([True, False]) is False
    assert C.kleene_and([True, None]) is None
    assert C.kleene_and([False, None]) is False   # False decides regardless of the unknown


def test_kleene_or():
    assert C.kleene_or([False, False]) is False
    assert C.kleene_or([False, True]) is True
    assert C.kleene_or([False, None]) is None
    assert C.kleene_or([True, None]) is True      # True decides regardless of the unknown


# --- C-HIGH / C-LOW ------------------------------------------------------------------------


def test_c_high_boundary_and_null():
    assert C.c_high(0.85) is True
    assert C.c_high(0.8499) is False
    assert C.c_high(None) is None
    assert C.c_high(float("nan")) is None


def test_c_low_boundary_and_null():
    assert C.c_low(0.15) is True
    assert C.c_low(0.1501) is False
    assert C.c_low(None) is None


# --- C-SHORT -------------------------------------------------------------------------------


def test_c_short_either_side_true():
    assert C.c_short(days_to_cover=5.0, borrow_fee_pct=None) is True
    assert C.c_short(days_to_cover=None, borrow_fee_pct=5.0) is True


def test_c_short_both_false():
    assert C.c_short(4.9, 4.9) is False


def test_c_short_both_missing_is_none():
    assert C.c_short(None, None) is None


def test_c_short_one_false_one_missing_is_none():
    assert C.c_short(4.9, None) is None


# --- C-OIBUILD / C-CROWD (pass-through of a precomputed decile flag) -----------------------


def test_c_oibuild_and_c_crowd_pass_through():
    assert C.c_oibuild(True) is True
    assert C.c_oibuild(False) is False
    assert C.c_oibuild(None) is None
    assert C.c_crowd(True) is True
    assert C.c_crowd(None) is None


# --- C-IVUP --------------------------------------------------------------------------------


def test_c_ivup_boundary_and_null():
    assert C.c_ivup(10.0) is True
    assert C.c_ivup(9.99) is False
    assert C.c_ivup(None) is None


# --- C-VOL ---------------------------------------------------------------------------------


def test_c_vol_all_pass():
    assert C.c_vol(iv30d=0.5, marketcap=5e9, has_tier1_atm_pair=True,
                    days_to_next_earnings=40) is True


def test_c_vol_boundaries():
    assert C.c_vol(0.30, 1e9, True, 36) is True
    assert C.c_vol(0.2999, 1e9, True, 36) is False
    assert C.c_vol(0.80, 20e9, True, 36) is True
    assert C.c_vol(0.8001, 20e9, True, 36) is False
    assert C.c_vol(0.5, 5e9, True, 35) is False       # "within 35 days" excludes exactly 35
    assert C.c_vol(0.5, 5e9, True, 36) is True


def test_c_vol_false_beats_unknown():
    # marketcap fails outright; missing earnings date cannot rescue it
    assert C.c_vol(0.5, 0.5e9, True, None) is False


def test_c_vol_unknown_earnings_with_everything_else_passing_is_none():
    assert C.c_vol(0.5, 5e9, True, None) is None


def test_c_vol_no_tier1_pair_is_false():
    assert C.c_vol(0.5, 5e9, False, 40) is False


def test_c_vol_no_tier1_pair_unknown_is_none():
    assert C.c_vol(0.5, 5e9, None, 40) is None


# --- C-RSI ---------------------------------------------------------------------------------


def test_c_rsi_boundary_and_null():
    assert C.c_rsi(30.0) is True
    assert C.c_rsi(30.01) is False
    assert C.c_rsi(None) is None


# --- pass-through structure conditions -----------------------------------------------------


@pytest.mark.parametrize("fn", [C.c_div, C.c_avwap, C.c_avwap_loss, C.c_poc, C.c_poc_loss,
                                 C.c_swing, C.c_swing_loss, C.c_leap, C.c_dp])
def test_passthrough_conditions_are_null_safe_identity(fn):
    assert fn(True) is True
    assert fn(False) is False
    assert fn(None) is None
