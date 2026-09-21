"""engine.name.flags (R3, findings/stock-deep-dive DESIGN/70 §4 X2/X5, §7 `flags`, §8 line E).

Synthetic bars whose beta is exact by construction, the X2/X5 on/off/null cases, and the three
stored fixtures. No network, no panel.
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
from engine.name import flags as F

pytestmark = pytest.mark.unit

D = date(2026, 9, 18)
SCHEMA = json.load(open(os.path.join(config.REPO, "schemas", "ticker.schema.json"), encoding="utf-8"))


def assert_valid(section: dict, name: str = "flags") -> None:
    assert schema.validate(section, {"$ref": f"#/$defs/{name}", "$defs": SCHEMA["$defs"]}) == []


def inputs(**kw):
    from engine.name.data import NameInputs
    return NameInputs(ticker=kw.pop("ticker", "X"), date=kw.pop("date", D), **kw)


def log_bars(n: int, mult: float, *, skip: int = 0) -> pd.DataFrame:
    """`n` sessions whose log returns are `mult x` a fixed non-constant sequence, so the OLS slope
    of a `mult = 2` series on a `mult = 1` series is exactly 2. `skip` drops every k-th session."""
    rets = [0.01 if i % 3 else -0.012 for i in range(n - 1)]
    closes, days = [100.0], [date(2025, 1, 6)]
    for i, r in enumerate(rets):
        closes.append(closes[-1] * math.exp(mult * r))
        days.append(days[-1] + timedelta(days=1))
    frame = pd.DataFrame({"date": days, "open": closes, "high": closes, "low": closes,
                          "close": closes, "adj": closes, "volume": [1e6] * n})
    return frame if not skip else frame[[i % skip != 0 for i in range(n)]].reset_index(drop=True)


BORROW = {"fee_rate": 0.25, "available_shares": 10_000_000.0, "asof": "2026-09-18",
          "decile": 0.118, "stale_days": 0, "rebate_rate": 3.63}
SI = {"current_short_position": 298_301_619.0, "days_to_cover": 2.14, "short_float": 0.0129,
      "settlement_date": "2026-08-31", "publication_date": "2026-09-14"}
IVOL = {"date": "2026-09-18", "vix": 14.81, "vix3m": 18.24, "vxn": 19.29, "vix9d": 12.27}
REGIME = {"label": "CHOP", "asof": "2026-09-04", "stale": True}


# ---- the rows ----------------------------------------------------------------------------------

def test_borrow_and_short_interest_rows_carry_their_own_dates():
    out = F.evaluate(inputs(borrow=BORROW, short_interest=SI), NAME_PARAMS)

    assert out["borrow"] == {"fee": 0.25, "available": 10_000_000.0, "date": "2026-09-18",
                             "decile": 0.118, "stale_days": 0}
    assert out["si"] == {"pct_float": 0.0129, "dtc": 2.14, "settlement": "2026-08-31",
                         "publication": "2026-09-14", "position": 298_301_619.0}
    assert out["source"]["borrow"].endswith("2026-09-18")
    assert "2026-08-31" in out["source"]["si"] and "2026-09-14" in out["source"]["si"]


def test_a_null_borrow_row_says_why_and_fires_nothing():
    out = F.evaluate(inputs(nulls=[{"field": "borrow", "reason": "IBKR file stale by 9 days"}]),
                     NAME_PARAMS)

    assert out["borrow"] is None and out["x2"] is False
    reasons = {n["field"]: n["reason"] for n in out["nulls"]}
    assert reasons["borrow"] == "IBKR file stale by 9 days"
    assert "x2" in reasons                      # X2 cannot fire on missing data, and says so


def test_vix_term_is_contango_when_the_three_month_is_above_the_spot_index():
    out = F.evaluate(inputs(index_vol=IVOL), NAME_PARAMS)

    assert out["vix"] == {"vix": 14.81, "vix3m": 18.24, "vxn": 19.29, "term": "contango",
                          "date": "2026-09-18"}


def test_vix_term_is_backwardation_when_the_three_month_is_below():
    out = F.evaluate(inputs(index_vol={**IVOL, "vix3m": 12.0}), NAME_PARAMS)

    assert out["vix"]["term"] == "backwardation"


def test_regime_carries_its_label_asof_and_staleness():
    out = F.evaluate(inputs(regime=REGIME), NAME_PARAMS)

    assert out["regime"] == "CHOP" and out["regime_asof"] == "2026-09-04"
    assert out["regime_stale"] is True and out["source"]["regime"].endswith("2026-09-04")


def test_form4_counts_purchases_and_sales_by_finnhub_code():
    rows = [{"code": "P", "shares": 100.0, "date": "2026-09-02"},
            {"code": "S", "shares": -80.0, "date": "2026-09-03"},
            {"code": "S", "shares": -20.0, "date": "2026-09-04"},
            {"code": "M", "shares": -500.0, "date": "2026-09-05"}]

    out = F.evaluate(inputs(form4=rows), NAME_PARAMS)

    assert out["form4"]["buys"] == 1 and out["form4"]["sells"] == 2 and out["form4"]["other"] == 1
    assert out["form4"]["rows"] == rows


def test_analyst_changes_pass_through_with_their_count():
    rows = [{"date": "2026-09-04", "firm": "Needham", "from": "Buy", "to": "Buy", "action": "reit"}]

    out = F.evaluate(inputs(analyst=rows), NAME_PARAMS)

    assert out["analyst"] == rows and out["analyst_n"] == 1


# ---- beta ---------------------------------------------------------------------------------------

def test_beta_250_is_the_ols_slope_of_log_returns_on_spy():
    out = F.evaluate(inputs(bars=log_bars(251, 2.0), spy_bars=log_bars(251, 1.0)), NAME_PARAMS)

    assert out["beta_250"] == pytest.approx(2.0)
    assert out["source"]["beta_250"].endswith("2025-09-13")      # the last common session


def test_beta_250_is_null_under_the_minimum_session_count():
    out = F.evaluate(inputs(bars=log_bars(100, 2.0), spy_bars=log_bars(100, 1.0)), NAME_PARAMS)

    assert out["beta_250"] is None
    assert any(n["field"] == "beta_250" for n in out["nulls"])


def test_beta_250_uses_only_sessions_both_series_have():
    thin = log_bars(251, 2.0, skip=2)            # the name is quoted on half the sessions SPY is
    out = F.evaluate(inputs(bars=thin, spy_bars=log_bars(251, 1.0)), NAME_PARAMS)

    # 125 common sessions -> 124 returns, over the merged dates on both sides, so the slope is
    # still exactly 2: returns are taken after the join, never before it.
    assert out["beta_250"] == pytest.approx(2.0)
    assert out["beta_n"] == 124


def test_beta_250_is_null_without_bars():
    out = F.evaluate(inputs(), NAME_PARAMS)

    assert out["beta_250"] is None
    assert any(n["field"] == "beta_250" for n in out["nulls"])


# ---- X2 and X5 (DESIGN/70 §4) --------------------------------------------------------------------

def test_x2_fires_when_the_borrow_fee_is_in_the_top_decile():
    out = F.evaluate(inputs(borrow={**BORROW, "decile": NAME_PARAMS.x2_borrow_decile}), NAME_PARAMS)

    assert out["x2"] is True and out["x2_reason"] == "borrow fee in the top decile of the day"


def test_x2_fires_when_available_shares_are_under_the_floor():
    out = F.evaluate(inputs(borrow={**BORROW, "available_shares": 99_999.0}), NAME_PARAMS)

    assert out["x2"] is True and "available" in out["x2_reason"]


def test_x2_is_false_on_a_deep_cheap_borrow():
    out = F.evaluate(inputs(borrow=BORROW), NAME_PARAMS)

    assert out["x2"] is False and out["x2_reason"] is None


def test_x5_fires_at_the_short_float_threshold_and_not_below():
    high = F.evaluate(inputs(short_interest={**SI, "short_float": NAME_PARAMS.x5_short_float_min}), NAME_PARAMS)
    low = F.evaluate(inputs(short_interest={**SI, "short_float": 0.2499}), NAME_PARAMS)

    assert high["x5"] is True and low["x5"] is False


def test_x5_is_false_and_recorded_when_short_float_is_null():
    out = F.evaluate(inputs(short_interest={**SI, "short_float": None}), NAME_PARAMS)

    assert out["x5"] is False
    assert any(n["field"] == "x5" for n in out["nulls"])
    assert out["si"]["pct_float"] is None


# ---- the all-null sheet, the schema and the fixtures ----------------------------------------------

def test_an_empty_name_inputs_yields_every_null_and_still_validates():
    out = F.evaluate(inputs(), NAME_PARAMS)

    assert out["borrow"] is None and out["si"] is None and out["vix"] is None
    assert out["regime"] is None and out["beta_250"] is None
    assert out["analyst"] == [] and out["form4"] == {"buys": 0, "sells": 0, "other": 0, "rows": []}
    assert out["x2"] is False and out["x5"] is False
    assert {n["field"] for n in out["nulls"]} >= {"borrow", "si", "vix", "regime", "beta_250", "x2", "x5"}
    assert_valid(out)


@pytest.mark.parametrize("ticker", name_fixtures.FIXTURE_TICKERS)
def test_every_fixture_flag_carries_a_date_in_its_source(ticker):
    out = F.evaluate(name_fixtures.load_fixture(ticker), NAME_PARAMS)

    assert_valid(out)
    for flag in ("borrow", "si", "beta_250", "analyst", "form4", "vix", "regime"):
        assert any(ch.isdigit() for ch in out["source"][flag]), flag
    assert json.loads(json.dumps(out)) == out


def test_oklo_short_float_is_under_x5_and_nvda_beta_is_measured():
    oklo = F.evaluate(name_fixtures.load_fixture("OKLO"), NAME_PARAMS)
    nvda = F.evaluate(name_fixtures.load_fixture("NVDA"), NAME_PARAMS)

    assert oklo["si"]["pct_float"] == pytest.approx(0.2047) and oklo["x5"] is False
    assert oklo["x2"] is False                   # decile 0.40, 2.6M shares available
    assert nvda["beta_250"] is not None and nvda["vix"]["term"] == "contango"
