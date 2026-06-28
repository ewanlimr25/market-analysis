#!/usr/bin/env python3
"""Unified per-(ticker,date) FEATURE TABLE across all 5 panel sources, for open-ended factor mining.

Spine = liquid screener universe (close>=5 AND close*avg30_volume>=50e6), one row per ticker-day.
LEFT JOIN per-ticker-day aggregates from dark pool / OI changes / hot chains / all options, plus
multi-day (trailing-5d, <=T) derivations and per-name realized vol (for VRP). Emits ~40 candidate factors
spanning the columns the Phase-2 fleet-mapped sweep never used.

Output: data/features.parquet
"""
import duckdb, glob, os
S=os.path.expanduser("~/Documents/Stocks")
D=os.path.expanduser("~/Development/market-analysis/data")
con=duckdb.connect()
def g(d,p): return sorted(glob.glob(f"{S}/{d}/{p}"))
SCR=g("Stock Screener","stock-screener-*.parquet"); DP=g("Dark pool","dp-eod-report-*.parquet")
OI=g("OI changes","chain-oi-changes-*.parquet"); HC=g("Hot Option Chains","hot-chains-*.parquet")
AO=g("All Options","bot-eod-report-*.parquet")

# ---- spine: screener-derived factors ----
con.execute(f"""CREATE TEMP TABLE spine AS
SELECT date, ticker, sector, marketcap, close, prev_close,
  put_call_ratio AS pcr, iv_rank, iv30d, iv30d_1d, iv30d_1w, iv30d_1m,
  implied_move_perc, volatility, net_call_premium, net_put_premium,
  call_open_interest AS call_oi, put_open_interest AS put_oi,
  total_volume, avg30_volume, week_52_high AS w52h, week_52_low AS w52l,
  bullish_premium, bearish_premium, call_volume, put_volume,
  -- derived
  CASE WHEN w52h>w52l THEN (close-week_52_low)/(week_52_high-week_52_low) END AS pct_52w_range,
  (iv30d - iv30d_1w) AS iv_mom_1w,
  (iv30d - iv30d_1m) AS iv_mom_1m,
  total_volume/nullif(avg30_volume,0) AS vol_accel,
  close/nullif(prev_close,0)-1 AS gap,
  (net_call_premium-net_put_premium)/nullif(marketcap,0) AS netprem_mcap,
  (net_call_premium-net_put_premium) AS netprem,
  call_open_interest/nullif(call_open_interest+put_open_interest,0) AS oi_call_share,
  ln(nullif(marketcap,0)) AS log_mcap,
  (bullish_premium-bearish_premium)/nullif(bullish_premium+bearish_premium,0) AS bull_bear_skew,
  call_volume/nullif(put_volume,0) AS cv_pv
FROM read_parquet({SCR!r})
WHERE close>=5 AND close*avg30_volume>=50e6""")

# ---- dark pool agg per ticker-day ----
con.execute(f"""CREATE TEMP TABLE dpagg AS
SELECT ticker, date,
  sum(premium) AS dp_prem,
  sum(CASE WHEN price>=(nbbo_bid+nbbo_ask)/2 THEN premium ELSE -premium END)/nullif(sum(premium),0) AS dp_buy_skew,
  greatest(sum(CASE WHEN price>=(nbbo_bid+nbbo_ask)/2 THEN premium ELSE 0 END),
           sum(CASE WHEN price<(nbbo_bid+nbbo_ask)/2 THEN premium ELSE 0 END))/nullif(sum(premium),0) AS dp_oneside,
  count(*) FILTER(WHERE size>=50000 OR premium>=2.8e6) AS dp_block_n,
  sum(volume) AS dp_vol
FROM read_parquet({DP!r}) WHERE canceled=false AND nbbo_bid>0 AND nbbo_ask>0
GROUP BY ticker, date""")

