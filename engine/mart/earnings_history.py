"""`earnings_history`: per-ticker realized earnings-move history and its point-in-time trailing
summary (G7, `findings/RESEARCH/47-edge-gaps.md` §2 G7). Feeds a per-name historical-move filter
that becomes a **registered S-A challenger after 2026-12-01** (D13; this module builds the
feature, not the filter -- nothing here changes S-A's frozen parameters).

VERIFIED BLOCKER (2026-09-07), read this before changing the date source below
====================================================================================
The spec this module implements asked for "the last 10 years of earnings dates from Finnhub
`/calendar/earnings`". Probed live against the real endpoint before writing any fetcher:

  - `/calendar/earnings?symbol=X&from=<10y ago>&to=<today>` returns EMPTY for any window ending
    more than about a month in the past (checked AAPL and the unfiltered endpoint against
    2024-01, 2025-01, 2025-09, 2026-01, 2026-06: all zero rows). The symbol-filtered form only
    ever returns the small number of near-term (upcoming, plus a few weeks trailing) rows Finnhub
    currently has estimates for -- for ADBE, exactly two rows regardless of how wide the window is
    (2026-09-10 and 2026-12-08).
  - `/stock/earnings?symbol=X&limit=40` is capped at 4 quarters (1 year) of trailing EPS-surprise
    history on the free tier regardless of `limit` (AAPL returned exactly 4 rows for `limit=40`).
  - The unfiltered `/calendar/earnings?from=..&to=..` DOES return real rows, but only within
    roughly one month back to several months forward of the call date, capped at 1500 rows total
    (sorted so a wide forward window silently drops the NEAREST dates once the cap is hit).

Conclusion: Finnhub's free tier has no historical earnings-date depth. This is consistent with
how the sibling repo already scoped this endpoint (`uw-daily-analysis/DESIGN/50-desk-sheet.md`
§2: "Finnhub `/calendar/earnings` (free, verified)" is cited only for the forward 10-session
calendar, never for history). `fetch_finnhub_calendar` below is still built and used -- it is the
literal ask and it IS useful for the forward-looking calendar -- but the HISTORICAL date source
for this module is `engine.mart.earnings_events` (already built, already point-in-time safe,
already carries an AMC/BMO `timing` label verified against `RESEARCH/40 E1`, 3,260 events across
1,755 tickers over the 2026-03-13 .. 2026-09-04 panel). See `results.md` for what this means for
the resulting per-name N (thin: most tickers get 0-2 prior events on this panel).

What this module does with real (Finnhub, Yahoo) data
====================================================================================
  1. `fetch_bars_cached`: ten years of split/dividend-adjusted daily bars per ticker via
     `scripts/chart.py` (`RESEARCH/20 §8.4`), cached under
     `data/mart/earnings_history/bars/<ticker>.parquet`, wrapped fail-soft the way
     `engine/mart/vix.py` wraps the same module (never raises; an empty frame on failure).
  2. `fetch_finnhub_calendar_cached`: the forward-looking Finnhub calendar per ticker (real,
     rate-limited at `RATE_LIMIT_SLEEP_SECONDS` between calls, cached under
     `data/mart/earnings_history/finnhub/<ticker>.json`), used only to log the AMC/BMO `hour`
     field where Finnhub actually has it (near-term names) and to keep the literal ask buildable
     against fixtures when the key is absent.
  3. `build_events`: one row per (ticker, E) from `earnings_events`, joined to that ticker's Yahoo
     bars, with the realized close-to-close move computed on the AMC/BMO alignment already in
     `earnings_events.timing` (postmarket -> pre=E, post=next session; premarket -> pre=prev
     session, post=E; unresolved -> flagged `timing_unknown`).
  4. `point_in_time_summary`: per ticker, an expanding-window trailing summary computed strictly
     from events with `E` earlier than the row's own `E` (never itself, never a later event).
  5. `validate_against_panel`: the Yahoo-bar move vs. `earnings_events.realized_move` for every
     one of the 3,260 panel events. NOT a cross-vendor check: `earnings_events.realized_move`
     reads `data/prices.parquet`, and `scripts/truthset/build_prices.py`'s own docstring says it
     fetches from "the Yahoo chart API (the same path" this module uses -- both numbers trace back
     to Yahoo. The result (100.0% match on the 3,259 available rows, exact to float precision) is
     still real evidence: it confirms this module's AMC/BMO pre/post alignment reproduces
     `earnings_events`' own construction bug-for-bug, that there is no split-adjustment drift
     between the two Yahoo pulls, and that the join/lookup code has no date-substitution bugs. See
     `results.md` §4.2 for the full accounting, including the caveat.

CLI: `python3 -m engine.mart.earnings_history --rebuild [--limit N] [--finnhub-sample N] [--force]`
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import date, timedelta

import duckdb
import pandas as pd

from engine import config
from engine.mart import earnings_events as ee
from engine.mart import store

if config.SCRIPTS not in sys.path:
    sys.path.insert(0, config.SCRIPTS)

TABLE_DIR = os.path.join(config.MART, "earnings_history")
BARS_DIR = os.path.join(TABLE_DIR, "bars")
FINNHUB_DIR = os.path.join(TABLE_DIR, "finnhub")
EVENTS_PATH = os.path.join(TABLE_DIR, "events.parquet")
SUMMARY_PATH = os.path.join(TABLE_DIR, "summary.parquet")

YAHOO_RANGE = "10y"
FINNHUB_BASE_URL = "https://finnhub.io/api/v1"
FINNHUB_TIMEOUT_SECONDS = 30
RATE_LIMIT_PER_MINUTE = 60          # Finnhub free-tier ceiling; constraint from the task brief
RATE_LIMIT_SLEEP_SECONDS = 60.0 / RATE_LIMIT_PER_MINUTE * 1.05   # 5% margin

MOVE_ABS_TOL = 0.005                # validation tolerance vs the panel: 0.5 points absolute ...
MOVE_REL_TOL = 0.03                 # ... or 3% relative to the panel's own move, whichever is larger
BIG_MOVE_THRESHOLDS = (0.05, 0.10)  # "share of moves > 5% and > 10%"

EVENTS_COLUMNS = (
    "ticker", "E", "er_time", "timing", "how", "pre", "post",
    "yahoo_close_pre", "yahoo_close_post", "realized_move_yahoo", "abs_move_yahoo",
    "panel_realized_move", "abs_diff_vs_panel", "matches_panel",
    "timing_unknown", "available",
)
SUMMARY_COLUMNS = (
    "ticker", "E", "n_prior", "median_abs_move_prior", "mean_abs_move_prior",
    "max_abs_move_prior", "share_gt5_prior", "share_gt10_prior",
)


# =============================================================================================
# Yahoo bars: fetch, cache, fail-soft (mirrors engine/mart/vix.py's wrapping of chart.py)
# =============================================================================================


def bars_path(ticker: str) -> str:
    return os.path.join(BARS_DIR, f"{ticker}.parquet")


def _empty_bars() -> pd.DataFrame:
    return pd.DataFrame(
        {"date": pd.Series([], dtype=object), "open": pd.Series([], dtype="float64"),
         "high": pd.Series([], dtype="float64"), "low": pd.Series([], dtype="float64"),
         "close": pd.Series([], dtype="float64"), "adj": pd.Series([], dtype="float64"),
         "volume": pd.Series([], dtype="float64")})


def fetch_bars_cached(ticker: str, rng: str = YAHOO_RANGE, force: bool = False) -> pd.DataFrame:
    """Ten years of daily bars for `ticker`, cached to disk. Never raises: returns an empty frame
    with a one-line warning on any network or parse failure (chart.py's own fail-soft-per-ticker
    philosophy, `scripts/chart.py`'s CLI `except Exception` branch).

    A genuine failure (network, parse) is NOT cached, so the next rebuild retries it; a clean
    response with zero rows (a real Yahoo answer, e.g. for a dead ticker) IS cached, so it is not
    refetched forever.
    """
    path = bars_path(ticker)
    if not force and os.path.exists(path):
        return pd.read_parquet(path)
    try:
        from chart import bars  # noqa: E402 (scripts/chart.py, network)

        rows = bars(ticker, rng)
    except Exception as exc:  # noqa: BLE001 - one bad ticker must not abort a panel-wide run
        print(f"[earnings_history] Yahoo bars fetch failed for {ticker}: {exc}")
        return _empty_bars()
    df = pd.DataFrame(rows) if rows else _empty_bars()
    if not df.empty:
        df = df.assign(date=pd.to_datetime(df["date"]).dt.date).sort_values("date").reset_index(drop=True)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    df.to_parquet(tmp, index=False)
    os.replace(tmp, path)
    return df


def _close_lookup(bars_df: pd.DataFrame) -> dict[date, float]:
    """{date: close} (split-adjusted, NOT dividend-adjusted -- matched to the screener's own
    convention; see `scripts/chart.py`'s `close` vs `adj` distinction in its module docstring)."""
    if bars_df.empty:
        return {}
    return dict(zip(bars_df["date"], bars_df["close"]))


# =============================================================================================
# Finnhub calendar: fetch, cache, fail-soft. Real, rate-limited, but see the module docstring --
# it cannot supply history, so it is used only for the forward-looking `hour` field.
# =============================================================================================


class FinnhubError(RuntimeError):
    pass


def _http_get_json(url: str) -> object:
    req = urllib.request.Request(url, headers={"User-Agent": "market-analysis-g7/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=FINNHUB_TIMEOUT_SECONDS) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError, ValueError, TimeoutError) as exc:
        raise FinnhubError(f"Finnhub request failed: {exc}") from exc


def finnhub_calendar_path(ticker: str) -> str:
    return os.path.join(FINNHUB_DIR, f"{ticker}.json")


def fetch_finnhub_calendar_cached(ticker: str, frm: str, to: str, key: str, getter=_http_get_json,
                                  force: bool = False) -> dict:
    """One symbol-filtered `/calendar/earnings` call, cached to disk.

    Always returns a dict with `available`; never raises. `available=False` covers both a missing
    key and a request failure, each with a distinct `skip_reason` so a caller (or a human reading
    the cache) can tell them apart.
    """
    path = finnhub_calendar_path(ticker)
    if not force and os.path.exists(path):
        return json.loads(open(path, encoding="utf-8").read())
    if not key:
        payload = {"ticker": ticker, "available": False, "skip_reason": "FINNHUB_API_KEY not set",
                  "rows": []}
    else:
        q = urllib.parse.urlencode({"symbol": ticker, "from": frm, "to": to, "token": key})
        try:
            resp = getter(f"{FINNHUB_BASE_URL}/calendar/earnings?{q}")
            rows = resp.get("earningsCalendar", []) if isinstance(resp, dict) else []
            payload = {"ticker": ticker, "available": True, "skip_reason": None, "rows": rows}
        except FinnhubError as exc:
            payload = {"ticker": ticker, "available": False, "skip_reason": str(exc), "rows": []}
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh)
    return payload


def fetch_finnhub_sample(tickers: list[str], key: str, as_of: date, forward_days: int = 180,
                         getter=_http_get_json, force: bool = False,
                         sleep_seconds: float = RATE_LIMIT_SLEEP_SECONDS) -> dict[str, dict]:
    """Rate-limited Finnhub calendar fetch over a bounded ticker sample. One call per ticker not
    already cached; sleeps `sleep_seconds` between LIVE calls only (cache hits are free)."""
    frm, to = as_of.isoformat(), (as_of + timedelta(days=forward_days)).isoformat()
    out = {}
    for tk in tickers:
        cached = not force and os.path.exists(finnhub_calendar_path(tk))
        out[tk] = fetch_finnhub_calendar_cached(tk, frm, to, key, getter, force)
        if not cached:
            time.sleep(sleep_seconds)
    return out


# =============================================================================================
# Events: earnings_events (dates + AMC/BMO alignment) x Yahoo bars (realized move)
# =============================================================================================


def load_earnings_events(con: duckdb.DuckDBPyConnection | None = None) -> pd.DataFrame:
    """Every `earnings_events` row (the historical date + AMC/BMO source, see module docstring)."""
    con = con or duckdb.connect()
    cols = "ticker, E, er_time, timing, how, pre, post, realized_move"
    df = store.read_table(con, ee.TABLE, columns=cols)
    if df.empty:
        return df
    for c in ("E", "pre", "post"):
        df[c] = pd.to_datetime(df[c]).dt.date
    return df.sort_values(["ticker", "E"]).reset_index(drop=True)


def ticker_universe(events: pd.DataFrame) -> list[str]:
    return sorted(events["ticker"].unique()) if not events.empty else []


def _event_row(row: pd.Series, closes: dict[date, float]) -> dict:
    pre_close, post_close = closes.get(row.pre), closes.get(row.post)
    available = pre_close is not None and post_close is not None and pre_close > 0 and post_close > 0
    move = (post_close / pre_close - 1.0) if available else float("nan")
    abs_move = abs(move) if available else float("nan")
    panel_move = float(row.realized_move) if pd.notna(row.realized_move) else float("nan")
    if available and not math.isnan(panel_move):
        diff = abs(abs_move - panel_move)
        tol = max(MOVE_ABS_TOL, MOVE_REL_TOL * panel_move)
        matches = bool(diff <= tol)
    else:
        diff, matches = float("nan"), False
    return {
        "ticker": row.ticker, "E": row.E, "er_time": row.er_time, "timing": row.timing,
        "how": row.how, "pre": row.pre, "post": row.post,
        "yahoo_close_pre": pre_close if pre_close is not None else float("nan"),
        "yahoo_close_post": post_close if post_close is not None else float("nan"),
        "realized_move_yahoo": move, "abs_move_yahoo": abs_move,
        "panel_realized_move": panel_move, "abs_diff_vs_panel": diff, "matches_panel": matches,
        "timing_unknown": row.timing == "unresolved", "available": available,
    }


def build_events(events: pd.DataFrame, bars_by_ticker: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """One row per (ticker, E); pure given the earnings_events frame and a ticker -> bars map."""
    if events.empty:
        return pd.DataFrame({c: pd.Series(dtype=object) for c in EVENTS_COLUMNS})
    rows = []
    for row in events.itertuples(index=False):
        closes = _close_lookup(bars_by_ticker.get(row.ticker, pd.DataFrame()))
        rows.append(_event_row(row, closes))
    out = pd.DataFrame(rows)
    return out.sort_values(["ticker", "E"]).reset_index(drop=True)[list(EVENTS_COLUMNS)]


# =============================================================================================
# Point-in-time trailing summary
# =============================================================================================


def _ticker_summary(g: pd.DataFrame) -> pd.DataFrame:
    """Expanding-window summary for one ticker's events, sorted by E ascending.

    Row i's stats use ONLY rows [0, i) that are `available` -- never row i itself, never a later
    event, and never an unavailable (missing-bars) event.
    """
    g = g.sort_values("E").reset_index(drop=True)
    moves = g["abs_move_yahoo"].where(g["available"]).tolist()
    out = []
    seen: list[float] = []
    for i in range(len(g)):
        if seen:
            s = pd.Series(seen)
            n = len(seen)
            out.append({
                "ticker": g.loc[i, "ticker"], "E": g.loc[i, "E"], "n_prior": n,
                "median_abs_move_prior": float(s.median()), "mean_abs_move_prior": float(s.mean()),
                "max_abs_move_prior": float(s.max()),
                "share_gt5_prior": float((s > BIG_MOVE_THRESHOLDS[0]).mean()),
                "share_gt10_prior": float((s > BIG_MOVE_THRESHOLDS[1]).mean()),
            })
        else:
            out.append({"ticker": g.loc[i, "ticker"], "E": g.loc[i, "E"], "n_prior": 0,
                        "median_abs_move_prior": float("nan"), "mean_abs_move_prior": float("nan"),
                        "max_abs_move_prior": float("nan"), "share_gt5_prior": float("nan"),
                        "share_gt10_prior": float("nan")})
        m = moves[i]
        if m is not None and not (isinstance(m, float) and math.isnan(m)):
            seen.append(m)
    return pd.DataFrame(out)


def point_in_time_summary(events_with_moves: pd.DataFrame) -> pd.DataFrame:
    """Per-ticker expanding trailing summary; see `_ticker_summary` for the point-in-time rule."""
    if events_with_moves.empty:
        return pd.DataFrame({c: pd.Series(dtype=object) for c in SUMMARY_COLUMNS})
    parts = [_ticker_summary(g) for _, g in events_with_moves.groupby("ticker", sort=False)]
    out = pd.concat(parts, ignore_index=True) if parts else pd.DataFrame(
        {c: pd.Series(dtype=object) for c in SUMMARY_COLUMNS})
    return out.sort_values(["ticker", "E"]).reset_index(drop=True)[list(SUMMARY_COLUMNS)]


# =============================================================================================
# Validation against the panel (task 4)
# =============================================================================================


@dataclass(frozen=True)
class ValidationResult:
    n_total: int
    n_available: int
    n_matches: int
    match_rate: float               # of the AVAILABLE rows
    coverage_rate: float            # available / total
    mean_abs_diff: float
    worst: pd.DataFrame             # top 10 largest |diff| among available rows


def validate_against_panel(events: pd.DataFrame, worst_n: int = 10) -> ValidationResult:
    n_total = len(events)
    avail = events[events["available"]]
    n_available = len(avail)
    n_matches = int(avail["matches_panel"].sum()) if n_available else 0
    mean_diff = float(avail["abs_diff_vs_panel"].mean()) if n_available else float("nan")
    worst = (avail.sort_values("abs_diff_vs_panel", ascending=False).head(worst_n)
            if n_available else avail)
    return ValidationResult(
        n_total=n_total, n_available=n_available, n_matches=n_matches,
        match_rate=(n_matches / n_available if n_available else float("nan")),
        coverage_rate=(n_available / n_total if n_total else float("nan")),
        mean_abs_diff=mean_diff, worst=worst)


# =============================================================================================
# Orchestration / CLI
# =============================================================================================


def _write(df: pd.DataFrame, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    df.to_parquet(tmp, index=False)
    os.replace(tmp, path)


def rebuild(limit: int | None = None, finnhub_sample: int = 0, force: bool = False,
           key: str | None = None) -> tuple[pd.DataFrame, pd.DataFrame, ValidationResult]:
    """Full build: load dates, fetch bars for every ticker (cached), optionally sample Finnhub,
    compute events + summary + validation, and write both parquet files."""
    from _env import get_key  # local import: keep the network key resolution isolated (scripts/_env.py)

    con = duckdb.connect()
    events_raw = load_earnings_events(con)
    tickers = ticker_universe(events_raw)
    if limit is not None:
        tickers = tickers[:limit]
        events_raw = events_raw[events_raw.ticker.isin(tickers)].reset_index(drop=True)

    t0 = time.time()
    bars_by_ticker = {tk: fetch_bars_cached(tk, force=force) for tk in tickers}
    bars_elapsed = time.time() - t0

    if finnhub_sample > 0:
        key = key if key is not None else get_key("FINNHUB_API_KEY")
        fetch_finnhub_sample(tickers[:finnhub_sample], key, date.today(), force=force)

    events = build_events(events_raw, bars_by_ticker)
    summary = point_in_time_summary(events)
    validation = validate_against_panel(events)

    _write(events, EVENTS_PATH)
    _write(summary, SUMMARY_PATH)

    n_bars_ok = sum(1 for df in bars_by_ticker.values() if not df.empty)
    print(f"earnings_history: {len(tickers)} tickers, {n_bars_ok} with Yahoo bars "
          f"({bars_elapsed:.0f}s), {len(events)} events, "
          f"match_rate={validation.match_rate:.3f} coverage={validation.coverage_rate:.3f}")
    return events, summary, validation


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="build earnings_history (events.parquet, summary.parquet)")
    ap.add_argument("--rebuild", action="store_true", required=True)
    ap.add_argument("--limit", type=int, default=None, help="cap the ticker universe (smoke test)")
    ap.add_argument("--finnhub-sample", type=int, default=0,
                    help="fetch the live Finnhub calendar for the first N tickers only")
    ap.add_argument("--force", action="store_true", help="refetch even if a cache file exists")
    args = ap.parse_args(argv)
    rebuild(limit=args.limit, finnhub_sample=args.finnhub_sample, force=args.force)
    return 0


if __name__ == "__main__":
    sys.exit(main())
