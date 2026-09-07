#!/usr/bin/env python3
"""G1 step 2 (RESEARCH/47 §2 G1): re-mark the frozen 612 S-A trade rows.

Reads `data/backtest/trades.parquet` (never writes it) and `data/backtest/g1_fills.parquet`
(from `scripts/fills.py`). Builds fresh exit marks for the two treatment-b windows (b1 =
10:30-11:30, b2 = 14:30-15:30) from raw All Options prints on each row's `post` date, using
`marking.print_mark` for tiers 1-2 (the exact champion mark logic, presented as a `late`-shaped
row so the real function applies unmodified — RESEARCH/47 has no separate custom-window marker)
and `marking.model_mark` plus the champion's own smile-scaled IV closure
(`strategies.sa_data.build_model_inputs`) for tier 3 (spot proxy: the underlying's close on
`post`, the same fallback `sa_data` already uses for any window other than `early`).

Five treatments per row: orig (unchanged), a (mid-fill cost only), b1, b2 (window move only),
ab1, ab2 (both). Writes `data/backtest/g1_remarked.parquet` (trades.parquet's columns plus one
net_usd/net_pct/cost_usd/gross_usd/n_legs block per non-orig treatment) and prints the
season-split table (`engine.validation.stats.cluster_t`, clustered by `pre`) for A1-SS, A1-IC,
A2-SS, A2-IC under all five, plus the RESEARCH/47 kill-rule verdict.

    python3 scripts/g1_remark.py [--out data/backtest]
"""
from __future__ import annotations

import argparse
import os
import sys
import time
from datetime import date

import duckdb
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from engine import marking as M                                            # noqa: E402
from engine.backtest_sa import load_inputs                                 # noqa: E402
from engine.config import ALL_OPTIONS_FILE, DATA, STOCKS, TIER1_MIN_SIZE   # noqa: E402
from engine.improve import fills as G                                      # noqa: E402
from engine.improve import g1_remark as R                                  # noqa: E402
from engine.strategies import sa_data                                      # noqa: E402
from engine.validation.stats import cluster_t                              # noqa: E402

OUT_DIR = os.path.join(DATA, "backtest")
TRADES_PATH = os.path.join(OUT_DIR, "trades.parquet")
FILLS_PATH = os.path.join(OUT_DIR, "g1_fills.parquet")
TREATMENTS = ("a", "b1", "b2", "ab1", "ab2")
WINDOW_TREATMENTS = {"b1": G.WINDOW_B1, "b2": G.WINDOW_B2, "ab1": G.WINDOW_B1, "ab2": G.WINDOW_B2}
VARIANT_STRUCTURES = (("A1", "SS"), ("A1", "IC"), ("A2", "SS"), ("A2", "IC"))


# ----------------------------------------------------------------------------- new exit marks (b1 / b2)


def _needed_ids_and_dates(trades: pd.DataFrame) -> tuple[set[str], set[date]]:
    ids, dates = set(), set()
    for leg in R.ALL_LEGS:
        col = trades[f"{leg}_id"].dropna()
        ids.update(col.tolist())
    dates.update(pd.to_datetime(trades["post"]).dt.date.tolist())
    return ids, dates


def _files_for_dates(dates: set[date], stocks: str) -> list[str]:
    out = []
    for d in sorted(dates):
        p = os.path.join(stocks, ALL_OPTIONS_FILE.format(d=d.isoformat()))
        if os.path.exists(p):
            out.append(p)
    return out


def build_window_rows(con, files: list[str], ids: set[str], window: str) -> pd.DataFrame:
    """Per (option_chain_id, date), VWAP / size / last bid-ask inside `window` (RESEARCH/20 §2.5
    prints are session-clean; same NOT canceled / size>0 / price>0 filter as `mart/daily_contract.py`)."""
    if not files or not ids:
        return pd.DataFrame(columns=["option_chain_id", "date", "vwap", "size_win", "last_bid", "last_ask"])
    lo, hi = G.CANDIDATE_WINDOWS[window]
    con.register("want_ids", pd.DataFrame({"option_chain_id": sorted(ids)}))
    sql = f"""
    WITH pr AS (
      SELECT t.option_chain_id AS option_chain_id,
             (t.executed_at AT TIME ZONE 'America/New_York')::TIMESTAMP AS et,
             t.price AS price, t.size AS size, t.nbbo_bid AS nbbo_bid, t.nbbo_ask AS nbbo_ask
      FROM read_parquet({files!r}) t
      JOIN want_ids w ON w.option_chain_id = t.option_chain_id
      WHERE NOT t.canceled AND t.size > 0 AND t.price > 0
        AND et::TIME >= TIME '{lo}' AND et::TIME <= TIME '{hi}'
    )
    SELECT option_chain_id, et::DATE AS date,
           sum(price * size) / nullif(sum(size), 0) AS vwap, sum(size) AS size_win,
           arg_max(nbbo_bid, et) AS last_bid, arg_max(nbbo_ask, et) AS last_ask
    FROM pr GROUP BY 1, 2
    """
    return con.execute(sql).df()


def _row_from_window(win_row) -> dict:
    return {"vwap_late": win_row.vwap, "size_late": win_row.size_win, "late_rel_spread": None,
            "late_last_bid": win_row.last_bid, "late_last_ask": win_row.last_ask,
            "last_nbbo_bid": win_row.last_bid, "last_nbbo_ask": win_row.last_ask}


