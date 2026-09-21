"""engine.name.data / data_sources (R1, findings/stock-deep-dive DESIGN/70 §1, §10).

Every unit test here runs on synthetic frames and injected getters: no network, no panel
(`~/Documents/Stocks`), no mart. The one test that reads the real marts carries
`@pytest.mark.integration` and is deselected by `make test`.
"""
from __future__ import annotations

import json
import os
from datetime import date, datetime, timezone

import pandas as pd
import pytest

import name_fixtures
from engine.mart import cboe_chain
from engine.name import data as D
from engine.name import data_sources as S
from engine.mart import store
from engine.strategies import sc_data

# This file mixes unit and integration tests, so each test carries its own marker
# (the convention of tests/test_earnings_events.py): `make test` is `pytest -m unit`.


# --------------------------------------------------------------------------------------------
# contract_sessions: the pure per-session aggregation (DESIGN/70 §1 row 1, L3/L4 inputs)
# --------------------------------------------------------------------------------------------

def _contract_rows() -> pd.DataFrame:
    d1, d2 = date(2026, 9, 17), date(2026, 9, 18)
    return pd.DataFrame({
        "date": [d1, d1, d1, d2, d2],
        "hc_volume": [250.0, None, 0.0, 300.0, 400.0],
        "n_prints": [10, 4, 1, 20, 6],
        "premium_total": [1000.0, 40.0, 5.0, 2000.0, 600.0],
    })


@pytest.mark.unit
def test_contract_sessions_counts_contracts_and_hot_chain_rows_per_session():
    out = D.contract_sessions(_contract_rows())

    assert list(out.columns) == list(D.CONTRACT_SESSION_COLUMNS)
    assert out["date"].tolist() == [date(2026, 9, 17), date(2026, 9, 18)]
    assert out["n_contracts"].tolist() == [3, 2]
    assert out["n_hot"].tolist() == [1, 2]                 # null and 0 hc_volume are not hot
    assert out["n_prints"].tolist() == [15, 26]
    assert out["premium_total"].tolist() == [1045.0, 2600.0]


@pytest.mark.unit
def test_contract_sessions_does_not_mutate_its_input():
    rows = _contract_rows()
    before = rows.copy()
    D.contract_sessions(rows)
    pd.testing.assert_frame_equal(rows, before)


@pytest.mark.unit
def test_contract_sessions_on_an_empty_frame_is_the_empty_schema():
    out = D.contract_sessions(pd.DataFrame())
    assert out.empty and list(out.columns) == list(D.CONTRACT_SESSION_COLUMNS)


# --------------------------------------------------------------------------------------------
# FOMC window (DESIGN/70 §1 `events.macro`)
# --------------------------------------------------------------------------------------------

@pytest.mark.unit
def test_fomc_dates_are_the_published_2026_2027_calendar():
    y26 = [x for x in D.FOMC_DATES if x.year == 2026]
    y27 = [x for x in D.FOMC_DATES if x.year == 2027]
    assert len(y26) == 8 and len(y27) == 8
    assert y26[0] == date(2026, 1, 28) and y26[-1] == date(2026, 12, 9)
    assert y27[0] == date(2027, 1, 27) and y27[-1] == date(2027, 12, 8)
    assert list(D.FOMC_DATES) == sorted(D.FOMC_DATES)


@pytest.mark.unit
def test_fomc_window_lists_only_decisions_inside_the_next_45_days():
    assert D.fomc_window(date(2026, 9, 18)) == ["2026-10-28"]
    assert D.fomc_window(date(2026, 9, 18), days=10) == []
    assert D.fomc_window(date(2026, 10, 28)) == ["2026-10-28", "2026-12-09"]   # today counts
    assert D.fomc_window(date(2026, 10, 29)) == ["2026-12-09"]


# --------------------------------------------------------------------------------------------
# yfinance chain normaliser (DESIGN/70 §1 "Live chain", fallback row)
# --------------------------------------------------------------------------------------------

def _yf_leg(right: str) -> pd.DataFrame:
    return pd.DataFrame({
        "contractSymbol": [f"ACME260925{right}00050000"],
        "lastTradeDate": [pd.Timestamp("2026-09-18 19:59:59", tz="UTC")],
        "strike": [50.0], "lastPrice": [2.5], "bid": [2.4], "ask": [2.6],
        "volume": [11.0], "openInterest": [222.0], "impliedVolatility": [0.31],
    })


