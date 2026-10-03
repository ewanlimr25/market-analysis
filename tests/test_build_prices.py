"""scripts/truthset/build_prices.py: the weekly rebuild keeps history the vendor stopped serving.

Yahoo drops a symbol's past bars once it delists, and the builder used to replace the whole file, so
every weekly rebuild deleted the history of names that had delisted since the last one (findings
market-analysis D28, 2026-10-03: 13 names, 8 E1 events)."""
from __future__ import annotations

import os
import sys

import duckdb
import pandas as pd
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts", "truthset"))
import build_prices as BP  # noqa: E402

pytestmark = pytest.mark.unit
COLS = ["ticker", "date", "open", "high", "low", "close", "adjclose", "volume"]


def _bar(ticker: str, day: str, close: float) -> tuple:
    return (ticker, day, close, close, close, close, close, 1000)


def _write_existing(path: str, rows: list[tuple]) -> None:
    df = pd.DataFrame(rows, columns=COLS).assign(date=lambda d: pd.to_datetime(d.date).dt.date)
    df.to_parquet(path, index=False)


def _read(path: str) -> pd.DataFrame:
    return duckdb.connect().execute(f"SELECT * FROM read_parquet('{path}') ORDER BY ticker, date").df()


def test_rows_the_vendor_no_longer_serves_are_kept(tmp_path):
    out = str(tmp_path / "prices.parquet")
    _write_existing(out, [_bar("AVB", "2026-07-21", 180.0), _bar("AVB", "2026-07-22", 181.0),
                          _bar("SPY", "2026-07-22", 600.0)])
    kept = BP.write_merged([_bar("AVB", "2026-08-14", 184.06), _bar("SPY", "2026-07-22", 601.0),
                            _bar("SPY", "2026-07-23", 602.0)], out)
    df = _read(out)
    assert kept == {"AVB": 2}
    assert df[df.ticker == "AVB"].close.tolist() == [180.0, 181.0, 184.06]
    assert df[df.ticker == "SPY"].close.tolist() == [601.0, 602.0]           # the new fetch wins on overlap
    assert list(df.columns) == COLS and str(df.date.dtype).startswith("datetime64")


def test_first_build_without_an_existing_file_writes_the_fetch(tmp_path):
    out = str(tmp_path / "prices.parquet")
    assert BP.write_merged([_bar("SPY", "2026-07-22", 600.0)], out) == {}
    assert _read(out).close.tolist() == [600.0]


def test_a_failed_ticker_keeps_its_whole_history(tmp_path):
    out = str(tmp_path / "prices.parquet")
    _write_existing(out, [_bar("XYZ", "2026-07-22", 10.0), _bar("SPY", "2026-07-22", 600.0)])
    assert BP.write_merged([_bar("SPY", "2026-07-22", 600.0)], out) == {"XYZ": 1}
    assert set(_read(out).ticker) == {"SPY", "XYZ"}


def test_no_temp_file_is_left_behind(tmp_path):
    out = str(tmp_path / "prices.parquet")
    BP.write_merged([_bar("SPY", "2026-07-22", 600.0)], out)
    assert sorted(os.listdir(tmp_path)) == ["prices.parquet"]


# ---- renamed symbols (D28 addendum) -------------------------------------------------------------

def test_a_renamed_symbol_is_fetched_under_its_new_name():
    assert BP.query_symbol("BK") == "BNY" and BP.query_symbol("SATS") == "ECHO" and BP.query_symbol("VSCO") == "VSXY"
    assert BP.query_symbol("BRKB") == "BRK-B" and BP.query_symbol("SPY") == "SPY"


def test_a_renamed_symbol_keeps_only_the_days_the_panel_used_the_old_name():
    rows = [_bar("BK", "2026-05-20", 130.0), _bar("BK", "2026-05-21", 131.0), _bar("BK", "2026-05-22", 132.0)]
    assert [r[1] for r in BP.trim_renamed("BK", rows)] == ["2026-05-20", "2026-05-21"]
    assert BP.trim_renamed("SPY", rows) == rows


def test_the_rename_map_never_points_a_symbol_at_itself_or_at_an_alias():
    from chart import RENAMES, YAHOO_ALIASES
    assert all(old != new and old not in YAHOO_ALIASES for old, (new, _) in RENAMES.items())
