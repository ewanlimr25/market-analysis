"""engine.research.intraday_flow: event selection SQL, labeling, and the per-day DuckDB build
(G2, RESEARCH/47-edge-gaps.md §2). Unit tests exercise the pure labeling functions on synthetic
frames; integration tests run `build_day` against a synthetic parquet panel written to tmp_path
(same pattern as tests/test_daily_contract.py). No test writes under ~/Documents/Stocks.
"""
from __future__ import annotations

import os
from datetime import date, datetime, timedelta, timezone

import duckdb
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import pytest

from engine import config
from engine.research import intraday_flow as ifl

pytestmark = pytest.mark.unit

D = date(2026, 7, 29)
ET_OFFSET_HOURS = 4  # EDT


def et(hh: int, mm: int, ss: int = 0, d: date = D) -> datetime:
    naive = datetime(d.year, d.month, d.day, hh, mm, ss)
    return (naive + timedelta(hours=ET_OFFSET_HOURS)).replace(tzinfo=timezone.utc)


# ----------------------------------------------------------------------------- label_direction


def test_label_direction_call_ask_and_put_bid_are_bullish():
    ot = pd.Series(["call", "put", "put", "call", "call", "put"])
    side = pd.Series(["ask", "bid", "ask", "bid", "mid", "no_side"])
    got = ifl.label_direction(ot, side)
    assert list(got) == ["bullish", "bullish", "bearish", "bearish", "excluded", "excluded"]


# ----------------------------------------------------------------------------- bucket labels


def _norm(values) -> list:
    """None and NaN both mean "no bucket"; normalize for a plain list comparison."""
    return [None if pd.isna(v) else v for v in values]


def test_label_size_bucket_boundaries():
    premium = pd.Series([250_000.0, 999_999.0, 1_000_000.0, 5_000_000.0, 249_999.0])
    got = ifl.label_size_bucket(premium)
    assert _norm(got) == ["250k_1m", "250k_1m", "gte_1m", "gte_1m", None]


def test_label_dte_bucket_boundaries():
    dte = pd.Series([0, 7, 8, 30, 31, -1])
    got = ifl.label_dte_bucket(dte)
    assert _norm(got) == ["0_7", "0_7", "8_30", "8_30", None, None]


def test_label_tod_bucket_boundaries_and_gaps():
    # label_tod_bucket takes wall-clock ET timestamps (already `AT TIME ZONE`-converted upstream),
    # so the fixture here is naive local time, not the UTC `et()` helper used for raw prints.
    wall = lambda hh, mm, ss=0: pd.Timestamp(datetime(D.year, D.month, D.day, hh, mm, ss))
    times = pd.Series([wall(9, 35), wall(10, 59, 59), wall(11, 0), wall(13, 59, 59), wall(14, 0),
                       wall(15, 30), wall(9, 34, 59), wall(15, 30, 1)])
    got = ifl.label_tod_bucket(times)
    assert _norm(got) == ["09:35-11:00", "09:35-11:00", "11:00-14:00", "11:00-14:00",
                          "14:00-15:30", "14:00-15:30", None, None]


# ----------------------------------------------------------------------------- OI classification


def test_classify_oi_join_opening_closing_mixed():
    oi = pd.Series([50.0, -50.0, 10.0, None, -49.0])
    size = pd.Series([50, 50, 50, 50, 50])
    got = ifl.classify_oi_join(oi, size)
    assert list(got) == ["OPENING", "CLOSING", "MIXED", "MIXED", "MIXED"]


def test_label_opening_proxy_volume_crosses_oi():
    volume = pd.Series([10, 100, 100])
    oi = pd.Series([100, 100, 99])
    got = ifl.label_opening_proxy(volume, oi)
    assert list(got) == [False, True, True]


def test_label_events_without_oi_frame_is_all_mixed():
    df = pd.DataFrame({
        "option_type": ["call"], "side": ["ask"], "premium": [300_000.0], "dte_cal": [3],
        "et": [pd.Timestamp(et(10, 0))], "option_chain_id": ["X"], "size": [10],
        "volume": [5], "open_interest": [100],
    })
    out = ifl.label_events(df, oi=None)
    assert out["classification_oi"].tolist() == ["MIXED"]
    assert out["oi_row_found"].tolist() == [False]
    assert out["direction"].tolist() == ["bullish"]
    assert out["size_bucket"].tolist() == ["250k_1m"]
    assert out["dte_bucket"].tolist() == ["0_7"]


