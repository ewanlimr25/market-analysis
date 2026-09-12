"""engine.mart.borrow: the IBKR `usa.txt` stock-loan parser, write-once daily snapshots and the
fail-soft `load_borrow` (RESEARCH/47 §2 G9)."""
from __future__ import annotations

from datetime import date

import pytest

from engine import config
from engine.mart import borrow as B
from engine.mart import store

pytestmark = pytest.mark.unit

USA_TXT = (
    "#BOF|2026.09.07|11:28:41\n"
    "#SYM|CUR|NAME|CON|ISIN|REBATERATE|FEERATE|AVAILABLE|FIGI|\n"
    "AAPL|USD|APPLE INC|265598|XXXXXXX31005|3.2652|0.3648|>10000000|BBG000B9XRY4|\n"
    "GME|USD|GAMESTOP CORP-CLASS A|36285627|XXXXXXXW1099|3.1963|0.4337|7600000|BBG000BB5BF6|\n"
    "#EOF|2\n"
)


def test_parse_available_handles_plain_and_greater_than_values():
    assert B.parse_available("7600000") == (7600000.0, False)
    assert B.parse_available(">10000000") == (10000000.0, True)
    val, uncapped = B.parse_available("garbage")
    assert val != val  # NaN
    assert uncapped is False


def test_parse_usa_txt_drops_marker_lines_and_keeps_two_symbols():
    df = B.parse_usa_txt(USA_TXT)
    assert list(df.columns) == B.COLUMNS
    assert sorted(df.symbol) == ["AAPL", "GME"]
    aapl = df[df.symbol == "AAPL"].iloc[0]
    assert aapl.fee_rate == pytest.approx(0.3648)
    assert aapl.rebate_rate == pytest.approx(3.2652)
    assert aapl.available_shares == 10000000.0
    assert bool(aapl.shares_uncapped) is True
    gme = df[df.symbol == "GME"].iloc[0]
    assert gme.available_shares == 7600000.0
    assert bool(gme.shares_uncapped) is False


def test_parse_usa_txt_empty_input_gives_empty_frame_with_the_right_columns():
    df = B.parse_usa_txt("")
    assert df.empty
    assert list(df.columns) == B.COLUMNS


def test_refresh_writes_a_partition_once(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    d = date(2026, 9, 7)
    df = B.refresh(d, fetch_text=lambda: USA_TXT)
    assert len(df) == 2
    assert store.has_partition(B.TABLE, d)
    # a second refresh with different content must not overwrite the existing partition
    B.refresh(d, fetch_text=lambda: USA_TXT.replace("7600000", "1"))
    back = store.read_partition(B.TABLE, d)
    assert back[back.symbol == "GME"].iloc[0].available_shares == 7600000.0


def test_load_borrow_is_fail_soft_when_the_day_has_no_snapshot(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    out = B.load_borrow(date(2026, 9, 7))
    assert out["available"] is False
    assert "2026-09-07" in out["reason"]
    assert out["data"].empty


def test_load_borrow_returns_the_snapshot_when_present(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    d = date(2026, 9, 7)
    B.refresh(d, fetch_text=lambda: USA_TXT)
    out = B.load_borrow(d)
    assert out["available"] is True
    assert out["reason"] is None
    assert len(out["data"]) == 2


def test_refresh_raises_on_transport_failure_rather_than_fabricating_data(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))

    def boom():
        raise TimeoutError("ftp connect timed out")

    with pytest.raises(TimeoutError):
        B.refresh(date(2026, 9, 7), fetch_text=boom)
    assert not store.has_partition(B.TABLE, date(2026, 9, 7))


def test_load_borrow_asof_prefers_the_exact_day(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    B.refresh(date(2026, 9, 10), fetch_text=lambda: USA_TXT.replace("7600000", "1"))
    B.refresh(date(2026, 9, 11), fetch_text=lambda: USA_TXT)
    out = B.load_borrow_asof(date(2026, 9, 11))
    assert out["available"] is True and out["asof"] == date(2026, 9, 11) and out["stale_days"] == 0
    assert out["data"][out["data"].symbol == "GME"].iloc[0].available_shares == 7600000.0


def test_load_borrow_asof_falls_back_to_the_latest_prior_snapshot_never_a_later_one(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    B.refresh(date(2026, 9, 9), fetch_text=lambda: USA_TXT.replace("7600000", "9"))
    B.refresh(date(2026, 9, 10), fetch_text=lambda: USA_TXT)
    B.refresh(date(2026, 9, 12), fetch_text=lambda: USA_TXT.replace("7600000", "12"))   # Saturday file, after the night
    out = B.load_borrow_asof(date(2026, 9, 11))
    assert out["available"] is True and out["asof"] == date(2026, 9, 10) and out["stale_days"] == 1
    assert out["data"][out["data"].symbol == "GME"].iloc[0].available_shares == 7600000.0


def test_load_borrow_asof_is_fail_soft_outside_the_window(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    B.refresh(date(2026, 9, 1), fetch_text=lambda: USA_TXT)
    out = B.load_borrow_asof(date(2026, 9, 11), max_stale_days=7)
    assert out["available"] is False and out["asof"] is None and out["stale_days"] is None
    assert out["data"].empty and "7 days" in out["reason"]
    assert B.load_borrow_asof(date(2026, 9, 8), max_stale_days=7)["asof"] == date(2026, 9, 1)
