"""G6 data layer: read-only access to the raw OI-changes and screener panels in
`~/Documents/Stocks` (never written to), and the orchestration that turns one expiry week's
loaded data into `g6_pins` rows.

`build_rows_for_week` is pure given already-loaded frames (tested on synthetic data in
`tests/test_expiry_pinning_data.py`); `load_oi_snapshot`, `screener_panel` and `build_pin_rows`
are the I/O around it.
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import date, timedelta

import duckdb
import pandas as pd

from engine import config
from engine.research.expiry_pinning import (ExpiryWeek, MIN_OI_CONTRACTS, build_expiry_calendar,
                                            combined_oi_by_strike, distance_frac, max_pain_strike,
                                            nearest_strike_distance, nearest_strike_to_close,
                                            parse_oi_snapshot, passes_universe, pin_strike,
                                            second_largest_oi_strike)

OI_DIR = "OI changes"
OI_FILE = "chain-oi-changes-{d}.parquet"
SCREENER_LOOKBACK_DAYS = 10   # buffer before `start` so the first week's prior_friday resolves

PIN_COLUMNS = (
    "underlying", "friday", "expiry", "is_monthly", "day_minus_1", "prior_friday",
    "total_oi", "marketcap", "issue_type", "close_day_minus_1", "close_expiry", "close_prior_friday",
    "pin_strike", "max_pain_strike", "placebo_second_strike", "placebo_nearest_strike",
    "dist_pin_expiry", "dist_pin_prior_friday", "dist_maxpain_expiry", "dist_maxpain_prior_friday",
    "dist_placebo_second_expiry", "dist_placebo_nearest_expiry",
    "nearest_any_strike_dist_expiry", "nearest_any_strike_dist_prior_friday", "n_strikes",
)


@dataclass(frozen=True)
class ScreenerRow:
    issue_type: str | None
    marketcap: float | None
    close: float | None


ScreenerIndex = dict[tuple[str, date], ScreenerRow]


def _quote(path: str) -> str:
    return "'" + path.replace("'", "''") + "'"


# ----------------------------------------------------------------------------- I/O


def oi_snapshot_path(d: date) -> str:
    return os.path.join(config.STOCKS, OI_DIR, OI_FILE.format(d=d.isoformat()))


def load_oi_snapshot(d: date) -> pd.DataFrame:
    """Raw (option_symbol, underlying_symbol, strike, curr_oi) rows from the OI-changes file
    dated `d`. `curr_oi` on the file dated D is OI effective at the start of D, i.e. as of the
    close of the trading day before D (RESEARCH/20 §5.1; cross-checked bit-for-bit against
    `daily_contract.open_interest` for the same date during this build). Empty frame if the
    file is missing (the panel's 19-session hole, RESEARCH/20 §1.3, or a date past the panel)."""
    path = oi_snapshot_path(d)
    if not os.path.exists(path):
        return pd.DataFrame(columns=["option_symbol", "underlying_symbol", "strike", "curr_oi"])
    con = duckdb.connect()
    return con.execute(
        f"SELECT option_symbol, underlying_symbol, strike, curr_oi "
        f"FROM read_parquet({_quote(path)})").df()


def screener_panel(start: date, end: date) -> pd.DataFrame:
    """One row per (ticker, date) with issue_type, marketcap, close, for date in [start, end]."""
    pattern = os.path.join(config.STOCKS, config.SCREENER_GLOB)
    con = duckdb.connect()
    df = con.execute(f"""
        SELECT date, ticker, any_value(issue_type) AS issue_type,
               any_value(marketcap) AS marketcap, any_value(close) AS close
        FROM read_parquet({_quote(pattern)})
        WHERE date BETWEEN DATE '{start}' AND DATE '{end}'
        GROUP BY date, ticker""").df()
    df["date"] = pd.to_datetime(df["date"]).dt.date
    return df


def screener_index(panel: pd.DataFrame) -> ScreenerIndex:
    return {(r.ticker, r.date): ScreenerRow(r.issue_type, r.marketcap, r.close)
            for r in panel.itertuples(index=False)}


# ----------------------------------------------------------------------------- pure row-building


def build_rows_for_week(week: ExpiryWeek, oi_snapshot_raw: pd.DataFrame,
                        screener: ScreenerIndex) -> list[dict]:
    """One `g6_pins` row per qualifying underlying for this expiry week, given the already-loaded
    (unparsed) OI-snapshot for `week.expiry` and a screener index. Pure: no file access."""
    parsed = parse_oi_snapshot(oi_snapshot_raw)
    this_expiry = parsed[parsed["expiry"] == week.expiry]
    if this_expiry.empty:
        return []
    totals = this_expiry.groupby("underlying_symbol")["curr_oi"].sum()
    qualifying = totals[totals >= MIN_OI_CONTRACTS].index
    rows = []
    for name in qualifying:
        scr_dm1 = screener.get((name, week.day_minus_1))
        if scr_dm1 is None:
            continue
        total_oi = float(totals[name])
        if not passes_universe(scr_dm1.issue_type, scr_dm1.marketcap, total_oi):
            continue
        scr_exp = screener.get((name, week.expiry))
        if scr_exp is None or scr_exp.close is None:
            continue
        row = _build_row(week, name, this_expiry, total_oi, scr_dm1, scr_exp,
                         screener.get((name, week.prior_friday)))
        rows.append(row)
    return rows


def _build_row(week: ExpiryWeek, name: str, this_expiry: pd.DataFrame, total_oi: float,
               scr_dm1: ScreenerRow, scr_exp: ScreenerRow, scr_pf: ScreenerRow | None) -> dict:
    name_oi = this_expiry[this_expiry["underlying_symbol"] == name]
    strike_oi = combined_oi_by_strike(name_oi[["option_type", "strike", "curr_oi"]])
    ref_close = scr_dm1.close
    close_exp = scr_exp.close
    close_pf = scr_pf.close if scr_pf is not None else None
    pin = pin_strike(strike_oi, ref_close)
    maxpain = max_pain_strike(name_oi, ref_close)
    second = second_largest_oi_strike(strike_oi, pin, ref_close)
    nearest = nearest_strike_to_close(strike_oi["strike"], ref_close)
    strikes = strike_oi["strike"]
    return {
        "underlying": name, "friday": week.friday, "expiry": week.expiry,
        "is_monthly": week.is_monthly, "day_minus_1": week.day_minus_1, "prior_friday": week.prior_friday,
        "total_oi": total_oi, "marketcap": scr_dm1.marketcap, "issue_type": scr_dm1.issue_type,
        "close_day_minus_1": ref_close, "close_expiry": close_exp, "close_prior_friday": close_pf,
        "pin_strike": pin, "max_pain_strike": maxpain,
        "placebo_second_strike": second, "placebo_nearest_strike": nearest,
        "dist_pin_expiry": distance_frac(close_exp, pin) if pin is not None else float("nan"),
        "dist_pin_prior_friday": (distance_frac(close_pf, pin)
                                  if pin is not None and close_pf is not None else float("nan")),
        "dist_maxpain_expiry": distance_frac(close_exp, maxpain) if maxpain is not None else float("nan"),
        "dist_maxpain_prior_friday": (distance_frac(close_pf, maxpain)
                                      if maxpain is not None and close_pf is not None else float("nan")),
        "dist_placebo_second_expiry": distance_frac(close_exp, second) if second is not None else float("nan"),
        "dist_placebo_nearest_expiry": distance_frac(close_exp, nearest) if nearest is not None else float("nan"),
        "nearest_any_strike_dist_expiry": nearest_strike_distance(strikes, close_exp),
        "nearest_any_strike_dist_prior_friday": (nearest_strike_distance(strikes, close_pf)
                                                 if close_pf is not None else float("nan")),
        "n_strikes": int(len(strike_oi)),
    }


# ----------------------------------------------------------------------------- driver


def build_pin_rows(start: date, end: date) -> tuple[pd.DataFrame, list[date]]:
    """Every `g6_pins` row for Friday expiries in [start, end]. Returns (rows, excluded_expiries)
    where the latter lists expiry dates with no usable OI snapshot (the panel gap)."""
    weeks = build_expiry_calendar(start, end)
    screener = screener_index(screener_panel(start - timedelta(days=SCREENER_LOOKBACK_DAYS), end))
    rows: list[dict] = []
    excluded: list[date] = []
    for week in weeks:
        oi_raw = load_oi_snapshot(week.expiry)
        if oi_raw.empty:
            excluded.append(week.expiry)     # the panel gap, or past the panel edge
            continue
        rows.extend(build_rows_for_week(week, oi_raw, screener))
    pins = pd.DataFrame(rows, columns=list(PIN_COLUMNS))
    return pins, excluded
