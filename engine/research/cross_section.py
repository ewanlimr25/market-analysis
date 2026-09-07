"""G4/G5 orchestrator: weekly cross-section of the IV spread, put skew, O/S ratio and the IV-spread
week-over-week change (RESEARCH/47 §2 G4/G5), formed at each Friday close on the panel.

Pipeline per formation Friday `d`:
  1. `engine.mart.daily_contract` partition for `d`, restricted to hot-chains-covered contracts
     (`hc_iv` not null -- RESEARCH/20 §4: the vendor's own per-contract EOD IV on the liquid ~90%
     of the tape). `delta_last` (from the same row, sourced from All Options) supplies delta.
  2. Per ticker: the expiry nearest 30 calendar days (`xs_factors.nearest_expiry`); universe
     eligibility requires that expiry to carry at least one hot-chains call with delta in
     [0.20, 0.60] and one put with delta in [-0.60, -0.20] (`xs_factors.has_delta_band`).
  3. For eligible tickers: `xs_factors.match_iv_at_delta` at 0.50 (call), -0.50 (put), -0.25 (put)
     -> `iv_spread`, `put_skew`. `data/features.parquet` (the screener spine, symlinked into every
     worktree) supplies `marketcap` (>= $1B, the other universe leg), `log_mcap`, `total_volume`,
     `call_volume`/`put_volume` (`xs_factors.os_ratio`) and `sector`.
  4. `engine.features.short_side.join_short_side` attaches point-in-time `short_interest` /
     `days_to_cover` as of that Friday.
  5. `data/returns.parquet` (horizon=5, `resolved=True`) supplies next-week excess.
  6. The immediately preceding formation's `iv_spread` (only when the calendar gap is <= 10 days,
     i.e. a true consecutive week -- the panel has multi-week gaps, see `DELTA_MAX_GAP_DAYS`)
     supplies `d_iv_spread`.

`run()` assembles the full panel and the 8-test table (4 factors x raw/residual), BH-corrected
across all 8, plus the power/projected-date read and the CBOE-chain-vs-hot-chains skew check.
"""
from __future__ import annotations

import os
from datetime import date

import numpy as np
import pandas as pd

from engine import config
from engine.features.short_side import join_short_side
from engine.mart import cboe_chain as CC
from engine.mart import store
from engine.research import xs_factors as XF
from engine.research import xs_stats as XS

FEATURES_FILE = os.path.join(config.DATA, "features.parquet")
RETURNS_FILE = os.path.join(config.DATA, "returns.parquet")
OUTCOME_HORIZON = 5                  # trading days, ~ one calendar week
DELTA_MAX_GAP_DAYS = 10              # only treat as a "one-week" change within this calendar gap
UNIVERSE_MCAP_MIN = 1e9
CONTROL_COLS = ["log_mcap", "total_volume", "short_interest", "days_to_cover"]
FACTOR_COLS = ["iv_spread", "put_skew", "os_ratio", "d_iv_spread"]
BH_FDR = 0.05
POWER_MIN_EFFECT_FLOOR = 1e-4        # a zero/near-zero observed mean IC has nothing to power on


# ------------------------------------------------------------------------------- formation dates


def formation_fridays() -> list[date]:
    """Every Friday with a `daily_contract` partition AND a resolved horizon-5 return in
    `data/returns.parquet` (the last panel Friday, 2026-09-04, has no resolved outcome yet and is
    excluded). Ascending."""
    dc_dates = set(store.available_dates("daily_contract"))
    fridays = sorted(d for d in dc_dates if d.weekday() == 4)
    if not os.path.exists(RETURNS_FILE):
        return []
    ret = pd.read_parquet(RETURNS_FILE, columns=["date", "horizon", "resolved"])
    ret = ret[ret["horizon"] == OUTCOME_HORIZON]
    ret["date"] = pd.to_datetime(ret["date"]).dt.date
    resolved_days = set(ret.loc[ret["resolved"], "date"])
    return [f for f in fridays if f in resolved_days]


# ------------------------------------------------------------------------------- per-week universe


