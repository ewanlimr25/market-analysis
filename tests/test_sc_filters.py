"""S-C R1 (DESIGN/90 §2, §3, §10): F1..F10, C2, expiry and ATM selection, the σ unit. Boundary
cases on every filter, a null earnings date failing closed, the Thursday before a holiday Friday."""
from __future__ import annotations

import math
from datetime import date, timedelta

import pandas as pd
import pytest

from engine.config import SC_PARAMS, SCParams
from engine.strategies import sc_filters as F

pytestmark = pytest.mark.unit

ENTRY = date(2026, 7, 10)                                   # a Friday
EXP = date(2026, 8, 7)                                      # +28 calendar days, a Friday


def _is_session(d: date) -> bool:
    return d.weekday() < 5 and d not in (date(2026, 4, 3), date(2026, 7, 3))   # Good Friday, Independence Day observed


def _row(**over) -> dict:
    base = {"ticker": "ACME", "issue_type": "Common Stock", "is_index": False, "close": 50.0, "marketcap": 5e9,
            "adv_usd_20d": 120e6, "iv30d": 0.45, "next_earnings_date": date(2026, 8, 20), "sector": "Healthcare"}
    return {**base, **over}


def _contract(option_type: str, strike: float, expiry: date = EXP, size_late: int = 40, spread: float = 0.05) -> dict:
    return {"option_type": option_type, "strike": strike, "expiry": pd.Timestamp(expiry), "size_late": size_late,
            "late_rel_spread": spread}


def _rows(*contracts) -> pd.DataFrame:
    return pd.DataFrame(list(contracts))


def _good_rows(strike: float = 50.0, spread: float = 0.05, size: int = 40) -> pd.DataFrame:
    return _rows(_contract("call", strike, size_late=size, spread=spread), _contract("put", strike, size_late=size, spread=spread))


# ---- F1 F2 F3 F4 F6 boundaries -------------------------------------------------------------------

def test_screener_filters_at_their_bounds():
    p = SC_PARAMS
    ok = F.screener_filters(_row(close=p.price_min, marketcap=p.mcap_min, adv_usd_20d=p.adv_min, iv30d=p.iv30d_min))
    assert ok == {"F1": True, "F2": True, "F3": True, "F4": True, "F6": True}
    assert F.screener_filters(_row(marketcap=p.mcap_max))["F3"] and F.screener_filters(_row(iv30d=p.iv30d_max))["F6"]
    assert not F.screener_filters(_row(close=p.price_min - 0.01))["F2"]
    assert not F.screener_filters(_row(marketcap=p.mcap_max + 1))["F3"] and not F.screener_filters(_row(marketcap=p.mcap_min - 1))["F3"]
    assert not F.screener_filters(_row(adv_usd_20d=p.adv_min - 1))["F4"]
    assert not F.screener_filters(_row(iv30d=p.iv30d_max + 1e-9))["F6"] and not F.screener_filters(_row(iv30d=p.iv30d_min - 1e-9))["F6"]


def test_f1_needs_common_or_adr_and_not_an_index_and_missing_numbers_fail():
    assert F.screener_filters(_row(issue_type="ADR"))["F1"]
    assert not F.screener_filters(_row(issue_type="ETF"))["F1"]
    assert not F.screener_filters(_row(is_index=True))["F1"]
    out = F.screener_filters(_row(close=None, marketcap=float("nan"), adv_usd_20d="x", iv30d=None))
    assert out == {"F1": True, "F2": False, "F3": False, "F4": False, "F6": False}


# ---- F7 expiry -----------------------------------------------------------------------------------

def test_select_expiry_takes_the_friday_nearest_28_days_inside_21_to_35_ties_earlier():
    cands = [ENTRY + timedelta(days=n) for n in (14, 21, 28, 35, 42)]        # all Fridays
    assert F.select_expiry(cands, ENTRY, _is_session) == ENTRY + timedelta(days=28)
    assert F.select_expiry([ENTRY + timedelta(21), ENTRY + timedelta(35)], ENTRY, _is_session) == ENTRY + timedelta(21)  # tie -> earlier
    assert F.select_expiry([ENTRY + timedelta(14), ENTRY + timedelta(42)], ENTRY, _is_session) is None
    assert F.select_expiry([ENTRY + timedelta(24)], ENTRY, _is_session) is None                       # a Monday
    assert F.select_expiry([], ENTRY, _is_session) is None
    assert F.select_expiry([pd.Timestamp(ENTRY + timedelta(28)), None], ENTRY, _is_session) == ENTRY + timedelta(28)


