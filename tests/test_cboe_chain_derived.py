"""G8 derived analytics on a synthetic chain: GEX, 25-delta skew, ATM IV, put-call OI ratio."""
from __future__ import annotations

from datetime import date

import pandas as pd
import pytest

from engine.mart import cboe_chain_derived as D

pytestmark = pytest.mark.unit

E1 = date(2026, 9, 11)   # front expiry, 4 days out from ASOF
E2 = date(2026, 10, 7)   # exactly 30 calendar days out from ASOF
ASOF = date(2026, 9, 7)


def _row(expiry, strike, right, delta, iv, gamma=0.0, oi=0.0, spot=100.0):
    return {"symbol": "TST", "expiry": expiry, "strike": strike, "right": right, "delta": delta,
            "iv": iv, "gamma": gamma, "open_interest": oi, "underlying_price": spot}


def synthetic_chain() -> pd.DataFrame:
    rows = [
        # front expiry E1: calls
        _row(E1, 100, "C", 0.30, 0.20, gamma=0.04, oi=800),
        _row(E1, 105, "C", 0.20, 0.18, gamma=0.05, oi=1000),
        _row(E1, 110, "C", 0.10, 0.16, gamma=0.02, oi=0),      # zero OI -> excluded from GEX
        # front expiry E1: puts
        _row(E1, 100, "P", -0.30, 0.22, gamma=0.06, oi=500),
        _row(E1, 95, "P", -0.20, 0.24, gamma=0.03, oi=400),
        _row(E1, 90, "P", -0.10, 0.28, gamma=-0.01, oi=50),    # negative gamma -> excluded from GEX
        # near-30d expiry E2: gamma 0 so it never contributes to GEX; used for skew/ATM/OI only
        _row(E2, 100, "C", 0.28, 0.25, gamma=0.0, oi=200),
        _row(E2, 100, "P", -0.28, 0.27, gamma=0.0, oi=100),
    ]
    return pd.DataFrame(rows)


def test_gex_per_strike_sign_and_filter():
    df = synthetic_chain()
    per_strike = D.gex_per_strike(df)
    got = dict(zip(per_strike.strike, per_strike.gex))
    # call100: +0.04*800*100*100 = 320000; put100: -0.06*500*100*100 = -300000 -> net 20000
    assert got[100] == pytest.approx(20000.0)
    # call105: +0.05*1000*100*100 = 500000
    assert got[105] == pytest.approx(500000.0)
    # put95: -0.03*400*100*100 = -120000
    assert got[95] == pytest.approx(-120000.0)
    # strike 110 (zero OI) and 90 (negative gamma) never appear
    assert set(got) == {95, 100, 105}
    assert 110 not in got and 90 not in got


def test_total_gex_sums_per_strike():
    df = synthetic_chain()
    assert D.total_gex(df) == pytest.approx(20000.0 + 500000.0 - 120000.0)


def test_gex_on_an_empty_chain_is_zero():
    assert D.total_gex(pd.DataFrame(columns=["expiry", "strike", "right", "gamma", "open_interest", "underlying_price"])) == 0.0
    assert D.gex_per_strike(pd.DataFrame()).empty


def test_skew_25d_interpolates_between_bracketing_deltas():
    df = synthetic_chain()
    res = D.skew_25d(df, E1)
    # calls: (0.20, 0.18) and (0.30, 0.20) -> interp at 0.25 = 0.19
    assert res["call_iv_25d"] == pytest.approx(0.19)
    # puts: (-0.30, 0.22) and (-0.20, 0.24) -> interp at -0.25 = 0.23
    assert res["put_iv_25d"] == pytest.approx(0.23)
    assert res["skew_25d"] == pytest.approx(0.23 - 0.19)
    assert res["expiry"] == E1


def test_skew_25d_is_none_when_a_side_has_fewer_than_two_points():
    df = pd.DataFrame([_row(E1, 100, "C", 0.30, 0.20)])
    res = D.skew_25d(df, E1)
    assert res["call_iv_25d"] is None or res["put_iv_25d"] is None
    assert res["skew_25d"] is None


def test_skew_by_expiry_covers_every_expiry_sorted():
    df = synthetic_chain()
    out = D.skew_by_expiry(df)
    assert out["expiry"].tolist() == [E1, E2]


def test_atm_iv_picks_the_strike_nearest_spot_and_averages_call_put():
    df = synthetic_chain()
    # spot = 100, strike 100 is exact ATM: call iv 0.20, put iv 0.22 -> mean 0.21
    assert D.atm_iv(df, E1) == pytest.approx(0.21)


def test_atm_iv_summary_front_and_near_30d():
    df = synthetic_chain()
    summary = D.atm_iv_summary(df, ASOF)
    assert summary["front_expiry"] == E1
    assert summary["front_atm_iv"] == pytest.approx(0.21)
    assert summary["near_30d_expiry"] == E2
    assert summary["near_30d_atm_iv"] == pytest.approx((0.25 + 0.27) / 2)


def test_front_expiry_and_nearest_expiry_to_on_empty_chain_are_none():
    empty = pd.DataFrame(columns=["expiry"])
    assert D.front_expiry(empty) is None
    assert D.nearest_expiry_to(empty, ASOF) is None
    assert D.atm_iv_summary(empty, ASOF) == {"front_expiry": None, "front_atm_iv": None,
                                              "near_30d_expiry": None, "near_30d_atm_iv": None}


def test_put_call_oi_ratio():
    df = synthetic_chain()
    # call OI: 800+1000+0+200 = 2000; put OI: 500+400+50+100 = 1050
    assert D.put_call_oi_ratio(df) == pytest.approx(1050.0 / 2000.0)


def test_put_call_oi_ratio_is_none_on_zero_call_oi_or_empty():
    only_puts = pd.DataFrame([_row(E1, 100, "P", -0.3, 0.2, oi=10)])
    assert D.put_call_oi_ratio(only_puts) is None
    assert D.put_call_oi_ratio(pd.DataFrame()) is None
