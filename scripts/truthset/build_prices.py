#!/usr/bin/env python3
"""Truth-set price cache builder.

Fetches daily OHLC (+adjclose, volume) from the Yahoo chart API (the same path the
calibration-audit uses for path-aware outcome resolution) for every ticker in
universe.json plus benchmarks, over a window with enough lead for ATR(14) and enough
tail for the longest forward horizon we can resolve inside the panel.

Output: data/prices.parquet  (columns: ticker, date, open, high, low, close, adjclose, volume)
Stdlib + duckdb only. Threaded with retry/backoff; fail-soft per ticker.

The rebuild MERGES into the existing file (2026-10-03, findings market-analysis D28): the fresh fetch
wins on every (ticker, date) it returns, and rows it no longer returns are kept. Yahoo stops serving a
symbol's past bars once it delists, so replacing the file deleted the history of every name that had
delisted since the last rebuild (13 names and 8 E1 events on 2026-10-03), a survivorship bias in every
backtest that reads this file. Kept rows are listed on stdout. A recycled symbol would therefore carry
the old issuer's bars before the new one's; the KEPT list is where to spot it.
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

# Fetch under the Yahoo alias, store under the PANEL's symbol: features.parquet is keyed BRKB,
# so storing BRK-B would leave the join just as broken, only harder to spot. The map itself now
# lives at the shared Yahoo boundary, `scripts/chart.py` -- this file kept the only copy until
# 2026-09-08, when the watch basket hit the same 404 on four names because it had no copy at all,
# and the one copy that existed was missing BFA and UHALB.
sys.path.insert(0, os.path.join(HERE, ".."))
from chart import YAHOO_ALIASES  # noqa: E402

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

COLUMNS = ("ticker", "date", "open", "high", "low", "close", "adjclose", "volume")
_TYPES = {"ticker": "VARCHAR", "date": "DATE", "open": "DOUBLE", "high": "DOUBLE", "low": "DOUBLE",
          "close": "DOUBLE", "adjclose": "DOUBLE", "volume": "BIGINT"}


def write_merged(rows, out_parquet):
    """Write `rows` (tuples in COLUMNS order) merged over `out_parquet`, atomically. The new rows win
    on (ticker, date); existing rows the fetch did not return are kept. Returns {ticker: kept rows}."""
    import duckdb
    cols = ", ".join(f"{c}::{t} AS {c}" for c, t in _TYPES.items())
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as fh:
        staging = fh.name
        fh.write(",".join(COLUMNS) + "\n")
        for r in rows:
            fh.write(",".join("" if x is None else str(x) for x in r) + "\n")
    tmp = out_parquet + ".tmp"
    try:
        con = duckdb.connect()
        con.execute(f"CREATE TEMP TABLE fresh AS SELECT {cols} FROM read_csv('{staging}', header=true, all_varchar=true)")
        if os.path.exists(out_parquet):
            con.execute(f"""CREATE TEMP TABLE kept AS SELECT {cols} FROM read_parquet('{out_parquet}') o
                            WHERE NOT EXISTS (SELECT 1 FROM fresh f WHERE f.ticker = o.ticker AND f.date = o.date)""")
        else:
            con.execute("CREATE TEMP TABLE kept AS SELECT * FROM fresh WHERE false")
        con.execute(f"""COPY (SELECT * FROM fresh UNION ALL SELECT * FROM kept ORDER BY ticker, date)
                        TO '{tmp}' (FORMAT PARQUET)""")
        os.replace(tmp, out_parquet)
        return dict(con.execute("SELECT ticker, count(*) FROM kept GROUP BY 1 ORDER BY 1").fetchall())
    finally:
        os.unlink(staging)
        if os.path.exists(tmp):
            os.unlink(tmp)


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
        print(f"\nUNPRICED ({len(missing)}/{len(syms)}) -- no bars this run; rows from earlier builds are kept (KEPT"
              " below), nothing after them exists, so fail these CLOSED downstream past their last date:")
        print("  " + " ".join(sorted(missing)))
        print("  If a name here is liquid and current, check YAHOO_ALIASES for a symbol-format mismatch.\n")
    kept = write_merged(all_rows, OUT_PARQUET)
    if kept:
        print(f"KEPT {sum(kept.values())} rows the fetch no longer returns, for {len(kept)} tickers "
              "(delisted or failed this run; their history stays):")
        print("  " + " ".join(f"{t}:{n}" for t, n in kept.items()))
    import duckdb
    n = duckdb.connect().execute(f"SELECT count(*), count(distinct ticker) FROM read_parquet('{OUT_PARQUET}')").fetchone()
    print(f"wrote {OUT_PARQUET}: {n[0]} rows, {n[1]} tickers")


if __name__ == "__main__":
    main()