@pytest.mark.unit
def test_normalize_yf_chain_matches_the_cboe_chain_column_set():
    at = datetime(2026, 9, 20, 17, 0, tzinfo=timezone.utc)
    out = S.normalize_yf_chain(_yf_leg("C"), _yf_leg("P"), symbol="ACME",
                               expiry=date(2026, 9, 25), underlying_price=49.5, fetched_at=at)

    assert list(out.columns) == list(cboe_chain.CHAIN_COLUMNS)
    assert len(out) == 2
    assert out["right"].tolist() == ["C", "P"]
    assert out["source"].unique().tolist() == ["yfinance"]
    assert out["expiry"].unique().tolist() == [date(2026, 9, 25)]
    assert out["mid"].tolist() == [2.5, 2.5]
    assert out["underlying_price"].unique().tolist() == [49.5]
    assert out["delta"].isna().all() and out["theo"].isna().all()   # yfinance carries no greeks


@pytest.mark.unit
def test_normalize_yf_chain_on_empty_legs_is_the_empty_chain_schema():
    out = S.normalize_yf_chain(pd.DataFrame(), pd.DataFrame(), symbol="ACME",
                               expiry=date(2026, 9, 25), underlying_price=None,
                               fetched_at=datetime.now(timezone.utc))
    assert out.empty and list(out.columns) == list(cboe_chain.CHAIN_COLUMNS)


# --------------------------------------------------------------------------------------------
# The three-source earnings date (DESIGN/70 §1 "Earnings date"; the sheet prints all three)
# --------------------------------------------------------------------------------------------

@pytest.mark.unit
def test_earnings_dates_carries_all_three_sources_with_date_hour_and_source():
    out = D.earnings_dates(
        screener={"next_earnings_date": date(2026, 11, 18), "er_time": "unknown"},
        finnhub={"available": True, "reason": None, "value": {"date": "2026-11-18", "hour": "amc"}},
        yfinance={"available": True, "reason": None, "value": {"date": "2026-11-17", "hour": None}},
        d=date(2026, 9, 18))

    assert list(out) == ["finnhub", "screener", "yfinance"]
    for name in out:
        assert set(out[name]) == {"date", "hour", "source", "reason"}
    assert out["finnhub"]["date"] == "2026-11-18" and out["finnhub"]["hour"] == "amc"
    assert out["screener"]["date"] == "2026-11-18" and out["screener"]["source"] == "screener 2026-09-18"
    assert out["yfinance"]["date"] == "2026-11-17"                 # disagreement is printed, not resolved


@pytest.mark.unit
def test_earnings_dates_marks_a_failed_or_absent_source_null_with_its_reason():
    out = D.earnings_dates(screener=None,
                           finnhub={"available": False, "reason": "HTTP 429", "value": None},
                           yfinance=S.skipped(), d=date(2026, 9, 18))
    assert out["finnhub"] == {"date": None, "hour": None, "source": S.FINNHUB_CALENDAR, "reason": "HTTP 429"}
    assert out["yfinance"]["date"] is None and out["yfinance"]["reason"] == S.OFFLINE
    assert out["screener"]["date"] is None and out["screener"]["reason"] == "no screener row"


# --------------------------------------------------------------------------------------------
# data_sources: offline skips every network call; every wrapper is fail-soft
# --------------------------------------------------------------------------------------------

@pytest.mark.unit
def test_collect_offline_marks_every_network_field_offline_and_calls_nothing():
    def boom(*a, **k):                                             # any network use is a failure
        raise AssertionError("network touched with online=False")

    out = S.collect("NVDA", date(2026, 9, 18), online=False, key="unused",
                    yf_ticker=boom, finnhub_getter=boom, finviz_runner=boom)

    assert set(out) == set(S.NETWORK_FIELDS)
    for field, res in out.items():
        assert res == {"available": False, "reason": S.OFFLINE, "value": None}, field


@pytest.mark.unit
def test_skipped_is_the_shared_fail_soft_shape():
    assert S.skipped("why") == {"available": False, "reason": "why", "value": None}


@pytest.mark.unit
def test_finnhub_earnings_date_parses_the_calendar_payload():
    payload = {"earningsCalendar": [{"date": "2026-08-26", "hour": "amc"},
                                    {"date": "2026-11-18", "hour": "amc"}]}
    out = S.finnhub_earnings_date("NVDA", date(2026, 9, 18), "KEY",
                                  fetch=lambda **k: {"available": True, "skip_reason": None,
                                                     "rows": payload["earningsCalendar"]})
    assert out["available"] is True
    assert out["value"] == {"date": "2026-11-18", "hour": "amc"}   # the first print on or after `d`


