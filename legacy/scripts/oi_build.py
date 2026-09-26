#!/usr/bin/env python3
"""Trailing N-day open-interest build, split call vs put, from the raw UW OI panel.

The OI_FADE lane's whole input. Exists because it kept being hand-written per run, and
the two ways to get it wrong are both silent:

  * `oi_change` is a RATIO; the contract delta is `oi_diff_plain`. Using the former
    returns plausible-looking fractions (a first attempt on 2026-07-24 did exactly this).
  * `oi_net_5d` is NET call MINUS put (CLAUDE.md). A call-only read sign-flips prints --
    it nearly inverted an exit on 2026-07-15 -- so call_net and put_net are always
    reported per day, never just the net. A net that goes negative because puts opened
    is a wash, NOT the call unwind that invalidates a short.

Also emits, per ticker:
  persistence_ratio = max |daily net| / |sum of daily net|
      -> ~1.0 means one institutional block, not organic multi-day building. On
         2026-07-24 this flagged MWH (0.999), YMM (0.997) and ALLY (1.25, already
         unwinding) while ALLE came in at 0.455 (genuinely organic).
  oi_rel_build = net_Nd / avg_30_day_call_oi
      -> the lane ranks on THIS, never raw net: raw ranking just lists mega-caps by
         options-book size and degenerates into a QQQ-beta short.

Usage:
  python3 scripts/oi_build.py --tickers ALLE,PLNT --date 2026-07-24
  python3 scripts/oi_build.py --tickers PLNT --date 2026-07-24 --days 5 --json
  python3 scripts/oi_build.py --date 2026-07-24 --top 15    # rank the panel by oi_rel_build
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date as _date

STOCKS = os.path.expanduser("~/Documents/Stocks")
OI_DIR = f"{STOCKS}/OI changes"
SCR_DIR = f"{STOCKS}/Stock Screener"

# canonical option-symbol call/put parse -- same expression as truthset/build_features.py
CP = r"regexp_extract(option_symbol,'\d{6}([CP])',1)"


def _panel_dates(date: str, days: int) -> list[str]:
    """The `days` most recent OI panel dates on or before `date`."""
    have = sorted(
        f.rsplit("-", 3)[-3:] and f[len("chain-oi-changes-"):-len(".parquet")]
        for f in os.listdir(OI_DIR) if f.startswith("chain-oi-changes-") and f.endswith(".parquet"))
    upto = [d for d in have if d <= date]
    return upto[-days:]


def build(tickers: list[str] | None, date: str, days: int = 5) -> dict:
    import duckdb
    con = duckdb.connect()
    dates = _panel_dates(date, days)
    if not dates:
        return {}
    where_tk = ""
    if tickers:
        names = ",".join(f"'{t.upper()}'" for t in tickers)
        where_tk = f" AND underlying_symbol IN ({names})"

    daily: dict[str, dict[str, dict]] = {}
    for d in dates:
        f = f"{OI_DIR}/chain-oi-changes-{d}.parquet"
        if not os.path.exists(f):
            continue
        rows = con.execute(f"""
            SELECT underlying_symbol,
                   sum(CASE WHEN {CP}='C' THEN oi_diff_plain ELSE 0 END) AS call_net,
                   sum(CASE WHEN {CP}='P' THEN oi_diff_plain ELSE 0 END) AS put_net
            FROM read_parquet('{f}')
            WHERE underlying_symbol IS NOT NULL{where_tk}
            GROUP BY underlying_symbol""").fetchall()
        for tk, c, p in rows:
            daily.setdefault(tk, {})[d] = {"call_net": int(c or 0), "put_net": int(p or 0),
                                           "net": int((c or 0) - (p or 0))}

    # OI base + liquidity context from the screener for the same trade date
    base: dict[str, dict] = {}
    scr = f"{SCR_DIR}/stock-screener-{date}.parquet"
    if os.path.exists(scr):
        for tk, oi, cl, av in con.execute(
                f"""SELECT ticker, any_value(avg_30_day_call_oi), any_value(close),
                           any_value(avg30_volume) FROM read_parquet('{scr}') GROUP BY ticker""").fetchall():
            base[tk] = {"avg_30d_call_oi": float(oi or 0), "close": float(cl or 0),
                        "avg30_volume": float(av or 0)}

    out: dict[str, dict] = {}
    for tk, per_day in daily.items():
        series = [per_day.get(d) for d in dates]
        nets = [s["net"] for s in series if s]
        if not nets:
            continue
        call_sum = sum(s["call_net"] for s in series if s)
        put_sum = sum(s["put_net"] for s in series if s)
        net_sum = call_sum - put_sum
        b = base.get(tk, {})
        oi_base = b.get("avg_30d_call_oi", 0.0)
        out[tk] = {
            "daily": [{"date": d, **per_day[d]} for d in dates if d in per_day],
            "call_Nd": call_sum, "put_Nd": put_sum, "net_Nd": net_sum,
            "persistence_ratio": round(max(abs(n) for n in nets) / abs(net_sum), 3) if net_sum else None,
            "avg_30d_call_oi": oi_base,
            "oi_rel_build": round(net_sum / oi_base, 3) if oi_base else None,
            "close": b.get("close"), "adv_usd": round(b.get("close", 0) * b.get("avg30_volume", 0)),
            "last_call_net": series[-1]["call_net"] if series[-1] else None,
        }
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tickers", help="comma-separated; omit with --top to rank the panel")
    ap.add_argument("--date", required=True)
    ap.add_argument("--days", type=int, default=5)
    ap.add_argument("--top", type=int, help="rank by oi_rel_build and print the top N")
    ap.add_argument("--min-net", type=int, default=1000, help="absolute build floor (default 1000)")
    ap.add_argument("--min-oi-base", type=int, default=1000, help="avg_30d_call_oi floor (default 1000)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    tickers = [t.strip() for t in a.tickers.split(",")] if a.tickers else None
    res = build(tickers, a.date, a.days)

    if a.top:
        # the lane's floors, fail-closed: a near-zero OI base turns noise into a top rank
        res = {k: v for k, v in res.items()
               if v["oi_rel_build"] is not None
               and abs(v["net_Nd"]) >= a.min_net
               and v["avg_30d_call_oi"] >= a.min_oi_base}
        res = dict(sorted(res.items(), key=lambda kv: -kv[1]["oi_rel_build"])[:a.top])

    if a.json:
        print(json.dumps(res, indent=2))
        return 0

    if not res:
        print("no rows (check the date has an OI panel, and the floors)")
        return 0
    for tk, v in res.items():
        print(f"\n{tk}  net_{a.days}d={v['net_Nd']:+,} (call {v['call_Nd']:+,} / put {v['put_Nd']:+,})"
              f"  rel_build={v['oi_rel_build']}  persistence={v['persistence_ratio']}")
        if v["persistence_ratio"] is not None and v["persistence_ratio"] > 0.85:
            print("   ** persistence > 0.85 -- likely a single-day block, not organic building")
        for d in v["daily"]:
            print(f"     {d['date']}  call {d['call_net']:+7,}  put {d['put_net']:+6,}  net {d['net']:+7,}")
        if v["last_call_net"] is not None and v["last_call_net"] < 0:
            print("   ** last call_net NEGATIVE -- calls genuinely closing (OI_FADE invalidation)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
