"""engine.name.range (R3, findings/stock-deep-dive DESIGN/70 §4D, §7 `range`, §8 line D).

Synthetic chains whose zero-gamma answer is known by construction, synthetic bars whose Wilder
ATR is hand-computed, and the three stored fixtures. No network, no panel.
"""
from __future__ import annotations

import json
import math
import os
from datetime import date, timedelta

import pandas as pd
import pytest

import name_fixtures
from engine import config, schema
from engine.config import NAME_PARAMS
from engine.name import range as R
from engine.strategies import sc_filters

pytestmark = pytest.mark.unit

D = date(2026, 9, 18)
SCHEMA = json.load(open(os.path.join(config.REPO, "schemas", "ticker.schema.json"), encoding="utf-8"))


def section_schema(name: str) -> dict:
    return {"$ref": f"#/$defs/{name}", "$defs": SCHEMA["$defs"]}


def assert_valid(section: dict, name: str = "range") -> None:
    assert schema.validate(section, section_schema(name)) == []


# ---- builders ---------------------------------------------------------------------------------

def chain(rows: list[dict], spot: float) -> pd.DataFrame:
    """A `cboe_chain`-shaped frame; `rows` carry expiry, strike, right and any of mid/gamma/oi."""
    return pd.DataFrame([{
        "symbol": "X", "expiry": r["expiry"], "strike": float(r["strike"]), "right": r["right"],
        "bid": r.get("bid", r.get("mid")), "ask": r.get("ask", r.get("mid")), "mid": r.get("mid"),
        "iv": r.get("iv", 0.3), "delta": r.get("delta", 0.5), "gamma": r.get("gamma", 0.0),
        "open_interest": r.get("oi", 0.0), "volume": 0.0, "underlying_price": spot,
    } for r in rows])


def gex_chain(per_strike: dict[float, float], spot: float) -> pd.DataFrame:
    """One row per strike whose signed GEX is exactly `per_strike[k]`: `gamma * oi * 100 * spot`
    with `right` carrying the sign (C = +1, P = -1), which is `gex_per_strike`'s convention."""
    rows = []
    for k, g in per_strike.items():
        scale = abs(g) / (100.0 * spot)
        rows.append({"expiry": D + timedelta(days=30), "strike": k, "right": "C" if g > 0 else "P",
                     "mid": 1.0, "gamma": 1.0, "oi": scale})
    return chain(rows, spot)


def bars(n: int, *, start: date = date(2026, 1, 2), high: float = 100.5, low: float = 99.5,
         close: float = 100.0) -> pd.DataFrame:
    days = [start + timedelta(days=i) for i in range(n)]
    return pd.DataFrame({"date": days, "open": [close] * n, "high": [high] * n, "low": [low] * n,
                         "close": [close] * n, "adj": [close] * n, "volume": [1e6] * n})


def inputs(**kw):
    from engine.name.data import NameInputs
    return NameInputs(ticker=kw.pop("ticker", "X"), date=kw.pop("date", D), **kw)


# ---- zero gamma (DECISIONS D10: nearest spot, not uw's first crossing) --------------------------

def test_zero_gamma_is_the_sign_change_nearest_spot_not_the_first_one():
    spot = 220.0
    df = gex_chain({60.0: -2.0, 70.0: +3.0, 100.0: +1.0, 200.0: -5.0, 210.0: -1.0, 230.0: +1.0}, spot)

    out = R.evaluate(inputs(chain=df, chain_meta={"source": "cboe_chain", "date": D.isoformat()}), NAME_PARAMS)

    assert out["zero_gamma_all_crossings"] == [70.0, 200.0]
    assert out["zero_gamma"] == 200.0            # |220 - 200| < |220 - 70|; uw would report ~70
    assert out["gex_sign"] == "-"
    assert out["gex_total"] == pytest.approx(-3.0)


def test_zero_gamma_is_null_when_cumulative_gex_never_changes_sign():
    df = gex_chain({60.0: 1.0, 70.0: 2.0, 200.0: 3.0}, 220.0)

    out = R.evaluate(inputs(chain=df, chain_meta={"source": "cboe_chain", "date": D.isoformat()}), NAME_PARAMS)

    assert out["zero_gamma"] is None
    assert out["zero_gamma_all_crossings"] == []
    assert out["gex_sign"] == "+"
    assert any(n["field"] == "zero_gamma" for n in out["nulls"])


