"""engine.name.premium (R2, findings/stock-deep-dive DESIGN/70 §3): section C and its verdict.

Offline throughout. The synthetic baseline is built so every number has a closed form:

    rv5 = 0.04 / 252 on 21 quality sessions   -> rv5_21   = 100 * sqrt(252 * rv5)      = 20.00
    one +3% session in 21 close-to-close ones -> rv_c2c_21 = 100 * ln(1.03) * sqrt(20)/21 * sqrt(252)
    iv30d 0.30                                -> spread_rv5 = +10.00, spread_c2c = +20.00 -> RICH

Each test then breaks exactly one of those inputs. The three stored fixtures pin the real numbers.
"""
from __future__ import annotations

import json
import math
import os
from datetime import date, timedelta

import jsonschema
import pandas as pd
import pytest

import name_fixtures
from engine.config import NAME_PARAMS
from engine.name import premium as P
from engine.name.data import NameInputs

pytestmark = pytest.mark.unit

DATE = date(2026, 9, 18)
SC_EXPIRY = date(2026, 10, 16)                # Friday, 28 calendar days out: what S-C picks
E1, E2 = date(2026, 9, 25), date(2026, 9, 28)  # the two slope expiries
SCHEMA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           "schemas", "ticker.schema.json")

RV5_FLAT = 0.04 / 252                          # -> rv5_21 = 20.00 vol points
MOVE = 0.03                                    # the one non-flat close-to-close session
RV_C2C = 100 * math.log(1 + MOVE) * math.sqrt(20) / 21 * math.sqrt(252)


# --------------------------------------------------------------------------------------------
# builders
# --------------------------------------------------------------------------------------------

def _screener(**over) -> dict:
    return {"ticker": "SYN", "close": 100.0, "issue_type": "Common Stock", "is_index": False,
            "marketcap": 5e9, "iv30d": 0.30, "sector": "Industrials",
            "next_earnings_date": "2026-12-18T00:00:00", "implied_move_perc": 0.06, **over}


def _contracts(expiry: date = SC_EXPIRY, size_late: float = 50.0) -> pd.DataFrame:
    rows = []
    for i in range(6):
        strike = 100.0 + 5 * i
        for option_type in ("call", "put"):
            rows.append({"option_chain_id": f"{option_type[0]}{strike}", "option_type": option_type,
                         "strike": strike, "expiry": expiry, "date": DATE, "size_late": size_late,
                         "vwap_late": 1.25, "late_rel_spread": 0.02, "late_last_bid": 1.2,
                         "late_last_ask": 1.3, "last_nbbo_bid": 1.2, "last_nbbo_ask": 1.3})
    return pd.DataFrame(rows)


def _rv(n_quality: int = 21, rv5: float = RV5_FLAT) -> pd.DataFrame:
    days = [DATE - timedelta(days=30 - i) for i in range(21)]
    return pd.DataFrame({"underlying_symbol": ["SYN"] * 21, "date": days, "rv5": [rv5] * 21,
                         "quality": [i >= 21 - n_quality for i in range(21)]})


def _bars(move: float = MOVE, n: int = 40, last: date = DATE) -> pd.DataFrame:
    """Flat closes but for one `move` session, so the last 21 log returns have a closed-form std."""
    closes, price = [], 100.0
    for i in range(n):
        price = price * (1 + move) if i == n - 5 else price
        closes.append(price)
    days = [last - timedelta(days=n - 1 - i) for i in range(n)]
    return pd.DataFrame({"date": days, "open": closes, "high": closes, "low": closes,
                         "close": closes, "adj": closes, "volume": [1e6] * n})


def _history(n: int = 70, iv: float = 0.30) -> pd.DataFrame:
    """`n` trailing screener rows whose iv30d rises to `iv` on the sheet date (percentile 100)."""
    days = [DATE - timedelta(days=n - 1 - i) for i in range(n)]
    ivs = [iv / 2] * (n - 1) + [iv]
    return pd.DataFrame({"date": days, "iv30d": ivs, "close": [100.0] * n})


def _chain(iv1: float = 0.30, iv2: float = 0.32) -> pd.DataFrame:
    rows = [{"expiry": e, "strike": 100.0, "right": r, "iv": v, "underlying_price": 100.0}
            for e, v in ((E1, iv1), (E2, iv2)) for r in ("C", "P")]
    return pd.DataFrame(rows)


