"""engine.mart.regsho: FINRA Reg SHO daily short-volume parsing and the fail-soft, write-once
snapshot loader. Control variable only -- RESEARCH/30 §5, RESEARCH/47 §2 G9."""
from __future__ import annotations

from datetime import date

import pytest

from engine import config
from engine.mart import regsho as R
from engine.mart import store

pytestmark = pytest.mark.unit

TEXT = (
    "Date|Symbol|ShortVolume|ShortExemptVolume|TotalVolume|Market\n"
    "20260904|A|388208.245298|1288|756283.190557|B,Q,N\n"
    "20260904|AAPL|500000|0|1000000|B,Q,N\n"
)


def test_parse_regsho_text_normalizes_columns_and_dates():
    df = R.parse_regsho_text(TEXT)
    assert list(df.columns) == R.COLUMNS
    row = df[df.symbol == "AAPL"].iloc[0]
    assert row.date == date(2026, 9, 4)
    assert row.short_volume == 500000
    assert row.total_volume == 1000000
    assert row.market == "B,Q,N"


def test_parse_regsho_text_empty_input_gives_empty_frame():
    df = R.parse_regsho_text("")
    assert df.empty
    assert list(df.columns) == R.COLUMNS


def test_parse_regsho_text_raises_on_missing_columns():
    with pytest.raises(ValueError):
        R.parse_regsho_text("Date|Symbol\n20260904|A\n")


def test_refresh_writes_a_partition_once(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    d = date(2026, 9, 4)
    df = R.refresh(d, fetch_text=lambda dd: TEXT)
    assert len(df) == 2
    assert store.has_partition(R.TABLE, d)
    R.refresh(d, fetch_text=lambda dd: TEXT.replace("500000", "1"))
    back = store.read_partition(R.TABLE, d)
    assert back[back.symbol == "AAPL"].iloc[0].short_volume == 500000


def test_load_regsho_is_fail_soft_when_missing(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    out = R.load_regsho(date(2026, 9, 4))
    assert out["available"] is False
    assert out["data"].empty


def test_load_regsho_returns_the_snapshot_when_present(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    d = date(2026, 9, 4)
    R.refresh(d, fetch_text=lambda dd: TEXT)
    out = R.load_regsho(d)
    assert out["available"] is True
    assert len(out["data"]) == 2
