"""The watch-basket retrospective panel builder (`DESIGN/110-watch-basket.md` §1, §5; R1 build,
§7; C-DIV-D added 2026-09-07 evening, re-run into this same panel). Assembles, for every (ticker,
night) in the §1 universe over the panel 2026-03-13 to 2026-09-04, every one of the 20 condition
values, the `bull`/`bear`/`vol` stacks and the LONG/SHORT/VOL/CONFLICT basket flags --
`data/backtest/wb_conditions.parquet`. The five descriptive tables of §5 are built from that frame
in `retro_tables.py`; `scripts/watch_retro.py` is the CLI entry point that calls `run()` and writes
both output files plus the results docs.

Source mapping (documented again in `results.md` for the owner):

  C-HIGH, C-LOW, C-OIBUILD, C-CROWD, C-IVUP, C-DP  <- `data/features.parquet` (pct_52w_range,
      oi_net_5d, netprem_mcap, ivrank_chg_5d, dp_prem) as the task brief names them for the
      retrospective; a universe ticker-night absent from that spine (a different filter: close>=5
      and 20-day dollar ADV>=50M, DESIGN/20 §8.2) gets `None` on those conditions, not `False`.
  C-SHORT        <- `engine.features.short_side.join_short_side` (FINRA days_to_cover,
      point-in-time; IBKR borrow_fee -- only one historical snapshot exists, 2026-09-07, so this
      condition is `None` on almost every panel night unless FINRA alone already decides `True`).
  C-VOL          <- screener `iv30d`/`marketcap`/`next_earnings_date` (universe frame) plus
      `tier1.build_tier1_flags` (S-C's F7/F8 tier-1 ATM pair).
  C-RSI, C-DIV, C-DIV-D, C-AVWAP(-LOSS), C-POC(-LOSS), C-POC-A(-LOSS), C-SWING(-LOSS)  <- `series.py` on the
      G7/own-cache Yahoo daily bars, one `TickerSeries` per unique ticker in the panel's universe.
  C-LEAP, C-DP   <- `flows.py`, one DuckDB scan per session of the raw All Options / Dark Pool
      exports (note C-DP is also usable from `features.parquet`'s `dp_prem`; this build uses the
      features.parquet value per the task brief -- see `results.md` for the two-source note).
"""
from __future__ import annotations

import os
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import date

import pandas as pd

from engine import config
from engine.features.short_side import join_short_side
from engine.mart import store
from engine.watch import bars as B
from engine.watch import basket as BK
from engine.watch import conditions as C
from engine.watch import flows as F
from engine.watch import series as S
from engine.watch import tier1 as T
from engine.watch import universe as U

PANEL_START = date(2026, 3, 13)
PANEL_END = date(2026, 9, 4)
FEATURES_PATH = os.path.join(config.DATA, "features.parquet")
RETURNS_PATH = os.path.join(config.DATA, "returns.parquet")
GRADE_HORIZONS = (5, 10, 21)

FEATURES_JOIN_COLS = ("pct_52w_range", "oi_net_5d", "netprem_mcap", "ivrank_chg_5d", "dp_prem")


def panel_dates() -> list[date]:
    return [d for d in store.available_dates("daily_contract") if PANEL_START <= d <= PANEL_END]


def load_features(path: str = FEATURES_PATH) -> pd.DataFrame:
    df = pd.read_parquet(path, columns=["ticker", "date", *FEATURES_JOIN_COLS])
    df["date"] = pd.to_datetime(df["date"]).dt.date
    return df


def load_returns(path: str = RETURNS_PATH) -> pd.DataFrame:
    df = pd.read_parquet(path, columns=["ticker", "date", "horizon", "excess", "resolved"])
    df["date"] = pd.to_datetime(df["date"]).dt.date
    return df[df["horizon"].isin(GRADE_HORIZONS) & df["resolved"]].reset_index(drop=True)


def _decile_flag(series: pd.Series) -> pd.Series:
    """Top-decile flag within one night's values: `rank(pct=True) >= 0.9` among non-null values,
    `None` (object dtype throughout, so it never collides with pandas' bool-dtype NA handling)
    where the value itself is null."""
    ranked = series.rank(pct=True, method="average")
    flag = (ranked >= 0.9).astype(object)
    flag[series.isna()] = None
    return flag


