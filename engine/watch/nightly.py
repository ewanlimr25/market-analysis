"""The watch-basket nightly step (`DESIGN/110-watch-basket.md` §7 R2), called by `make daily`
after the S-B step (`engine.daily`). `nightly(con, d, force_ledger, ledger_dir)` builds tonight's
universe, evaluates the 17 conditions from LIVE sources (`live.py`, `tier1.py`, `flows.py`,
`series.py` -- results.md §5's replacement table), the stacks and the four baskets, emits one row
per (name, night, basket) for LONG/SHORT/VOL (CONFLICT is logged in the return value only, never
the ledger, DESIGN/110 §3), applies the 21-session episode rule (`engine.watch.basket`), writes to
`ledger/wb/forward_signals.parquet`, and grades earlier open rows at h5/h10/h21 against SPY excess
computed from the screener spine. Fail-soft at the step level (DESIGN/110 §1's null-safety
principle applied to the whole nightly, not just per condition): any exception here is caught and
the return dict says `available: False` with a `reason`, so a broken watch step never blocks the
S-A/S-B report or `signals.json`.
"""
from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from typing import Callable

import pandas as pd

from engine import calendar as cal
from engine import policy as POL
from engine.config import LEDGER_WB_DIR, LEDGER_WB_OPEN
from engine.features.short_side import join_short_side
from engine.watch import bars as B
from engine.watch import basket as BK
from engine.watch import conditions as C
from engine.watch import flows as F
from engine.watch import live as LV
from engine.watch import series as S
from engine.watch import tier1 as T
from engine.watch import universe as U
from engine.watch.wb_ledger import WB_KEY, read_ledger, write_ledger

BARS_FETCH_WORKERS = 16

POLICY_ID = "wb-1.0"
BENCHMARK = "spy_excess"
GRADE_HORIZONS = (5, 10, 21)
EMIT_BASKETS = ("LONG", "SHORT", "VOL")       # CONFLICT is logged only, DESIGN/110 §3
SPY_TICKER = "SPY"

EVAL_COLUMNS = ("ticker", "date", "pct_52w_range", "days_to_cover", "borrow_fee_pct",
                "c_oibuild_raw", "c_crowd_raw", "ivrank_chg_5d", "iv30d", "marketcap",
                "has_tier1_atm_pair", "next_earnings_date", "c_leap_raw", "c_dp_raw")


def _is_missing(x) -> bool:
    return x is None or x is pd.NA or x is pd.NaT or (isinstance(x, float) and x != x)


def _to_bool_or_none(x) -> bool | None:
    return None if _is_missing(x) else bool(x)


def ledger_open(d: date, force_ledger: bool = False) -> bool:
    return d >= LEDGER_WB_OPEN or force_ledger


# =============================================================================================
# Universe + raw inputs, all from live sources (results.md §5)
# =============================================================================================

def build_universe_frame(d: date) -> pd.DataFrame:
    """Tonight's §1 universe plus every raw input the 17 conditions need, all live sources."""
    universe = U.build_universe([d])
    if universe.empty:
        return universe
    universe = LV.add_pct_52w_range(universe)

    oi = LV.build_oi_net_5d([d])
    universe = universe.merge(oi, on=["ticker", "date"], how="left")
    universe["c_oibuild_raw"] = LV.decile_flag(universe["oi_net_5d"])

    prem = LV.build_total_premium([d])
    universe = universe.merge(prem, on=["ticker", "date"], how="left")
    if LV.all_options_file_exists(d):
        universe["tot_prem"] = universe["tot_prem"].fillna(0.0)
    universe["premium_to_mcap"] = universe["tot_prem"] / universe["marketcap"]
    universe["c_crowd_raw"] = LV.decile_flag(universe["premium_to_mcap"])

    ivrank = LV.build_ivrank_chg_5d([d])
    universe = universe.merge(ivrank, on=["ticker", "date"], how="left")

    spine = universe[["ticker", "date"]].reset_index(drop=True)
    side = join_short_side(spine)
    universe = universe.reset_index(drop=True)
    universe["days_to_cover"] = side["days_to_cover"].to_numpy()
    universe["borrow_fee_pct"] = side["borrow_fee"].to_numpy()

    flags = T.build_tier1_flags([d])
    universe = universe.merge(flags, on=["ticker", "date"], how="left")
    universe["has_tier1_atm_pair"] = universe["has_tier1_atm_pair"].fillna(False)

    leap = F.build_leap_flags([d])
    universe = universe.merge(leap[["ticker", "date"]].assign(c_leap_raw=True), on=["ticker", "date"], how="left")
    if LV.all_options_file_exists(d):
        universe["c_leap_raw"] = universe["c_leap_raw"].fillna(False)

    dp = F.build_dp_flags([d])
    universe = universe.merge(dp[["ticker", "date"]].assign(c_dp_raw=True), on=["ticker", "date"], how="left")
    if LV.dark_pool_file_exists(d):
        universe["c_dp_raw"] = universe["c_dp_raw"].fillna(False)

    return universe.reset_index(drop=True)


