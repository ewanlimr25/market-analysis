"""Has Yahoo posted a session's daily close yet? (the nightly agent, scripts/nightly.py; findings DESIGN/120 §10)

Yahoo's chart API keeps a session's daily bar with an empty close until hours after the bell: on 2026-11-20 SPY's and
QQQ's were still empty at 21:29 ET and filled by 21:36. `build_prices.py` skips an empty bar, so a truth set rebuilt
before then stops short of the session, and the last session of a week cannot settle on it (D39, D40). The agent asks
here first, two small requests a sweep, and its night waits until both closes are there or the evening runs out
(nightly.CLOSE_WAIT_UNTIL).
"""
from __future__ import annotations

import json
import time
import urllib.request
from datetime import date

SYMBOLS = ("SPY", "QQQ")  # what S-B and S-C settle on, and what make daily's truth-set check reads
CHART = "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?period1={start}&period2={end}&interval=1d"
TIMEOUT = 25
DAY = 86400


def close_of(symbol: str, day: date) -> float | None:
    """The session's close as Yahoo's daily bars carry it, or None while its bar is empty or missing. Bars are dated
    and asked for exactly as build_prices.py does it (UTC day of the bar; local midnight bounds)."""
    start = int(time.mktime(day.timetuple()))
    url = CHART.format(symbol=symbol, start=start - 3 * DAY, end=start + DAY)
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
        result = json.load(response)["chart"]["result"][0]
    closes = result["indicators"]["quote"][0]["close"]
    for stamp, close in zip(result.get("timestamp") or [], closes):
        if time.strftime("%Y-%m-%d", time.gmtime(stamp)) == day.isoformat():
            return close
    return None


def posted(day: date) -> str:
    """"" once every symbol has the session's close, else why not, for the owner. It raises when Yahoo cannot be
    asked or answers in a shape it does not know: the agent tells that as a failure, never as a quiet wait."""
    missing = [symbol for symbol in SYMBOLS if close_of(symbol, day) is None]
    return f"Yahoo has not posted the close for {' and '.join(missing)} yet" if missing else ""
