"""The regime gate, shared by the harness / lanes / live scan.

Single source of truth for "what regime is it, and is the crash guard on?".

Extracted from `retro_harness.py` on 2026-07-25 for the same reason `hz_end` was extracted
into `_calendar.py` the day before: the definition kept being re-derived per caller and kept
coming back different. In the 2026-W30 weekly review the Phase-B momentum lane independently
reported the week as CHOP with ret10 -1.37%, while the panel gave PULLBACK at -2.122% -- a
disagreement large enough to flip the label and the lane's regime-fit. Nothing reconciled the
two automatically; it was caught by hand.

Two definitions here are easy to get wrong when re-deriving, and both are load-bearing:
  * `drawdown15` is min(last 15 closes) / close_10_sessions_back - 1. It is NOT a peak-to-
    trough drawdown. A peak-based re-derivation gives a different number and silently changes
    which arm of the crash guard fires.
  * `ret5`/`ret10` are close-to-close over 5 and 10 *trading* sessions from the panel grid,
    not calendar days.

Stdlib + duckdb only. Reads the truth-set price panel, so it inherits the panel edge: a date
past the edge resolves against the last available bar. Callers wanting a live read past the
edge must supply prices themselves -- see `regime_check.py --explain` for the staleness flag.
"""
from __future__ import annotations

import os

HERE = os.path.dirname(os.path.abspath(__file__))
PX = os.path.join(HERE, "..", "data", "prices.parquet")

# Label thresholds on trailing 10-session SPY return.
UPTREND_RET10 = 0.015
PULLBACK_RET10 = -0.015


def classify_regime(T, con=None) -> dict:
    """Regime label + crash-guard verdict for signal-day T.

    Returns {label, ret5, ret10, drawdown15, s1_standdown, asof, stale}.
    `asof` is the last panel bar at or before T; `stale` is True when that bar is
    earlier than T (i.e. T is past the panel edge, or a non-trading day).
    """
    if con is None:
        import duckdb
        con = duckdb.connect()
    r = con.execute(f"""
      WITH s AS (SELECT date, close, row_number() OVER (ORDER BY date) rn
                 FROM read_parquet('{PX}') WHERE ticker='SPY' AND date<=DATE '{T}')
      SELECT
        (SELECT close FROM s ORDER BY date DESC LIMIT 1) c0,
        (SELECT close FROM s ORDER BY date DESC LIMIT 1 OFFSET 5) c5,
        (SELECT close FROM s ORDER BY date DESC LIMIT 1 OFFSET 10) c10,
        (SELECT min(close) FROM (SELECT close FROM s ORDER BY date DESC LIMIT 15)) lo15,
        (SELECT date  FROM s ORDER BY date DESC LIMIT 1) d0
    """).fetchone()
    c0, c5, c10, lo15, d0 = r
    asof = d0.isoformat() if d0 else None
    stale = bool(asof and asof != str(T))
    if not (c0 and c10):
        return {"label": "UNKNOWN", "ret5": None, "ret10": None, "drawdown15": None,
                "s1_standdown": True, "asof": asof, "stale": stale}
    ret5 = c0 / c5 - 1 if c5 else 0
    ret10 = c0 / c10 - 1 if c10 else 0
    drawdown15 = (lo15 / c10 - 1) if (lo15 and c10) else 0
    # crash/V-rebound/squeeze guard for the momentum short leg:
    #   (a) strong 5d up-thrust (esp. off a recent dip)  -> rebound/junk-rally/squeeze already underway;
    #   (b) sharp UNCONFIRMED 5d dip (ret5<-2% while ret10 not in a downtrend) -> mean-reversion BOUNCE risk.
    # (b) added 2026-07-18 calibration audit: MOM_SHORT sized book was 0-for-9 shorting into short-term
    # SPY dips (trailing ret5 ~ -2.5%) that then V-rebounded. It is the mirror of (a); it deliberately does
    # NOT fire in a confirmed downtrend (ret10<=-2%), where the short leg is supposed to work.
    s1_standdown = ((ret5 > 0.025) or (ret5 > 0.015 and drawdown15 < -0.02)
                    or (ret5 < -0.02 and ret10 > -0.02))
    if ret10 > UPTREND_RET10:
        label = "UPTREND"
    elif ret10 < PULLBACK_RET10:
        label = "PULLBACK"
    else:
        label = "CHOP"
    if s1_standdown:
        label += "/REBOUND-THRUST"
    return {"label": label, "ret5": round(ret5, 4), "ret10": round(ret10, 4),
            "drawdown15": round(drawdown15, 4), "s1_standdown": s1_standdown,
            "asof": asof, "stale": stale}
