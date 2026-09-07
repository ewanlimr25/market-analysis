"""engine.mart.intraday_rv: the per-(underlying, day) realized-vol bundle (G7,
findings/RESEARCH/47-edge-gaps.md §2 G7).

Unit tests exercise the pure math (`day_level`, `_gk_bucket`, `with_close_to_close`) on synthetic
bucket frames -- no DuckDB, no panel. Integration tests run `aggregate_day` end to end against a
synthetic All Options parquet in tmp_path (same style as `test_daily_contract.py`) and, separately,
against the real panel day 2026-07-29, skipped when the panel is absent.
"""
from __future__ import annotations

import math
import os
from datetime import date, datetime, timedelta, timezone

import duckdb
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import pytest

from engine import config
from engine.mart import intraday_rv as irv
from engine.mart import store

D = date(2026, 7, 29)
ET_OFFSET_HOURS = 4

# Same 30-column vendor schema as tests/test_daily_contract.py, duplicated locally so this file
# has no cross-test import dependency.
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


def et(hh: int, mm: int, ss: int = 0, d: date = D) -> datetime:
    naive = datetime(d.year, d.month, d.day, hh, mm, ss)
    return (naive + timedelta(hours=ET_OFFSET_HOURS)).replace(tzinfo=timezone.utc)


def make_print(ts: datetime, price: float, size: int, cid: str, **over) -> dict:
    row = {
        "executed_at": ts, "underlying_symbol": cid[:3], "option_chain_id": cid, "side": "ask",
        "strike": 100.0, "option_type": "call" if cid[9] == "C" else "put",
        "expiry": date(2026, 7, 31), "underlying_price": 101.0,
        "nbbo_bid": price - 0.05, "nbbo_ask": price + 0.05,
        "ewma_nbbo_bid": price - 0.05, "ewma_nbbo_ask": price + 0.05,
        "price": price, "size": size, "premium": price * size * 100.0, "volume": size,
        "open_interest": 500, "implied_volatility": 0.25, "delta": 0.5, "theta": -0.01,
        "gamma": 0.02, "vega": 0.03, "rho": 0.001, "theo": price, "sector": "Technology",
        "exchange": "CBOE", "report_flags": "", "canceled": False,
        "upstream_condition_detail": "slan", "equity_type": "Common Stock",
    }
    return {**row, **over}


def bucket_row(sym: str, hh: int, mm: int, n: int, lo: float, hi: float, o: float, c: float,
               d: date = D) -> dict:
    ts = datetime(d.year, d.month, d.day, hh, 0) + timedelta(minutes=mm)
    return {"underlying_symbol": sym, "bucket": ts, "n": n, "lo": lo, "hi": hi, "o": o, "c": c}


def buckets_df(rows: list[dict]) -> pd.DataFrame:
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------- unit: _gk_bucket


@pytest.mark.unit
def test_gk_bucket_is_zero_for_a_flat_single_print_bucket():
    assert irv._gk_bucket(100.0, 100.0, 100.0, 100.0) == 0.0


@pytest.mark.unit
def test_gk_bucket_matches_hand_computation():
    o, h, l, c = 100.0, 101.0, 99.0, 100.5
    expected = 0.5 * math.log(h / l) ** 2 - (2 * math.log(2) - 1) * math.log(c / o) ** 2
    assert irv._gk_bucket(o, h, l, c) == pytest.approx(expected)


@pytest.mark.unit
def test_gk_bucket_is_never_negative_for_self_consistent_ohlc():
    # For any O, C in [L, H] (guaranteed by fetch_buckets's construction: lo/hi are the bucket's
    # own min/max, o/c are prices drawn from the same bucket), |ln(C/O)| <= ln(H/L), and the GK
    # coefficients (0.5 vs 2*ln2-1 ~= 0.386) make the formula non-negative by construction. This
    # property test covers the real input space; the floor below covers malformed input.
    cases = [(100.0, 101.0, 99.0, 100.5), (50.0, 50.2, 49.8, 49.9), (10.0, 10.0, 10.0, 10.0),
             (200.0, 205.0, 195.0, 195.5), (5.0, 5.5, 5.0, 5.5)]
    for o, h, l, c in cases:
        assert irv._gk_bucket(o, h, l, c) >= 0.0


@pytest.mark.unit
def test_gk_bucket_floors_negative_contributions_from_inconsistent_input():
    # A malformed bucket (close far outside [low, high], which fetch_buckets's own construction
    # cannot produce) drives the raw GK formula negative; the floor still returns a valid
    # (non-negative) contribution rather than corrupting the day's sum.
    o, h, l, c = 100.0, 100.1, 99.9, 90.0
    raw = 0.5 * math.log(h / l) ** 2 - (2 * math.log(2) - 1) * math.log(c / o) ** 2
    assert raw < 0  # confirms the fixture actually exercises the floor
    assert irv._gk_bucket(o, h, l, c) == 0.0


