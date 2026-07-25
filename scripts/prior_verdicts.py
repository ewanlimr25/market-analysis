#!/usr/bin/env python3
"""What did we already decide about this ticker?

Sweeps the recent `analyses/{scan,weekly}/*/decision.json`, `conviction_*.json` and
`lane_status[]` for a ticker and prints every prior adjudication: sized calls, VETOes,
watch-only downgrades, exclusions, held positions and their invalidations.

Exists because lane sub-agents do not carry prior state, so they re-propose names that were
already killed -- and they re-propose them with a clean bill of health, because the reason for
the kill lives outside the lane's own gates. In the 2026-W30 weekly review the OI_FADE lane
returned ALLE as its clean new starter and SSNC as a watch. Both had been adjudicated the night
before: ALLE on a fundamentals VETO (raised FY26 guidance plus two same-day PT raises above
spot), SSNC on catalyst resolution. Neither was catchable from inside the lane. The same gap
bites held positions -- the momentum lane read ORCL against its superseded entry-era stop
rather than the tightened one recorded at the trim.

Run this on every candidate BEFORE scoring it, and on every held name before re-reading its
invalidation.

Exit code is 1 when anything blocking is found (VETO / EXCLUDED / skip), so it can gate a loop.

Usage:
  python3 scripts/prior_verdicts.py --tickers ALLE,SSNC
  python3 scripts/prior_verdicts.py --tickers ORCL --days 30
  python3 scripts/prior_verdicts.py --tickers ALLE --json
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
from datetime import date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
ANALYSES = os.path.join(ROOT, "analyses")

# Substrings that mean "this name was stopped", checked case-insensitively against
# any verdict/size/tier/disposition field.
BLOCKING = ("veto", "excluded", "skip", "no_name_cleared", "stood_down", "cut")


def _files(days: int) -> list[str]:
    """Recent decision/conviction files, newest first."""
    cutoff = (date.today() - timedelta(days=days)).isoformat()
    out: list[str] = []
    for pat in ("scan/*/decision.json", "scan/*/conviction_*.json",
                "weekly/*/decision.json"):
        for p in glob.glob(os.path.join(ANALYSES, pat)):
            # the directory name carries the date (2026-07-24 or 2026-W30)
            stamp = os.path.basename(os.path.dirname(p))
            if stamp.startswith("2") and "W" not in stamp and stamp < cutoff:
                continue
            out.append(p)
    return sorted(out, reverse=True)


def _walk(node, ticker: str, path: str, hits: list[dict]) -> None:
    """Collect any dict that names `ticker` in a ticker-ish field."""
    if isinstance(node, dict):
        for key in ("ticker", "symbol"):
            if str(node.get(key, "")).upper() == ticker:
                hits.append({"where": path, "entry": node})
                break
        for k, v in node.items():
            _walk(v, ticker, f"{path}.{k}", hits)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            _walk(v, ticker, f"{path}[{i}]", hits)


# Fields that mark an entry as a live POSITION record rather than commentary. These carry
# the current invalidation and must never be suppressed as low-priority context: on 2026-W30
# the ORCL position record (invalidation_new "close > $123.50") ranked below three older
# entries still quoting the SUPERSEDED "$144.22" stop, which is precisely the mistake the
# momentum lane made unaided.
POSITION_FIELDS = ("entry_price", "entry_date", "invalidation_new", "hard_exit_deadline",
                   "gross_pnl_pct")


def _is_position(entry: dict) -> bool:
    return any(entry.get(f) not in (None, "") for f in POSITION_FIELDS)


def _summarize(entry: dict) -> tuple[str, bool]:
    """One-line gist of an adjudication + whether it is blocking."""
    bits: list[str] = []
    for k in ("lane", "direction", "tier", "final_size", "verdict", "disposition",
              "fundamentals_verdict", "status"):
        if entry.get(k) not in (None, ""):
            bits.append(f"{k}={entry[k]}")
    blob = json.dumps(entry).lower()
    blocking = any(b in blob for b in BLOCKING)
    for k in ("invalidation_new", "invalidation", "hard_exit_deadline",
              "entry_or_trigger", "note", "action_taken"):
        if entry.get(k):
            txt = str(entry[k])
            bits.append(f"{k}: {txt[:240]}{'...' if len(txt) > 240 else ''}")
            break
    return " | ".join(bits) if bits else "(entry with no verdict fields)", blocking


def lookup(tickers: list[str], days: int) -> dict:
    out: dict[str, list[dict]] = {}
    files = _files(days)  # newest first
    for t in tickers:
        found: list[dict] = []
        for age, p in enumerate(files):
            try:
                with open(p) as fh:
                    doc = json.load(fh)
            except (OSError, json.JSONDecodeError):
                continue
            hits: list[dict] = []
            _walk(doc, t, "$", hits)
            # Free-text mentions (watchlist_write_back, notes) that never name a ticker field.
            # Word-boundary, not substring: a plain `in` match reports "ALLE" inside "STALLED"
            # and "MU" inside "MUCH", which buries the real verdicts in noise.
            word = re.compile(rf"\b{re.escape(t)}\b")
            texts = [s for s in _strings(doc) if word.search(s) and len(s) > 20]
            for h in hits:
                gist, blocking = _summarize(h["entry"])
                found.append({"file": os.path.relpath(p, ROOT), "where": h["where"],
                              "gist": gist, "blocking": blocking, "age": age,
                              "position": _is_position(h["entry"])})
            for s in texts[:3]:
                found.append({"file": os.path.relpath(p, ROOT), "where": "$(free text)",
                              "gist": s[:400] + ("..." if len(s) > 400 else ""),
                              "blocking": any(b in s.lower() for b in BLOCKING),
                              "age": age, "position": False})
        out[t] = found
    return out


def _strings(node) -> list[str]:
    if isinstance(node, str):
        return [node]
    if isinstance(node, dict):
        return [s for v in node.values() for s in _strings(v)]
    if isinstance(node, list):
        return [s for v in node for s in _strings(v)]
    return []


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tickers", required=True, help="comma-separated")
    ap.add_argument("--days", type=int, default=21, help="how far back to sweep (default 21)")
    ap.add_argument("--context", type=int, default=2,
                    help="max non-blocking mentions to show per ticker (default 2)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    tickers = [t.strip().upper() for t in a.tickers.split(",") if t.strip()]
    res = lookup(tickers, a.days)

    if a.json:
        print(json.dumps(res, indent=2))
        return 1 if any(h["blocking"] for v in res.values() for h in v) else 0

    any_block = False
    for t, hits in res.items():
        if not hits:
            print(f"\n{t}: no prior adjudication in the last {a.days}d -- clean")
            continue
        blocking = [h for h in hits if h["blocking"]]
        positions = [h for h in hits if h["position"]]
        any_block = any_block or bool(blocking)
        mark = "  <-- PRIOR BLOCKING VERDICT" if blocking else ""
        if positions:
            mark += "  [HELD POSITION ON RECORD]"
        print(f"\n{t}: {len(hits)} prior mention(s){mark}")
        # Rank: POSITION records first, then blocking verdicts, then other keyed records,
        # then free-text prose -- and NEWEST-FIRST inside every group. Recency has to beat
        # severity within the position group: older entries also carry entry_price, so a
        # blocking-but-stale record would otherwise outrank the current one and re-surface
        # a superseded stop.
        def _rank(h: dict) -> tuple[int, int]:
            if h["position"]:
                grp = 0
            elif h["blocking"]:
                grp = 1
            elif "free text" not in h["where"]:
                grp = 2
            else:
                grp = 3
            return grp, h["age"]

        seen: set[str] = set()
        shown_ctx = 0
        ranked = sorted(hits, key=_rank)
        newest_pos = next((h for h in ranked if h["position"]), None)
        if newest_pos and len(positions) > 1:
            print(f"      NOTE: {len(positions)} position records on file. The one below is the "
                  f"NEWEST ({newest_pos['file']}); older ones may quote a SUPERSEDED invalidation.")
        for h in ranked:
            if h["gist"] in seen:
                continue
            seen.add(h["gist"])
            protected = h["blocking"] or h["position"]
            if not protected:
                shown_ctx += 1
                if shown_ctx > a.context:
                    continue
            flag = "!" if h["blocking"] else ("*" if h["position"] else " ")
            print(f"  {flag} [{h['file']}]")
            print(f"      {h['gist']}")
        extra = max(0, shown_ctx - a.context)
        if extra:
            print(f"    ... {extra} more non-blocking mention(s); --context N to show more")
    if any_block:
        print("\nAt least one name carries a prior blocking verdict. Do not re-score it "
              "without stating what changed.")
    return 1 if any_block else 0


if __name__ == "__main__":
    sys.exit(main())
