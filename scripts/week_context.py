#!/usr/bin/env python3
"""The /weekly-review diary substrate in one call: candles, sector spread, notable flow.

Replaces the four ad-hoc snippets the weekly review kept re-writing inline -- weekly candle
anatomy, sector-ETF week returns, the week's largest dark-pool prints, and per-series staleness.

Staleness is the reason this is a script and not a one-liner. In 2026-W30 the XLC series was a
session stale (last bar 07-23), so its "week return" silently spanned a different window than
every other sector and would have been quoted as -6.45% alongside figures measured 07-17->07-24.
It was caught by eye. Every series here carries its own `asof` and is flagged STALE when it
does not reach the requested week end, and partial weekly bars are flagged via n_days < 5.

Diary only -- 0 signal. Raw flow measured as beta in research/20 and 70 and is not scored.

Usage:
  python3 scripts/week_context.py --week-end 2026-07-24
  python3 scripts/week_context.py --week-end 2026-07-24 --weeks 6
  python3 scripts/week_context.py --week-end 2026-07-24 --json
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, "..", "data"))
PX = os.path.join(DATA, "prices.parquet")
WK = os.path.join(DATA, "weekly_features.parquet")
STOCKS = os.path.expanduser("~/Documents/Stocks")

INDICES = ["SPY", "QQQ", "IWM"]
SECTORS = ["XLK", "XLE", "XLF", "XLV", "XLY", "XLP", "XLI", "XLU", "XLB", "XLRE", "XLC", "SMH"]


def _con():
    import duckdb
    return duckdb.connect()


def candles(week_end: str, tickers: list[str], weeks: int) -> dict:
    con = _con()
    out: dict[str, list[dict]] = {}
    for t in tickers:
        rows = con.execute(f"""
            SELECT wk_start, w_open, w_high, w_low, w_close, w_ret, close_pos, body_frac,
                   n_days, inside_week, outside_week, higher_high, lower_low,
                   hammer_or_hanging, star_or_inverted, follow_through
            FROM read_parquet('{WK}')
            WHERE ticker='{t}' AND wk_start <= DATE '{week_end}'
            ORDER BY wk_start DESC LIMIT {weeks}""").fetchall()
        cols = ["wk_start", "w_open", "w_high", "w_low", "w_close", "w_ret", "close_pos",
                "body_frac", "n_days", "inside_week", "outside_week", "higher_high",
                "lower_low", "hammer_or_hanging", "star_or_inverted", "follow_through"]
        recs = []
        for r in reversed(rows):
            d = dict(zip(cols, r))
            d["wk_start"] = str(d["wk_start"])[:10]
            tags = [n.replace("_week", "").replace("_or_", "/") for n in
                    ("outside_week", "inside_week", "higher_high", "lower_low",
                     "hammer_or_hanging", "star_or_inverted") if d.get(n)]
            d["tags"] = tags
            # A weekly bar built from fewer than 5 sessions is partial -- either a holiday
            # week or, more often, a week still in progress at the panel edge.
            d["partial"] = (d.get("n_days") or 0) < 5
            recs.append(d)
        out[t] = recs
    return out


def sector_week(week_end: str, tickers: list[str], sessions: int = 5) -> dict:
    """N-session return per ETF, each with its own asof + STALE flag."""
    con = _con()
    out: dict[str, dict] = {}
    for t in tickers:
        rows = con.execute(f"""
            SELECT date, close FROM read_parquet('{PX}')
            WHERE ticker='{t}' AND date <= DATE '{week_end}'
            ORDER BY date DESC LIMIT {sessions + 1}""").fetchall()
        if len(rows) < sessions + 1:
            out[t] = {"ret": None, "asof": None, "stale": True,
                      "reason": "insufficient history"}
            continue
        asof = rows[0][0].isoformat()
        out[t] = {
            "ret": round(rows[0][1] / rows[sessions][1] - 1, 5),
            "asof": asof,
            "from": rows[sessions][0].isoformat(),
            "stale": asof != week_end,
        }
    return out


def notable_flow(week_start: str, week_end: str, top: int) -> list[dict]:
    files = sorted(glob.glob(f"{STOCKS}/Dark pool/*.parquet"))
    if not files:
        return []
    con = _con()
    rows = con.execute(f"""
        SELECT ticker, SUM(premium)/1e6 AS dp_mm, COUNT(*) AS n
        FROM read_parquet({files!r})
        WHERE CAST(executed_at AS DATE) BETWEEN DATE '{week_start}' AND DATE '{week_end}'
        GROUP BY ticker ORDER BY dp_mm DESC LIMIT {top}""").fetchall()
    return [{"ticker": r[0], "dp_musd": round(r[1], 1), "prints": int(r[2])} for r in rows]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--week-end", required=True, help="last trading day of the week, YYYY-MM-DD")
    ap.add_argument("--week-start", help="defaults to week-end minus 4 sessions")
    ap.add_argument("--weeks", type=int, default=6, help="weekly candles to show (default 6)")
    ap.add_argument("--tickers", help="extra tickers for the candle table, comma-separated")
    ap.add_argument("--top", type=int, default=15, help="dark-pool rows (default 15)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    idx = INDICES + [t.strip().upper() for t in (a.tickers or "").split(",") if t.strip()]
    con = _con()
    if a.week_start:
        wk_start = a.week_start
    else:
        r = con.execute(f"""SELECT date FROM read_parquet('{PX}') WHERE ticker='SPY'
                            AND date <= DATE '{a.week_end}' ORDER BY date DESC LIMIT 5""").fetchall()
        wk_start = r[-1][0].isoformat() if len(r) == 5 else a.week_end

    ctx = {"week_start": wk_start, "week_end": a.week_end,
           "candles": candles(a.week_end, idx, a.weeks),
           "sectors": sector_week(a.week_end, SECTORS),
           "notable_flow": notable_flow(wk_start, a.week_end, a.top)}

    if a.json:
        print(json.dumps(ctx, indent=2, default=str))
        return 0

    print(f"week {wk_start} .. {a.week_end}\n")
    for t, recs in ctx["candles"].items():
        print(f"=== {t}")
        for d in recs:
            flags = ",".join(d["tags"])
            part = "  [PARTIAL n_days=%d]" % d["n_days"] if d["partial"] else ""
            print(f"  {d['wk_start']} O{d['w_open']:9.2f} H{d['w_high']:9.2f} L{d['w_low']:9.2f} "
                  f"C{d['w_close']:9.2f} ret{d['w_ret'] * 100:+6.2f}% cpos{d['close_pos']:.2f} "
                  f"body{d['body_frac']:.2f} ft{str(d['follow_through'])[:1]} {flags}{part}")
        print()

    print("=== sector 5-session returns")
    ranked = sorted(ctx["sectors"].items(),
                    key=lambda kv: (kv[1]["ret"] is None, -(kv[1]["ret"] or 0)))
    stale_any = False
    for t, v in ranked:
        if v["ret"] is None:
            print(f"  {t:6s}     n/a   {v.get('reason', '')}")
            continue
        mark = ""
        if v["stale"]:
            stale_any = True
            mark = f"   <-- STALE, last bar {v['asof']} (window {v['from']}..{v['asof']})"
        print(f"  {t:6s} {v['ret'] * 100:+7.2f}%{mark}")
    if stale_any:
        print("\n  ! A stale series spans a DIFFERENT window than the others. Do not quote it")
        print("    alongside them as if it were the same week.")

    print("\n=== dark-pool premium this week (diary only, 0 signal)")
    for r in ctx["notable_flow"]:
        print(f"  {r['ticker']:6s} ${r['dp_musd']:>9,.1f}M  {r['prints']:>7,} prints")
    return 0


if __name__ == "__main__":
    sys.exit(main())
