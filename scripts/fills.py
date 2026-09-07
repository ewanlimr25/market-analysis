#!/usr/bin/env python3
"""G1 step 1 (RESEARCH/47 §2 G1): fill-quality classification over the whole panel.

One DuckDB pass over 103 days of All Options prints (~10.9M rows/day), single-leg lane only
(`engine.improve.fills.SINGLE_LEG_CODES`), classified against the print's own NBBO. Writes:
  data/backtest/g1_fills.parquet      long-format aggregate, `cut` in {bucket, window}
  data/backtest/g1_fills_summary.md   the share tables

`cut='bucket'` rows are (tier30, bucket30, sweep, dte_bucket, class) -> volume/premium: the
general fill-quality picture (RESEARCH/47 item 1). `cut='window'` rows are (tier, window, class)
-> volume/premium for each of `fills.CANDIDATE_WINDOWS` (early, late, b1, b2): the crosswalk
`engine/improve/g1_remark.py` re-marks the frozen S-A rows against.

    python3 scripts/fills.py [--out data/backtest] [--stocks ~/Documents/Stocks]
"""
from __future__ import annotations

import argparse
import os
import sys
import time

import duckdb
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from engine.config import ALL_OPTIONS_FILE, DATA, STOCKS, TIER1_MIN_SIZE   # noqa: E402
from engine.improve import fills as G                                      # noqa: E402

OUT_DIR = os.path.join(DATA, "backtest")
CUT_BUCKET, CUT_WINDOW = "bucket", "window"


def _window_block(window: str) -> str:
    return f"""SELECT '{CUT_WINDOW}' AS cut, tier_{window} AS tier, '{window}' AS dim2,
       NULL AS sweep, NULL AS dte_bucket, class, sum(size) AS volume, sum(premium) AS premium, count(*) AS n
FROM t WHERE is_{window} GROUP BY 1, 2, 3, 4, 5, 6"""


def build_sql(glob_path: str) -> str:
    is_flags = ",\n         ".join(f"{G.in_window_sql('et::TIME', w)} AS is_{w}" for w in G.CANDIDATE_WINDOWS)
    tier_flags = ",\n    ".join(
        f"CASE WHEN SUM(size) FILTER (WHERE is_{w}) OVER (PARTITION BY option_chain_id, d) "
        f">= {TIER1_MIN_SIZE} THEN 1 ELSE 2 END AS tier_{w}" for w in G.CANDIDATE_WINDOWS)
    window_union = "\nUNION ALL\n".join(_window_block(w) for w in G.CANDIDATE_WINDOWS)
    return f"""
WITH base AS (
  SELECT option_chain_id,
         (executed_at AT TIME ZONE 'America/New_York')::TIMESTAMP AS et,
         side, price, nbbo_bid AS bid, nbbo_ask AS ask, expiry, report_flags, size, premium
  FROM read_parquet({glob_path!r})
  WHERE NOT canceled AND size > 0 AND price > 0
    AND {G.single_leg_codes_sql()}
    AND side != '{G.SIDE_EXCLUDED}'
    AND nbbo_bid > 0 AND nbbo_ask >= nbbo_bid
    AND {G.SESSION_WHERE}
), p AS (
  SELECT option_chain_id, et::DATE AS d, size, premium,
         CAST(FLOOR(date_diff('minute', TIME '{G.SESSION_START}', et::TIME) / {G.BUCKET_MINUTES}) AS INTEGER) AS bucket30_idx,
         {G.dte_bucket_sql("date_diff('day', et::DATE, expiry)")} AS dte_bucket,
         (report_flags LIKE '%intermarket_sweep%') AS sweep,
         {G.classify_fill_sql("side", "price", "bid", "ask")} AS class,
         {is_flags}
  FROM base
), t AS (
  SELECT *,
    CASE WHEN SUM(size) OVER (PARTITION BY option_chain_id, d, bucket30_idx) >= {TIER1_MIN_SIZE}
         THEN 1 ELSE 2 END AS tier30,
    {tier_flags}
  FROM p
)
SELECT '{CUT_BUCKET}' AS cut, tier30 AS tier, CAST(bucket30_idx AS VARCHAR) AS dim2,
       sweep, dte_bucket, class, sum(size) AS volume, sum(premium) AS premium, count(*) AS n
FROM t GROUP BY 1, 2, 3, 4, 5, 6
UNION ALL
{window_union}
"""


