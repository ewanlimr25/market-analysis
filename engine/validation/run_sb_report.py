"""Produce the S-B validation report (DESIGN/80 §6) as markdown from data/backtest/sb_*.parquet.

    python3 -m engine.validation.run_sb_report [--out data/backtest/sb_report.md]
"""
from __future__ import annotations

import argparse
import json
import os

import numpy as np
import pandas as pd

from engine import backtest_sb as B
from engine.config import SB_DSR_TRIALS, SB_GO_T_MIN, SB_NW_LAG, SB_WINDOWS
from engine.strategies.sa_data import as_dates
from engine.validation import sb_harness as H
from engine.validation.sb_alt_structures import TABLE_COLS as ALT_COLS, alt_structure_table
from engine.validation.sb_glossary import appendix

PCT = ("worst_ror", "mean_ror", "median_ror", "mean_marked", "mean_proxy", "mean_p1", "mean_p2", "mean_p3", "marked_mean_ror",
       "proxy_mean_ror", "gap_ror", "marked_cost_ror", "worst_ror", "best_ror", "mean_win_ror", "mean_without_worst_1pct",
       "mean_without_best_1pct", "mean_credit_over_width", "mean_cost_over_credit", "hit", "ror")
SLEEVE_COLS = ["sleeve", "window", "n", "expiries", "mean_ror", "median_ror", "hit", "nw_t", "nw_p", "cl_t", "cl_p",
               "net_usd_total", "mean_credit_over_width", "mean_cost_over_credit", "mean_x", "mean_risk_usd"]


def section(title: str, body: str) -> str:
    return f"\n## {title}\n\n{body}\n"


def _load(name: str) -> pd.DataFrame:
    path = os.path.join(B.OUT_DIR, name)
    if not os.path.exists(path):
        return pd.DataFrame()
    df = pd.read_parquet(path)
    return as_dates(df, ("entry", "expiry", "gate_asof", "E", "pre", "post"))


def inputs_section() -> str:
    path = os.path.join(B.OUT_DIR, "sb_inputs.json")
    if not os.path.exists(path):
        return "_no sb_inputs.json_"
    spans = json.load(open(path))
    return "\n".join(f"- {k}: {v}" for k, v in spans.items())


def gate_share(sens: pd.DataFrame) -> str:
    if sens.empty:
        return "_no proxy positions_"
    base, off = sens[sens.sensitivity == "base"], sens[sens.sensitivity == "gate_off"]
    rows = []
    for u in sorted(set(off.underlying)):
        b, o = base[(base.underlying == u) & (base.structure == "PS")], off[(off.underlying == u) & (off.structure == "PS")]
        years = sorted(set(o.entry.map(lambda d: d.year)))
        for y in years:
            n_on, n_all = int((b.entry.map(lambda d: d.year) == y).sum()), int((o.entry.map(lambda d: d.year) == y).sum())
            rows.append({"underlying": u, "year": y, "entry_sessions": n_all, "gate_on": n_on, "on_share": n_on / n_all if n_all else np.nan})
        rows.append({"underlying": u, "year": "all", "entry_sessions": len(o), "gate_on": len(b), "on_share": len(b) / len(o) if len(o) else np.nan})
    return H.md(pd.DataFrame(rows), pct_cols=("on_share",))


def tails(df: pd.DataFrame) -> str:
    rows, worst = [], []
    for u, s in H.SLEEVES:
        rep = H.tail_report(df, u, s)
        if rep.get("n", 0) == 0:
            continue
        rows.append({k: rep[k] for k in ("sleeve", "n", "mean_ror", "worst_ror", "worst_entry", "best_ror", "mean_win_ror",
                                          "worst_decile_share_of_loss", "full_width_losses", "mean_without_worst_1pct",
                                          "mean_without_best_1pct", "skew", "kurt")})
        if s == "PS":
            w = rep["worst_10"].assign(entry=rep["worst_10"].entry.astype(str), expiry=rep["worst_10"].expiry.astype(str))
            worst.append(f"\nWorst 10 positions, {rep['sleeve']} (pooled):\n\n" + H.md(w, pct_cols=("ror",)))
    return H.md(pd.DataFrame(rows), pct_cols=PCT) + "\n" + "\n".join(worst)


