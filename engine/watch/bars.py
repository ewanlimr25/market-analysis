"""Daily OHLCV for the watch basket (`DESIGN/110-watch-basket.md` §1, R1 build in §7).

Reuses the G7 earnings-history bars cache (`data/mart/earnings_history/bars/<TICKER>.parquet`,
1,755 names, `engine/mart/earnings_history.py:fetch_bars_cached`) read-only -- this module never
writes there. Anything it fetches or refreshes lands under its own directory,
`data/mart/watch/bars/<TICKER>.parquet`, and the two caches are never merged into one file.

**A cache is only as good as its tail.** `series.evaluate_bar_conditions` needs a bar EXACTLY on
its as-of date and returns all-null otherwise, so a cache that stops one session short silences
every bar-derived condition for that ticker. Until 2026-09-08 nothing here ever refreshed one:
both caches were written once, on 09-07, and the first live nightly evaluated 11 of its 20
conditions as null for all 2,041 universe names. So callers that need a specific session pass
`as_of=` and get a cache guaranteed to reach it if Yahoo has it at all, in one fetch pass:

  1. the freshest of the two caches, when it already covers `as_of` -- no network;
  2. else an incremental `TAIL_RANGE` refresh, merged over that cache (a re-fetched session wins,
     so Yahoo's own correction of a session always lands);
  3. else, when the multi-day array STILL lacks `as_of`, the session recovered from
     `chart.session_bar` -- Yahoo publishes the current session into its multi-day arrays hours
     late, long after the nightly runs (`scripts/chart.py:session_bar`).

Every loader in this package fails soft (`DESIGN/110` §1: "a condition whose input is missing is
null, never false"): a fetch failure returns whatever was already cached -- an empty frame when
that is nothing -- and never an exception. A genuine failure is not written, so it is retried on
the next call; a clean zero-row response IS written (a real "no data" answer, e.g. a dead ticker).
"""
from __future__ import annotations

import os
import sys
from datetime import date

import pandas as pd

from engine import config

EARNINGS_HISTORY_BARS_DIR = os.path.join(config.MART, "earnings_history", "bars")
WATCH_DIR = os.path.join(config.MART, "watch")
WATCH_BARS_DIR = os.path.join(WATCH_DIR, "bars")
YAHOO_RANGE = "10y"
# The refresh window for a ticker whose history we already hold. Wide enough to close a gap of any
# plausible length (a name absent from a few nightlies, a long holiday) without re-paying 10y of
# bars 2,000 times a night: ~8 KB per response against ~100 KB for the full range.
TAIL_RANGE = "3mo"
BAR_COLUMNS = ("date", "open", "high", "low", "close", "adj", "volume")
# A session both the cache and a fresh fetch carry must agree to within this fraction, or the two
# are on different adjustment bases (`_same_basis`). Yahoo serves identical values across ranges,
# so the real signal is a split factor (2x, 3x, ...); the tolerance only absorbs float noise.
REBASE_TOLERANCE = 0.001
REBASE_EPSILON = 1e-9


def _empty_bars() -> pd.DataFrame:
    return pd.DataFrame({c: pd.Series([], dtype=("object" if c == "date" else "float64"))
                          for c in BAR_COLUMNS})


def earnings_history_bars_path(ticker: str) -> str:
    return os.path.join(EARNINGS_HISTORY_BARS_DIR, f"{ticker}.parquet")


def watch_bars_path(ticker: str) -> str:
    return os.path.join(WATCH_BARS_DIR, f"{ticker}.parquet")


def _frame(rows) -> pd.DataFrame:
    """Bar dicts from `scripts/chart.py` -> the module's own frame: `BAR_COLUMNS`, `date` as a
    `datetime.date`, oldest first."""
    if not rows:
        return _empty_bars()
    df = pd.DataFrame(rows)
    df = df.assign(date=pd.to_datetime(df["date"]).dt.date).sort_values("date").reset_index(drop=True)
    return df[list(BAR_COLUMNS)]


def _read(path: str) -> pd.DataFrame | None:
    """A cached frame, or None when the file cannot be used (truncated, wrong schema, unreadable),
    which callers treat exactly as if it were absent -- so the ticker re-fetches in FULL rather
    than tail-refreshing onto nothing.

    Never raises. `nightly.build_ticker_series_map` runs this under a thread pool whose exceptions
    re-raise in the parent, where `nightly()` catches them at STEP level: one bad file would blank
    the whole watch basket instead of nulling one ticker (DESIGN/110 §1).
    """
    try:
        df = pd.read_parquet(path)
        return _empty_bars() if df.empty else _frame(df.to_dict("records"))
    except Exception as exc:  # noqa: BLE001 -- a corrupt cache is one ticker's problem, not the run's
        print(f"[watch.bars] unreadable cache {path}: {exc}")
        return None


