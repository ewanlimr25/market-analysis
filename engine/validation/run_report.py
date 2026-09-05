"""Produce the S-A validation report (DESIGN/70 §4) as markdown from the mart and trades.parquet.

    python3 -m engine.validation.run_report [--out data/backtest/report.md] [--no-rerun]

Sections: §4.3 reproduction of E1 and the two straddle checks; filter funnel; primary season
table; BH per season; deflated Sharpe; PBO; tail; robustness; go/no-go.
"""
from __future__ import annotations

import argparse
import os

import duckdb
import numpy as np
import pandas as pd

from engine import backtest_sa as B
from engine.config import DSR_TRIALS, SAParams
from engine.strategies import sa_data
from engine.validation import harness as H
from engine.validation import stats as S

E1_REFERENCE = {"n": 3260, "mean": 0.015591057918827214, "t": 7.24}   # RESEARCH/40 E1 headline
PCT = ("mean_net_pct", "median_net_pct", "mean_gross_pct", "mean_cost_pct", "mean_s1", "mean_s2", "mean_s3",
       "mean_net_pct_x", "worst_event_pct", "best_event_pct", "mean_win_pct", "mean_without_worst_1pct",
       "mean_without_best_1pct")
PRIMARY_COLS = ["variant", "structure", "season", "n", "dates", "mean_net_pct", "median_net_pct", "hit", "t", "p",
                "mean_gross_pct", "mean_cost_pct", "straddle_over_implied"]


def section(title: str, body: str) -> str:
    return f"\n## {title}\n\n{body}\n"


def reproduction(events: pd.DataFrame, trades: pd.DataFrame) -> str:
    rep = H.reproduce_e1(events, E1_REFERENCE)
    lines = [f"E1 headline from `earnings_events`: N {rep['n']} (ref {rep['ref_n']}), {rep['dates']} pre-dates, "
             f"mean implied−realized {100 * rep['mean']:+.4f}% (ref {100 * rep['ref_mean']:+.4f}%), "
             f"t {rep['t']:.2f} (ref {rep['ref_t']:.2f}) — N match: {rep['n_match']}, mean match: {rep['mean_match']}, t match: {rep['t_match']}."]
    a1 = trades[(trades.variant == "A1") & (trades.structure == "SS")]
    key = ["ticker", "E"]
    m = a1.merge(events[key + ["proxy_pnl"]], on=key, how="left")
    soi = m.straddle_over_implied
    lines.append(f"(a) marked late straddle / vendor implied move on the {len(m)} A1 events: mean {soi.mean():.3f}, "
                 f"median {soi.median():.3f}, IQR {soi.quantile(.25):.3f}–{soi.quantile(.75):.3f} (07-29 spot check: 1.20).")
    lines.append(f"(b) on the same events: proxy (implied−realized) {100 * m.proxy_pnl.mean():+.2f}%, marked SS gross "
                 f"{100 * m.gross_pct.mean():+.2f}%, cost {100 * m.cost_pct.mean():.2f}%, net {100 * m.net_pct.mean():+.2f}% of spot. "
                 f"Gap proxy→gross {100 * (m.proxy_pnl.mean() - m.gross_pct.mean()):+.2f}pp; gross→net {100 * m.cost_pct.mean():.2f}pp.")
    lines.append(f"Mean absolute realized move {100 * m.realized_move.mean():.2f}% vs mean marked straddle "
                 f"{100 * (m.credit_entry / m.spot).mean():.2f}% of spot (the §4.3 comparison); exit debit {100 * (m.debit_exit / m.spot).mean():.2f}%.")
    return "\n\n".join(lines)


def funnel(events: pd.DataFrame, trades: pd.DataFrame, suppressed: pd.DataFrame) -> str:
    counts = suppressed[suppressed.variant == "A1"].first_fail.value_counts()
    order = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8"]
    rows = [{"filter": f, "first_fail_count": int(counts.get(f, 0))} for f in order]
    n_a1 = trades[(trades.variant == "A1") & (trades.structure == "SS")].shape[0]
    n_a2 = trades[(trades.variant == "A2") & (trades.structure == "SS")].shape[0]
    a2_sector = int((suppressed[suppressed.variant == "A2"].first_fail == "A2_sector").sum())
    tab = pd.DataFrame(rows)
    return (f"{len(events)} events → A1 {n_a1} traded, A2 {n_a2} traded (A2 sector cut removed {a2_sector}).\n\n"
            + H.md(tab, ["filter", "first_fail_count"]))