def test_gex_is_null_without_a_chain():
    out = R.evaluate(inputs(), NAME_PARAMS)

    assert out["gex_total"] is None and out["gex_sign"] is None and out["zero_gamma"] is None
    assert {n["field"] for n in out["nulls"]} >= {"gex_total", "zero_gamma"}


# ---- the front straddle ------------------------------------------------------------------------

def straddle_inputs(**kw):
    front, early = D + timedelta(days=7), D + timedelta(days=3)
    df = chain([
        {"expiry": early, "strike": 100.0, "right": "C", "mid": 9.0},
        {"expiry": early, "strike": 100.0, "right": "P", "mid": 9.0},
        {"expiry": front, "strike": 95.0, "right": "C", "mid": 7.0},
        {"expiry": front, "strike": 95.0, "right": "P", "mid": 2.0},
        {"expiry": front, "strike": 100.0, "right": "C", "mid": 4.0},
        {"expiry": front, "strike": 100.0, "right": "P", "mid": 3.5},
        {"expiry": front, "strike": 105.0, "right": "P", "mid": 8.0},
    ], 101.0)
    kw.setdefault("chain", df)
    kw.setdefault("chain_meta", {"source": "cboe_chain", "date": D.isoformat()})
    kw.setdefault("screener", {"close": 101.0, "iv30d": 0.40})
    return inputs(**kw), front, early


def test_straddle_front_marks_the_atm_pair_at_the_first_expiry_with_seven_calendar_dte():
    ins, front, _ = straddle_inputs()

    out = R.evaluate(ins, NAME_PARAMS)

    assert out["straddle_front"]["expiry"] == front.isoformat()   # the 3-DTE expiry is skipped
    assert out["straddle_front"]["strike"] == 100.0               # nearest screener close 101
    assert out["straddle_front"]["mark"] == pytest.approx(7.5)    # 4.0 + 3.5, both legs quoted
    assert out["straddle_front"]["mark_source"] == f"cboe_chain {D.isoformat()}"
    assert out["straddle_front"]["tier"] is None
    assert out["box_1s_front"] == pytest.approx(7.5)


def test_straddle_front_uses_the_expiry_r2_already_chose_when_events_is_given():
    ins, front, early = straddle_inputs()

    out = R.evaluate(ins, NAME_PARAMS, {"expiries": [front.isoformat(), (front + timedelta(days=7)).isoformat()]})

    assert out["straddle_front"]["expiry"] == front.isoformat()
    assert out["source"]["straddle_front"].endswith(D.isoformat())


def contract_row(option_type: str, strike: float, expiry: date, vwap: float, size: int) -> dict:
    return {"underlying_symbol": "X", "option_type": option_type, "strike": strike, "expiry": expiry,
            "date": D, "dte_cal": (expiry - D).days, "vwap_late": vwap, "size_late": size,
            "late_rel_spread": 0.02, "late_last_bid": vwap - 0.05, "late_last_ask": vwap + 0.05,
            "last_nbbo_bid": vwap - 0.05, "last_nbbo_ask": vwap + 0.05}


def test_straddle_front_falls_back_to_the_daily_contract_late_mark_when_the_chain_is_stale():
    front = D + timedelta(days=7)
    rows = pd.DataFrame([contract_row("call", 100.0, front, 4.0, 10),
                         contract_row("put", 100.0, front, 3.5, 10),
                         contract_row("call", 130.0, front, 0.1, 10)])
    ins = inputs(contracts_today=rows, screener={"close": 101.0, "iv30d": 0.40},
                 chain_meta={"source": "cboe_chain", "date": "2026-09-17"})

    out = R.evaluate(ins, NAME_PARAMS)

    assert out["straddle_front"]["strike"] == 100.0
    assert out["straddle_front"]["mark"] == pytest.approx(7.5)
    assert out["straddle_front"]["tier"] == 1
    assert out["straddle_front"]["mark_source"] == "daily_contract tier 1"
    assert out["box_1s_front"] == pytest.approx(7.5)


