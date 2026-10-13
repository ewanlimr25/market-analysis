"""engine.screener: UW's Stock Screener export read under the engine's column names, in either format.

On 2026-10-12 the export changed (findings market-analysis D37): `is_index` was folded into `issue_type`
('Index'), `total_volume` became `stock_volume`, and about 150 columns were added. The first nightly on it
failed in the watch basket's universe read; S-C's Friday entry, the ticker sheet and the truth set's
features read the same columns.
"""
from __future__ import annotations

import os
from datetime import date

import duckdb
import pandas as pd
import pytest

from engine import screener as SC
from engine.name import data as ND
from engine.name import data_marts as DM
from engine.strategies import sc_data
from engine.watch import universe as U

OLD_DAY, NEW_DAY = date(2026, 10, 9), date(2026, 10, 12)
TICKERS = ["AAPL", "SPX", "QQQ"]
SHARED = {"marketcap": [3.4e12, None, 3.0e11], "close": [254.0, 6700.0, 600.0], "iv30d": [0.25, 0.15, 0.2],
          "iv_rank": [30.0, 20.0, 25.0], "week_52_high": [260.0, 6800.0, 610.0],
          "week_52_low": [170.0, 4800.0, 450.0], "sector": ["Technology", None, None],
          "bullish_premium": [1e6, 0.0, 2e6], "bearish_premium": [5e5, 0.0, 1e6],
          "net_call_premium": [1e5, 0.0, 2e5], "net_put_premium": [-1e5, 0.0, -2e5],
          "avg30_volume": [39e6, 0.0, 50e6]}


def _old_format(d: date = OLD_DAY) -> pd.DataFrame:
    return pd.DataFrame({"date": [d] * 3, "ticker": TICKERS, "issue_type": ["Common Stock", None, "ETF"],
                         "is_index": [False, True, False], "total_volume": [31_679_931, 0, 40_000_000],
                         "next_earnings_date": [date(2026, 10, 29), None, None], **SHARED})


def _new_format(d: date = NEW_DAY) -> pd.DataFrame:
    return pd.DataFrame({"date": [d] * 3, "ticker": TICKERS, "issue_type": ["Common Stock", "Index", "ETF"],
                         "stock_volume": [19_535_127, 0, 30_000_000], "relative_volume": [0.49, 0.0, 0.6],
                         "next_earnings_date": [date(2026, 10, 29), None, None], **SHARED})


@pytest.fixture
def stocks(tmp_path) -> str:
    """A stocks dir holding the last old-format export and the first new-format one."""
    folder = tmp_path / "Stock Screener"
    folder.mkdir()
    _old_format().to_parquet(folder / f"stock-screener-{OLD_DAY.isoformat()}.parquet", index=False)
    _new_format().to_parquet(folder / f"stock-screener-{NEW_DAY.isoformat()}.parquet", index=False)
    return str(tmp_path)


def _select(stocks_dir: str, days: list[date]) -> pd.DataFrame:
    paths = [os.path.join(stocks_dir, "Stock Screener", f"stock-screener-{d.isoformat()}.parquet") for d in days]
    con = duckdb.connect()
    source = f"read_parquet({paths!r}, union_by_name=true)"
    cols = SC.select_list(con, source, ("date", "ticker", "is_index", "total_volume"))
    return con.execute(f"SELECT {cols} FROM {source} ORDER BY date, ticker").df()


# ---- the helpers ----------------------------------------------------------------------------------
@pytest.mark.unit
def test_select_list_reads_the_old_format_as_it_was(stocks):
    out = _select(stocks, [OLD_DAY])
    assert out.ticker.tolist() == ["AAPL", "QQQ", "SPX"]
    assert out.is_index.tolist() == [False, False, True] and out.total_volume.tolist() == [31_679_931, 40_000_000, 0]


@pytest.mark.unit
def test_select_list_answers_the_old_names_from_the_new_format(stocks):
    out = _select(stocks, [NEW_DAY])
    assert out.is_index.tolist() == [False, False, True]                  # issue_type 'Index'
    assert out.total_volume.tolist() == [19_535_127, 30_000_000, 0]       # stock_volume


@pytest.mark.unit
def test_select_list_reads_both_formats_in_one_scan(stocks):
    out = _select(stocks, [OLD_DAY, NEW_DAY])
    assert len(out) == 6 and out.is_index.notna().all() and out.total_volume.notna().all()
    assert out[out.ticker == "SPX"].is_index.tolist() == [True, True]


@pytest.mark.unit
def test_with_old_names_fills_a_new_format_frame_and_leaves_an_old_one_alone():
    new = SC.with_old_names(_new_format())
    assert new.is_index.tolist() == [False, True, False]
    assert new.total_volume.tolist() == [19_535_127, 0, 30_000_000]
    old = _old_format()
    assert SC.with_old_names(old).equals(old)


# ---- the readers that broke -----------------------------------------------------------------------
@pytest.mark.unit
def test_the_watch_basket_universe_reads_across_the_format_change(stocks):
    panel = U.load_screener_panel([OLD_DAY, NEW_DAY], stocks_dir=stocks)
    assert len(panel) == 6 and set(U.SCREENER_COLUMNS) <= set(panel.columns)
    assert panel[panel.ticker == "SPX"].is_index.tolist() == [True, True]


@pytest.mark.unit
def test_s_c_reads_a_new_format_export(stocks):
    rows = sc_data.load_screener_rows(duckdb.connect(), NEW_DAY, stocks_dir=stocks)
    assert dict(zip(rows.ticker, rows.is_index)) == {"AAPL": False, "SPX": True, "QQQ": False}


@pytest.mark.unit
def test_the_ticker_sheet_reads_a_new_format_export(stocks):
    con = duckdb.connect()
    day, _, note = DM.screener_day(con, NEW_DAY, stocks_dir=stocks)
    assert note is None and dict(zip(day.ticker, day.total_volume))["AAPL"] == 19_535_127
    universe, note = DM.universe_today(day, ND.UNIVERSE_COLUMNS)
    assert note is None and len(universe) == 3
    history, _, note = DM.screener_history(con, "AAPL", NEW_DAY, 5, ND.SCREENER_HISTORY_COLUMNS, stocks_dir=stocks)
    assert note is None and history.total_volume.tolist() == [31_679_931, 19_535_127]
