#!/usr/bin/env python3
"""Reconcile the prior conviction file against today's closes -- marks, excess, and
whether each invalidation is still a REACHABLE stop.

Scan sub-agents do not carry open positions, so the orchestrator redoes this by hand every
run. The column that matters is the last one: distance to each invalidation leg, compared
against the open gain.

On 2026-07-24 ORCL was +12.58% gross on a short whose documented invalidation was
`RSI>45 AND close>$144.22` -- an AND-conjunction set at entry, whose price leg had drifted
25.4% away AND sat ABOVE the $131.54 entry. Held to that stop the trade would have given
back the entire gain and become a loss before any exit fired. The invalidation had gone
VESTIGIAL: dormant, so it looked satisfied, while protecting nothing. That check is
mechanical and should not depend on anyone noticing.

Usage:
  python3 scripts/held_book.py --prior analyses/scan/2026-07-23/conviction_2026-07-23.json
  python3 scripts/held_book.py --prior <file> --benchmark SPY --json
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chart import bars, rsi14  # noqa: E402

CLOSED = ("CLOSED", "DROPPED", "CUT_CONFIRMED", "COVER", "EXIT")
# A real invalidation level is always a THRESHOLD, so require a comparison operator
# immediately before it. Bare dollar figures in prose are usually something else --
# analyst price targets ("DB cut $61->$55"), or a distance ("price clause $18+ away") --
# and parsing those as legs produced false VESTIGIAL warnings on a sound position.
# The (?<!-) guard stops the ">" inside "->" from reading as an operator, and the
# mandatory "$" keeps a non-price threshold like "RSI>45" out of the price legs.
PRICE_RE = re.compile(r"(?<!-)[><≥≤]\s*\$\s*([0-9]+(?:\.[0-9]+)?)")
RSI_RE = re.compile(r"RSI\s*[>≥]\s*([0-9]+(?:\.[0-9]+)?)", re.I)


def _positions(doc: dict) -> list[dict]:
    rec = doc.get("held_position_reconciliation") or {}
    return [p for p in rec.get("positions", [])
            if not any(k in str(p.get("verdict", "")).upper() for k in CLOSED)
            and not any(k in str(p.get("status", "")).upper() for k in CLOSED)]


def _invalidation_text(p: dict) -> str:
    """Pull the invalidation clause out of a position record.

    Two formats in the wild: dedicated `invalidation*` keys (2026-07-24 onward) and, in
    older files, the clause buried in `rationale` prose. For the latter, take a window
    starting at the word "invalidation" rather than scanning the whole record -- prose is
    full of unrelated numbers (entry prices, 52w anchors) that would parse as fake legs.
    """
    # Skip superseded clauses -- a tightened position records both `invalidation_old` and
    # `invalidation_new`, and scoring the retired level re-flags a stop that was just fixed.
    keyed = " ".join(str(p[k]) for k in p
                     if "invalidation" in k.lower() and p[k]
                     and not any(w in k.lower() for w in ("old", "prior", "previous", "was")))
    if keyed:
        return keyed
    for k, v in p.items():
        if not isinstance(v, str):
            continue
        m = re.search(r"invalidation", v, re.I)
        if m:
            return v[m.start():m.start() + 220]
    return ""


def reconcile(prior_path: str, benchmark: str = "SPY") -> dict:
    doc = json.load(open(prior_path))
    bench = bars(benchmark, "1mo")
    bench_ret = bench[-1]["close"] / bench[-2]["close"] - 1 if len(bench) > 1 else 0.0
    asof = bench[-1]["date"]

    out = {"as_of": asof, "benchmark": benchmark,
           "benchmark_day_ret_pct": round(100 * bench_ret, 3), "positions": []}

    for p in _positions(doc):
        tk = p.get("ticker")
        direction = (p.get("direction") or "long").lower()
        entry = p.get("entry_price")
        try:
            b = bars(tk, "3mo")
        except Exception as e:
            out["positions"].append({"ticker": tk, "error": f"{type(e).__name__}: {e}"})
            continue
        close, prev = b[-1]["close"], b[-2]["close"]
        sign = -1 if direction == "short" else 1
        gross = sign * (close / entry - 1) if entry else None
        day = close / prev - 1
        # excess for the position = its directional move less the benchmark's, same sign
        day_excess = sign * (day - bench_ret)

        text = _invalidation_text(p)
        legs = []
        for lvl in (float(x) for x in PRICE_RE.findall(text)):
            dist = (lvl / close - 1)
            legs.append({"kind": "price", "level": lvl,
                         "distance_pct": round(100 * dist, 2),
                         "beyond_entry": bool(entry and ((lvl > entry) if direction == "short" else (lvl < entry)))})
        for lvl in (float(x) for x in RSI_RE.findall(text)):
            r = rsi14(tk)
            legs.append({"kind": "rsi", "level": lvl, "current": r,
                         "distance_pts": round(lvl - r, 2) if r is not None else None})

        # VESTIGIAL: a price stop further away than the open gain, or one that has drifted
        # to the wrong side of entry, cannot protect the position -- it only converts a
        # winner into a loser before firing.
        gain_pct = 100 * gross if gross is not None else 0.0
        vestigial = [l for l in legs if l["kind"] == "price"
                     and (abs(l["distance_pct"]) > max(gain_pct, 0) or l["beyond_entry"])]

        out["positions"].append({
            "ticker": tk, "lane": p.get("lane"), "direction": direction,
            "entry_date": p.get("entry_date"), "entry_price": entry,
            "close": round(close, 4),
            "gross_pnl_pct": round(100 * gross, 2) if gross is not None else None,
            "day_pct": round(100 * day, 2),
            "day_excess_pct": round(100 * day_excess, 2),
            "invalidation": text or None,
            "legs": legs,
            "vestigial": bool(vestigial),
            "vestigial_reason": ("; ".join(
                f"price leg ${l['level']:.2f} is {abs(l['distance_pct']):.1f}% away"
                + (" and beyond entry" if l["beyond_entry"] else "")
                for l in vestigial) or None) if vestigial else None,
        })
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prior", required=True, help="path to the previous conviction_*.json")
    ap.add_argument("--benchmark", default="SPY")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    res = reconcile(a.prior, a.benchmark)
    if a.json:
        print(json.dumps(res, indent=2))
        return 0

    print(f"held-book reconciliation as of {res['as_of']}  "
          f"({res['benchmark']} {res['benchmark_day_ret_pct']:+.2f}% on the day)")
    if not res["positions"]:
        print("  no open positions carried in that file")
    for p in res["positions"]:
        if "error" in p:
            print(f"\n  {p['ticker']}: ERROR {p['error']}")
            continue
        print(f"\n  {p['ticker']} {p['direction']} ({p['lane']}) entry {p['entry_price']} "
              f"{p['entry_date']} -> {p['close']}")
        print(f"    gross {p['gross_pnl_pct']:+.2f}%   today {p['day_pct']:+.2f}%   "
              f"excess {p['day_excess_pct']:+.2f}%")
        for l in p["legs"]:
            if l["kind"] == "price":
                print(f"    price leg ${l['level']:.2f}: {l['distance_pct']:+.2f}% away"
                      + ("  [beyond entry]" if l["beyond_entry"] else ""))
            else:
                print(f"    RSI leg >{l['level']:.0f}: now {l['current']} "
                      f"({l['distance_pts']} pts away)")
        if p["vestigial"]:
            print(f"    ** VESTIGIAL INVALIDATION -- {p['vestigial_reason']}."
                  f"\n       Re-derive as a profit-protection level; it is not currently a stop.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
