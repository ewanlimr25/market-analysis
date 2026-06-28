#!/usr/bin/env python3
"""Systematic cross-sectional factor scan over features.parquet vs forward EXCESS.

For each factor x horizon: daily cross-sectional rank-IC (Spearman per day, averaged), its t-stat,
the decile long-short spread (D10-D1 mean excess), and the per-regime IC sign (A/B1/B2). A real
cross-sectional edge has |IC t-stat| high AND a sign-stable IC across regimes. excess already nets SPY,
so a nonzero IC is alpha, not beta. Look-ahead-safe (factor at T, excess from >T).
"""
import duckdb, os, math
D=os.path.expanduser("~/Development/market-analysis/data")
con=duckdb.connect()
con.execute(f"CREATE TEMP VIEW F AS SELECT * FROM read_parquet('{D}/features.parquet')")
con.execute(f"CREATE TEMP VIEW R AS SELECT ticker,date,horizon,excess,resolved FROM read_parquet('{D}/returns.parquet')")

FACTORS=['pcr','iv_rank','iv30d','implied_move_perc','volatility','vrp_name',
 'pct_52w_range','iv_mom_1w','iv_mom_1m','ivrank_chg_5d','vol_accel','gap',
 'netprem_mcap','netprem','bull_bear_skew','cv_pv','oi_call_share','log_mcap',
 'dp_buy_skew','dp_oneside','dp_block_n','dp_vol_share','dp_buy_skew_5d',
 'oi_net_cp','leap_net_build','oi_net_5d','netprem_5d',
 'hc_smart_dir','hc_sweep_share','hc_ml_share','hc_floor_share','hc_smart_5d']
HOR=[3,5,10,21]
REG={"A":"F.date BETWEEN DATE '2026-03-13' AND DATE '2026-03-27'",
     "B1":"F.date BETWEEN DATE '2026-04-27' AND DATE '2026-06-12'",
     "B2":"F.date BETWEEN DATE '2026-06-15' AND DATE '2026-06-26'"}

def ic(factor,h,where=""):
    q=f"""
    WITH j AS (SELECT F.date, F.{factor} AS f, R.excess AS e
              FROM F JOIN R ON F.ticker=R.ticker AND F.date=R.date
              WHERE R.horizon={h} AND R.resolved AND F.{factor} IS NOT NULL {where}),
    rk AS (SELECT date, rank() OVER (PARTITION BY date ORDER BY f) rf, rank() OVER (PARTITION BY date ORDER BY e) re FROM j),
    perday AS (SELECT date, corr(rf,re) ic, count(*) n FROM rk GROUP BY date HAVING count(*)>=20),
    dec AS (SELECT date, ntile(10) OVER (PARTITION BY date ORDER BY f) d, e FROM j),
    spread AS (SELECT date, avg(e) FILTER(WHERE d=10)-avg(e) FILTER(WHERE d=1) s FROM dec GROUP BY date)
    SELECT (SELECT avg(ic) FROM perday),(SELECT stddev_samp(ic) FROM perday),(SELECT count(*) FROM perday),
           (SELECT avg(s) FROM spread)"""
    r=con.execute(q).fetchone()
    if not r or r[0] is None: return None
    mean,sd,nd,spread=r
    t=mean/(sd/math.sqrt(nd)) if (sd and nd>1) else 0
    return dict(ic=mean,t=t,nd=nd,spread=spread)

rows=[]
for fac in FACTORS:
    best=None
    for h in HOR:
        a=ic(fac,h)
        if not a: continue
        regsign={k:(ic(fac,h,f"AND {v}") or {}).get('ic') for k,v in REG.items()}
        stable = all(s is not None for s in regsign.values()) and \
                 (all((s or 0)>0 for s in regsign.values()) or all((s or 0)<0 for s in regsign.values()))
        rec=dict(factor=fac,h=h,**a,stable=stable,reg=regsign)
        if best is None or abs(a['t'])>abs(best['t']): best=rec
    if best: rows.append(best)

rows.sort(key=lambda r:-abs(r['t']))
print(f"{'factor':<16}{'h':>3}{'IC':>8}{'t':>7}{'LSspread':>10}{'stable':>7}  regimeIC(A/B1/B2)")
for r in rows:
    rg=r['reg']; sg=lambda x: f"{x:+.02f}" if x is not None else "  na"
    flag="<<" if (abs(r['t'])>=3 and r['stable']) else ("<" if abs(r['t'])>=2.5 and r['stable'] else "")
    print(f"{r['factor']:<16}{r['h']:>3}{r['ic']:>+8.3f}{r['t']:>+7.1f}{(r['spread'] or 0):>+10.4f}{str(r['stable']):>7}  {sg(rg['A'])}/{sg(rg['B1'])}/{sg(rg['B2'])} {flag}")
print("\n<< = |t|>=3 AND regime-sign-stable (durable candidate);  < = |t|>=2.5 AND stable")
print("note: ~32 factors x 4 horizons => multiple testing; require |t|>=3 + stability + a mechanism before trusting.")
