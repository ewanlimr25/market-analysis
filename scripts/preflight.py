#!/usr/bin/env python3
"""Is tonight's data safe to scan on? One command, run before Phase A.

Checks the two things that have silently corrupted a scan:

  1. UW panel presence + row counts for the trade date. "Stale UW data -> abort and ask
     for a re-export" is a documented failure mode of /market-scan, previously satisfied
     with ad-hoc `ls` and hand-written counts.
  2. Truth-set panel edge vs the trade date. On 2026-07-24 the momentum lane silently
     computed its regime off a parquet that ended 2026-07-17 and returned an INVERTED
     read -- CHOP / "unconfirmed dip" where the live tape was PULLBACK / confirmed
     downtrend. Both land on s1_standdown=FALSE, so nothing broke that day, but the lane's
     caution narrative was built on numbers that were five sessions stale.

Exit 0 = clear, 1 = something a lane could silently misread. Advisory either way: it
prints, it does not block.

Usage:
  python3 scripts/preflight.py --date 2026-07-24
  python3 scripts/preflight.py --date 2026-07-24 --json
"""
from __future__ import annotations

import argparse
import json
import os
import sys

STOCKS = os.path.expanduser("~/Documents/Stocks")
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")

GROUPS = {
    "All Options": "bot-eod-report-{d}.parquet",
    "Dark pool": "dp-eod-report-{d}.parquet",
    "Hot Option Chains": "hot-chains-{d}.parquet",
    "OI changes": "chain-oi-changes-{d}.parquet",
    "Stock Screener": "stock-screener-{d}.parquet",
}
TRUTH_SETS = ("prices", "returns", "features")


def check(date: str) -> dict:
    import duckdb
    con = duckdb.connect()
    out: dict = {"date": date, "panel": {}, "truth_set": {}, "ok": True, "warnings": []}

    for group, pat in GROUPS.items():
        path = f"{STOCKS}/{group}/{pat.format(d=date)}"
        if not os.path.exists(path):
            out["panel"][group] = {"present": False, "rows": None}
            out["ok"] = False
            out["warnings"].append(f"{group}: no export for {date} -- re-export before scanning")
            continue
        try:
            n = con.execute(f"SELECT count(*) FROM read_parquet('{path}')").fetchone()[0]
        except Exception as e:
            out["panel"][group] = {"present": True, "rows": None, "error": str(e)[:120]}
            out["ok"] = False
            out["warnings"].append(f"{group}: unreadable ({type(e).__name__})")
            continue
        out["panel"][group] = {"present": True, "rows": n}
        if n == 0:
            out["ok"] = False
            out["warnings"].append(f"{group}: export is EMPTY")

    for name in TRUTH_SETS:
        path = os.path.join(DATA, f"{name}.parquet")
        if not os.path.exists(path):
            out["truth_set"][name] = {"max_date": None}
            out["warnings"].append(f"{name}.parquet missing")
            out["ok"] = False
            continue
        mx = con.execute(f"SELECT max(date) FROM read_parquet('{path}')").fetchone()[0]
        mx = mx.isoformat() if mx else None
        stale = bool(mx and mx < date)
        out["truth_set"][name] = {"max_date": mx, "stale_vs_trade_date": stale}
        if stale:
            out["ok"] = False
            out["warnings"].append(
                f"{name}.parquet ends {mx}, BEFORE the {date} trade date -- any lane reading it "
                f"gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_{name}.py")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    res = check(a.date)
    if a.json:
        print(json.dumps(res, indent=2))
        return 0 if res["ok"] else 1

    print(f"preflight for {a.date}")
    present = sum(1 for v in res["panel"].values() if v["present"])
    print(f"\n  UW panel: {present}/{len(GROUPS)} groups present")
    for g, v in res["panel"].items():
        mark = "ok  " if v["present"] and v.get("rows") else "MISS"
        rows = f"{v['rows']:,} rows" if v.get("rows") else "-"
        print(f"    [{mark}] {g:20s} {rows}")
    print("\n  truth set:")
    for n, v in res["truth_set"].items():
        mark = "STALE" if v.get("stale_vs_trade_date") else "ok   "
        print(f"    [{mark}] {n+'.parquet':22s} -> {v['max_date']}")

    if res["warnings"]:
        print("\n  WARNINGS")
        for w in res["warnings"]:
            print(f"    - {w}")
    else:
        print("\n  clear: panel complete and truth set reaches the trade date")
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
