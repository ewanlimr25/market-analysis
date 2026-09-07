#!/usr/bin/env python3
"""G2 -- intraday flow event study driver (RESEARCH/47-edge-gaps.md §2 G2, DESIGN/60 §4 S-F).

  python3 scripts/intraday_flow.py                  # whole panel: build + analyze
  python3 scripts/intraday_flow.py --days 3          # smoke test on the first 3 panel days
  python3 scripts/intraday_flow.py --force           # rebuild every g2_events/g2_path partition
  python3 scripts/intraday_flow.py --build-only       # skip the analysis / results write
  python3 scripts/intraday_flow.py --analyze-only     # skip the (re)build, use existing partitions

Writes `data/backtest/g2_events/date=*/part.parquet` and `data/backtest/g2_path/date=*/part.parquet`
(this worktree only; never `data/mart`), then
`~/Development/findings/market-analysis/artifacts/edge-gaps/g2/{results.md,results.json}`.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time

import duckdb
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from engine.research import intraday_flow as ifl  # noqa: E402
from engine.research import intraday_flow_cells as cells
from engine.research import intraday_flow_store as store

RESULTS_DIR = os.path.expanduser(
    "~/Development/findings/market-analysis/artifacts/edge-gaps/g2")


def build_panel(days: int | None, force: bool) -> dict:
    """Build (or reuse) every day's g2_events / g2_path partition. Returns a run summary."""
    dates = ifl.panel_dates()
    if days is not None:
        dates = dates[:days]
    con = duckdb.connect()
    t0 = time.perf_counter()
    day_summaries = []
    for d in dates:
        if not force and store.has_partition(store.EVENTS_TABLE, d) and \
                store.has_partition(store.PATH_TABLE, d):
            day_summaries.append({"date": d.isoformat(), "cached": True})
            continue
        build = ifl.build_day(con, d)
        store.write_partition(build.events, store.EVENTS_TABLE, d)
        store.write_partition(build.path, store.PATH_TABLE, d)
        n_events = len(build.events)
        print(f"{d}  {build.n_raw_prints:>9,} prints  {n_events:>6,} events  "
             f"{len(build.path):>6,} path rows  {build.seconds:6.1f}s", flush=True)
        day_summaries.append({"date": d.isoformat(), "cached": False,
                              "n_raw_prints": build.n_raw_prints, "n_events": n_events,
                              "n_path_rows": len(build.path), "seconds": build.seconds})
    total_seconds = time.perf_counter() - t0
    print(f"build: {len(dates)} days, {total_seconds:.1f}s total", flush=True)
    return {"n_days": len(dates), "seconds": total_seconds, "days": day_summaries}


def _outcomes_for_all_days() -> pd.DataFrame:
    """Per-day outcome join (asof matching never crosses days), concatenated."""
    dates = store.available_dates(store.EVENTS_TABLE)
    frames = []
    for d in dates:
        events = store.read_partition(store.EVENTS_TABLE, d)
        if events.empty:
            continue
        path = store.read_partition(store.PATH_TABLE, d)
        frames.append(cells.join_outcomes(events, path))
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame(
        columns=list(cells.OUTCOME_COLUMNS))


def _exclusion_counts(events: pd.DataFrame) -> dict:
    n = len(events)
    return {
        "n_qualifying_events": int(n),
        "n_excluded_direction_mid_or_no_side": int((events["direction"] == "excluded").sum()),
        "n_bullish": int((events["direction"] == "bullish").sum()),
        "n_bearish": int((events["direction"] == "bearish").sum()),
        "n_no_oi_row": int((~events["oi_row_found"]).sum()),
        "n_underlyings": int(events["underlying_symbol"].nunique()),
        "n_days": int(events["date"].nunique()),
    }


def analyze(out_dir: str = RESULTS_DIR, build_summary: dict | None = None) -> dict:
    t0 = time.perf_counter()
    events = store.read_table(store.EVENTS_TABLE)
    exclusions = _exclusion_counts(events) if len(events) else {"n_qualifying_events": 0}
    long_df = _outcomes_for_all_days()
    cell_df = cells.cell_stats(long_df)
    cell_df = cells.add_bh_and_stability(cell_df, long_df)
    descriptive = cells.descriptive_oi_share(events) if len(events) else pd.DataFrame()
    survivors = cell_df[cell_df.get("survivor", pd.Series(dtype=bool)) == True]  # noqa: E712
    seconds = time.perf_counter() - t0
    n_tested = int(cell_df["tested"].sum()) if "tested" in cell_df else 0

    os.makedirs(out_dir, exist_ok=True)
    cell_df.to_json(os.path.join(out_dir, "cells.json"), orient="records", indent=2)
    verdict = ("KILLED: no cell survives BH at q={q} with a sign stable across both halves"
              if len(survivors) == 0 else
              f"NOT KILLED: {len(survivors)} of {n_tested} tested cells survive BH at "
              "q={q} with a sign stable across both halves").format(q=ifl.BH_FDR)
    summary = {
        "n_cells_theoretical": (len(ifl.SIZE_BUCKETS) * len(ifl.DTE_BUCKETS) * len(ifl.TOD_BUCKETS)
                                * len(ifl.CLASSIFICATIONS) * len(ifl.HORIZONS_MIN) * 2),
        "n_cells_tested": n_tested,
        "n_bh_survivors": int(len(survivors)),
        "bh_fdr": ifl.BH_FDR,
        "min_clusters_per_dim": ifl.MIN_CLUSTERS_PER_DIM,
        "exclusions": exclusions,
        "build_seconds": (build_summary or {}).get("seconds"),
        "analysis_seconds": seconds,
        "verdict": verdict,
        "survivors": survivors.to_dict("records"),
    }
    with open(os.path.join(out_dir, "results.json"), "w") as f:
        json.dump(summary, f, indent=2, default=str)
    descriptive.to_json(os.path.join(out_dir, "descriptive_oi_share.json"), orient="records", indent=2)
    print(f"analyze: {len(cell_df)} cells ({summary['n_cells_tested']} tested), "
         f"{summary['n_bh_survivors']} BH survivors, {seconds:.1f}s", flush=True)
    return {"summary": summary, "cell_df": cell_df, "descriptive": descriptive}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--days", type=int, default=None, help="limit to the first N panel days (smoke test)")
    ap.add_argument("--force", action="store_true", help="rebuild every day's partitions")
    ap.add_argument("--build-only", action="store_true")
    ap.add_argument("--analyze-only", action="store_true")
    ap.add_argument("--out-dir", default=RESULTS_DIR)
    args = ap.parse_args(argv)

    build_summary = None if args.analyze_only else build_panel(args.days, args.force)
    if not args.build_only:
        analyze(args.out_dir, build_summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
