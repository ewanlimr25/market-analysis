"""P3: the marking engine (DESIGN/70 §2) — tier selection, BS fallback, spread floor, intrinsic, costs."""
from __future__ import annotations

import math
from datetime import date

import numpy as np
import pytest

from engine import bs
from engine import marking as M
from engine.config import (COMMISSION_PER_CONTRACT, CONTRACT_MULTIPLIER, MODEL_SPREAD_FLOOR,
                           RISK_FREE_RATE, TIER1_MIN_SIZE)

pytestmark = pytest.mark.unit


def _row(**kw):
    base = dict(option_chain_id="XYZ260807C00100000", underlying_symbol="XYZ", option_type="call",
                strike=100.0, expiry=date(2026, 8, 7), date=date(2026, 7, 29),
                vwap_late=2.50, size_late=25, late_rel_spread=0.08, late_last_bid=2.40, late_last_ask=2.60,
                vwap_early=3.10, size_early=12, early_rel_spread=0.06, early_last_bid=3.00, early_last_ask=3.20,
                last_price=2.55, last_nbbo_bid=2.45, last_nbbo_ask=2.65, n_prints=40, size_total=60,
                late_nbbo_mid=2.50, early_nbbo_mid=3.10, iv_vwap=0.45, underlying_last=100.5)
    base.update(kw)
    return base


# ---- Black-Scholes -----------------------------------------------------------------------------

def test_bs_matches_py_vollib_reference():
    from py_vollib.black_scholes import black_scholes
    S, K, t, r, sigma = 100.0, 105.0, 30 / 365, RISK_FREE_RATE, 0.35
    assert bs.price(S, K, t, r, sigma, "call") == pytest.approx(black_scholes("c", S, K, t, r, sigma), abs=1e-8)
    assert bs.price(S, K, t, r, sigma, "put") == pytest.approx(black_scholes("p", S, K, t, r, sigma), abs=1e-8)


def test_bs_put_call_parity_and_vectorized():
    S, K, t, r, sigma = np.array([100.0, 80.0]), np.array([100.0, 90.0]), np.array([0.1, 0.05]), 0.04, np.array([0.3, 0.6])
    c = bs.price(S, K, t, r, sigma, "call")
    p = bs.price(S, K, t, r, sigma, "put")
    np.testing.assert_allclose(c - p, S - K * np.exp(-r * t), atol=1e-10)


def test_bs_zero_time_is_intrinsic():
    assert bs.price(110.0, 100.0, 0.0, 0.04, 0.3, "call") == pytest.approx(10.0)
    assert bs.price(110.0, 100.0, 0.0, 0.04, 0.3, "put") == pytest.approx(0.0)


def test_bs_rejects_bad_inputs():
    with pytest.raises(ValueError):
        bs.price(100.0, 100.0, 0.1, 0.04, -0.2, "call")
    with pytest.raises(ValueError):
        bs.price(100.0, 100.0, 0.1, 0.04, 0.2, "straddle")


# ---- tiers 1 and 2 from a daily_contract row -----------------------------------------------------

def test_tier1_late_uses_vwap_and_late_spread():
    m = M.print_mark(_row(), M.WHEN_LATE)
    assert (m.price, m.rel_spread, m.tier, m.source) == (2.50, 0.08, 1, M.SOURCE_PRINT_VWAP)


def test_tier1_early_uses_early_vwap():
    m = M.print_mark(_row(), M.WHEN_EARLY)
    assert (m.price, m.rel_spread, m.tier) == (3.10, 0.06, 1)


def test_tier2_thin_window_uses_last_nbbo_mid_of_that_window():
    m = M.print_mark(_row(size_late=TIER1_MIN_SIZE - 1), M.WHEN_LATE)
    assert m.tier == 2 and m.source == M.SOURCE_PRINT_NBBO
    assert m.price == pytest.approx(2.50)                  # (2.40 + 2.60) / 2
    assert m.rel_spread == pytest.approx(0.20 / 2.50)


def test_tier1_boundary_is_inclusive():
    assert M.print_mark(_row(size_late=TIER1_MIN_SIZE), M.WHEN_LATE).tier == 1


def test_no_prints_in_window_returns_none():
    assert M.print_mark(_row(size_late=0, vwap_late=None), M.WHEN_LATE) is None
    assert M.print_mark(_row(size_early=None, vwap_early=None), M.WHEN_EARLY) is None


def test_tier1_spread_falls_back_when_window_spread_is_null():
    m = M.print_mark(_row(late_rel_spread=None, late_last_bid=None, late_last_ask=None), M.WHEN_LATE)
    assert m.tier == 1 and m.rel_spread == pytest.approx(0.20 / 2.55)   # session last NBBO


def test_tier2_with_invalid_nbbo_falls_back_to_vwap_and_nan_spread():
    m = M.print_mark(_row(size_late=2, late_rel_spread=None, late_last_bid=None, late_last_ask=None,
                          last_nbbo_bid=None, last_nbbo_ask=None), M.WHEN_LATE)
    assert m.tier == 2 and m.price == 2.50 and math.isnan(m.rel_spread)


def test_close_mark_uses_last_print():
    m = M.print_mark(_row(), M.WHEN_CLOSE)
    assert m.price == 2.55 and m.rel_spread == pytest.approx(0.20 / 2.55) and m.tier == 1


