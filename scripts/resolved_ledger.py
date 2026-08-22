#!/usr/bin/env python3
"""Durable ledger of RESOLVED forward calls -- so a matured measurement cannot un-happen.

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
  python3 scripts/resolved_ledger.py --update analyses/audit/2026-08-22/resolved_calls.json
  python3 scripts/resolved_ledger.py --report
"""
from __future__ import annotations

import argparse
import json
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DEFAULT_LEDGER = os.path.join(ROOT, "analyses", "audit", "resolved_ledger.json")

# Excess is stored to 4dp by the resolvers; a re-derivation differing by less than this is
# floating-point/rounding noise, not a retraction. The 08-22 audit saw exactly one such row
# (CG, -7.7649 -> -7.7648) across a resolver swap and it must not be reported as a change.
TOL_PP = 1e-3

# The fields that constitute the measurement itself.
MEASURED = ("T1_status", "T1_entry", "T1_exit", "T1_excess_pct", "T1_win", "T1_base_hit",
            "T1_tk_ret_pct", "T1_spy_ret_pct")


def key(row: dict) -> str:
    """Stable identity of a call: the signal, not the run that measured it."""
    return f"{row.get('report_date')}|{row.get('ticker')}|{row.get('lane')}|{row.get('horizon')}"


def merge(ledger: dict, fresh: list[dict]) -> tuple[dict, list[dict]]:
    """Fold freshly-resolved rows into the ledger. Returns (new_ledger, conflicts)."""
    out = dict(ledger)
    conflicts: list[dict] = []

    for r in fresh:
        k = key(r)
        prior = out.get(k)
        is_resolved = r.get("T1_status") == "RESOLVED"

        if prior is None:
            if is_resolved:
                out[k] = {f: r.get(f) for f in MEASURED} | {
                    "report_date": r.get("report_date"), "ticker": r.get("ticker"),
                    "lane": r.get("lane"), "horizon": r.get("horizon")}
            continue

        if not is_resolved:
            conflicts.append({"key": k, "kind": "RETRACTED",
                              "was": prior.get("T1_excess_pct"), "now": None,
                              "why": r.get("T1_why") or r.get("why")})
            continue

        was, now = prior.get("T1_excess_pct"), r.get("T1_excess_pct")
        if was is not None and now is not None and abs(was - now) > TOL_PP:
            conflicts.append({"key": k, "kind": "CHANGED", "was": was, "now": now,
                              "why": "re-derivation disagrees with the recorded measurement"})

    return out, conflicts


def apply(ledger: dict, fresh: list[dict]) -> tuple[list[dict], list[dict]]:
    """Return `fresh` with retracted rows restored from the ledger, plus the conflict list."""
    _, conflicts = merge(ledger, fresh)
    retracted = {c["key"] for c in conflicts if c["kind"] == "RETRACTED"}

    out = []
    for r in fresh:
        k = key(r)
        if k in retracted:
            out.append(dict(r) | {f: ledger[k].get(f) for f in MEASURED}
                       | {"status": ledger[k].get("T1_status"), "from_ledger": True})
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


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--update", metavar="RESOLVED_CALLS_JSON",
                    help="fold an audit's resolved_calls.json into the ledger")
    ap.add_argument("--report", action="store_true", help="summarise the ledger")
    ap.add_argument("--ledger", default=DEFAULT_LEDGER)
    a = ap.parse_args()

    ledger = load(a.ledger)

    if a.update:
        with open(a.update) as fh:
            fresh = json.load(fh)
        new, conflicts = merge(ledger, fresh)
        added = len(new) - len(ledger)
        save(a.ledger, new)
        print(f"ledger {len(ledger)} -> {len(new)} rows (+{added}) [{a.ledger}]")
        if not conflicts:
            print("no conflicts: every prior measurement re-derived identically")
        for c in conflicts:
            print(f"  !! {c['kind']:<10} {c['key']}  was {c['was']} now {c['now']}  -- {c['why']}")
        print(f"\n{len(conflicts)} conflict(s). RETRACTED rows keep their recorded value; "
              f"pass the ledger through `apply()` to restore them into the audit book.")
        return 1 if conflicts else 0

    if a.report or not a.update:
        if not ledger:
            print(f"ledger is empty ({a.ledger})")
            return 0
        import collections
        by = collections.Counter(v.get("lane") for v in ledger.values())
        print(f"{len(ledger)} resolved measurements [{a.ledger}]")
        for lane, n in sorted(by.items()):
            print(f"  {lane:<14}{n:>5}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
