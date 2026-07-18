#!/usr/bin/env python3
"""Retrospective harness for the redesigned /market-scan workflow.

Given a signal-day T, mechanically fires the redesign's directional lanes (S1/S2/S4) under the
regime gate, and — because we have hindsight — resolves each call's realized forward EXCESS vs SPY
from the truth set. Run across all 54 panel days, it validates the redesign against known outcomes
and contrasts it with the old system's actual decision.json calls.

Lanes (all evidence-cited in DESIGN/40):
  S1 relative-weakness short  : screener close<=1.02*week_52_low, liquid; SHORT; h=10; regime-gated (stand down in rebound/squeeze)
  S2 DP-concentration revert  : dark pool one-sided >=90% of daily $ , total>=$10M; LONG (long-tilted); h=5; earnings-gated
  S4 PCR-high contrarian-long : screener put_call_ratio top 5% x-section, option-liquid, non-earnings; LONG (advisory); h=5

Usage:
  python3 retro_harness.py --date 2026-06-23           # fire + resolve one day
  python3 retro_harness.py --all                       # validate across all panel days (aggregate excess by lane)
  python3 retro_harness.py --all --compare-old         # also resolve the old system's decision.json calls
"""
import duckdb, glob, json, argparse, os, statistics
from datetime import date as _date

STOCKS = os.path.expanduser("~/Documents/Stocks")
DATA   = os.path.expanduser("~/Development/market-analysis/data")
OLD    = os.path.expanduser("~/Development/uw-daily-analysis/analyses/daily")
RET    = os.path.join(DATA, "returns.parquet")
PX     = os.path.join(DATA, "prices.parquet")
SCR = sorted(glob.glob(f"{STOCKS}/Stock Screener/stock-screener-*.parquet"))
DP  = sorted(glob.glob(f"{STOCKS}/Dark pool/dp-eod-report-*.parquet"))
FEAT = os.path.join(DATA, "features.parquet")   # for the oi_net_5d fade lane (Phase 7)

con = duckdb.connect()

def panel_dates():
    return [r[0].isoformat() for r in con.execute(
        f"SELECT distinct date FROM read_parquet({SCR!r}) ORDER BY date").fetchall()]

# ---- regime gate (from SPY) -------------------------------------------------
def classify_regime(T):
    r = con.execute(f"""
      WITH s AS (SELECT date, close, row_number() OVER (ORDER BY date) rn
                 FROM read_parquet('{PX}') WHERE ticker='SPY' AND date<=DATE '{T}')
      SELECT
        (SELECT close FROM s ORDER BY date DESC LIMIT 1) c0,
        (SELECT close FROM s ORDER BY date DESC LIMIT 1 OFFSET 5) c5,
        (SELECT close FROM s ORDER BY date DESC LIMIT 1 OFFSET 10) c10,
        (SELECT min(close) FROM (SELECT close FROM s ORDER BY date DESC LIMIT 15)) lo15
    """).fetchone()
    c0,c5,c10,lo15 = r
    if not (c0 and c10): return {"label":"UNKNOWN","ret5":None,"ret10":None,"s1_standdown":True}
    ret5  = c0/c5  - 1 if c5  else 0
    ret10 = c0/c10 - 1 if c10 else 0
    drawdown15 = (lo15/c10 - 1) if (lo15 and c10) else 0
    # crash/V-rebound/squeeze guard for S1 shorts:
    #   (a) strong 5d up-thrust (esp. off a recent dip)  -> rebound/junk-rally/squeeze already underway;
    #   (b) sharp UNCONFIRMED 5d dip (ret5<-2% while ret10 not in a downtrend) -> mean-reversion BOUNCE risk.
    # (b) added 2026-07-18 calibration audit: MOM_SHORT sized book was 0-for-9 shorting into short-term
    # SPY dips (trailing ret5 ~ -2.5%) that then V-rebounded. It is the mirror of (a); it deliberately does
    # NOT fire in a confirmed downtrend (ret10<=-2%), where the short leg is supposed to work.
    s1_standdown = ((ret5 > 0.025) or (ret5 > 0.015 and drawdown15 < -0.02)
                    or (ret5 < -0.02 and ret10 > -0.02))
    if ret10 >  0.015: label = "UPTREND"
    elif ret10 < -0.015: label = "PULLBACK"
    else: label = "CHOP"
    if s1_standdown: label += "/REBOUND-THRUST"
    return {"label":label,"ret5":round(ret5,4),"ret10":round(ret10,4),"s1_standdown":s1_standdown}

