"""Tests for `suppression_resolve.classify_missing` -- delisting vs vendor retraction.

Anchored on 2026-09-05, when BOTH INCONCLUSIVE suppression rows were labelled "delisted/halted?"
and NEITHER was delisted: CRNX had lost 25 contiguous interior sessions to a vendor retraction
(it traded through 09-02), and WBS served 13 bars over 07-17..08-20 with holes. Booking a
retraction as a delisting writes off recoverable evidence permanently.

`/calibration-audit` already carried the rule as prose -- "the delisting signature is a TRAILING
stop, never an interior hole" -- so the tool that produces the evidence now enforces it.
"""
from __future__ import annotations

import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))

import suppression_resolve as S  # noqa: E402

pytestmark = pytest.mark.unit

GRID = ["2026-08-03", "2026-08-04", "2026-08-05", "2026-08-06", "2026-08-07",
        "2026-08-10", "2026-08-11", "2026-08-12", "2026-08-13", "2026-08-14"]


def bars_for(dates):
    return [{"date": d, "adj": 100.0} for d in dates]


class TestClassifyMissing:

    def test_trailing_stop_with_no_interior_hole_is_a_delisting(self):
        # Arrange -- the name stops dead partway through the grid
        b = bars_for(GRID[:4])

        # Act
        kind, why = S.classify_missing(b, GRID, ["2026-08-04", "2026-08-13"])

        # Assert
        assert kind == "DELISTED"
        assert "trailing stop" in why

    def test_an_interior_hole_is_a_vendor_retraction(self):
        """CRNX's signature: bars resume after the gap, so the name never stopped trading."""
        b = bars_for([d for d in GRID if d not in ("2026-08-05", "2026-08-06", "2026-08-07")])
        kind, why = S.classify_missing(b, GRID, ["2026-08-05", "2026-08-14"])
        assert kind == "VENDOR_HOLE"
        assert "3 interior hole(s)" in why

    def test_a_delisted_name_that_also_has_interior_holes_is_not_called_a_delisting(self):
        """Ambiguous evidence must fail toward the recoverable reading, never write the row off."""
        b = bars_for(["2026-08-03", "2026-08-05", "2026-08-06"])
        kind, _ = S.classify_missing(b, GRID, ["2026-08-03", "2026-08-13"])
        assert kind == "VENDOR_HOLE"

    def test_every_inconclusive_row_carries_a_kind(self):
        """The old code emitted a bare 'delisted/halted?' string and nothing machine-readable."""
        for b, want in ((bars_for(GRID[:3]), "DELISTED"),
                        (bars_for([GRID[0], GRID[9]]), "VENDOR_HOLE")):
            kind, why = S.classify_missing(b, GRID, ["2026-08-13"])
            assert kind == want
            assert why