def run(glob_path: str, threads: int = 8) -> pd.DataFrame:
    con = duckdb.connect()
    con.execute(f"PRAGMA threads={threads}")
    df = con.execute(build_sql(glob_path)).df()
    is_bucket = df["cut"] == CUT_BUCKET
    df["dim2"] = df["dim2"].mask(is_bucket, df.loc[is_bucket, "dim2"].astype(int).map(G.bucket30_label))
    return df.sort_values(["cut", "tier", "dim2", "sweep", "dte_bucket", "class"]).reset_index(drop=True)


def _share_table(df: pd.DataFrame, cut: str, group_cols: list[str]) -> pd.DataFrame:
    sub = df[df["cut"] == cut]
    rows = []
    for key, g in sub.groupby(group_cols, dropna=False):
        key = key if isinstance(key, tuple) else (key,)
        r = G.mid_or_better_share(g.to_dict("records"))
        rows.append({**dict(zip(group_cols, key)), "volume": r.volume, "premium": r.premium,
                    "mid_or_better_volume_share": r.volume_share, "mid_or_better_premium_share": r.premium_share})
    return pd.DataFrame(rows)


def _fmt(t: pd.DataFrame, cols: list[str]) -> str:
    t = t.copy()
    t["mid_or_better_volume_share"] = (t["mid_or_better_volume_share"] * 100).round(1)
    t["mid_or_better_premium_share"] = (t["mid_or_better_premium_share"] * 100).round(1)
    header = "| " + " | ".join(cols + ["volume", "premium", "mid+ volume %", "mid+ premium %"]) + " |"
    sep = "|" + "---|" * (len(cols) + 4)
    lines = [header, sep]
    for _, r in t.iterrows():
        vals = [str(r[c]) for c in cols] + [f"{r.volume:,.0f}", f"{r.premium:,.0f}",
                f"{r.mid_or_better_volume_share}", f"{r.mid_or_better_premium_share}"]
        lines.append("| " + " | ".join(vals) + " |")
    return "\n".join(lines)


def write_summary(df: pd.DataFrame, path: str, n_days: int) -> None:
    by_tier_window = _share_table(df, CUT_WINDOW, ["tier", "dim2"])
    by_tier_bucket = _share_table(df, CUT_BUCKET, ["tier", "dim2"])
    by_sweep = _share_table(df, CUT_BUCKET, ["tier", "sweep"])
    by_dte = _share_table(df, CUT_BUCKET, ["tier", "dte_bucket"])
    total_volume = df.loc[df.cut == CUT_BUCKET, "volume"].sum()
    total_premium = df.loc[df.cut == CUT_BUCKET, "premium"].sum()

    text = f"""# G1 fill-quality: single-leg prints against the panel's own NBBO

{n_days} trading days, single-leg lane (`{', '.join(G.SINGLE_LEG_CODES)}`), `no_side` excluded, valid
NBBO required (`nbbo_bid > 0 AND nbbo_ask >= nbbo_bid`). Total volume {total_volume:,.0f} contracts,
premium ${total_premium:,.0f}. Class = position in the print's own NBBO, signed by aggressor side
(`engine/improve/fills.py::classify_fill`); tolerance {G.TOL_FRAC:.0%} of the half-spread.

## By tier and marking window (the re-marking crosswalk, G1 item 2)

`early`/`late` are the windows the marking engine already uses; `b1` = 10:30-11:30, `b2` = 14:30-15:30
(the two candidate exit windows for treatment b). Windows overlap (`late` and `b2` share 15:00-15:30).

{_fmt(by_tier_window, ['tier', 'dim2'])}

## By tier and 30-minute ET bucket

{_fmt(by_tier_bucket, ['tier', 'dim2'])}

## By tier and sweep flag

{_fmt(by_sweep, ['tier', 'sweep'])}

## By tier and DTE bucket

{_fmt(by_dte, ['tier', 'dte_bucket'])}
"""
    with open(path, "w") as f:
        f.write(text)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=OUT_DIR)
    ap.add_argument("--stocks", default=STOCKS)
    args = ap.parse_args()

    t0 = time.time()
    glob_path = os.path.join(args.stocks, ALL_OPTIONS_FILE.format(d="*"))
    n_days = len([f for f in os.listdir(os.path.join(args.stocks, "All Options")) if f.endswith(".parquet")])
    df = run(glob_path)
    os.makedirs(args.out, exist_ok=True)
    df.to_parquet(os.path.join(args.out, "g1_fills.parquet"), index=False)
    write_summary(df, os.path.join(args.out, "g1_fills_summary.md"), n_days)
    print(f"g1_fills: {len(df)} aggregate rows, {n_days} days, {time.time() - t0:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
