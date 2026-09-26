"""Run S-C on the panel (DESIGN/90 §5, R3 of §10): one entry per ISO week, F1..F10 per variant, SS and
IB marked at the late window, the §4 caps, settlement at expiry.

    python3 -m engine.backtest_sc [--out data/backtest]

Outputs under --out: sc_trades.parquet (every selected structure, `cap_pass` the portfolio view,
graded where the expiry close is known), sc_suppressed.parquet (first failing filter per name and
week; F10 / C2 cuts per variant), sc_dropped.parquet (unmarkable or degenerate structures),
sc_inputs.json (the spans the run used). The S-B book-budget cap reads `sb_marked.parquet` from the
same directory when it exists (positions open from entry to expiry), else it never binds.
"""
from __future__ import annotations

import argparse
import json
import os
import time
from datetime import date
from typing import Callable

import duckdb
import pandas as pd

from engine import calendar as cal
from engine import config
from engine import marking as M
from engine.strategies import sa_data, sb_data, sc
from engine.strategies import sb_proxy as P
from engine.strategies import sc_data as D

OUT_DIR = os.path.join(config.DATA, "backtest")
SB_MARKED_FILE = "sb_marked.parquet"


def _write_atomic(df: pd.DataFrame, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    df.to_parquet(tmp, index=False)
    os.replace(tmp, path)


def wing_resolver(con, entry: date, universe: pd.DataFrame, contracts: pd.DataFrame) -> Callable[[list[str]], M.MarkResolver]:
    """Tiers 1-2 from the entry session's prints; tier 3 from the screener's close and iv30d, scaled
    by the contract's last iv_vwap within MODEL_IV_LOOKBACK sessions, with the name's 20-session
    median spread floored at 5% -- S-A's model inputs (`sa_data.build_model_inputs`)."""
    def factory(tickers: list[str]) -> M.MarkResolver:
        sel = contracts[contracts["underlying_symbol"].isin(tickers)]
        rows = {(r["option_chain_id"], entry): r for r in sel.to_dict("records")}
        hist_dates = sa_data.history_dates([entry])
        hist = D.load_rows_for_underlyings(con, tickers, hist_dates)
        uni = universe.drop_duplicates("ticker").set_index("ticker")
        prices = {(t, entry): (float(uni.at[t, "close"]), float(uni.at[t, "close"])) for t in tickers}
        iv = {**sa_data.load_iv30d(con, tickers, hist_dates), **{(t, entry): uni.at[t, "iv30d"] for t in tickers}}
        spreads = sa_data.load_spread_history(con, pd.DataFrame({"ticker": tickers, "pre": [entry] * len(tickers)}))
        return M.MarkResolver(rows, sa_data.build_model_inputs(prices, iv, spreads, hist, {}))
    return factory


def sb_open_fn(out_dir: str) -> tuple[Callable[[date], bool], str]:
    path = os.path.join(out_dir, SB_MARKED_FILE)
    if not os.path.exists(path):
        return (lambda d: False), "absent (budget cap never binds)"
    sb = pd.read_parquet(path, columns=["entry", "expiry"])
    spans = [(pd.Timestamp(e).date(), pd.Timestamp(x).date()) for e, x in zip(sb["entry"], sb["expiry"])]
    return (lambda d: any(e <= d < x for e, x in spans)), f"{path} ({len(spans)} positions)"


def load_weeks(con) -> tuple[list[sc.WeekInput], list[date]]:
    panel = D.panel_sessions()
    if not panel:
        return [], []
    sessions = cal.trading_days(panel[0], panel[-1])
    entries = [d for d in P.entry_sessions(sessions, sessions[0], sessions[-1]) if d in set(panel)]
    weeks = []
    for d in entries:
        universe = D.load_entry_universe(con, d)
        if universe.empty:
            continue
        contracts = D.load_contract_rows(con, universe["ticker"], d)
        weeks.append(sc.WeekInput(d, universe, contracts, wing_resolver(con, d, universe, contracts)))
    return weeks, entries


def _summary(trades: pd.DataFrame) -> str:
    if trades.empty:
        return "no positions"
    g = trades[trades["graded"]].groupby(["variant", "structure"]).agg(
        n=("ror", "size"), weeks=("entry", "nunique"), mean_ror=("ror", "mean"), net_usd=("net_usd", "sum"))
    return g.to_string()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=OUT_DIR)
    a = ap.parse_args()
    t0 = time.time()
    con = duckdb.connect()
    weeks, entries = load_weeks(con)
    tickers = sorted({t for w in weeks for t in w.universe["ticker"]})
    through = D.prices_through(con)
    closes = sb_data.load_closes(con, tickers, entries[0] if entries else None, None)
    sb_open, sb_note = sb_open_fn(a.out)
    res = sc.run(weeks, closes, D.PrintCloses(con), prices_through=through, sb_open_on=sb_open)
    for name, df in (("sc_trades", res.trades), ("sc_suppressed", res.suppressed), ("sc_dropped", res.dropped)):
        _write_atomic(df, os.path.join(a.out, f"{name}.parquet"))
    spans = {"entries": [str(d) for d in entries], "n_weeks": len(weeks), "prices_through": str(through),
             "sb_open": sb_note, "params": config.SC_PARAMS.__dict__ | {"c2_excluded_sectors": list(config.SC_PARAMS.c2_excluded_sectors)}}
    with open(os.path.join(a.out, "sc_inputs.json"), "w") as fh:
        json.dump(spans, fh, indent=1, default=str)
    print(_summary(res.trades))
    print(f"{len(res.trades)} structures, {int(res.trades['graded'].sum()) if len(res.trades) else 0} graded, "
          f"{len(res.dropped)} dropped, {len(weeks)} weeks in {time.time() - t0:.1f}s -> {a.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
