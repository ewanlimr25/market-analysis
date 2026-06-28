#!/usr/bin/env python3
"""Forward-return + excess-vs-SPY + path-aware matrix (truth set core).

Long format, one row per (ticker, date, horizon):
  fwd_ret   = adjclose[T+h]/adjclose[T] - 1                 (total return)
  spy_ret   = SPY adjclose[T+h]/adjclose[T] - 1
  excess    = fwd_ret - spy_ret                              (EDGE, not beta)
  mfe_pct   = max(high) over (T+1 .. T+h) / close[T] - 1     (best excursion)
  mae_pct   = min(low)  over (T+1 .. T+h) / close[T] - 1     (worst excursion)
  atr14_pct = 0.5*ATR(14, true range) at T / close[T]        (=> R for the +/-1R path rule)
  long_R_win  / short_R_win  : approximate path-aware +/-1R win flags
  resolved  : forward bar exists (else INCONCLUSIVE / data_unavailable)

Horizons (trading days): 1,3,5,10,21,42,63  (~0DTE/next-sess, swing 3/10, weekly 5/10, LEAP 1mo/2mo/3mo).
Returns are on the real continuous trading calendar (Yahoo grid) so the panel's April export
gap does not corrupt forward windows. Look-ahead is the caller's job: only join signals on
date<=T to outcomes computed from date>T.
"""
import duckdb, os
HERE=os.path.dirname(os.path.abspath(__file__))
DATA=os.path.join(HERE,"..","..","data")
P=os.path.join(DATA,"prices.parquet")
OUT=os.path.join(DATA,"returns.parquet")
HORIZONS=[1,3,5,10,21,42,63]
con=duckdb.connect()

# base series with true-range ATR(14) and 0.5*ATR as R
con.execute(f"""CREATE TEMP TABLE px AS
SELECT ticker, date, open, high, low, close, adjclose, volume,
  lag(close) OVER w AS prev_close
FROM read_parquet('{P}')
WINDOW w AS (PARTITION BY ticker ORDER BY date);
""")
con.execute("""CREATE TEMP TABLE tr AS
SELECT *, greatest(high-low, abs(high-prev_close), abs(low-prev_close)) AS true_range
FROM px;""")
con.execute("""CREATE TEMP TABLE atr AS
SELECT *,
  avg(true_range) OVER (PARTITION BY ticker ORDER BY date ROWS BETWEEN 13 PRECEDING AND CURRENT ROW) AS atr14
FROM tr;""")

# SPY forward returns per horizon (for excess)
spy_cols=",\n".join(
  f"(lead(adjclose,{h}) OVER w / adjclose - 1) AS spy_ret_{h}" for h in HORIZONS)
con.execute(f"""CREATE TEMP TABLE spy AS
SELECT date, {spy_cols}
FROM read_parquet('{P}')
WHERE ticker='SPY'
WINDOW w AS (ORDER BY date);""")

# per-ticker forward returns + path excursions per horizon, then UNPIVOT to long
sel=["ticker","date","close","adjclose","atr14","(0.5*atr14/close) AS R_pct"]
for h in HORIZONS:
    sel.append(f"(lead(adjclose,{h}) OVER w / adjclose - 1) AS fwd_{h}")
    sel.append(f"(max(high) OVER (PARTITION BY ticker ORDER BY date ROWS BETWEEN 1 FOLLOWING AND {h} FOLLOWING)/close - 1) AS mfe_{h}")
    sel.append(f"(min(low)  OVER (PARTITION BY ticker ORDER BY date ROWS BETWEEN 1 FOLLOWING AND {h} FOLLOWING)/close - 1) AS mae_{h}")
con.execute(f"""CREATE TEMP TABLE wide AS
SELECT {', '.join(sel)}
FROM atr
WINDOW w AS (PARTITION BY ticker ORDER BY date);""")

# build long format
unions=[]
for h in HORIZONS:
    unions.append(f"""
    SELECT w.ticker, w.date, {h} AS horizon, w.close, w.atr14, w.R_pct,
      w.fwd_{h} AS fwd_ret, s.spy_ret_{h} AS spy_ret,
      (w.fwd_{h} - s.spy_ret_{h}) AS excess,
      w.mfe_{h} AS mfe_pct, w.mae_{h} AS mae_pct,
      (w.fwd_{h} IS NOT NULL) AS resolved,
      -- approximate path-aware +/-1R: target reached and stop not breached over the window
      (w.R_pct IS NOT NULL AND w.mfe_{h} >= w.R_pct AND w.mae_{h} > -w.R_pct) AS long_R_win,
      (w.R_pct IS NOT NULL AND -w.mae_{h} >= w.R_pct AND w.mfe_{h} < w.R_pct) AS short_R_win
    FROM wide w LEFT JOIN spy s USING(date)""")
con.execute(f"CREATE TEMP TABLE longt AS {' UNION ALL '.join(unions)};")
con.execute(f"COPY (SELECT * FROM longt) TO '{OUT}' (FORMAT PARQUET);")

# sanity
r=con.execute(f"""SELECT count(*),
   count(*) FILTER(WHERE resolved),
   count(distinct ticker), min(date), max(date)
   FROM read_parquet('{OUT}')""").fetchone()
print("returns rows / resolved / tickers / min / max:", r)
# resolution by horizon, restricted to panel signal-days only (proxy: dates that exist in panel)
print("\nresolved-fraction by horizon (all dates):")
for h in HORIZONS:
    a=con.execute(f"SELECT count(*) FILTER(WHERE resolved)*1.0/count(*) FROM read_parquet('{OUT}') WHERE horizon={h}").fetchone()[0]
    print(f"  h={h:>2}: {a:.2f}")
# example: SPY excess sanity (should be ~0 for SPY itself)
e=con.execute(f"SELECT horizon, avg(excess) FROM read_parquet('{OUT}') WHERE ticker='SPY' GROUP BY horizon ORDER BY horizon").fetchall()
print("\nSPY self-excess (should be ~0):", [(h,round(x,5)) for h,x in e])
print("wrote",OUT)
