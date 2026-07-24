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
import urllib.request, json, time, os, sys
from concurrent.futures import ThreadPoolExecutor, as_completed

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "..", "data")
UNIV = os.path.join(DATA, "universe.json")
OUT_CSV = os.path.join(DATA, "prices.csv")
OUT_PARQUET = os.path.join(DATA, "prices.parquet")

# lead for ATR(14)/regime context; tail through last panel date
START = "2026-01-15"
END   = "2026-07-18"   # inclusive-ish; chart API uses period2 exclusive of next day (extended 2026-07-18 to include panel through 2026-07-17)

def epoch(d): return int(time.mktime(time.strptime(d, "%Y-%m-%d")))

def fetch(sym, retries=4):
    p1, p2 = epoch(START), epoch(END) + 86400
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}"
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
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(fetch, s): s for s in syms}
        for n, f in enumerate(as_completed(futs), 1):
            rows = f.result()
            if rows:
                ok += 1
                all_rows.extend(rows)
            if n % 50 == 0:
                print(f"  {n}/{len(syms)} done, {ok} ok, {len(all_rows)} rows")
    # write csv
    with open(OUT_CSV, "w") as fh:
        fh.write("ticker,date,open,high,low,close,adjclose,volume\n")
        for r in all_rows:
            fh.write(",".join("" if x is None else str(x) for x in r) + "\n")
    print(f"wrote {OUT_CSV} ({len(all_rows)} rows, {ok}/{len(syms)} symbols)")
    # load to parquet via duckdb
    try:
        import duckdb
        con = duckdb.connect()
        con.execute(f"""COPY (SELECT ticker, date::DATE AS date, open, high, low, close, adjclose, volume
                          FROM read_csv_auto('{OUT_CSV}', header=true)) TO '{OUT_PARQUET}' (FORMAT PARQUET)""")
        n = con.execute(f"SELECT count(*), count(distinct ticker) FROM read_parquet('{OUT_PARQUET}')").fetchone()
        print(f"wrote {OUT_PARQUET}: {n[0]} rows, {n[1]} tickers")
    except Exception as e:
        print("parquet step failed (csv still written):", e)

if __name__ == "__main__":
    main()