# ---- lanes ------------------------------------------------------------------
def fire(T):
    reg = classify_regime(T)
    calls = []
    # S1 relative-weakness short (h=10), regime-gated
    if not reg["s1_standdown"]:
        rows = con.execute(f"""
          SELECT ticker, close, week_52_low, close/nullif(week_52_low,0)-1 AS dist
          FROM read_parquet({SCR!r})
          WHERE date=DATE '{T}' AND close>=5 AND close*avg30_volume>=50e6
            AND week_52_low>0 AND close<=1.02*week_52_low
            AND issue_type IN ('Common Stock','ADR')   -- exclude ETPs (leveraged/inverse/cash) [audit 2026-07-18]
            AND (next_earnings_date IS NULL OR next_earnings_date > DATE '{T}'+10)
          ORDER BY dist ASC LIMIT 15""").fetchall()
        for tk,cl,lo,dist in rows:
            calls.append({"ticker":tk,"lane":"MOM_SHORT","direction":"short","horizon":10,
                "regime":reg["label"],"size":"starter","entry":round(cl,2),
                "invalidation":f"reclaims 52w-low anchor {round(lo,2)} / market V-rebound"})
    # MOM_LONG — near-52w-HIGH momentum (the cleaner leg, Phase 7 / RESEARCH/70); long, h=10 (also 21)
    rows = con.execute(f"""
      SELECT ticker, close, week_52_high, close/nullif(week_52_high,0) AS prox
      FROM read_parquet({SCR!r})
      WHERE date=DATE '{T}' AND close>=5 AND close*avg30_volume>=50e6
        AND week_52_high>0 AND close>=0.95*week_52_high
        AND issue_type IN ('Common Stock','ADR')   -- exclude ETPs [audit 2026-07-18]
        AND (next_earnings_date IS NULL OR next_earnings_date > DATE '{T}'+10)
      ORDER BY prox DESC LIMIT 15""").fetchall()
    for tk,cl,hi,prox in rows:
        calls.append({"ticker":tk,"lane":"MOM_LONG","direction":"long","horizon":10,
            "regime":reg["label"],"size":"starter","entry":round(cl,2),
            "invalidation":f"loses the 52w-high breakout / sharp risk-off reversal"})
    # OI_FADE — heavy 5-day net call-OI build => UNDERperformance (oi_net_5d, t=-7.1, Phase 7); short, h=10
    try:
        rows = con.execute(f"""
          SELECT f.ticker, f.oi_net_5d FROM read_parquet('{FEAT}') f
          WHERE f.date=DATE '{T}' AND f.oi_net_5d IS NOT NULL AND f.close>=5
            AND f.close*f.avg30_volume>=50e6
          ORDER BY f.oi_net_5d DESC LIMIT 15""").fetchall()
        for tk,v in rows:
            calls.append({"ticker":tk,"lane":"OI_FADE","direction":"short","horizon":10,
                "regime":reg["label"],"size":"starter","entry":None,
                "invalidation":"OI build reverses / name breaks out on real catalyst"})
    except Exception:
        pass
    # S2 DP one-sided concentration revert (h=5), long-tilted, earnings-gated
    erjoin = f"""JOIN (SELECT ticker, any_value(next_earnings_date) ned, any_value(issue_type) it,
                 any_value(is_index) idx FROM read_parquet({SCR!r})
                 WHERE date=DATE '{T}' GROUP BY ticker) e USING(ticker)"""
    rows = con.execute(f"""
      WITH dp AS (
        SELECT ticker,
          sum(premium) tot,
          sum(CASE WHEN price>=(nbbo_bid+nbbo_ask)/2 THEN premium ELSE 0 END) buyp,
          sum(CASE WHEN price< (nbbo_bid+nbbo_ask)/2 THEN premium ELSE 0 END) sellp
        FROM read_parquet({DP!r})
        WHERE date=DATE '{T}' AND canceled=false AND nbbo_bid>0 AND nbbo_ask>0
        GROUP BY ticker HAVING sum(premium)>=10e6)
      SELECT ticker, tot, buyp/tot AS buyshare FROM dp
      {erjoin}
      WHERE (buyp/tot>=0.90 OR sellp/tot>=0.90)
        AND (e.ned IS NULL OR e.ned > DATE '{T}'+5)   -- veto ER anywhere inside the h5 window (was +3; leak fixed audit 2026-07-18)
        AND e.it='Common Stock' AND e.idx=false
      ORDER BY tot DESC LIMIT 15""").fetchall()
    for tk,tot,buyshare in rows:
        calls.append({"ticker":tk,"lane":"S2_dp_revert","direction":"long","horizon":5,
            "regime":reg["label"],"size":"starter","entry":None,
            "invalidation":"news/earnings emerges; concentration not repeated next session"})
    # S4 PCR-high contrarian-long (h=5), advisory
    rows = con.execute(f"""
      WITH d AS (
        SELECT ticker, put_call_ratio, close,
          quantile_cont(put_call_ratio,0.95) OVER () AS p95
        FROM read_parquet({SCR!r})
        WHERE date=DATE '{T}' AND close>=5 AND close*avg30_volume>=50e6
          AND call_volume>0 AND put_volume>0 AND (call_volume+put_volume)>=1000
          AND issue_type IN ('Common Stock','ADR')   -- exclude ETPs [audit 2026-07-18]
          AND (next_earnings_date IS NULL OR next_earnings_date> DATE '{T}'+5))   -- full h5 window (was +3) [audit 2026-07-18]
      SELECT ticker, put_call_ratio FROM d WHERE put_call_ratio>=p95
      ORDER BY put_call_ratio DESC LIMIT 15""").fetchall()
    for tk,pcr in rows:
        calls.append({"ticker":tk,"lane":"S4_pcr_fade","direction":"long","horizon":5,
            "regime":reg["label"],"size":"advisory","entry":None,
            "invalidation":"put-heavy turns out informed (gap down on news)"})
    return reg, calls

