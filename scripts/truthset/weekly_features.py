#!/usr/bin/env python3
"""Weekly candle resample + technical/structure features for /weekly-review.

Resamples daily OHLC -> weekly (Mon-Fri) bars per ticker and computes price-action structure features:
candle anatomy (body/wick/close-position), week-vs-prior-week structure (inside/outside/HH/LL),
reversal-candle flags (hammer/hanging, shooting-star), weekly direction & follow-through.

IMPORTANT (honesty): these features are computed for DOCUMENTATION (the weekly market diary) and are
PRE-REGISTERED, NOT scored. On this panel there are only ~11 weeks — far too few to validate any weekly
candle/structure edge (the literature on candlestick patterns is weak-to-null on liquid names:
Marshall-Young-Rose 2006). The edge test is deferred to the extended (multi-year) panel. This script
produces the diary substrate + an illustrative table; it makes NO edge claim.

Output: data/weekly_features.parquet  + prints an illustrative SPY/QQQ/IWM weekly-structure table.
"""
import duckdb, os
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "..", "data")
PX = os.path.join(DATA, "prices.parquet")
OUT = os.path.join(DATA, "weekly_features.parquet")
con = duckdb.connect()

# weekly bars (ISO week): first open, max high, min low, last close, summed volume
con.execute(f"""CREATE TEMP TABLE wk AS
WITH d AS (SELECT ticker, date, open, high, low, close, volume,
             date_trunc('week', date) AS wk_start FROM read_parquet('{PX}'))
SELECT ticker, wk_start,
  arg_min(open, date) AS w_open, max(high) AS w_high, min(low) AS w_low,
  arg_max(close, date) AS w_close, sum(volume) AS w_vol, count(*) AS n_days
FROM d GROUP BY ticker, wk_start HAVING count(*) >= 3""")  # require a near-full week

# structure features + lag-to-prior-week
con.execute("""CREATE TEMP TABLE wf AS
SELECT *,
  (w_high - w_low) AS rng,
  abs(w_close - w_open) AS body,
  (w_high - greatest(w_open, w_close)) AS upper_wick,
  (least(w_open, w_close) - w_low) AS lower_wick,
  CASE WHEN w_high>w_low THEN (w_close - w_low)/(w_high - w_low) END AS close_pos,
  CASE WHEN w_high>w_low THEN abs(w_close-w_open)/(w_high-w_low) END AS body_frac,
  CASE WHEN w_close>=w_open THEN 1 ELSE -1 END AS dir,
  (w_close/w_open - 1) AS w_ret,
  lag(w_high) OVER w AS prev_high, lag(w_low) OVER w AS prev_low,
  lag(w_close) OVER w AS prev_close, lag(w_close>=w_open) OVER w AS prev_up
FROM wk WINDOW w AS (PARTITION BY ticker ORDER BY wk_start)""")

con.execute(f"""COPY (
SELECT *,
  (w_high>prev_high AND w_low<prev_low) AS outside_week,
  (w_high<prev_high AND w_low>prev_low) AS inside_week,
  (w_high>prev_high) AS higher_high,
  (w_low<prev_low) AS lower_low,
  -- reversal candles (generic; direction-agnostic flags, NOT scored):
  (lower_wick >= 2*body AND close_pos >= 0.6) AS hammer_or_hanging,
  (upper_wick >= 2*body AND close_pos <= 0.4) AS star_or_inverted,
  -- did this week continue the prior week's direction?
  ((w_close>=w_open) = prev_up) AS follow_through
FROM wf) TO '{OUT}' (FORMAT PARQUET)""")

n = con.execute(f"SELECT count(*), count(distinct ticker), count(distinct wk_start) FROM read_parquet('{OUT}')").fetchone()
print(f"weekly_features.parquet: {n[0]} rows, {n[1]} tickers, {n[2]} weeks")
print("\nILLUSTRATIVE ONLY (n=~11 weeks — NOT an edge claim) — SPY/QQQ/IWM weekly structure:")
print(f"{'wk_start':<12}{'sym':<5}{'close':>9}{'w_ret':>8}{'close_pos':>10}{'body_frac':>10}  flags")
for sym in ('SPY','QQQ','IWM'):
    for r in con.execute(f"""SELECT wk_start, w_close, w_ret, close_pos, body_frac, dir,
              inside_week, outside_week, hammer_or_hanging, star_or_inverted, follow_through
              FROM read_parquet('{OUT}') WHERE ticker='{sym}' ORDER BY wk_start""").fetchall():
        flags=[]
        if r[6]: flags.append("inside")
        if r[7]: flags.append("outside")
        if r[8]: flags.append("hammer/hanging")
        if r[9]: flags.append("star/inverted")
        if r[10] is False: flags.append("reversal-wk")
        cp = f"{r[3]:.2f}" if r[3] is not None else "  na"
        bf = f"{r[4]:.2f}" if r[4] is not None else "  na"
        print(f"{str(r[0]):<12}{sym:<5}{r[1]:>9.2f}{r[2]*100:>7.1f}%{cp:>10}{bf:>10}  {','.join(flags)}")
    print()
