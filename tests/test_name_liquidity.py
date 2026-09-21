"""engine.name.liquidity (R2, findings/stock-deep-dive DESIGN/70 §2): the L1..L6 stop/go floor.

Every test runs offline on synthetic `NameInputs` or on the stored `tests/fixtures/name/` slices:
no network, no panel, no mart. The synthetic baseline `_inputs()` clears all six floors; each
floor test breaks exactly one input and asserts the floor that must name it.
"""
from __future__ import annotations

import json
import os
from datetime import date, timedelta

import jsonschema
import pandas as pd
import pytest

import name_fixtures
from engine.config import NAME_PARAMS
from engine.name import liquidity as L
from engine.name.data import NameInputs

pytestmark = pytest.mark.unit

DATE = date(2026, 9, 18)
FRONT = date(2026, 9, 25)          # 7 calendar days out: the first expiry L6 may use
NEAR = date(2026, 9, 21)           # 3 calendar days out: too near for L6
SCHEMA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           "schemas", "ticker.schema.json")


# --------------------------------------------------------------------------------------------
# helpers: one synthetic name that clears every floor, and the schema check
# --------------------------------------------------------------------------------------------

def _contract(chain_id: str, option_type: str, strike: float, expiry: date, *,
              size_late: float = 50.0, spread: float = 0.02) -> dict:
    return {"option_chain_id": chain_id, "underlying_symbol": "SYN", "option_type": option_type,
            "strike": strike, "expiry": expiry, "date": DATE, "size_late": size_late,
            "vwap_late": 1.25, "late_rel_spread": spread, "late_last_bid": 1.2,
            "late_last_ask": 1.3, "last_nbbo_bid": 1.2, "last_nbbo_ask": 1.3}


def _contracts(n_strikes: int = 150, expiry: date = FRONT, **atm) -> pd.DataFrame:
    """`n_strikes` strikes x call/put at one expiry, the strike-100 pair overridable by `atm`.

    The grid is $5 wide so strike 100 is the only one inside L6's 2.5% band around close = 100.
    """
    rows = []
    for i in range(n_strikes):
        strike = 100.0 + 5 * i      # strike 100 is the ATM pair (close = 100)
        for option_type in ("call", "put"):
            kwargs = atm if strike == 100.0 else {}
            rows.append(_contract(f"{option_type[0]}{strike}", option_type, strike, expiry, **kwargs))
    return pd.DataFrame(rows)


def _sessions(n_hot: int = 20, n_sessions: int = 21) -> pd.DataFrame:
    days = [date(2026, 8, 20) + timedelta(days=i) for i in range(n_sessions)]
    return pd.DataFrame({"date": days,
                         "n_contracts": [300] * n_sessions, "n_hot": [n_hot] * n_sessions,
                         "n_prints": [1000] * n_sessions, "premium_total": [1e6] * n_sessions})


def _screener(**over) -> dict:
    return {"ticker": "SYN", "close": 100.0, "issue_type": "Common Stock", "is_index": False,
            "marketcap": 5e9, "iv30d": 0.5, "sector": "Industrials", **over}


def _inputs(*, screener=None, contracts=None, sessions=None, adv: float | None = 100e6) -> NameInputs:
    """A synthetic name that clears L1..L6; each test breaks exactly one of these."""
    return NameInputs(ticker="SYN", date=DATE,
                      screener=_screener() if screener is None else screener,
                      contracts_today=_contracts() if contracts is None else contracts,
                      contract_sessions=_sessions() if sessions is None else sessions,
                      adv_usd_20d=adv)


def _validate(section: dict) -> None:
    schema = json.loads(open(SCHEMA_PATH, encoding="utf-8").read())
    jsonschema.validate(section, {"$ref": "#/$defs/liquidity", "$defs": schema["$defs"]})


# --------------------------------------------------------------------------------------------
# the baseline, and L1 / L2
# --------------------------------------------------------------------------------------------

def test_a_name_clearing_every_floor_can_price_with_no_failing_floor():
    out = L.evaluate(_inputs())

    assert out["can_price"] is True
    assert out["failing"] is None
    assert out["contracts"] == 300
    assert out["hot_chain_days"] == 21
    assert out["adv_usd"] == 100e6
    assert out["atm_strike"] == 100.0
    assert out["atm_expiry"] == FRONT.isoformat()
    assert out["tier"] == 1
    assert out["atm_spread"] == pytest.approx(0.02)
    assert out["nulls"] == []


