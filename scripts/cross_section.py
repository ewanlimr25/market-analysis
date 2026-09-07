#!/usr/bin/env python3
"""Run the G4/G5 weekly cross-section (RESEARCH/47 §2 G4/G5) and write the panel and results.

  python3 scripts/cross_section.py
  python3 scripts/cross_section.py --out-dir data/backtest --prefix g4

Writes `<out-dir>/<prefix>_factors.parquet` (ticker x formation x factors x controls x outcome)
and `<out-dir>/<prefix>_results.json` (the 8-test table, power, universe counts, the CBOE-vs-hot-
chains skew check). Refuses to overwrite an existing file unless `--force` is passed.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from engine.research import cross_section as CS   # noqa: E402


class _JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, date):
            return o.isoformat()
        try:
            import numpy as np
            if isinstance(o, (np.integer,)):
                return int(o)
            if isinstance(o, (np.floating,)):
                return float(o)
            if isinstance(o, np.bool_):
                return bool(o)
        except ImportError:
            pass
        return super().default(o)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out-dir", default=os.path.join("data", "backtest"))
    ap.add_argument("--prefix", default="g4")
    ap.add_argument("--force", action="store_true", help="overwrite existing output files")
    a = ap.parse_args()

    factors_path = os.path.join(a.out_dir, f"{a.prefix}_factors.parquet")
    results_path = os.path.join(a.out_dir, f"{a.prefix}_results.json")
    if not a.force:
        existing = [p for p in (factors_path, results_path) if os.path.exists(p)]
        if existing:
            print(f"refusing to overwrite existing file(s): {existing} (pass --force)", file=sys.stderr)
            return 1

    panel, results = CS.run()
    os.makedirs(a.out_dir, exist_ok=True)
    panel.to_parquet(factors_path, index=False)
    with open(results_path, "w") as f:
        json.dump(results, f, indent=1, cls=_JSONEncoder)

    print(f"{len(panel):,} panel rows across {results['n_formations']} formations -> {factors_path}")
    print(f"results -> {results_path}")
    for row in results["tests"]:
        print(f"  {row['factor']:>12} {row['variant']:>8}  mean_ic={row['mean_ic']:+.4f} "
              f"nw_t={row['nw_t']:+.2f} bh_q={row['bh_q']:.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
