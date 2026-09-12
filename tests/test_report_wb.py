"""engine.report's "Watch basket" section (DESIGN/110-watch-basket.md §7 R2, item 5): the count
distribution lines, the LONG/SHORT/VOL tick tables, the CONFLICT count, and the fixed read
sentence. Built from a real `engine.watch.nightly.nightly` state (synthetic `evaluate_fn`, no
mart/network) so a key the nightly adds and the renderer ignores would still show up missing from
the text, not silently dropped."""
from __future__ import annotations

from datetime import date

import pytest

from engine import report as R
from engine.watch import nightly as N
from test_watch_nightly import CONFLICT_IDS, LONG_IDS, SHORT_IDS, _cond_row, _evaluate_fn

pytestmark = pytest.mark.unit

D0 = date(2026, 6, 9)


def _base_signals(wb_state):
    return {"date": D0.isoformat(), "season": "off", "preflight": {"ok": True, "warnings": []},
            "candidates": [], "suppressed": [], "graded": [], "season_running": [], "ledger": {},
            "sb_state": None, "watch_basket": wb_state}


def test_render_includes_the_watch_basket_header_and_fixed_sentence(tmp_path):
    wb = N.nightly(None, D0, force_ledger=True, ledger_dir=str(tmp_path),
                   evaluate_fn=_evaluate_fn([_cond_row("LONGCO", D0, LONG_IDS)]))
    text = R.render(_base_signals(wb))
    assert "## Watch basket (wb-1.0, exploration, paper only)" in text
    assert R.WB_READ_SENTENCE in text
    assert "nothing here is a trade" in text


def test_render_wb_shows_long_short_vol_tables_with_a_tick_per_condition(tmp_path):
    rows = [_cond_row("LONGCO", D0, LONG_IDS), _cond_row("SHORTCO", D0, SHORT_IDS)]
    wb = N.nightly(None, D0, force_ledger=True, ledger_dir=str(tmp_path), evaluate_fn=_evaluate_fn(rows))
    text = R.render_wb(wb)
    assert "### LONG (1)" in text and "### SHORT (1)" in text and "### VOL (0)" in text
    assert "LONGCO" in text and "SHORTCO" in text
    # a tick column per condition id, e.g. C-HIGH is true for LONGCO
    assert "C-HIGH" in text and "C-SWING" in text
    # the new anchored-POC pair (DESIGN/110 §2) shows up too -- report.py iterates ALL_CONDITIONS
    # dynamically, so no renderer edit was needed for it
    assert "C-POC-A" in text and "C-POC-A-LOSS" in text
    assert "CONFLICT (logged only, never a basket, DESIGN/110 §3): 0." in text


def test_render_wb_reports_conflict_count_without_a_ledger_row(tmp_path):
    wb = N.nightly(None, D0, force_ledger=True, ledger_dir=str(tmp_path),
                   evaluate_fn=_evaluate_fn([_cond_row("CFLCO", D0, CONFLICT_IDS)]))
    text = R.render_wb(wb)
    assert "CONFLICT (logged only, never a basket, DESIGN/110 §3): 1." in text
    assert "CFLCO" not in text.split("CONFLICT (logged only")[0].split("### VOL")[-1]


def test_render_wb_shows_ledger_counts_and_open_state(tmp_path):
    wb = N.nightly(None, D0, force_ledger=True, ledger_dir=str(tmp_path),
                   evaluate_fn=_evaluate_fn([_cond_row("LONGCO", D0, LONG_IDS)]))
    text = R.render_wb(wb)
    assert "Ledger: emitted 1 (skipped 0), graded 0; ledger open." in text


def test_render_wb_before_open_date_says_closed(tmp_path):
    wb = N.nightly(None, D0, force_ledger=False, ledger_dir=str(tmp_path),
                   evaluate_fn=_evaluate_fn([_cond_row("LONGCO", D0, LONG_IDS)]))
    text = R.render_wb(wb)
    assert "CLOSED (before 2026-09-08; nothing written)" in text


def test_render_wb_unavailable_shows_the_reason(tmp_path):
    def boom(d):
        raise RuntimeError("synthetic failure")
    wb = N.nightly(None, D0, force_ledger=True, ledger_dir=str(tmp_path), evaluate_fn=boom)
    text = R.render_wb(wb)
    assert "unavailable" in text and "synthetic failure" in text


def test_render_wb_no_state_at_all():
    assert "step not run" in R.render_wb(None)


def test_render_without_watch_basket_key_omits_the_section_gracefully():
    # d1.0/d1.1-shaped documents: no "watch_basket" key at all
    signals = {**_base_signals(None)}
    del signals["watch_basket"]
    text = R.render(signals)
    assert "## Watch basket" in text
    assert "step not run" in text


def test_wb_borrow_line_names_exact_fallback_and_missing_snapshots():
    from engine.report import _wb_borrow_line
    assert "the session's own" in _wb_borrow_line({"asof": "2026-09-11", "stale_days": 0, "names_with_fee": 900})
    assert "fallback, 1 day old" in _wb_borrow_line({"asof": "2026-09-10", "stale_days": 1, "names_with_fee": 812})
    assert "fallback, 3 days old" in _wb_borrow_line({"asof": "2026-09-08", "stale_days": 3, "names_with_fee": 5})
    assert "none within the fallback window" in _wb_borrow_line({"asof": None, "stale_days": None, "names_with_fee": 0})
    assert "pre-d1.5" in _wb_borrow_line(None)
