#!/usr/bin/env python3
"""Truth-set universe builder — the ticker spine `build_prices.py` fetches.

Exists because `universe.json` was hand-frozen at 785 tickers on 2026-06-28 and never
regenerated, while `build_features.py` built its spine from the live screener every night.
By 2026-08-07 that was 783 tickers in prices.parquet against 2,471 in features.parquet:
**1,688 feature tickers had no price row at all.**

That gap fails OPEN, which is why it survived so long. A lane that gates a candidate on
prices.parquet gets an empty result for a missing ticker, and an empty result is
indistinguishable from "the check passed" unless the caller tests for presence. The names
most likely to be missing are exactly the ones that entered the liquid universe recently.

Gate: the SAME liquid screener gate `build_features.py` applies to its spine
(close >= 5 AND close * avg30_volume >= 50e6), taken as a union across all panel days —
a ticker that cleared on ANY day needs price history, because features carries the
per-day gate itself and lanes join back to prices for every row they consider.

No ETP/issue_type filter here on purpose: this is a price-fetch list, not a tradeable
universe. Lanes exclude ETFs themselves, and they need the bars to do it.

Output: data/universe.json (sorted JSON list of tickers). Benchmarks (SPY/QQQ/IWM) are
unioned in by build_prices.py, not stored here.

Usage:
  python3 scripts/truthset/build_universe.py            # rewrite data/universe.json
  python3 scripts/truthset/build_universe.py --dry-run  # report the delta, write nothing
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "..", "data")
OUT = os.path.join(DATA, "universe.json")
SCREENER = os.path.expanduser("~/Documents/Stocks/Stock Screener")

MIN_CLOSE = 5
MIN_DOLLAR_ADV = 50e6
# Yahoo's chart API wants BRK-B, not BRK.B. The panel has been all-plain so far; anything
# that is not is surfaced rather than silently mangled or dropped.
PLAIN_TICKER = re.compile(r"[A-Z]{1,5}")


def build(dry_run: bool = False) -> dict:
    import duckdb

    files = sorted(glob.glob(os.path.join(SCREENER, "stock-screener-*.parquet")))
    if not files:
        sys.exit(f"no screener exports under {SCREENER} — nothing to build from")

    con = duckdb.connect()
    file_list = "['" + "','".join(files) + "']"
    rows = con.execute(
        f"""SELECT DISTINCT ticker FROM read_parquet({file_list})
            WHERE close >= {MIN_CLOSE} AND close * avg30_volume >= {MIN_DOLLAR_ADV}
            ORDER BY ticker"""
    ).fetchall()
    tickers = [r[0] for r in rows]

    odd = [t for t in tickers if not PLAIN_TICKER.fullmatch(t)]
    if odd:
        print(f"WARNING: {len(odd)} non-plain symbols may need Yahoo normalization: {odd[:20]}")

    try:
        previous = set(json.load(open(OUT)))
    except (OSError, ValueError):
        previous = set()

    added = sorted(set(tickers) - previous)
    dropped = sorted(previous - set(tickers))

    print(f"screener panel : {len(files)} days, {os.path.basename(files[0])} -> {os.path.basename(files[-1])}")
    print(f"liquid gate    : close>={MIN_CLOSE} AND close*avg30_volume>={MIN_DOLLAR_ADV:.0f}")
    print(f"universe       : {len(previous)} -> {len(tickers)}  (+{len(added)} / -{len(dropped)})")
    if dropped:
        # A drop means a name that once cleared the gate no longer appears anywhere in the
        # panel. Worth a look: prices for it will stop refreshing, and any open position or
        # unmatured signal row on that name silently loses its outcome data.
        print(f"DROPPED (check for open rows): {dropped[:20]}")

    if dry_run:
        print("--dry-run: no write")
    else:
        with open(OUT, "w") as fh:
            json.dump(tickers, fh, indent=0)
            fh.write("\n")
        print(f"wrote {OUT} ({len(tickers)} tickers)")

    return {"n": len(tickers), "added": len(added), "dropped": len(dropped)}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="report the delta without writing")
    build(dry_run=ap.parse_args().dry_run)


if __name__ == "__main__":
    main()