def _load_hot_chain_day(d: date) -> pd.DataFrame:
    df = store.read_partition("daily_contract", d)
    hot = df[df["hc_iv"].notna()].copy()
    hot["iv"] = pd.to_numeric(hot["hc_iv"], errors="coerce")
    return hot


def _ticker_factor_row(ticker: str, rows: pd.DataFrame) -> dict | None:
    """One eligible ticker's raw factor reads for the expiry nearest 30 days, or `None` if the
    ticker fails the delta-coverage leg of universe eligibility."""
    expiries = rows[["expiry", "dte_cal"]]
    expiry = XF.nearest_expiry(expiries)
    if expiry is None:
        return None
    at_expiry = rows[rows["expiry"] == expiry]
    calls = XF.clean_deltas(at_expiry[at_expiry["option_type"] == "call"][["delta_last", "iv"]]
                             .rename(columns={"delta_last": "delta"}), sign=+1)
    puts = XF.clean_deltas(at_expiry[at_expiry["option_type"] == "put"][["delta_last", "iv"]]
                            .rename(columns={"delta_last": "delta"}), sign=-1)
    if not (XF.has_delta_band(calls, XF.ELIGIBLE_CALL_DELTA_BAND)
            and XF.has_delta_band(puts, XF.ELIGIBLE_PUT_DELTA_BAND)):
        return None
    atm_call = XF.match_iv_at_delta(calls, XF.TARGET_CALL_DELTA)
    atm_put = XF.match_iv_at_delta(puts, XF.TARGET_PUT_DELTA_ATM)
    put_25d = XF.match_iv_at_delta(puts, XF.TARGET_PUT_DELTA_25D)
    return {
        "ticker": ticker, "expiry_used": expiry, "dte_cal_used": int(at_expiry["dte_cal"].iloc[0]),
        "n_calls_hot": int(len(calls)), "n_puts_hot": int(len(puts)),
        "atm_call_iv": atm_call.iv, "atm_call_method": atm_call.method,
        "atm_put_iv": atm_put.iv, "atm_put_method": atm_put.method,
        "put25_iv": put_25d.iv, "put25_method": put_25d.method,
        "iv_spread": XF.iv_spread(atm_call, atm_put), "put_skew": XF.put_skew(put_25d, atm_call),
    }


def build_week_factors(d: date, hot: pd.DataFrame | None = None,
                        screener: pd.DataFrame | None = None,
                        join_short_side_fn=join_short_side) -> pd.DataFrame:
    """One row per universe-eligible ticker for formation Friday `d`: delta-matched IV reads,
    `iv_spread`, `put_skew`, `os_ratio`, controls and `sector`/`marketcap`. No outcome and no
    `d_iv_spread` yet (both need the panel, added by `run()`). `hot`, `screener` and
    `join_short_side_fn` are injectable so tests never touch the mart, the screener spine or the
    short-interest table."""
    hot = _load_hot_chain_day(d) if hot is None else hot
    rows = [row for ticker, grp in hot.groupby("underlying_symbol", sort=False)
            if (row := _ticker_factor_row(ticker, grp)) is not None]
    factors = pd.DataFrame(rows)
    if factors.empty:
        return factors.assign(formation_date=pd.Series(dtype="object"))

    if screener is None:
        feat = pd.read_parquet(FEATURES_FILE)
        screener = feat[feat["date"] == d]
    keep = ["ticker", "marketcap", "log_mcap", "sector", "total_volume", "avg30_volume",
            "call_volume", "put_volume"]
    merged = factors.merge(screener[keep], on="ticker", how="inner")
    merged = merged[merged["marketcap"] >= UNIVERSE_MCAP_MIN].reset_index(drop=True)
    if merged.empty:
        return merged.assign(formation_date=pd.Series(dtype="object"))

    ratio, source = zip(*merged.apply(
        lambda r: XF.os_ratio(r["call_volume"], r["put_volume"], r["total_volume"], r["avg30_volume"]), axis=1))
    merged["os_ratio"], merged["os_source"] = ratio, source

    spine = pd.DataFrame({"ticker": merged["ticker"], "date": d})
    side = join_short_side_fn(spine)
    merged["short_interest"] = side["short_interest"].to_numpy()
    merged["days_to_cover"] = side["days_to_cover"].to_numpy()
    merged["formation_date"] = d
    return merged


