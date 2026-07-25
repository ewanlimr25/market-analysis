#!/usr/bin/env python3
"""Path-aware Yahoo chart-API reads: OHLC, trailing returns, 52w range, Wilder RSI.

CLAUDE.md mandates the chart API for outcomes (never the close-only `mcp__yahoo-finance__*`
tools), but the only chart code in the repo was `truthset/build_prices.py` -- bulk, 785
symbols, writes a parquet, unusable ad hoc. So every scan hand-rolled urllib again (four
separate times on 2026-07-24 alone), and RSI had no implementation anywhere despite being
half of a live invalidation.

Importable: `from chart import bars, rets, w52, rsi14`.

Usage:
  python3 scripts/chart.py --tickers SPY,ORCL,PLNT --ohlc 6
  python3 scripts/chart.py --ticker SPY  --rets 5,10
  python3 scripts/chart.py --ticker ORCL --52w --rsi 14
  python3 scripts/chart.py --tickers SPY,QQQ,^VIX --ohlc 3 --json
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import urllib.request

UA = {"User-Agent": "Mozilla/5.0"}


def bars(ticker: str, rng: str = "6mo") -> list[dict]:
    """Daily OHLCV, oldest first. Rows with a null close are dropped (holidays/halts)."""
    url = (f"https://query2.finance.yahoo.com/v8/finance/chart/{ticker}"
           f"?range={rng}&interval=1d")
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=25) as r:
        res = json.load(r)["chart"]["result"][0]
    ts, q = res["timestamp"], res["indicators"]["quote"][0]
    out = []
    for i, t in enumerate(ts):
        if q["close"][i] is None:
            continue
        out.append({"date": dt.datetime.fromtimestamp(t, dt.UTC).strftime("%Y-%m-%d"),
                    "open": q["open"][i], "high": q["high"][i], "low": q["low"][i],
                    "close": q["close"][i], "volume": q["volume"][i]})
    return out


def rets(ticker: str, horizons=(5, 10), rng: str = "6mo") -> dict:
    """Trailing simple returns over N TRADING days (matching the truth-set grid)."""
    b = bars(ticker, rng)
    c = [x["close"] for x in b]
    out = {"close": round(c[-1], 4), "date": b[-1]["date"]}
    for h in horizons:
        out[f"ret{h}"] = round(c[-1] / c[-1 - h] - 1, 5) if len(c) > h else None
        out[f"ret{h}_from"] = b[-1 - h]["date"] if len(c) > h else None
    return out


def w52(ticker: str) -> dict:
    """52-week high/low and position in range (0 = at the low, 1 = at the high)."""
    b = bars(ticker, "1y")
    hi = max(x["high"] for x in b)
    lo = min(x["low"] for x in b)
    last = b[-1]["close"]
    return {"close": round(last, 4), "w52_high": round(hi, 4), "w52_low": round(lo, 4),
            "w52_high_date": next(x["date"] for x in b if x["high"] == hi),
            "w52_low_date": next(x["date"] for x in b if x["low"] == lo),
            "pct_52w_range": round((last - lo) / (hi - lo), 4) if hi > lo else None,
            "off_high_pct": round(last / hi - 1, 4) if hi else None}


def rsi14(ticker: str, n: int = 14, rng: str = "6mo") -> float | None:
    """Wilder-smoothed RSI (the standard definition, not a simple moving average)."""
    c = [x["close"] for x in bars(ticker, rng)]
    if len(c) <= n:
        return None
    gains = [max(c[i] - c[i - 1], 0) for i in range(1, len(c))]
    losses = [max(c[i - 1] - c[i], 0) for i in range(1, len(c))]
    ag, al = sum(gains[:n]) / n, sum(losses[:n]) / n
    for i in range(n, len(gains)):
        ag = (ag * (n - 1) + gains[i]) / n
        al = (al * (n - 1) + losses[i]) / n
    if al == 0:
        return 100.0
    return round(100 - 100 / (1 + ag / al), 2)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ticker")
    ap.add_argument("--tickers")
    ap.add_argument("--ohlc", type=int, metavar="N", help="print the last N daily bars")
    ap.add_argument("--rets", help="comma-separated horizons, e.g. 5,10")
    ap.add_argument("--52w", dest="w52", action="store_true")
    ap.add_argument("--rsi", type=int, nargs="?", const=14, metavar="N")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    names = [t.strip() for t in (a.tickers or a.ticker or "").split(",") if t.strip()]
    if not names:
        ap.error("need --ticker or --tickers")
    if not (a.ohlc or a.rets or a.w52 or a.rsi):
        a.ohlc = 5

    result: dict[str, dict] = {}
    for t in names:
        r: dict = {}
        try:
            if a.ohlc:
                r["ohlc"] = bars(t)[-a.ohlc:]
            if a.rets:
                r["rets"] = rets(t, tuple(int(h) for h in a.rets.split(",")))
            if a.w52:
                r["w52"] = w52(t)
            if a.rsi:
                r[f"rsi{a.rsi}"] = rsi14(t, a.rsi)
        except Exception as e:              # fail soft per ticker, like build_prices
            r["error"] = f"{type(e).__name__}: {e}"
        result[t] = r

    if a.json:
        print(json.dumps(result, indent=2))
        return 0

    for t, r in result.items():
        print(f"\n=== {t}")
        if "error" in r:
            print(f"  ERROR {r['error']}")
            continue
        for row in r.get("ohlc", []):
            print(f"  {row['date']}  O{row['open']:>9.2f} H{row['high']:>9.2f} "
                  f"L{row['low']:>9.2f} C{row['close']:>9.2f}")
        if "rets" in r:
            v = r["rets"]
            parts = [f"close {v['close']} ({v['date']})"]
            for k in v:
                if k.startswith("ret") and not k.endswith("_from") and v[k] is not None:
                    parts.append(f"{k} {100*v[k]:+.3f}% (vs {v[k+'_from']})")
            print("  " + " | ".join(parts))
        if "w52" in r:
            v = r["w52"]
            print(f"  close {v['close']} | 52w {v['w52_low']} ({v['w52_low_date']}) .. "
                  f"{v['w52_high']} ({v['w52_high_date']}) | pct_range {100*v['pct_52w_range']:.1f}% "
                  f"| off_high {100*v['off_high_pct']:.1f}%")
        for k, val in r.items():
            if k.startswith("rsi"):
                print(f"  {k.upper()} (Wilder) = {val}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
