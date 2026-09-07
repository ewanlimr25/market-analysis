"""The gross ramp decomposition (DESIGN/91 §4): finite-difference Greeks off `engine.bs.price`,
and the delta/vega/residual split of a straddle's mark change."""
from __future__ import annotations

import math

import pytest

from engine import bs
from engine.strategies import sg_decomposition as D

pytestmark = pytest.mark.unit

R = 0.04


def test_numeric_delta_matches_bs_call_put_parity_signs():
    call = D.LegGreekInputs(spot=100.0, strike=100.0, t_years=0.05, iv=0.5, option_type="call")
    put = D.LegGreekInputs(spot=100.0, strike=100.0, t_years=0.05, iv=0.5, option_type="put")
    dc, dp = D.numeric_delta(call, R), D.numeric_delta(put, R)
    assert 0.4 < dc < 0.7
    assert -0.6 < dp < -0.3
    # put-call parity: call delta - put delta = e^{-r t} (discount close to 1 at short T)
    assert dc - dp == pytest.approx(math.exp(-R * 0.05), abs=1e-2)


def test_numeric_delta_deep_itm_call_near_one_and_otm_near_zero():
    deep_itm = D.LegGreekInputs(spot=200.0, strike=100.0, t_years=0.05, iv=0.3, option_type="call")
    deep_otm = D.LegGreekInputs(spot=50.0, strike=100.0, t_years=0.05, iv=0.3, option_type="call")
    assert D.numeric_delta(deep_itm, R) == pytest.approx(1.0, abs=1e-2)
    assert D.numeric_delta(deep_otm, R) == pytest.approx(0.0, abs=1e-2)


def test_numeric_vega_positive_and_symmetric_for_call_and_put():
    call = D.LegGreekInputs(spot=100.0, strike=100.0, t_years=0.1, iv=0.4, option_type="call")
    put = D.LegGreekInputs(spot=100.0, strike=100.0, t_years=0.1, iv=0.4, option_type="put")
    vc, vp = D.numeric_vega(call, R), D.numeric_vega(put, R)
    assert vc > 0 and vp > 0
    assert vc == pytest.approx(vp, rel=1e-6)


def test_numeric_delta_and_vega_zero_at_expiry():
    g = D.LegGreekInputs(spot=100.0, strike=100.0, t_years=0.0, iv=0.4, option_type="call")
    assert D.numeric_delta(g, R) == 0.0
    assert D.numeric_vega(g, R) == 0.0


def test_decomposition_sums_to_gross_pnl_on_synthetic_legs():
    spot_entry, spot_exit = 100.0, 108.0
    k, t_entry = 100.0, 0.05
    iv_entry, iv_exit = 0.45, 0.30
    call_entry = bs.price(spot_entry, k, t_entry, R, iv_entry, "call")
    put_entry = bs.price(spot_entry, k, t_entry, R, iv_entry, "put")
    call_exit = bs.price(spot_exit, k, 0.01, R, iv_exit, "call")
    put_exit = bs.price(spot_exit, k, 0.01, R, iv_exit, "put")
    call_g = D.LegGreekInputs(spot_entry, k, t_entry, iv_entry, "call")
    put_g = D.LegGreekInputs(spot_entry, k, t_entry, iv_entry, "put")
    net_delta = D.numeric_delta(call_g, R) + D.numeric_delta(put_g, R)
    net_vega = D.numeric_vega(call_g, R) + D.numeric_vega(put_g, R)
    dec = D.decompose(call_entry + put_entry, call_exit + put_exit, spot_entry, spot_exit,
                      net_delta, net_vega, iv_entry, iv_exit)
    gross = (call_exit + put_exit - call_entry - put_entry) / spot_entry
    assert dec.unhedged_pnl_pct == pytest.approx(gross)
    # delta_hedged + delta = unhedged, and vega + residual = delta_hedged, by construction
    assert dec.delta_pnl_pct + dec.delta_hedged_pnl_pct == pytest.approx(dec.unhedged_pnl_pct)
    assert dec.vega_pnl_pct + dec.residual_pnl_pct == pytest.approx(dec.delta_hedged_pnl_pct)


def test_decomposition_vega_pnl_nan_when_iv_missing():
    dec = D.decompose(5.0, 6.0, 100.0, 101.0, 0.1, 2.0, None, 0.4)
    assert math.isnan(dec.vega_pnl_pct)
    assert math.isnan(dec.residual_pnl_pct)
