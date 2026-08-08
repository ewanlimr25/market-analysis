#!/usr/bin/env python3
"""Truth-set price cache builder.

Fetches daily OHLC (+adjclose, volume) from the Yahoo chart API (the same path the
calibration-audit uses for path-aware outcome resolution) for every ticker in
universe.json plus benchmarks, over a window with enough lead for ATR(14) and enough
tail for the longest forward horizon we can resolve inside the panel.

Output: data/prices.parquet  (columns: ticker, date, open, high, low, close, adjclose, volume)
Stdlib + duckdb only. Threaded with retry/backoff; fail-soft per ticker.
"""
from __future__ import annotations
import urllib.request, json, time, os, sys, datetime, tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "..", "data")
UNIV = os.path.join(DATA, "universe.json")
OUT_PARQUET = os.path.join(DATA, "prices.parquet")

# lead for ATR(14)/regime context; tail through last panel date
START = "2026-01-15"

# The panel writes share classes concatenated (BRKB); the Yahoo chart API wants them
# hyphenated (BRK-B). Both are plain A-Z strings, so nothing about BRKB *looks* like it
# needs translating -- it just 404s, and a 404 here is a ticker with no price rows, which
# is the fail-open gap this cache exists to close. Fetch under the alias, store under the
# PANEL's symbol: features.parquet is keyed BRKB, so storing BRK-B would leave the join
# just as broken, only harder to spot.
YAHOO_ALIASES = {
    "BRKB": "BRK-B",
    "BFB": "BF-B",
    "HEIA": "HEI-A",
    "MOGA": "MOG-A",
    "PBRA": "PBR-A",
}

def resolve_end():
    """Panel tail date. Defaults to TODAY so the truth set cannot silently rot.

    A hardcoded END is what let the panel sit 5 sessions stale on 2026-07-24 while
    every lane still read from it — the constant was correct when written and simply
    was never bumped again. Override with `--end YYYY-MM-DD` (or TRUTHSET_END) when
    you need to reproduce a historical panel edge exactly.
    Note the chart API treats period2 as exclusive of the next day, so END lands on
    the last TRADING day <= END (a weekend END just resolves back to that Friday).
    """
    for i, a in enumerate(sys.argv):
        if a == "--end" and i + 1 < len(sys.argv):
            return sys.argv[i + 1]
        if a.startswith("--end="):
            return a.split("=", 1)[1]
    return os.environ.get("TRUTHSET_END") or datetime.date.today().isoformat()

END = resolve_end()

def epoch(d): return int(time.mktime(time.strptime(d, "%Y-%m-%d")))

def fetch(sym, retries=4):
    """Fetch `sym`'s bars, labelling every row with `sym` itself (the panel's symbol)
    even when the request goes out under a different Yahoo alias."""
    query = YAHOO_ALIASES.get(sym, sym)
    p1, p2 = epoch(START), epoch(END) + 86400
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{query}"
           f"?period1={p1}&period2={p2}&interval=1d&events=div%2Csplit")
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=25) as r:
                d = json.load(r)
            res = d["chart"]["result"][0]
            ts = res["timestamp"]
            q = res["indicators"]["quote"][0]
            adj = res["indicators"].get("adjclose", [{}])[0].get("adjclose", [None]*len(ts))
            rows = []
            for j, t in enumerate(ts):
                o, h, l, c, v = q["open"][j], q["high"][j], q["low"][j], q["close"][j], q["volume"][j]
                if c is None:
                    continue
                day = time.strftime("%Y-%m-%d", time.gmtime(t))
                ac = adj[j] if adj and adj[j] is not None else c
                rows.append((sym, day, o, h, l, c, ac, v))
            return rows
        except Exception as e:
            last = e
            time.sleep(0.6 * (i + 1) + 0.2 * (hash(sym) % 5) / 5)
    sys.stderr.write(f"FAIL {sym}: {last}\n")
    return []

def main():
    syms = sorted(set(json.load(open(UNIV))) | {"SPY", "QQQ", "IWM"})
    print(f"fetching {len(syms)} symbols {START}..{END}")
    all_rows = []
    ok = 0
    missing = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(fetch, s): s for s in syms}
        for n, f in enumerate(as_completed(futs), 1):
            rows = f.result()
            if rows:
                ok += 1
                all_rows.extend(rows)
            else:
                missing.append(futs[f])
            if n % 50 == 0:
                print(f"  {n}/{len(syms)} done, {ok} ok, {len(all_rows)} rows")
    print(f"fetched {len(all_rows)} rows, {ok}/{len(syms)} symbols")
    # Surfaced loudly, because this is the failure mode that fails OPEN: a ticker with no
    # price rows makes every downstream gate return an empty result, and an empty result
    # reads as "check passed" unless the caller tests for presence. Treat anything listed
    # here as unpriced -> not tradeable, never as cleared.
    if missing:
        print(f"\nUNPRICED ({len(missing)}/{len(syms)}) -- no bars, fail these CLOSED downstream:")
        print("  " + " ".join(sorted(missing)))
        print("  If a name here is liquid and current, check YAHOO_ALIASES for a symbol-format mismatch.\n")
    # CSV is a staging format for duckdb's loader, not an output. It used to be written
    # to data/prices.csv, where it sat as a 12MB duplicate of the parquet that no script
    # ever read. Staged in a tempfile instead so the only artifact is the parquet.
    import duckdb
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as fh:
        staging = fh.name
        fh.write("ticker,date,open,high,low,close,adjclose,volume\n")
        for r in all_rows:
            fh.write(",".join("" if x is None else str(x) for x in r) + "\n")
    try:
        con = duckdb.connect()
        con.execute(f"""COPY (SELECT ticker, date::DATE AS date, open, high, low, close, adjclose, volume
                          FROM read_csv_auto('{staging}', header=true)) TO '{OUT_PARQUET}' (FORMAT PARQUET)""")
        n = con.execute(f"SELECT count(*), count(distinct ticker) FROM read_parquet('{OUT_PARQUET}')").fetchone()
        print(f"wrote {OUT_PARQUET}: {n[0]} rows, {n[1]} tickers")
    finally:
        os.unlink(staging)

if __name__ == "__main__":
    main()
