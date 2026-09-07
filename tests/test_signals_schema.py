"""U2 (findings DESIGN/95 §5, D20): `signals.json` is stamped, strict JSON, and validates against
schemas/signals.schema.json. The document is assembled through `engine.daily.assemble` from rows the
real builders produce (S-A via `sa.evaluate_event` / `grade_rows`, S-B via `sb_daily.run`), so a key
the builders add and the schema lacks fails here before it fails on a real night."""
from __future__ import annotations

import glob
import json
import os
import subprocess
import sys
from datetime import date

import numpy as np
import pandas as pd
import pytest

from engine import daily as D
from engine import ledger as L
from engine import marking as M
from engine import portfolio
from engine import sb_daily as SD
from engine import schema as SCH
from engine.config import REPO, SA_PARAMS, SIZING
from engine.strategies import sa
from engine.watch import nightly as WBN
from test_sa_strategy import _event, _model_inputs, _post_rows, _pre_rows, _resolver
from test_sb_strategy import ENTRY, EXP, _index_vol, _rows
from test_watch_nightly import LONG_IDS, _cond_row, _evaluate_fn

pytestmark = pytest.mark.unit

SESSION = date(2026, 7, 29)
STRICT = dict(parse_constant=lambda c: (_ for _ in ()).throw(ValueError(f"non-finite {c}")))


