"""The FINRA loader on a total failure: one retry, then a failure the nightly shows (findings market-analysis D40, O17)."""
from __future__ import annotations

import json
import os
import sys
from datetime import date

import pytest

from engine import config
from engine.mart import short_interest as SI
from engine.mart import store

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))
import preflight  # noqa: E402

pytestmark = pytest.mark.unit

CSV = ('"accountingYearMonthNumber","symbolCode","issueName","issuerServicesGroupExchangeCode",'
       '"marketClassCode","currentShortPositionQuantity","previousShortPositionQuantity","stockSplitFlag",'
       '"averageDailyVolumeQuantity","daysToCoverQuantity","revisionFlag","changePercent",'
       '"changePreviousNumber","settlementDate"\n'
       '20260814,"AAPL","Apple Inc.","R","NMS",116327753,115000000,,47000000,2.47,,1.15,1327753,"2026-08-14"\n')
NO_DNS = OSError("<urlopen error [Errno 8] nodename nor servname provided, or not known>")
SYMBOLS = ["AAPL", "MSFT"]


class Network:
    """A FINRA that is down for the first `down_calls` requests, then answers."""

    def __init__(self, down_calls: int) -> None:
        self.down_calls, self.calls = down_calls, 0

    def __call__(self, symbol: str) -> str:
        self.calls += 1
        if self.calls <= self.down_calls:
            raise NO_DNS
        return CSV.replace("AAPL", symbol)


@pytest.fixture
def waits(tmp_path, monkeypatch) -> list[float]:
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    monkeypatch.setattr(config, "DATA", str(tmp_path))
    recorded: list[float] = []
    monkeypatch.setattr(SI.time, "sleep", recorded.append)
    return recorded


def _main(monkeypatch, network: Network) -> int:
    monkeypatch.setattr(SI, "fetch_symbol_text", network)
    monkeypatch.setattr("engine.fetch_list.load", lambda path: list(SYMBOLS))
    monkeypatch.setattr("sys.argv", ["short_interest", "--refresh", "--workers", "1"])
    return SI.main()


def _marker() -> str:
    return os.path.join(config.DATA, SI.FAILED_MARKER)


def test_every_symbol_failing_waits_then_retries_and_recovers(waits):
    network = Network(down_calls=len(SYMBOLS))
    df, errors = SI.refresh_with_retry(SYMBOLS, fetch_text=network)
    assert waits == [SI.RETRY_WAIT_S]
    assert errors == []
    assert set(df.symbol) == set(SYMBOLS)
    assert store.has_partition(SI.TABLE, date(2026, 8, 14))


def test_it_retries_only_once(waits):
    network = Network(down_calls=99)
    df, errors = SI.refresh_with_retry(SYMBOLS, fetch_text=network)
    assert waits == [SI.RETRY_WAIT_S]
    assert network.calls == 2 * len(SYMBOLS)
    assert df.empty and len(errors) == len(SYMBOLS)


def test_a_partial_failure_does_not_retry(waits):
    df, errors = SI.refresh_with_retry(SYMBOLS, fetch_text=Network(down_calls=1))
    assert waits == []
    assert len(errors) == 1 and len(df) == 1


def test_an_empty_universe_is_not_a_failure(waits):
    df, errors = SI.refresh_with_retry([], fetch_text=Network(down_calls=99))
    assert waits == [] and errors == [] and df.empty


def test_main_exits_nonzero_and_leaves_a_marker_when_the_retry_also_fails(waits, monkeypatch, capsys):
    assert _main(monkeypatch, Network(down_calls=99)) == SI.EXIT_TOTAL_FAILURE
    with open(_marker()) as fh:
        marker = json.load(fh)
    assert marker["symbols"] == len(SYMBOLS)
    assert "nodename" in marker["error"]
    assert "FAILED" in capsys.readouterr().err


def test_main_exits_zero_with_no_marker_when_the_retry_recovers(waits, monkeypatch):
    assert _main(monkeypatch, Network(down_calls=len(SYMBOLS))) == 0
    assert not os.path.exists(_marker())


def test_a_later_success_clears_the_marker(waits, monkeypatch):
    _main(monkeypatch, Network(down_calls=99))
    assert os.path.exists(_marker())
    assert _main(monkeypatch, Network(down_calls=0)) == 0
    assert not os.path.exists(_marker())


def test_a_partial_failure_clears_the_marker_too(waits, monkeypatch):
    _main(monkeypatch, Network(down_calls=99))
    assert _main(monkeypatch, Network(down_calls=1)) == 0
    assert not os.path.exists(_marker())


def test_preflight_and_the_loader_agree_on_the_marker():
    assert preflight.FINRA_FAILED_MARKER == SI.FAILED_MARKER


def test_preflight_has_nothing_to_say_without_a_marker(tmp_path):
    assert preflight.finra_warning(str(tmp_path)) is None


def test_the_nightly_preflight_leads_with_the_failed_pull(waits, monkeypatch, tmp_path):
    _main(monkeypatch, Network(down_calls=99))
    monkeypatch.setattr(preflight, "DATA", str(tmp_path))
    monkeypatch.setattr(preflight, "STOCKS", str(tmp_path / "no-panel"))
    result = preflight.check("2026-11-16")
    assert result["ok"] is False
    assert result["warnings"][0].startswith("FINRA short interest")
    assert "make loaders-weekly" in result["warnings"][0]
    assert str(tmp_path) not in result["warnings"][0]   # the report is public: no machine path


def test_an_unreadable_marker_still_warns(tmp_path):
    os.makedirs(tmp_path / "logs")
    (tmp_path / preflight.FINRA_FAILED_MARKER).write_text("not json")
    assert preflight.finra_warning(str(tmp_path)).startswith("FINRA short interest")
