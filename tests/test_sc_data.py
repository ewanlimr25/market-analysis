"""engine.strategies.sc_data: the screener + ADV entry universe and contract rows, on temp files."""
from __future__ import annotations

from datetime import date, timedelta

import duckdb
import pandas as pd
import pytest

from engine import config
from engine.mart import store
from engine.strategies import sc_data as D

pytestmark = pytest.mark.unit


def _prices(tmp_path, ticker="ACME", n=25, close=50.0, volume=2_000_000):
    days = [date(2026, 6, 1) + timedelta(days=i) for i in range(40) if (date(2026, 6, 1) + timedelta(days=i)).weekday() < 5][:n]
    df = pd.DataFrame({"ticker": ticker, "date": days, "open": close, "high": close, "low": close, "close": close,
                       "adjclose": close, "volume": volume})
    path = tmp_path / "prices.parquet"
    df.to_parquet(path, index=False)
    return str(path), days


def test_adv_is_the_20_session_mean_dollar_volume_ending_at_the_date(tmp_path):
    path, days = _prices(tmp_path)
    con = duckdb.connect()
    adv = D.adv_usd_20d(con, ["ACME", "NOPE"], days[-1], path)
    assert adv == {"ACME": pytest.approx(50.0 * 2_000_000)}
    early = D.adv_usd_20d(con, ["ACME"], days[5], path)          # only 6 sessions on or before: below the minimum
    assert early == {}


def test_entry_universe_attaches_adv_and_is_empty_without_a_screener(tmp_path):
    path, days = _prices(tmp_path)
    d = days[-1]
    scr_dir = tmp_path / "Stock Screener"
    scr_dir.mkdir()
    pd.DataFrame({"date": [d, d], "ticker": ["ACME", "ZZZ"], "issue_type": ["Common Stock", "ETF"], "is_index": [False, False],
                  "close": [50.0, 20.0], "marketcap": [5e9, 1e9], "iv30d": [0.4, 0.5],
                  "next_earnings_date": [pd.Timestamp(d + timedelta(days=60)), pd.NaT], "sector": ["Energy", "X"]}
                 ).to_parquet(scr_dir / f"stock-screener-{d.isoformat()}.parquet", index=False)
    con = duckdb.connect()
    uni = D.load_entry_universe(con, d, str(tmp_path), path)
    assert list(uni["ticker"]) == ["ACME", "ZZZ"]
    assert uni["adv_usd_20d"].iloc[0] == pytest.approx(1e8) and pd.isna(uni["adv_usd_20d"].iloc[1])
    assert uni["next_earnings_date"].iloc[0] == d + timedelta(days=60) and pd.isna(uni["next_earnings_date"].iloc[1])
    assert D.load_entry_universe(con, d - timedelta(days=1), str(tmp_path), path).empty


def test_contract_rows_come_from_the_partition_of_the_day(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    d = date(2026, 7, 10)
    rows = pd.DataFrame({"underlying_symbol": ["ACME", "ACME", "OTHER"], "option_type": ["call", "put", "call"],
                         "strike": [50.0, 50.0, 10.0], "expiry": pd.to_datetime([date(2026, 8, 7)] * 3), "date": [d] * 3,
                         "size_late": [40, 40, 40], "late_rel_spread": [0.05, 0.05, 0.05], "dte_cal": [28, 28, 28]})
    store.write_partition(rows, D.CONTRACTS, d)
    con = duckdb.connect()
    got = D.load_contract_rows(con, ["ACME"], d)
    assert len(got) == 2 and got["expiry"].iloc[0] == date(2026, 8, 7)
    assert D.load_contract_rows(con, ["ACME"], d + timedelta(days=1)).empty