def _attach_outcome(panel: pd.DataFrame) -> pd.DataFrame:
    ret = pd.read_parquet(RETURNS_FILE, columns=["ticker", "date", "horizon", "resolved", "excess"])
    ret = ret[(ret["horizon"] == OUTCOME_HORIZON) & ret["resolved"]]
    ret = ret.rename(columns={"date": "formation_date", "excess": "next_week_excess"})
    ret["formation_date"] = pd.to_datetime(ret["formation_date"]).dt.date
    return panel.merge(ret[["ticker", "formation_date", "next_week_excess"]],
                        on=["ticker", "formation_date"], how="left")


def _attach_delta_iv_spread(panel: pd.DataFrame, formations: list[date]) -> pd.DataFrame:
    """`d_iv_spread`: this week's `iv_spread` minus the immediately preceding formation's, only
    when that formation is within `DELTA_MAX_GAP_DAYS` calendar days (a true consecutive week)."""
    order = {f: i for i, f in enumerate(formations)}
    by_ticker = panel.set_index(["ticker", "formation_date"])["iv_spread"]
    d_spread, gap_days = [], []
    for _, r in panel.iterrows():
        idx = order[r["formation_date"]]
        if idx == 0:
            d_spread.append(np.nan); gap_days.append(np.nan)
            continue
        prev_date = formations[idx - 1]
        gap = (r["formation_date"] - prev_date).days
        gap_days.append(gap)
        if gap > DELTA_MAX_GAP_DAYS or (r["ticker"], prev_date) not in by_ticker.index:
            d_spread.append(np.nan)
            continue
        prev_val = by_ticker.loc[(r["ticker"], prev_date)]
        d_spread.append(r["iv_spread"] - prev_val if pd.notna(prev_val) and pd.notna(r["iv_spread"]) else np.nan)
    return panel.assign(d_iv_spread=d_spread, d_iv_spread_gap_days=gap_days)


def build_panel(formations: list[date] | None = None) -> pd.DataFrame:
    """The full ticker x formation panel across every formation Friday, with outcomes and
    `d_iv_spread` attached."""
    formations = formation_fridays() if formations is None else formations
    weeks = [build_week_factors(d) for d in formations]
    weeks = [w for w in weeks if not w.empty]
    if not weeks:
        return pd.DataFrame()
    panel = pd.concat(weeks, ignore_index=True)
    panel = _attach_outcome(panel)
    panel = _attach_delta_iv_spread(panel, formations)
    return panel


def build_week_factors_with_delta(d: date, formations: list[date] | None = None) -> pd.DataFrame:
    """`build_week_factors(d)` plus `d_iv_spread`, for a live/dry-run caller that only wants one
    week (`scripts/xs_rows.py`) rather than the whole panel. Reuses `_attach_delta_iv_spread`
    against the immediately preceding formation only."""
    all_formations = formation_fridays() if formations is None else formations
    if d not in all_formations:
        raise ValueError(f"{d} is not a formation Friday (no daily_contract partition, or its "
                          f"horizon-{OUTCOME_HORIZON} outcome is not resolved yet)")
    idx = all_formations.index(d)
    week = build_week_factors(d)
    if week.empty or idx == 0:
        return week.assign(d_iv_spread=np.nan, d_iv_spread_gap_days=np.nan) if len(week) else week
    prev_date = all_formations[idx - 1]
    two_weeks = pd.concat([build_week_factors(prev_date), week], ignore_index=True)
    two_weeks = _attach_delta_iv_spread(two_weeks, [prev_date, d])
    return two_weeks[two_weeks["formation_date"] == d].reset_index(drop=True)


# ------------------------------------------------------------------------------- factor testing