def build_new_exit_marks(con, trades: pd.DataFrame, window: str, stocks: str = STOCKS) -> dict:
    """row index -> {leg: Mark | None} for every present leg, marked inside `window` on that
    row's `post` date. Tier 1-2 from real prints (`marking.print_mark`); tier 3 (no print in the
    window) from `marking.model_mark` with the champion's smile-scaled IV and this window's DTE."""
    ids, dates = _needed_ids_and_dates(trades)
    files = _files_for_dates(dates, stocks)
    win = build_window_rows(con, files, ids, window)
    by_key = {(r.option_chain_id, r.date): r for r in win.itertuples()}

    inputs = load_inputs(con)
    model_inputs = sa_data.build_model_inputs(inputs["prices"], inputs["iv30d"], inputs["spreads"],
                                              inputs["wing_hist"], inputs["spread_key"])

    out: dict[int, dict[str, M.Mark | None]] = {}
    for idx, row in trades.iterrows():
        d = row["post"]
        marks: dict[str, M.Mark | None] = {}
        for leg in R.present_legs(row):
            cid = row[f"{leg}_id"]
            w = by_key.get((cid, d))
            mark = M.print_mark(_row_from_window(w), M.WHEN_LATE, TIER1_MIN_SIZE) if w is not None else None
            if mark is None:
                contract = R.contract_for_leg(row, leg)
                mi = model_inputs(contract, d, window)
                mark = M.model_mark(mi.spot, contract.strike, (contract.expiry - d).days, mi.iv,
                                    contract.option_type, mi.rel_spread) if mi is not None else None
            marks[leg] = mark
        out[idx] = marks
    return out


# ----------------------------------------------------------------------------- driver


def run(out_dir: str = OUT_DIR, stocks: str = STOCKS) -> pd.DataFrame:
    trades = pd.read_parquet(TRADES_PATH)
    fills = pd.read_parquet(FILLS_PATH)
    lookup = R.build_mid_share_lookup(fills[fills.cut == "window"])

    con = duckdb.connect()
    con.execute("PRAGMA threads=8")

    out = trades
    out = R.apply_treatment(out, "a", lookup, exit_window=G.WINDOW_EARLY, apply_a=True)
    b_marks: dict[str, dict] = {}
    for wt in ("b1", "b2"):
        window = WINDOW_TREATMENTS[wt]
        b_marks[wt] = build_new_exit_marks(con, trades, window, stocks)
        out = R.apply_treatment(out, wt, lookup=None, exit_window=window,
                                exit_marks_by_row=b_marks[wt], apply_a=False)
    for wt, base in (("ab1", "b1"), ("ab2", "b2")):
        window = WINDOW_TREATMENTS[wt]
        out = R.apply_treatment(out, wt, lookup, exit_window=window,
                                exit_marks_by_row=b_marks[base], apply_a=True)

    os.makedirs(out_dir, exist_ok=True)
    out.to_parquet(os.path.join(out_dir, "g1_remarked.parquet"), index=False)
    return out


# ----------------------------------------------------------------------------- season-split report
# Reuses `trades.parquet`'s own `season` column (RESEARCH/45 §4: S1/S2/off on `pre`, frozen by
# `earnings_events`) rather than recomputing the boundary, so the split cannot drift from §4's.


def season_table(remarked: pd.DataFrame) -> pd.DataFrame:
    rows = []
    net_cols = {"orig": "net_pct"} | {t: f"net_pct_{t}" for t in TREATMENTS}
    for variant, structure in VARIANT_STRUCTURES:
        sub = remarked[(remarked.variant == variant) & (remarked.structure == structure)]
        for season in ("S1", "S2"):
            s = sub[sub.season == season]
            for treatment, col in net_cols.items():
                r = cluster_t(s[col], s["pre"])
                rows.append({"variant": variant, "structure": structure, "season": season,
                            "treatment": treatment, **r})
    return pd.DataFrame(rows)


def kill_rule_verdict(table: pd.DataFrame) -> str:
    """RESEARCH/47 §2 G1: if the re-marked A1-SS net is still <= 0 in either season, G1 closes."""
    a1_ss = table[(table.variant == "A1") & (table.structure == "SS") & (table.treatment != "orig")]
    still_losing = a1_ss[a1_ss["mean"] <= 0]
    if len(still_losing):
        cells = ", ".join(f"{r.treatment}/{r.season}" for r in still_losing.itertuples())
        return f"CLOSED: A1-SS net <= 0 under {cells} (RESEARCH/47 kill rule)"
    return "NOT CLOSED: every re-marking treatment lifts A1-SS net > 0 in both seasons"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=OUT_DIR)
    ap.add_argument("--stocks", default=STOCKS)
    args = ap.parse_args()

    t0 = time.time()
    remarked = run(args.out, args.stocks)
    table = season_table(remarked)
    pd.set_option("display.width", 200)
    print(table[["variant", "structure", "season", "treatment", "n", "mean", "median", "hit", "t", "p"]]
         .to_string(index=False))
    verdict = kill_rule_verdict(table)
    print(f"\nVERDICT: {verdict}")
    table.to_csv(os.path.join(args.out, "g1_remark_season_table.csv"), index=False)
    print(f"\n{time.time() - t0:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
