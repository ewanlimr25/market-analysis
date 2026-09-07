"""Tier-1 ATM pair, C-VOL's `has_tier1_atm_pair` input (`DESIGN/110-watch-basket.md` §2, "S-C
funnel" evidence). Reuses S-C's own expiry and ATM-pair rules verbatim
(`findings/market-analysis/DESIGN/90-sc-spec.md` F7, F8) rather than inventing a new one:

  F7 expiry: the listed expiry with calendar DTE in [21, 35] nearest to `t + 28`.
  F8 ATM pair: a call and a put at the strike nearest `underlying_last` with
      `|K/S - 1| <= 2.5%`, each with `size_late >= 20` (tier 1).

Computed per session from that day's `daily_contract` partition -- one DuckDB query, no Python
loop over contracts. A ticker absent from the query's output either had no row in the [21, 35] DTE
window that day (a determined `False`, filled in by the caller against the universe frame) or was
not in `daily_contract` at all that day (excluded from the universe upstream, so moot here).
"""
from __future__ import annotations

import os
from datetime import date

import duckdb
import pandas as pd

from engine.mart import store

TABLE = "daily_contract"
DTE_CAL_MIN, DTE_CAL_MAX = 21, 35     # S-C F7
TARGET_DTE_CAL = 28                   # S-C F7, "nearest to t + 28"
ATM_BAND = 0.025                      # S-C F8, |K/S - 1| <= 2.5%
MIN_SIZE_LATE = 20                    # S-C F8, tier-1 entry

_QUERY = """
WITH c AS (
  SELECT underlying_symbol, option_type, strike, expiry, dte_cal, size_late, underlying_last
  FROM read_parquet(?)
  WHERE dte_cal BETWEEN {dte_lo} AND {dte_hi} AND underlying_last > 0
),
expiry_pick AS (
  SELECT underlying_symbol, expiry,
         ROW_NUMBER() OVER (PARTITION BY underlying_symbol
                             ORDER BY ABS(dte_cal - {target}), expiry) AS rn
  FROM (SELECT DISTINCT underlying_symbol, expiry, dte_cal FROM c)
),
chosen AS (SELECT underlying_symbol, expiry FROM expiry_pick WHERE rn = 1),
cand AS (SELECT c.* FROM c JOIN chosen USING (underlying_symbol, expiry)),
strike_pick AS (
  SELECT underlying_symbol, strike, underlying_last,
         ROW_NUMBER() OVER (PARTITION BY underlying_symbol
                             ORDER BY ABS(strike / underlying_last - 1)) AS rn
  FROM (SELECT DISTINCT underlying_symbol, strike, underlying_last FROM cand)
),
nearest AS (
  SELECT underlying_symbol, strike FROM strike_pick
  WHERE rn = 1 AND ABS(strike / underlying_last - 1) <= {band}
)
SELECT cand.underlying_symbol AS ticker,
       (max(CASE WHEN option_type = 'call' AND size_late >= {min_size} THEN 1 ELSE 0 END) = 1
        AND max(CASE WHEN option_type = 'put' AND size_late >= {min_size} THEN 1 ELSE 0 END) = 1
       ) AS has_tier1_atm_pair
FROM cand JOIN nearest USING (underlying_symbol, strike)
GROUP BY 1
"""


def tier1_atm_flags_for_partition(partition_path: str, con: duckdb.DuckDBPyConnection | None = None) -> pd.DataFrame:
    """`(ticker, has_tier1_atm_pair)` for one `daily_contract` partition file. A ticker not
    returned had no expiry in the [21, 35] DTE window that day -- the caller fills that in as
    `False` against its own universe frame, not this function (which only speaks about tickers it
    could actually examine)."""
    if not partition_path or not os.path.exists(partition_path):
        return pd.DataFrame(columns=["ticker", "has_tier1_atm_pair"])
    con = con or duckdb.connect()
    q = _QUERY.format(dte_lo=DTE_CAL_MIN, dte_hi=DTE_CAL_MAX, target=TARGET_DTE_CAL,
                       band=ATM_BAND, min_size=MIN_SIZE_LATE)
    return con.execute(q, [partition_path]).df()


def build_tier1_flags(dates: list[date]) -> pd.DataFrame:
    """`(ticker, date, has_tier1_atm_pair)` across every date in `dates` that has a
    `daily_contract` partition. Missing dates are silently skipped (the universe builder already
    restricts to dates with coverage)."""
    con = duckdb.connect()
    frames = []
    for d in dates:
        path = store.partition_path(TABLE, d)
        flags = tier1_atm_flags_for_partition(path, con)
        if not flags.empty:
            frames.append(flags.assign(date=d))
    if not frames:
        return pd.DataFrame(columns=["ticker", "date", "has_tier1_atm_pair"])
    return pd.concat(frames, ignore_index=True)
