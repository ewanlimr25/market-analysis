"""engine.mart.daily_contract: the per-(contract, day) materialized table (DESIGN/70 §1.1, §7.3).

Unit tests run on synthetic All Options / Hot Chains parquet files written into tmp_path with the
vendor's 30-column schema. Integration tests read the real panel day 2026-07-29 and skip when it
is absent. No test writes under ~/Documents/Stocks.
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
from engine.mart import daily_contract as dc
from engine.mart import store

D = date(2026, 7, 29)
D2 = date(2026, 7, 30)
ET_OFFSET_HOURS = 4                    # EDT: ET = UTC - 4h on both synthetic days

EXPECTED_COLUMNS = [
    "option_chain_id", "underlying_symbol", "option_type", "strike", "expiry", "date",
    "dte", "dte_cal", "n_prints", "size_total", "premium_total",
    "vwap_all", "vwap_late", "size_late", "vwap_early", "size_early",
    "last_price", "last_nbbo_bid", "last_nbbo_ask", "last_ts",
    "late_nbbo_mid", "late_rel_spread", "early_nbbo_mid", "early_rel_spread",
    "late_last_bid", "late_last_ask", "early_last_bid", "early_last_ask",
    "iv_vwap", "delta_last", "gamma_last", "vega_last",
    "open_interest", "underlying_last", "hc_close", "hc_iv", "hc_volume",
]

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
assert len(ALL_OPTIONS_SCHEMA) == 30

HOT_CHAINS_SCHEMA = pa.schema([
    ("option_symbol", pa.string()), ("date", pa.date32()), ("volume", pa.int64()),
    ("open_interest", pa.int64()), ("premium", pa.float64()), ("high", pa.float64()),
    ("low", pa.float64()), ("open", pa.float64()), ("close", pa.float64()), ("iv", pa.float64()),
    ("bid", pa.float64()), ("ask", pa.float64()), ("trades", pa.int64()),
    ("avg_price", pa.float64()), ("close_1", pa.float64()),
])

CALL = "AAA260731C00100000"
PUT = "AAA260731P00100000"
OTHER = "BBB260821C00050000"


# ----------------------------------------------------------------------------- synthetic tape


def et(hh: int, mm: int, ss: int = 0, us: int = 0, d: date = D) -> datetime:
    """A tz-aware UTC instant for the given Eastern (EDT) wall-clock time on d."""
    naive = datetime(d.year, d.month, d.day, hh, mm, ss, us)
    return (naive + timedelta(hours=ET_OFFSET_HOURS)).replace(tzinfo=timezone.utc)


def make_print(ts: datetime, price: float, size: int, cid: str = CALL, **over) -> dict:
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


def write_all_options(path: str, prints: list[dict]) -> str:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    pq.write_table(pa.Table.from_pylist(prints, schema=ALL_OPTIONS_SCHEMA), path)
    return path


def write_hot_chains(path: str, rows: list[dict]) -> str:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    pq.write_table(pa.Table.from_pylist(rows, schema=HOT_CHAINS_SCHEMA), path)
    return path


def hc_row(cid: str, close: float, iv: float = 0.4, volume: int = 250) -> dict:
    return {"option_symbol": cid, "date": D, "volume": volume, "open_interest": 500,
            "premium": 1e5, "high": close, "low": close, "open": close, "close": close, "iv": iv,
            "bid": close - 0.05, "ask": close + 0.05, "trades": 10, "avg_price": close,
            "close_1": 101.0}


def basic_prints() -> list[dict]:
    """Two contracts: CALL prints early/mid/late, PUT prints only early."""
    return [
        make_print(et(9, 45), 1.00, 10), make_print(et(12, 0), 2.00, 10),
        make_print(et(15, 30), 3.00, 10),
        make_print(et(10, 0), 0.50, 20, cid=PUT), make_print(et(10, 20), 0.70, 20, cid=PUT),
    ]


def aggregate(prints: list[dict], tmp_path, hc_rows: list[dict] | None = None,
              d: date = D) -> pd.DataFrame:
    ao = write_all_options(str(tmp_path / f"ao-{d}.parquet"), prints)
    hc = write_hot_chains(str(tmp_path / f"hc-{d}.parquet"), hc_rows) if hc_rows is not None else None
    return dc.aggregate_day(duckdb.connect(), ao, hc, d)


def row_of(df: pd.DataFrame, cid: str) -> pd.Series:
    rows = df[df["option_chain_id"] == cid]
    assert len(rows) == 1, f"expected exactly one row for {cid}, got {len(rows)}"
    return rows.iloc[0]


# ----------------------------------------------------------------------------- unit: schema


@pytest.mark.unit
def test_output_has_the_exact_column_list_and_dtypes(tmp_path):
    df = aggregate(basic_prints(), tmp_path)

    assert list(df.columns) == EXPECTED_COLUMNS
    for c in ("option_chain_id", "underlying_symbol", "option_type"):
        assert pd.api.types.is_string_dtype(df[c]), c
    assert df["strike"].dtype == "float64"
    for c in ("expiry", "date", "last_ts"):
        assert pd.api.types.is_datetime64_any_dtype(df[c]), c
    for c in ("dte", "dte_cal", "n_prints", "size_total", "size_late", "size_early",
              "open_interest", "hc_volume"):
        assert pd.api.types.is_integer_dtype(df[c]), c
    for c in ("premium_total", "vwap_all", "vwap_late", "vwap_early", "last_price", "iv_vwap",
              "delta_last", "late_nbbo_mid", "late_rel_spread", "hc_close", "hc_iv"):
        assert pd.api.types.is_float_dtype(df[c]), c
    assert (df["date"] == pd.Timestamp(D)).all()
    assert list(df["option_chain_id"]) == sorted(df["option_chain_id"])


@pytest.mark.unit
def test_keys_and_dte_come_from_the_contract(tmp_path):
    df = aggregate(basic_prints(), tmp_path)
    call = row_of(df, CALL)

    assert call["underlying_symbol"] == "AAA" and call["option_type"] == "call"
    assert call["strike"] == 100.0 and call["expiry"] == pd.Timestamp(date(2026, 7, 31))
    assert call["dte"] == 2                      # Thu 07-30, Fri 07-31
    assert call["dte_cal"] == 2
    assert call["open_interest"] == 500
    assert call["underlying_last"] == 101.0


# ----------------------------------------------------------------------------- unit: windows


@pytest.mark.unit
def test_session_window_and_late_early_boundaries(tmp_path):
    prints = [
        make_print(et(9, 29, 59), 9.0, 100),            # before the open: excluded
        make_print(et(9, 30, 0), 1.0, 10),              # open: early
        make_print(et(10, 15), 1.0, 10),                # 14:15 UTC: early
        make_print(et(10, 30, 0), 1.0, 10),             # early boundary inclusive
        make_print(et(10, 30, 0, 1), 2.0, 10),          # one microsecond past: not early
        make_print(et(12, 0), 2.0, 10),
        make_print(et(14, 59, 59), 2.0, 10),            # not late
        make_print(et(15, 0, 0), 3.0, 10),              # late boundary inclusive
        make_print(et(15, 30), 3.0, 10),                # 19:30 UTC: late
        make_print(et(16, 0, 30), 3.0, 10),             # closing rotation: late, and the last print
        make_print(et(16, 1, 0), 9.0, 100),             # 20:01 UTC: excluded
    ]
    call = row_of(aggregate(prints, tmp_path), CALL)

    assert call["n_prints"] == 9 and call["size_total"] == 90
    assert call["vwap_all"] == 2.0
    assert call["vwap_early"] == 1.0 and call["size_early"] == 30
    assert call["vwap_late"] == 3.0 and call["size_late"] == 30
    assert call["last_price"] == 3.0
    assert call["last_ts"] == pd.Timestamp("2026-07-29 16:00:30")
    assert call["premium_total"] == 3000.0 + 6000.0 + 9000.0


@pytest.mark.unit
def test_canceled_prints_are_excluded_everywhere(tmp_path):
    prints = [
        make_print(et(10, 0), 1.0, 10),
        make_print(et(15, 30), 50.0, 1000, canceled=True, delta=-20.0),
        make_print(et(15, 45), 1.0, 10),
    ]
    call = row_of(aggregate(prints, tmp_path), CALL)

    assert call["n_prints"] == 2 and call["size_total"] == 20
    assert call["vwap_all"] == 1.0 and call["vwap_late"] == 1.0 and call["size_late"] == 10
    assert call["last_price"] == 1.0 and call["delta_last"] == 0.5


@pytest.mark.unit
def test_zero_size_or_zero_price_prints_are_excluded(tmp_path):
    prints = [
        make_print(et(10, 0), 1.0, 10),
        make_print(et(15, 30), 0.0, 10),
        make_print(et(15, 40), 5.0, 0),
    ]
    call = row_of(aggregate(prints, tmp_path), CALL)

    assert call["n_prints"] == 1 and call["size_total"] == 10
    assert call["size_late"] == 0 and pd.isna(call["vwap_late"])


@pytest.mark.unit
def test_delta_is_clipped_before_the_last_print_is_selected(tmp_path):
    prints = [
        make_print(et(10, 0), 1.0, 10, delta=0.4),
        make_print(et(15, 30), 1.0, 10, delta=-20.0),
        make_print(et(10, 0), 1.0, 10, cid=PUT, delta=-0.4),
        make_print(et(15, 30), 1.0, 10, cid=PUT, delta=7.0),
    ]
    df = aggregate(prints, tmp_path)

    assert row_of(df, CALL)["delta_last"] == -1.0
    assert row_of(df, PUT)["delta_last"] == 1.0


@pytest.mark.unit
def test_contract_without_late_prints_has_null_late_vwap_and_zero_late_size(tmp_path):
    put = row_of(aggregate(basic_prints(), tmp_path), PUT)

    assert pd.isna(put["vwap_late"]) and put["size_late"] == 0
    assert pd.isna(put["late_nbbo_mid"]) and pd.isna(put["late_rel_spread"])
    assert pd.isna(put["late_last_bid"]) and pd.isna(put["late_last_ask"])
    assert put["vwap_early"] == pytest.approx(0.6) and put["size_early"] == 40
    assert put["early_nbbo_mid"] == pytest.approx(0.6)


@pytest.mark.unit
def test_spread_statistics_ignore_invalid_nbbo_but_vwap_keeps_the_prints(tmp_path):
    prints = [
        make_print(et(15, 10), 1.10, 10, nbbo_bid=1.0, nbbo_ask=1.2),      # valid
        make_print(et(15, 20), 1.30, 10, nbbo_bid=0.0, nbbo_ask=1.5),      # bid <= 0
        make_print(et(15, 30), 1.45, 10, nbbo_bid=1.5, nbbo_ask=1.4),      # ask < bid
    ]
    call = row_of(aggregate(prints, tmp_path), CALL)

    assert call["size_late"] == 30
    assert call["vwap_late"] == pytest.approx((11.0 + 13.0 + 14.5) / 30)
    assert call["vwap_all"] == call["vwap_late"]
    assert call["late_nbbo_mid"] == pytest.approx(1.1)
    assert call["late_rel_spread"] == pytest.approx(0.2 / 1.1, abs=1e-6)
    assert call["late_last_bid"] == 1.0 and call["late_last_ask"] == 1.2
    assert call["last_nbbo_bid"] == 1.5 and call["last_nbbo_ask"] == 1.4    # last print regardless


@pytest.mark.unit
def test_size_weighted_spread_statistics(tmp_path):
    prints = [
        make_print(et(9, 40), 1.0, 10, nbbo_bid=0.9, nbbo_ask=1.1),         # mid 1.0, rel 0.2
        make_print(et(9, 50), 2.0, 30, nbbo_bid=1.9, nbbo_ask=2.1),         # mid 2.0, rel 0.1
    ]
    call = row_of(aggregate(prints, tmp_path), CALL)

    assert call["early_nbbo_mid"] == pytest.approx((1.0 * 10 + 2.0 * 30) / 40)
    assert call["early_rel_spread"] == pytest.approx((0.2 * 10 + 0.1 * 30) / 40, abs=1e-6)
    assert call["early_last_bid"] == 1.9 and call["early_last_ask"] == 2.1


@pytest.mark.unit
def test_vwap_arithmetic_is_exact(tmp_path):
    prints = [make_print(et(11, 0), 1.00, 10), make_print(et(11, 5), 1.50, 30)]
    call = row_of(aggregate(prints, tmp_path), CALL)

    assert call["vwap_all"] == 1.375
    assert call["premium_total"] == 1.00 * 10 * 100 + 1.50 * 30 * 100


@pytest.mark.unit
def test_iv_vwap_skips_null_iv_prints(tmp_path):
    prints = [
        make_print(et(11, 0), 1.0, 10, implied_volatility=0.20),
        make_print(et(11, 5), 1.0, 30, implied_volatility=None),
        make_print(et(11, 6), 1.0, 10, implied_volatility=0.40),
    ]
    call = row_of(aggregate(prints, tmp_path), CALL)

    assert call["iv_vwap"] == pytest.approx(0.30)
    assert call["size_total"] == 50


# ----------------------------------------------------------------------------- unit: hot chains


@pytest.mark.unit
def test_hot_chains_join_fills_hc_columns_and_leaves_them_null_without_a_file(tmp_path):
    joined = aggregate(basic_prints(), tmp_path, hc_rows=[hc_row(CALL, 2.75, iv=0.33, volume=777)])
    call, put = row_of(joined, CALL), row_of(joined, PUT)
    assert call["hc_close"] == 2.75 and call["hc_iv"] == 0.33 and call["hc_volume"] == 777
    assert pd.isna(put["hc_close"]) and pd.isna(put["hc_iv"]) and pd.isna(put["hc_volume"])

    alone = aggregate(basic_prints(), tmp_path / "nohc", hc_rows=None)
    assert alone["hc_close"].isna().all() and alone["hc_iv"].isna().all()
    assert alone["hc_volume"].isna().all()
    assert list(alone.columns) == EXPECTED_COLUMNS


@pytest.mark.unit
def test_multiple_underlyings_are_kept_apart(tmp_path):
    prints = basic_prints() + [make_print(et(11, 0), 0.10, 5, cid=OTHER, strike=50.0,
                                          expiry=date(2026, 8, 21), underlying_price=49.0)]
    df = aggregate(prints, tmp_path)

    assert len(df) == 3
    other = row_of(df, OTHER)
    assert other["underlying_symbol"] == "BBB" and other["strike"] == 50.0
    assert other["dte"] == 17 and other["dte_cal"] == 23
    assert other["underlying_last"] == 49.0


# ----------------------------------------------------------------------------- unit: determinism


@pytest.mark.unit
def test_aggregate_day_is_deterministic(tmp_path):
    prints = basic_prints() + [make_print(et(15, 30 + (i % 20), i % 60), 1.0 + i / 100, 1 + i % 7)
                               for i in range(300)]
    ao = write_all_options(str(tmp_path / "ao.parquet"), prints)
    hc = write_hot_chains(str(tmp_path / "hc.parquet"), [hc_row(CALL, 1.5)])

    first = dc.aggregate_day(duckdb.connect(), ao, hc, D)
    second = dc.aggregate_day(duckdb.connect(), ao, hc, D)

    pd.testing.assert_frame_equal(first, second, check_exact=True)


@pytest.fixture
def synthetic_panel(tmp_path, monkeypatch):
    stocks, mart = tmp_path / "stocks", tmp_path / "mart"
    monkeypatch.setattr(config, "STOCKS", str(stocks))
    monkeypatch.setattr(config, "MART", str(mart))
    for d in (D, D2):
        prints = [{**p, "executed_at": p["executed_at"] + (d - D)} for p in basic_prints()]
        write_all_options(str(stocks / config.ALL_OPTIONS_FILE.format(d=d)), prints)
    write_hot_chains(str(stocks / config.HOT_CHAINS_FILE.format(d=D)), [hc_row(CALL, 2.9)])
    return stocks, mart


@pytest.mark.unit
def test_panel_dates_enumerates_the_all_options_directory(synthetic_panel):
    assert dc.panel_dates() == [D, D2]


@pytest.mark.unit
def test_one_day_build_equals_the_full_rebuild_slice(synthetic_panel):
    dc.rebuild()
    from_rebuild = {d: store.read_partition(dc.TABLE, d) for d in (D, D2)}

    for d in (D, D2):
        rebuilt = dc.build_day(d, force=True)
        pd.testing.assert_frame_equal(rebuilt, from_rebuild[d], check_exact=True)
        pd.testing.assert_frame_equal(store.read_partition(dc.TABLE, d), from_rebuild[d],
                                      check_exact=True)
    assert from_rebuild[D].loc[from_rebuild[D]["option_chain_id"] == CALL, "hc_close"].iloc[0] == 2.9
    assert from_rebuild[D2]["hc_close"].isna().all()           # no Hot Chains file for D2


@pytest.mark.unit
def test_build_day_returns_the_existing_partition_unless_forced(synthetic_panel):
    first = dc.build_day(D)
    path = store.partition_path(dc.TABLE, D)
    mtime = os.path.getmtime(path)

    again = dc.build_day(D)
    assert os.path.getmtime(path) == mtime
    pd.testing.assert_frame_equal(first, again, check_exact=True)


@pytest.mark.unit
def test_build_day_raises_when_the_all_options_file_is_missing(synthetic_panel):
    with pytest.raises(FileNotFoundError, match="2026-08-03"):
        dc.build_day(date(2026, 8, 3))


# ----------------------------------------------------------------------------- integration

REAL_DAY = date(2026, 7, 29)
REAL_AO = os.path.join(config.STOCKS, config.ALL_OPTIONS_FILE.format(d=REAL_DAY))
REAL_HC = os.path.join(config.STOCKS, config.HOT_CHAINS_FILE.format(d=REAL_DAY))
needs_panel = pytest.mark.skipif(not os.path.exists(REAL_AO), reason="UW panel not available")

INDEPENDENT_COUNT_SQL = f"""
SELECT count(DISTINCT option_chain_id)
FROM read_parquet('{REAL_AO}')
WHERE NOT canceled AND size > 0 AND price > 0
  AND ((executed_at AT TIME ZONE '{config.ET_TZ}')::TIMESTAMP)::TIME >= TIME '{config.SESSION_START}'
  AND ((executed_at AT TIME ZONE '{config.ET_TZ}')::TIMESTAMP)::TIME <  TIME '{config.SESSION_END_EXCL}'