# =============================================================================================
# The 17 conditions, stacks and baskets (unchanged rules, `conditions.py` / `basket.py`)
# =============================================================================================

def evaluate_conditions(universe: pd.DataFrame, series_map: dict[str, S.TickerSeries | None]) -> pd.DataFrame:
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
            "C-AVWAP": C.c_avwap(bar["avwap_reclaim"]),
            "C-AVWAP-LOSS": C.c_avwap_loss(bar["avwap_loss"]),
            "C-POC": C.c_poc(bar["poc_accept"]),
            "C-POC-LOSS": C.c_poc_loss(bar["poc_loss"]),
            "C-SWING": C.c_swing(bar["swing_up"]),
            "C-SWING-LOSS": C.c_swing_loss(bar["swing_down"]),
            "C-LEAP": C.c_leap(_to_bool_or_none(cols["c_leap_raw"][i])),
            "C-DP": C.c_dp(_to_bool_or_none(cols["c_dp_raw"][i])),
        })
    return pd.DataFrame(rows)


def add_stacks_and_baskets(cond_df: pd.DataFrame) -> pd.DataFrame:
    out = cond_df.copy()
    records = cond_df[list(C.ALL_CONDITIONS)].to_dict("records")
    stack_rows = [BK.stacks(r) for r in records]
    out["bull"] = [s["bull"] for s in stack_rows]
    out["bear"] = [s["bear"] for s in stack_rows]
    out["vol"] = [s["vol"] for s in stack_rows]
    out["true_ids"] = [s["true_ids"] for s in stack_rows]
    out["null_ids"] = [s["null_ids"] for s in stack_rows]
    basket_rows = [BK.baskets(r, s) for r, s in zip(records, stack_rows)]
    for name in BK.BASKET_NAMES:
        out[name] = [b[name] for b in basket_rows]
    return out


def build_ticker_series_map(tickers: list[str], max_workers: int = BARS_FETCH_WORKERS) -> dict[str, S.TickerSeries | None]:
    """Fetches (or confirms cached) daily bars for every ticker ONCE, in parallel, and builds each
    `TickerSeries` from the bars already in hand. Unlike calling `retro.py`'s `warm_bars_cache`
    followed by the generic per-ticker `build_ticker_series` (R1's own sequence, fine for a
    one-time 103-night backtest build), a second, separate fetch pass here would hit every
    permanently-missing ticker's Yahoo 404 (`bars.py`: a failure is never cached) TWICE, every
    single night, forever -- real repeated network cost the nightly's 30 s budget cannot absorb."""
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        bars_list = list(pool.map(B.load_daily_bars, tickers))
    return {t: S.build_ticker_series(t, daily=bars) for t, bars in zip(tickers, bars_list)}


def evaluate_universe(d: date) -> tuple[pd.DataFrame, int]:
    universe = build_universe_frame(d)
    universe_n = int(len(universe))
    if universe.empty:
        cols = ["ticker", "date", *C.ALL_CONDITIONS, "bull", "bear", "vol", "true_ids", "null_ids",
                *BK.BASKET_NAMES]
        return pd.DataFrame(columns=cols), universe_n
    tickers = sorted(universe["ticker"].unique())
    series_map = build_ticker_series_map(tickers)
    cond_df = evaluate_conditions(universe, series_map)
    cond_df = add_stacks_and_baskets(cond_df)
    return cond_df, universe_n


# =============================================================================================
# Episodes (DESIGN/110 §4): LONG/SHORT/VOL history from the persisted ledger; CONFLICT is never
# persisted (§3, "logged, not a basket"), so it has no cross-night history here and is always a
# fresh "episode" in the nightly's return value -- documented in results.md.
# =============================================================================================

def _all_candidate_rows(cond_df: pd.DataFrame) -> pd.DataFrame:
    if cond_df.empty:
        return pd.DataFrame(columns=["ticker", "date", "basket"])
    recs = [{"ticker": row["ticker"], "date": row["date"], "basket": basket}
            for row in cond_df.to_dict("records") for basket in BK.BASKET_NAMES if row[basket]]
    return pd.DataFrame(recs, columns=["ticker", "date", "basket"])