def test_straddle_front_is_null_with_a_reason_when_neither_source_prices_the_pair():
    ins = inputs(screener={"close": 101.0, "iv30d": 0.40})

    out = R.evaluate(ins, NAME_PARAMS)

    assert out["straddle_front"] is None and out["box_1s_front"] is None
    assert any(n["field"] == "straddle_front" for n in out["nulls"])


# ---- the two boxes and ATR ---------------------------------------------------------------------

def test_box_1s_21_is_sigma_hold_over_thirty_calendar_days():
    out = R.evaluate(inputs(screener={"close": 200.0, "iv30d": 0.32}), NAME_PARAMS)

    assert out["box_1s_21"] == pytest.approx(sc_filters.sigma_hold(200.0, 0.32, 30))
    assert out["box_1s_21"] == pytest.approx(200.0 * 0.32 * math.sqrt(30 / 365))
    assert out["source"]["box_1s_21"].startswith("screener")


def test_atr14_is_the_last_wilder_value_on_or_before_the_sheet_date():
    frame = bars(16, start=date(2026, 8, 1))
    frame.loc[15, ["high", "low"]] = [101.5, 99.5]               # the 15th true range is 2.0
    frame.loc[:, "date"] = [date(2026, 8, 1) + timedelta(days=i) for i in range(16)]
    later = frame.iloc[[15]].assign(date=[D + timedelta(days=1)], high=[900.0], low=[0.0])
    ins = inputs(bars=pd.concat([frame, later], ignore_index=True))

    out = R.evaluate(ins, NAME_PARAMS)

    assert out["atr14"] == pytest.approx(15 / 14)                # (1.0 x 13 + 2.0) / 14
    assert out["source"]["atr14"].endswith(date(2026, 8, 16).isoformat())


def test_atr14_is_null_under_fifteen_bars():
    out = R.evaluate(inputs(bars=bars(10)), NAME_PARAMS)

    assert out["atr14"] is None
    assert any(n["field"] == "atr14" for n in out["nulls"])


# ---- the all-null sheet and the schema ---------------------------------------------------------

def test_an_empty_name_inputs_yields_every_null_and_still_validates():
    out = R.evaluate(inputs(), NAME_PARAMS)

    assert out["straddle_front"] is None and out["box_1s_front"] is None
    assert out["box_1s_21"] is None and out["atr14"] is None
    assert out["gex_sign"] is None and out["zero_gamma"] is None
    assert {n["field"] for n in out["nulls"]} >= {"straddle_front", "box_1s_21", "atr14", "gex_total"}
    assert_valid(out)


def test_evaluate_does_not_mutate_the_chain_it_reads():
    df = gex_chain({60.0: -2.0, 70.0: 3.0}, 220.0)
    before = df.copy()

    R.evaluate(inputs(chain=df, chain_meta={"source": "cboe_chain", "date": D.isoformat()}), NAME_PARAMS)

    pd.testing.assert_frame_equal(df, before)


# ---- the three stored fixtures -----------------------------------------------------------------

@pytest.mark.parametrize("ticker", name_fixtures.FIXTURE_TICKERS)
def test_every_fixture_range_section_validates_and_names_its_sources(ticker):
    out = R.evaluate(name_fixtures.load_fixture(ticker), NAME_PARAMS)

    assert_valid(out)
    assert out["box_1s_21"] is not None and out["atr14"] is not None
    assert out["source"]["gex_total"].startswith("cboe_chain 2026-09-18")
    assert json.loads(json.dumps(out)) == out                    # strict JSON, no numpy, no NaN


def test_nvda_gex_and_zero_gamma_come_from_the_stored_chain():
    out = R.evaluate(name_fixtures.load_fixture("NVDA"), NAME_PARAMS)

    assert out["gex_sign"] in ("+", "-") and out["gex_total"] is not None
    assert out["straddle_front"]["expiry"] == "2026-09-25"       # the 3- and 5-DTE expiries are skipped
    assert out["straddle_front"]["mark_source"] == "cboe_chain 2026-09-18"
    if out["zero_gamma"] is not None:                            # a crossing is a fact of the chain
        assert out["zero_gamma"] in out["zero_gamma_all_crossings"]
        nearest = min(out["zero_gamma_all_crossings"], key=lambda k: abs(k - out["spot"]))
        assert out["zero_gamma"] == nearest