def _write(ticker: str, df: pd.DataFrame) -> None:
    path = watch_bars_path(ticker)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # PID-suffixed: this now writes once per universe ticker per night, so a `make daily` and a
    # `retro` build running together would otherwise interleave bytes into one temp file.
    tmp = f"{path}.{os.getpid()}.tmp"
    df.to_parquet(tmp, index=False)
    os.replace(tmp, path)


def _tail_date(df: pd.DataFrame | None) -> date | None:
    """The newest session in `df`, or None when there is none."""
    if df is None or df.empty:
        return None
    return df["date"].iloc[-1]


def _cached(ticker: str, as_of: date | None = None) -> pd.DataFrame | None:
    """The best cached history for `ticker`, or None when neither file exists.

    Freshest, not first-found: once this module has refreshed a ticker its own cache runs ahead of
    the read-only G7 one, and a fixed lookup order would keep serving the stale file forever. But
    reading both files unconditionally costs ~12 s per nightly on a 2,000-name universe (a 10-year
    parquet per ticker, parsed), so a named `as_of` that the first cache already covers ends the
    search there -- the steady-state path, and the reason this module's own cache is tried first.
    """
    frames = []
    for path in (watch_bars_path(ticker), earnings_history_bars_path(ticker)):
        if not os.path.exists(path):
            continue
        df = _read(path)
        if df is None:
            continue
        if as_of is not None and _covers(df, as_of):
            return df
        frames.append(df)
    if not frames:
        return None
    return max(frames, key=lambda f: _tail_date(f) or date.min)


def _covers(df: pd.DataFrame | None, as_of: date | None) -> bool:
    """Whether `df` can answer a question asked as of `as_of`. No `as_of` means the caller has no
    session in mind, so any cache at all will do (the retro panel's behaviour, unchanged)."""
    if df is None:
        return False
    if as_of is None:
        return True
    tail = _tail_date(df)
    return tail is not None and tail >= as_of


def _merge(base: pd.DataFrame | None, add: pd.DataFrame | None) -> pd.DataFrame:
    """`base` extended by `add`; on a session both carry, `add` wins -- it is the newer read, and
    that is how Yahoo's official bar replaces one recovered from the single-day endpoint."""
    frames = [f for f in (base, add) if f is not None and not f.empty]
    if not frames:
        return _empty_bars()
    out = pd.concat(frames, ignore_index=True)
    return (out.drop_duplicates(subset="date", keep="last")
               .sort_values("date").reset_index(drop=True)[list(BAR_COLUMNS)])


def _same_basis(cached: pd.DataFrame, fetched: pd.DataFrame | None) -> bool:
    """Whether `fetched` can be merged onto `cached` at all.

    Yahoo back-adjusts the WHOLE raw OHLC history when a split executes -- MNST 2:1 (effective
    2026-08-11) serves 2026-07-01 as 48.67 today and served ~97.35 before it, identically under
    every range. A cache written on the old basis, tail-refreshed on the new one, would carry both:
    a fake -50% overnight move at the boundary, which is not a null but a VALUE, so ATR-14, RSI-14,
    the zigzag pivots and the 52-week extremes all emit confident nonsense from it for as long as
    the boundary sits inside `series.LOOKBACK_52W_SESSIONS`. So the two are merged only when they
    agree on a session they both carry -- and NO shared session means the basis cannot be checked,
    which is equally disqualifying (a cache staler than `TAIL_RANGE` would also leave a hole).
    """
    if cached.empty or fetched is None or fetched.empty:
        return True                                # nothing to splice
    both = cached.merge(fetched, on="date", suffixes=("_cached", "_fetched"))
    if both.empty:
        return False
    ref = both["close_cached"].abs().clip(lower=REBASE_EPSILON)
    return bool((((both["close_cached"] - both["close_fetched"]).abs() / ref) <= REBASE_TOLERANCE).all())


def _chart():
    """`scripts/chart.py`, the repo's single Yahoo boundary (share-class aliasing, null-session
    healing and split back-adjustment all live there)."""
    if config.SCRIPTS not in sys.path:
        sys.path.insert(0, config.SCRIPTS)
    import chart  # noqa: E402 -- scripts/chart.py, network

    return chart


