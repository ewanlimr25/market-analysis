"""Produce the S-C validation report (DESIGN/90 §6) as markdown from data/backtest/sc_*.parquet and,
once it exists, the forward ledger `ledger/sc/`.

    python3 -m engine.validation.run_sc_report [--out data/backtest/sc_report.md]

The in-sample panel is window M. Until every pair holds SC_READ_MIN_WEEKS graded forward entry-weeks
the go / no-go prints NOT DUE and every number here is descriptive (§6: interim readings change nothing).
"""
from __future__ import annotations

import argparse
import json
import os
from datetime import date

import duckdb
import pandas as pd

from engine import backtest_sc as B
from engine import calendar as cal
from engine import ledger as L
from engine.config import LEDGER_SC_DIR, SB_PARAMS, SB_VOL_INDEX, SC_DSR_TRIALS, SC_GO_T_MIN, SC_NW_LAG, SC_READ_MIN_WEEKS
from engine.mart import earnings_events as EE
from engine.mart import index_vol as IV
from engine.strategies import sb_gate as G
from engine.strategies.sa_data import as_dates
from engine.validation import sc_harness as H

PCT = ("mean_ror", "median_ror", "hit", "mean_cost_ror", "worst_ror", "best_ror", "mean_without_worst_1pct",
       "worst_decile_share_of_loss", "mean_f", "mean_m", "mean_pooled", "cost_ror", "ror")
PAIR_COLS = ["pair", "window", "n", "weeks", "mean_ror", "median_ror", "hit", "nw_t", "nw_p", "net_usd_total", "mean_cost_ror"]
STRATA = ("cap_tercile", "iv_tercile", "sector", "regime", "sb_gate", "month")
GATE_UNDERLYING = "SPY"


def section(title: str, body: str) -> str:
    return f"\n## {title}\n\n{body}\n"


def _load(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        return pd.DataFrame()
    return as_dates(pd.read_parquet(path), ("entry", "expiry", "E"))


def load_forward() -> pd.DataFrame:
    """Champion rows of `ledger/sc/` (R5); empty until the ledger opens."""
    if not os.path.isdir(LEDGER_SC_DIR):
        return pd.DataFrame()
    df = L.read_signals(LEDGER_SC_DIR)
    if df.empty:
        return df
    return as_dates(df[df["role"] == "champion"], ("entry", "expiry", "E"))


def with_strata(df: pd.DataFrame, con) -> pd.DataFrame:
    """Adds the two context strata that are not on the rows: the regime label and S-B's gate on entry."""
    if df.empty:
        return df
    entries = sorted(set(df["entry"]))
    regime_fn = EE.default_regime_fn(con)
    iv = IV.on_sessions(IV.load_index_vol(), cal.is_trading_day)
    gate = {d: G.gate(iv, d, cal.prev_session(d), SB_VOL_INDEX[GATE_UNDERLYING], SB_PARAMS).reason for d in entries}
    regime = {d: regime_fn(d) for d in entries}
    return df.assign(regime=df["entry"].map(regime), sb_gate=df["entry"].map(gate))


def tails(df: pd.DataFrame) -> str:
    rows, worst = [], []
    for v, s in H.PAIRS:
        rep = H.tail_report(df, v, s)
        if rep.get("n", 0) == 0:
            continue
        rows.append({k: rep[k] for k in ("pair", "n", "mean_ror", "worst_ror", "best_ror", "worst_decile_share_of_loss",
                                          "realized_stress", "mean_without_worst_1pct", "skew")})
        w = rep["worst_10"].assign(entry=rep["worst_10"]["entry"].astype(str), expiry=rep["worst_10"]["expiry"].astype(str))
        worst.append(f"\nWorst 10 positions, {rep['pair']}:\n\n" + H.md(w, pct_cols=("ror",)))
    return H.md(pd.DataFrame(rows), pct_cols=PCT) + "\n" + "\n".join(worst)


def funnel(suppressed: pd.DataFrame) -> str:
    if suppressed.empty:
        return "_no suppressed table_"
    tab = suppressed.assign(variant=suppressed["variant"].fillna("all")).groupby(["variant", "reason"]).size()
    return H.md(tab.reset_index(name="n"))


def build(con=None) -> str:
    con = con or duckdb.connect()
    ins = with_strata(_load(os.path.join(B.OUT_DIR, "sc_trades.parquet")), con)
    fwd = with_strata(load_forward(), con)
    sup = _load(os.path.join(B.OUT_DIR, "sc_suppressed.parquet"))
    spans = os.path.join(B.OUT_DIR, "sc_inputs.json")
    parts = ["# S-C backtest report (generated)\n",
             section("Inputs", "\n".join(f"- {k}: {v}" for k, v in json.load(open(spans)).items()) if os.path.exists(spans) else "_no sc_inputs.json_")]
    parts.append(section(f"Count trigger (read at {SC_READ_MIN_WEEKS} graded forward entry-weeks per pair)",
                         H.md(H.count_status(fwd), ["pair", "forward_weeks", "required", "status", "scale_required"])))
    if ins.empty:
        return "\n".join(parts + [section("In-sample", "_no sc_trades.parquet; run make backtest-sc_")])
    pool = H.pooled(ins, fwd)
    parts.append(section(f"Mean net return on risk, entry-week series; NW(lag {SC_NW_LAG}) t",
                         H.md(H.pair_table(ins, fwd), PAIR_COLS, pct_cols=PCT)))
    parts.append(section("BH(0.10) across the four pairs (pooled; descriptive before the read)",
                         H.md(H.bh_table(pool), ["pair", "weeks", "mean_ror", "nw_t", "nw_p", "bh_pass"], pct_cols=PCT)))
    parts.append(section(f"Deflated Sharpe ({SC_DSR_TRIALS} trials, weekly series, pooled)",
                         H.md(H.dsr_table(pool), ["pair", "n", "sr", "sr_star", "deflated_sr", "dsr_prob", "sr_star_null", "deflated_sr_null", "dsr_prob_null", "skew", "kurt"])))
    parts.append(section("PBO (CSCV over entry-week blocks; descriptive)", "\n".join(f"- {k}: {v}" for k, v in H.pbo_report(pool).items())))
    parts.append(section("Month rule (net $ by expiry month at the frozen sizing, pooled)",
                         H.md(H.month_table(pool), ["pair", "n_months", "median_month_usd", "worst_month", "worst_month_usd", "worst_over_median", "months_negative", "month_rule_pass"])))
    parts.append(section("Tail (pooled)", tails(pool)))
    for name in STRATA:
        parts.append(section(f"Stratum: {name} (descriptive; cannot promote)", H.md(H.strata_table(pool, name), pct_cols=PCT)))
    parts.append(section("Funnel: suppressed names by first failing filter (all weeks)", funnel(sup)))
    parts.append(section(f"Go / no-go (DESIGN/90 §6; forward t >= {SC_GO_T_MIN}; criterion 4 on the null benchmark)",
                         H.md(H.go_no_go(ins, fwd), None, pct_cols=PCT)))
    return "\n".join(parts)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(B.OUT_DIR, "sc_report.md"))
    a = ap.parse_args()
    text = build()
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with open(a.out, "w") as fh:
        fh.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
