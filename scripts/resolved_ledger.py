#!/usr/bin/env python3
"""Durable ledger of RESOLVED measurements -- so a matured measurement cannot un-happen.

Covers TWO record kinds, both of which are re-derived from the live vendor feed every cycle:
  CALL         a `calls[]` row      (audit `resolved_calls.json`)
  SUPPRESSION  a gate-suppressed    (`suppression_resolve.py --out`)  [added 2026-09-05]

Why this exists
---------------
The 2026-08-22 calibration audit found that EQR (OI_FADE, signalled 2026-07-09) had resolved
cleanly at the 08-15 audit and, a week later, could not be resolved at all: Yahoo had RETRACTED
11 sessions it previously served (2026-07-23 -> 08-10), identically on both hosts and both query
forms, and the 08-21 truth-set rebuild inherited the gap. OI_FADE's forward book shrank from 81
to 80 cluster-units with no code change and no new information.

Every audit re-derives realized excess from the live vendor feed. That operation is **not
idempotent**, so the audit book is not append-only and a lane's N can go DOWN. Once a window has
matured and been measured, that measurement IS the record; re-deriving it can only lose.

Suppressions were left uncovered until 2026-09-05, and the gap bit: CRNX lost **25 contiguous
sessions** to a vendor retraction that cycle. Its four `calls[]` rows were restored from this
ledger; its suppression row had no such record and simply vanished from the gate-effectiveness
cohort. A gate that suppresses its own evidence cannot also afford to lose it to the feed.

Contract
--------
- Only RESOLVED rows enter the ledger. OPEN/PENDING/INCONCLUSIVE rows are not measurements.
- The FIRST matured measurement wins. A later re-derivation never overwrites it -- it either
  agrees (silent), or it is reported as a conflict for a human to read.
- Nothing is silently repaired: `apply()` marks every restored row `from_ledger: True`.
- Pure/immutable: `merge()` and `apply()` return new objects and never mutate their inputs.

The ledger lives under `analyses/audit/`, which CLAUDE.md keeps local-only (gitignored), the same
status as the audit working files it protects. `scripts/` is the right home for the CODE because
a fix made only inside a dated audit directory does not survive the cycle -- the same reasoning
that moved `suppression_resolve.py` here.

Usage:
  python3 scripts/resolved_ledger.py --update analyses/audit/<date>/resolved_calls.json
  python3 scripts/resolved_ledger.py --update-suppressions analyses/audit/<date>/suppressions.json
  python3 scripts/resolved_ledger.py --report
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DEFAULT_LEDGER = os.path.join(ROOT, "analyses", "audit", "resolved_ledger.json")
DEFAULT_SUPPRESSION_LEDGER = os.path.join(ROOT, "analyses", "audit",
                                          "suppression_ledger.json")

# Excess is stored to 4dp by the resolvers; a re-derivation differing by less than this is
# floating-point/rounding noise, not a retraction. The 08-22 audit saw exactly one such row
# (CG, -7.7649 -> -7.7648) across a resolver swap and it must not be reported as a change.
TOL_PP = 1e-3

@dataclass(frozen=True)
class Schema:
    """How one record KIND identifies and measures itself.

    Two kinds share this module because they share the whole problem: both are re-derived from a
    non-idempotent feed, and both lose evidence silently when the feed retracts. Only the field
    names differ, so the mechanism is written once.
    """

    name: str
    prefix: str               # namespaces the key so kinds cannot collide in one file
    identity: tuple[str, ...]  # the SIGNAL, never the run that measured it
    status_field: str
    measured: tuple[str, ...]
    value_field: str
    why_fields: tuple[str, ...]


CALL = Schema(
    name="call", prefix="",
    identity=("report_date", "ticker", "lane", "horizon"),
    status_field="T1_status",
    measured=("T1_status", "T1_entry", "T1_exit", "T1_excess_pct", "T1_win", "T1_base_hit",
              "T1_tk_ret_pct", "T1_spy_ret_pct"),
    value_field="T1_excess_pct",
    why_fields=("T1_why", "why"),
)

SUPPRESSION = Schema(
    name="suppression", prefix="sup",
    # `period` distinguishes a weekly (2026-W34) from a daily envelope on the same name+lane.
    identity=("period", "report_date", "ticker", "lane", "horizon"),
    status_field="status",
    measured=("status", "entry", "exit", "excess_pct", "gate_correct"),
    value_field="excess_pct",
    why_fields=("why",),
)

# Back-compat: callers written before the schema split import MEASURED directly.
MEASURED = CALL.measured


def key(row: dict, schema: Schema = CALL) -> str:
    """Stable identity of a measurement: the signal, not the run that measured it."""
    parts = [schema.prefix] if schema.prefix else []
    parts += [str(row.get(f)) for f in schema.identity]
    return "|".join(parts)


def _why(row: dict, schema: Schema) -> str | None:
    return next((row[f] for f in schema.why_fields if row.get(f)), None)


def merge(ledger: dict, fresh: list[dict],
          schema: Schema = CALL) -> tuple[dict, list[dict]]:
    """Fold freshly-resolved rows into the ledger. Returns (new_ledger, conflicts)."""
    out = dict(ledger)
    conflicts: list[dict] = []

    for r in fresh:
        k = key(r, schema)
        prior = out.get(k)
        is_resolved = r.get(schema.status_field) == "RESOLVED"

        if prior is None:
            if is_resolved:
                out[k] = ({f: r.get(f) for f in schema.measured}
                          | {f: r.get(f) for f in schema.identity}
                          | {"kind": schema.name})
            continue

        if not is_resolved:
            conflicts.append({"key": k, "kind": "RETRACTED",
                              "was": prior.get(schema.value_field), "now": None,
                              "why": _why(r, schema)})
            continue

        was, now = prior.get(schema.value_field), r.get(schema.value_field)
        if was is not None and now is not None and abs(was - now) > TOL_PP:
            conflicts.append({"key": k, "kind": "CHANGED", "was": was, "now": now,
                              "why": "re-derivation disagrees with the recorded measurement"})

    return out, conflicts


def apply(ledger: dict, fresh: list[dict],
          schema: Schema = CALL) -> tuple[list[dict], list[dict]]:
    """Return `fresh` with retracted rows restored from the ledger, plus the conflict list."""
    _, conflicts = merge(ledger, fresh, schema)
    retracted = {c["key"] for c in conflicts if c["kind"] == "RETRACTED"}

    out = []
    for r in fresh:
        k = key(r, schema)
        if k in retracted:
            restored = dict(r) | {f: ledger[k].get(f) for f in schema.measured}
            # `status` is the audit-side view of the row; keep it in step with the schema's own.
            out.append(restored | {"status": ledger[k].get(schema.status_field),
                                   "from_ledger": True})
        else:
            out.append(dict(r))
    return out, conflicts


def load(path: str) -> dict:
    if not os.path.exists(path):
        return {}
    with open(path) as fh:
        return json.load(fh)


def save(path: str, ledger: dict) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as fh:
        json.dump(ledger, fh, indent=1, sort_keys=True)


def _update(path: str, ledger_path: str, schema: Schema) -> int:
    """Fold one resolver's output into its ledger. Returns the process exit code."""
    ledger = load(ledger_path)
    with open(path) as fh:
        fresh = json.load(fh)
    new_ledger, conflicts = merge(ledger, fresh, schema)
    added = len(new_ledger) - len(ledger)
    save(ledger_path, new_ledger)
    print(f"{schema.name} ledger {len(ledger)} -> {len(new_ledger)} rows (+{added}) [{ledger_path}]")
    if not conflicts:
        print("no conflicts: every prior measurement re-derived identically")
    for c in conflicts:
        print(f"  !! {c['kind']:<10} {c['key']}  was {c['was']} now {c['now']}  -- {c['why']}")
    print(f"\n{len(conflicts)} conflict(s). RETRACTED rows keep their recorded value; "
          f"pass the ledger through `apply()` to restore them into the audit book.")
    return 1 if conflicts else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--update", metavar="RESOLVED_CALLS_JSON",
                    help="fold an audit's resolved_calls.json into the CALL ledger")
    ap.add_argument("--update-suppressions", metavar="SUPPRESSIONS_JSON",
                    help="fold suppression_resolve.py --out into the SUPPRESSION ledger")
    ap.add_argument("--report", action="store_true", help="summarise both ledgers")
    ap.add_argument("--ledger", default=DEFAULT_LEDGER)
    ap.add_argument("--suppression-ledger", default=DEFAULT_SUPPRESSION_LEDGER)
    a = ap.parse_args()

    rc = 0
    if a.update:
        rc |= _update(a.update, a.ledger, CALL)
    if a.update_suppressions:
        rc |= _update(a.update_suppressions, a.suppression_ledger, SUPPRESSION)
    if a.update or a.update_suppressions:
        return rc

    import collections
    for label, path in (("call", a.ledger), ("suppression", a.suppression_ledger)):
        ledger = load(path)
        if not ledger:
            print(f"{label} ledger is empty ({path})")
            continue
        by = collections.Counter(v.get("lane") for v in ledger.values())
        print(f"{len(ledger)} resolved {label} measurements [{path}]")
        for lane, n in sorted(by.items()):
            print(f"  {lane:<14}{n:>5}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