# ---- OI changes agg per ticker-day (call/put via OCC) ----
con.execute(f"""CREATE TEMP TABLE oiagg AS
WITH x AS (SELECT underlying_symbol AS ticker, curr_date AS date, oi_diff_plain, dte, avg_price,
            regexp_extract(option_symbol,'\\d{{6}}([CP])',1) AS cp, stock_price FROM read_parquet({OI!r}))
SELECT ticker, date,
  sum(CASE WHEN cp='C' AND oi_diff_plain>0 THEN oi_diff_plain ELSE 0 END) AS oi_call_build,
  sum(CASE WHEN cp='P' AND oi_diff_plain>0 THEN oi_diff_plain ELSE 0 END) AS oi_put_build,
  sum(CASE WHEN cp='C' THEN oi_diff_plain ELSE -oi_diff_plain END) AS oi_net_cp,
  sum(CASE WHEN dte>=180 AND oi_diff_plain>0 THEN oi_diff_plain*(CASE WHEN cp='C' THEN 1 ELSE -1 END) ELSE 0 END) AS leap_net_build
FROM x GROUP BY ticker, date""")

# ---- hot chains agg per ticker-day ----
con.execute(f"""CREATE TEMP TABLE hcagg AS
WITH x AS (SELECT regexp_replace(option_symbol,'[0-9].*$','') AS ticker, date,
            regexp_extract(option_symbol,'\\d{{6}}([CP])',1) AS cp,
            volume, ask_side_volume, bid_side_volume, sweep_volume, multileg_volume, floor_volume, premium FROM read_parquet({HC!r}))
SELECT ticker, date,
  sum((ask_side_volume-bid_side_volume)*(CASE WHEN cp='C' THEN 1 ELSE -1 END)) AS hc_smart_dir,
  sum(sweep_volume)/nullif(sum(volume),0) AS hc_sweep_share,
  sum(multileg_volume)/nullif(sum(volume),0) AS hc_ml_share,
  sum(floor_volume)/nullif(sum(volume),0) AS hc_floor_share
FROM x GROUP BY ticker, date""")

# ---- realized vol (20d) from prices, for per-name VRP ----
con.execute(f"""CREATE TEMP TABLE rv AS
WITH r AS (SELECT ticker, date, close/lag(close) OVER (PARTITION BY ticker ORDER BY date)-1 AS ret
           FROM read_parquet('{D}/prices.parquet'))
SELECT ticker, date, stddev_samp(ret) OVER (PARTITION BY ticker ORDER BY date ROWS BETWEEN 19 PRECEDING AND CURRENT ROW)*sqrt(252) AS rvol20
FROM r""")

# ---- assemble + multi-day trailing-5d derivations ----
con.execute(f"""CREATE TEMP TABLE feat AS
SELECT s.*,
  d.dp_prem, d.dp_buy_skew, d.dp_oneside, d.dp_block_n, d.dp_vol,
  o.oi_call_build, o.oi_put_build, o.oi_net_cp, o.leap_net_build,
  h.hc_smart_dir, h.hc_sweep_share, h.hc_ml_share, h.hc_floor_share,
  rv.rvol20,
  (s.iv30d/100.0 - rv.rvol20) AS vrp_name,
  d.dp_vol/nullif(s.total_volume,0) AS dp_vol_share
FROM spine s
LEFT JOIN dpagg d USING(ticker,date)
LEFT JOIN oiagg o USING(ticker,date)
LEFT JOIN hcagg h USING(ticker,date)
LEFT JOIN rv USING(ticker,date)""")

# trailing-5d (<=T) persistence/acceleration factors
con.execute("""CREATE TEMP TABLE featm AS
SELECT *,
  avg(dp_buy_skew) OVER w AS dp_buy_skew_5d,
  avg(netprem) OVER w AS netprem_5d,
  avg(oi_net_cp) OVER w AS oi_net_5d,
  (iv_rank - lag(iv_rank,5) OVER (PARTITION BY ticker ORDER BY date)) AS ivrank_chg_5d,
  avg(hc_smart_dir) OVER w AS hc_smart_5d
FROM feat
WINDOW w AS (PARTITION BY ticker ORDER BY date ROWS BETWEEN 4 PRECEDING AND CURRENT ROW)""")

con.execute(f"COPY (SELECT * FROM featm) TO '{D}/features.parquet' (FORMAT PARQUET)")
n=con.execute(f"SELECT count(*), count(distinct ticker), count(distinct date) FROM read_parquet('{D}/features.parquet')").fetchone()
cols=[c[0] for c in con.execute(f"DESCRIBE SELECT * FROM read_parquet('{D}/features.parquet')").fetchall()]
print("features.parquet rows / tickers / dates:", n)
print("n columns:", len(cols))
print("factor columns:", [c for c in cols if c not in ('date','ticker','sector')])
