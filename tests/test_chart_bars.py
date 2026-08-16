"""Data-integrity regression tests for scripts/chart.py `bars()`.

Anchored on two silent corruptions found by the 2026-08-15 calibration audit, both in the
shared Yahoo read path (`held_book.py`, `suppression_resolve.py`, every audit resolver):

1. Transient null closes. The chart API served `close: null` for individual sessions on
   liquid names, varying per REQUEST -- 115 tickers / 273 sessions in one pass. Re-fetching
   MSM returned real closes for exactly the two days the first fetch had blanked. Dropping
   the rows made 51 perfectly resolvable calls read INCONCLUSIVE, indistinguishable from
   windows that had not matured.

2. An unpropagated split. MNST 2:1 (effective 2026-08-11) still had `adjclose` == raw close
   on both sides four sessions later (90.36 -> 45.53), so any window crossing it would book
   a fake -50%.

The parsing/repair layer is pure, so all of this is tested without touching the network.
"""
from __future__ import annotations

import datetime as dt
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))

import chart as C  # noqa: E402

pytestmark = pytest.mark.unit


def _ts(date: str) -> int:
    """Yahoo serves epoch seconds; build them the same way `_parse` reads them."""
    return int(dt.datetime.strptime(date, "%Y-%m-%d").replace(tzinfo=dt.UTC).timestamp())


def payload(dates, closes, adj=None, splits=None):
    """A minimal chart-API `result` object: null closes are passed through as None."""
    n = len(dates)
    return {
        "timestamp": [_ts(d) for d in dates],
        "indicators": {
            "quote": [{"open": list(closes), "high": list(closes), "low": list(closes),
                       "close": list(closes), "volume": [1_000] * n}],
            "adjclose": [{"adjclose": list(adj if adj is not None else closes)}],
        },
        "events": {"splits": {
            str(i): {"date": _ts(s["date"]), "numerator": s["num"],
                     "denominator": s["den"], "splitRatio": s.get("ratio", "")}
            for i, s in enumerate(splits or [])}},
    }


class TestParse:
    """The session grid must survive blanked values -- that is what makes a hole detectable."""

    def test_grid_keeps_blanked_sessions_but_bars_drop_them(self):
        # Arrange
        res = payload(["2026-07-20", "2026-07-21", "2026-07-22", "2026-07-23"],
                      [370.60, None, None, 381.79])
        # Act
        by_date, grid, _ = C._parse(res)
        # Assert
        assert len(grid) == 4, "timestamp grid must retain null sessions"
        assert sorted(by_date) == ["2026-07-20", "2026-07-23"]

    def test_missing_adjclose_falls_back_to_raw_close(self):
        res = payload(["2026-07-20"], [10.0])
        del res["indicators"]["adjclose"]
        by_date, _, _ = C._parse(res)
        assert by_date["2026-07-20"]["adj"] == 10.0


class TestInteriorHoles:
    """Interior holes are retryable; a trailing stop is a delisting and must NOT be."""

    def test_detects_interior_hole(self):
        res = payload(["2026-07-20", "2026-07-21", "2026-07-22", "2026-07-23"],
                      [370.60, None, None, 381.79])
        by_date, grid, _ = C._parse(res)
        assert C._interior_holes(by_date, grid) == ["2026-07-21", "2026-07-22"]

    def test_trailing_gap_is_not_a_hole(self):
        # CPRX/TMHC/NUVL/GTLS delisted mid-window in cash mergers; Yahoo serves a stub.
        # Retrying those forever would paper over a genuine INCONCLUSIVE.
        res = payload(["2026-07-14", "2026-07-15", "2026-07-16"], [12.0, None, None])
        by_date, grid, _ = C._parse(res)
        assert C._interior_holes(by_date, grid) == []

    def test_leading_gap_is_not_a_hole(self):
        res = payload(["2026-07-14", "2026-07-15", "2026-07-16"], [None, None, 12.0])
        by_date, grid, _ = C._parse(res)
        assert C._interior_holes(by_date, grid) == []

    def test_dense_series_has_no_holes(self):
        res = payload(["2026-07-20", "2026-07-21"], [1.0, 2.0])
        by_date, grid, _ = C._parse(res)
        assert C._interior_holes(by_date, grid) == []


