"""S-C R1 descriptive table: E2's F3 / F6 justification under RV5, close-to-close beside
(DESIGN/90 §0 note). Writes data/backtest/sc_rv5_f3_f6.md.

    python3 scripts/sc_rv5_table.py [--out data/backtest/sc_rv5_f3_f6.md]
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

import argparse

import duckdb
import pandas as pd

from engine import config
from engine.mart import store
from engine.research import sc_rv5 as R
from engine.validation.harness import md
from engine.watch.universe import load_screener_panel

PCT = ("iv30d_med", "rv5_med", "c2c_med", "iv_gt_rv5", "iv_gt_c2c")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(config.DATA, "backtest", "sc_rv5_f3_f6.md"))
    a = ap.parse_args()
    con = duckdb.connect()
    rv = store.read_table(con, config.SC_RV_TABLE, where="quality",
                          columns="underlying_symbol AS ticker, date, rv5, close_to_close_ret")
    rv["date"] = pd.to_datetime(rv["date"]).dt.date
    sessions = store.available_dates(config.SC_RV_TABLE)
    windows = R.forward_windows(rv)
    screener = load_screener_panel(sorted(set(windows["T"])))
    earnings = store.read_table(con, "earnings_events", columns="ticker, E")
    earnings["E"] = pd.to_datetime(earnings["E"]).dt.date
    df = R.assemble(windows, screener, earnings, sessions)
    tab = R.strata_table(df)
    text = "\n".join([
        "# S-C R1 descriptive: E2's F3 / F6 under RV5 (generated)", "",
        f"Forward {R.WINDOW}-session windows on `intraday_rv` quality rows ({len(windows):,} windows, "
        f"{df['ticker'].nunique():,} names, {df['T'].nunique()} entry dates, {df['month'].nunique()} months); "
        "VRP = iv30d − realized, vol points; `t_month` clusters on the month of T (DESIGN/90 §0 note, 2026-09-07). "
        "Earnings-free = no `earnings_events` print inside the window. Descriptive only: F3 and F6 stand as written.", "",
        md(tab, R.TABLE_COLS, pct_cols=PCT), "",
    ])
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with open(a.out, "w") as fh:
        fh.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
