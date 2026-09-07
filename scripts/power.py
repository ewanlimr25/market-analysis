#!/usr/bin/env python3
"""How many independent units a challenger needs (DESIGN/100 §4).

  python3 scripts/power.py --strategy sb --min-effect 0.01                 # sd from the champion ledger, else the backtest
  python3 scripts/power.py --strategy sb --min-effect 0.01 --sd 0.06       # explicit sd
Prints the sd used and its source, the autocorrelation inflation, n_required and the projected date.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date

import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from engine import ledger as L                       # noqa: E402
from engine import policy as POL                     # noqa: E402
from engine.config import LEDGER_DIR                 # noqa: E402
from engine.improve import power as PW               # noqa: E402
from engine.improve.spec import spec                 # noqa: E402


def champion_series(strategy: str, ledger_root: str) -> tuple[pd.Series, str]:
    sp = spec(strategy)
    led = L.read_ledger(sp.ledger_dir(ledger_root))
    if len(led) and "role" in led.columns:
        rows = led[(led["policy_id"] == sp.champion_id) & (led["role"] == POL.ROLE_CHAMPION)]
        if len(rows) >= PW.MIN_SERIES:
            return rows.sort_values(sp.unit)[sp.metric], f"ledger {sp.champion_id} (n={len(rows)})"
    if os.path.exists(sp.backtest_file):
        bt = pd.read_parquet(sp.backtest_file)
        col = sp.metric if sp.metric in bt.columns else None
        if col:
            return bt.sort_values(sp.entry_col if sp.entry_col in bt.columns else bt.columns[0])[col], f"backtest {os.path.basename(sp.backtest_file)} (n={len(bt)})"
    return pd.Series(dtype=float), "none"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strategy", required=True)
    ap.add_argument("--min-effect", type=float, required=True, help="smallest reward difference worth detecting (metric units)")
    ap.add_argument("--sd", type=float, default=None)
    ap.add_argument("--alpha", type=float, default=PW.ALPHA)
    ap.add_argument("--power", type=float, default=PW.POWER)
    ap.add_argument("--units-per-week", type=float, default=None)
    ap.add_argument("--start", default=date.today().isoformat())
    ap.add_argument("--ledger-dir", default=LEDGER_DIR)
    a = ap.parse_args()
    sp = spec(a.strategy)
    series, source = champion_series(a.strategy, a.ledger_dir)
    if a.sd is None and series.empty:
        print("no series for the realised sd (empty ledger and no backtest file); pass --sd", file=sys.stderr)
        return 1
    out = PW.plan(a.min_effect, series if len(series) else None, sp.lag, date.fromisoformat(a.start),
                  a.units_per_week or sp.units_per_week, a.alpha, a.power, a.sd)
    out["series_source"] = source if a.sd is None else "explicit --sd"
    print(json.dumps(out, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
