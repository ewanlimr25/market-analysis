"""Verdict/status disposition for held_book.

Regression test for the substring-matching bug that hid a live position twice
(2026-07-31 and 2026-08-03: `HOLD_TO_BINDING_EXIT` contains "EXIT", so PLNT was filtered
out as closed and the tool reported "no open positions" on the final session of its h10
window).

Every string below is a verdict or status that ACTUALLY appears in the tracked
`analyses/*/*/conviction_*.json` panel -- this pins the real vocabulary, not an invented one.
"""
from __future__ import annotations

import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))

from held_book import _head, _is_closed, _positions  # noqa: E402

# (verdict, still_open) -- observed in the panel as of 2026-08-03
OPEN_VERDICTS = ["HOLD", "HOLD_TRIMMED_50PCT", "HOLD_TO_BINDING_EXIT"]
CLOSED_VERDICTS = ["CLOSED_CONFIRMED", "CLOSED_ON_TIME_STOP", "EXIT", "CUT/TRIM",
                   "CUT", "CUT_CONFIRMED", "DROPPED_CONFIRMED", "CLOSE"]
OPEN_STATUSES = ["LIVE"]
CLOSED_STATUSES = ["CLOSED", "CLOSED_PRIOR_SESSION", "CLOSED_RETROACTIVE_RECONCILIATION"]


@pytest.mark.unit
@pytest.mark.parametrize("verdict", OPEN_VERDICTS)
def test_open_verdicts_are_not_filtered(verdict: str) -> None:
    assert not _is_closed({"verdict": verdict}), f"{verdict} is a live position"


@pytest.mark.unit
@pytest.mark.parametrize("verdict", CLOSED_VERDICTS)
def test_closed_verdicts_are_filtered(verdict: str) -> None:
    assert _is_closed({"verdict": verdict}), f"{verdict} is closed"


@pytest.mark.unit
@pytest.mark.parametrize("status", OPEN_STATUSES)
def test_open_statuses_are_not_filtered(status: str) -> None:
    assert not _is_closed({"status": status})


@pytest.mark.unit
@pytest.mark.parametrize("status", CLOSED_STATUSES)
def test_closed_statuses_are_filtered(status: str) -> None:
    assert _is_closed({"status": status})


@pytest.mark.unit
def test_the_exact_bug_that_hid_plnt() -> None:
    """The 2026-08-03 PLNT record must reconcile as OPEN, not be silently dropped."""
    doc = {"held_position_reconciliation": {"positions": [
        {"ticker": "PLNT", "verdict": "HOLD_TO_BINDING_EXIT", "direction": "short"},
    ]}}
    open_p, closed_p = _positions(doc)
    assert [p["ticker"] for p in open_p] == ["PLNT"]
    assert closed_p == []


@pytest.mark.unit
def test_unknown_verdict_fails_toward_visibility() -> None:
    """An unrecognized/missing verdict must stay OPEN -- hiding a live position is the
    unrecoverable failure, showing a closed one is not."""
    doc = {"held_position_reconciliation": {"positions": [
        {"ticker": "AAA", "verdict": "SOMETHING_NEW"},
        {"ticker": "BBB"},
        {"ticker": "CCC", "verdict": None},
    ]}}
    open_p, closed_p = _positions(doc)
    assert [p["ticker"] for p in open_p] == ["AAA", "BBB", "CCC"]
    assert closed_p == []


@pytest.mark.unit
def test_a_closing_status_overrides_a_hold_verdict() -> None:
    doc = {"held_position_reconciliation": {"positions": [
        {"ticker": "AAA", "verdict": "HOLD", "status": "CLOSED_PRIOR_SESSION"},
    ]}}
    open_p, closed_p = _positions(doc)
    assert open_p == []
    assert [p["ticker"] for p in closed_p] == ["AAA"]


@pytest.mark.unit
@pytest.mark.parametrize("raw,expected", [
    ("CUT/TRIM", "CUT"), ("HOLD_TO_BINDING_EXIT", "HOLD"), ("HOLD_TRIMMED_50PCT", "HOLD"),
    ("CLOSED_ON_TIME_STOP", "CLOSED"), ("  hold  ", "HOLD"), ("", ""), (None, ""),
    ("50PCT_TRIM", ""),
])
def test_head_tokenization(raw: object, expected: str) -> None:
    assert _head(raw) == expected


@pytest.mark.unit
def test_missing_reconciliation_block_is_empty_not_an_error() -> None:
    assert _positions({}) == ([], [])
    assert _positions({"held_position_reconciliation": None}) == ([], [])
    assert _positions({"held_position_reconciliation": {"positions": None}}) == ([], [])
