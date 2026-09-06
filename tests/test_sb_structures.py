"""Q3: S-B expiry rule, sigma unit, targets, band selection, PS/IC legs, max loss, sizing (DESIGN/80 §3-§4)."""
from __future__ import annotations

import math
from datetime import date

import pandas as pd
import pytest

from engine import marking as M
from engine.config import SB_PARAMS, SB_SIZING, SBParams, SBSizing
from engine.strategies import sb_structures as SB
from engine.strategies import sa_structures as ST

pytestmark = pytest.mark.unit


def _is_session(d: date) -> bool:
    return d.weekday() < 5 and d != date(2026, 4, 3)          # Good Friday 2026


def test_sigma_unit_and_targets():
    m = SB.sigma_unit(20.0, 21)
    assert m == pytest.approx(0.20 * math.sqrt(21 / 365))
    k = SB.target_strikes(100.0, m, SB_PARAMS)
    assert k == {"p1": pytest.approx(100 * (1 - m)), "p2": pytest.approx(100 * (1 - 2 * m)),
                 "c1": pytest.approx(100 * (1 + m)), "c2": pytest.approx(100 * (1 + 2 * m))}


def test_select_expiry_prefers_the_friday_nearest_21_days_inside_the_window():
    entry = date(2026, 7, 10)                                   # a Friday
    cands = [date(2026, 7, 13), date(2026, 7, 17), date(2026, 7, 24), date(2026, 7, 31), date(2026, 8, 3), date(2026, 8, 7)]
    assert SB.select_expiry(cands, entry, _is_session, SB_PARAMS) == date(2026, 7, 31)     # exactly 21 days, Friday
    assert SB.select_expiry([date(2026, 7, 24), date(2026, 8, 7)], entry, _is_session, SB_PARAMS) == date(2026, 7, 24)  # tie 14 vs 28 -> earlier
    assert SB.select_expiry([date(2026, 7, 13), date(2026, 8, 3)], entry, _is_session, SB_PARAMS) is None            # no Friday
    assert SB.select_expiry([date(2026, 7, 16), date(2026, 8, 14)], entry, _is_session, SB_PARAMS) is None            # Thu (not a holiday week), 35 days


def test_select_expiry_accepts_the_thursday_before_a_holiday_friday():
    entry = date(2026, 3, 13)
    assert SB.select_expiry([date(2026, 4, 2), date(2026, 4, 10)], entry, _is_session, SB_PARAMS) == date(2026, 4, 2)


def test_proxy_expiry_rolls_a_holiday_friday_back_to_the_prior_session():
    from datetime import timedelta
    sessions = [date(2026, 3, 13) + timedelta(days=i) for i in range(40)]
    sessions = [d for d in sessions if _is_session(d)]
    assert SB.proxy_expiry(date(2026, 3, 13), sessions, SB_PARAMS) == date(2026, 4, 2)
    assert SB.proxy_expiry(date(2026, 3, 20), sessions, SB_PARAMS) == date(2026, 4, 10)
    assert SB.proxy_expiry(date(2026, 4, 10), sessions, SB_PARAMS) is None                # past the session list


def _rows(strikes_sizes: dict[tuple[str, float], int], spread: float = 0.01) -> pd.DataFrame:
    rows = []
    for (typ, k), size in strikes_sizes.items():
        rows.append({"option_chain_id": f"SPY260731{'C' if typ == 'call' else 'P'}{int(k * 1000):08d}", "underlying_symbol": "SPY",
                     "option_type": typ, "strike": float(k), "expiry": date(2026, 7, 31), "date": date(2026, 7, 10),
                     "vwap_late": 1.0 + k / 100, "size_late": size, "late_rel_spread": spread, "late_last_bid": None, "late_last_ask": None,
                     "last_nbbo_bid": None, "last_nbbo_ask": None})
    return pd.DataFrame(rows)