def _fetch_daily(ticker: str, rng: str) -> pd.DataFrame | None:
    """Yahoo's multi-day daily array. None when the CALL failed (not cached, retried next time);
    an empty frame is a real answer and is cached."""
    try:
        rows = _chart().bars(ticker, rng)
    except Exception as exc:  # noqa: BLE001 -- one bad ticker must not abort a nightly/panel run
        print(f"[watch.bars] Yahoo fetch failed for {ticker}: {exc}")
        return None
    return _frame(rows)


def _today() -> date:
    """Indirected so a test can pin it; `_fetch_session` is the only caller."""
    return date.today()


def _fetch_session(ticker: str, as_of: date) -> pd.DataFrame | None:
    """The `as_of` session from the single-day endpoint, or None.

    Only TODAY is reachable this way -- the endpoint always answers about the current session --
    so a backfill or a retro panel returns before the request rather than paying a round-trip per
    ticker for a result that would be discarded. The returned bar's date is checked even then.
    """
    if as_of != _today():
        return None
    try:
        bar = _chart().session_bar(ticker)
    except Exception as exc:  # noqa: BLE001 -- same fail-soft contract as the daily fetch
        print(f"[watch.bars] Yahoo session fetch failed for {ticker}: {exc}")
        return None
    if not bar:
        return None
    frame = _frame([bar])
    return frame if _tail_date(frame) == as_of else None


def _refresh(ticker: str, cached: pd.DataFrame | None, rng: str, as_of: date | None) -> pd.DataFrame:
    """One fetch pass: the incremental tail when history is already held, the full `rng` when it is
    not, then the as-of session if the daily array still falls short. Never returns less than
    `cached`."""
    fetched = _fetch_daily(ticker, TAIL_RANGE if cached is not None else rng)
    if cached is not None and not _same_basis(cached, fetched):
        full = _fetch_daily(ticker, rng)           # the cache is unmergeable; only a whole series
        if full is not None and not full.empty:    # fetched at once is internally coherent
            cached, fetched = None, full
    if fetched is None and cached is None:
        return _empty_bars()                       # nothing held, nothing fetched, nothing cached
    merged = _merge(cached, fetched)
    if as_of is not None and not _covers(merged, as_of):
        merged = _merge(merged, _fetch_session(ticker, as_of))
    if cached is None or not merged.equals(cached):
        _write(ticker, merged)                     # an outage must not rewrite the whole universe
    return merged


def load_daily_bars(ticker: str, rng: str = YAHOO_RANGE, *, as_of: date | None = None,
                    force: bool = False) -> pd.DataFrame:
    """Daily OHLCV for `ticker`, oldest first, columns `BAR_COLUMNS`.

    `as_of` and `force` are keyword-only: `as_of` was inserted ahead of `force`, and a stale
    3-positional call would otherwise read a bool as a date. `as_of` is the session the caller
    must be able to evaluate: pass it and a cache that stops
    earlier is refreshed (see the module docstring for the three steps). Omit it and any cached
    frame is returned as-is. `force` re-fetches regardless. Never raises -- an unresolvable ticker
    returns an empty frame (`_empty_bars()`), which every condition in `conditions.py` treats as
    `None`, never `False`.
    """
    cached = None if force else _cached(ticker, as_of)
    if _covers(cached, as_of):
        return cached
    return _refresh(ticker, cached, rng, as_of)


def bars_as_of(daily: pd.DataFrame, as_of: date) -> pd.DataFrame:
    """`daily` truncated to rows with `date <= as_of` -- the point-in-time slice every indicator
    and condition in this package must use (no lookahead)."""
    if daily.empty:
        return daily
    return daily[daily["date"] <= as_of].reset_index(drop=True)


def weekly_bars(daily: pd.DataFrame) -> pd.DataFrame:
    """Resample daily bars to one row per ISO week (anchored Friday): `open` = the week's first
    session's open, `high`/`low` = the week's extremes, `close` = the week's LAST session's close
    (not necessarily a Friday -- a holiday-shortened week still closes on its last trading day),
    `volume` = the week's summed volume. Weeks with no trading session are dropped."""
    if daily.empty:
        return pd.DataFrame({c: pd.Series([], dtype=("object" if c == "week_end" else "float64"))
                              for c in ("week_end", "open", "high", "low", "close", "volume")})
    d = daily.copy()
    d["date"] = pd.to_datetime(d["date"])
    d = d.set_index("date").sort_index()
    wk = d.resample("W-FRI").agg({"open": "first", "high": "max", "low": "min",
                                   "close": "last", "volume": "sum"})
    wk = wk.dropna(subset=["close"]).reset_index().rename(columns={"date": "week_end"})
    wk["week_end"] = wk["week_end"].dt.date
    return wk