def test_label_events_joins_oi_frame_on_option_chain_id():
    df = pd.DataFrame({
        "option_type": ["put"], "side": ["ask"], "premium": [2_000_000.0], "dte_cal": [20],
        "et": [pd.Timestamp(et(12, 0))], "option_chain_id": ["X"], "size": [40],
        "volume": [5], "open_interest": [1000],
    })
    oi = pd.DataFrame({"option_symbol": ["X"], "oi_diff_plain": [45]})
    out = ifl.label_events(df, oi=oi)
    assert out["classification_oi"].tolist() == ["OPENING"]
    assert out["oi_row_found"].tolist() == [True]
    assert out["direction"].tolist() == ["bearish"]
    assert out["size_bucket"].tolist() == ["gte_1m"]
    assert out["dte_bucket"].tolist() == ["8_30"]


# ----------------------------------------------------------------------------- integration


ALL_OPTIONS_SCHEMA = pa.schema([
    ("executed_at", pa.timestamp("us", tz="UTC")), ("underlying_symbol", pa.string()),
    ("option_chain_id", pa.string()), ("side", pa.string()), ("strike", pa.float64()),
    ("option_type", pa.string()), ("expiry", pa.date32()), ("underlying_price", pa.float64()),
    ("nbbo_bid", pa.float64()), ("nbbo_ask", pa.float64()), ("ewma_nbbo_bid", pa.float64()),
    ("ewma_nbbo_ask", pa.float64()), ("price", pa.float64()), ("size", pa.int64()),
    ("premium", pa.float64()), ("volume", pa.int64()), ("open_interest", pa.int64()),
    ("implied_volatility", pa.float64()), ("delta", pa.float64()), ("theta", pa.float64()),
    ("gamma", pa.float64()), ("vega", pa.float64()), ("rho", pa.float64()), ("theo", pa.float64()),
    ("sector", pa.string()), ("exchange", pa.string()), ("report_flags", pa.string()),
    ("canceled", pa.bool_()), ("upstream_condition_detail", pa.string()), ("equity_type", pa.string()),
])
OI_CHANGES_SCHEMA = pa.schema([
    ("oi_diff_plain", pa.int64()), ("option_symbol", pa.string()), ("underlying_symbol", pa.string()),
    ("strike", pa.float64()), ("last_oi", pa.int64()), ("curr_oi", pa.int64()), ("volume", pa.int64()),
    ("last_date", pa.date32()), ("curr_date", pa.date32()), ("oi_change", pa.float64()),
    ("rnk", pa.int64()), ("last_fill", pa.float64()), ("last_ask", pa.float64()),
    ("last_bid", pa.float64()), ("percentage_of_total", pa.float64()),
    ("prev_total_premium", pa.float64()), ("prev_neutral_volume", pa.int64()),
    ("prev_mid_volume", pa.int64()), ("prev_bid_volume", pa.int64()), ("prev_ask_volume", pa.int64()),
    ("prev_stock_multi_leg_volume", pa.int64()), ("prev_multi_leg_volume", pa.int64()),
    ("trades", pa.int64()), ("avg_price", pa.float64()), ("curr_vol", pa.int64()),
    ("prev_vol", pa.int64()), ("next_earnings_date", pa.date32()), ("er_time", pa.string()),
    ("sector", pa.string()), ("stock_price", pa.float64()), ("dte", pa.int64()),
])

BIG = "AAA260821C00100000"   # DTE well within range from D


def make_print(ts: datetime, cid: str, price: float, size: int, side: str, underlying_price: float,
               code: str = "auto", volume: int | None = None, open_interest: int = 1000) -> dict:
    return {
        "executed_at": ts, "underlying_symbol": cid[:3], "option_chain_id": cid, "side": side,
        "strike": 100.0, "option_type": "call" if cid[9] == "C" else "put",
        "expiry": date(2026, 8, 21), "underlying_price": underlying_price,
        "nbbo_bid": price - 0.05, "nbbo_ask": price + 0.05,
        "ewma_nbbo_bid": price - 0.05, "ewma_nbbo_ask": price + 0.05,
        "price": price, "size": size, "premium": price * size * 100.0,
        "volume": volume if volume is not None else size, "open_interest": open_interest,
        "implied_volatility": 0.3, "delta": 0.5, "theta": -0.01, "gamma": 0.01, "vega": 0.1,
        "rho": 0.01, "theo": price, "sector": "Technology", "exchange": "XCBO",
        "report_flags": "{}", "canceled": False, "upstream_condition_detail": code,
        "equity_type": "Common Stock",
    }