def build() -> str:
    proxy, proxy_sens = _load("sb_proxy.parquet"), _load("sb_proxy_sens.parquet")
    marked, marked_sens, skipped = _load("sb_marked.parquet"), _load("sb_marked_sens.parquet"), _load("sb_marked_skipped.parquet")
    parts = ["# S-B backtest report (generated)\n", section("Inputs", inputs_section())]
    parts.append(section("Gate ON share of entry sessions (proxy, by year)", gate_share(proxy_sens)))
    parts.append(section(f"Proxy: mean net return on risk per position; NW(lag {SB_NW_LAG}) t and expiry-clustered t",
                         H.md(H.sleeve_table(proxy), SLEEVE_COLS, pct_cols=PCT) if len(proxy) else "_no proxy positions_"))
    if len(proxy):
        parts.append(section("BH(0.10) across the four sleeves (proxy, pooled, on the NW p)",
                             H.md(H.bh_table(proxy), ["sleeve", "n", "mean_ror", "nw_t", "nw_p", "bh_pass"], pct_cols=PCT)))
        for w in ("pooled",) + tuple(SB_WINDOWS):
            parts.append(section(f"Deflated Sharpe ({SB_DSR_TRIALS} trials) — proxy {w}",
                                 H.md(H.dsr_table(proxy, w), ["sleeve", "n", "sr", "sr_star", "deflated_sr", "dsr_prob", "sr_star_null", "deflated_sr_null", "dsr_prob_null", "skew", "kurt"])))
        parts.append(section("PBO (CSCV over 16 entry blocks, proxy pooled)", "\n".join(f"- {k}: {v}" for k, v in H.pbo_report(proxy).items())))
        parts.append(section("Month rule (proxy; worst expiry-month vs median month, $ at frozen sizing)",
                             H.md(H.monthly_table(proxy), ["sleeve", "n_months", "median_month_usd", "worst_month", "worst_month_usd",
                                                           "worst_over_median", "months_negative", "month_rule_pass"])))
        parts.append(section("Tail report (proxy, pooled)", tails(proxy)))
        parts.append(section("Gate modes and sensitivities (proxy, pooled; descriptive)",
                             H.md(H.gate_table(proxy_sens), ["sensitivity", "sleeve", "n", "mean_ror", "nw_t", "cl_t", "net_usd_total", "mean_cost_over_credit"], pct_cols=PCT)))
        alt = alt_structure_table(proxy_sens)
        parts.append(section("Other structures on the proxy (descriptive; not sleeves, never a verdict input)",
                             ("Single legs, naked shorts and the call spread re-priced on the same entry rows with the frozen "
                              "smile and costs. Risk: debit = premium; credit spread = width - credit; naked = the 2-sigma "
                              "stress loss (the matching spread's max loss), Reg-T proxy margin beside. `PS` here is the "
                              "champion recomputed as a check. Drafts: `ledger/challengers/drafts/sb-c-callspread.json`, "
                              "`sb-c-nakedput-margin.json`.\n\n" + H.md(alt, ALT_COLS, pct_cols=PCT)) if len(alt) else "_no sensitivities_"))
    parts.append(section("Marked (panel): sleeve table", H.md(H.sleeve_table(marked, ("P3",)), SLEEVE_COLS, pct_cols=PCT) if len(marked) else "_no marked positions_"))
    if len(marked):
        parts.append(section("Marked vs proxy on the same positions (§6.7 criterion 2)",
                             H.md(H.overlap_table(marked, proxy), ["sleeve", "n_marked", "n_overlap", "marked_mean_ror", "proxy_mean_ror", "gap_ror", "marked_cost_ror", "overlap_pass"], pct_cols=PCT)))
        tiers = marked.groupby(["underlying", "structure"]).agg(n=("entry", "size"), graded=("graded", "sum"), entry_tier_max=("entry_tier_max", "max"),
                                                                mean_credit=("credit_entry", "mean"), mean_width=("width", "mean"), mean_cost_over_credit=("cost_over_credit", "mean")).reset_index()
        parts.append(section("Marked: tiers, credit, width, cost", H.md(tiers, pct_cols=("mean_cost_over_credit",))))
        if len(skipped):
            parts.append(section("Marked: skipped entries by reason", H.md(skipped.groupby(["underlying", "structure", "reason"]).size().reset_index(name="n"))))
        parts.append(section("Marked sensitivities (descriptive)",
                             H.md(H.gate_table(marked_sens), ["sensitivity", "sleeve", "n", "mean_ror", "nw_t", "net_usd_total"], pct_cols=PCT)))
    parts.append(section(f"Go / no-go (DESIGN/80 §6.7; t >= {SB_GO_T_MIN}; read 2026-12-01)",
                         H.md(H.go_no_go(proxy, marked), ["sleeve", "n_proxy", "mean_proxy", "nw_t_proxy", "bh_pass", "mean_p1", "mean_p2", "mean_p3",
                                                         "n_marked", "mean_marked", "gap_ror", "worst_over_median", "deflated_sr", "deflated_sr_null", "forward_n",
                                                         "c1_proxy", "c2_marked", "c3_month", "c4_dsr", "c4_dsr_null", "c5_scale", "verdict", "note"], pct_cols=PCT)
                         if len(proxy) else "_no proxy positions_"))
    parts.append(appendix())
    return "\n".join(parts)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(B.OUT_DIR, "sb_report.md"))
    a = ap.parse_args()
    text = build()
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with open(a.out, "w") as fh:
        fh.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
