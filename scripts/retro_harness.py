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
  python3 retro_harness.py --all --oi-variant both     # grade the RAW vs the LIVE OI_FADE rule
"""
import duckdb, glob, json, argparse, os, statistics, sys
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

# Gates compare against the end of the real TRADING-day window, never DATE 'T'+N
# calendar days -- see scripts/_calendar.py for why. [audit 2026-07-24]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _calendar import hz_end  # noqa: E402
from _regime import classify_regime as _classify_regime  # noqa: E402

def panel_dates():
    return [r[0].isoformat() for r in con.execute(
        f"SELECT distinct date FROM read_parquet({SCR!r}) ORDER BY date").fetchall()]

# ---- lane thresholds --------------------------------------------------------
# S4 fades an over-hedged CROWD, which requires an actual two-sided book. The original
# filter (call_volume>0 AND put_volume>0 AND call_volume+put_volume>=1000) put no real
# floor on the CALL leg, so a name with 3 calls against 2,046 puts cleared it and printed
# PCR 682 (NWG, 2026-08-17). Across the panel the median S4 selection carried only 154
# call contracts, p25=66, p10=20 -- PCR on a two-digit denominator measures illiquidity,
# not sentiment, and moves >0.5% per single contract.
# Floor chosen on RATIO-STABILITY grounds (one contract must not move PCR materially),
# not by maximising measured excess -- raising it monotonically LOWERS S4's measured mean.
# [audit 2026-08-17]
S4_MIN_CALL_VOLUME = 250

# ---- OI_FADE: the harness rule vs the LIVE rule -----------------------------------------
# The baseline OI_FADE lane below ranks by RAW `oi_net_5d`. The live lane
# (`.claude/agents/oi-flow-fade.md`, `scripts/oi_build.py`) ranks by `oi_rel_build`
# = net_5d / avg_30_day_call_oi and drops single-day blocks via `persistence_ratio`.
# Those are DIFFERENT RULES, so the +0.0038 prior and the forward book grade different
# things and the gap between them cannot be read as decay (2026-08-18 scan FINDING 1;
# 2026-08-22 audit proposal 6). `--oi-variant both` grades all three selections on the same
# panel -- baseline, raw-rank-on-the-live-pool, and the live rule -- so the RULE difference is
# separated from the POOL difference instead of being read off one confounded number.
#
# NOT implementable here, and therefore still ungraded: the live lane's news/catalyst gates
# need the news tape, which the panel does not carry. `live` is the live RANKING plus the
# persistence gate -- it prices the SELECTION difference, not the gating difference.
OI_PERSISTENCE_MAX = 0.85          # oi_build.py flags >0.85 as a single institutional block
_OI_LIVE_PANEL_READY = False


def _ensure_oi_live_panel():
    """Materialise the 5-day OI build panel once -- a window scan per panel day is too slow."""
    global _OI_LIVE_PANEL_READY
    if _OI_LIVE_PANEL_READY:
        return
    con.execute(f"""
      CREATE OR REPLACE TEMP TABLE oi_live AS
      WITH w AS (
        SELECT ticker, date, close, avg30_volume,
               sum(oi_net_cp)      OVER win AS net_sum,
               max(abs(oi_net_cp)) OVER win AS max_abs,
               count(oi_net_cp)    OVER win AS nobs
        FROM read_parquet('{FEAT}')
        WINDOW win AS (PARTITION BY ticker ORDER BY date ROWS BETWEEN 4 PRECEDING AND CURRENT ROW)
      )
      SELECT ticker, date, close, avg30_volume, net_sum,
             CASE WHEN net_sum<>0 THEN max_abs/abs(net_sum) END AS persistence
      FROM w WHERE nobs=5""")
    _OI_LIVE_PANEL_READY = True


def oi_fade_pool_candidates(T, rank="rel", persistence_gate=True, limit=15):
    """OI_FADE selection on the LIVE-ELIGIBLE pool: a full 5-day OI window and a real call book.

    `rank="rel"` is the live rule (oi_rel_build = net_5d / avg_30_day_call_oi);
    `rank="raw"` is the baseline rule (net 5-day build) run on the SAME pool.

    Why the pool is restricted, and why that matters for the comparison: the baseline lane
    ranks on `features.oi_net_5d`, which is `avg(oi_net_cp)` over `ROWS BETWEEN 4 PRECEDING
    AND CURRENT ROW` -- and `avg` does NOT require five observations. A ticker with a partial
    window is divided by k<5, which inflates it into the top-15. Measured 2026-08-22: 75 of
    the baseline's 1,237 resolved rows (6.1%) have a partial window and carry mean +0.0277,
    against +0.0013 for the 1,162 full-window rows. **More than half the lane's headline
    +0.0029 comes from 6% of rows that never had a full 5-day build** -- the same shape as the
    S4 PCR-denominator artifact. `oi_rel_build` cannot even be computed for them (no call-OI
    base), so any raw-vs-live comparison must hold the pool fixed or it prices the artifact
    instead of the rule.
    """
    _ensure_oi_live_panel()
    order = "o.net_sum/s.acoi DESC" if rank == "rel" else "o.net_sum DESC"
    pgate = (f"AND (o.persistence IS NULL OR o.persistence <= {OI_PERSISTENCE_MAX})"
             if persistence_gate else "")
    return con.execute(f"""
      SELECT o.ticker, o.net_sum/s.acoi AS rel_build, o.persistence
      FROM oi_live o
      JOIN (SELECT ticker, any_value(avg_30_day_call_oi) acoi,
                   any_value(next_earnings_date) ned, any_value(issue_type) it,
                   any_value(is_index) idx
            FROM read_parquet({SCR!r}) WHERE date=DATE '{T}' GROUP BY ticker) s USING(ticker)
      WHERE o.date=DATE '{T}' AND s.acoi>0 AND o.net_sum>0
        AND o.close>=5 AND o.close*o.avg30_volume>=50e6
        AND (s.ned IS NULL OR s.ned > DATE '{hz_end(T,10)}')
        AND s.it IN ('Common Stock','ADR') AND s.idx=false {pgate}
      ORDER BY {order} LIMIT {limit}""").fetchall()

# ---- regime gate (from SPY) -------------------------------------------------
# Lives in scripts/_regime.py so the harness, the live scan and the lanes cannot drift
# apart on the label or the crash guard -- same reasoning as the _calendar.hz_end move.
# [2026-W30 weekly review: a Phase-B lane reported CHOP/-1.37% against the panel's
#  PULLBACK/-2.122%, and nothing reconciled them automatically.]
def classify_regime(T):
    return _classify_regime(T, con)

# ---- lanes ------------------------------------------------------------------
def fire(T, oi_variant="raw"):
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
            AND (next_earnings_date IS NULL OR next_earnings_date > DATE '{hz_end(T,10)}')  -- trading-day h10 [audit 2026-07-24]
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
        AND (next_earnings_date IS NULL OR next_earnings_date > DATE '{hz_end(T,10)}')  -- trading-day h10 [audit 2026-07-24]
      ORDER BY prox DESC LIMIT 15""").fetchall()
    for tk,cl,hi,prox in rows:
        calls.append({"ticker":tk,"lane":"MOM_LONG","direction":"long","horizon":10,
            "regime":reg["label"],"size":"starter","entry":round(cl,2),
            "invalidation":f"loses the 52w-high breakout / sharp risk-off reversal"})
    # OI_FADE — heavy 5-day net call-OI build => UNDERperformance (oi_net_5d, t=-7.1, Phase 7); short, h=10
    try:
        rows = con.execute(f"""
          SELECT f.ticker, f.oi_net_5d FROM read_parquet('{FEAT}') f
          JOIN (SELECT ticker, any_value(next_earnings_date) ned, any_value(issue_type) it,
                       any_value(is_index) idx FROM read_parquet({SCR!r})
                WHERE date=DATE '{T}' GROUP BY ticker) e USING(ticker)
          WHERE f.date=DATE '{T}' AND f.oi_net_5d IS NOT NULL AND f.close>=5
            AND f.close*f.avg30_volume>=50e6
            -- [audit 2026-07-24] this lane previously had NO earnings gate and NO ETP
            -- exclusion (the 2026-07-18 hygiene pass reached MOM_SHORT/MOM_LONG/S4 and
            -- skipped it, since features.parquet carries no issue_type). 34% of its picks
            -- were untradeable -- 301/1095 slots ETFs, 72 earnings-in-h10 -- and the edge
            -- was carried largely by shorting leveraged inverse ETFs (SOXS up to +0.98
            -- short-excess/obs across a semis rally), i.e. beta, not an OI edge.
            AND (e.ned IS NULL OR e.ned > DATE '{hz_end(T,10)}')
            AND e.it IN ('Common Stock','ADR') AND e.idx=false
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
        AND (e.ned IS NULL OR e.ned > DATE '{hz_end(T,5)}')   -- veto ER anywhere inside the h5 window (+3 -> +5 audit 2026-07-18; calendar -> trading-day audit 2026-07-24)
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
          AND call_volume>={S4_MIN_CALL_VOLUME} AND put_volume>0 AND (call_volume+put_volume)>=1000   -- real call book, not a 3-contract denominator [audit 2026-08-17]
          AND issue_type IN ('Common Stock','ADR')   -- exclude ETPs [audit 2026-07-18]
          AND (next_earnings_date IS NULL OR next_earnings_date> DATE '{hz_end(T,5)}'))   -- full h5 window (+3 -> +5 audit 2026-07-18; calendar -> trading-day audit 2026-07-24)
      SELECT ticker, put_call_ratio FROM d WHERE put_call_ratio>=p95
      ORDER BY put_call_ratio DESC LIMIT 15""").fetchall()
    for tk,pcr in rows:
        calls.append({"ticker":tk,"lane":"S4_pcr_fade","direction":"long","horizon":5,
            "regime":reg["label"],"size":"advisory","entry":None,
            "invalidation":"put-heavy turns out informed (gap down on news)"})
    # OI_FADE (LIVE rule) -- emitted under its own lane name so a `both` run compares the two
    # selections side by side on identical days. The raw block above is untouched: `raw` (the
    # default) must stay bit-identical to the recorded baseline. [audit 2026-08-22]
    if oi_variant in ("live", "both"):
        # OI_FADE_RAWPOOL isolates the RULE from the POOL: raw ranking on the live-eligible
        # pool. OI_FADE vs OI_FADE_RAWPOOL is the partial-window artifact; OI_FADE_RAWPOOL vs
        # OI_FADE_LIVE is the actual raw-vs-live rule comparison. Reading the headline
        # OI_FADE vs OI_FADE_LIVE alone conflates the two.
        variants = ((("OI_FADE_RAWPOOL", "raw", False),) if oi_variant == "both" else ()) + \
                   (("OI_FADE_LIVE", "rel", True),)
        for lane_name, rank, pgate in variants:
            try:
                for tk, _rel, _pers in oi_fade_pool_candidates(T, rank, pgate):
                    calls.append({"ticker":tk,"lane":lane_name,"direction":"short","horizon":10,
                        "regime":reg["label"],"size":"starter","entry":None,
                        "invalidation":"OI build reverses / name breaks out on real catalyst"})
            except Exception:
                pass
    if oi_variant == "live":
        calls = [c for c in calls if c["lane"] != "OI_FADE"]
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

def run_all(compare_old=False, oi_variant="raw"):
    dates = panel_dates()
    lane_acc = {}   # lane -> list of (dir_excess, win, base_hit)
    standdowns=0
    for T in dates:
        reg, calls = fire(T, oi_variant)
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
    ap.add_argument("--oi-variant", choices=("raw","live","both"), default="raw",
                    help="OI_FADE selection rule: raw oi_net_5d (baseline), the live "
                         "oi_rel_build+persistence rule, or both side by side")
    a=ap.parse_args()
    if a.all: run_all(a.compare_old, a.oi_variant)
    elif a.date:
        reg,calls=fire(a.date, a.oi_variant)
        print(f"REGIME {a.date}: {reg}")
        res={(r[0],r[1]):r for r in resolve(a.date,calls)}
        for c in calls:
            r=res.get((c['ticker'],c['lane']))
            de=f"{r[4]:+.4f}" if (r and r[4] is not None) else "unresolved"
            print(f"  {c['lane']:<14} {c['ticker']:<6} {c['direction']:<5} h{c['horizon']} size={c['size']:<8} realized_excess={de}  inval: {c['invalidation']}")
    else: ap.print_help()