# ----------------------------------------------------------------------------- unit: day_level


@pytest.mark.unit
def test_day_level_empty_input_has_the_right_shape():
    out = irv.day_level(pd.DataFrame({"underlying_symbol": [], "bucket": [], "n": [], "lo": [],
                                      "hi": [], "o": [], "c": []}))
    assert out.empty
    assert "underlying_symbol" in out.columns and "quality" in out.columns


@pytest.mark.unit
def test_day_level_rv5_zero_for_a_perfectly_flat_price_path():
    rows = [bucket_row("FLAT", 9, 30 + 5 * i, n=1, lo=100.0, hi=100.0, o=100.0, c=100.0)
            for i in range(5)]
    out = irv.day_level(buckets_df(rows)).iloc[0]
    assert out.rv5 == pytest.approx(0.0)
    assert out.parkinson == pytest.approx(0.0)
    assert out.gk == pytest.approx(0.0)
    assert out.open_to_close_ret == pytest.approx(0.0)


@pytest.mark.unit
def test_day_level_rv5_matches_hand_computed_sum_of_squared_log_returns():
    closes = [100.0, 101.0, 100.5, 102.0]
    rows = [bucket_row("X", 9, 30 + 5 * i, n=1, lo=c, hi=c, o=c, c=c)
            for i, c in enumerate(closes)]
    out = irv.day_level(buckets_df(rows)).iloc[0]
    expected = sum(math.log(closes[i] / closes[i - 1]) ** 2 for i in range(1, len(closes)))
    assert out.rv5 == pytest.approx(expected)
    assert out.n_buckets == 4
    assert out.n_obs == 4


@pytest.mark.unit
def test_day_level_parkinson_matches_hand_computed_sum():
    rows = [bucket_row("X", 9, 30, n=1, lo=99.0, hi=101.0, o=100.0, c=100.5),
            bucket_row("X", 9, 35, n=1, lo=100.0, hi=102.0, o=100.5, c=101.0)]
    out = irv.day_level(buckets_df(rows)).iloc[0]
    scale = 1.0 / (4.0 * math.log(2.0))
    expected = scale * (math.log(101.0 / 99.0) ** 2 + math.log(102.0 / 100.0) ** 2)
    assert out.parkinson == pytest.approx(expected)


@pytest.mark.unit
def test_day_level_open_to_close_uses_first_open_and_last_close():
    rows = [bucket_row("X", 9, 30, n=3, lo=99.0, hi=101.0, o=100.0, c=100.5),
            bucket_row("X", 9, 35, n=2, lo=100.0, hi=102.0, o=100.5, c=101.0),
            bucket_row("X", 9, 40, n=1, lo=101.0, hi=101.5, o=101.0, c=101.3)]
    out = irv.day_level(buckets_df(rows)).iloc[0]
    assert out.open_px == pytest.approx(100.0)
    assert out.close_px == pytest.approx(101.3)
    assert out.open_to_close_ret == pytest.approx(math.log(101.3 / 100.0))
    assert out.n_obs == 6


@pytest.mark.unit
def test_quality_false_when_observation_count_is_below_the_floor():
    rows = [bucket_row("X", 9, 30 + 5 * i, n=1, lo=100.0, hi=100.0, o=100.0, c=100.0)
            for i in range(irv.QUALITY_MIN_OBS - 10)]
    out = irv.day_level(buckets_df(rows)).iloc[0]
    assert out.n_obs < irv.QUALITY_MIN_OBS
    assert out.quality is False or out.quality == False  # noqa: E712 (numpy bool)


@pytest.mark.unit
def test_quality_false_when_a_bucket_gap_exceeds_the_limit():
    rows = [bucket_row("X", 9, 30, n=irv.QUALITY_MIN_OBS, lo=100.0, hi=100.0, o=100.0, c=100.0),
            bucket_row("X", 10, 30, n=irv.QUALITY_MIN_OBS, lo=100.0, hi=100.0, o=100.0, c=100.0)]
    out = irv.day_level(buckets_df(rows)).iloc[0]
    assert out.max_gap_minutes == pytest.approx(60.0)
    assert not out.quality


@pytest.mark.unit
def test_quality_true_when_both_thresholds_are_met():
    rows = [bucket_row("X", 9, 30 + 5 * i, n=irv.QUALITY_MIN_OBS, lo=100.0, hi=100.0, o=100.0, c=100.0)
            for i in range(3)]
    out = irv.day_level(buckets_df(rows)).iloc[0]
    assert out.n_obs >= irv.QUALITY_MIN_OBS
    assert out.max_gap_minutes <= irv.QUALITY_MAX_GAP_MINUTES
    assert out.quality


