"""engine.mart.short_interest: FINRA consolidated short interest parsing, write-once partitions and
the point-in-time `load_short_interest` rule (RESEARCH/47 §2 G9).
"""
from __future__ import annotations

from datetime import date

import pandas as pd
import pytest

from engine import calendar as cal
from engine import config
from engine.mart import short_interest as SI
from engine.mart import store

pytestmark = pytest.mark.unit

CSV_AAPL = (
    "accountingYearMonthNumber,symbolCode,issueName,issuerServicesGroupExchangeCode,marketClassCode,"
    "currentShortPositionQuantity,previousShortPositionQuantity,stockSplitFlag,averageDailyVolumeQuantity,"
    "daysToCoverQuantity,revisionFlag,changePercent,changePreviousNumber,settlementDate\n"
    '20260814,AAPL,Apple Inc.,R,NNM,116327753,141606163,,46065396,2.53,,-17.85,-25278410,2026-08-14\n'
    '20260731,AAPL,Apple Inc.,R,NNM,141606163,146547784,,58400983,2.42,,-3.37,-4941621,2026-07-31\n'
)
CSV_MSFT = (
    "accountingYearMonthNumber,symbolCode,issueName,issuerServicesGroupExchangeCode,marketClassCode,"
    "currentShortPositionQuantity,previousShortPositionQuantity,stockSplitFlag,averageDailyVolumeQuantity,"
    "daysToCoverQuantity,revisionFlag,changePercent,changePreviousNumber,settlementDate\n"
    '20260814,MSFT,Microsoft Corp,R,NNM,50000000,49000000,,20000000,2.50,,2.04,1000000,2026-08-14\n'
)


def test_parse_finra_csv_normalizes_and_renames_columns():
    df = SI.parse_finra_csv(CSV_AAPL)
    assert list(df.columns) == SI.COLUMNS
    assert df.symbol.tolist() == ["AAPL", "AAPL"]
    row = df[df.settlement_date == date(2026, 8, 14)].iloc[0]
    assert row.current_short_position == 116327753
    assert row.previous_short_position == 141606163
    assert row.avg_daily_volume == 46065396
    assert row.days_to_cover == pytest.approx(2.53)
    assert row.change_percent == pytest.approx(-17.85)
    # sorted by (symbol, settlement_date)
    assert df.settlement_date.tolist() == [date(2026, 7, 31), date(2026, 8, 14)]


def test_parse_finra_csv_empty_input_gives_empty_frame_with_the_right_columns():
    df = SI.parse_finra_csv("")
    assert df.empty
    assert list(df.columns) == SI.COLUMNS


def test_parse_finra_csv_raises_on_missing_columns():
    with pytest.raises(ValueError):
        SI.parse_finra_csv("nonsense,without,the,right,columns\n1,2,3,4,5\n")


def test_publication_date_is_nine_trading_days_after_settlement():
    assert SI.publication_date(date(2026, 8, 14)) == cal.next_session(date(2026, 8, 14), 9)
    assert SI.publication_date(date(2026, 8, 14)) == date(2026, 8, 27)


def test_write_settlement_partitions_is_write_once(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    df = SI.parse_finra_csv(CSV_AAPL)
    paths = SI.write_settlement_partitions(df)
    assert len(paths) == 2
    assert store.has_partition(SI.TABLE, date(2026, 8, 14))
    # a second write with different data for an existing date must not overwrite it
    changed = df.copy()
    changed.loc[changed.settlement_date == date(2026, 8, 14), "current_short_position"] = 999
    SI.write_settlement_partitions(changed)
    back = store.read_partition(SI.TABLE, date(2026, 8, 14))
    assert back.current_short_position.iloc[0] == 116327753


def test_refresh_fetches_every_symbol_combines_and_writes(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    texts = {"AAPL": CSV_AAPL, "MSFT": CSV_MSFT}
    df = SI.refresh(["AAPL", "MSFT"], fetch_text=lambda s: texts[s])
    assert len(df) == 3
    assert set(df.symbol) == {"AAPL", "MSFT"}
    assert store.has_partition(SI.TABLE, date(2026, 8, 14))
    on_disk = store.read_partition(SI.TABLE, date(2026, 8, 14))
    assert set(on_disk.symbol) == {"AAPL", "MSFT"}


def test_refresh_is_fail_soft_per_symbol(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))

    def flaky(symbol):
        if symbol == "BAD":
            raise TimeoutError("boom")
        return CSV_AAPL if symbol == "AAPL" else CSV_MSFT

    errors = []
    df = SI.refresh(["AAPL", "BAD", "MSFT"], fetch_text=flaky, on_error=lambda s, e: errors.append((s, e)))
    assert errors == [("BAD", errors[0][1])]
    assert isinstance(errors[0][1], TimeoutError)
    assert set(df.symbol) == {"AAPL", "MSFT"}


def test_refresh_runs_fine_with_multiple_workers(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    texts = {"AAPL": CSV_AAPL, "MSFT": CSV_MSFT}
    df = SI.refresh(["AAPL", "MSFT"], fetch_text=lambda s: texts[s], max_workers=4)
    assert set(df.symbol) == {"AAPL", "MSFT"}


def test_load_short_interest_returns_empty_when_the_table_does_not_exist(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    out = SI.load_short_interest(date(2026, 9, 1))
    assert out.empty
    assert list(out.columns) == SI.COLUMNS


def test_load_short_interest_hides_a_row_before_its_publication_date(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    SI.refresh(["AAPL"], fetch_text=lambda s: CSV_AAPL)
    pub = SI.publication_date(date(2026, 8, 14))
    # the day before publication: the 08-14 row must not be visible; 07-31 (published earlier) is
    before = SI.load_short_interest(cal.prev_session(pub))
    assert before.iloc[0].settlement_date == date(2026, 7, 31)
    # on the publication date itself: now visible
    on_pub = SI.load_short_interest(pub)
    assert on_pub.iloc[0].settlement_date == date(2026, 8, 14)
    assert on_pub.iloc[0].current_short_position == 116327753


def test_load_short_interest_picks_the_latest_visible_settlement_per_symbol(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    texts = {"AAPL": CSV_AAPL, "MSFT": CSV_MSFT}
    SI.refresh(["AAPL", "MSFT"], fetch_text=lambda s: texts[s])
    far_future = date(2027, 1, 1)
    out = SI.load_short_interest(far_future)
    assert len(out) == 2
    aapl = out[out.symbol == "AAPL"].iloc[0]
    assert aapl.settlement_date == date(2026, 8, 14)


def test_load_short_interest_before_any_publication_is_empty(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    SI.refresh(["AAPL"], fetch_text=lambda s: CSV_AAPL)
    out = SI.load_short_interest(date(2000, 1, 1))
    assert out.empty