def test_select_expiry_accepts_the_thursday_before_a_holiday_friday():
    entry = date(2026, 3, 6)                                  # Friday; Good Friday 2026-04-03 is 28 days out
    thursday = date(2026, 4, 2)
    assert F.select_expiry([thursday], entry, _is_session) == thursday
    assert F.select_expiry([date(2026, 4, 9)], entry, _is_session) is None                      # an ordinary Thursday, 34 days


# ---- F5 earnings ---------------------------------------------------------------------------------

def test_earnings_must_be_known_and_strictly_after_expiry_null_fails_closed():
    assert F.earnings_ok(EXP + timedelta(days=1), EXP)
    assert F.earnings_ok(pd.Timestamp(EXP + timedelta(days=1)), EXP)
    assert F.earnings_ok("2026-08-10", EXP)
    assert not F.earnings_ok(EXP, EXP)                       # on the expiry session: inside the window
    assert not F.earnings_ok(EXP - timedelta(days=7), EXP)
    assert not F.earnings_ok(None, EXP) and not F.earnings_ok(float("nan"), EXP) and not F.earnings_ok(pd.NaT, EXP)
    assert not F.earnings_ok("not a date", EXP)


# ---- F8 F9 ATM pair ------------------------------------------------------------------------------

def test_atm_pair_nearest_strike_inside_the_band_with_both_legs_at_size_ties_lower():
    rows = _rows(_contract("call", 50.0), _contract("put", 50.0), _contract("call", 51.0), _contract("put", 51.0))
    assert F.select_atm_pair(rows, 50.5).strike == 50.0                                        # tie -> lower
    assert F.select_atm_pair(rows, 50.8).strike == 51.0
    assert F.select_atm_pair(rows, 53.0) is None                                               # 51/53 = 3.9% > 2.5%
    thin = _rows(_contract("call", 50.0, size_late=SC_PARAMS.leg_size_min - 1), _contract("put", 50.0))
    assert F.select_atm_pair(thin, 50.0) is None                                               # the call is thin
    edge = _rows(_contract("call", 50.0, size_late=SC_PARAMS.leg_size_min), _contract("put", 50.0, size_late=SC_PARAMS.leg_size_min))
    assert F.select_atm_pair(edge, 50.0).strike == 50.0
    assert F.select_atm_pair(_rows(_contract("call", 50.0)), 50.0) is None                     # no put
    assert F.select_atm_pair(pd.DataFrame(), 50.0) is None and F.select_atm_pair(rows, 0.0) is None


def test_spreads_at_the_bound_pass_and_unknown_fails():
    pair = F.select_atm_pair(_good_rows(spread=SC_PARAMS.spread_max), 50.0)
    assert F.spreads_ok(pair) and pair.mean_spread == pytest.approx(SC_PARAMS.spread_max)
    over = F.select_atm_pair(_rows(_contract("call", 50.0, spread=0.05), _contract("put", 50.0, spread=SC_PARAMS.spread_max + 0.001)), 50.0)
    assert not F.spreads_ok(over)
    unknown = F.select_atm_pair(_rows(_contract("call", 50.0, spread=None), _contract("put", 50.0)), 50.0)
    assert not F.spreads_ok(unknown) and math.isnan(unknown.mean_spread)


# ---- C2, σ, wings --------------------------------------------------------------------------------

def test_c2_excludes_technology_only_and_sigma_and_wings_follow_the_spec():
    assert not F.c2_ok("Technology") and F.c2_ok("Healthcare") and F.c2_ok(None)
    s = F.sigma_hold(50.0, 0.45, 28)
    assert s == pytest.approx(50.0 * 0.45 * math.sqrt(28 / 365))
    assert F.wing_targets(50.0, s) == (pytest.approx(50.0 + 2 * s), pytest.approx(50.0 - 2 * s))


# ---- evaluate_name and F10 -----------------------------------------------------------------------

