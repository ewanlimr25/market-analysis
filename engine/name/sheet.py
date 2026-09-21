"""`make ticker T=<SYMBOL> [DATE=] [DIRECTION=] [E=]` (findings/stock-deep-dive DESIGN/70 §0, §7, R6):
one name, one date -> `analyses/ticker/<SYMBOL>/<DATE>/{inputs/, ticker.json, report.md}` and the
ledger rows of §6. No model, no directional forecast; the owner's `DIRECTION=` is priced and
ledgered, never produced.

Order of a run (`run`): the call time is taken first (the `context_read` tag is decided from what
existed *before* this run wrote anything); inputs are read back from `inputs/` when they were
written before (a sheet re-derives offline and identically) or loaded and written; the sections
A..G are computed as pure functions over the inputs; the ledger rows are built and emitted
(write-once); `ticker.json` is validated against `schemas/ticker.schema.json` -- a failure is a hard
error, not a WARN -- and `report.md` is rendered from it.
"""
from __future__ import annotations

import argparse
import dataclasses
import os
import sys
import time
from datetime import date, datetime, timezone

from engine import calendar as cal
from engine import ledger as L
from engine import schema as SCH
from engine.config import ANALYSES_TICKER, LEDGER_NAME_DIR, NAME_PARAMS, NAME_POLICY_ID, NAME_SCHEMA_VERSION, NAME_SIZING
from engine.mart import cboe_chain
from engine.name import context as CX
from engine.name import context_tag as CT
from engine.name import data as D
from engine.name import events as EV
from engine.name import flags as FL
from engine.name import ledger_rows as LR
from engine.name import liquidity as LQ
from engine.name import premium as PR
from engine.name import range as RG
from engine.name import report as RP
from engine.name import structures as ST

INPUTS_DIR = "inputs"
REPORT_FILE = "report.md"
SCHEMA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "schemas", "ticker.schema.json")
SECTIONS = ("liquidity", "events", "premium", "range", "flags", "context")


class SheetValidationError(RuntimeError):
    """`ticker.json` does not match schema n1.0 (DESIGN/70 §7: a hard error)."""


def _prefixed_nulls(section: str, block: dict) -> list[dict]:
    """Section nulls with the section name in front (unless the module already put it there)."""
    out = []
    for n in block.get("nulls") or []:
        field = str(n["field"])
        out.append({"field": field if field.startswith(section + ".") else f"{section}.{field}", "reason": str(n["reason"])})
    return out


def sections(inputs: D.NameInputs, params=NAME_PARAMS) -> dict:
    """Sections A..F as pure functions over the inputs (each module owns its `source` and `nulls`)."""
    liquidity = LQ.evaluate(inputs, params)
    events = EV.evaluate(inputs, params)
    premium = PR.evaluate(inputs, params, events)
    range_ = RG.evaluate(inputs, params, events)
    flags = FL.evaluate(inputs, params)
    context = CX.evaluate(inputs, params)
    return {"liquidity": liquidity, "events": events, "premium": premium, "range": range_, "flags": flags, "context": context}


def assemble(inputs: D.NameInputs, secs: dict, structures: list[dict], rows: list[dict], *, direction: str | None,
             sizing=NAME_SIZING, context_read: str = CT.NONE, inputs_dir: str = "",
             present_before: list[bool] | None = None) -> dict:
    """The `ticker.json` document (strict-JSON clean, unvalidated), plus the raw ledger rows under `_rows`."""
    nulls = [{"field": str(n["field"]), "reason": str(n["reason"])} for n in inputs.nulls]
    for name in SECTIONS:
        nulls += _prefixed_nulls(name, secs[name])
    doc = {"schema": NAME_SCHEMA_VERSION, "policy_id": NAME_POLICY_ID, "ticker": inputs.ticker, "date": inputs.date.isoformat(),
           "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"), "E": float(sizing.equity),
           "direction": direction, **secs, "structures": structures,
           "ledger_rows": LR.summary(rows, present_before or [False] * len(rows)), "context_read": context_read,
           "inputs_dir": inputs_dir, "nulls": nulls}
    return {**SCH.clean(doc), "_rows": rows}


def build(inputs: D.NameInputs, *, direction: str | None, sizing=NAME_SIZING, params=NAME_PARAMS,
          context_read: str = CT.NONE, inputs_dir: str = "") -> dict:
    """Sections, structures, rows and the document for one `NameInputs`, without any I/O (tests)."""
    secs = sections(inputs, params)
    structures = ST.build(inputs, params, sizing, liquidity=secs["liquidity"], events=secs["events"],
                          premium=secs["premium"], range_=secs["range"], flags=secs["flags"], direction=direction)
    rows = build_rows(inputs, secs, structures, direction, context_read)
    return assemble(inputs, secs, structures, rows, direction=direction, sizing=sizing, context_read=context_read,
                    inputs_dir=inputs_dir)


def build_rows(inputs: D.NameInputs, secs: dict, structures: list[dict], direction: str | None, context_read: str) -> list[dict]:
    rows = []
    sheet = LR.sheet_row(inputs.ticker, inputs.date, secs["liquidity"], secs["premium"], structures)
    if sheet is not None:
        rows.append(sheet)
    if direction:
        rows += LR.disc_rows(inputs.ticker, inputs.date, direction, structures, context_read)
    return rows


def validate(doc: dict) -> list[str]:
    return SCH.validate({k: v for k, v in doc.items() if not k.startswith("_")}, SCH.load_schema(SCHEMA_PATH))