def _events(**over) -> dict:
    earnings = {"date": "2026-12-17", "session": "post", "session_date": "2026-12-18",
                "sources": [], "confirmed": True, "days_to": 91}
    out = {"earnings": {**earnings, **over.pop("earnings", {})},
           "ex_div": None, "expiries": [E1.isoformat(), E2.isoformat()], "macro": [],
           "x1_window_end": "2026-12-18"}
    return {**out, **over}


def _inputs(**over) -> NameInputs:
    kwargs = {"ticker": "SYN", "date": DATE, "screener": _screener(),
              "contracts_today": _contracts(), "rv": _rv(), "bars": _bars(),
              "screener_history": _history(), "chain": _chain(), "adv_usd_20d": 100e6,
              "earnings_events": pd.DataFrame(), "earnings_history": pd.DataFrame()}
    return NameInputs(**{**kwargs, **over})


def _validate(section: dict) -> None:
    schema = json.loads(open(SCHEMA_PATH, encoding="utf-8").read())
    jsonschema.validate(section, {"$ref": "#/$defs/premium", "$defs": schema["$defs"]})


# --------------------------------------------------------------------------------------------
# the four vol numbers and the two spreads
# --------------------------------------------------------------------------------------------

def test_the_baseline_prints_both_vols_as_points_and_iv_as_the_decimal():
    out = P.evaluate(_inputs(), NAME_PARAMS, _events())

    assert out["iv30d"] == pytest.approx(0.30)                       # a decimal, as the screener has it
    assert out["rv5_21"] == pytest.approx(20.0)
    assert out["rv_c2c_21"] == pytest.approx(RV_C2C)
    assert out["spread_rv5"] == pytest.approx(10.0)                  # 100 x iv30d - rv5_21, vol points
    assert out["spread_c2c"] == pytest.approx(30.0 - RV_C2C)
    assert "vol points" in out["source"]["spread_rv5"]


def test_rv5_uses_only_quality_sessions_and_annualises_the_daily_variance():
    out = P.evaluate(_inputs(rv=_rv(n_quality=21, rv5=0.09 / 252)), NAME_PARAMS, _events())

    assert out["rv5_21"] == pytest.approx(30.0)                      # 100 x sqrt(252 x 0.09/252)


def test_rv5_is_null_below_the_fifteen_quality_session_minimum():
    out = P.evaluate(_inputs(rv=_rv(n_quality=14)), NAME_PARAMS, _events())

    assert out["rv5_21"] is None and out["spread_rv5"] is None
    assert out["verdict"] == "CANNOT_MEASURE"
    assert any(n["field"] == "premium.rv5_21" for n in out["nulls"])


def test_the_rv_source_names_the_window_the_lagging_panel_actually_carried():
    inputs = _inputs()
    out = P.evaluate(inputs, NAME_PARAMS, _events())

    assert inputs.rv["date"].max().isoformat() in out["source"]["rv5_21"]


def test_the_close_to_close_window_ends_on_or_before_the_sheet_date():
    bars = pd.concat([_bars(), _bars(move=0.5, n=5, last=DATE + timedelta(days=5))],
                     ignore_index=True)
    out = P.evaluate(_inputs(bars=bars), NAME_PARAMS, _events())

    assert out["rv_c2c_21"] == pytest.approx(RV_C2C)                 # the future bars are ignored


def test_both_vol_numbers_are_null_with_a_reason_when_their_inputs_are_empty():
    out = P.evaluate(_inputs(rv=pd.DataFrame(), bars=pd.DataFrame()), NAME_PARAMS, _events())

    assert out["rv5_21"] is None and out["rv_c2c_21"] is None
    assert {"premium.rv5_21", "premium.rv_c2c_21"} <= {n["field"] for n in out["nulls"]}


def test_a_null_iv30d_leaves_both_spreads_null():
    out = P.evaluate(_inputs(screener=_screener(iv30d=None)), NAME_PARAMS, _events())

    assert out["iv30d"] is None and out["spread_rv5"] is None and out["spread_c2c"] is None
    assert any(n["field"] == "premium.iv30d" for n in out["nulls"])


# --------------------------------------------------------------------------------------------
# iv_pct_own and slope
# --------------------------------------------------------------------------------------------

def test_iv_pct_own_is_the_percentile_of_todays_iv_in_the_names_own_history():
    out = P.evaluate(_inputs(), NAME_PARAMS, _events())

    assert out["iv_pct_own"] == pytest.approx(100.0)                 # the highest of its 70 sessions


