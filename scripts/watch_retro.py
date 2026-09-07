#!/usr/bin/env python3
"""Watch-basket retrospective build (DESIGN/110-watch-basket.md §5, R1 build in §7).

Assembles every one of the 17 conditions for every (ticker, night) in the §1 universe over the
panel 2026-03-13 to 2026-09-04, then the five descriptive tables of §5.

  python3 scripts/watch_retro.py

Writes `data/backtest/wb_conditions.parquet` (ticker x date x condition values x bull/bear/vol
counts x basket flags) and `data/backtest/wb_retro.json` (the five tables, diagnostics, runtime).
Paper-only, descriptive: nothing here touches `ledger/` or a frozen parameter.
"""
from __future__ import annotations

import json
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from engine import config                        # noqa: E402
from engine.watch import retro as R               # noqa: E402
from engine.watch import retro_tables as RT       # noqa: E402
from engine.watch.conditions import ALL_CONDITIONS, SIGN_MINUS, SIGN_PLUS  # noqa: E402

OUT_DIR = os.path.join(config.DATA, "backtest")
CONDITIONS_PATH = os.path.join(OUT_DIR, "wb_conditions.parquet")
RETRO_JSON_PATH = os.path.join(OUT_DIR, "wb_retro.json")


def _write_atomic_parquet(df, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    df.to_parquet(tmp, index=False)
    os.replace(tmp, path)


def main() -> int:
    t0 = time.time()
    cond_df, diag = R.build_panel()
    _write_atomic_parquet(cond_df, CONDITIONS_PATH)

    returns_df = R.load_returns()
    condition_tbl = RT.condition_table(cond_df, returns_df)
    bull_tbl = RT.count_table(cond_df, returns_df, "bull", max_count=len(SIGN_PLUS))
    bear_tbl = RT.count_table(cond_df, returns_df, "bear", max_count=len(SIGN_MINUS))
    basket_tbl = RT.basket_table(cond_df, returns_df)
    examples = RT.worked_examples(cond_df, returns_df, n=6)
    nightly_sizes = RT.nightly_basket_sizes(cond_df)

    elapsed = time.time() - t0
    report = {
        "panel": {"start": R.PANEL_START.isoformat(), "end": R.PANEL_END.isoformat(),
                  "n_nights": diag["n_nights"], "n_universe_rows": diag["n_universe_rows"],
                  "n_tickers": diag["n_tickers"]},
        "runtime_s": elapsed,
        "build_elapsed_s": diag["elapsed_s"],
        "condition_table": condition_tbl.to_dict("records"),
        "bull_count_table": bull_tbl.to_dict("records"),
        "bear_count_table": bear_tbl.to_dict("records"),
        "basket_table": basket_tbl.to_dict("records"),
        "worked_examples": examples,
        "nightly_basket_sizes": nightly_sizes,
    }
    os.makedirs(OUT_DIR, exist_ok=True)
    tmp = RETRO_JSON_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=2, default=str)
    os.replace(tmp, RETRO_JSON_PATH)

    print(f"watch_retro: {diag['n_nights']} nights, {diag['n_tickers']} tickers, "
          f"{diag['n_universe_rows']} universe rows, {len(ALL_CONDITIONS)} conditions")
    print(f"watch_retro: build {diag['elapsed_s']:.1f}s, total {elapsed:.1f}s")
    print(f"watch_retro: wrote {CONDITIONS_PATH}")
    print(f"watch_retro: wrote {RETRO_JSON_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
