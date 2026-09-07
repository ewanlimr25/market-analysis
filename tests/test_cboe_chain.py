"""G8: the CBOE delayed option-chain loader (RESEARCH/47 §2 G8; artifacts/edge-gaps/g8).

Parser on a saved, truncated real payload; write-once and fail-soft behaviour with injected
fetchers/clocks, no network."""
from __future__ import annotations

import json
import os
from datetime import date, datetime, timezone

import pandas as pd
import pytest

from engine.mart import cboe_chain as C

pytestmark = pytest.mark.unit

FIXTURE = os.path.join(os.path.dirname(__file__), "fixtures", "cboe_chain_spy_truncated.json")
FETCHED_AT = datetime(2026, 9, 7, 15, 30, tzinfo=timezone.utc)


def _fixture_payload() -> dict:
    with open(FIXTURE) as fh:
        return json.load(fh)


def test_parse_occ_code_reads_expiry_right_and_strike():
    assert C.parse_occ_code("SPY260908C00500000") == (date(2026, 9, 8), "C", 500.0)
    assert C.parse_occ_code("SPY260908P00505500") == (date(2026, 9, 8), "P", 505.5)


def test_parse_occ_code_rejects_garbage():
    assert C.parse_occ_code("BADCODE") is None
    assert C.parse_occ_code("SPY26090XC00500000") is None
    assert C.parse_occ_code("") is None


def test_parse_chain_on_the_truncated_real_fixture(caplog):
    payload = _fixture_payload()
    with caplog.at_level("WARNING"):
        df = C.parse_chain(payload, FETCHED_AT)
    # fixture has 18 option rows, 2 deliberately malformed (rejected)
    assert len(df) == 16
    assert list(df.columns) == C.CHAIN_COLUMNS
    assert set(df.right) <= {"C", "P"}
    assert (df.symbol == "SPY").all()
    assert (df.fetched_at == FETCHED_AT).all()
    assert (df.source == "cboe_delayed").all()
    assert df.underlying_price.iloc[0] == pytest.approx(payload["data"]["current_price"])
    assert any("rejected 2/18" in r.message for r in caplog.records)


def test_parse_chain_mid_is_the_bid_ask_average():
    payload = _fixture_payload()
    df = C.parse_chain(payload, FETCHED_AT)
    row = df[df.option_code == "SPY260908C00500000"].iloc[0]
    assert row.mid == pytest.approx((row.bid + row.ask) / 2.0)


def test_parse_chain_on_an_empty_options_list_returns_empty_schema_stable_frame():
    df = C.parse_chain({"symbol": "SPY", "data": {"symbol": "SPY", "options": [], "current_price": 100.0}}, FETCHED_AT)
    assert df.empty
    assert list(df.columns) == C.CHAIN_COLUMNS


def test_parse_chain_on_a_payload_with_no_data_key_returns_empty_not_a_crash():
    df = C.parse_chain({"symbol": "SPY"}, FETCHED_AT)
    assert df.empty


def test_chain_asof_date_reads_the_underlying_last_trade_time():
    payload = _fixture_payload()
    assert C.chain_asof_date(payload) == date(2026, 9, 4)


def test_chain_asof_date_is_none_without_a_last_trade_time():
    assert C.chain_asof_date({"data": {}}) is None


def test_store_and_load_chain_round_trip(tmp_path, monkeypatch):
    monkeypatch.setattr(C, "CBOE_CHAIN_DIR", str(tmp_path))
    df = C.parse_chain(_fixture_payload(), FETCHED_AT)
    path = C.store_chain(df, "SPY", date(2026, 9, 4))
    assert path == os.path.join(str(tmp_path), "symbol=SPY", "date=2026-09-04", "part.parquet")
    assert os.path.exists(path) and not os.path.exists(path + ".tmp")
    loaded = C.load_chain("SPY", date(2026, 9, 4))
    assert len(loaded) == len(df)
    assert C.has_chain("SPY", date(2026, 9, 4))
    assert not C.has_chain("SPY", date(2026, 9, 5))