def test_iv_pct_own_is_null_below_the_sixty_three_session_minimum():
    out = P.evaluate(_inputs(screener_history=_history(n=62)), NAME_PARAMS, _events())

    assert out["iv_pct_own"] is None
    assert any(n["field"] == "premium.iv_pct_own" for n in out["nulls"])


def test_slope_is_the_second_expirys_atm_iv_minus_the_firsts_in_points():
    out = P.evaluate(_inputs(), NAME_PARAMS, _events())

    assert out["slope"] == pytest.approx(2.0)                        # 100 x (0.32 - 0.30)


def test_slope_is_null_without_a_live_chain():
    out = P.evaluate(_inputs(chain=None), NAME_PARAMS, _events())

    assert out["slope"] is None
    assert any(n["field"] == "premium.slope" for n in out["nulls"])


def test_slope_is_null_when_the_section_found_fewer_than_two_expiries():
    out = P.evaluate(_inputs(), NAME_PARAMS, _events(expiries=[E1.isoformat()]))

    assert out["slope"] is None


# --------------------------------------------------------------------------------------------
# the prior-print table
# --------------------------------------------------------------------------------------------

def _events_panel(rows) -> pd.DataFrame:
    return pd.DataFrame([{"ticker": "SYN", "E": e, "implied_move_perc": imp, "realized_move": real}
                         for e, imp, real in rows])


def test_each_panel_print_carries_its_implied_move_its_realized_move_and_the_ratio():
    panel = _events_panel([(date(2026, 5, 20), 0.05, -0.10), (date(2026, 8, 26), 0.04, 0.02)])
    out = P.evaluate(_inputs(earnings_events=panel), NAME_PARAMS, _events())

    assert [r["E"] for r in out["earnings_history"]] == ["2026-05-20", "2026-08-26"]
    assert out["earnings_history"][0]["realized_move"] == pytest.approx(0.10)   # sign is dropped
    assert out["earnings_history"][0]["ratio"] == pytest.approx(2.0)
    assert out["earnings_history"][0]["implied_source"] == "screener implied_move_perc"
    assert out["median_ratio_8"] == pytest.approx(1.25)                          # median(2.0, 0.5)


def test_the_ten_year_panel_only_adds_prints_the_events_panel_does_not_have():
    panel = _events_panel([(date(2026, 8, 26), 0.04, 0.02)])
    older = pd.DataFrame([{"ticker": "SYN", "E": date(2024, 2, 1), "abs_move_yahoo": 0.07},
                          {"ticker": "SYN", "E": date(2026, 8, 26), "abs_move_yahoo": 0.99}])
    out = P.evaluate(_inputs(earnings_events=panel, earnings_history=older), NAME_PARAMS, _events())

    assert [r["E"] for r in out["earnings_history"]] == ["2024-02-01", "2026-08-26"]
    assert out["earnings_history"][0]["implied_move"] is None
    assert out["earnings_history"][0]["realized_move"] == pytest.approx(0.07)
    assert out["earnings_history"][0]["ratio"] is None
    assert out["earnings_history"][1]["realized_move"] == pytest.approx(0.02)    # the panel wins


def test_only_the_last_eight_prints_are_kept():
    panel = _events_panel([(date(2024, 1, 1) + timedelta(days=90 * i), 0.05, 0.05)
                           for i in range(12)])
    out = P.evaluate(_inputs(earnings_events=panel), NAME_PARAMS, _events())

    assert len(out["earnings_history"]) == NAME_PARAMS.earnings_history_n == 8
    kept = (date(2024, 1, 1) + timedelta(days=90 * 4)).isoformat()                # the 5th of 12
    assert out["earnings_history"][0]["E"] == kept


def test_no_prior_prints_is_an_empty_table_and_a_null_median():
    out = P.evaluate(_inputs(), NAME_PARAMS, _events())

    assert out["earnings_history"] == [] and out["median_ratio_8"] is None


# --------------------------------------------------------------------------------------------
# the S-C verdicts the sheet grades its own filters with
# --------------------------------------------------------------------------------------------

def test_a_name_inside_every_s_c_band_passes_with_its_expiry_and_sigma():
    out = P.evaluate(_inputs(), NAME_PARAMS, _events())

    assert out["sc"]["pass"] is True and out["sc"]["failing"] is None
    assert out["sc"]["expiry"] == "2026-10-16" and out["sc"]["dte_cal"] == 28
    assert out["sc"]["sigma_hold"] == pytest.approx(100 * 0.30 * math.sqrt(28 / 365))
    assert set(out["sc"]["verdicts"]) == {f"F{i}" for i in range(1, 10)}