@pytest.mark.unit
def test_quality_false_for_a_single_populated_bucket_no_return_available():
    rows = [bucket_row("X", 9, 30, n=irv.QUALITY_MIN_OBS, lo=100.0, hi=100.0, o=100.0, c=100.0)]
    out = irv.day_level(buckets_df(rows)).iloc[0]
    assert out.n_buckets == 1
    assert not out.quality


@pytest.mark.unit
def test_day_level_handles_multiple_underlyings_independently():
    rows = [bucket_row("A", 9, 30, n=1, lo=10.0, hi=10.0, o=10.0, c=10.0),
            bucket_row("A", 9, 35, n=1, lo=11.0, hi=11.0, o=11.0, c=11.0),
            bucket_row("B", 9, 30, n=1, lo=50.0, hi=50.0, o=50.0, c=50.0)]
    out = irv.day_level(buckets_df(rows))
    assert sorted(out.underlying_symbol) == ["A", "B"]
    assert out.set_index("underlying_symbol").loc["B", "n_buckets"] == 1


# ----------------------------------------------------------------------------- unit: close-to-close


@pytest.mark.unit
def test_with_close_to_close_computes_log_return_from_prices_parquet(tmp_path):
    prices = pd.DataFrame({"ticker": ["AAA", "AAA", "BBB"],
                           "date": [date(2026, 7, 28), date(2026, 7, 29), date(2026, 7, 29)],
                           "close": [100.0, 105.0, 50.0]})
    path = str(tmp_path / "prices.parquet")
    prices.to_parquet(path, index=False)
    day = pd.DataFrame({"underlying_symbol": ["AAA", "BBB"]})
    out = irv.with_close_to_close(day, duckdb.connect(), path, date(2026, 7, 29))
    row = out.set_index("underlying_symbol").loc["AAA"]
    assert row.prices_close == pytest.approx(105.0)
    assert row.prices_close_prev == pytest.approx(100.0)
    assert row.close_to_close_ret == pytest.approx(math.log(105.0 / 100.0))
    assert pd.isna(out.set_index("underlying_symbol").loc["BBB", "close_to_close_ret"])


@pytest.mark.unit
def test_with_close_to_close_is_null_when_prior_session_is_missing(tmp_path):
    prices = pd.DataFrame({"ticker": ["AAA"], "date": [date(2026, 7, 29)], "close": [105.0]})
    path = str(tmp_path / "prices.parquet")
    prices.to_parquet(path, index=False)
    day = pd.DataFrame({"underlying_symbol": ["AAA"]})
    out = irv.with_close_to_close(day, duckdb.connect(), path, date(2026, 7, 29))
    assert pd.isna(out.iloc[0].close_to_close_ret)
    assert out.iloc[0].prices_close == pytest.approx(105.0)


# ----------------------------------------------------------------------------- integration: pipeline


def write_all_options(path: str, prints: list[dict]) -> str:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    pq.write_table(pa.Table.from_pylist(prints, schema=ALL_OPTIONS_SCHEMA), path)
    return path


@pytest.mark.unit
def test_aggregate_day_end_to_end_on_a_synthetic_tape(tmp_path):
    prints = [make_print(et(9, 30), 1.00, 10, cid="AAA260731C00100000",
                         **{"underlying_symbol": "AAA", "underlying_price": 100.0}),
              make_print(et(9, 33), 1.05, 10, cid="AAA260731C00100000",
                         **{"underlying_symbol": "AAA", "underlying_price": 101.0}),
              make_print(et(9, 40), 1.10, 10, cid="AAA260731C00100000",
                         **{"underlying_symbol": "AAA", "underlying_price": 102.0})]
    ao = write_all_options(str(tmp_path / "ao.parquet"), prints)
    prices = pd.DataFrame({"ticker": ["AAA", "AAA"],
                           "date": [date(2026, 7, 28), D],
                           "close": [99.0, 102.0]})
    prices_path = str(tmp_path / "prices.parquet")
    prices.to_parquet(prices_path, index=False)

    df = irv.aggregate_day(duckdb.connect(), ao, prices_path, D)
    assert list(df.columns) == list(irv.COLUMNS)
    row = df.iloc[0]
    assert row.underlying_symbol == "AAA"
    assert row.date == D
    assert row.n_obs == 3
    assert row.n_buckets == 2  # 09:30 bucket (2 prints) + 09:40 bucket (1 print)
    assert row.close_to_close_ret == pytest.approx(math.log(102.0 / 99.0))