def test_evaluate_name_passes_a_clean_name_and_names_the_first_failure():
    ev = F.evaluate_name(_row(), _good_rows(), ENTRY, _is_session)
    assert ev["reason"] is None and F.passed_all(ev) and ev["expiry"] == EXP and ev["dte_cal"] == 28
    assert ev["pair"].strike == 50.0 and ev["mean_spread"] == pytest.approx(0.05) and ev["c2"]
    assert ev["sigma_hold"] == pytest.approx(F.sigma_hold(50.0, 0.45, 28))

    assert F.evaluate_name(_row(issue_type="ETF"), _good_rows(), ENTRY, _is_session)["reason"] == "F1"
    assert F.evaluate_name(_row(marketcap=30e9), _good_rows(), ENTRY, _is_session)["reason"] == "F3"
    no_expiry = F.evaluate_name(_row(), _good_rows(), ENTRY + timedelta(days=21), _is_session)   # expiry only 7 days out
    assert no_expiry["reason"] == "F7" and no_expiry["F5"] is None                             # F5 not evaluated
    assert F.evaluate_name(_row(next_earnings_date=None), _good_rows(), ENTRY, _is_session)["reason"] == "F5"
    assert F.evaluate_name(_row(next_earnings_date=EXP), _good_rows(), ENTRY, _is_session)["reason"] == "F5"
    assert F.evaluate_name(_row(iv30d=0.9), _good_rows(), ENTRY, _is_session)["reason"] == "F6"
    assert F.evaluate_name(_row(), _good_rows(size=5), ENTRY, _is_session)["reason"] == "F8"
    assert F.evaluate_name(_row(), _good_rows(spread=0.12), ENTRY, _is_session)["reason"] == "F9"
    assert F.evaluate_name(_row(), pd.DataFrame(), ENTRY, _is_session)["reason"] == "F7"


def _pool(n: int) -> list[dict]:
    evs = []
    for i in range(n):
        sector = "Technology" if i % 3 == 0 else "Energy"
        ev = F.evaluate_name(_row(ticker=f"T{i:02d}", sector=sector), _good_rows(spread=0.02 + 0.001 * i), ENTRY, _is_session)
        evs.append(ev)
    return evs


def test_select_top_takes_the_ten_lowest_spreads_and_c2_drops_technology():
    evs = _pool(15) + [F.evaluate_name(_row(ticker="BAD", iv30d=0.1), _good_rows(spread=0.001), ENTRY, _is_session)]
    c1 = F.select_top(evs, "C1")
    assert [e["ticker"] for e in c1] == [f"T{i:02d}" for i in range(10)] and c1[0]["rank"] == 1 and c1[0]["variant"] == "C1"
    c2 = F.select_top(evs, "C2")
    assert len(c2) == 10 and all(e["sector"] != "Technology" for e in c2) and c2[0]["ticker"] == "T01"
    assert F.select_top(evs, "C1", SCParams(select_n=3))[-1]["ticker"] == "T02"
    with pytest.raises(ValueError):
        F.select_top(evs, "C3")


def test_select_top_is_deterministic_on_tied_spreads():
    evs = [F.evaluate_name(_row(ticker=t), _good_rows(spread=0.03), ENTRY, _is_session) for t in ("ZED", "ABC", "MID")]
    assert [e["ticker"] for e in F.select_top(evs, "C1")] == ["ABC", "MID", "ZED"]


def test_funnel_counts_are_cumulative_in_evaluation_order():
    evs = _pool(12)
    evs.append(F.evaluate_name(_row(ticker="X1", close=5.0), _good_rows(), ENTRY, _is_session))              # F2
    evs.append(F.evaluate_name(_row(ticker="X2", next_earnings_date=None), _good_rows(), ENTRY, _is_session))  # F5
    evs.append(F.evaluate_name(_row(ticker="X3"), _good_rows(spread=0.2), ENTRY, _is_session))                # F9
    c = F.funnel_counts(evs)
    assert c["names"] == 15 and c["F1"] == 15 and c["F2"] == 14 and c["F4"] == 14 and c["F7"] == 14
    assert c["F5"] == 13 and c["F6"] == 13 and c["F8"] == 13 and c["F9"] == 12
    assert c["C1"] == 10 and c["C2"] == 8                                                                      # 12 pass; 4 are Technology