def add_cross_sectional_deciles(universe: pd.DataFrame) -> pd.DataFrame:
    """Adds `c_oibuild_raw`/`c_crowd_raw` (`True`/`False`/`None`, object dtype) -- the top decile
    of `oi_net_5d` and of `netprem_mcap` computed PER NIGHT across the universe (DESIGN/110 §2)."""
    out = universe.copy()
    out["c_oibuild_raw"] = out.groupby("date")["oi_net_5d"].transform(_decile_flag)
    out["c_crowd_raw"] = out.groupby("date")["netprem_mcap"].transform(_decile_flag)
    return out


def attach_short_side(universe: pd.DataFrame) -> pd.DataFrame:
    spine = universe[["ticker", "date"]].reset_index(drop=True)
    side = join_short_side(spine)
    out = universe.reset_index(drop=True).copy()
    out["days_to_cover"] = side["days_to_cover"].to_numpy()
    out["borrow_fee_pct"] = side["borrow_fee"].to_numpy()
    return out


def attach_tier1(universe: pd.DataFrame, dates: list[date]) -> pd.DataFrame:
    flags = T.build_tier1_flags(dates)
    out = universe.merge(flags, on=["ticker", "date"], how="left")
    out["has_tier1_atm_pair"] = out["has_tier1_atm_pair"].fillna(False)
    return out


def attach_leap_dp(universe: pd.DataFrame, dates: list[date]) -> pd.DataFrame:
    leap = F.build_leap_flags(dates)
    dp = F.build_dp_flags(dates)
    out = universe.merge(leap[["ticker", "date"]].assign(c_leap_raw=True), on=["ticker", "date"], how="left")
    out = out.merge(dp[["ticker", "date"]].assign(c_dp_flow_raw=True), on=["ticker", "date"], how="left")
    out["c_leap_raw"] = out["c_leap_raw"].fillna(False)
    out["c_dp_flow_raw"] = out["c_dp_flow_raw"].fillna(False)
    return out


def warm_bars_cache(tickers: list[str], as_of: date | None = None, max_workers: int = 16) -> None:
    """Fetch (or confirm-cached) daily bars for every ticker up front, in parallel -- a plain
    HTTP GET releases the GIL while waiting, so threads help even under CPython.

    `as_of` is the panel's LAST night: a cache that stops before it evaluates that night's
    bar-derived conditions as null for every ticker (`bars.py`, 2026-09-08). Passing the last
    night covers every earlier one too, since the refresh only ever extends the tail."""
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        list(pool.map(lambda t: B.load_daily_bars(t, as_of=as_of), tickers))


def build_ticker_series_map(tickers: list[str], as_of: date | None = None) -> dict[str, S.TickerSeries | None]:
    """`as_of` is passed through only so `bars.load_daily_bars` can stop at the first cache that
    covers it; `warm_bars_cache` has already done any fetching."""
    return {t: S.build_ticker_series(t, daily=B.load_daily_bars(t, as_of=as_of)) for t in tickers}


def _is_missing(x) -> bool:
    return x is None or x is pd.NA or x is pd.NaT or (isinstance(x, float) and x != x)


def _to_bool_or_none(x) -> bool | None:
    return None if _is_missing(x) else bool(x)


def _dp_flag(dp_prem) -> bool | None:
    """C-DP from `features.parquet`'s `dp_prem` (the task brief's named source), null-safe."""
    return None if _is_missing(dp_prem) else bool(dp_prem >= F.C_DP_MIN_PREMIUM)


EVAL_COLUMNS = ("ticker", "date", "pct_52w_range", "days_to_cover", "borrow_fee_pct",
                "c_oibuild_raw", "c_crowd_raw", "ivrank_chg_5d", "iv30d", "marketcap",
                "has_tier1_atm_pair", "next_earnings_date", "c_leap_raw", "dp_prem")


