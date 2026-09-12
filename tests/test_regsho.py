"""engine.mart.regsho: FINRA Reg SHO daily short-volume parsing and the fail-soft, write-once
snapshot loader. Control variable only -- RESEARCH/30 §5, RESEARCH/47 §2 G9."""
from __future__ import annotations

import urllib.error
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


def _http_error(code: int) -> urllib.error.HTTPError:
    return urllib.error.HTTPError("https://cdn.finra.org/x", code, "Forbidden", hdrs=None, fp=None)


def test_refresh_missing_stores_published_weekdays_and_records_the_rest(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    published = {date(2026, 9, 10), date(2026, 9, 11)}

    def fetch(d):
        if d in published:
            return TEXT.replace("20260904", d.strftime("%Y%m%d"))
        if d == date(2026, 9, 9):
            raise urllib.error.URLError("dns down")
        raise _http_error(403)

    out = R.refresh_missing(date(2026, 9, 12), lookback_days=4, fetch_text=fetch)
    by_date = {r["date"]: r for r in out}
    assert sorted(by_date) == [date(2026, 9, 8), date(2026, 9, 9), date(2026, 9, 10), date(2026, 9, 11)]   # 09-12 Sat skipped
    assert by_date[date(2026, 9, 8)]["status"] == R.STATUS_NOT_PUBLISHED
    assert by_date[date(2026, 9, 9)]["status"] == R.STATUS_ERROR
    assert by_date[date(2026, 9, 10)]["status"] == R.STATUS_STORED and by_date[date(2026, 9, 10)]["rows"] == 2
    assert store.has_partition(R.TABLE, date(2026, 9, 11)) and not store.has_partition(R.TABLE, date(2026, 9, 8))


def test_refresh_missing_skips_days_already_stored(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    R.refresh(date(2026, 9, 11), fetch_text=lambda dd: TEXT)
    calls = []

    def fetch(d):
        calls.append(d)
        raise _http_error(404)

    out = R.refresh_missing(date(2026, 9, 11), lookback_days=1, fetch_text=fetch)
    assert calls == [date(2026, 9, 10)]
    assert out == [{"date": date(2026, 9, 10), "status": R.STATUS_NOT_PUBLISHED, "rows": 0, "reason": "HTTP 404"}]


def test_summarize_catchup_names_each_outcome():
    line = R.summarize_catchup([
        {"date": date(2026, 9, 11), "status": R.STATUS_STORED, "rows": 5000, "reason": None},
        {"date": date(2026, 9, 12), "status": R.STATUS_NOT_PUBLISHED, "rows": 0, "reason": "HTTP 403"},
        {"date": date(2026, 9, 9), "status": R.STATUS_ERROR, "rows": 0, "reason": "dns down"},
    ])
    assert line.startswith("regsho: stored 2026-09-11 (5000 symbols); not published: 2026-09-12; errors: 2026-09-09: dns down")
    assert R.summarize_catchup([]).startswith("regsho: nothing new to store")
