#!/usr/bin/env python3
"""Regime read from the panel -- and an arbitrator for what a sub-agent claims it is.

Two jobs:

  1. Print the authoritative regime for a date, straight from `_regime.classify_regime`
     (the same function the harness gates on), with an explicit staleness flag.
  2. ARBITRATE. Given a figure a lane/sub-agent reported back, check it against the panel
     and exit non-zero when they disagree past tolerance.

Job 2 is why this exists. In the 2026-W30 weekly review the Phase-B momentum lane reported
the week as "CHOP, ret10 -1.37%" while the panel gave PULLBACK at -2.122%. Both numbers were
stated with equal confidence in an agent's structured return; the disagreement was caught only
because the orchestrator happened to recompute it by hand. A lane that mis-reads the regime
mis-scores its own regime-fit, so this is a scoring error, not a reporting one.

Staleness is reported, never hidden: `uw risk market-regime --date` was observed echoing the
latest cached snapshot regardless of the date asked for, and `retro_harness.py --date` returns
the last panel bar for any date past the edge. Both look like a valid answer for the date you
asked about. This prints `asof` and `STALE` so the substitution is visible.

Usage:
  python3 scripts/regime_check.py --date 2026-07-24
  python3 scripts/regime_check.py --date 2026-07-24 --json
  python3 scripts/regime_check.py --date 2026-07-24 --claim-label CHOP --claim-ret10 -0.0137
  python3 scripts/regime_check.py --range 2026-07-20:2026-07-24        # Mon->Fri trajectory
"""
from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _calendar import trading_days  # noqa: E402
from _regime import classify_regime  # noqa: E402

# A lane quoting ret10 more than 25bp from the panel is not a rounding difference.
RET_TOL = 0.0025


def _fmt(r: dict) -> str:
    pct = lambda x: "  n/a  " if x is None else f"{x * 100:+7.3f}%"  # noqa: E731
    flag = "  [STALE -- panel bar is {}]".format(r["asof"]) if r["stale"] else ""
    return (f"{r['label']:22s} ret5 {pct(r['ret5'])}  ret10 {pct(r['ret10'])}  "
            f"dd15 {pct(r['drawdown15'])}  s1_standdown={str(r['s1_standdown']):5s}{flag}")


def arbitrate(r: dict, label: str | None, ret5: float | None, ret10: float | None) -> list[str]:
    """Return a list of disagreement strings; empty means the claim checks out."""
    bad: list[str] = []
    if label is not None:
        # Compare the base label; a /REBOUND-THRUST suffix is reported separately.
        panel_base = r["label"].split("/")[0]
        if label.strip().upper().split("/")[0] != panel_base:
            bad.append(f"label: claimed {label!r}, panel says {r['label']!r}")
    for name, claimed in (("ret5", ret5), ("ret10", ret10)):
        if claimed is None:
            continue
        actual = r[name]
        if actual is None:
            bad.append(f"{name}: claimed {claimed:+.4f}, panel has no value")
        elif abs(claimed - actual) > RET_TOL:
            bad.append(f"{name}: claimed {claimed:+.4f}, panel says {actual:+.4f} "
                       f"(off by {abs(claimed - actual) * 100:.2f}pp)")
    return bad


def main() -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--date", help="trade date YYYY-MM-DD")
    g.add_argument("--range", dest="rng", help="START:END, prints every trading day in between")
    ap.add_argument("--claim-label", help="regime label a sub-agent reported, e.g. CHOP")
    ap.add_argument("--claim-ret5", type=float, help="ret5 a sub-agent reported, as a decimal")
    ap.add_argument("--claim-ret10", type=float, help="ret10 a sub-agent reported, as a decimal")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if a.rng:
        start, _, end = a.rng.partition(":")
        if not end:
            print("--range needs START:END", file=sys.stderr)
            return 2
        days = [d.isoformat() for d in trading_days()
                if start <= d.isoformat() <= end]
        if not days:
            print(f"no panel trading days in {start}..{end}", file=sys.stderr)
            return 1
        rows = {d: classify_regime(d) for d in days}
        if a.json:
            print(json.dumps(rows, indent=2))
            return 0
        for d, r in rows.items():
            print(f"  {d}  {_fmt(r)}")
        first, last = rows[days[0]], rows[days[-1]]
        print(f"\ntrajectory: {first['label']} -> {last['label']}   "
              f"ret10 {first['ret10']:+.4f} -> {last['ret10']:+.4f}")
        return 0

    r = classify_regime(a.date)
    claims = (a.claim_label, a.claim_ret5, a.claim_ret10)
    bad = arbitrate(r, *claims) if any(c is not None for c in claims) else []

    if a.json:
        print(json.dumps({**r, "disagreements": bad}, indent=2))
    else:
        print(f"regime {a.date}: {_fmt(r)}")
        if any(c is not None for c in claims):
            if bad:
                print("\nDISAGREES WITH THE PANEL:")
                for b in bad:
                    print(f"  ! {b}")
                print("\nUse the panel figure. A lane that mis-reads the regime mis-scores its own regime-fit.")
            else:
                print("\nclaim checks out against the panel")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
