#!/usr/bin/env python3
"""Fetch price + 20d dollar-ADV from the screener panel and apply the C12 liquidity floor.

`excess_winrate.py` already owns the floor ARITHMETIC, but its docstring says "the agent
populates `price` and `adv_usd`" -- and that hand-population is the step that fails. On
2026-07-24 PLNT's $-ADV was reported as ~$250M when it is ~$87M (1.63M sh x $53.48), a
2.9x error caught downstream by risk-sizer rather than at source. This closes the fetch.

Thresholds are IMPORTED from excess_winrate, never re-declared, so there is exactly one
definition of the floor in the repo.

Usage:
  python3 scripts/liquidity.py --tickers PLNT,ALLE,QS --date 2026-07-24
  python3 scripts/liquidity.py --tickers PLNT --date 2026-07-24 --json
  python3 scripts/liquidity.py --tickers A,B,C --date 2026-07-24 --pass-only
"""
from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from excess_winrate import MIN_ADV_USD, MIN_PRICE  # noqa: E402  -- single source of truth

STOCKS = os.path.expanduser("~/Documents/Stocks")


def fetch(tickers: list[str], date: str) -> dict:
    """{ticker: {price, adv_usd, avg30_volume, verdict, reason}}; fail-closed."""
    path = f"{STOCKS}/Stock Screener/stock-screener-{date}.parquet"
    out: dict[str, dict] = {}
    if not os.path.exists(path):
        for t in tickers:
            out[t.upper()] = {"price": None, "adv_usd": None, "avg30_volume": None,
                              "verdict": "FAIL", "reason": f"no screener panel for {date} -- fail closed"}
        return out

    import duckdb
    names = ",".join(f"'{t.upper()}'" for t in tickers)
    rows = duckdb.connect().execute(
        f"""SELECT ticker, any_value(close), any_value(avg30_volume), any_value(issue_type)
            FROM read_parquet('{path}') WHERE ticker IN ({names}) GROUP BY ticker""").fetchall()
    found = {r[0]: r[1:] for r in rows}
    for t in (x.upper() for x in tickers):
        if t not in found:
            out[t] = {"price": None, "adv_usd": None, "avg30_volume": None, "issue_type": None,
                      "verdict": "FAIL", "reason": "absent from screener panel -- fail closed"}
            continue
        close, vol, issue = found[t]
        price = float(close or 0)
        adv = price * float(vol or 0)
        reasons = []
        if price < MIN_PRICE:
            reasons.append(f"price ${price:.2f} < ${MIN_PRICE:.0f}")
        if adv < MIN_ADV_USD:
            reasons.append(f"$-ADV ${adv/1e6:.1f}M < ${MIN_ADV_USD/1e6:.0f}M")
        out[t] = {"price": round(price, 2), "adv_usd": round(adv), "avg30_volume": round(float(vol or 0)),
                  "issue_type": issue,
                  "verdict": "FAIL" if reasons else "PASS",
                  "reason": "; ".join(reasons) if reasons else "clears price and $-ADV floors"}
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tickers", required=True)
    ap.add_argument("--date", required=True)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--pass-only", action="store_true")
    a = ap.parse_args()

    res = fetch([t.strip() for t in a.tickers.split(",") if t.strip()], a.date)
    if a.pass_only:
        for t, v in res.items():
            if v["verdict"] == "PASS":
                print(t)
        return 0
    if a.json:
        print(json.dumps(res, indent=2))
        return 0

    print(f"floor: price >= ${MIN_PRICE:.0f} AND 20d $-ADV >= ${MIN_ADV_USD/1e6:.0f}M  (fail-closed)")
    for t, v in res.items():
        px = f"${v['price']:.2f}" if v["price"] is not None else "  n/a"
        adv = f"${v['adv_usd']/1e6:8.1f}M" if v["adv_usd"] is not None else "      n/a"
        print(f"  {v['verdict']:4s} {t:8s} {px:>9s}  ADV {adv}  {v['reason']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
