#!/usr/bin/env python3
"""Did the OI build survive its own catalyst, or was it just pre-print positioning?

`earnings_gate.py` looks FORWARD -- it asks whether a print lands inside the coming horizon.
It is structurally blind to a catalyst that already landed INSIDE the trailing build window,
so a name whose call-OI accumulation was pre-print positioning that has already paid off will
sail through the gate while being completely signal-dead.

That is the SSNC case (2026-W30). SSNC ranked top of the OI_FADE screen at oi_rel_build 2.493
and PASSED `earnings_gate.py --horizon 21` cleanly, because its next print was 2026-10-22. But
its entire build (+335/+3,070/+731 on 07-20/21/22) landed BEFORE its 07-23 after-close print,
then went +0 and +1 while the stock gapped +10.35%. The crowd was right and had already been
paid; there was nothing left to fade. Persistence does not catch this -- persistence measures
day-concentration, not catalyst timing.

The discriminator is whether the build CONTINUED past the print:
  SSNC  post-catalyst net    +1  of +4,113  (0.0%)  -> RESOLVED, do not fade
  ALLE  post-catalyst net +1,533 of +4,308 (35.6%)  -> LIVE, still a crowd

The past catalyst date is recovered by reading `next_earnings_date` from the screener panel as
it stood at the START of the window -- the forward-looking field, read from the past.

Fails CLOSED: if the window-start panel is missing or the ticker is absent, the verdict is
UNKNOWN and is treated as blocking, never as a clean pass.

Usage:
  python3 scripts/catalyst_split.py --tickers SSNC,ALLE --date 2026-07-24 --days 10
  python3 scripts/catalyst_split.py --tickers SSNC --date 2026-07-24 --days 10 --json
"""
from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from oi_build import build as oi_build_series  # noqa: E402

STOCKS = os.path.expanduser("~/Documents/Stocks")

# A build with less than this share of its net accruing AFTER the catalyst is treated as
# resolved pre-print positioning rather than a live crowd.
LIVE_POST_SHARE = 0.15


def _screener(date: str) -> str | None:
    p = f"{STOCKS}/Stock Screener/stock-screener-{date}.parquet"
    return p if os.path.exists(p) else None


def _earnings_asof(tickers: list[str], asof: str) -> dict[str, str | None]:
    """next_earnings_date as the screener saw it on `asof` -- i.e. a forward field read
    from the past, which is how a catalyst that has since occurred is recovered."""
    path = _screener(asof)
    if path is None:
        return {}
    import duckdb
    names = ",".join(f"'{t.upper()}'" for t in tickers)
    rows = duckdb.connect().execute(
        f"""SELECT ticker, any_value(next_earnings_date) FROM read_parquet('{path}')
            WHERE ticker IN ({names}) GROUP BY ticker""").fetchall()
    return {r[0]: (r[1].isoformat() if r[1] else None) for r in rows}


def split(tickers: list[str], date: str, days: int) -> dict:
    res = oi_build_series(tickers, date, days)
    out: dict[str, dict] = {}

    # Window start = earliest day the build series actually covers.
    starts = [v["daily"][0]["date"] for v in res.values() if v.get("daily")]
    window_start = min(starts) if starts else date
    asof = _earnings_asof(tickers, window_start)

    for t in (x.upper() for x in tickers):
        v = res.get(t)
        if not v or not v.get("daily"):
            out[t] = {"verdict": "UNKNOWN", "reason": "no OI build series -- fail closed",
                      "catalyst": None}
            continue
        daily = v["daily"]
        if t not in asof:
            out[t] = {"verdict": "UNKNOWN", "catalyst": None,
                      "reason": f"ticker absent from the {window_start} screener panel -- fail closed",
                      "net_total": v.get("net")}
            continue

        cat = asof[t]
        net_total = sum(d["call_net"] - d["put_net"] for d in daily)
        if cat is None or not (window_start <= cat <= date):
            out[t] = {"verdict": "NO_CATALYST_IN_WINDOW", "catalyst": cat,
                      "window": [window_start, date], "net_total": net_total,
                      "reason": f"no earnings inside the {days}d build window "
                                f"({window_start}..{date}); forward gate governs"}
            continue

        pre = sum(d["call_net"] - d["put_net"] for d in daily if d["date"] < cat)
        post = sum(d["call_net"] - d["put_net"] for d in daily if d["date"] >= cat)
        share = (post / net_total) if net_total else 0.0
        live = share >= LIVE_POST_SHARE
        out[t] = {
            "verdict": "LIVE_BUILD" if live else "RESOLVED_PRE_PRINT",
            "catalyst": cat, "window": [window_start, date],
            "net_total": net_total, "pre_catalyst_net": pre, "post_catalyst_net": post,
            "post_share": round(share, 4),
            "reason": (f"{post:+,} of {net_total:+,} ({share:.1%}) accrued on/after the {cat} "
                       f"print -- build {'CONTINUED past' if live else 'DIED at'} its catalyst"),
        }
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tickers", required=True, help="comma-separated")
    ap.add_argument("--date", required=True, help="as-of date YYYY-MM-DD")
    ap.add_argument("--days", type=int, default=10, help="build window in trading days (default 10)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    tickers = [t.strip().upper() for t in a.tickers.split(",") if t.strip()]
    res = split(tickers, a.date, a.days)

    if a.json:
        print(json.dumps(res, indent=2))
    else:
        print(f"catalyst-in-build-window check, {a.days}d window ending {a.date}\n")
        for t, v in res.items():
            mark = {"LIVE_BUILD": "LIVE    ", "RESOLVED_PRE_PRINT": "RESOLVED",
                    "NO_CATALYST_IN_WINDOW": "no-cat  ", "UNKNOWN": "UNKNOWN "}[v["verdict"]]
            print(f"  {mark} {t:8s} {v['reason']}")
        resolved = [t for t, v in res.items() if v["verdict"] == "RESOLVED_PRE_PRINT"]
        unknown = [t for t, v in res.items() if v["verdict"] == "UNKNOWN"]
        if resolved:
            print(f"\nDo not fade: {', '.join(resolved)} -- the build did not survive its catalyst.")
        if unknown:
            print(f"\nCould not evaluate: {', '.join(unknown)} -- treated as blocking (fail closed), "
                  "which is NOT the same as a resolved build. Check the panel before overriding.")
    return 1 if any(v["verdict"] in ("RESOLVED_PRE_PRINT", "UNKNOWN") for v in res.values()) else 0


if __name__ == "__main__":
    sys.exit(main())
