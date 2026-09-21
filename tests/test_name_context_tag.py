"""D13: `context_read` on every disc-1.0 row is set by the writer from file mtimes, never by hand
(findings/stock-deep-dive DESIGN/70 §6)."""
from __future__ import annotations

import os
import time

import pytest

from engine.name import context_tag as CT

pytestmark = pytest.mark.unit


def _touch(path: str, mtime: float) -> None:
    with open(path, "w") as fh:
        fh.write("{}")
    os.utime(path, (mtime, mtime))


def test_no_prior_sheet_is_none(tmp_path):
    assert CT.context_read(str(tmp_path), call_time=time.time()) == "none"


def test_sheet_written_before_the_call_is_sheet_only(tmp_path):
    now = time.time()
    _touch(str(tmp_path / CT.SHEET_FILE), now - 60)
    assert CT.context_read(str(tmp_path), call_time=now) == "sheet_only"


def test_narration_written_before_the_call_is_narrate(tmp_path):
    now = time.time()
    _touch(str(tmp_path / CT.SHEET_FILE), now - 120)
    _touch(str(tmp_path / CT.NARRATE_FILE), now - 60)
    assert CT.context_read(str(tmp_path), call_time=now) == "narrate"


def test_a_sheet_written_after_the_call_does_not_count(tmp_path):
    now = time.time()
    _touch(str(tmp_path / CT.SHEET_FILE), now + 60)     # the writer is about to write it in this same run
    assert CT.context_read(str(tmp_path), call_time=now) == "none"


def test_narration_without_a_sheet_is_still_narrate(tmp_path):
    now = time.time()
    _touch(str(tmp_path / CT.NARRATE_FILE), now - 60)
    assert CT.context_read(str(tmp_path), call_time=now) == "narrate"


def test_values_are_the_frozen_set():
    from engine.config import CONTEXT_READ_VALUES
    assert CT.NONE in CONTEXT_READ_VALUES and CT.SHEET_ONLY in CONTEXT_READ_VALUES and CT.NARRATE in CONTEXT_READ_VALUES