class TestSplitAdjustment:
    """The MNST case: adjclose lagging a fresh split fabricates a ~-50% move."""

    MNST_DATES = ["2026-08-06", "2026-08-07", "2026-08-11", "2026-08-12"]
    MNST_RAW = [94.16, 90.36, 45.53, 45.98]
    MNST_SPLIT = [{"date": "2026-08-11", "num": 2.0, "den": 1.0, "ratio": "2:1"}]

    def test_unadjusted_split_is_repaired(self):
        # Arrange -- adj == raw close on BOTH sides, which is the defect
        by_date, _, splits = C._parse(payload(self.MNST_DATES, self.MNST_RAW,
                                              adj=self.MNST_RAW, splits=self.MNST_SPLIT))
        # Act
        fixed = C._apply_splits(by_date, splits)
        # Assert -- pre-split halved, post-split untouched
        assert fixed["2026-08-07"]["adj"] == pytest.approx(45.18)
        assert fixed["2026-08-11"]["adj"] == pytest.approx(45.53)
        crossing = fixed["2026-08-11"]["adj"] / fixed["2026-08-07"]["adj"] - 1
        assert crossing == pytest.approx(0.00775, abs=1e-4), "a real ~+0.8% day, not -50%"

    def test_already_adjusted_split_is_left_alone(self):
        # CRWD 4:1 on 2026-07-02 was served correctly; re-scaling it would CREATE the bug.
        adj = [48.30, 48.50, 48.60, 49.00]
        by_date, _, splits = C._parse(payload(
            ["2026-07-01", "2026-07-02", "2026-07-03", "2026-07-06"], [193.18, 48.50, 48.60, 49.00],
            adj=adj, splits=[{"date": "2026-07-02", "num": 4.0, "den": 1.0, "ratio": "4:1"}]))
        fixed = C._apply_splits(by_date, splits)
        assert [fixed[d]["adj"] for d in sorted(fixed)] == adj

    def test_split_at_range_edge_is_skipped(self):
        by_date, _, splits = C._parse(payload(
            ["2026-08-11", "2026-08-12"], [45.53, 45.98],
            splits=[{"date": "2026-08-11", "num": 2.0, "den": 1.0, "ratio": "2:1"}]))
        assert C._apply_splits(by_date, splits) == by_date

    def test_raw_close_is_never_rewritten(self):
        """Only `adj` is back-adjusted; `close` stays the tape price."""
        by_date, _, splits = C._parse(payload(self.MNST_DATES, self.MNST_RAW,
                                              adj=self.MNST_RAW, splits=self.MNST_SPLIT))
        fixed = C._apply_splits(by_date, splits)
        assert fixed["2026-08-07"]["close"] == 90.36

    def test_does_not_mutate_its_input(self):
        by_date, _, splits = C._parse(payload(self.MNST_DATES, self.MNST_RAW,
                                              adj=self.MNST_RAW, splits=self.MNST_SPLIT))
        C._apply_splits(by_date, splits)
        assert by_date["2026-08-07"]["adj"] == 90.36


class TestBarsRetry:
    """`bars()` must merge a blanked session recovered on a later attempt."""

    def test_hole_filled_by_retry(self, monkeypatch):
        # Arrange -- first fetch blanks 07-21/07-22 (the observed GD response), retry serves them
        first = payload(["2026-07-20", "2026-07-21", "2026-07-22", "2026-07-23"],
                        [370.60, None, None, 381.79])
        second = payload(["2026-07-20", "2026-07-21", "2026-07-22", "2026-07-23"],
                         [370.60, 373.10, 377.40, 381.79])
        calls = []

        def fake(ticker, rng, host):
            calls.append(host)
            return first if len(calls) == 1 else second

        monkeypatch.setattr(C, "_fetch", fake)
        # Act
        out = C.bars("GD", "1y")
        # Assert
        assert [b["date"] for b in out] == ["2026-07-20", "2026-07-21", "2026-07-22", "2026-07-23"]
        assert out[1]["close"] == 373.10
        assert calls[:2] == ["query2", "query1"], "retry must rotate the host"

    def test_no_retry_when_series_is_dense(self, monkeypatch):
        calls = []

        def fake(ticker, rng, host):
            calls.append(host)
            return payload(["2026-07-20", "2026-07-21"], [1.0, 2.0])

        monkeypatch.setattr(C, "_fetch", fake)
        C.bars("SPY", "1y")
        assert len(calls) == 1, "a dense series must cost exactly one request"

    def test_retry_stops_at_max_tries(self, monkeypatch):
        calls = []

        def fake(ticker, rng, host):
            calls.append(host)
            return payload(["2026-07-20", "2026-07-21", "2026-07-22"], [1.0, None, 3.0])

        monkeypatch.setattr(C, "_fetch", fake)
        out = C.bars("GD", "1y")
        assert len(calls) == C.MAX_FETCH_TRIES
        assert [b["date"] for b in out] == ["2026-07-20", "2026-07-22"], "unfilled hole stays a gap"

    def test_failing_retry_does_not_lose_the_first_fetch(self, monkeypatch):
        def fake(ticker, rng, host):
            if host == "query2":
                return payload(["2026-07-20", "2026-07-21", "2026-07-22"], [1.0, None, 3.0])
            raise TimeoutError("upstream down")

        monkeypatch.setattr(C, "_fetch", fake)
        out = C.bars("GD", "1y")
        assert [b["date"] for b in out] == ["2026-07-20", "2026-07-22"]

    def test_bars_are_sorted_oldest_first_after_merge(self, monkeypatch):
        first = payload(["2026-07-20", "2026-07-21", "2026-07-22"], [1.0, None, 3.0])
        second = payload(["2026-07-20", "2026-07-21", "2026-07-22"], [1.0, 2.0, 3.0])
        seq = [first, second]
        monkeypatch.setattr(C, "_fetch", lambda t, r, h: seq.pop(0) if seq else second)
        out = C.bars("GD", "1y")
        assert [b["date"] for b in out] == sorted(b["date"] for b in out)