def test_a_market_cap_above_s_c_s_band_fails_f3_first():
    out = P.evaluate(_inputs(screener=_screener(marketcap=25e9)), NAME_PARAMS, _events())

    assert out["sc"]["pass"] is False and out["sc"]["failing"] == "F3"
    assert out["sc"]["verdicts"]["F6"] is True            # F6 is still reported, and still passes


def test_the_s_c_block_reads_the_sheets_own_dollar_adv():
    out = P.evaluate(_inputs(adv_usd_20d=1e6), NAME_PARAMS, _events())

    assert out["sc"]["failing"] == "F4"


# --------------------------------------------------------------------------------------------
# the S-A measurement line, X1 and the verdict table
# --------------------------------------------------------------------------------------------

def test_no_s_a_line_when_the_print_is_outside_the_thirty_day_window():
    out = P.evaluate(_inputs(), NAME_PARAMS, _events())

    assert out["sa"] is None


def test_an_s_a_line_appears_inside_the_window_and_says_s_a_is_closed():
    out = P.evaluate(_inputs(), NAME_PARAMS,
                     _events(earnings={"days_to": 12, "session_date": "2026-09-30"}))

    assert out["sa"]["window_days"] == 30
    assert set(out["sa"]["filters"]) == {"F1", "F2", "F3", "F4", "F7", "F8"}
    assert out["sa"]["filters"]["F8"] is True            # "post" -> postmarket, how = labelled
    assert out["sa"]["first_fail"] is None
    assert "closed at retail execution" in out["sa"]["note"]


def test_the_s_a_line_names_its_first_failing_filter():
    out = P.evaluate(_inputs(screener=_screener(implied_move_perc=0.005)), NAME_PARAMS,
                     _events(earnings={"days_to": 12, "session_date": "2026-09-30"}))

    assert out["sa"]["first_fail"] == "F7"


def test_x1_is_false_when_the_print_falls_after_the_premium_expiry():
    out = P.evaluate(_inputs(), NAME_PARAMS, _events())

    assert out["x1"] is False


def test_x1_is_true_when_a_premium_structure_at_that_expiry_would_sit_on_the_print():
    out = P.evaluate(_inputs(), NAME_PARAMS,
                     _events(earnings={"session_date": "2026-10-09", "days_to": 21},
                             x1_window_end="2026-10-09"))

    assert out["x1"] is True


def test_x1_is_true_whenever_the_earnings_sources_did_not_confirm():
    out = P.evaluate(_inputs(), NAME_PARAMS,
                     _events(earnings={"confirmed": False}, x1_window_end="2026-11-02"))

    assert out["x1"] is True


def test_x1_falls_back_to_the_next_friday_after_twenty_eight_days_without_an_s_c_expiry():
    out = P.evaluate(_inputs(screener=_screener(marketcap=25e9)), NAME_PARAMS,
                     _events(earnings={"session_date": "2026-10-16", "days_to": 28},
                             x1_window_end="2026-10-16"))

    assert out["sc"]["expiry"] is None
    assert out["x1"] is True                             # 2026-09-18 + 28 days IS Friday 10-16


# --------------------------------------------------------------------------------------------
# the verdict table (DESIGN/70 §3; the label never sizes anything)
# --------------------------------------------------------------------------------------------

def test_rich_needs_both_spreads_wide_and_no_x1():
    out = P.evaluate(_inputs(), NAME_PARAMS, _events())

    assert out["verdict"] == "RICH"


def test_rich_becomes_fair_the_moment_x1_applies():
    out = P.evaluate(_inputs(), NAME_PARAMS, _events(earnings={"confirmed": False}))

    assert out["x1"] is True and out["verdict"] == "FAIR"


def test_a_middling_spread_is_fair():
    out = P.evaluate(_inputs(screener=_screener(iv30d=0.25)), NAME_PARAMS, _events())

    assert out["spread_rv5"] == pytest.approx(5.0) and out["verdict"] == "FAIR"


def test_a_thin_rv5_spread_is_cheap():
    out = P.evaluate(_inputs(screener=_screener(iv30d=0.21)), NAME_PARAMS, _events())

    assert out["spread_rv5"] == pytest.approx(1.0) and out["verdict"] == "CHEAP"