@pytest.mark.unit
def test_finnhub_earnings_date_is_fail_soft_when_the_call_fails():
    out = S.finnhub_earnings_date("NVDA", date(2026, 9, 18), "KEY",
                                  fetch=lambda **k: {"available": False, "skip_reason": "HTTP 429", "rows": []})
    assert out == {"available": False, "reason": "HTTP 429", "value": None}

    def raiser(**k):
        raise RuntimeError("boom")

    assert S.finnhub_earnings_date("NVDA", date(2026, 9, 18), "KEY", fetch=raiser)["available"] is False


@pytest.mark.unit
def test_finnhub_insider_transactions_keeps_the_last_30_calendar_days():
    rows = [{"transactionDate": "2026-09-15", "name": "A", "transactionCode": "S",
             "change": -100, "transactionPrice": 10.0},
            {"transactionDate": "2026-06-01", "name": "B", "transactionCode": "P",
             "change": 50, "transactionPrice": 9.0}]
    out = S.finnhub_insider_transactions("NVDA", date(2026, 9, 18), "KEY",
                                         getter=lambda url: {"data": rows, "symbol": "NVDA"})
    assert out["available"] is True
    assert out["value"] == [{"date": "2026-09-15", "name": "A", "code": "S",
                             "shares": -100.0, "price": 10.0}]


@pytest.mark.unit
def test_finnhub_insider_transactions_without_a_key_is_fail_soft():
    out = S.finnhub_insider_transactions("NVDA", date(2026, 9, 18), None)
    assert out["available"] is False and "FINNHUB_API_KEY" in out["reason"]


class _FakeYf:
    """The two `yfinance.Ticker` attributes R1 reads, plus a switch to make either one raise."""

    def __init__(self, calendar=None, upgrades=None, info=None, raises=False):
        self._calendar, self._upgrades, self._info, self._raises = calendar, upgrades, info, raises

    def _guard(self):
        if self._raises:
            raise RuntimeError("yfinance said no")

    @property
    def calendar(self):
        self._guard()
        return self._calendar

    @property
    def upgrades_downgrades(self):
        self._guard()
        return self._upgrades

    @property
    def info(self):
        self._guard()
        return self._info


@pytest.mark.unit
def test_yf_earnings_date_reads_the_calendar_block():
    fake = _FakeYf(calendar={"Earnings Date": [date(2026, 11, 17)], "Ex-Dividend Date": date(2026, 9, 9)})
    out = S.yf_earnings_date("NVDA", yf_ticker=lambda t: fake)
    assert out["available"] is True and out["value"] == {"date": "2026-11-17", "hour": None}


@pytest.mark.unit
def test_every_yfinance_wrapper_is_fail_soft():
    fake = _FakeYf(raises=True)
    for call in (lambda: S.yf_earnings_date("NVDA", yf_ticker=lambda t: fake),
                 lambda: S.yf_upgrades_downgrades("NVDA", date(2026, 9, 4), date(2026, 9, 18),
                                                  yf_ticker=lambda t: fake),
                 lambda: S.yf_short_percent_of_float("NVDA", yf_ticker=lambda t: fake)):
        out = call()
        assert out["available"] is False and out["value"] is None
        assert "yfinance said no" in out["reason"]


@pytest.mark.unit
def test_yf_upgrades_downgrades_keeps_only_grade_dates_inside_the_window():
    frame = pd.DataFrame({"Firm": ["A", "B"], "ToGrade": ["Buy", "Hold"],
                          "FromGrade": ["Hold", "Buy"], "Action": ["up", "down"]},
                         index=pd.DatetimeIndex([pd.Timestamp("2026-09-15"), pd.Timestamp("2026-08-01")],
                                                name="GradeDate"))
    out = S.yf_upgrades_downgrades("NVDA", date(2026, 9, 4), date(2026, 9, 18),
                                   yf_ticker=lambda t: _FakeYf(upgrades=frame))
    assert out["available"] is True
    assert out["value"] == [{"date": "2026-09-15", "firm": "A", "from": "Hold", "to": "Buy", "action": "up"}]


@pytest.mark.unit
def test_yf_short_percent_of_float_reads_info():
    out = S.yf_short_percent_of_float("NVDA", yf_ticker=lambda t: _FakeYf(info={"shortPercentOfFloat": 0.0129}))
    assert out["value"] == {"short_float": 0.0129, "short_float_source": S.YF_INFO}


