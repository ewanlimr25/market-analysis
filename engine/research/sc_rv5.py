"""S-C R1 descriptive table (DESIGN/90 §0 note, 2026-09-07): E2's F3 (market-cap band) and F6
(iv30d band) justifications re-run with realized vol = RV5 from `data/mart/intraday_rv`, the
close-to-close measure beside it. Forward windows, as E2: for every (ticker, T) the next `WINDOW`
panel sessions must all be quality rows; VRP = iv30d − RV (vol points, annualised). Earnings-free
excludes windows with a real `earnings_events` print inside [T+1, T+WINDOW] (the historical
prints, as G7 did, not the screener's forward date). The independent unit is the month of T.
Descriptive: nothing here feeds a filter value; F3 and F6 stand as written in the spec.
"""
from __future__ import annotations

import math
from datetime import date

import numpy as np
import pandas as pd

from engine.config import SC_PARAMS, ISSUE_TYPES
from engine.validation.stats import cluster_t

WINDOW = 21                       # E2's 21-session measurement window
ANNUALIZATION = 252
MCAP_BANDS = (("< $1B", 0.0, 1e9), ("$1B to $20B (F3)", 1e9, 20e9), ("> $20B", 20e9, math.inf))
IV_BANDS = (("< 30%", 0.0, 0.30), ("30% to 80% (F6)", 0.30, 0.80), ("> 80%", 0.80, math.inf))
TABLE_COLS = ["stratum", "n", "months", "iv30d_med", "rv5_med", "c2c_med", "vrp_rv5_mean", "vrp_rv5_med", "iv_gt_rv5",
              "t_month_rv5", "vrp_c2c_mean", "vrp_c2c_med", "iv_gt_c2c", "t_month_c2c"]


def forward_windows(rv: pd.DataFrame, window: int = WINDOW) -> pd.DataFrame:
    """`rv`: quality rows only, columns ticker, date, rv5, close_to_close_ret. One row per (ticker, T)
    whose next `window` quality rows are consecutive panel sessions (the ticker's own row sequence
    spans exactly `window` distinct sessions after T with no gap in the panel's session list)."""
    if rv is None or rv.empty:
        return pd.DataFrame(columns=["ticker", "T", "rv5_fwd", "c2c_fwd"])
    sessions = sorted(set(rv["date"]))
    idx = {d: i for i, d in enumerate(sessions)}
    out = []
    for ticker, g in rv.sort_values("date").groupby("ticker", sort=False):
        dates = g["date"].to_numpy()
        rv5 = g["rv5"].to_numpy(dtype=float)
        c2c = g["close_to_close_ret"].to_numpy(dtype=float)
        pos = np.array([idx[d] for d in dates])
        for i in range(len(g) - window):
            if pos[i + window] - pos[i] != window:          # a non-quality or missing session inside
                continue
            seg_rv5, seg_c2c = rv5[i + 1: i + window + 1], c2c[i + 1: i + window + 1]
            if np.isnan(seg_rv5).any() or np.isnan(seg_c2c).any():
                continue
            out.append({"ticker": ticker, "T": dates[i],
                        "rv5_fwd": math.sqrt(seg_rv5.sum() * ANNUALIZATION / window),
                        "c2c_fwd": float(np.std(seg_c2c, ddof=1) * math.sqrt(ANNUALIZATION))})
    return pd.DataFrame(out, columns=["ticker", "T", "rv5_fwd", "c2c_fwd"])


def assemble(windows: pd.DataFrame, screener: pd.DataFrame, earnings: pd.DataFrame | None,
             sessions: list[date], window: int = WINDOW) -> pd.DataFrame:
    """Join the screener row of (ticker, T) -- iv30d, marketcap, sector, issue_type -- and flag
    windows with an earnings print inside (T, T + window sessions]. Keeps Common/ADR only."""
    if windows.empty:
        return pd.DataFrame(columns=[*windows.columns, "iv30d", "marketcap", "sector", "earnings_in_window", "vrp_rv5", "vrp_c2c", "month"])
    scr = screener.rename(columns={"date": "T"})[["ticker", "T", "iv30d", "marketcap", "sector", "issue_type"]]
    df = windows.merge(scr, on=["ticker", "T"], how="inner")
    df = df[df["issue_type"].isin(ISSUE_TYPES)].drop(columns=["issue_type"])
    idx = {d: i for i, d in enumerate(sessions)}
    end = {d: sessions[min(idx[d] + window, len(sessions) - 1)] for d in idx}
    flag = pd.Series(False, index=df.index)
    if earnings is not None and not earnings.empty:
        e = earnings[["ticker", "E"]].drop_duplicates()
        by_ticker = {t: sorted(g["E"]) for t, g in e.groupby("ticker")}
        flag = pd.Series([any(T < x <= end.get(T, T) for x in by_ticker.get(t, ())) for t, T in zip(df["ticker"], df["T"])],
                         index=df.index)
    df["earnings_in_window"] = flag
    df["vrp_rv5"] = (df["iv30d"] - df["rv5_fwd"]) * 100.0
    df["vrp_c2c"] = (df["iv30d"] - df["c2c_fwd"]) * 100.0
    df["month"] = [f"{d.year}-{d.month:02d}" for d in df["T"]]
    return df.dropna(subset=["iv30d", "marketcap"]).reset_index(drop=True)


def _stratum(df: pd.DataFrame, name: str) -> dict:
    t5, tc = cluster_t(df["vrp_rv5"], df["month"]), cluster_t(df["vrp_c2c"], df["month"])
    return {"stratum": name, "n": int(len(df)), "months": t5["G"],
            "iv30d_med": float(df["iv30d"].median()), "rv5_med": float(df["rv5_fwd"].median()), "c2c_med": float(df["c2c_fwd"].median()),
            "vrp_rv5_mean": t5["mean"], "vrp_rv5_med": float(df["vrp_rv5"].median()),
            "iv_gt_rv5": float((df["vrp_rv5"] > 0).mean()), "t_month_rv5": t5["t"],
            "vrp_c2c_mean": tc["mean"], "vrp_c2c_med": float(df["vrp_c2c"].median()),
            "iv_gt_c2c": float((df["vrp_c2c"] > 0).mean()), "t_month_c2c": tc["t"]}


def strata_table(df: pd.DataFrame, params=SC_PARAMS) -> pd.DataFrame:
    """Earnings-free rows: all, the F3 market-cap bands, the F6 iv30d bands, and the two bands jointly."""
    if df.empty:
        return pd.DataFrame(columns=TABLE_COLS)
    free = df[~df["earnings_in_window"]]
    rows = [_stratum(df, "all windows"), _stratum(free, "earnings-free")]
    for name, lo, hi in MCAP_BANDS:
        sub = free[(free["marketcap"] >= lo) & (free["marketcap"] < hi)]
        if len(sub):
            rows.append(_stratum(sub, f"earnings-free, mcap {name}"))
    for name, lo, hi in IV_BANDS:
        sub = free[(free["iv30d"] >= lo) & (free["iv30d"] < hi)]
        if len(sub):
            rows.append(_stratum(sub, f"earnings-free, iv30d {name}"))
    both = free[(free["marketcap"] >= params.mcap_min) & (free["marketcap"] <= params.mcap_max)
                & (free["iv30d"] >= params.iv30d_min) & (free["iv30d"] <= params.iv30d_max)]
    if len(both):
        rows.append(_stratum(both, "earnings-free, F3 and F6 (the S-C band)"))
    return pd.DataFrame(rows, columns=TABLE_COLS)