# ---- tier 3 model and tier 4 intrinsic ---------------------------------------------------------

def test_model_mark_prices_with_bs_and_floors_the_spread():
    m = M.model_mark(spot=100.0, strike=105.0, dte_cal=9, iv=0.5, option_type="call", rel_spread=0.02)
    assert m.tier == 3 and m.source == M.SOURCE_MODEL
    assert m.price == pytest.approx(bs.price(100.0, 105.0, 9 / 365, RISK_FREE_RATE, 0.5, "call"))
    assert m.rel_spread == MODEL_SPREAD_FLOOR


def test_model_mark_keeps_a_wider_spread():
    m = M.model_mark(spot=100.0, strike=105.0, dte_cal=9, iv=0.5, option_type="put", rel_spread=0.12)
    assert m.rel_spread == 0.12


def test_model_mark_requires_positive_inputs():
    assert M.model_mark(spot=None, strike=105.0, dte_cal=9, iv=0.5, option_type="call", rel_spread=0.1) is None
    assert M.model_mark(spot=100.0, strike=105.0, dte_cal=9, iv=float("nan"), option_type="call", rel_spread=0.1) is None


def test_intrinsic_mark_at_expiry():
    c = M.intrinsic_mark(spot=104.0, strike=100.0, option_type="call")
    p = M.intrinsic_mark(spot=104.0, strike=100.0, option_type="put")
    assert (c.price, c.rel_spread, c.tier, c.source) == (4.0, 0.0, 4, M.SOURCE_INTRINSIC)
    assert p.price == 0.0


def test_model_iv_blends_the_contracts_smile_ratio_onto_todays_iv30d():
    # contract printed at iv 0.60 when the name's iv30d was 0.40 -> ratio 1.5; today iv30d is 0.30
    assert M.model_iv(iv30d_today=0.30, iv_vwap_last=0.60, iv30d_last=0.40) == pytest.approx(0.45)
    assert M.model_iv(iv30d_today=0.30, iv_vwap_last=None, iv30d_last=None) == 0.30
    assert M.model_iv(iv30d_today=0.30, iv_vwap_last=5.0, iv30d_last=0.40) == pytest.approx(0.30 * M.MODEL_IV_RATIO_MAX)
    assert M.model_iv(iv30d_today=None, iv_vwap_last=0.6, iv30d_last=0.4) is None


# ---- the resolver: falls through the tiers ----------------------------------------------------

def _inputs(**kw):
    base = dict(spot=100.0, iv=0.5, rel_spread=0.02)
    base.update(kw)
    return M.ModelInputs(**base)


def test_resolver_uses_print_row_when_present():
    contract = M.Contract("XYZ260807C00100000", "XYZ", "call", 100.0, date(2026, 8, 7))
    r = M.MarkResolver(rows={(contract.option_chain_id, date(2026, 7, 29)): _row()}, model_inputs=lambda *a: _inputs())
    assert r.mark(contract, date(2026, 7, 29), M.WHEN_LATE).tier == 1


def test_resolver_falls_to_model_when_no_row():
    contract = M.Contract("XYZ260807C00105000", "XYZ", "call", 105.0, date(2026, 8, 7))
    r = M.MarkResolver(rows={}, model_inputs=lambda *a: _inputs())
    m = r.mark(contract, date(2026, 7, 29), M.WHEN_LATE)
    assert m.tier == 3 and m.rel_spread == MODEL_SPREAD_FLOOR


def test_resolver_intrinsic_on_expiry_close():
    contract = M.Contract("XYZ260807C00100000", "XYZ", "call", 100.0, date(2026, 8, 7))
    r = M.MarkResolver(rows={}, model_inputs=lambda *a: _inputs(spot=103.0))
    m = r.mark(contract, date(2026, 8, 7), M.WHEN_CLOSE)
    assert m.tier == 4 and m.price == 3.0


def test_resolver_returns_none_when_nothing_can_mark():
    contract = M.Contract("XYZ260807C00100000", "XYZ", "call", 100.0, date(2026, 8, 7))
    r = M.MarkResolver(rows={}, model_inputs=lambda *a: None)
    assert r.mark(contract, date(2026, 7, 29), M.WHEN_LATE) is None


# ---- costs ------------------------------------------------------------------------------------

def test_leg_cost_is_half_spread_plus_commission_per_contract():
    m = M.Mark(price=2.00, rel_spread=0.10, tier=1, source=M.SOURCE_PRINT_VWAP)
    expected = (0.5 * 0.10 * 2.00 * CONTRACT_MULTIPLIER + COMMISSION_PER_CONTRACT) * 3
    assert M.leg_cost(m, 3) == pytest.approx(expected)


def test_leg_cost_applies_floor_to_nan_spread():
    m = M.Mark(price=2.00, rel_spread=float("nan"), tier=2, source=M.SOURCE_PRINT_NBBO)
    expected = (0.5 * MODEL_SPREAD_FLOOR * 2.00 * CONTRACT_MULTIPLIER + COMMISSION_PER_CONTRACT)
    assert M.leg_cost(m, 1) == pytest.approx(expected)


def test_leg_cost_scales_with_cost_multiplier():
    m = M.Mark(price=2.00, rel_spread=0.10, tier=1, source=M.SOURCE_PRINT_VWAP)
    assert M.leg_cost(m, 1, cost_mult=2.0) == pytest.approx(2 * M.leg_cost(m, 1))
