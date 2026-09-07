"""engine.mart.finviz_short: the `fz quote --agent` wrapper, fail-soft when the CLI's own output is
missing the short-interest fields (RESEARCH/47 §2 G9; reproduced live 2026-09-07, see module docstring).
"""
from __future__ import annotations

import json
import subprocess

import pytest

from engine.mart import finviz_short as FS

pytestmark = pytest.mark.unit


class _FakeCompleted:
    def __init__(self, stdout: str):
        self.stdout = stdout


def _runner(stdout: str):
    return lambda *a, **kw: _FakeCompleted(stdout)


def test_short_float_returns_the_fields_when_present():
    stdout = json.dumps({"ticker": "AAPL", "fundamentals": {
        "Short Float": "0.92%", "Short Ratio": "1.10", "Short Interest": "120.30M", "Market Cap": "4.6T"}})
    out = FS.short_float("AAPL", runner=_runner(stdout))
    assert out == {"available": True, "reason": None, "short_float": "0.92%",
                    "short_ratio": "1.10", "short_interest": "120.30M"}


def test_short_float_is_fail_soft_when_the_fields_are_absent_from_the_cli_output():
    """Reproduces the live `fz` regression: a real quote with only the 14-key fundamentals subset."""
    stdout = json.dumps({"ticker": "AAPL", "fundamentals": {
        "Book/sh": "7.36", "Market Cap": "4669.71B"}})
    out = FS.short_float("AAPL", runner=_runner(stdout))
    assert out["available"] is False
    assert "regression" in out["reason"] or "absent" in out["reason"]
    assert out["short_float"] is None and out["short_ratio"] is None and out["short_interest"] is None


def test_short_float_is_fail_soft_on_unparseable_json():
    out = FS.short_float("AAPL", runner=_runner("not json"))
    assert out["available"] is False
    assert "unparseable" in out["reason"]


def test_short_float_is_fail_soft_when_fz_is_missing():
    def runner(*a, **kw):
        raise FileNotFoundError("fz not found")
    out = FS.short_float("AAPL", runner=runner)
    assert out["available"] is False
    assert "PATH" in out["reason"]


def test_short_float_is_fail_soft_on_timeout():
    def runner(*a, **kw):
        raise subprocess.TimeoutExpired(cmd="fz", timeout=30)
    out = FS.short_float("AAPL", runner=runner)
    assert out["available"] is False
    assert "timed out" in out["reason"]


def test_short_float_is_fail_soft_on_nonzero_exit():
    def runner(*a, **kw):
        raise subprocess.CalledProcessError(returncode=2, cmd="fz", stderr="rate limited")
    out = FS.short_float("AAPL", runner=runner)
    assert out["available"] is False
    assert "rate limited" in out["reason"]


def test_parse_quote_raises_on_bad_json():
    with pytest.raises(ValueError):
        FS.parse_quote("{not json")
