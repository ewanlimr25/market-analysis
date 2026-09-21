"""DESIGN/70 §7-§9: the sheet end to end on the stored fixtures -- schema-valid, re-derivable offline,
ledger rows write-once, `context_read` from what existed before the call."""
from __future__ import annotations

import json
import os
import shutil
import time
from datetime import date

import pytest

import name_fixtures
from engine import ledger as L
from engine.name import sheet as SH

pytestmark = pytest.mark.unit

D = date(2026, 9, 18)


def _public(doc: dict) -> dict:
    return {k: v for k, v in doc.items() if not k.startswith("_")}


def _stage(tmp_path, ticker: str) -> str:
    """Copy the fixture's inputs to where `run` looks for them; returns the out_root."""
    root = tmp_path / "analyses"
    dst = root / ticker / D.isoformat() / SH.INPUTS_DIR
    shutil.copytree(name_fixtures.fixture_dir(ticker), dst)
    return str(root)


@pytest.mark.parametrize("ticker", name_fixtures.FIXTURE_TICKERS)
def test_every_fixture_builds_a_schema_valid_sheet(ticker):
    doc = SH.build(name_fixtures.load_fixture(ticker), direction=None)
    assert SH.validate(doc) == []
    assert doc["schema"] == "n1.0" and doc["ticker"] == ticker and doc["date"] == D.isoformat()


def test_the_liquid_name_writes_a_sheet_row_and_the_thin_one_none():
    nvda = SH.build(name_fixtures.load_fixture("NVDA"), direction=None)
    assert [r["gate_verdict"] for r in nvda["ledger_rows"]] == ["F3"] and nvda["liquidity"]["can_price"]
    bl = SH.build(name_fixtures.load_fixture("BL"), direction=None)
    assert bl["ledger_rows"] == [] and bl["structures"] == [] and bl["liquidity"]["failing"] == "L3"


def test_a_direction_adds_the_two_disc_rows_and_the_context_tag():
    doc = SH.build(name_fixtures.load_fixture("NVDA"), direction="long", context_read="narrate")
    kinds = [(r["policy_id"], r["structure"]) for r in doc["ledger_rows"]]
    assert kinds == [("sheet-1.0", "IB"), ("disc-1.0", "SHARES"), ("disc-1.0", "DEBIT_VERTICAL")]
    assert doc["context_read"] == "narrate" and all(r["context_read"] == "narrate" for r in doc["_rows"][1:])
    assert SH.validate(doc) == []


def test_run_is_offline_reproducible_and_write_once(tmp_path):
    root = _stage(tmp_path, "NVDA")
    ledger = str(tmp_path / "ledger")
    first = SH.run("NVDA", D, offline=True, out_root=root, ledger_dir=ledger)
    out_dir = os.path.join(root, "NVDA", D.isoformat())
    assert set(os.listdir(out_dir)) >= {"ticker.json", "report.md", "inputs"}
    on_disk = json.load(open(os.path.join(out_dir, "ticker.json")))
    assert on_disk == _public(first)
    assert len(L.read_signals(ledger)) == 1 and first["ledger_rows"][0]["written"] is True
    second = SH.run("NVDA", D, offline=True, out_root=root, ledger_dir=ledger)
    a, b = _public(first), _public(second)
    for k in ("generated", "ledger_rows", "context_read"):           # the tag sees the first sheet, by design
        a.pop(k), b.pop(k)
    assert a == b                                                    # same inputs -> same sheet
    assert len(L.read_signals(ledger)) == 1 and second["ledger_rows"][0]["written"] is False


def test_context_read_is_decided_before_the_run_writes(tmp_path):
    root = _stage(tmp_path, "NVDA")
    ledger = str(tmp_path / "ledger")
    no_sheet = SH.run("NVDA", D, direction="long", offline=True, out_root=root, ledger_dir=ledger)
    assert no_sheet["context_read"] == "none"
    time.sleep(0.01)
    after = SH.run("NVDA", D, direction="short", offline=True, out_root=root, ledger_dir=ledger)
    assert after["context_read"] == "sheet_only"
    rows = L.read_signals(ledger)
    assert sorted(rows[rows.policy_id == "disc-1.0"]["context_read"].unique()) == ["none", "sheet_only"]


def test_an_invalid_document_is_a_hard_error(tmp_path):
    doc = SH.build(name_fixtures.load_fixture("BL"), direction=None)
    with pytest.raises(SH.SheetValidationError):
        SH.write({**doc, "premium": {**doc["premium"], "verdict": "MAYBE"}}, str(tmp_path))
    assert not os.path.exists(tmp_path / "ticker.json")