def factor_weekly_stats(panel: pd.DataFrame, factor_col: str, variant: str) -> pd.DataFrame:
    """Per-formation IC and decile spread for one (factor, raw/residual) test, indexed in
    formation-date order (shared by `run_factor_tests` and `power_for_factor` so the residual pass
    is computed once)."""
    outcome = "next_week_excess"
    if variant == "raw":
        work = panel
    else:
        resids = [XS.residualize_week(g, factor_col, CONTROL_COLS)
                  for _, g in panel.groupby("formation_date", sort=True)]
        work = panel.assign(**{factor_col: pd.concat(resids).reindex(panel.index)})
    return XS.per_week_stats(work, factor_col, outcome, "formation_date")


def _factor_test(panel: pd.DataFrame, factor_col: str, variant: str) -> dict:
    weekly = factor_weekly_stats(panel, factor_col, variant)
    summary = XS.summarize_ic(weekly.set_index("formation_date")["ic"])
    summary.update({
        "factor": factor_col, "variant": variant,
        "mean_decile_spread": float(weekly["decile_spread"].mean(skipna=True)),
        "median_universe_n": float(weekly["n_ic"].median()) if len(weekly) else float("nan"),
    })
    return summary


def run_factor_tests(panel: pd.DataFrame) -> pd.DataFrame:
    """The 8 pre-registered tests (4 factors x raw/residual), with BH q-values across all 8."""
    tests = [_factor_test(panel, f, v) for f in FACTOR_COLS for v in ("raw", "residual")]
    out = pd.DataFrame(tests)
    out["bh_q"] = XS.bh_qvalues(out["nw_p"].fillna(1.0))
    return out


# ------------------------------------------------------------------------------- power


def power_for_factor(panel: pd.DataFrame, factor_col: str, variant: str, mean_ic: float,
                      start: date, units_per_week: float = 1.0) -> dict:
    """Formations needed to detect the observed mean |IC| at 80% power (`engine.improve.power`),
    treating each formation's IC as the unit; and the projected calendar date at
    `units_per_week` formations/week."""
    from engine.improve import power as PW
    weekly = factor_weekly_stats(panel, factor_col, variant)
    x = weekly.set_index("formation_date")["ic"].dropna()
    min_effect = max(abs(float(mean_ic)), POWER_MIN_EFFECT_FLOOR)
    if len(x) < 2 or x.std(ddof=1) == 0:
        return {"factor": factor_col, "variant": variant, "n_required": None,
                "adjudicate_on": None, "reason": "insufficient dispersion in the observed IC series"}
    plan = PW.plan(min_effect, x, XS.NW_LAG, start, units_per_week)
    plan.update({"factor": factor_col, "variant": variant})
    return plan


# ------------------------------------------------------------------------------- CBOE data-quality check


