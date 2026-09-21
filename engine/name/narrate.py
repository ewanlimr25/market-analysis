"""`make narrate T=<SYMBOL> [DATE=]` (findings/stock-deep-dive DESIGN/70 §6, DECISIONS D13): the one
surviving home of the old skill's qualitative layer, written to `analyses/ticker/<T>/<DATE>/narrate.md`.

It is a facts page, not a verdict: headlines over the trailing 14 days (Finnhub `/company-news`),
analyst changes over the last 10 sessions, Form 4 lines over 30 days, and a fixed
disconfirming-facts checklist read off `ticker.json` (earnings inside the window, borrow decile,
short float, liquidity floor). It cannot change a number: nothing here is read by any module.
Its only effect on the ledger is the `context_read = narrate` stratum on later `disc-1.0` rows for
the same (ticker, date), stamped from this file's mtime (`engine/name/context_tag.py`), which is
how the layer's value is tested (§6) instead of assumed.

The optional model summary D13 mentions is not built: the engine carries no model key, and the test
is about whether the owner decides better after reading the facts, which needs no summary.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date, timedelta
from typing import Callable

from engine import calendar as cal
from engine.config import ANALYSES_TICKER
from engine.name import data_sources as DS
from engine.name.context_tag import NARRATE_FILE, SHEET_FILE

NEWS_DAYS = 14
MAX_HEADLINES = 40
CHECKLIST = ("earnings inside the window", "borrow decile (X2)", "short float (X5)", "liquidity floor (X3)", "premium X1")


def finnhub_news(ticker: str, d: date, key: str | None, *, getter: Callable = DS._http_get_json,
                 days: int = NEWS_DAYS) -> dict:
    """Headlines in `[d - days, d]`; fail-soft `{available, reason, rows: [{date, headline, source, url}]}`."""
    if not key:
        return {"available": False, "reason": "no FINNHUB_API_KEY", "rows": []}
    frm, to = (d - timedelta(days=days)).isoformat(), d.isoformat()
    url = f"https://finnhub.io/api/v1/company-news?symbol={ticker}&from={frm}&to={to}&token={key}"
    try:
        raw = getter(url)
    except Exception as exc:  # network / HTTP / JSON: the page still writes
        return {"available": False, "reason": DS._scrub(str(exc)[:200], key), "rows": []}
    rows = []
    for a in raw if isinstance(raw, list) else []:
        ts = a.get("datetime")
        day = date.fromtimestamp(ts).isoformat() if isinstance(ts, (int, float)) else None
        rows.append({"date": day, "headline": str(a.get("headline") or "")[:200], "source": a.get("source"), "url": a.get("url")})
    rows.sort(key=lambda r: r["date"] or "", reverse=True)
    return {"available": True, "reason": None, "rows": rows[:MAX_HEADLINES]}


def checklist(sheet: dict | None) -> list[str]:
    """The fixed disconfirming-facts lines, each a fact from `ticker.json` or 'no sheet'."""
    if not sheet:
        return [f"- {item}: no sheet for this date (run `make ticker` first)" for item in CHECKLIST]
    ev, pr, fl, lq = sheet["events"]["earnings"], sheet["premium"], sheet["flags"], sheet["liquidity"]
    b, si = fl.get("borrow") or {}, fl.get("si") or {}
    return [
        f"- earnings inside the window: {ev.get('date') or 'unknown'} ({'confirmed' if ev.get('confirmed') else 'NOT confirmed'}, "
        f"{ev.get('days_to') if ev.get('days_to') is not None else '?'} days)",
        f"- borrow decile (X2): {b.get('decile') if b else 'null'} fee {b.get('fee') if b else 'null'} available {b.get('available') if b else 'null'} -> X2 {fl.get('x2')}",
        f"- short float (X5): {si.get('pct_float') if si else 'null'} DTC {si.get('dtc') if si else 'null'} -> X5 {fl.get('x5')}",
        f"- liquidity floor (X3): {'CAN_PRICE' if lq.get('can_price') else 'CANNOT_PRICE ' + str(lq.get('failing'))} "
        f"(contracts {lq.get('contracts')}, hot-chain days {lq.get('hot_chain_days')})",
        f"- premium X1: {pr.get('x1')} (verdict {pr.get('verdict')}, spread_rv5 {pr.get('spread_rv5')})",
    ]


def render(ticker: str, d: date, sheet: dict | None, news: dict, analyst: list[dict], form4: list[dict]) -> str:
    parts = [f"# {ticker} — {d.isoformat()} — narrate (facts only; changes no number)", "",
             "## Disconfirming-facts checklist", *checklist(sheet), "",
             f"## Headlines, last {NEWS_DAYS} days ({'Finnhub' if news['available'] else 'unavailable: ' + str(news['reason'])})"]
    parts += [f"- {r['date'] or '?'} · {r['headline']} ({r['source'] or '?'})" for r in news["rows"]] or ["- none"]
    parts += ["", "## Analyst changes, last 10 sessions"]
    parts += [f"- {a.get('date')} · {a.get('firm')}: {a.get('from') or '?'} -> {a.get('to') or '?'} ({a.get('action')})" for a in analyst] or ["- none"]
    parts += ["", "## Form 4, last 30 days"]
    parts += [f"- {f.get('date')} · {f.get('name')} · {f.get('code')} · {f.get('shares')} @ {f.get('price')}" for f in form4] or ["- none"]
    return "\n".join(parts) + "\n"


def run(ticker: str, d: date, out_root: str = ANALYSES_TICKER, key: str | None = None,
        news_fn: Callable = finnhub_news, analyst_fn: Callable = DS.yf_upgrades_downgrades,
        form4_fn: Callable = DS.finnhub_insider_transactions) -> str:
    key = key or DS.finnhub_key()
    out_dir = os.path.join(out_root, ticker, d.isoformat())
    sheet = None
    sheet_path = os.path.join(out_dir, SHEET_FILE)
    if os.path.exists(sheet_path):
        with open(sheet_path) as fh:
            sheet = json.load(fh)
    news = news_fn(ticker, d, key)
    analyst = analyst_fn(ticker, cal.prev_session(d, 10), d).get("value") or []
    form4 = form4_fn(ticker, d, key).get("value") or []
    text = render(ticker, d, sheet, news, analyst, form4)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, NARRATE_FILE)
    with open(path, "w") as fh:
        fh.write(text)
    return path


def main() -> int:
    ap = argparse.ArgumentParser(description="The qualitative layer for one name and date; writes narrate.md.")
    ap.add_argument("--ticker", required=True)
    ap.add_argument("--date", required=True)
    ap.add_argument("--out-root", default=ANALYSES_TICKER)
    a = ap.parse_args()
    path = run(a.ticker.upper(), cal.parse_date(a.date), a.out_root)
    print(f"narrate: {path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
