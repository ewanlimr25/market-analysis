"""Layer-3 PR-WT arms, computed from code so they ARE reproducible.
Fixes the recorded defect: pre-W35 Layer-3 base rates lived in prose and matched no predicate.
Scoring currency = EXCESS vs SPY over the SAME forward weeks (invariant #1).
Clustered by wk_start: every ticker in a week shares one market shock.
"""
import duckdb, math

WF = 'data/weekly_features.parquet'
con = duckdb.connect()

# forward k-week compounded return per ticker, and SPY's, then excess.
def build(k):
    q = f"""
    with base as (
      select ticker, wk_start, w_close, w_ret, close_pos, body_frac,
             inside_week, outside_week, higher_high, lower_low,
             hammer_or_hanging, star_or_inverted, follow_through,
             lead(w_close, {k}) over (partition by ticker order by wk_start) as fwd_close
      from '{WF}'
    ),
    fwd as (select *, fwd_close/w_close - 1.0 as fwd_ret from base where fwd_close is not null),
    spy as (select wk_start, fwd_ret as spy_fwd from fwd where ticker='SPY')
    select f.*, f.fwd_ret - s.spy_fwd as excess
    from fwd f join spy s using (wk_start)
    where f.ticker <> 'SPY'
    """
    return con.execute(q).df()

def clustered(df, mask, label, k):
    sub = df[mask]
    if len(sub) == 0:
        print(f"  {label:<34} n=0"); return
    # cluster mean by week, then t across weeks (the repo's clustering rule)
    g = sub.groupby('wk_start')['excess'].mean()
    n_rows, n_wk = len(sub), len(g)
    m = g.mean(); sd = g.std(ddof=1)
    t = m/(sd/math.sqrt(n_wk)) if n_wk > 1 and sd and sd > 0 else float('nan')
    base = df[~mask]
    bm = base.groupby('wk_start')['excess'].mean().mean() if len(base) else float('nan')
    print(f"  {label:<34} rows={n_rows:>6}  weeks={n_wk:>3}  excess={m:+.4f}  vs_rest={bm:+.4f}  diff={m-bm:+.4f}  t_wk={t:+.2f}")

for k in (2, 4):
    print(f"\n=== forward {k}-week EXCESS vs SPY  (cross-sectional, clustered by week) ===")
    df = build(k)
    print(f"  panel: {len(df)} rows, {df.wk_start.nunique()} weeks, {df.ticker.nunique()} tickers")
    clustered(df, df.hammer_or_hanging == True, "A hammer_or_hanging", k)
    clustered(df, (df.lower_low == True) & (df.close_pos >= 0.70), "B undercut+reclaim (LL & cpos>=.7)", k)
    clustered(df, df.inside_week == True, "C inside_week", k)
    clustered(df, df.follow_through == True, "D follow_through", k)
    clustered(df, df.outside_week == True, "E outside_week", k)
    clustered(df, df.star_or_inverted == True, "F star_or_inverted", k)
