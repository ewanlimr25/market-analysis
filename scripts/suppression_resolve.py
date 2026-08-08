#!/usr/bin/env python3
"""Resolve the names a GATE SUPPRESSED -- the counterfactual book behind Step 4 of /calibration-audit.

A gate that works erases its own evidence. Suppressed names live in `lane_status[].candidates`,
never in `calls[]`, so an audit resolver that harvests tickers from `calls[]` alone -- which is what
every audit through 2026-08-08 did -- has no bars for them and prints them as "unresolved",
indistinguishable from a window that simply has not matured. The 2026-08-01 audit reported
"4/5 suppressions resolvable" and read it as thin evidence; part of it was that gap. Fetching the
missing names recovered ACVA immediately (-3.03%, correctly suppressed).

This lives in `scripts/` on purpose: `analyses/audit/` is gitignored, so a fix made only in an audit
directory does not survive to the next cycle.

Reports four states, never a bare "unresolved":
  RESOLVED     window matured, excess computed
  OPEN         h-window has not matured against the current session grid
  PENDING      no entry session has traded yet (the final Friday book on a weekend run)
  INCONCLUSIVE genuinely unresolvable (no bars, delisted mid-window)

Excess is path-aware vs the conditional benchmark on the trading-day grid, adjusted closes:
    excess = sign * ( tk[exit]/tk[entry] - 1  -  spy[exit]/spy[entry] - 1 )
Entry is the session STRICTLY AFTER report_date (the panel exports post-8PM, so that is the first
tradable session) -- the same T1 convention the audit resolver uses.

Usage:
  python3 scripts/suppression_resolve.py
  python3 scripts/suppression_resolve.py --since 2026-07-01 --json
  python3 scripts/suppression_resolve.py --out analyses/audit/2026-08-15/suppressions.json
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import statistics as st
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chart import bars  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

# Lane -> (horizon, direction the lane would have taken). Must match the lane agents; a
# suppressed MOM_SHORT name is graded as the SHORT it would have been, not as a long.
LANE_HZ = {
    "MOM_LONG": (10, "long"),
    "MOM_SHORT": (10, "short"),
    "OI_FADE": (10, "short"),
    "S2_dp_revert": (5, "long"),
    "S4_pcr_fade": (10, "long"),
}
BENCH = "SPY"


def harvest(since: str | None = None) -> list[dict]:
    """Every `lane_status[].candidates` row across the scan + weekly envelopes."""
    import glob

    rows = []
    for pat in ("analyses/weekly/*/decision.json", "analyses/scan/*/decision.json"):
        for f in sorted(glob.glob(os.path.join(ROOT, pat))):
            with open(f) as fh:
                d = json.load(fh)
            rd = d.get("report_date")
            if not rd or (since and rd < since):
                continue
            for ls in d.get("lane_status") or []:
                for c in ls.get("candidates") or []:
                    tk = c if isinstance(c, str) else (c.get("ticker") if isinstance(c, dict) else None)
                    if tk:
                        rows.append({
                            "period": d.get("iso_week") or rd,
                            "report_date": rd,
                            "lane": ls.get("lane"),
                            "disposition": ls.get("disposition"),
                            "ticker": tk,
                        })
    return rows


def resolve(rows: list[dict]) -> list[dict]:
    tickers = sorted({r["ticker"] for r in rows} | {BENCH})
    px: dict[str, list[dict] | None] = {}
    for t in tickers:
        try:
            px[t] = bars(t, "1y")
        except Exception as exc:  # noqa: BLE001 -- record the failure, never guess a price
            px[t] = None
            print(f"  ! bars unavailable for {t}: {exc}", file=sys.stderr)

    spy = px.get(BENCH)
    if not spy:
        raise SystemExit(f"{BENCH} bars unavailable -- cannot compute excess")
    grid = [b["date"] for b in spy]

    out = []
    for r in rows:
        rec = dict(r)
        h, direction = LANE_HZ.get(r["lane"], (10, "long"))
        rec["horizon"], rec["direction"] = h, direction
        b = px.get(r["ticker"])
        ei = next((i for i, d in enumerate(grid) if d > r["report_date"]), None)
        if ei is None:
            rec["status"] = "PENDING"
            rec["why"] = f"no entry session yet (last {grid[-1]})"
        elif ei + h >= len(grid):
            rec["status"] = "OPEN"
            rec["entry"] = grid[ei]
            rec["why"] = f"h{h} window not matured (last {grid[-1]})"
        elif not b:
            rec["status"] = "INCONCLUSIVE"
            rec["why"] = "no bars"
        else:
            ix = {x["date"]: i for i, x in enumerate(b)}
            ed, xd = grid[ei], grid[ei + h]
            if ed not in ix or xd not in ix:
                rec["status"] = "INCONCLUSIVE"
                rec["why"] = f"no bar on {ed if ed not in ix else xd} (delisted/halted?)"
            else:
                sign = -1.0 if direction == "short" else 1.0
                tr = b[ix[xd]]["adj"] / b[ix[ed]]["adj"] - 1
                sr = spy[ei + h]["adj"] / spy[ei]["adj"] - 1
                rec["status"] = "RESOLVED"
                rec["entry"], rec["exit"] = ed, xd
                rec["excess_pct"] = round(sign * (tr - sr) * 100, 4)
                # Negative excess => the name would have LOST => the gate saved money.
                rec["gate_correct"] = bool(rec["excess_pct"] < 0)
        out.append(rec)
    return out


def report(res: list[dict]) -> None:
    print(f"\nsuppressed candidate-rows: {len(res)}  "
          f"{dict(collections.Counter(r['status'] for r in res))}")

    done = [r for r in res if r["status"] == "RESOLVED"]
    if not done:
        print("\nNo suppression has matured yet -- report N=0, never a verdict.")
        return

    print(f"\n{'period':<12}{'lane':<14}{'disposition':<18}{'ticker':<8}{'excess':>9}  verdict")
    for r in sorted(done, key=lambda z: (str(z["period"]), z["lane"], z["ticker"])):
        print(f"{str(r['period']):<12}{r['lane']:<14}{str(r['disposition']):<18}{r['ticker']:<8}"
              f"{r['excess_pct']:>+9.2f}%  {'saved' if r['gate_correct'] else 'COST EDGE'}")

    ex = [r["excess_pct"] for r in done]
    good = sum(1 for r in done if r["gate_correct"])
    print(f"\n{good}/{len(ex)} suppressions correct · mean avoided excess {st.fmean(ex):+.2f}% "
          f"· median {st.median(ex):+.2f}%")

    # One lane-period basket is ONE correlated observation, not N names.
    byb = collections.defaultdict(list)
    for r in done:
        byb[(r["period"], r["lane"])].append(r["excess_pct"])
    bask = [st.fmean(v) for v in byb.values()]
    print(f"basket-clustered (the honest unit): {len(bask)} lane-periods · mean {st.fmean(bask):+.2f}%")
    conf = "DURABLE" if len(bask) >= 30 else ("PROVISIONAL" if len(bask) >= 10 else "ANECDOTE")
    print(f"confidence: [{conf}] -- never recommend removing a gate on <10 baskets")

    still = collections.Counter((r["period"], r["lane"]) for r in res if r["status"] == "OPEN")
    if still:
        print(f"\nstill OPEN ({sum(still.values())} names) -- these mature into the next cycle:")
        for (p, ln), c in sorted(still.items()):
            print(f"  {p:<12}{ln:<14}{c}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--since", help="only envelopes with report_date >= this (YYYY-MM-DD)")
    ap.add_argument("--out", help="write the resolved rows to this JSON path")
    ap.add_argument("--json", action="store_true", help="print JSON instead of the table")
    a = ap.parse_args()

    rows = harvest(a.since)
    if not rows:
        print("no lane_status[] candidates found -- nothing to resolve")
        return
    res = resolve(rows)

    if a.out:
        os.makedirs(os.path.dirname(a.out), exist_ok=True)
        with open(a.out, "w") as fh:
            json.dump(res, fh, indent=1)
        print(f"wrote {len(res)} rows -> {a.out}")
    if a.json:
        print(json.dumps(res, indent=1))
    else:
        report(res)


if __name__ == "__main__":
    main()
