"""Tests for scripts/resolved_ledger.py -- the durable resolved-call ledger.

Anchored on the 2026-08-22 calibration audit: EQR (OI_FADE, signalled 2026-07-09) resolved
cleanly at the 08-15 audit, and by 08-22 Yahoo had RETRACTED 11 sessions it previously served
(2026-07-23 -> 08-10), persistently across both hosts and both query forms. The 08-21 truth-set
rebuild inherited the gap. The call therefore un-resolved itself: OI_FADE's forward book shrank
81 -> 80 cluster-units with no code change and no new information.

Re-deriving a matured excess from a live vendor feed is NOT idempotent. Once a window has
matured and been measured, that measurement is the record.
"""
from __future__ import annotations

import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))

import resolved_ledger as L  # noqa: E402

pytestmark = pytest.mark.unit


def row(rd="2026-07-09", tk="EQR", lane="OI_FADE", h=10, status="RESOLVED", exc=1.23, **kw):
    return {"report_date": rd, "ticker": tk, "lane": lane, "horizon": h,
            "T1_status": status, "T1_excess_pct": exc,
            "T1_entry": kw.get("entry", "2026-07-10"), "T1_exit": kw.get("exit", "2026-07-24")}


class TestKeying:
    def test_key_is_stable_across_reruns(self):
        assert L.key(row()) == L.key(row())

    def test_key_separates_horizons_of_the_same_signal(self):
        assert L.key(row(h=5)) != L.key(row(h=10))


class TestMerge:
    def test_new_resolved_row_is_recorded(self):
        led, conflicts = L.merge({}, [row()])
        assert L.key(row()) in led
        assert conflicts == []

    def test_unresolved_row_is_not_recorded(self):
        led, _ = L.merge({}, [row(status="OPEN")])
        assert led == {}, "only matured measurements enter the ledger"

    def test_does_not_mutate_the_input_ledger(self):
        before = {}
        L.merge(before, [row()])
        assert before == {}, "merge must return a new ledger, never mutate"

    def test_agreeing_rerun_is_not_a_conflict(self):
        led, _ = L.merge({}, [row()])
        led2, conflicts = L.merge(led, [row()])
        assert conflicts == []
        assert led2 == led


class TestVendorRetraction:
    """The EQR case: a row that WAS resolved comes back unresolvable."""

    def test_retracted_row_keeps_its_recorded_value(self):
        led, _ = L.merge({}, [row(exc=1.23)])
        led2, conflicts = L.merge(led, [row(status="INCONCLUSIVE", exc=None)])
        assert led2[L.key(row())]["T1_excess_pct"] == 1.23, "the measurement stands"
        assert len(conflicts) == 1
        assert conflicts[0]["kind"] == "RETRACTED"

    def test_retraction_is_reported_not_silent(self):
        led, _ = L.merge({}, [row()])
        _, conflicts = L.merge(led, [row(status="INCONCLUSIVE", exc=None)])
        assert "EQR" in conflicts[0]["key"]

    def test_changed_value_keeps_the_first_measurement_and_flags(self):
        led, _ = L.merge({}, [row(exc=1.23)])
        led2, conflicts = L.merge(led, [row(exc=9.99)])
        assert led2[L.key(row())]["T1_excess_pct"] == 1.23, "first matured measurement wins"
        assert conflicts[0]["kind"] == "CHANGED"
        assert conflicts[0]["was"] == 1.23 and conflicts[0]["now"] == 9.99

    def test_rounding_noise_is_not_flagged_as_changed(self):
        # The 08-22 audit saw one row move by 0.0001pp across a resolver swap; that is not
        # a retraction and must not spam the conflict report.
        led, _ = L.merge({}, [row(exc=-7.7649)])
        _, conflicts = L.merge(led, [row(exc=-7.7648)])
        assert conflicts == []


