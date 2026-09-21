"""engine.name.events (R2, findings/stock-deep-dive DESIGN/70 §1 row "Earnings date" and §7).

Offline throughout: synthetic `NameInputs` plus the three stored `tests/fixtures/name/` slices.
The agreement rule under test is the one in the module docstring -- three sources, each mapping
its `(date, hour)` to a set of plausible earnings *sessions*, and `confirmed` only when the
primary is non-null and every non-null source's set shares a session.
"""
from __future__ import annotations

import json
import os
from datetime import date

import jsonschema
import pandas as pd
import pytest

import name_fixtures
from engine.config import NAME_PARAMS
from engine.name import events as E
from engine.name.data import NameInputs

pytestmark = pytest.mark.unit

DATE = date(2026, 9, 18)                                  # a Friday
SCHEMA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           "schemas", "ticker.schema.json")


def _source(d: str | None, hour: str | None = None, name: str = "src") -> dict:
    return {"date": d, "hour": hour, "source": name, "reason": None if d else "null"}


def _dates(finnhub=None, screener=None, yfinance=None) -> dict:
    return {"finnhub": finnhub or _source(None), "screener": screener or _source(None),
            "yfinance": yfinance or _source(None)}


def _chain(expiries) -> pd.DataFrame:
    return pd.DataFrame({"symbol": ["SYN"] * len(expiries), "expiry": list(expiries),
                         "strike": [100.0] * len(expiries), "right": ["C"] * len(expiries)})


def _inputs(**over) -> NameInputs:
    kwargs = {"ticker": "SYN", "date": DATE, "screener": {"ticker": "SYN"},
              "earnings_dates": _dates(), "fomc": []}
    return NameInputs(**{**kwargs, **over})


def _validate(section: dict) -> None:
    schema = json.loads(open(SCHEMA_PATH, encoding="utf-8").read())
    jsonschema.validate(section, {"$ref": "#/$defs/events", "$defs": schema["$defs"]})


# --------------------------------------------------------------------------------------------
# the (date, hour) -> plausible sessions map
# --------------------------------------------------------------------------------------------

def test_a_before_open_print_is_reflected_by_the_close_of_its_own_session():
    assert E.session_set(date(2026, 11, 17), "bmo") == {date(2026, 11, 17)}


def test_an_after_close_print_is_reflected_by_the_next_sessions_close():
    assert E.session_set(date(2026, 11, 17), "amc") == {date(2026, 11, 18)}


def test_an_unknown_hour_leaves_both_sessions_plausible():
    assert E.session_set(date(2026, 11, 17), None) == {date(2026, 11, 17), date(2026, 11, 18)}
    assert E.session_set(date(2026, 11, 17), "unknown") == {date(2026, 11, 17), date(2026, 11, 18)}


def test_a_before_open_print_on_a_non_session_rolls_to_the_next_session():
    assert E.session_set(date(2026, 11, 21), "bmo") == {date(2026, 11, 23)}   # a Saturday


def test_the_screeners_and_finnhubs_hour_spellings_map_to_the_same_sessions():
    assert E.session_set(date(2026, 11, 17), "premarket") == E.session_set(date(2026, 11, 17), "bmo")
    assert E.session_set(date(2026, 11, 17), "postmarket") == E.session_set(date(2026, 11, 17), "amc")


def test_a_null_date_has_no_plausible_session_at_all():
    assert E.session_set(None, "amc") is None


# --------------------------------------------------------------------------------------------
# confirmation: the intersection of every non-null source's set
# --------------------------------------------------------------------------------------------

def test_three_sources_that_share_one_session_confirm_it_even_on_different_dates():
    out = E.evaluate(_inputs(earnings_dates=_dates(
        finnhub=_source("2026-11-17", "amc"),                  # -> {11-18}
        screener=_source("2026-11-18", "unknown"),             # -> {11-18, 11-19}
        yfinance=_source("2026-11-17", None))))                # -> {11-17, 11-18}

    assert out["earnings"]["confirmed"] is True
    assert out["earnings"]["session_date"] == "2026-11-18"
    assert out["earnings"]["date"] == "2026-11-17"             # the primary's own date, printed as is


def test_sources_whose_sessions_never_meet_are_not_confirmed():
    out = E.evaluate(_inputs(earnings_dates=_dates(
        finnhub=_source("2026-11-04", "amc"),                  # -> {11-05}
        yfinance=_source("2026-11-03", None))))                # -> {11-03, 11-04}

    assert out["earnings"]["confirmed"] is False
    assert any("disagree" in n["reason"] for n in out["nulls"])


def test_a_null_primary_is_never_confirmed_even_when_the_others_agree():
    out = E.evaluate(_inputs(earnings_dates=_dates(
        screener=_source("2026-11-18", "unknown"), yfinance=_source("2026-11-18", None))))

    assert out["earnings"]["confirmed"] is False
    assert out["earnings"]["date"] is None
    assert any(n["field"] == "events.earnings.date" for n in out["nulls"])


def test_the_primary_alone_confirms_when_the_other_two_are_null():
    out = E.evaluate(_inputs(earnings_dates=_dates(finnhub=_source("2026-11-17", "bmo"))))

    assert out["earnings"]["confirmed"] is True
    assert out["earnings"]["session_date"] == "2026-11-17"


def test_the_session_label_and_the_days_to_come_from_the_primary_and_the_session():
    out = E.evaluate(_inputs(earnings_dates=_dates(finnhub=_source("2026-11-17", "amc"))))

    assert out["earnings"]["session"] == "post"
    assert out["earnings"]["days_to"] == (date(2026, 11, 18) - DATE).days


