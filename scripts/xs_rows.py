#!/usr/bin/env python3
"""Dry run of the G4/G5 exploration row generator (RESEARCH/47 §2; DESIGN/100 §6). Prints the rows
`engine.strategies.xs.build_rows` would emit for one formation Friday and writes nothing to
`ledger/` -- wiring this into `make daily` is left to the orchestrator (task spec, "Where to work").

  python3 scripts/xs_rows.py --date 2026-08-28
  python3 scripts/xs_rows.py --date 2026-08-28 --grade     # also resolves next-week excess, if known
"""
from __future__ import annotations

import argparse
import os
import sys
from datetime import date

import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from engine.research import cross_section as CS   # noqa: E402
from engine.strategies import xs as XS             # noqa: E402


def _outcome_lookup():
    ret = pd.read_parquet(CS.RETURNS_FILE, columns=["ticker", "date", "horizon", "resolved", "excess"])
    ret = ret[(ret["horizon"] == CS.OUTCOME_HORIZON) & ret["resolved"]]
    ret["date"] = pd.to_datetime(ret["date"]).dt.date
    table = ret.set_index(["ticker", "date"])["excess"]

    def lookup(ticker: str, formation_date) -> float | None:
        key = (ticker, formation_date)
        return float(table.loc[key]) if key in table.index else None
    return lookup


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--date", required=True, type=date.fromisoformat)
    ap.add_argument("--grade", action="store_true", help="also resolve next-week excess where known")
    a = ap.parse_args()

    week = CS.build_week_factors_with_delta(a.date)
    if week.empty:
        print(f"no universe-eligible tickers for {a.date}", file=sys.stderr)
        return 1
    rows = XS.build_rows(week, formation_date=a.date)
    if not XS.check_key_unique(rows):
        print("KEY not unique on generated rows -- refusing to print", file=sys.stderr)
        return 1
    if a.grade:
        rows = XS.grade_rows(rows, _outcome_lookup())

    with pd.option_context("display.max_rows", None, "display.width", 200):
        print(rows.to_string(index=False))
    print(f"\n{len(rows)} exploration rows for {a.date} "
          f"({len(rows) // (2 * XS.N_PER_SIDE) if XS.N_PER_SIDE else 0} factors x top/bottom, "
          f"up to {XS.N_PER_SIDE} names a side); NOT written to ledger/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