def _walk(node, path="#"):
    if isinstance(node, dict):
        yield path, node
        for k, v in node.items():
            yield from _walk(v, f"{path}/{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from _walk(v, f"{path}/{i}")


def test_every_object_in_the_schema_is_closed():
    schema = SCH.load_schema()
    assert schema["properties"]["schema_version"] == {"enum": list(SCH.SCHEMA_VERSIONS)} and SCH.SCHEMA_VERSION == SCH.SCHEMA_VERSIONS[-1]
    assert schema["properties"]["report_kind"] == {"const": SCH.REPORT_KIND}
    open_objects = [p for p, node in _walk(schema) if node.get("type") == "object" and "additionalProperties" not in node]
    assert open_objects == [], f"objects without additionalProperties: {open_objects}"


def test_committed_daily_outputs_validate_and_parse_strictly():
    files = sorted(glob.glob(os.path.join(REPO, "analyses", "daily", "*", "signals.json")))
    assert files, "no committed nightly output found"
    for path in files:
        with open(path) as fh:
            signals = json.load(fh, **STRICT)
        assert SCH.validate(signals) == [], path
        assert signals["schema_version"] in SCH.SCHEMA_VERSIONS and signals["report_kind"] == SCH.REPORT_KIND


# ---- a full document from the real builders ------------------------------------------------------

def _sa_pieces(tmp):
    entry_only = sa.evaluate_event(_event(), _pre_rows(), _resolver(), SA_PARAMS, SIZING, with_exit=False)
    cands = portfolio.apply_caps(pd.DataFrame(entry_only.trades), SIZING)
    suppressed = pd.DataFrame(sa.evaluate_event(_event(sector="Technology"), _pre_rows(), _resolver(), SA_PARAMS, SIZING,
                                                with_exit=False).suppressed)
    unmarkable = sa.evaluate_event(_event(), _pre_rows(), M.MarkResolver({}, lambda *a: None), SA_PARAMS, SIZING, with_exit=False)
    L.emit(tmp, cands, SESSION)
    stored = L.read_signals(tmp).assign(post=pd.Timestamp("2026-07-30"))
    post_rows = {(r["option_chain_id"], r["date"]): r for r in _post_rows().to_dict("records")}
    graded, _ = D.grade_rows(stored, M.MarkResolver(post_rows, _model_inputs))
    _, dropped_grade = D.grade_rows(stored, M.MarkResolver({}, lambda *a: None))
    run = sa.RunResult(cands, suppressed, pd.DataFrame(unmarkable.dropped))
    ledger = graded.assign(season="S2")
    return run, graded, dropped_grade, D.season_running(ledger, "S2")


def _sb_state(tmp, when):
    def rows_loader(con, underlyings, d):
        return _rows().assign(underlying_symbol="SPY") if d == ENTRY else pd.DataFrame()
    def close_loader(con, ticker, d):
        return {("SPY", EXP): 92.0}.get((ticker, d))
    state = SD.run(None, when, tmp, _index_vol(), rows_loader, close_loader, force_ledger=True)
    return {**state, "refresh": {"ok": True, "through": when.isoformat()}}


def _preflight_ok():
    return {"date": SESSION.isoformat(), "panel": {"All Options": {"present": True, "rows": 12},
                                                  "Dark pool": {"present": False, "rows": None}},
            "truth_set": {"prices": {"max_date": SESSION.isoformat(), "stale_vs_trade_date": False},
                          "features": {"max_date": None}},
            "ok": False, "warnings": ["Dark pool: no export"]}


def test_full_nightly_document_from_real_builders_validates(tmp_path):
    run, graded, dropped_grade, running = _sa_pieces(str(tmp_path / "sa"))
    assert len(run.trades) == 4 and len(run.suppressed) == 1 and len(run.dropped) == 1 and len(graded) == 4
    assert len(dropped_grade) == 4 and len(running) == 4
    sb_entry = _sb_state(str(tmp_path / "sb"), ENTRY)
    sb_expiry = _sb_state(str(tmp_path / "sb"), EXP)
    assert len(sb_entry["candidates"]) == 2 and len(sb_entry["exploration"]) == 2          # champion + exploration book (DESIGN/100)
    assert len(sb_expiry["graded"]) == 4 and len(sb_expiry["running"]) == 4
    counts = {"emitted": 4, "skipped": 0, "graded": 4, "ledger_open": True}
    for sb in (sb_entry, sb_expiry):
        doc = D.assemble(SESSION, _preflight_ok(), {"daily_contract_rows": 1, "earnings_events_rows": 0},
                         run, graded, dropped_grade, running, counts, sb)
        assert SCH.validate(doc) == []
        text = SCH.dumps(doc)
        assert SCH.validate(json.loads(text, **STRICT)) == []
    assert list(doc)[:2] == ["schema_version", "report_kind"]
    assert {c["contracts"] for c in doc["candidates"]} and "n" not in doc["candidates"][0]
    assert doc["sb_state"]["running"][0]["n"] == 1                     # a count, kept as `n`


# ---- d1.4: C-POC-A/C-POC-A-LOSS widen watch_basket.count_distribution to 0..8 (DESIGN/110 §2/§8) --

def test_schema_version_defaults_to_d1_4_and_earlier_docs_stay_valid():
    assert SCH.SCHEMA_VERSION == "d1.4" and SCH.SCHEMA_VERSIONS == ("d1.0", "d1.1", "d1.2", "d1.3", "d1.4")
    for old in ("d1.0", "d1.1", "d1.2", "d1.3"):
        # a document from before the watch basket existed: no `watch_basket` key at all
        base = {"schema_version": old, "report_kind": SCH.REPORT_KIND, "date": SESSION.isoformat(), "season": "S2",
                "preflight": {"ok": True, "warnings": []}, "mart": {"daily_contract_rows": 0, "earnings_events_rows": 0},
                "candidates": [], "suppressed": [], "dropped": [], "graded": [], "season_running": [],
                "ledger": {"emitted": 0, "skipped": 0, "graded": 0, "ledger_open": False},
                "sb_state": {"date": SESSION.isoformat(), "gate": {}, "candidates": [], "graded": [], "refresh": {"ok": True}}}
        assert SCH.validate(base) == []


def test_a_d1_2_shaped_bull_distribution_without_key_7_still_validates():
    """A genuine pre-C-DIV-D d1.2 document's `count_distribution.bull` only ever had keys "0".."6"
    (`SIGN_PLUS` was 6 long); the widened d1.3 bound must not retroactively require a "7" that
    document never had."""
    old_bull = {str(i): 0 for i in range(7)}
    assert set(old_bull) == {"0", "1", "2", "3", "4", "5", "6"}
    wb = {"available": True, "reason": None, "universe_n": 0,
          "count_distribution": {"bull": old_bull, "bear": {str(i): 0 for i in range(8)}},
          "top_bull": [], "top_bear": [], "long": [], "short": [], "vol": [], "conflict": [],
          "ledger_open": False, "wb_emitted": 0, "wb_skipped": 0, "wb_graded": 0, "elapsed_s": 0.1}
    base = {"schema_version": "d1.2", "report_kind": SCH.REPORT_KIND, "date": SESSION.isoformat(), "season": "S2",
            "preflight": {"ok": True, "warnings": []}, "mart": {"daily_contract_rows": 0, "earnings_events_rows": 0},
            "candidates": [], "suppressed": [], "dropped": [], "graded": [], "season_running": [],
            "ledger": {"emitted": 0, "skipped": 0, "graded": 0, "ledger_open": False},
            "sb_state": {"date": SESSION.isoformat(), "gate": {}, "candidates": [], "graded": [], "refresh": {"ok": True}},
            "watch_basket": wb}
    assert SCH.validate(base) == []


def test_a_d1_3_shaped_bull_and_bear_distribution_without_key_8_still_validates():
    """A genuine pre-C-POC-A d1.3 document's `count_distribution.bull`/`.bear` only ever had keys
    "0".."7" (`SIGN_PLUS`/`SIGN_MINUS` were 7 long each); the widened d1.4 bound must not
    retroactively require an "8" that document never had."""
    old_dist = {str(i): 0 for i in range(8)}
    assert set(old_dist) == {"0", "1", "2", "3", "4", "5", "6", "7"}
    wb = {"available": True, "reason": None, "universe_n": 0,
          "count_distribution": {"bull": old_dist, "bear": dict(old_dist)},
          "top_bull": [], "top_bear": [], "long": [], "short": [], "vol": [], "conflict": [],
          "ledger_open": False, "wb_emitted": 0, "wb_skipped": 0, "wb_graded": 0, "elapsed_s": 0.1}
    base = {"schema_version": "d1.3", "report_kind": SCH.REPORT_KIND, "date": SESSION.isoformat(), "season": "S2",
            "preflight": {"ok": True, "warnings": []}, "mart": {"daily_contract_rows": 0, "earnings_events_rows": 0},
            "candidates": [], "suppressed": [], "dropped": [], "graded": [], "season_running": [],
            "ledger": {"emitted": 0, "skipped": 0, "graded": 0, "ledger_open": False},
            "sb_state": {"date": SESSION.isoformat(), "gate": {}, "candidates": [], "graded": [], "refresh": {"ok": True}},
            "watch_basket": wb}
    assert SCH.validate(base) == []


def test_document_with_a_real_watch_basket_state_validates(tmp_path):
    run, graded, dropped_grade, running = _sa_pieces(str(tmp_path / "sa"))
    sb = _sb_state(str(tmp_path / "sb"), ENTRY)
    counts = {"emitted": 0, "skipped": 0, "graded": 0, "ledger_open": False}
    rows = [_cond_row("LONGCO", SESSION, LONG_IDS)]
    wb = WBN.nightly(None, SESSION, force_ledger=True, ledger_dir=str(tmp_path / "wb"), evaluate_fn=_evaluate_fn(rows))
    assert wb["available"] is True and wb["wb_emitted"] == 1
    doc = D.assemble(SESSION, _preflight_ok(), {"daily_contract_rows": 1, "earnings_events_rows": 0},
                     run, graded, dropped_grade, running, counts, sb, wb)
    assert doc["schema_version"] == "d1.4"
    assert SCH.validate(doc) == []
    text = SCH.dumps(doc)
    assert SCH.validate(json.loads(text, **STRICT)) == []
    assert doc["watch_basket"]["long"][0]["ticker"] == "LONGCO"
    assert set(doc["watch_basket"]["count_distribution"]["bull"]) == {str(i) for i in range(9)}
    assert set(doc["watch_basket"]["count_distribution"]["bear"]) == {str(i) for i in range(9)}


def test_watch_basket_unavailable_shape_validates():
    wb = WBN.nightly(None, SESSION, force_ledger=True, ledger_dir="/nonexistent",
                     evaluate_fn=lambda d: (_ for _ in ()).throw(RuntimeError("boom")))
    assert wb["available"] is False
    empty = sa.RunResult(pd.DataFrame(), pd.DataFrame(), pd.DataFrame())
    counts = {"emitted": 0, "skipped": 0, "graded": 0, "ledger_open": False}
    sb_error = {"date": SESSION.isoformat(), "error": "S-B step failed: boom", "candidates": [], "graded": [], "gate": {},
                "refresh": {"ok": False, "error": "timeout"}}
    doc = D.assemble(SESSION, {"ok": False, "warnings": ["preflight failed: timeout"]}, {"daily_contract_rows": 0, "earnings_events_rows": 0},
                     empty, pd.DataFrame(), pd.DataFrame(), [], counts, sb_error, wb)
    assert SCH.validate(doc) == []


def test_watch_basket_omitted_keeps_the_document_valid(tmp_path):
    """`wb_state=None` (the default): no `watch_basket` key at all, still a valid document."""
    run, graded, dropped_grade, running = _sa_pieces(str(tmp_path / "sa"))
    counts = {"emitted": 0, "skipped": 0, "graded": 0, "ledger_open": False}
    doc = D.assemble(SESSION, _preflight_ok(), {"daily_contract_rows": 1, "earnings_events_rows": 0},
                     run, graded, dropped_grade, running, counts, _sb_state(str(tmp_path / "sb"), ENTRY))
    assert "watch_basket" not in doc
    assert SCH.validate(doc) == []


def test_failure_shapes_validate(tmp_path):
    empty = sa.RunResult(pd.DataFrame(), pd.DataFrame(), pd.DataFrame())
    counts = {"emitted": 0, "skipped": 0, "graded": 0, "ledger_open": False}
    sb_error = {"date": SESSION.isoformat(), "error": "S-B step failed: boom", "candidates": [], "graded": [], "gate": {},
                "refresh": {"ok": False, "error": "timeout"}}
    doc = D.assemble(SESSION, {"ok": False, "warnings": ["preflight failed: timeout"]}, {"daily_contract_rows": 0, "earnings_events_rows": 0},
                     empty, pd.DataFrame(), pd.DataFrame(), [], counts, sb_error)
    assert SCH.validate(doc) == []


def test_nan_inf_dates_and_numpy_never_reach_the_file():
    body = {"date": SESSION, "season": "S2", "preflight": {"ok": True, "warnings": []},
            "mart": {"daily_contract_rows": np.int64(3), "earnings_events_rows": 0},
            "candidates": [], "suppressed": [], "dropped": [], "graded": [],
            "season_running": [{"variant": "A1", "structure": "SS", "n": np.int64(1), "dates": 1,
                                "mean_net_pct": float("nan"), "t": float("inf"), "net_usd_total": np.float64(12.5)}],
            "ledger": {"emitted": 0, "skipped": 0, "graded": 0, "ledger_open": False},
            "sb_state": {"date": SESSION.isoformat(), "gate": {}, "candidates": [], "graded": [], "refresh": {"ok": True}}}
    doc = SCH.clean(SCH.stamp(body))
    text = SCH.dumps(doc)
    assert "NaN" not in text and "Infinity" not in text
    back = json.loads(text, **STRICT)
    assert back["date"] == SESSION.isoformat() and back["season_running"][0]["mean_net_pct"] is None
    assert back["season_running"][0]["t"] is None and back["mart"]["daily_contract_rows"] == 3
    assert SCH.validate(back) == []


def test_validate_names_the_path_of_a_drift(tmp_path):
    run, graded, dropped_grade, running = _sa_pieces(str(tmp_path / "sa"))
    doc = D.assemble(SESSION, _preflight_ok(), {"daily_contract_rows": 1, "earnings_events_rows": 0},
                     run, graded, dropped_grade, running, {"emitted": 0, "skipped": 0, "graded": 0, "ledger_open": False},
                     _sb_state(str(tmp_path / "sb"), ENTRY))
    drifted = {**doc, "candidates": [{**doc["candidates"][0], "n": 1}] + doc["candidates"][1:]}
    errors = SCH.validate(drifted)
    assert len(errors) == 1 and errors[0].startswith("candidates/0:") and "'n'" in errors[0]
    assert SCH.validate({**doc, "schema_version": "d0.9"})[0].startswith("schema_version:")


def test_validate_signals_script_exit_codes(tmp_path):
    committed = sorted(glob.glob(os.path.join(REPO, "analyses", "daily", "*", "signals.json")))[-1]
    script = os.path.join(REPO, "scripts", "validate_signals.py")
    ok = subprocess.run([sys.executable, script, "--file", committed], capture_output=True, text=True)
    assert ok.returncode == 0 and ok.stdout.startswith("VALID:")
    with open(committed) as fh:
        tampered = json.load(fh)
    tampered["sb_state"]["gate"]["SPX"] = tampered["sb_state"]["gate"].get("SPY")
    bad = tmp_path / "signals.json"
    bad.write_text(json.dumps(tampered))
    res = subprocess.run([sys.executable, script, "--file", str(bad)], capture_output=True, text=True)
    assert res.returncode == 1 and "INVALID" in res.stdout and "sb_state/gate" in res.stdout
    nan = tmp_path / "nan.json"
    nan.write_text('{"schema_version": "d1.0", "x": NaN}')
    res = subprocess.run([sys.executable, script, "--file", str(nan)], capture_output=True, text=True)
    assert res.returncode == 1 and "non-finite" in res.stdout