def write(doc: dict, out_dir: str) -> list[str]:
    """`ticker.json` + `report.md`; raises `SheetValidationError` before writing anything invalid."""
    public = {k: v for k, v in doc.items() if not k.startswith("_")}
    errors = validate(public)
    if errors:
        raise SheetValidationError(f"{public['ticker']} {public['date']}: {len(errors)} schema violations: " + "; ".join(errors[:8]))
    os.makedirs(out_dir, exist_ok=True)
    paths = []
    for name, text in ((CT.SHEET_FILE, SCH.dumps(public)), (REPORT_FILE, RP.render(public))):
        path = os.path.join(out_dir, name)
        with open(path, "w") as fh:
            fh.write(text)
        paths.append(path)
    return paths


def load_or_read_inputs(ticker: str, d: date, inputs_dir: str, *, offline: bool, refresh: bool, con=None) -> D.NameInputs:
    if os.path.isdir(inputs_dir) and not refresh:
        return D.read_inputs(inputs_dir)
    inputs = D.load_inputs(ticker, d, con=con, online=not offline)
    D.write_inputs(inputs, inputs_dir)
    return inputs


def run(ticker: str, d: date, *, direction: str | None = None, equity: float | None = None, allow_undefined: bool = False,
        offline: bool = False, refresh: bool = False, out_root: str = ANALYSES_TICKER, ledger_dir: str | None = LEDGER_NAME_DIR,
        con=None, call_time: float | None = None) -> dict:
    """One sheet end to end; returns the written document (with `_paths`)."""
    ticker = ticker.upper()
    if direction is not None and direction not in ("long", "short"):
        raise ValueError(f"direction must be long or short, got {direction!r}")
    call_time = time.time() if call_time is None else call_time
    out_dir = os.path.join(out_root, ticker, d.isoformat())
    context_read = CT.context_read(out_dir, call_time)
    inputs_dir = os.path.join(out_dir, INPUTS_DIR)
    inputs = load_or_read_inputs(ticker, d, inputs_dir, offline=offline, refresh=refresh, con=con)
    sizing = dataclasses.replace(NAME_SIZING, equity=float(equity or NAME_SIZING.equity), allow_undefined=allow_undefined)
    secs = sections(inputs)
    structures = ST.build(inputs, NAME_PARAMS, sizing, liquidity=secs["liquidity"], events=secs["events"],
                          premium=secs["premium"], range_=secs["range"], flags=secs["flags"], direction=direction)
    rows = build_rows(inputs, secs, structures, direction, context_read)
    present = [False] * len(rows)
    if ledger_dir and rows:
        existing = L.read_signals(ledger_dir)
        present = [LR.already_present(existing, r) for r in rows]
        L.emit(ledger_dir, LR.frame(rows), d)
    doc = assemble(inputs, secs, structures, rows, direction=direction, sizing=sizing, context_read=context_read,
                   inputs_dir=inputs_dir, present_before=present)
    paths = write(doc, out_dir)
    return {**doc, "_paths": paths}


def _symbols(a) -> list[str]:
    syms = [a.ticker.upper()] if a.ticker else []
    if a.symbols_file:
        syms = cboe_chain.merge_symbols(syms, cboe_chain.read_symbols_file(a.symbols_file))
    return syms


def main() -> int:
    ap = argparse.ArgumentParser(description="The ticker sheet: one name, one date, no model.")
    ap.add_argument("--ticker")
    ap.add_argument("--symbols-file", help="one sheet per symbol in the file (no DIRECTION)")
    ap.add_argument("--date", required=True)
    ap.add_argument("--direction", choices=("long", "short"))
    ap.add_argument("--equity", type=float)
    ap.add_argument("--allow-undefined", action="store_true")
    ap.add_argument("--offline", action="store_true", help="no network: stored inputs or marts only")
    ap.add_argument("--refresh", action="store_true", help="reload inputs even if inputs/ exists")
    ap.add_argument("--out-root", default=ANALYSES_TICKER)
    ap.add_argument("--ledger-dir", default=LEDGER_NAME_DIR)
    ap.add_argument("--no-ledger", action="store_true")
    a = ap.parse_args()
    syms = _symbols(a)
    if not syms:
        ap.error("pass --ticker or --symbols-file")
    if a.direction and len(syms) != 1:
        ap.error("--direction takes exactly one --ticker")
    d = cal.parse_date(a.date)
    failures = 0
    for sym in syms:
        try:
            doc = run(sym, d, direction=a.direction, equity=a.equity, allow_undefined=a.allow_undefined, offline=a.offline,
                      refresh=a.refresh, out_root=a.out_root, ledger_dir=None if a.no_ledger else a.ledger_dir)
        except Exception as exc:  # one bad name never stops a batch; the failure is printed, not hidden
            failures += 1
            print(f"{sym}: FAILED {type(exc).__name__}: {str(exc)[:300]}", file=sys.stderr)
            continue
        q, p = doc["liquidity"], doc["premium"]
        print(f"{sym}: {'CAN_PRICE' if q['can_price'] else 'CANNOT_PRICE ' + str(q['failing'])} · {p['verdict']} · "
              f"sc {p['sc'].get('failing') or 'PASS'} · x1 {p['x1']} · structures {len(doc['structures'])} · "
              f"ledger {[r['gate_verdict'] for r in doc['ledger_rows']]} · nulls {len(doc['nulls'])} -> {doc['_paths'][1]}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