def write_all_options(path: str, rows: list[dict]) -> None:
    table = pa.Table.from_pylist(rows, schema=ALL_OPTIONS_SCHEMA)
    pq.write_table(table, path)


@pytest.fixture
def synthetic_panel(tmp_path, monkeypatch):
    stocks = tmp_path / "Stocks"
    (stocks / "All Options").mkdir(parents=True)
    (stocks / "OI changes").mkdir(parents=True)
    monkeypatch.setattr(config, "STOCKS", str(stocks))

    # 150 background prints on AAA to clear the >=100 distinct underlying_price liquidity floor,
    # spread across the session so the 5-minute path has several buckets.
    background = []
    for i in range(150):
        minute = 30 + (i % 300)
        hh, mm = 9 + minute // 60, minute % 60
        background.append(make_print(et(hh, mm, i % 60), "AAA260821P00090000", 1.0, 1, "bid",
                                      100.0 + 0.01 * i, code="slan", open_interest=500))
    events = [
        # qualifying bullish OPENING event at 10:00: premium 25*110*100=$275,000 (>=$250k floor),
        # D+1 OI diff +110 (>= this print's size) => OPENING
        make_print(et(10, 0), BIG, 25.0, 110, "ask", 100.0, code="auto", open_interest=500),
        # qualifying bearish event (put at ask) at 12:30, single-leg isoi sweep
        make_print(et(12, 30), "AAA260821P00100000", 30.0, 90, "ask", 101.0, code="isoi",
                   open_interest=500),
        # below the premium floor -> excluded from events
        make_print(et(10, 5), "AAA260821C00110000", 1.0, 10, "ask", 100.0, code="auto"),
        # multi-leg code -> excluded from events even though premium qualifies
        make_print(et(10, 10), "AAA260821C00120000", 30.0, 100, "ask", 100.0, code="mlet"),
        # outside the 09:35-15:30 window -> excluded
        make_print(et(9, 30), "AAA260821C00130000", 30.0, 100, "ask", 100.0, code="auto"),
    ]
    write_all_options(str(stocks / "All Options" / f"bot-eod-report-{D.isoformat()}.parquet"),
                      background + events)

    d1 = date(2026, 7, 30)
    oi_row = {**{f.name: None for f in OI_CHANGES_SCHEMA}, "option_symbol": BIG, "oi_diff_plain": 110,
             "underlying_symbol": "AAA", "last_oi": 390, "curr_oi": 500, "volume": 110,
             "last_date": D, "curr_date": d1, "oi_change": 0.282}
    table = pa.Table.from_pylist([oi_row], schema=OI_CHANGES_SCHEMA)
    pq.write_table(table, str(stocks / "OI changes" / f"chain-oi-changes-{d1.isoformat()}.parquet"))
    return stocks


@pytest.mark.integration
def test_build_day_selects_only_qualifying_single_leg_events(synthetic_panel):
    build = ifl.build_day(duckdb.connect(), D)
    assert build.date == D
    assert set(build.events["option_chain_id"]) == {BIG, "AAA260821P00100000"}
    assert (build.events["date"] == D).all()


@pytest.mark.integration
def test_build_day_classifies_the_opening_print_via_the_d_plus_1_oi_file(synthetic_panel):
    build = ifl.build_day(duckdb.connect(), D)
    row = build.events.set_index("option_chain_id").loc[BIG]
    assert row["classification_oi"] == "OPENING"
    assert row["direction"] == "bullish"
    assert row["oi_row_found"]


@pytest.mark.integration
def test_build_day_path_covers_the_liquid_underlying_only(synthetic_panel):
    build = ifl.build_day(duckdb.connect(), D)
    assert set(build.path["underlying_symbol"]) == {"AAA"}
    assert build.n_raw_prints >= 150


@pytest.mark.integration
def test_build_day_raises_when_the_all_options_file_is_missing(synthetic_panel):
    with pytest.raises(FileNotFoundError, match="2026-08-03"):
        ifl.build_day(duckdb.connect(), date(2026, 8, 3))