"""


@pytest.fixture(scope="module")
def real_day_frame() -> pd.DataFrame:
    hc = REAL_HC if os.path.exists(REAL_HC) else None
    return dc.aggregate_day(duckdb.connect(), REAL_AO, hc, REAL_DAY)


@pytest.mark.integration
@needs_panel
def test_real_day_row_count_matches_distinct_contracts_in_session(real_day_frame):
    expected = duckdb.connect().execute(INDEPENDENT_COUNT_SQL).fetchone()[0]

    assert len(real_day_frame) == expected
    assert real_day_frame["option_chain_id"].is_unique


@pytest.mark.integration
@needs_panel
def test_real_day_spy_put_has_late_prints_in_the_late_window(real_day_frame):
    spy = row_of(real_day_frame, "SPY260729P00735000")

    assert spy["size_late"] > 0 and spy["vwap_late"] > 0
    assert pd.Timestamp("2026-07-29 15:00:00") <= spy["last_ts"] < pd.Timestamp("2026-07-29 16:01:00")
    assert spy["dte"] == 0 and spy["dte_cal"] == 0
    assert -1.0 <= spy["delta_last"] <= 0.0


@pytest.mark.integration
@needs_panel
def test_real_day_builds_identically_across_thread_counts(real_day_frame):
    con = duckdb.connect()
    con.execute("PRAGMA threads=2")
    hc = REAL_HC if os.path.exists(REAL_HC) else None

    again = dc.aggregate_day(con, REAL_AO, hc, REAL_DAY)

    pd.testing.assert_frame_equal(real_day_frame, again, check_exact=True)