@pytest.mark.unit
def test_short_float_prefers_finviz_and_falls_back_to_yfinance():
    fv = {"available": True, "reason": None, "short_float": "1.29%", "short_ratio": "2.29",
          "short_interest": "298.30M"}
    out = S.short_float("NVDA", finviz=lambda t: fv, yf_ticker=lambda t: _FakeYf(info={}))
    assert out["value"] == {"short_float": pytest.approx(0.0129), "short_float_source": S.FINVIZ}

    broken = {"available": False, "reason": "fz regression", "short_float": None}
    out = S.short_float("NVDA", finviz=lambda t: broken,
                        yf_ticker=lambda t: _FakeYf(info={"shortPercentOfFloat": 0.02}))
    assert out["value"] == {"short_float": 0.02, "short_float_source": S.YF_INFO}


# --------------------------------------------------------------------------------------------
# write_inputs / read_inputs: the sheet re-derives offline from this directory (DESIGN/70 §1)
# --------------------------------------------------------------------------------------------

def _frame(**cols) -> pd.DataFrame:
    return pd.DataFrame(cols)


def _synthetic_inputs(chain: pd.DataFrame | None = None) -> D.NameInputs:
    d = date(2026, 9, 18)
    rows = _contract_rows()
    return D.NameInputs(
        ticker="ACME", date=d,
        screener={"ticker": "ACME", "close": 50.0, "iv30d": 0.41, "issue_type": "Common Stock"},
        contracts_today=_frame(option_chain_id=["ACME1"], date=[d], expiry=[date(2026, 10, 16)],
                               strike=[50.0], option_type=["C"], hc_volume=[300.0]),
        contract_sessions=D.contract_sessions(rows),
        rv=_frame(underlying_symbol=["ACME"], date=[d], rv5=[0.0004], quality=[True]),
        bars=_frame(date=[date(2026, 9, 17), d], open=[49.0, 50.0], high=[51.0, 51.5],
                    low=[48.0, 49.5], close=[50.0, 51.0], adj=[50.0, 51.0], volume=[1e6, 2e6]),
        spy_bars=_frame(date=[d], open=[600.0], high=[605.0], low=[599.0], close=[604.0],
                        adj=[604.0], volume=[7e7]),
        screener_history=_frame(date=[d], close=[50.0], iv30d=[0.41], iv_rank=[12.0],
                                bullish_premium=[1e6], bearish_premium=[9e5], total_volume=[1e6],
                                avg30_volume=[9e5], marketcap=[8e9]),
        universe_today=_frame(ticker=["ACME", "ZZZ"], bullish_premium=[1e6, 2e6],
                              bearish_premium=[9e5, 1e6], total_volume=[1e6, 3e6],
                              avg30_volume=[9e5, 2e6], issue_type=["Common Stock", "ETF"],
                              is_index=[False, False]),
        adv_usd_20d=1.2e8,
        earnings_events=_frame(ticker=["ACME"], E=[date(2026, 8, 12)], realized_move=[0.04]),
        earnings_history=_frame(ticker=["ACME"], E=[date(2026, 8, 12)], abs_move_yahoo=[0.041]),
        earnings_dates=D.earnings_dates(screener={"next_earnings_date": date(2026, 11, 5), "er_time": "amc"},
                                        finnhub=S.skipped(), yfinance=S.skipped(), d=d),
        chain=chain,
        chain_meta={"source": None, "date": None, "reason": "offline", "rows": 0},
        borrow={"fee_rate": 0.3, "rebate_rate": 4.5, "available_shares": 5e5,
                "asof": "2026-09-18", "stale_days": 0, "decile": 0.42},
        short_interest={"current_short_position": 1e6, "days_to_cover": 1.2,
                        "settlement_date": "2026-08-31", "publication_date": "2026-09-11",
                        "short_float": 0.03, "short_float_source": S.YF_INFO},
        analyst=[{"date": "2026-09-15", "firm": "A", "from": "Hold", "to": "Buy", "action": "up"}],
        form4=[{"date": "2026-09-02", "name": "B", "code": "S", "shares": -100.0, "price": 51.0}],
        index_vol={"date": "2026-09-18", "vix": 16.2, "vix3m": 18.0, "vxn": 21.0, "vix9d": 15.1},
        regime={"label": "UPTREND", "ret5": 0.01, "ret10": 0.02},
        fomc=D.fomc_window(d),
        nulls=[{"field": "chain", "reason": "offline"}],
        sources={"screener": "screener 2026-09-18", "contracts_today": "daily_contract 2026-09-18"})


