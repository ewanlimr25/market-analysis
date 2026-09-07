"""Produce the S-G validation report (DESIGN/91 §6 G5) as markdown from `data/backtest/g3_*.parquet`.

    python3 -m engine.validation.run_report_sg [--out data/backtest/g3_report.md]

Sections: funnel; marks and tiers; primary season table; BH per season; deflated Sharpe (10-trial
charge); PBO; tail; spread halves; the gross ramp decomposition; go/no-go (DESIGN/91 §4).
"""
from __future__ import annotations

import argparse
import os

import duckdb
import pandas as pd

from engine.backtest_sg import OUT_DIR
from engine.config import SG_BH_FDR, SG_DSR_TRIALS, SG_PARAMS
from engine.strategies import sg_data
from engine.validation import harness as H
from engine.validation import sg_harness as SH

PCT = ("mean_net_pct", "median_net_pct", "mean_gross_pct", "mean_cost_pct", "mean_s1", "mean_s2",
      "mean_pooled", "mean_low_spread", "mean_wide_spread", "worst_event_pct", "best_event_pct",
      "mean_win_pct", "mean_without_worst_1pct", "mean_without_best_1pct", "unhedged_pnl_pct",
      "delta_pnl_pct", "delta_hedged_pnl_pct", "vega_pnl_pct", "residual_pnl_pct", "net_pct_prem")
PRIMARY_COLS = ["variant", "structure", "season", "n", "dates", "mean_net_pct", "median_net_pct", "hit", "t", "p",
               "mean_gross_pct", "mean_cost_pct"]


def section(title: str, body: str) -> str:
    return f"\n## {title}\n\n{body}\n"


def funnel(events: pd.DataFrame, trades: pd.DataFrame, suppressed: pd.DataFrame, dropped: pd.DataFrame) -> str:
    lines = [f"{len(events)} events x {len(SG_PARAMS.entry_offsets)} entry offsets evaluated."]
    for offset in SG_PARAMS.entry_offsets:
        sub = suppressed[suppressed.offset == offset]
        counts = sub.first_fail.value_counts()
        tab = pd.DataFrame([{"filter": f, "first_fail_count": int(counts.get(f, 0))} for f in
                            ("F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8")])
        n_ls = len(trades[(trades.offset == offset) & (trades.structure == "LS")])
        n_lg = len(trades[(trades.offset == offset) & (trades.structure == "LG")])
        n_lg_dropped = len(dropped[(dropped.offset == offset) & (dropped.structure == "LG")])
        lines.append(f"\n**offset −{offset}**: LS traded {n_ls}, LG traded {n_lg} "
                     f"(LG dropped {n_lg_dropped}: {dropped[(dropped.offset == offset) & (dropped.structure == 'LG')].reason.value_counts().to_dict() if n_lg_dropped else {}})\n\n"
                     + H.md(tab, ["filter", "first_fail_count"]))
    return "\n".join(lines)


def tiers(trades: pd.DataFrame) -> str:
    rows = []
    for (v, s), g in trades.groupby(["variant", "structure"]):
        rows.append({"variant": v, "structure": s, "n": len(g),
                    "entry_tier1": int((g.entry_tier_max == 1).sum()), "entry_model": int((g.entry_tier_max == 3).sum()),
                    "exit_tier1": int((g.exit_tier_max == 1).sum()), "exit_tier2": int((g.exit_tier_max == 2).sum()),
                    "exit_model": int((g.exit_tier_max == 3).sum()), "mean_atm_spread_entry": float(g.atm_spread_entry.mean()),
                    "median_dte": float(g.dte.median())})
    return H.md(pd.DataFrame(rows))


def tails(trades: pd.DataFrame, season: str) -> str:
    rows = []
    for v, s in SH.SG_PAIRS:
        rep = SH.tail_report(trades, v, s, season)
        if rep.get("n", 0) == 0:
            continue
        rows.append({k: rep[k] for k in ("variant", "structure", "n", "mean_net_pct", "worst_event_pct",
                                          "best_event_pct", "mean_win_pct", "worst_to_mean_win",
                                          "worst_decile_share_of_loss", "mean_without_worst_1pct",
                                          "mean_without_best_1pct", "skew", "kurt")})
    return H.md(pd.DataFrame(rows), pct_cols=PCT)


def build() -> str:
    trades = pd.read_parquet(os.path.join(OUT_DIR, "g3_trades.parquet"))
    suppressed = pd.read_parquet(os.path.join(OUT_DIR, "g3_suppressed.parquet"))
    dropped = pd.read_parquet(os.path.join(OUT_DIR, "g3_dropped.parquet"))
    events = sg_data.load_events(duckdb.connect())
    parts = ["# S-G backtest report (generated, DESIGN/91)\n"]
    parts.append(section("Filter funnel by entry offset", funnel(events, trades, suppressed, dropped)))
    parts.append(section("Marks and tiers by (offset, structure)", tiers(trades)))
    parts.append(section("Primary table: mean net P&L in % of spot, t clustered by entry day",
                         H.md(SH.primary_table(trades), PRIMARY_COLS, pct_cols=PCT)))
    for sea in ("S1", "S2", H.POOLED):
        bh = SH.bh_table(trades, sea)
        parts.append(section(f"BH({SG_BH_FDR}) across the four primary tests — {sea}",
                             H.md(bh, ["variant", "structure", "n", "mean_net_pct", "t", "p", "bh_pass"], pct_cols=PCT)))
    for sea in ("S1", "S2", H.POOLED):
        dsr = SH.dsr_table(trades, sea)
        parts.append(section(f"Deflated Sharpe ({SG_DSR_TRIALS} trials) — {sea}",
                             H.md(dsr, ["variant", "structure", "n", "sr", "sr_star", "deflated_sr", "dsr_prob", "skew", "kurt"])))
    pbo = SH.pbo_report(trades)
    parts.append(section("PBO (CSCV over entry-day blocks, pooled)", "\n".join(f"- {k}: {v}" for k, v in pbo.items())))
    parts.append(section("Tail report — pooled", tails(trades, H.POOLED)))
    for sea in ("S1", "S2"):
        parts.append(section(f"Tail report — {sea}", tails(trades, sea)))
    median = SH.spread_median(trades)
    halves = SH.spread_half_table(trades, median)
    parts.append(section(f"Spread halves (median atm_spread_entry on G3a-LS = {median:.4f})",
                         H.md(halves, ["half", "variant", "structure", "n", "mean_net_pct", "t"], pct_cols=PCT)))
    decomp_season = SH.decomposition_summary(trades, ("season",))
    decomp_half = SH.decomposition_summary(trades.assign(spread_half=(trades.atm_spread_entry > median).map({True: "wide", False: "low"})),
                                           ("spread_half",))
    parts.append(section("Gross ramp decomposition (G3a-LS): by season", H.md(decomp_season, pct_cols=PCT)))
    parts.append(section("Gross ramp decomposition (G3a-LS): by spread half", H.md(decomp_half, pct_cols=PCT)))
    parts.append(section("Go / no-go (DESIGN/91 §4)",
                         H.md(SH.go_no_go(trades), ["variant", "structure", "n_s1", "n_s2", "mean_s1", "mean_s2",
                                                   "mean_pooled", "t_pooled", "mean_low_spread", "mean_wide_spread",
                                                   "verdict", "note"], pct_cols=PCT)))
    return "\n".join(parts)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(OUT_DIR, "g3_report.md"))
    a = ap.parse_args()
    text = build()
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with open(a.out, "w") as fh:
        fh.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
