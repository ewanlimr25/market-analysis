#!/usr/bin/env python3
"""G10: S-B challengers from the CBOE vol-index family, on the three-year proxy (`engine.improve.sb_challengers`).

  python3 scripts/sb_challengers.py                      # table to stdout, writes data/backtest/g10_sb_challengers.*
  python3 scripts/sb_challengers.py --refresh-ext         # also refetch VVIX/SKEW (network) before running
  python3 scripts/sb_challengers.py --drafts              # also write the registration drafts under ledger/challengers/drafts/

Every challenger is an ADDITIONAL condition on top of the frozen champion gate (`sb_gate.py`,
unedited); nothing here selects a "best" threshold -- every grid value is run and reported. Drafts
are not registrations: `registered` is the non-ISO marker `PENDING-2026-12-01` so they cannot be
mistaken for a live one before the 2026-12-01 read (D22).
"""
from __future__ import annotations

import argparse
import json
import os
import sys

import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from engine import backtest_sb as BT                              # noqa: E402
from engine import config                                         # noqa: E402
from engine.improve import sb_challengers as C                    # noqa: E402
from engine.mart import index_vol_ext as EXT                      # noqa: E402
from engine.strategies import sb_proxy as P                       # noqa: E402
from engine.validation import sb_harness as H                     # noqa: E402

OUT_DIR = os.path.join(config.DATA, "backtest")
DRAFTS_DIR = os.path.join(config.LEDGER_DIR, "challengers", "drafts")


def _write_atomic_parquet(df: pd.DataFrame, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    df.to_parquet(tmp, index=False)
    os.replace(tmp, path)


def write_drafts(summary: pd.DataFrame, plan: dict) -> list[str]:
    os.makedirs(DRAFTS_DIR, exist_ok=True)
    written = []
    for ch in C.CHALLENGERS:
        sub = summary[summary["challenger_id"] == ch.challenger_id]
        best = sub.loc[sub["mean_ror"].idxmax()] if len(sub) and sub["mean_ror"].notna().any() else None
        sleeve = str(best["sleeve"]) if best is not None else H.sleeve_name(*H.SLEEVES[0])
        draft = C.draft_registration(ch, sleeve, plan)
        path = os.path.join(DRAFTS_DIR, f"{ch.challenger_id}.json")
        with open(path, "w") as fh:
            json.dump(draft, fh, indent=1)
            fh.write("\n")
        written.append(path)
    return written


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh-ext", action="store_true", help="refetch VVIX/SKEW (network) before running")
    ap.add_argument("--drafts", action="store_true", help="also write ledger/challengers/drafts/sb-c-*.json")
    ap.add_argument("--out", default=OUT_DIR)
    a = ap.parse_args()
    if a.refresh_ext:
        EXT.refresh()
    inputs = BT.proxy_inputs()
    ext = EXT.load_index_vol_ext()
    merged = C.merged_vol_frame(inputs.index_vol, ext)
    champion = P.run_proxy(inputs, gate_mode="both")
    summary = C.build_summary(inputs, merged, champion)
    _write_atomic_parquet(summary, os.path.join(a.out, "g10_sb_challengers.parquet"))
    plan = C.power_plan()
    meta = {"trial_count": C.TRIAL_COUNT, "min_effect": C.CHALLENGER_MIN_EFFECT, "power_plan": plan,
           "entries_total": C.total_entry_weeks(inputs), "champion_n": int(len(champion))}
    with open(os.path.join(a.out, "g10_sb_challengers.json"), "w") as fh:
        json.dump(meta, fh, indent=1, default=str)
    if a.drafts:
        written = write_drafts(summary, plan)
        print(f"wrote {len(written)} drafts under {DRAFTS_DIR}")
    with pd.option_context("display.width", 200, "display.max_columns", 30):
        print(summary[["challenger_id", "sleeve", "footprint", "n_positions", "mean_ror", "nw_t",
                       "units_lost_diff", "units_lost_t", "matched_max_abs_diff"]].to_string(index=False))
    print(f"\n{C.TRIAL_COUNT} distinct challenger trials, {len(summary)} sleeve-level rows -> {a.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