@pytest.mark.parametrize("hour,label", [("bmo", "pre"), ("amc", "post"), ("dmh", "unknown"),
                                        (None, "unknown")])
def test_the_session_label_maps_every_primary_hour(hour, label):
    out = E.evaluate(_inputs(earnings_dates=_dates(finnhub=_source("2026-11-17", hour))))

    assert out["earnings"]["session"] == label


def test_all_three_sources_are_printed_side_by_side_whatever_they_say():
    out = E.evaluate(_inputs(earnings_dates=_dates(finnhub=_source("2026-11-17", "amc"))))

    assert [s["name"] for s in out["earnings"]["sources"]] == ["finnhub", "screener", "yfinance"]
    assert [s["date"] for s in out["earnings"]["sources"]] == ["2026-11-17", None, None]


# --------------------------------------------------------------------------------------------
# ex-dividend, expiries, macro, and the X1 window
# --------------------------------------------------------------------------------------------

def test_ex_div_is_printed_only_when_the_next_dividend_is_ahead_of_the_sheet_date():
    ahead = E.evaluate(_inputs(screener={"next_dividend_date": "2026-12-04T00:00:00"}))
    behind = E.evaluate(_inputs(screener={"next_dividend_date": "2026-09-10T00:00:00"}))

    assert ahead["ex_div"] == "2026-12-04"
    assert behind["ex_div"] is None


def test_an_unparseable_next_dividend_date_is_a_null_not_an_exception():
    out = E.evaluate(_inputs(screener={"next_dividend_date": "NaT"}))

    assert out["ex_div"] is None


def test_expiries_are_the_first_two_chain_expiries_at_least_seven_calendar_days_out():
    chain = _chain([date(2026, 9, 21), date(2026, 9, 25), date(2026, 9, 28), date(2026, 9, 30)])
    out = E.evaluate(_inputs(chain=chain))

    assert out["expiries"] == ["2026-09-25", "2026-09-28"]       # 09-21 is 3 calendar days out


def test_expiries_fall_back_to_the_days_contract_prints_when_there_is_no_chain():
    rows = pd.DataFrame({"expiry": [date(2026, 9, 18), date(2026, 10, 2), date(2026, 10, 16)],
                         "option_chain_id": ["a", "b", "c"]})
    out = E.evaluate(_inputs(chain=None, contracts_today=rows))

    assert out["expiries"] == ["2026-10-02", "2026-10-16"]
    assert "daily_contract" in out["source"]["expiries"]


def test_a_name_with_no_chain_and_no_prints_reports_no_expiries_with_a_reason():
    out = E.evaluate(_inputs())

    assert out["expiries"] == []
    assert any(n["field"] == "events.expiries" for n in out["nulls"])


def test_macro_carries_every_fomc_decision_the_loader_found():
    out = E.evaluate(_inputs(fomc=["2026-10-28"]))

    assert out["macro"] == [{"date": "2026-10-28", "event": "FOMC"}]


def test_x1_blocks_through_the_earnings_session_when_the_sources_agree():
    out = E.evaluate(_inputs(earnings_dates=_dates(finnhub=_source("2026-11-17", "amc"))))

    assert out["x1_window_end"] == "2026-11-18"


def test_x1_blocks_for_the_unknown_earnings_window_when_they_do_not():
    out = E.evaluate(_inputs(earnings_dates=_dates(screener=_source("2026-11-18", "unknown"))))

    assert out["x1_window_end"] == "2026-11-02"                  # DATE + x1_unknown_earnings_days
    assert NAME_PARAMS.x1_unknown_earnings_days == 45


# --------------------------------------------------------------------------------------------
# the three stored fixtures and the schema
# --------------------------------------------------------------------------------------------

def test_the_nvda_fixture_agrees_on_the_november_eighteenth_session():
    out = E.evaluate(name_fixtures.load_fixture("NVDA"), NAME_PARAMS)

    assert out["earnings"]["confirmed"] is True
    assert out["earnings"]["session_date"] == "2026-11-18"
    assert out["earnings"]["date"] == "2026-11-17"
    assert out["earnings"]["session"] == "post"
    assert out["earnings"]["days_to"] == 61
    assert out["ex_div"] is None                                 # 2026-09-10 is behind the sheet
    assert out["expiries"] == ["2026-09-25", "2026-09-28"]
    assert out["macro"] == [{"date": "2026-10-28", "event": "FOMC"}]
    _validate(out)


def test_the_bl_fixture_sources_disagree_so_x1_runs_for_the_unknown_window():
    out = E.evaluate(name_fixtures.load_fixture("BL"), NAME_PARAMS)

    assert out["earnings"]["confirmed"] is False
    assert out["x1_window_end"] == "2026-11-02"
    _validate(out)


def test_the_oklo_fixture_confirms_on_a_null_primary_hour():
    out = E.evaluate(name_fixtures.load_fixture("OKLO"), NAME_PARAMS)

    assert out["earnings"]["confirmed"] is True
    assert out["earnings"]["session"] == "unknown"
    assert out["earnings"]["session_date"] == "2026-11-10"
    assert out["expiries"] == ["2026-09-25", "2026-10-02"]
    _validate(out)


def test_an_empty_inputs_object_still_produces_a_valid_all_null_section():
    out = E.evaluate(NameInputs(ticker="X", date=DATE))

    assert out["earnings"]["date"] is None and out["earnings"]["session"] is None
    assert out["earnings"]["confirmed"] is False and out["earnings"]["days_to"] is None
    assert len(out["earnings"]["sources"]) == 3
    assert out["ex_div"] is None and out["expiries"] == [] and out["macro"] == []
    assert {n["field"] for n in out["nulls"]} >= {"events.earnings.date", "events.expiries"}
    _validate(out)