def _assert_same(a: D.NameInputs, b: D.NameInputs) -> None:
    for name in D.FRAME_FIELDS:
        fa, fb = getattr(a, name), getattr(b, name)
        if fa is None or fb is None:
            assert fa is None and fb is None, name
            continue
        pd.testing.assert_frame_equal(fa, fb, check_dtype=False, obj=name)
    for name in ("ticker", "date", "nulls", "sources", *D.VALUE_FIELDS):
        assert getattr(a, name) == getattr(b, name), name


@pytest.mark.unit
def test_write_inputs_and_read_inputs_round_trip(tmp_path):
    inputs = _synthetic_inputs(chain=_frame(symbol=["ACME"], expiry=[date(2026, 10, 16)],
                                            strike=[50.0], right=["C"], bid=[2.0], ask=[2.2],
                                            mid=[2.1], source=["cboe_delayed"]))
    written = D.write_inputs(inputs, str(tmp_path))

    assert str(tmp_path / "meta.json") in written and str(tmp_path / "chain.parquet") in written
    _assert_same(inputs, D.read_inputs(str(tmp_path)))


@pytest.mark.unit
def test_write_inputs_omits_the_chain_file_when_there_is_no_chain(tmp_path):
    inputs = _synthetic_inputs(chain=None)
    written = D.write_inputs(inputs, str(tmp_path))
    assert not (tmp_path / "chain.parquet").exists()
    assert all(not p.endswith("chain.parquet") for p in written)
    _assert_same(inputs, D.read_inputs(str(tmp_path)))


@pytest.mark.unit
def test_write_inputs_meta_carries_ticker_date_nulls_and_sources(tmp_path):
    D.write_inputs(_synthetic_inputs(), str(tmp_path))
    meta = json.loads((tmp_path / "meta.json").read_text())
    assert meta["ticker"] == "ACME" and meta["date"] == "2026-09-18"
    assert meta["nulls"] == [{"field": "chain", "reason": "offline"}]
    assert meta["sources"]["screener"] == "screener 2026-09-18"


# --------------------------------------------------------------------------------------------
# Integration: the real marts, offline (DESIGN/70 §10 R1 acceptance)
# --------------------------------------------------------------------------------------------

needs_real_data = pytest.mark.skipif(
    not (os.path.exists(sc_data.screener_path(date(2026, 9, 18)))
         and store.has_partition("daily_contract", date(2026, 9, 18))),
    reason="the screener panel or the daily_contract mart is not on disk")


@pytest.mark.integration
@needs_real_data
def test_load_inputs_offline_reads_nvda_2026_09_18_from_the_marts():
    inputs = D.load_inputs("NVDA", date(2026, 9, 18), online=False)

    assert len(inputs.contracts_today) == 2051            # RESEARCH/20 §6.2
    assert inputs.screener is not None and inputs.screener["ticker"] == "NVDA"
    assert inputs.contract_sessions["date"].iloc[-1] == date(2026, 9, 18)
    assert inputs.chain is not None and inputs.chain_meta["source"] == "cboe_chain"
    assert {n["reason"] for n in inputs.nulls} >= {S.OFFLINE}


# --------------------------------------------------------------------------------------------
# The stored fixtures the rest of the package tests on (tests/name_fixtures.py)
# --------------------------------------------------------------------------------------------

@pytest.mark.unit
@pytest.mark.parametrize("ticker", name_fixtures.FIXTURE_TICKERS)
def test_every_fixture_loads_offline_with_the_shape_r2_expects(ticker):
    inputs = name_fixtures.load_fixture(ticker)

    assert inputs.ticker == ticker and inputs.date == date(2026, 9, 18)
    assert inputs.screener["ticker"] == ticker
    assert inputs.contract_sessions["date"].iloc[-1] == date(2026, 9, 18)
    assert len(inputs.contract_sessions) == 21                 # NAME_PARAMS.hot_chain_window
    assert list(inputs.chain.columns) == list(cboe_chain.CHAIN_COLUMNS)
    assert set(inputs.earnings_dates) == {"finnhub", "screener", "yfinance"}
    assert inputs.nulls == []                                  # all three loaded clean on 2026-09-20
    assert set(inputs.sources) >= set(D.FRAME_FIELDS) | set(D.VALUE_FIELDS) - {"chain_meta"}


@pytest.mark.unit
def test_the_fixtures_span_the_liquidity_floor():
    """BL is the thin name (fails L3 at 300 contracts), NVDA the liquid one (RESEARCH/20 §1.2)."""
    assert len(name_fixtures.load_fixture("NVDA").contracts_today) == 2051
    assert len(name_fixtures.load_fixture("BL").contracts_today) < 300
    assert len(name_fixtures.load_fixture("OKLO").contracts_today) >= 300