@pytest.mark.unit
def test_aggregate_day_excludes_canceled_and_zero_size_prints(tmp_path):
    prints = [make_print(et(9, 30), 1.00, 10, cid="AAA260731C00100000",
                         **{"underlying_symbol": "AAA", "underlying_price": 100.0}),
              make_print(et(9, 31), 1.00, 0, cid="AAA260731C00100000",
                         **{"underlying_symbol": "AAA", "underlying_price": 999.0}),
              make_print(et(9, 32), 1.00, 10, cid="AAA260731C00100000",
                         **{"underlying_symbol": "AAA", "underlying_price": 100.5, "canceled": True})]
    ao = write_all_options(str(tmp_path / "ao.parquet"), prints)
    prices_path = str(tmp_path / "prices.parquet")
    pd.DataFrame({"ticker": [], "date": [], "close": []}).to_parquet(prices_path, index=False)
    df = irv.aggregate_day(duckdb.connect(), ao, prices_path, D)
    assert len(df) == 1
    assert df.iloc[0].n_obs == 1
    assert df.iloc[0].high_px == pytest.approx(100.0)


# ----------------------------------------------------------------------------- integration: store


@pytest.mark.unit
def test_build_day_raises_when_the_all_options_file_is_absent(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "STOCKS", str(tmp_path / "empty_stocks"))
    with pytest.raises(FileNotFoundError):
        irv.build_day(date(2099, 1, 1))


@pytest.mark.unit
def test_rebuild_is_fail_soft_one_bad_day_does_not_abort_the_run(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    monkeypatch.setattr(irv.store.config, "MART", str(tmp_path / "mart"))
    ao_dir = tmp_path / "stocks" / "All Options"
    ao_dir.mkdir(parents=True)
    good_day = date(2026, 7, 30)
    write_all_options(str(ao_dir / f"bot-eod-report-{good_day.isoformat()}.parquet"),
                      [make_print(et(9, 30, d=good_day), 1.00, 10, cid="AAA260731C00100000",
                                 **{"underlying_symbol": "AAA", "underlying_price": 100.0})])
    # D (2026-07-29) has no All Options file: build_day for it must fail without aborting the run
    monkeypatch.setattr(config, "STOCKS", str(tmp_path / "stocks"))
    monkeypatch.setattr(config, "PRICES", str(tmp_path / "prices.parquet"))
    pd.DataFrame({"ticker": [], "date": [], "close": []}).to_parquet(config.PRICES, index=False)
    monkeypatch.setattr(irv, "panel_dates", lambda: [D, good_day])

    results = irv.rebuild()
    by_date = {r.date: r for r in results}
    assert by_date[D].error is not None
    assert by_date[good_day].error is None
    assert by_date[good_day].rows == 1


@pytest.mark.unit
def test_build_day_writes_and_reuses_a_partition(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    monkeypatch.setattr(irv.store.config, "MART", str(tmp_path / "mart"))
    ao_dir = tmp_path / "stocks" / "All Options"
    ao_dir.mkdir(parents=True)
    prints = [make_print(et(9, 30), 1.00, 10, cid="AAA260731C00100000",
                         **{"underlying_symbol": "AAA", "underlying_price": 100.0})]
    write_all_options(str(ao_dir / f"bot-eod-report-{D.isoformat()}.parquet"), prints)
    monkeypatch.setattr(config, "STOCKS", str(tmp_path / "stocks"))
    monkeypatch.setattr(config, "PRICES", str(tmp_path / "prices.parquet"))
    pd.DataFrame({"ticker": [], "date": [], "close": []}).to_parquet(config.PRICES, index=False)

    df1 = irv.build_day(D)
    assert store.has_partition(irv.TABLE, D)
    df2 = irv.build_day(D)  # reused, not rebuilt
    pd.testing.assert_frame_equal(df1.reset_index(drop=True), df2.reset_index(drop=True))


# ----------------------------------------------------------------------------- integration: real panel


@pytest.mark.integration
def test_aggregate_day_on_the_real_panel_day():
    ao = os.path.join(config.STOCKS, config.ALL_OPTIONS_FILE.format(d="2026-07-29"))
    if not os.path.exists(ao):
        pytest.skip("panel day 2026-07-29 not present")
    df = irv.aggregate_day(duckdb.connect(), ao, config.PRICES, date(2026, 7, 29))
    assert len(df) > 1000
    spy = df[df.underlying_symbol == "SPY"].iloc[0]
    assert spy.quality
    assert spy.n_obs > 100_000
    # RV5, Parkinson and GK should agree in order of magnitude on a normal SPY day.
    ann = {k: math.sqrt(spy[k] * 252) for k in ("rv5", "parkinson", "gk")}
    assert 0.05 < ann["rv5"] < 0.60
    assert 0.05 < ann["parkinson"] < 0.60
    assert 0.05 < ann["gk"] < 0.60
