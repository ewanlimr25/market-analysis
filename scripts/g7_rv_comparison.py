#!/usr/bin/env python3
"""G7 task 2: the RV-measure comparison table `DESIGN/90-sc-spec.md` would consume if S-C's
realized-vol definition moved from close-to-close (`RESEARCH/40 E2`'s RV21) to the intraday
measures in `engine/mart/intraday_rv.py`.

For the S-C-style universe (marketcap $1B-$20B, `iv30d` 30-80%, Common Stock/ADR, from the
screener -- `DESIGN/90` F1/F3/F6, without F2/F4/F5/F7-F10 which are strategy selection, not a
vol-measurement question) and every trailing 20-PANEL-SESSION window ending on day T where the
name's `intraday_rv.quality` flag is True on all 20 days (mirrors `RESEARCH/40 E2`'s "requiring
exactly 21 sessions", one shorter to match S-C's own DTE-linked window rather than E2's independent
choice):

  rv5_20d      = sqrt(sum(rv5 over the 20 days)        * 252 / 20)
  parkinson_20d= sqrt(sum(parkinson over the 20 days)  * 252 / 20)
  c2c_20d      = stdev(close_to_close_ret over the 20 days, ddof=1) * sqrt(252)   (E2's own method,
                 recomputed here from the SAME 20 sessions and the SAME prices.parquet source so
                 all three measures are apples-to-apples on the identical window)

reports: Pearson correlation between every pair, the mean ratio (RV5/close-to-close,
Parkinson/close-to-close), and the implied-minus-realized premium (screener `iv30d` on T minus
each measure): mean and share positive.

Usage: `python3 scripts/g7_rv_comparison.py [--json out.json]`
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys

import duckdb
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from engine import config  # noqa: E402
from engine.mart import store  # noqa: E402

WINDOW = 20
ANNUALIZATION = 252
MCAP_MIN, MCAP_MAX = 1e9, 20e9    # DESIGN/90 F3
IV_MIN, IV_MAX = 0.30, 0.80       # DESIGN/90 F6


def load_intraday_rv(con: duckdb.DuckDBPyConnection) -> pd.DataFrame:
    cols = "underlying_symbol AS ticker, date, quality, rv5, parkinson, close_to_close_ret"
    df = store.read_table(con, "intraday_rv", where="quality", columns=cols)
    df["date"] = pd.to_datetime(df["date"]).dt.date
    return df.sort_values(["ticker", "date"]).reset_index(drop=True)


def load_screener_slice(con: duckdb.DuckDBPyConnection) -> pd.DataFrame:
    """One row per (ticker, date): issue_type, marketcap, iv30d -- every screener export."""
    types = ", ".join(f"'{t}'" for t in config.ISSUE_TYPES)
    g = os.path.join(config.STOCKS, config.SCREENER_GLOB)
    df = con.execute(f"""
        SELECT date, ticker, any_value(issue_type) issue_type, any_value(marketcap) marketcap,
               any_value(iv30d) iv30d
        FROM read_parquet('{g}') WHERE issue_type IN ({types}) GROUP BY date, ticker""").df()
    df["date"] = pd.to_datetime(df["date"]).dt.date
    return df


def load_earnings_dates(con: duckdb.DuckDBPyConnection) -> pd.DataFrame:
    """(ticker, E) from `earnings_events` -- the real historical print dates, used to detect
    whether a TRAILING window actually contained a print (the screener's own
    `next_earnings_date` is forward-looking from T and cannot tell us that retroactively)."""
    df = store.read_table(con, "earnings_events", columns="ticker, E")
    df["E"] = pd.to_datetime(df["E"]).dt.date
    return df


def rolling_windows(rv: pd.DataFrame) -> pd.DataFrame:
    """Every (ticker, T) with WINDOW consecutive quality=True panel sessions ending on T.

    'Consecutive' means consecutive rows in this ticker's own quality-row sequence AND spanning
    exactly WINDOW calendar trading days with no drop-out (checked via the row count over the
    date span, since `rv` already contains only quality rows -- a gap shows up as a shorter
    window for the same span, which the count check below rejects, matching E2's "requiring
    exactly N sessions" rule).
    """
    from engine import calendar as cal

    out = []
    for tk, g in rv.groupby("ticker", sort=False):
        g = g.sort_values("date").reset_index(drop=True)
        if len(g) < WINDOW:
            continue
        dates = g["date"].tolist()
        rv5 = g["rv5"].to_numpy()
        pk = g["parkinson"].to_numpy()
        c2c = g["close_to_close_ret"].to_numpy()
        for i in range(WINDOW - 1, len(g)):
            lo, hi = dates[i - WINDOW + 1], dates[i]
            span_sessions = len(cal.trading_days(lo, hi))
            if span_sessions != WINDOW:
                continue  # a non-quality or missing day inside the span -> not a clean window
            c2c_win = c2c[i - WINDOW + 1: i + 1]
            if np.isnan(c2c_win).any():
                continue
            out.append({
                "ticker": tk, "date": hi, "window_start": lo,
                "rv5_20d": math.sqrt(rv5[i - WINDOW + 1: i + 1].sum() * ANNUALIZATION / WINDOW),
                "parkinson_20d": math.sqrt(pk[i - WINDOW + 1: i + 1].sum() * ANNUALIZATION / WINDOW),
                "c2c_20d": float(np.std(c2c_win, ddof=1) * math.sqrt(ANNUALIZATION)),
            })
    return pd.DataFrame(out)


def apply_sc_universe(windows: pd.DataFrame, screener: pd.DataFrame,
                      earnings: pd.DataFrame | None = None,
                      earnings_free_only: bool = False) -> pd.DataFrame:
    """DESIGN/90 F1 (via `load_screener_slice`'s issue_type filter), F3, F6 on the window's own
    end date T. `earnings_free_only` reproduces F5 / `RESEARCH/40 E2`'s exclusion, using the real
    historical print dates from `earnings_events` (`earnings`): a window with a print anywhere in
    [window_start, T] is a scheduled-print window, a different and much higher-vol population."""
    merged = windows.merge(screener, on=["ticker", "date"], how="inner")
    out = merged[(merged.marketcap >= MCAP_MIN) & (merged.marketcap <= MCAP_MAX)
                & (merged.iv30d >= IV_MIN) & (merged.iv30d <= IV_MAX)]
    if earnings_free_only:
        assert earnings is not None
        has_print = out.merge(earnings, on="ticker", how="left")
        in_window = (has_print["E"] >= has_print["window_start"]) & (has_print["E"] <= has_print["date"])
        tickers_with_print = set(zip(has_print.loc[in_window, "ticker"], has_print.loc[in_window, "date"]))
        keep = [(t, d) not in tickers_with_print for t, d in zip(out.ticker, out.date)]
        out = out[keep]
    return out.reset_index(drop=True)


def summarize(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"n": 0}
    corr = df[["rv5_20d", "c2c_20d", "parkinson_20d"]].corr(method="pearson")
    prem_rv5 = df.iv30d - df.rv5_20d
    prem_c2c = df.iv30d - df.c2c_20d
    prem_pk = df.iv30d - df.parkinson_20d
    return {
        "n": int(len(df)), "n_tickers": int(df.ticker.nunique()), "n_dates": int(df.date.nunique()),
        "corr_rv5_c2c": float(corr.loc["rv5_20d", "c2c_20d"]),
        "corr_rv5_parkinson": float(corr.loc["rv5_20d", "parkinson_20d"]),
        "corr_c2c_parkinson": float(corr.loc["c2c_20d", "parkinson_20d"]),
        "mean_ratio_rv5_over_c2c": float((df.rv5_20d / df.c2c_20d).mean()),
        "mean_ratio_parkinson_over_c2c": float((df.parkinson_20d / df.c2c_20d).mean()),
        "premium_rv5_mean": float(prem_rv5.mean()), "premium_rv5_share_positive": float((prem_rv5 > 0).mean()),
        "premium_c2c_mean": float(prem_c2c.mean()), "premium_c2c_share_positive": float((prem_c2c > 0).mean()),
        "premium_parkinson_mean": float(prem_pk.mean()),
        "premium_parkinson_share_positive": float((prem_pk > 0).mean()),
        "median_rv5_20d": float(df.rv5_20d.median()), "median_c2c_20d": float(df.c2c_20d.median()),
        "median_parkinson_20d": float(df.parkinson_20d.median()),
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", default=None)
    args = ap.parse_args(argv)

    con = duckdb.connect()
    rv = load_intraday_rv(con)
    windows = rolling_windows(rv)
    screener = load_screener_slice(con)
    earnings = load_earnings_dates(con)

    all_windows = apply_sc_universe(windows, screener)
    ex_earnings = apply_sc_universe(windows, screener, earnings, earnings_free_only=True)
    result = {"all_windows": summarize(all_windows), "earnings_free": summarize(ex_earnings)}

    print(json.dumps(result, indent=2))
    if args.json:
        with open(args.json, "w") as fh:
            json.dump(result, fh, indent=2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
