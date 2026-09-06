"""Run S-B (DESIGN/80 §5): the three-year proxy from CBOE and Yahoo closes, and the marked run on
the panel, plus the descriptive gate modes and sensitivities of §6.6.

    python3 -m engine.backtest_sb [--refresh] [--out data/backtest]

Outputs under --out: sb_proxy.parquet (base), sb_proxy_sens.parquet (every mode / sensitivity
with a `sensitivity` column), sb_marked.parquet, sb_marked_sens.parquet, sb_marked_skipped.parquet,
sb_inputs.json (the input spans the run used). `--refresh` refetches CBOE and the Yahoo bars into
data/mart/index_vol/; without it the mart files are used, else the artifacts frozen on 2026-09-05.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from dataclasses import replace

import duckdb
import pandas as pd

from engine import calendar as cal
from engine import config
from engine.config import INDEX_VOL_DIR, SB_PARAMS, SB_SIZING, SB_UNDERLYINGS, SCRIPTS
from engine.mart import index_vol as IV
from engine.strategies import sb, sb_data
from engine.strategies import sb_proxy as P

OUT_DIR = os.path.join(config.DATA, "backtest")
PROXY_PRICES_FILE = os.path.join(INDEX_VOL_DIR, "proxy_prices.parquet")
PROXY_RANGE = "3y"
PROXY_SENSITIVITIES = (("base", {}), ("gate_off", {"gate_mode": "off"}), ("g1_only", {"gate_mode": "g1"}),
                       ("g2_only", {"gate_mode": "g2"}), ("costs_x2", {"cost_mult": 2.0}),
                       ("wing_1.5", {"params": replace(SB_PARAMS, wing_sigma=1.5)}))
MARKED_SENSITIVITIES = (("base", {}), ("gate_off", {"gate_mode": "off"}),
                        ("band_0.15", {"params": replace(SB_PARAMS, strike_band_sigma=0.15)}),
                        ("wing_1.5", {"params": replace(SB_PARAMS, wing_sigma=1.5)}))


def _write_atomic(df: pd.DataFrame, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    df.to_parquet(tmp, index=False)
    os.replace(tmp, path)


def refresh_inputs() -> dict:
    """Network: CBOE series and the Yahoo 3y bars for SPY/QQQ into data/mart/index_vol/."""
    iv = IV.refresh()
    if SCRIPTS not in sys.path:
        sys.path.insert(0, SCRIPTS)
    from chart import bars  # noqa: E402
    frames = []
    for sym in SB_UNDERLYINGS:
        b = pd.DataFrame(bars(sym, PROXY_RANGE))[["date", "open", "high", "low", "close"]]
        frames.append(b.assign(date=pd.to_datetime(b["date"]).dt.date, ticker=sym))
    px = pd.concat(frames, ignore_index=True)
    _write_atomic(px, PROXY_PRICES_FILE)
    return {"index_vol_through": str(IV.latest_date(iv)), "prices_through": str(px["date"].max())}


def proxy_inputs() -> P.ProxyInputs:
    prices = PROXY_PRICES_FILE if os.path.exists(PROXY_PRICES_FILE) else config.PROXY_PRICES_FALLBACK
    return P.load_inputs(None, prices)


def run_proxy_all(inputs: P.ProxyInputs) -> tuple[pd.DataFrame, pd.DataFrame]:
    frames = []
    for name, kw in PROXY_SENSITIVITIES:
        df = P.run_proxy(inputs, **kw)
        frames.append(df.assign(sensitivity=name))
    sens = pd.concat([f for f in frames if len(f)], ignore_index=True) if any(len(f) for f in frames) else pd.DataFrame()
    base = sens[sens.sensitivity == "base"].drop(columns=["sensitivity"]).reset_index(drop=True) if len(sens) else pd.DataFrame()
    return base, sens


def marked_inputs(con) -> dict | None:
    panel = sb_data.panel_sessions()
    if not panel:
        return None
    sessions = cal.trading_days(panel[0], panel[-1])
    entries = P.entry_sessions(sessions, sessions[0], sessions[-1])
    entry_rows = {d: sb_data.load_entry_rows(con, SB_UNDERLYINGS, d) for d in entries}
    closes = sb_data.load_closes(con, SB_UNDERLYINGS, sessions[0], None)
    return {"entry_rows": entry_rows, "closes": closes, "sessions": sessions, "index_vol": IV.load_index_vol(),
            "panel": (panel[0], panel[-1])}


def run_marked_all(inputs: dict) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    frames, skipped_base = [], pd.DataFrame()
    for name, kw in MARKED_SENSITIVITIES:
        trades, skipped = sb.run_marked(inputs["entry_rows"], inputs["index_vol"], inputs["closes"], inputs["sessions"],
                                        kw.get("params", SB_PARAMS), SB_SIZING, kw.get("gate_mode", "both"))
        frames.append(trades.assign(sensitivity=name) if len(trades) else trades)
        if name == "base":
            skipped_base = skipped
    sens = pd.concat([f for f in frames if len(f)], ignore_index=True) if any(len(f) for f in frames) else pd.DataFrame()
    base = sens[sens.sensitivity == "base"].drop(columns=["sensitivity"]).reset_index(drop=True) if len(sens) else pd.DataFrame()
    return base, sens, skipped_base


def _summary(df: pd.DataFrame, label: str) -> str:
    if df.empty:
        return f"{label}: no positions"
    g = df[df.ror.notna()].groupby(["underlying", "structure"]).agg(n=("ror", "size"), mean_ror=("ror", "mean"), net_usd=("net_usd", "sum"))
    return f"{label}:\n{g.to_string()}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true", help="refetch CBOE + Yahoo inputs (network)")
    ap.add_argument("--out", default=OUT_DIR)
    a = ap.parse_args()
    t0 = time.time()
    spans = {}
    if a.refresh:
        spans["refreshed"] = refresh_inputs()
    inputs = proxy_inputs()
    spans["proxy"] = {"index_vol": [str(inputs.index_vol.date.min()), str(inputs.index_vol.date.max())],
                      "sessions": [str(inputs.sessions[0]), str(inputs.sessions[-1])], "n_sessions": len(inputs.sessions)}
    proxy, proxy_sens = run_proxy_all(inputs)
    _write_atomic(proxy, os.path.join(a.out, "sb_proxy.parquet"))
    _write_atomic(proxy_sens, os.path.join(a.out, "sb_proxy_sens.parquet"))
    print(_summary(proxy, f"proxy (base, {len(proxy)} positions, {time.time() - t0:.1f}s)"))
    con = duckdb.connect()
    m_in = marked_inputs(con)
    if m_in is None:
        print("marked: no daily_contract partitions on disk")
        marked, marked_sens, skipped = pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
    else:
        spans["marked"] = {"panel": [str(m_in["panel"][0]), str(m_in["panel"][1])], "n_entry_sessions": len(m_in["entry_rows"])}
        marked, marked_sens, skipped = run_marked_all(m_in)
        print(_summary(marked, f"marked (base, {len(marked)} positions, {int(marked.graded.sum()) if len(marked) else 0} graded)"))
    _write_atomic(marked, os.path.join(a.out, "sb_marked.parquet"))
    _write_atomic(marked_sens, os.path.join(a.out, "sb_marked_sens.parquet"))
    _write_atomic(skipped, os.path.join(a.out, "sb_marked_skipped.parquet"))
    with open(os.path.join(a.out, "sb_inputs.json"), "w") as fh:
        json.dump(spans, fh, indent=1)
    print(f"done in {time.time() - t0:.1f}s -> {a.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