# ---- resolve realized excess from truth set ---------------------------------
def resolve(T, calls):
    if not calls: return []
    con.execute("CREATE OR REPLACE TEMP TABLE c AS SELECT * FROM (VALUES " +
        ",".join(f"('{c['ticker']}', '{c['lane']}', '{c['direction']}', {c['horizon']})" for c in calls) +
        ") t(ticker, lane, direction, horizon)")
    rows = con.execute(f"""
      SELECT c.ticker,c.lane,c.direction,c.horizon,
        r.excess * (CASE WHEN c.direction='short' THEN -1 ELSE 1 END) AS dir_excess,
        CASE WHEN c.direction='short' THEN (r.spy_ret<0) ELSE (r.spy_ret>0) END AS base_hit,
        r.resolved
      FROM c LEFT JOIN read_parquet('{RET}') r
        ON c.ticker=r.ticker AND r.date=DATE '{T}' AND r.horizon=c.horizon
    """).fetchall()
    return rows

def run_all(compare_old=False):
    dates = panel_dates()
    lane_acc = {}   # lane -> list of (dir_excess, win, base_hit)
    standdowns=0
    for T in dates:
        reg, calls = fire(T)
        if reg["s1_standdown"]: standdowns+=1
        for tk,lane,dr,h,de,bh,res in resolve(T, calls):
            if not res or de is None: continue
            lane_acc.setdefault(lane,[]).append((de, 1 if de>0 else 0, 1 if bh else 0))
    print(f"\n=== REDESIGN retro-validation across {len(dates)} panel days ===")
    print(f"S1 stand-down days (regime gate fired): {standdowns}/{len(dates)}")
    print(f"{'lane':<14}{'n':>5}{'mean_exc':>10}{'hit':>7}{'base':>7}{'hit-base':>10}{'median':>9}")
    for lane,acc in sorted(lane_acc.items()):
        n=len(acc); me=statistics.mean(a[0] for a in acc); hit=statistics.mean(a[1] for a in acc)
        base=statistics.mean(a[2] for a in acc); med=statistics.median(a[0] for a in acc)
        print(f"{lane:<14}{n:>5}{me:>+10.4f}{hit:>7.2f}{base:>7.2f}{hit-base:>+10.3f}{med:>+9.4f}")
    if compare_old:
        compare_old_system()

def compare_old_system():
    print(f"\n=== OLD system (analyses/daily/*/decision.json) realized excess ===")
    files = sorted(glob.glob(f"{OLD}/*/decision.json"))
    tier_acc={}
    for f in files:
        try: env=json.load(open(f))
        except: continue
        T=env.get("report_date")
        for call in env.get("calls",[]):
            tk=call.get("ticker"); tier=call.get("tier"); dr=call.get("direction","")
            h=10 if call.get("horizon")=="swing" else (5 if call.get("horizon")=="weekly" else None)
            if not (tk and h and dr in ("long","short")): continue
            r=con.execute(f"""SELECT r.excess*(CASE WHEN '{dr}'='short' THEN -1 ELSE 1 END),
                 CASE WHEN '{dr}'='short' THEN (r.spy_ret<0) ELSE (r.spy_ret>0) END, r.resolved
                 FROM read_parquet('{RET}') r WHERE r.ticker='{tk}' AND r.date=DATE '{T}' AND r.horizon={h}""").fetchone()
            if not r or not r[2] or r[0] is None: continue
            tier_acc.setdefault(tier or "?",[]).append((r[0],1 if r[0]>0 else 0,1 if r[1] else 0))
    print(f"{'tier':<10}{'n':>5}{'mean_exc':>10}{'hit':>7}{'base':>7}{'hit-base':>10}")
    for tier,acc in sorted(tier_acc.items()):
        n=len(acc);
        if not n: continue
        me=statistics.mean(a[0] for a in acc); hit=statistics.mean(a[1] for a in acc); base=statistics.mean(a[2] for a in acc)
        print(f"{tier:<10}{n:>5}{me:>+10.4f}{hit:>7.2f}{base:>7.2f}{hit-base:>+10.3f}")

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--date"); ap.add_argument("--all",action="store_true")
    ap.add_argument("--compare-old",action="store_true")
    a=ap.parse_args()
    if a.all: run_all(a.compare_old)
    elif a.date:
        reg,calls=fire(a.date)
        print(f"REGIME {a.date}: {reg}")
        res={(r[0],r[1]):r for r in resolve(a.date,calls)}
        for c in calls:
            r=res.get((c['ticker'],c['lane']))
            de=f"{r[4]:+.4f}" if (r and r[4] is not None) else "unresolved"
            print(f"  {c['lane']:<14} {c['ticker']:<6} {c['direction']:<5} h{c['horizon']} size={c['size']:<8} realized_excess={de}  inval: {c['invalidation']}")
    else: ap.print_help()