def evaluate_conditions(universe: pd.DataFrame, series_map: dict[str, S.TickerSeries | None]) -> pd.DataFrame:
    """Evaluates the 20 conditions for every row of `universe` (already carrying every raw input
    column this module's `attach_*`/`add_cross_sectional_deciles` functions produce). Returns a
    frame with `ticker`, `date` and one column per condition id (`True`/`False`/`None`).

    Plain-list iteration (not `itertuples`/`_asdict`) -- at panel scale (tens of thousands of
    ticker-nights) the dict-construction overhead of `_asdict()` per row is measurable; this stays
    a pure Python loop only because `series.evaluate_bar_conditions` itself needs one lookup per
    (ticker, night) into that ticker's own `TickerSeries`.
    """
    cols = {c: universe[c].tolist() for c in EVAL_COLUMNS}
    n = len(universe)
    rows = []
    for i in range(n):
        ticker, dt = cols["ticker"][i], cols["date"][i]
        bar = S.evaluate_bar_conditions(series_map.get(ticker), dt)
        next_earn = cols["next_earnings_date"][i]
        days_to_earn = None if _is_missing(next_earn) else (next_earn - dt).days
        rows.append({
            "ticker": ticker, "date": dt,
            "C-HIGH": C.c_high(cols["pct_52w_range"][i]),
            "C-LOW": C.c_low(cols["pct_52w_range"][i]),
            "C-SHORT": C.c_short(cols["days_to_cover"][i], cols["borrow_fee_pct"][i]),
            "C-OIBUILD": C.c_oibuild(_to_bool_or_none(cols["c_oibuild_raw"][i])),
            "C-CROWD": C.c_crowd(_to_bool_or_none(cols["c_crowd_raw"][i])),
            "C-IVUP": C.c_ivup(cols["ivrank_chg_5d"][i]),
            "C-VOL": C.c_vol(cols["iv30d"][i], cols["marketcap"][i],
                             bool(cols["has_tier1_atm_pair"][i]), days_to_earn),
            "C-RSI": C.c_rsi(bar["rsi_last"]),
            "C-DIV": C.c_div(bar["div_flag"]),
            "C-DIV-D": C.c_div_d(bar["div_d_flag"]),
            "C-AVWAP": C.c_avwap(bar["avwap_reclaim"]),
            "C-AVWAP-LOSS": C.c_avwap_loss(bar["avwap_loss"]),
            "C-POC": C.c_poc(bar["poc_accept"]),
            "C-POC-LOSS": C.c_poc_loss(bar["poc_loss"]),
            "C-POC-A": C.c_poc_a(bar["poc_a_accept"]),
            "C-POC-A-LOSS": C.c_poc_a_loss(bar["poc_a_loss"]),
            "C-SWING": C.c_swing(bar["swing_up"]),
            "C-SWING-LOSS": C.c_swing_loss(bar["swing_down"]),
            "C-LEAP": C.c_leap(bool(cols["c_leap_raw"][i])),
            "C-DP": C.c_dp(_dp_flag(cols["dp_prem"][i])),
        })
    return pd.DataFrame(rows)


def add_stacks_and_baskets(cond_df: pd.DataFrame) -> pd.DataFrame:
    out = cond_df.copy()
    stack_rows = [BK.stacks(row) for row in cond_df[list(C.ALL_CONDITIONS)].to_dict("records")]
    out["bull"] = [s["bull"] for s in stack_rows]
    out["bear"] = [s["bear"] for s in stack_rows]
    out["vol"] = [s["vol"] for s in stack_rows]
    basket_rows = [BK.baskets(row, stack) for row, stack in
                   zip(cond_df[list(C.ALL_CONDITIONS)].to_dict("records"), stack_rows)]
    for name in BK.BASKET_NAMES:
        out[name] = [b[name] for b in basket_rows]
    out["CONFLICT_LOGGED"] = out["CONFLICT"]  # DESIGN/110 §3: logged only, never a tradable basket
    return out


def build_panel() -> tuple[pd.DataFrame, dict]:
    """The full R1 pipeline. Returns the assembled `wb_conditions`-shaped frame and a dict of
    diagnostics (`elapsed_s`, `n_universe_rows`, `n_tickers`, `n_nights`)."""
    t0 = time.time()
    dates = panel_dates()
    universe = U.build_universe(dates)
    features = load_features()
    universe = universe.merge(features, on=["ticker", "date"], how="left")
    universe = add_cross_sectional_deciles(universe)
    universe = attach_short_side(universe)
    universe = attach_tier1(universe, dates)
    universe = attach_leap_dp(universe, dates)

    tickers = sorted(universe["ticker"].unique())
    panel_end = max(dates) if dates else None
    warm_bars_cache(tickers, as_of=panel_end)
    series_map = build_ticker_series_map(tickers, as_of=panel_end)

    cond_df = evaluate_conditions(universe, series_map)
    cond_df = add_stacks_and_baskets(cond_df)
    diagnostics = {
        "elapsed_s": time.time() - t0, "n_universe_rows": int(len(universe)),
        "n_tickers": int(len(tickers)), "n_nights": int(len(dates)),
    }
    return cond_df, diagnostics