def test_l1_fails_when_the_issue_type_is_outside_the_sheets_three():
    out = L.evaluate(_inputs(screener=_screener(issue_type="Warrant")))

    assert out["failing"] == "L1"
    assert out["can_price"] is False


def test_l1_fails_on_an_index_even_with_an_allowed_issue_type():
    out = L.evaluate(_inputs(screener=_screener(is_index=True)))

    assert out["failing"] == "L1"


def test_l1_accepts_an_etf_because_the_sheet_extends_s_c_f1():
    out = L.evaluate(_inputs(screener=_screener(issue_type="ETF")))

    assert out["verdicts"]["L1"] is True
    assert out["can_price"] is True


def test_l1_fails_closed_with_a_reason_when_there_is_no_screener_row():
    out = L.evaluate(NameInputs(ticker="SYN", date=DATE))

    assert out["failing"] == "L1"
    assert any(n["field"] == "liquidity.screener" for n in out["nulls"])


def test_l2_fails_below_the_ten_dollar_price_floor():
    out = L.evaluate(_inputs(screener=_screener(close=9.99)))

    assert out["failing"] == "L2"
    assert out["verdicts"]["L1"] is True


# --------------------------------------------------------------------------------------------
# L3 / L4 / L5: the counts the marts answer
# --------------------------------------------------------------------------------------------

def test_l3_counts_distinct_option_chain_ids_and_fails_below_three_hundred():
    out = L.evaluate(_inputs(contracts=_contracts(n_strikes=149)))    # 298 contracts

    assert out["contracts"] == 298
    assert out["failing"] == "L3"


def test_l3_counts_a_contract_that_printed_twice_once():
    rows = _contracts()
    out = L.evaluate(_inputs(contracts=pd.concat([rows, rows], ignore_index=True)))

    assert out["contracts"] == 300
    assert out["verdicts"]["L3"] is True


def test_l3_fails_closed_with_a_reason_when_no_contract_rows_were_read():
    out = L.evaluate(_inputs(contracts=pd.DataFrame()))

    assert out["contracts"] is None
    assert out["failing"] == "L3"
    assert any(n["field"] == "liquidity.contracts" for n in out["nulls"])


def test_l4_counts_only_sessions_with_ten_or_more_hot_chain_contracts():
    sessions = _sessions()
    sessions.loc[:6, "n_hot"] = 9                                     # 7 thin sessions of 21
    out = L.evaluate(_inputs(sessions=sessions))

    assert out["hot_chain_days"] == 14
    assert out["failing"] == "L4"


def test_l4_passes_at_exactly_fifteen_hot_sessions():
    sessions = _sessions()
    sessions.loc[:5, "n_hot"] = 0
    out = L.evaluate(_inputs(sessions=sessions))

    assert out["hot_chain_days"] == 15
    assert out["verdicts"]["L4"] is True


def test_l4_fails_closed_with_a_reason_when_no_sessions_were_read():
    out = L.evaluate(_inputs(sessions=pd.DataFrame()))

    assert out["hot_chain_days"] is None
    assert out["failing"] == "L4"
    assert any(n["field"] == "liquidity.hot_chain_days" for n in out["nulls"])


def test_l5_fails_below_the_fifty_million_dollar_adv_floor():
    out = L.evaluate(_inputs(adv=49_999_999.0))

    assert out["failing"] == "L5"


def test_l5_fails_closed_with_a_reason_when_adv_is_null():
    out = L.evaluate(_inputs(adv=None))

    assert out["adv_usd"] is None
    assert out["failing"] == "L5"
    assert any(n["field"] == "liquidity.adv_usd" for n in out["nulls"])


# --------------------------------------------------------------------------------------------
# L6: the front-expiry ATM pair, its tier and its spread
# --------------------------------------------------------------------------------------------

def test_l6_uses_the_front_listed_expiry_at_least_seven_calendar_days_out():
    near = _contracts(expiry=NEAR)                                    # 3 DTE: skipped
    rows = pd.concat([near, _contracts(expiry=FRONT)], ignore_index=True)
    rows["option_chain_id"] = rows["option_chain_id"] + rows["expiry"].astype(str)
    out = L.evaluate(_inputs(contracts=rows))

    assert out["atm_expiry"] == FRONT.isoformat()
    assert out["can_price"] is True


def test_l6_fails_when_an_atm_leg_spread_is_above_the_eight_percent_cap():
    out = L.evaluate(_inputs(contracts=_contracts(spread=0.081)))

    assert out["failing"] == "L6"
    assert out["atm_spread"] == pytest.approx(0.081)


