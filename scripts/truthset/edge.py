#!/usr/bin/env python3
"""Shared edge-measurement helper. ONE canonical, look-ahead-safe outcome resolver so every
per-source extraction agent reports comparable numbers.

INPUT  : a signals file (parquet OR csv) with columns:
           ticker (str), date (DATE/str 'YYYY-MM-DD' = signal day T),
           signal_name (str), direction ('long'|'short'), strength (float; bigger=stronger conviction)
OUTPUT : ranked edge table (stdout JSON + optional --out parquet), grouped by (signal_name, horizon, regime).

Per group it reports (excess = ticker_fwd_ret - SPY_same-window_ret; dir_excess = excess * (+1 long / -1 short)):
  n            decided (resolved) rows
  mean_exc     mean directional excess (the EDGE; >0 = beat SPY in thesis direction)
  med_exc      median directional excess
  hit          P(dir_excess > 0)
  base         same-window SPY base rate in thesis direction (long: P(spy>0); short: P(spy<0))
  hit_x_base   hit - base   (excess hit-rate; the number that separates edge from beta)
  ic           Spearman(strength, dir_excess) over the group
  path_win     mean path-aware +/-1R win flag (long_R_win/short_R_win)
  p            two-sided normal-approx p-value on mean_dir_excess != 0 (BH-correct downstream)

Regimes: A=03-13..03-27, B1=04-27..06-12, B2=06-15..06-26, plus ALL.
Usage: python3 edge.py --signals sig.parquet [--out edge.parquet] [--min-n 8] [--horizons 1,3,5,10,21]
"""
import duckdb, json, argparse, math, os
HERE=os.path.dirname(os.path.abspath(__file__))
RET=os.path.join(HERE,"..","..","data","returns.parquet")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--signals",required=True)
    ap.add_argument("--out",default=None)
    ap.add_argument("--min-n",type=int,default=8)
    ap.add_argument("--horizons",default="1,3,5,10,21")
    ap.add_argument("--top",type=int,default=200)
    a=ap.parse_args()
    hs=[int(x) for x in a.horizons.split(",")]
    con=duckdb.connect()
    reader = (f"read_parquet('{a.signals}')" if a.signals.endswith("parquet")
              else f"read_csv_auto('{a.signals}', header=true)")
    con.execute(f"""CREATE TEMP TABLE sig AS
      SELECT ticker, date::DATE AS date, signal_name,
             lower(direction) AS direction, CAST(strength AS DOUBLE) AS strength
      FROM {reader} WHERE direction IS NOT NULL""")
    # join to returns; build dir_excess and base-rate flags
    con.execute(f"""CREATE TEMP TABLE j AS
      SELECT s.signal_name, s.direction, s.strength, r.horizon, s.date,
        CASE WHEN s.direction='short' THEN -1 ELSE 1 END AS dir,
        r.excess * (CASE WHEN s.direction='short' THEN -1 ELSE 1 END) AS dir_excess,
        CASE WHEN s.direction='short'
             THEN (CASE WHEN r.spy_ret<0 THEN 1.0 ELSE 0 END)
             ELSE (CASE WHEN r.spy_ret>0 THEN 1.0 ELSE 0 END) END AS base_hit,
        CASE WHEN s.direction='short' THEN r.short_R_win ELSE r.long_R_win END AS path_win,
        CASE WHEN s.date BETWEEN DATE '2026-03-13' AND DATE '2026-03-27' THEN 'A'
             WHEN s.date BETWEEN DATE '2026-04-27' AND DATE '2026-06-12' THEN 'B1'
             WHEN s.date BETWEEN DATE '2026-06-15' AND DATE '2026-06-26' THEN 'B2'
             ELSE 'OTHER' END AS regime
      FROM sig s JOIN read_parquet('{RET}') r
        ON s.ticker=r.ticker AND s.date=r.date
      WHERE r.resolved AND r.horizon IN ({','.join(map(str,hs))})""")

    def agg(regime_filter, regime_label):
        q=f"""WITH ranked AS (
            SELECT signal_name, direction, horizon, dir_excess, base_hit, path_win,
              rank() OVER (PARTITION BY signal_name,horizon ORDER BY strength)    AS rk_s,
              rank() OVER (PARTITION BY signal_name,horizon ORDER BY dir_excess)  AS rk_e
            FROM j {regime_filter})
          SELECT signal_name, direction, horizon,
            count(*) n, avg(dir_excess) mean_exc, median(dir_excess) med_exc,
            avg(CASE WHEN dir_excess>0 THEN 1.0 ELSE 0 END) hit,
            avg(base_hit) base, avg(CASE WHEN path_win THEN 1.0 ELSE 0 END) path_win,
            stddev_samp(dir_excess) sd,
            corr(rk_s, rk_e) ic
          FROM ranked
          GROUP BY signal_name, direction, horizon
          HAVING count(*)>={a.min_n}
          ORDER BY signal_name, horizon"""
        out=[]
        for row in con.execute(q).fetchall():
            (name,direction,h,n,mean_exc,med_exc,hit,base,path_win,sd,ic)=row
            # normal-approx p on mean_dir_excess != 0
            if sd and n>1 and sd>0:
                z=mean_exc/(sd/math.sqrt(n)); p=math.erfc(abs(z)/math.sqrt(2))
            else: p=None
            out.append(dict(signal_name=name,direction=direction,horizon=h,regime=regime_label,
                n=int(n),mean_exc=round(mean_exc,4),med_exc=round(med_exc,4),
                hit=round(hit,3),base=round(base,3),hit_x_base=round(hit-base,3),
                path_win=round(path_win,3) if path_win is not None else None,
                ic=round(ic,3) if ic is not None else None,
                p=round(p,4) if p is not None else None))
        return out

    rows=[]
    rows+=agg("","ALL")
    for rf,lbl in [("WHERE regime='A'","A"),("WHERE regime='B1'","B1"),("WHERE regime='B2'","B2")]:
        rows+=agg(rf,lbl)
    # rank ALL-regime rows by mean_exc for convenience
    allrows=[r for r in rows if r["regime"]=="ALL"]
    allrows.sort(key=lambda r:-r["mean_exc"])
    print(json.dumps({"n_signal_rows":con.execute("SELECT count(*) FROM sig").fetchone()[0],
                      "n_joined":con.execute("SELECT count(*) FROM j").fetchone()[0],
                      "all_regime_ranked":allrows[:a.top],
                      "by_regime":[r for r in rows if r["regime"]!="ALL"]}, indent=1, default=str))
    if a.out:
        con.execute("CREATE TEMP TABLE res AS SELECT * FROM (SELECT 1) WHERE 1=0")  # placeholder
        import csv
        outcsv=a.out.replace(".parquet",".csv")
        with open(outcsv,"w",newline="") as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
        print("wrote",outcsv)

if __name__=="__main__": main()
