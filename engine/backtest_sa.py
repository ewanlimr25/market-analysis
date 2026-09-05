"""Run S-A over the mart and write trades.parquet / suppressed.parquet (DESIGN/70 §3.4, §7 P4).

Two passes: select legs for every event to learn which contracts must be marked on `post`
(and which wing contracts need an IV lookback), load exactly those rows, then evaluate.
"""
from __future__ import annotations

import argparse
import os
import time
from datetime import date

import duckdb
import pandas as pd

from engine import marking as M
from engine.config import DATA, SA_PARAMS, SIZING, SAParams, SizingParams
from engine import portfolio
from engine.strategies import sa, sa_data
from engine.strategies import sa_filters as F
from engine.strategies import sa_structures as ST

OUT_DIR = os.path.join(DATA, "backtest")
# the widest F3 band any pre-registered sensitivity uses (DESIGN/70 §4.1 robustness report)
LOAD_MCAP_LO, LOAD_MCAP_HI = 1e9, 100e9


def _selections(events: pd.DataFrame, pre_rows: pd.DataFrame, params: SAParams) -> list[tuple[dict, sa.Selection]]:
    groups = {k: g for k, g in pre_rows.groupby(["underlying_symbol", "date"], sort=False)}
    out = []
    for ev in events.to_dict("records"):
        rows = groups.get((ev["ticker"], F.to_date(ev["pre"])))
        if rows is None:
            continue
        sel, _ = sa.select_legs(ev, rows, params)
        if sel is not None:
            out.append((ev, sel))
    return out


def _leg_ids(ev: dict, sel: sa.Selection) -> tuple[list[str], list[str]]:
    sym = ev["ticker"]
    atm = [ST.osi_id(sym, sel.expiry, t, sel.pair.strike) for t in ("call", "put")]
    wings = [ST.osi_id(sym, sel.expiry, "call", sel.k_up), ST.osi_id(sym, sel.expiry, "put", sel.k_dn)]
    return atm, wings


def load_inputs(con, params: SAParams = SA_PARAMS) -> dict:
    t0 = time.time()
    events = sa_data.load_events(con)
    pre_rows = sa_data.load_pre_rows(con, events, LOAD_MCAP_LO, LOAD_MCAP_HI)
    wide = SAParams(**{**params.__dict__, "mcap_min": LOAD_MCAP_LO, "mcap_max": LOAD_MCAP_HI})
    picks = _selections(events, pre_rows, wide)
    ids, wing_ids, posts, pres = set(), set(), set(), set()
    for ev, sel in picks:
        atm, wings = _leg_ids(ev, sel)
        ids.update(atm + wings)
        wing_ids.update(wings)
        posts.add(F.to_date(ev["post"]))
        pres.add(F.to_date(ev["pre"]))
    hist_dates = sa_data.history_dates(posts)
    exit_rows = sa_data.load_rows_for_contracts(con, ids, posts)
    wing_hist = sa_data.load_rows_for_contracts(con, wing_ids, hist_dates | pres)
    tickers = {ev["ticker"] for ev, _ in picks}
    all_dates = posts | pres | hist_dates
    prices = sa_data.load_prices(con, tickers, all_dates)
    iv30d = sa_data.load_iv30d(con, tickers, all_dates)
    spreads = sa_data.load_spread_history(con, events)
    spread_key = {(ev["ticker"], F.to_date(ev["post"])): (ev["ticker"], F.to_date(ev["pre"])) for ev, _ in picks}
    print(f"loaded: {len(events)} events, {len(pre_rows)} pre rows, {len(picks)} selectable, "
          f"{len(exit_rows)} exit rows, {len(wing_hist)} wing-history rows ({time.time() - t0:.1f}s)")
    return {"events": events, "pre_rows": pre_rows, "exit_rows": exit_rows, "wing_hist": wing_hist,
            "prices": prices, "iv30d": iv30d, "spreads": spreads, "spread_key": spread_key}


def build_resolver(inputs: dict) -> M.MarkResolver:
    rows = {}
    for df in (inputs["pre_rows"], inputs["exit_rows"], inputs["wing_hist"]):
        if len(df):
            for r in df.to_dict("records"):
                rows[(r["option_chain_id"], F.to_date(r["date"]))] = r
    model = sa_data.build_model_inputs(inputs["prices"], inputs["iv30d"], inputs["spreads"],
                                       inputs["wing_hist"], inputs["spread_key"])
    return M.MarkResolver(rows, model)


def run_sa(inputs: dict, params: SAParams = SA_PARAMS, sizing: SizingParams = SIZING,
           cost_mult: float = 1.0) -> sa.RunResult:
    resolver = build_resolver(inputs)
    res = sa.run(inputs["events"], inputs["pre_rows"], resolver, params, sizing, cost_mult)
    trades = portfolio.apply_caps(res.trades, sizing) if len(res.trades) else res.trades
    return sa.RunResult(trades, res.suppressed, res.dropped)


def write_outputs(res: sa.RunResult, out_dir: str = OUT_DIR) -> None:
    os.makedirs(out_dir, exist_ok=True)
    res.trades.to_parquet(os.path.join(out_dir, "trades.parquet"), index=False)
    res.suppressed.to_parquet(os.path.join(out_dir, "suppressed.parquet"), index=False)
    res.dropped.to_parquet(os.path.join(out_dir, "dropped.parquet"), index=False)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=OUT_DIR)
    args = ap.parse_args()
    con = duckdb.connect()
    res = run_sa(load_inputs(con))
    write_outputs(res, args.out)
    t = res.trades
    print(f"trades {len(t)} rows; suppressed {len(res.suppressed)}; dropped {len(res.dropped)}")
    if len(t):
        print(t.groupby(["variant", "structure"]).agg(n=("net_pct", "size"), mean_net_pct=("net_pct", "mean")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