class TestApply:
    """`apply` is what an audit calls: fresh rows in, ledger-backed rows out."""

    def test_restores_a_retracted_row_into_the_audit_book(self):
        led, _ = L.merge({}, [row(exc=1.23)])
        fresh = [row(status="INCONCLUSIVE", exc=None)]
        out, conflicts = L.apply(led, fresh)
        assert out[0]["T1_status"] == "RESOLVED"
        assert out[0]["T1_excess_pct"] == 1.23
        assert out[0]["from_ledger"] is True
        assert len(conflicts) == 1

    def test_leaves_genuinely_open_rows_alone(self):
        out, conflicts = L.apply({}, [row(status="OPEN", exc=None)])
        assert out[0]["T1_status"] == "OPEN"
        assert conflicts == []

    def test_does_not_mutate_the_fresh_rows(self):
        led, _ = L.merge({}, [row(exc=1.23)])
        fresh = [row(status="INCONCLUSIVE", exc=None)]
        L.apply(led, fresh)
        assert fresh[0]["T1_status"] == "INCONCLUSIVE"


def sup_row(period="2026-W33", rd="2026-08-14", tk="CRNX", lane="MOM_LONG", h=10,
            status="RESOLVED", exc=-3.21, **kw):
    """A `suppression_resolve.py` row -- the SAME problem, different field names."""
    return {"period": period, "report_date": rd, "ticker": tk, "lane": lane, "horizon": h,
            "status": status, "excess_pct": exc, "gate_correct": (exc or 0) < 0,
            "entry": kw.get("entry", "2026-08-17"), "exit": kw.get("exit", "2026-08-31")}


class TestSuppressionSchema:
    """Suppressions were uncovered until 2026-09-05, and the gap bit.

    CRNX lost 25 contiguous sessions to a vendor retraction that cycle. Its four `calls[]` rows
    were restored from the call ledger; its suppression row had no such record and vanished from
    the gate-effectiveness cohort. A gate that suppresses its own evidence cannot also afford to
    lose it to the feed.
    """

    def test_a_matured_suppression_survives_a_later_retraction(self):
        # Arrange -- the measurement was taken while the feed still served the bars
        led, _ = L.merge({}, [sup_row(exc=-3.21)], L.SUPPRESSION)

        # Act -- a later cycle cannot resolve it at all
        fresh = [sup_row(status="INCONCLUSIVE", exc=None)]
        out, conflicts = L.apply(led, fresh, L.SUPPRESSION)

        # Assert -- the recorded measurement IS the record
        assert out[0]["status"] == "RESOLVED"
        assert out[0]["excess_pct"] == -3.21
        assert out[0]["gate_correct"] is True
        assert out[0]["from_ledger"] is True
        assert [c["kind"] for c in conflicts] == ["RETRACTED"]

    def test_only_resolved_suppressions_enter_the_ledger(self):
        led, conflicts = L.merge({}, [sup_row(status="OPEN", exc=None)], L.SUPPRESSION)
        assert led == {}
        assert conflicts == []

    def test_period_is_part_of_the_identity(self):
        """A weekly and a daily envelope can suppress the same name+lane in the same week."""
        led, _ = L.merge({}, [sup_row(period="2026-W33"), sup_row(period="2026-08-14")],
                         L.SUPPRESSION)
        assert len(led) == 2

    def test_suppression_keys_cannot_collide_with_call_keys(self):
        call_k = L.key({"report_date": "2026-08-14", "ticker": "CRNX",
                        "lane": "MOM_LONG", "horizon": 10})
        sup_k = L.key(sup_row(), L.SUPPRESSION)
        assert call_k != sup_k
        assert sup_k.startswith("sup|")

    def test_call_keys_are_unchanged_by_the_schema_split(self):
        """The 475-row call ledger on disk must stay addressable."""
        assert L.key({"report_date": "2026-07-09", "ticker": "EQR",
                      "lane": "OI_FADE", "horizon": 10}) == "2026-07-09|EQR|OI_FADE|10"

    def test_a_disagreeing_re_derivation_is_reported_not_overwritten(self):
        led, _ = L.merge({}, [sup_row(exc=-3.21)], L.SUPPRESSION)
        led2, conflicts = L.merge(led, [sup_row(exc=+1.00)], L.SUPPRESSION)
        assert [c["kind"] for c in conflicts] == ["CHANGED"]
        assert led2[L.key(sup_row(), L.SUPPRESSION)]["excess_pct"] == -3.21
