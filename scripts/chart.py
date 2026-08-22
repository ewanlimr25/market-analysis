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

# Yahoo blanks individual sessions at random -- see `bars()`. Which sessions come back null
# varies per REQUEST, not per ticker or endpoint, so a retry on a rotated host decorrelates the
# draw. Two hosts is enough: the 2026-08-15 audit emptied 115 hole-y tickers down to 1 this way.
HOSTS = ("query2", "query1")
MAX_FETCH_TRIES = 4


def _parse(res: dict) -> tuple[dict[str, dict], list[str], list[dict]]:
    """Chart-API result -> (bars keyed by date, the FULL session grid, split events).

    The grid comes from `timestamp`, which Yahoo populates even for sessions whose OHLC is
    null -- that is what makes a blanked session distinguishable from a non-trading day.
    """
    ts, q = res["timestamp"], res["indicators"]["quote"][0]
    # Yahoo omits `adjclose` on some symbols; fall back to raw close rather than failing.
    adj = (res["indicators"].get("adjclose") or [{}])[0].get("adjclose") or q["close"]
    grid, by_date = [], {}
    for i, t in enumerate(ts):
        d = dt.datetime.fromtimestamp(t, dt.UTC).strftime("%Y-%m-%d")
        grid.append(d)
        if q["close"][i] is None or adj[i] is None:
            continue
        by_date[d] = {"date": d, "open": q["open"][i], "high": q["high"][i],
                      "low": q["low"][i], "close": q["close"][i], "adj": adj[i],
                      "volume": q["volume"][i]}
    splits = [{"date": dt.datetime.fromtimestamp(s["date"], dt.UTC).strftime("%Y-%m-%d"),
               "factor": float(s["denominator"]) / float(s["numerator"]),
               "ratio": str(s.get("splitRatio", ""))}
              for s in ((res.get("events") or {}).get("splits") or {}).values()]
    return by_date, grid, sorted(splits, key=lambda s: s["date"])


def _interior_holes(by_date: dict[str, dict], grid: list[str]) -> list[str]:
    """Sessions on the grid that fall strictly INSIDE the ticker's own span but have no bar.

    Interior only, deliberately. A ticker that simply stops (delisting, cash merger) trails off
    the end of the grid, and retrying that forever would be a bug -- the 2026-08-15 audit's four
    cash-merger delistings must stay INCONCLUSIVE rather than be papered over.
    """
    if not by_date:
        return []
    lo, hi = min(by_date), max(by_date)
    return [d for d in grid if lo < d < hi and d not in by_date]


def _apply_splits(by_date: dict[str, dict], splits: list[dict]) -> dict[str, dict]:
    """Back-adjust `adj` across any split Yahoo has not yet propagated into `adjclose`.

    Yahoo's adjclose is normally split-adjusted, but it LAGS on freshly-executed splits. MNST
    2:1 (effective 2026-08-11) was still serving adj == raw close on both sides four sessions
    later: 90.36 -> 45.53. Any window crossing that books a fake -50%, which dwarfs every real
    signal this repo measures. Detected by comparing the observed jump across the split to the
    split factor -- if the boundary move looks more like the factor than like a normal session,
    the series is unadjusted and every pre-split `adj` is scaled.

    Returns a new mapping; the input is not mutated.
    """
    out = {d: dict(b) for d, b in by_date.items()}
    for sp in splits:
        before = sorted(d for d in out if d < sp["date"])
        after = sorted(d for d in out if d >= sp["date"])
        if not before or not after:
            continue                                  # split sits at the edge of the range
        jump = out[after[0]]["adj"] / out[before[-1]]["adj"]
        if abs(jump - sp["factor"]) >= abs(jump - 1.0):
            continue                                  # already adjusted -- normal 1-day move
        for d in before:
            out[d] = {**out[d], "adj": out[d]["adj"] * sp["factor"]}
    return out


def _fetch(ticker: str, rng: str, host: str) -> dict:
    url = (f"https://{host}.finance.yahoo.com/v8/finance/chart/{ticker}"
           f"?range={rng}&interval=1d&events=div%2Csplit")
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=25) as r:
        return json.load(r)["chart"]["result"][0]


def _healed(ticker: str, rng: str) -> tuple[dict[str, dict], list[str]]:
    """Fetch + self-heal, returning (bars keyed by date, the FULL session grid).

    Split out from `bars()` so callers that need to know what is MISSING can get the grid;
    `bars()` alone returns a sparse list that is indistinguishable from a dense one.
    """
    res = _fetch(ticker, rng, HOSTS[0])
    by_date, grid, splits = _parse(res)

    for attempt in range(1, MAX_FETCH_TRIES):
        if not _interior_holes(by_date, grid):
            break
        try:
            more, more_grid, more_splits = _parse(_fetch(ticker, rng, HOSTS[attempt % len(HOSTS)]))
        except Exception:                             # noqa: BLE001 -- a failed retry is not
            continue                                  # fatal; we still have the first fetch
        by_date = {**more, **by_date}                 # keep what we already trust
        grid = more_grid if len(more_grid) > len(grid) else grid
        splits = splits or more_splits

    return _apply_splits(by_date, splits), grid