def episode_map(cond_df: pd.DataFrame, existing: pd.DataFrame, d: date) -> dict[tuple[str, str], bool]:
    all_candidates = _all_candidate_rows(cond_df)
    if all_candidates.empty:
        return {}
    emit_cand = all_candidates[all_candidates["basket"].isin(EMIT_BASKETS)]
    conflict_cand = all_candidates[~all_candidates["basket"].isin(EMIT_BASKETS)]
    out = {(r.ticker, r.basket): True for r in conflict_cand.itertuples(index=False)}
    if emit_cand.empty:
        return out
    if existing.empty:
        history = emit_cand
    else:
        prior = existing[["ticker", "basket", "date"]].copy()
        prior["date"] = pd.to_datetime(prior["date"]).dt.date
        history = pd.concat([prior, emit_cand], ignore_index=True)
    start = min(history["date"])
    order = cal.session_index(cal.trading_days(start, d))
    episoded = BK.assign_episodes(history, ["ticker", "basket"], "date", order)
    tonight = episoded[episoded["date"] == d]
    for r in tonight.itertuples(index=False):
        out[(r.ticker, r.basket)] = bool(r.episode_start == d)
    return out


# =============================================================================================
# Ledger rows
# =============================================================================================

def _stamp_row(row: dict, basket: str, episode: bool) -> dict:
    d = row["date"]
    d_str = d.isoformat() if hasattr(d, "isoformat") else d
    base = {"ticker": row["ticker"], "date": d_str, "basket": basket,
            "bull": int(row["bull"]), "bear": int(row["bear"]), "vol": bool(row["vol"]),
            "true_ids": list(row["true_ids"]), "null_ids": list(row["null_ids"]),
            "episode": bool(episode), "benchmark": BENCHMARK,
            "excess_h5": None, "excess_h10": None, "excess_h21": None, "emitted_at": d_str}
    gate_verdict = f"{basket}:{row['bull']}/{row['bear']}:{','.join(row['true_ids'])}"
    return POL.stamp(base, POLICY_ID, POL.ROLE_EXPLORATION, gate_verdict)


def _emit_rows(cond_df: pd.DataFrame, episodes: dict) -> pd.DataFrame:
    if cond_df.empty:
        return pd.DataFrame()
    recs = [_stamp_row(row, basket, episodes.get((row["ticker"], basket), True))
            for row in cond_df.to_dict("records") for basket in EMIT_BASKETS if row[basket]]
    return pd.DataFrame(recs)


def emit(ledger_dir: str, new_rows: pd.DataFrame, existing: pd.DataFrame) -> tuple[int, int, pd.DataFrame]:
    """Append rows whose `WB_KEY` is not already in `existing`; returns (emitted, skipped, the
    frame now on disk -- unchanged from `existing` when nothing new was written)."""
    if new_rows.empty:
        return 0, 0, existing
    POL.require_policy_columns(new_rows)
    if existing.empty:
        fresh = new_rows
    else:
        seen = set(map(tuple, existing[WB_KEY].astype(str).to_numpy()))
        mask = [tuple(str(v) for v in row) not in seen for row in new_rows[WB_KEY].to_numpy()]
        fresh = new_rows[mask]
    emitted, skipped = len(fresh), len(new_rows) - len(fresh)
    if emitted == 0:
        return 0, skipped, existing
    merged = fresh if existing.empty else pd.concat([existing, fresh], ignore_index=True)
    write_ledger(ledger_dir, merged)
    return emitted, skipped, merged


# =============================================================================================
# Grading: h5/h10/h21 SPY excess from the screener spine, filled in once per row per horizon
# =============================================================================================

def grade_open_rows(ledger_dir: str, d: date) -> int:
    """Fills `excess_h5`/`excess_h10`/`excess_h21` on rows whose target session has closed on or
    before `d` and whose value is still null. A cell already filled is never touched again
    (append-only in spirit: only a `None` cell can become a number). Returns the number of cells
    filled tonight."""
    df = read_ledger(ledger_dir)
    if df.empty:
        return 0
    grade_cols = [f"excess_h{h}" for h in GRADE_HORIZONS]
    open_mask = df[grade_cols].isna().any(axis=1)
    if not open_mask.any():
        return 0
    due: dict[tuple[int, int], tuple[date, date]] = {}
    tickers, dates_needed = {SPY_TICKER}, set()
    for idx in df[open_mask].index:
        entry_date = date.fromisoformat(df.at[idx, "date"])
        ticker = df.at[idx, "ticker"]
        tickers.add(ticker)
        for h in GRADE_HORIZONS:
            if pd.notna(df.at[idx, f"excess_h{h}"]):
                continue
            target = cal.next_session(entry_date, h)
            if target > d:
                continue
            due[(idx, h)] = (entry_date, target)
            dates_needed.update((entry_date, target))
    if not due:
        return 0
    closes = LV.load_closes(tickers, dates_needed)
    n_graded = 0
    for (idx, h), (entry_date, target) in due.items():
        ticker = df.at[idx, "ticker"]
        c0, c1 = closes.get((ticker, entry_date)), closes.get((ticker, target))
        s0, s1 = closes.get((SPY_TICKER, entry_date)), closes.get((SPY_TICKER, target))
        if None in (c0, c1, s0, s1) or c0 == 0 or s0 == 0:
            continue
        fwd_ret, spy_ret = c1 / c0 - 1, s1 / s0 - 1
        df.at[idx, f"excess_h{h}"] = fwd_ret - spy_ret
        n_graded += 1
    if n_graded:
        write_ledger(ledger_dir, df)
    return n_graded