def tiers(trades: pd.DataFrame) -> str:
    a1 = trades[trades.variant == "A1"]
    rows = []
    for s, g in a1.groupby("structure"):
        rows.append({"structure": s, "n": len(g), "entry_tier1": int((g.entry_tier_max == 1).sum()),
                     "entry_tier3_wing": int((g.entry_tier_max == 3).sum()),
                     "exit_tier1": int((g.exit_tier_max == 1).sum()), "exit_tier2": int((g.exit_tier_max == 2).sum()),
                     "exit_tier3_model": int((g.exit_tier_max == 3).sum()),
                     "mean_entry_spread": float(g[["call_entry_spread", "put_entry_spread"]].mean(axis=1).mean()),
                     "mean_exit_spread": float(g[["call_exit_spread", "put_exit_spread"]].mean(axis=1).mean()),
                     "median_dte": float(g.dte.median()), "share_dte_le5": float((g.dte <= 5).mean())})
    return H.md(pd.DataFrame(rows))


def tails(trades: pd.DataFrame, season: str) -> str:
    out = []
    rows = []
    for v, s in H.PAIRS:
        rep = H.tail_report(trades, v, s, season)
        if rep.get("n", 0) == 0:
            continue
        rows.append({k: rep[k] for k in ("variant", "structure", "n", "mean_net_pct", "worst_event_pct", "best_event_pct",
                                          "mean_win_pct", "worst_to_mean_win", "worst_decile_share_of_loss",
                                          "mean_without_worst_1pct", "mean_without_best_1pct", "skew", "kurt", "stress_breaches")})
        if v == "A1":
            out.append(f"\nWorst 10 events, {v} {s} ({season}):\n\n" + H.md(rep["worst_10"].assign(
                E=rep["worst_10"].E.astype(str), pre=rep["worst_10"].pre.astype(str)), pct_cols=("net_pct", "implied", "realized_move")))
    return H.md(pd.DataFrame(rows), pct_cols=PCT) + "\n" + "\n".join(out)


def build(no_rerun: bool) -> str:
    con = duckdb.connect()
    trades = pd.read_parquet(os.path.join(B.OUT_DIR, "trades.parquet"))
    suppressed = pd.read_parquet(os.path.join(B.OUT_DIR, "suppressed.parquet"))
    trades = sa_data.as_dates(trades, ("E", "pre", "post", "expiry"))
    events = sa_data.load_events(con)
    parts = ["# S-A backtest report (generated)\n"]
    parts.append(section("§4.3 reproduction and straddle checks", reproduction(events, trades)))
    parts.append(section("Filter funnel (A1, first failing filter)", funnel(events, trades, suppressed)))
    parts.append(section("Marks and costs by structure (A1)", tiers(trades)))
    parts.append(section("Primary table: mean net P&L in % of notional, t clustered by print date",
                         H.md(H.primary_table(trades), PRIMARY_COLS, pct_cols=PCT)))
    for sea in ("S1", "S2", "pooled"):
        bh = H.bh_table(trades, sea)
        parts.append(section(f"BH(0.10) across the four primary tests — {sea}",
                             H.md(bh, ["variant", "structure", "n", "mean_net_pct", "t", "p", "bh_pass"], pct_cols=PCT)))
    for sea in ("S1", "S2", "pooled"):
        parts.append(section(f"Deflated Sharpe ({DSR_TRIALS} trials) — {sea}",
                             H.md(H.dsr_table(trades, sea), ["variant", "structure", "n", "sr", "sr_star", "deflated_sr", "dsr_prob", "skew", "kurt"])))
    pbo = H.pbo_report(trades, "pooled")
    parts.append(section("PBO (CSCV over 16 print-date blocks, pooled)", "\n".join(f"- {k}: {v}" for k, v in pbo.items())))
    parts.append(section("Tail report — pooled", tails(trades, "pooled")))
    for sea in ("S1", "S2"):
        parts.append(section(f"Tail report — {sea}", tails(trades, sea)))
    rerun = None
    if not no_rerun:
        inputs = B.load_inputs(con)

        def rerun(params: SAParams, cost_mult: float) -> pd.DataFrame:  # noqa: E306
            return sa_data.as_dates(B.run_sa(inputs, params, cost_mult=cost_mult).trades, ("E", "pre", "post", "expiry"))
    rob = H.robustness_table(trades, "pooled", rerun)
    parts.append(section("Robustness (descriptive; cannot promote a configuration) — pooled",
                         H.md(rob, ["sensitivity", "variant", "structure", "n", "dates", "mean_net_pct", "t", "mean_cost_pct"], pct_cols=PCT)))
    parts.append(section("Go / no-go (DESIGN/70 §4.2, read on Season 3 alone)",
                         H.md(H.go_no_go(trades), ["variant", "structure", "n_s3", "mean_s1", "mean_s2", "mean_s3", "t_s3",
                                                   "c1_t_and_bh", "c2_sign_s1_s2", "c3_dsr_positive", "c4_tail", "c5_n60", "verdict", "note"], pct_cols=PCT)))
    return "\n".join(parts)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(B.OUT_DIR, "report.md"))
    ap.add_argument("--no-rerun", action="store_true")
    a = ap.parse_args()
    text = build(a.no_rerun)
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with open(a.out, "w") as fh:
        fh.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