def test_a_close_to_close_spread_below_minus_five_is_cheap_however_wide_rv5_looks():
    bars = _bars(move=0.30)                                   # c2c far above iv: spread_c2c << -5
    out = P.evaluate(_inputs(bars=bars), NAME_PARAMS, _events())

    assert out["spread_c2c"] < NAME_PARAMS.cheap_spread_c2c and out["verdict"] == "CHEAP"


# --------------------------------------------------------------------------------------------
# the three stored fixtures and the schema
# --------------------------------------------------------------------------------------------

def _fixture(ticker: str) -> dict:
    from engine.name import events as E
    inputs = name_fixtures.load_fixture(ticker)
    return P.evaluate(inputs, NAME_PARAMS, E.evaluate(inputs, NAME_PARAMS))


def test_the_nvda_fixture_is_cheap_on_close_to_close_and_fails_s_c_f3():
    out = _fixture("NVDA")

    assert out["iv30d"] == pytest.approx(0.3139, abs=1e-4)
    assert out["rv5_21"] == pytest.approx(24.07, abs=0.01)
    assert out["rv_c2c_21"] == pytest.approx(43.64, abs=0.01)
    assert out["spread_rv5"] == pytest.approx(7.32, abs=0.01)
    assert out["spread_c2c"] == pytest.approx(-12.25, abs=0.01)
    assert out["slope"] == pytest.approx(-1.61, abs=0.01)
    assert out["verdict"] == "CHEAP"                          # spread_c2c <= -5
    assert out["sc"]["failing"] == "F3"                       # marketcap above $20B
    assert out["sc"]["verdicts"]["F6"] is True                # and F6 still passes at 0.314
    assert out["x1"] is False and out["sa"] is None
    assert out["median_ratio_8"] == pytest.approx(1.0385, abs=1e-4)
    _validate(out)


def test_the_oklo_fixture_reaches_f8_before_failing():
    out = _fixture("OKLO")

    assert out["sc"]["failing"] == "F8"                       # no ATM pair at 20+ lots on both legs
    assert out["sc"]["verdicts"]["F3"] is True and out["sc"]["verdicts"]["F6"] is True
    assert out["sc"]["expiry"] == "2026-10-16"
    assert out["verdict"] == "CHEAP"
    _validate(out)


def test_the_bl_fixture_cannot_measure_because_no_rv_session_is_quality():
    out = _fixture("BL")

    assert out["rv5_21"] is None and out["verdict"] == "CANNOT_MEASURE"
    assert out["sc"]["failing"] in {"F3", "F4", "F7", "F8"}
    assert out["x1"] is True                                  # its three sources disagree
    _validate(out)


def test_an_empty_inputs_object_still_produces_a_valid_all_null_section():
    from engine.name import events as E
    inputs = NameInputs(ticker="X", date=DATE)
    out = P.evaluate(inputs, NAME_PARAMS, E.evaluate(inputs, NAME_PARAMS))

    assert all(out[k] is None for k in ("iv30d", "iv_pct_own", "rv5_21", "rv_c2c_21",
                                        "spread_rv5", "spread_c2c", "slope", "median_ratio_8"))
    assert out["verdict"] == "CANNOT_MEASURE" and out["earnings_history"] == []
    assert out["sc"]["pass"] is False and out["sa"] is None and out["x1"] is True
    assert {"premium.iv30d", "premium.rv5_21"} <= {n["field"] for n in out["nulls"]}
    _validate(out)


def test_b2_an_etf_is_never_x1_on_a_null_earnings_date():
    """B2: an ETF has no print; the null-date rule would otherwise exclude every ETF sheet forever."""
    from datetime import date as _date
    from engine.name.data import NameInputs
    etf = NameInputs(ticker="SMH", date=_date(2026, 9, 18),
                     screener={"ticker": "SMH", "issue_type": "ETF", "close": 573.0, "iv30d": 0.308})
    events = {"earnings": {"date": None, "session": None, "sources": [], "confirmed": False, "days_to": None},
              "x1_window_end": "2026-11-02", "expiries": [], "macro": [], "source": {}, "nulls": []}
    assert P._x1(etf, NAME_PARAMS, events, {"pass": False, "failing": "F1", "expiry": None}) is False
    stock = NameInputs(ticker="X", date=_date(2026, 9, 18), screener={"ticker": "X", "issue_type": "Common Stock", "close": 50.0})
    assert P._x1(stock, NAME_PARAMS, events, {"pass": False, "failing": "F3", "expiry": None}) is True