def bars_grid(ticker: str, rng: str = "6mo") -> tuple[list[dict], list[str]]:
    """`bars()` plus the full session grid, so a caller can see which sessions are absent."""
    by_date, grid = _healed(ticker, rng)
    return [b for _, b in sorted(by_date.items())], grid


def gaps(ticker: str, rng: str = "6mo") -> list[str]:
    """Interior sessions with no bar after every retry -- an UNHEALABLE vendor gap.

    Not every hole is transient. EQR was served missing 11 sessions (2026-07-23 -> 08-10)
    identically on both hosts AND both query forms, and the truth-set rebuild inherited it;
    a previously-RESOLVED call became INCONCLUSIVE a week later. Retrying cannot fix that,
    so callers must be able to ASK. [audit 2026-08-22]
    """
    by_date, grid = _healed(ticker, rng)
    return _interior_holes(by_date, grid)


def bars(ticker: str, rng: str = "6mo") -> list[dict]:
    """Daily OHLCV + `adj` (split/dividend-adjusted close), oldest first.

    **Use `adj`, not `close`, for any multi-day return or excess** -- the truth set
    (`truthset/build_prices.py`) and every calibration-audit resolver measure on adjusted
    closes, so mixing the two silently mis-prices any window containing a dividend or split.

    Self-heals two Yahoo defects that both corrupt returns silently (found 2026-08-15):

    1. **Transient null closes.** The chart endpoint intermittently serves `close: null` for
       individual sessions on perfectly liquid names -- GD, MSM, MAT, PLNT among 115 tickers in
       one audit pass -- and which sessions blank varies per request. Dropping them leaves a
       hole, and a window whose entry or exit lands in one silently fails to resolve. Any
       interior hole is re-fetched on a rotated host and merged, up to MAX_FETCH_TRIES.
    2. **Unpropagated splits** -- see `_apply_splits`.

    A hole that survives every retry is left as a genuine gap; callers must still handle a
    missing date rather than assume the grid is dense -- use `gaps()` or `bars_grid()` to
    detect one instead of indexing by position.
    """
    return bars_grid(ticker, rng)[0]


def rets(ticker: str, horizons=(5, 10), rng: str = "6mo") -> dict:
    """Trailing simple returns over N TRADING days, anchored on the SESSION GRID by date.

    Previously this walked back `h` POSITIONS in the returned bar list. That is only the same
    thing when the series is dense, and an unhealable vendor gap makes it silently wrong:
    on EQR (11 missing sessions) `rets(10)` reached back 21 real sessions and still labelled
    itself `ret10` -- a 2.1x overstatement, in the read path `held_book.py` and the lanes use.

    Anchors on `grid` instead, and REFUSES (returns None + `retN_why`) when the anchor session
    has no bar, rather than substituting a different one. `retN_gaps` counts missing sessions
    inside the window even when both endpoints are present, so a caller can tell that the
    return is arithmetically fine but the window is not the h sessions it claims.

    Returns are computed on `adj`, per this module's own rule for multi-day returns -- the old
    close-based read booked the split factor as a price move on any lookback crossing a split.
    [audit 2026-08-22]
    """
    rows, grid = bars_grid(ticker, rng)
    if not rows:
        return {"close": None, "date": None}
    by_date = {b["date"]: b for b in rows}
    last = rows[-1]["date"]
    gi = grid.index(last)
    out = {"close": round(rows[-1]["close"], 4), "date": last}

    for h in horizons:
        ai = gi - h
        if ai < 0:
            out[f"ret{h}"], out[f"ret{h}_from"] = None, None
            out[f"ret{h}_why"] = f"only {gi} sessions of history before {last}"
            continue
        anchor = grid[ai]
        window = grid[ai:gi + 1]
        out[f"ret{h}_from"] = anchor
        out[f"ret{h}_sessions"] = h
        out[f"ret{h}_gaps"] = sum(1 for d in window if d not in by_date)
        if anchor not in by_date:
            out[f"ret{h}"] = None
            out[f"ret{h}_why"] = (f"no bar on anchor session {anchor} (vendor gap) -- "
                                  f"refusing to substitute a different session")
            continue
        out[f"ret{h}"] = by_date[last]["adj"] / by_date[anchor]["adj"] - 1
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
            # Only the bare `retN` keys are values; `_from`/`_sessions`/`_gaps`/`_why` are
            # metadata and must not be formatted as percentages. [audit 2026-08-22]
            for k in sorted(k for k in v if k.startswith("ret") and k[3:].isdigit()):
                if v[k] is None:
                    parts.append(f"{k} UNAVAILABLE ({v.get(k + '_why', 'no reason given')})")
                    continue
                note = f" [{v[k + '_gaps']} session(s) missing in window]" if v.get(k + "_gaps") else ""
                parts.append(f"{k} {100*v[k]:+.3f}% (vs {v[k + '_from']}){note}")
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