# =============================================================================================
# Nightly report shape (the optional `watch_basket` object in `signals.json`)
# =============================================================================================

def _count_distribution(cond_df: pd.DataFrame, col: str, max_count: int) -> dict[str, int]:
    counts = cond_df[col].value_counts().to_dict() if not cond_df.empty else {}
    return {str(i): int(counts.get(i, 0)) for i in range(max_count + 1)}


def _top_n(cond_df: pd.DataFrame, col: str, n: int = 20) -> list[dict]:
    if cond_df.empty:
        return []
    top = cond_df.sort_values([col, "ticker"], ascending=[False, True]).head(n)
    return [{"ticker": r.ticker, col: int(getattr(r, col)), "true_ids": list(r.true_ids)}
            for r in top.itertuples(index=False)]


def _basket_list(cond_df: pd.DataFrame, basket: str, episodes: dict) -> list[dict]:
    if cond_df.empty:
        return []
    sub = cond_df[cond_df[basket]]
    out = [{"ticker": r.ticker, "bull": int(r.bull), "bear": int(r.bear),
            "true_ids": list(r.true_ids), "null_ids": list(r.null_ids),
            "episode": bool(episodes.get((r.ticker, basket), True))}
           for r in sub.itertuples(index=False)]
    return sorted(out, key=lambda x: x["ticker"])


# =============================================================================================
# Entry points
# =============================================================================================

EvaluateFn = Callable[[date], tuple[pd.DataFrame, int]]


def run(con, d: date, ledger_dir: str = LEDGER_WB_DIR, force_ledger: bool = False,
        evaluate_fn: EvaluateFn = evaluate_universe) -> dict:
    existing = read_ledger(ledger_dir)
    cond_df, universe_n = evaluate_fn(d)
    episodes = episode_map(cond_df, existing, d)

    is_open = ledger_open(d, force_ledger)
    new_rows = _emit_rows(cond_df, episodes)
    emitted, skipped = 0, 0
    if is_open:
        emitted, skipped, existing = emit(ledger_dir, new_rows, existing)

    n_graded = grade_open_rows(ledger_dir, d) if is_open else 0

    return {
        "available": True, "reason": None, "universe_n": universe_n,
        "count_distribution": {"bull": _count_distribution(cond_df, "bull", len(C.SIGN_PLUS)),
                                "bear": _count_distribution(cond_df, "bear", len(C.SIGN_MINUS))},
        "top_bull": _top_n(cond_df, "bull"), "top_bear": _top_n(cond_df, "bear"),
        "long": _basket_list(cond_df, "LONG", episodes), "short": _basket_list(cond_df, "SHORT", episodes),
        "vol": _basket_list(cond_df, "VOL", episodes), "conflict": _basket_list(cond_df, "CONFLICT", episodes),
        "ledger_open": is_open, "wb_emitted": emitted, "wb_skipped": skipped, "wb_graded": n_graded,
    }


def _unavailable(d: date, force_ledger: bool, reason: str) -> dict:
    empty = pd.DataFrame()
    return {"available": False, "reason": reason[:300], "universe_n": 0,
            "count_distribution": {"bull": _count_distribution(empty, "bull", len(C.SIGN_PLUS)),
                                    "bear": _count_distribution(empty, "bear", len(C.SIGN_MINUS))},
            "top_bull": [], "top_bear": [], "long": [], "short": [], "vol": [], "conflict": [],
            "ledger_open": ledger_open(d, force_ledger), "wb_emitted": 0, "wb_skipped": 0, "wb_graded": 0}


def nightly(con, d: date, force_ledger: bool = False, ledger_dir: str = LEDGER_WB_DIR,
            evaluate_fn: EvaluateFn = evaluate_universe) -> dict:
    """The production entry point: `run`, timed, never raising. `ledger_dir` follows
    `make daily --ledger-dir` (`engine.daily.wb_ledger_dir`) so a test run never touches the real
    ledger."""
    t0 = time.time()
    try:
        state = run(con, d, ledger_dir, force_ledger, evaluate_fn)
    except Exception as exc:  # the S-A/S-B report must still be written; DESIGN/110 §1 at the step level
        state = _unavailable(d, force_ledger, f"watch_basket step failed: {exc}")
    state["elapsed_s"] = round(time.time() - t0, 2)
    return state