def cboe_vs_hot_chains_skew(symbols: tuple[str, ...] = ("SPY", "QQQ")) -> dict:
    """For every symbol with a stored CBOE chain, the put-skew (`put25_iv - atm_call_iv`, this
    module's own definition, reapplied to the CBOE chain via `xs_factors.match_iv_at_delta`)
    compared against the hot-chains-based `put_skew` computed on the same date, as a data-quality
    check only (RESEARCH/47 §2 G4 task spec) -- not a factor, and not enough points (one date, up
    to `len(symbols)` names) for a meaningful Pearson correlation."""
    rows = []
    cboe_dates = sorted(_cboe_dates_for(symbols))
    for symbol, d in cboe_dates:
        chain = CC.load_chain(symbol, d)
        expiry_candidates = chain[["expiry"]].drop_duplicates()
        expiry_candidates["dte_cal"] = (pd.to_datetime(expiry_candidates["expiry"]) - pd.Timestamp(d)).dt.days
        near = XF.nearest_expiry(expiry_candidates)
        at_expiry = chain[chain["expiry"] == near]
        calls = XF.clean_deltas(at_expiry[at_expiry["right"] == "C"][["delta", "iv"]], sign=+1)
        puts = XF.clean_deltas(at_expiry[at_expiry["right"] == "P"][["delta", "iv"]], sign=-1)
        atm_call = XF.match_iv_at_delta(calls, XF.TARGET_CALL_DELTA)
        put_25d = XF.match_iv_at_delta(puts, XF.TARGET_PUT_DELTA_25D)
        cboe_skew = XF.put_skew(put_25d, atm_call)
        near_gap = int((pd.Timestamp(near) - pd.Timestamp(d)).days) if near is not None else None

        hot = _load_hot_chain_day(d)
        hot_ticker = hot[hot["underlying_symbol"] == symbol]
        hot_row = _ticker_factor_row(symbol, hot_ticker) if len(hot_ticker) else None
        hot_skew = hot_row["put_skew"] if hot_row else None
        rows.append({"symbol": symbol, "date": d.isoformat(), "cboe_put_skew": cboe_skew,
                     "hot_chains_put_skew": hot_skew, "near_expiry_cal_days": near_gap})
    out = pd.DataFrame(rows)
    valid = out.dropna(subset=["cboe_put_skew", "hot_chains_put_skew"])
    corr = float(np.corrcoef(valid["cboe_put_skew"], valid["hot_chains_put_skew"])[0, 1]) \
        if len(valid) >= 2 and valid["cboe_put_skew"].nunique() > 1 else float("nan")
    return {"rows": out.to_dict(orient="records"), "n": int(len(valid)), "pearson_r": corr,
            "note": "n is the count of (symbol, date) pairs with both sides computed; with only "
                    "SPY/QQQ on one stored date this is not a meaningful correlation sample -- read "
                    "the paired values, not r."}


def _cboe_dates_for(symbols: tuple[str, ...]) -> list[tuple[str, date]]:
    """`(symbol, date)` pairs actually stored under `data/mart/cboe_chain/symbol=<SYM>/date=<D>`
    (a two-level partition, so `engine.mart.store.available_dates` -- which expects `date=<D>`
    directly under the table dir -- does not see it)."""
    import glob
    import re
    out = []
    date_re = re.compile(r"date=(\d{4}-\d{2}-\d{2})")
    for symbol in symbols:
        pattern = os.path.join(config.MART, "cboe_chain", f"symbol={symbol}", "date=*", "part.parquet")
        for path in glob.glob(pattern):
            m = date_re.search(path)
            if m:
                out.append((symbol, date.fromisoformat(m.group(1))))
    return out


# ------------------------------------------------------------------------------- top level


def universe_counts(panel: pd.DataFrame) -> dict:
    """Universe size per formation week: min/median/max ticker count."""
    if panel is None or panel.empty:
        return {"min": None, "median": None, "max": None, "n_weeks": 0}
    counts = panel.groupby("formation_date").size()
    return {"min": int(counts.min()), "median": float(counts.median()), "max": int(counts.max()),
            "n_weeks": int(len(counts)), "by_week": {str(k): int(v) for k, v in counts.items()}}


def run(start_for_power: date | None = None) -> tuple[pd.DataFrame, dict]:
    """The full G4/G5 pipeline: panel, the 8-test table (BH-corrected), power/projected-date for
    each test, universe counts and the CBOE-vs-hot-chains skew check. Returns `(panel, results)`;
    `scripts/cross_section.py` writes `panel` to `g4_factors.parquet` and `results` to
    `g4_results.json`."""
    formations = formation_fridays()
    panel = build_panel(formations)
    tests = run_factor_tests(panel) if not panel.empty else pd.DataFrame()
    start = start_for_power or (formations[-1] if formations else date.today())
    power = [power_for_factor(panel, row["factor"], row["variant"], row["mean_ic"], start)
             for _, row in tests.iterrows()] if len(tests) else []
    results = {
        "formations": [d.isoformat() for d in formations],
        "n_formations": len(formations),
        "universe": universe_counts(panel),
        "tests": tests.to_dict(orient="records"),
        "power": power,
        "cboe_vs_hot_chains_skew": cboe_vs_hot_chains_skew(),
        "bh_fdr": BH_FDR,
        "control_cols": CONTROL_COLS,
        "factor_cols": FACTOR_COLS,
    }
    return panel, results