def test_band_selection_takes_the_nearest_tier1_strike_and_breaks_ties_toward_the_money():
    rows = _rows({("put", 95.0): 10, ("put", 94.0): 2, ("put", 96.0): 10, ("put", 90.0): 7, ("put", 97.0): 10})
    band = 0.25 * 0.048 * 100                                   # 1.2 points
    r = SB.select_leg_row(rows, "put", target=95.2, band_abs=band, spot=100.0, min_size=5)
    assert r["strike"] == 95.0                                  # nearest tier-1 (94 is thin)
    r = SB.select_leg_row(rows, "put", target=95.5, band_abs=band, spot=100.0, min_size=5)
    assert r["strike"] == 96.0                                  # 95 and 96 tie at 0.5 -> nearer the money
    assert SB.select_leg_row(rows, "put", target=92.0, band_abs=band, spot=100.0, min_size=5) is None      # only 90 (2 away) beyond band
    assert SB.select_leg_row(rows, "call", target=105.0, band_abs=band, spot=100.0, min_size=5) is None    # no calls


def test_ordering_width_max_loss_and_sizing_by_hand():
    strikes = {"p1": 95.0, "p2": 90.0, "c1": 105.0, "c2": 111.0}
    assert SB.strikes_ordered(strikes, 100.0, "PS") and SB.strikes_ordered(strikes, 100.0, "IC")
    assert not SB.strikes_ordered({"p1": 95.0, "p2": 95.0}, 100.0, "PS")
    assert not SB.strikes_ordered({"p1": 101.0, "p2": 90.0}, 100.0, "PS")
    assert SB.width(strikes, "PS") == 5.0 and SB.width(strikes, "IC") == 6.0
    assert SB.max_loss_per_contract(strikes, "PS", credit_per_share=1.2) == pytest.approx((5.0 - 1.2) * 100)
    assert SB.max_loss_per_contract(strikes, "IC", credit_per_share=1.9) == pytest.approx((6.0 - 1.9) * 100)
    assert SB.size_position(380.0, SB_SIZING) == 7                                        # floor(3000 / 380)
    assert SB.size_position(2700.0, SB_SIZING) == 1 and SB.size_position(9000.0, SB_SIZING) == 1   # minimum one


def test_legs_price_and_settle_through_the_shared_engine():
    strikes = {"p1": 95.0, "p2": 90.0}
    entry = {"p1": M.Mark(2.0, 0.01, 1, "print_vwap"), "p2": M.Mark(0.8, 0.02, 1, "print_vwap")}
    exits = SB.settle_marks(strikes, "PS", close=92.0)
    assert exits["p1"].price == 3.0 and exits["p2"].price == 0.0 and exits["p1"].tier == 4
    legs = SB.build_legs("SPY", date(2026, 7, 31), strikes, entry, exits, "PS")
    assert [l.name for l in legs] == ["p1", "p2"] and legs[0].side == ST.SHORT and legs[1].side == ST.LONG
    priced = ST.price_legs(legs, 2)
    assert priced["credit_entry"] == pytest.approx(1.2) and priced["debit_exit"] == pytest.approx(3.0)
    assert priced["gross_usd"] == pytest.approx((1.2 - 3.0) * 100 * 2)
    exp_entry = (0.5 * 0.01 * 2.0 * 100 + 0.65) * 2 + (0.5 * 0.02 * 0.8 * 100 + 0.65) * 2
    assert priced["entry_cost_usd"] == pytest.approx(exp_entry)
    assert priced["exit_cost_usd"] == pytest.approx(0.65 * 2 * 2)                          # spread 0 at expiry
    ic = SB.build_legs("SPY", date(2026, 7, 31), {**strikes, "c1": 105.0, "c2": 110.0},
                       {**entry, "c1": M.Mark(0.5, 0.02, 1, "print_vwap"), "c2": M.Mark(0.1, 0.2, 1, "print_vwap")},
                       SB.settle_marks({**strikes, "c1": 105.0, "c2": 110.0}, "IC", 112.0), "IC")
    assert [l.name for l in ic] == ["p1", "p2", "c1", "c2"] and ic[2].exit.price == 7.0 and ic[3].exit.price == 2.0
