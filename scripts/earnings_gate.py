#!/usr/bin/env python3
"""Earnings gate on the real TRADING-day horizon window.

Answers one question: does this name report inside the h-day window opening after T?

Exists because the gate kept being hand-written per lane and kept being wrong. On
2026-07-24 the live S2 lane passed 5 names whose ER landed inside its own h5 window
(AOS/BAX/KKR/PBF 07-30, CCJ 07-31) and S4 passed 4 inside h10 (DOX/NI 08-05, KGS 08-06,
WEN 08-07) -- both had filtered on a hardcoded date 2-3 days short of their own horizon.
The same defect sat in all five `retro_harness` lanes (fixed 2b32bad).

Window end comes from `_calendar.hz_end`, so this and the harness cannot drift apart.
Fails CLOSED: an unknown ticker or unreadable panel is reported BLOCKED, never PASS.

Usage:
  python3 scripts/earnings_gate.py --date 2026-07-24 --horizon 10 --tickers ALLE,MP,ORCL
  python3 scripts/earnings_gate.py --date 2026-07-24 --horizon 5  --tickers ED,KKR --json
  python3 scripts/earnings_gate.py --date 2026-07-24 --horizon 10 --tickers A,B --pass-only
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _calendar import hz_end, horizon_window  # noqa: E402

STOCKS = os.path.expanduser("~/Documents/Stocks")


def _screener(date: str) -> str | None:
    p = f"{STOCKS}/Stock Screener/stock-screener-{date}.parquet"
    return p if os.path.exists(p) else None


def check(tickers: list[str], date: str, horizon: int) -> dict:
    """{ticker: {verdict, next_earnings_date, window_end, reason}}; fail-closed."""
    first, end = horizon_window(date, horizon)
    out: dict[str, dict] = {}
    path = _screener(date)
    if path is None:
        for t in tickers:
            out[t] = {"verdict": "BLOCKED", "next_earnings_date": None, "window_end": end,
                      "reason": f"no screener panel for {date} -- fail closed"}
        return out

    import duckdb
    names = ",".join(f"'{t.upper()}'" for t in tickers)
    rows = duckdb.connect().execute(
        f"""SELECT ticker, any_value(next_earnings_date) FROM read_parquet('{path}')
            WHERE ticker IN ({names}) GROUP BY ticker""").fetchall()
    found = {r[0]: r[1] for r in rows}
    for t in (x.upper() for x in tickers):
        if t not in found:
            out[t] = {"verdict": "BLOCKED", "next_earnings_date": None, "window_end": end,
                      "reason": "ticker absent from screener panel -- fail closed"}
            continue
        ned = found[t]
        if ned is None:
            out[t] = {"verdict": "PASS", "next_earnings_date": None, "window_end": end,
                      "reason": "no scheduled earnings"}
        elif ned.isoformat() <= end:
            out[t] = {"verdict": "BLOCKED", "next_earnings_date": ned.isoformat(), "window_end": end,
                      "reason": f"reports {ned.isoformat()}, inside h{horizon} ({first}..{end})"}
        else:
            out[t] = {"verdict": "PASS", "next_earnings_date": ned.isoformat(), "window_end": end,
                      "reason": f"reports {ned.isoformat()}, clear of h{horizon} (ends {end})"}
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tickers", required=True, help="comma-separated")
    ap.add_argument("--date", required=True, help="trade date YYYY-MM-DD")
    ap.add_argument("--horizon", type=int, required=True, choices=[1, 3, 5, 10, 21, 42, 63])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--pass-only", action="store_true", help="print only surviving tickers, one per line")
    a = ap.parse_args()

    res = check([t.strip() for t in a.tickers.split(",") if t.strip()], a.date, a.horizon)
    if a.pass_only:
        for t, v in res.items():
            if v["verdict"] == "PASS":
                print(t)
        return 0
    if a.json:
        print(json.dumps(res, indent=2))
        return 0

    first, end = horizon_window(a.date, a.horizon)
    print(f"h{a.horizon} window from {a.date}: {first} .. {end}  (trading days)")
    for t, v in res.items():
        mark = "PASS   " if v["verdict"] == "PASS" else "BLOCKED"
        print(f"  {mark} {t:8s} {v['reason']}")
    blocked = sum(1 for v in res.values() if v["verdict"] != "PASS")
    print(f"\n{len(res) - blocked} pass, {blocked} blocked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
