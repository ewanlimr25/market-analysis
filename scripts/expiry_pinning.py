#!/usr/bin/env python3
"""G6: expiration-day pinning on single names (`findings/market-analysis/RESEARCH/47-edge-gaps.md`
§2 G6; Ni-Pearson-Poteshman 2005). Companion write-up:
`findings/market-analysis/artifacts/edge-gaps/g6/results.md`.

  python3 scripts/expiry_pinning.py build                 # -> data/backtest/g6_pins.parquet
  python3 scripts/expiry_pinning.py report [--out DIR]     # rate tables + verdict -> stdout, DIR/results.json

`make expiry-pinning` runs both.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import numpy as np                                             # noqa: E402
import pandas as pd                                            # noqa: E402

from engine import config                                       # noqa: E402
from engine.research import expiry_pinning_data as D             # noqa: E402
from engine.research import expiry_pinning_stats as S            # noqa: E402
from engine.research.expiry_pinning import build_expiry_calendar  # noqa: E402

PANEL_START = date(2026, 3, 13)
PANEL_END = date(2026, 9, 4)
PINS_PATH = os.path.join(config.DATA, "backtest", "g6_pins.parquet")
DEFAULT_OUT = os.path.expanduser("~/Development/findings/market-analysis/artifacts/edge-gaps/g6")


def _json_default(obj):
    if isinstance(obj, (date,)):
        return obj.isoformat()
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.floating,)):
        return float(obj)
    if isinstance(obj, (np.bool_,)):
        return bool(obj)
    return str(obj)


def cmd_build(_args: argparse.Namespace) -> int:
    pins, excluded = D.build_pin_rows(PANEL_START, PANEL_END)
    if pins.empty:
        print("error: no g6_pins rows built (check the panel is mounted)", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(PINS_PATH), exist_ok=True)
    pins.to_parquet(PINS_PATH, index=False)
    print(f"g6_pins: {len(pins)} rows, {pins['underlying'].nunique()} names, "
         f"{pins['expiry'].nunique()} usable expiries, {len(excluded)} excluded (panel gap): "
         f"{[d.isoformat() for d in sorted(excluded)]}")
    print(f"-> {PINS_PATH}")
    return 0


def cmd_report(args: argparse.Namespace) -> int:
    if not os.path.exists(PINS_PATH):
        print(f"error: {PINS_PATH} not found; run `build` first", file=sys.stderr)
        return 1
    pins = pd.read_parquet(PINS_PATH)
    weeks = build_expiry_calendar(PANEL_START, PANEL_END)
    all_expiries = {w.expiry for w in weeks}
    usable_expiries = set(pins["expiry"].unique())
    excluded = sorted(all_expiries - usable_expiries)
    report = S.build_full_report(pins, n_fridays_total=len(weeks), excluded_expiries=excluded)
    out_dir = args.out
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "results.json")
    with open(out_path, "w") as f:
        json.dump(report, f, indent=2, default=_json_default)
    print(json.dumps(report, indent=2, default=_json_default))
    print(f"-> {out_path}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("build", help="build g6_pins.parquet from the raw panel")
    p_report = sub.add_parser("report", help="rate tables + verdict from g6_pins.parquet")
    p_report.add_argument("--out", default=DEFAULT_OUT, help="directory for results.json")
    args = parser.parse_args(argv)
    return {"build": cmd_build, "report": cmd_report}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