def test_store_chain_is_write_once_unless_forced(tmp_path, monkeypatch):
    monkeypatch.setattr(C, "CBOE_CHAIN_DIR", str(tmp_path))
    df = C.parse_chain(_fixture_payload(), FETCHED_AT)
    C.store_chain(df, "SPY", date(2026, 9, 4))
    with pytest.raises(FileExistsError):
        C.store_chain(df, "SPY", date(2026, 9, 4))
    # force=True overwrites
    smaller = df.iloc[:3]
    C.store_chain(smaller, "SPY", date(2026, 9, 4), force=True)
    assert len(C.load_chain("SPY", date(2026, 9, 4))) == 3


def test_load_chain_raises_a_clear_error_when_never_fetched(tmp_path, monkeypatch):
    monkeypatch.setattr(C, "CBOE_CHAIN_DIR", str(tmp_path))
    with pytest.raises(FileNotFoundError):
        C.load_chain("SPY", date(2026, 9, 4))


def test_normalize_symbol_strips_index_prefixes():
    assert C._normalize_symbol("_SPX") == "SPX"
    assert C._normalize_symbol("^VIX") == "VIX"
    assert C._normalize_symbol("spy") == "SPY"


def test_fetch_chain_raises_cboe_fetch_error_on_a_network_failure():
    import urllib.error

    def bad_opener(req, timeout):
        raise urllib.error.URLError("boom")

    with pytest.raises(C.CboeFetchError):
        C.fetch_chain("SPY", opener=bad_opener)


def test_fetch_chain_raises_on_unparseable_json():
    class FakeResp:
        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def read(self):
            return b"not json"

    def opener(req, timeout):
        return FakeResp()

    with pytest.raises(C.CboeFetchError):
        C.fetch_chain("SPY", opener=opener)


def test_fetch_chain_raises_when_the_payload_has_no_data_key():
    class FakeResp:
        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def read(self):
            return json.dumps({"symbol": "SPY"}).encode()

    def opener(req, timeout):
        return FakeResp()

    with pytest.raises(C.CboeFetchError):
        C.fetch_chain("SPY", opener=opener)


def _fake_fetch(payload_by_symbol: dict):
    def fetch(symbol: str) -> dict:
        if symbol not in payload_by_symbol:
            raise C.CboeFetchError(f"no fixture for {symbol}")
        return payload_by_symbol[symbol]
    return fetch


def test_refresh_one_stores_and_reports_available(tmp_path, monkeypatch):
    monkeypatch.setattr(C, "CBOE_CHAIN_DIR", str(tmp_path))
    fetch = _fake_fetch({"SPY": _fixture_payload()})
    result = C.refresh_one("SPY", fetch=fetch, now=lambda: FETCHED_AT)
    assert result["available"] is True
    assert result["rows"] == 16
    assert result["asof_date"] == "2026-09-04"
    assert C.has_chain("SPY", date(2026, 9, 4))


def test_refresh_one_is_fail_soft_on_a_fetch_error(tmp_path, monkeypatch):
    monkeypatch.setattr(C, "CBOE_CHAIN_DIR", str(tmp_path))
    fetch = _fake_fetch({})
    result = C.refresh_one("SPY", fetch=fetch, now=lambda: FETCHED_AT)
    assert result["available"] is False
    assert "no fixture" in result["reason"]
    assert result["rows"] == 0


def test_refresh_chains_isolates_one_bad_symbol_from_the_rest(tmp_path, monkeypatch):
    monkeypatch.setattr(C, "CBOE_CHAIN_DIR", str(tmp_path))
    fetch = _fake_fetch({"SPY": _fixture_payload()})
    result = C.refresh_chains(["SPY", "QQQ"], fetch=fetch, now=lambda: FETCHED_AT)
    assert result["SPY"]["available"] is True
    assert result["QQQ"]["available"] is False
    assert set(result) == {"SPY", "QQQ"}


def test_refresh_one_never_raises_even_on_a_store_failure(tmp_path, monkeypatch):
    # CBOE_CHAIN_DIR points at a path that cannot be created (a file, not a dir, in the way)
    blocker = tmp_path / "symbol=SPY"
    blocker.parent.mkdir(parents=True, exist_ok=True) if False else None
    monkeypatch.setattr(C, "CBOE_CHAIN_DIR", str(tmp_path / "blocked"))
    (tmp_path / "blocked").write_text("i am a file, not a directory")
    fetch = _fake_fetch({"SPY": _fixture_payload()})
    result = C.refresh_one("SPY", fetch=fetch, now=lambda: FETCHED_AT)
    assert result["available"] is False