def test_l6_fails_when_neither_atm_leg_printed_the_minimum_size():
    out = L.evaluate(_inputs(contracts=_contracts(size_late=4.0)))

    assert out["failing"] == "L6"
    assert out["atm_strike"] is None
    assert any(n["field"] == "liquidity.atm_spread" for n in out["nulls"])


def test_l6_fails_when_a_selected_atm_leg_has_no_late_print_to_mark():
    rows = _contracts()                                               # sized, so the pair selects ..
    rows.loc[rows["strike"] == 100.0, "vwap_late"] = None             # .. but neither leg marks
    out = L.evaluate(_inputs(contracts=rows))

    assert out["failing"] == "L6"
    assert out["atm_strike"] == 100.0 and out["tier"] is None
    assert any(n["field"] == "liquidity.tier" for n in out["nulls"])


def test_l6_marks_a_selected_pair_at_tier_one_because_its_leg_size_is_the_tier_one_minimum():
    """D26 option 1: L6's `atm_leg_size_min` IS `marking.TIER1_MIN_SIZE`, so a pair that clears
    the size test always marks at tier 1 -- `tier <= 2` can only fail on an unmarkable leg."""
    out = L.evaluate(_inputs(contracts=_contracts(size_late=float(NAME_PARAMS.atm_leg_size_min))))

    assert out["tier"] == 1
    assert out["verdicts"]["L6"] is True


# --------------------------------------------------------------------------------------------
# order, nulls and the schema
# --------------------------------------------------------------------------------------------

def test_the_first_failing_floor_in_l1_to_l6_order_is_the_one_named():
    out = L.evaluate(_inputs(screener=_screener(close=5.0), contracts=pd.DataFrame(), adv=None))

    assert out["failing"] == "L2"                                     # L3 and L5 fail too
    assert out["verdicts"]["L3"] is False and out["verdicts"]["L5"] is False


def test_an_empty_inputs_object_still_produces_a_valid_all_null_section():
    out = L.evaluate(NameInputs(ticker="X", date=DATE))

    assert out["can_price"] is False and out["failing"] == "L1"
    assert all(out[k] is None for k in ("contracts", "hot_chain_days", "adv_usd", "atm_spread", "tier"))
    assert {n["field"] for n in out["nulls"]} >= {"liquidity.screener", "liquidity.contracts",
                                                 "liquidity.hot_chain_days", "liquidity.adv_usd"}
    _validate(out)


# --------------------------------------------------------------------------------------------
# the three stored fixtures (RESEARCH/20 §1.2: NVDA and OKLO price, BL does not)
# --------------------------------------------------------------------------------------------

@pytest.mark.parametrize("ticker", ["NVDA", "OKLO"])
def test_the_liquid_fixtures_can_price(ticker):
    out = L.evaluate(name_fixtures.load_fixture(ticker), NAME_PARAMS)

    if ticker == "OKLO":      # B1: L6 is measured at the monthly the sheet prices; OKLO has no 5-lot ATM pair there (S-C F8 agrees)
        assert out["can_price"] is False and out["failing"] == "L6" and out["atm_expiry"] == "2026-10-16"
        _validate(out)
        return
    assert out["can_price"] is True
    assert out["failing"] is None
    assert out["tier"] <= NAME_PARAMS.atm_tier_max
    assert out["atm_spread"] <= NAME_PARAMS.atm_spread_max
    _validate(out)


def test_the_thin_fixture_fails_l3_on_fifteen_contracts():
    out = L.evaluate(name_fixtures.load_fixture("BL"), NAME_PARAMS)

    assert out["can_price"] is False
    assert out["failing"] == "L3"
    assert out["contracts"] == 15
    assert out["hot_chain_days"] == 0
    _validate(out)


def test_the_nvda_fixture_reports_the_premium_expiry_atm_pair():
    out = L.evaluate(name_fixtures.load_fixture("NVDA"), NAME_PARAMS)

    assert out["atm_expiry"] == "2026-10-16"                          # B1: S-C's [21, 35]-DTE Friday nearest t + 28
    assert out["atm_strike"] == 220.0                                 # nearest close (222.27) with 5+ lots on both legs
    assert out["contracts"] == 2051
    assert out["hot_chain_days"] == 21


def test_every_number_in_the_section_names_a_source():
    out = L.evaluate(name_fixtures.load_fixture("NVDA"), NAME_PARAMS)

    assert {"contracts", "hot_chain_days", "adv_usd", "atm_spread"} <= set(out["source"])
    assert all(isinstance(v, str) and v for v in out["source"].values())
