#!/usr/bin/env python3
"""Finnhub fundamentals enrichment for the Phase-1.5 fundamentals gate.

Pulls free-tier Finnhub endpoints for ONE ticker and emits a single JSON
object on stdout that the ``fundamentals-gate`` agent consumes to confirm,
caution, or veto a flow-driven conviction call. The script is intentionally
**direction-agnostic** — it surfaces facts and splits them into bullish /
bearish / caution buckets; the agent cross-references the trade thesis
direction to decide CONFIRM / CAUTION / VETO.

Endpoints (all Finnhub free tier):
  /stock/metric?metric=all   valuation + quality + leverage ratios
  /stock/earnings            trailing EPS-surprise history (beat/miss streak)
  /stock/insider-sentiment   MSPR (insider buy/sell pressure, -100..+100)
  /company-news              catalyst stack over the lookback window
  /calendar/earnings         next scheduled earnings date (event risk)

Look-ahead guard: every dated record is filtered to ``<= --date``.

Usage:
    python3 scripts/finnhub_enrich.py --ticker NVDA --date 2026-05-23 [--lookback 14]

Exit code: always 0. When the key is missing or the ticker is non-US the
script still prints a valid JSON object with ``available=false`` and a
``skip_reason`` so the calling agent never parses an empty payload.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from _env import get_key  # noqa: E402

BASE_URL = "https://finnhub.io/api/v1"
TIMEOUT_SECONDS = 30
MAX_NEWS = 15

# (finnhub_metric_key, output_key)
METRIC_KEYS = [
    ("peBasicExclExtraTTM", "pe_ttm"),
    ("psAnnual", "ps"),
    ("pbAnnual", "pb"),
    ("pegRatio", "peg"),
    ("roeTTM", "roe_ttm"),
    ("roaTTM", "roa_ttm"),
    ("grossMarginTTM", "gross_margin_ttm"),
    ("operatingMarginTTM", "operating_margin_ttm"),
    ("netProfitMarginTTM", "net_margin_ttm"),
    ("revenueGrowthTTMYoy", "rev_growth_yoy"),
    ("epsGrowthTTMYoy", "eps_growth_yoy"),
    ("currentRatioAnnual", "current_ratio"),
    ("totalDebt/totalEquityAnnual", "debt_to_equity"),
    ("dividendYieldIndicatedAnnual", "dividend_yield"),
    ("beta", "beta"),
    ("52WeekHigh", "high_52w"),
    ("52WeekLow", "low_52w"),
]


class FinnhubError(RuntimeError):
    """Non-transient Finnhub failure (4xx other than 429, or network)."""


class FinnhubPremiumError(FinnhubError):
    """HTTP 403 — endpoint requires a paid Finnhub plan."""


def is_us_ticker(ticker: str) -> bool:
    """Finnhub free tier is US-equity-focused; suffix tickers (.TO, .L) are not covered."""
    return "." not in ticker


def _http_get_json(url: str) -> object:
    """One HTTP GET returning parsed JSON. Raises typed errors.

    Isolated so tests can monkeypatch it without touching the network.
    """
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "uw-daily-analysis/1.0"})
        with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:  # pragma: no cover - network path
        if exc.code == 403:
            raise FinnhubPremiumError(f"403 from {url}") from exc
        raise FinnhubError(f"HTTP {exc.code} from Finnhub: {exc.reason}") from exc
    except (urllib.error.URLError, ValueError, TimeoutError) as exc:  # pragma: no cover
        raise FinnhubError(f"Finnhub request failed: {exc}") from exc


def finnhub_get(path: str, params: dict, key: str, getter=_http_get_json) -> object:
    """GET a Finnhub endpoint with the token appended."""
    query = urllib.parse.urlencode({**params, "token": key})
    return getter(f"{BASE_URL}{path}?{query}")


# ---------- pure transforms --------------------------------------------------


def summarize_metrics(resp: object) -> dict:
    """Extract the tracked ratios from a /stock/metric response."""
    metric = resp.get("metric", {}) if isinstance(resp, dict) else {}
    out: dict = {}
    for src_key, out_key in METRIC_KEYS:
        val = metric.get(src_key)
        if isinstance(val, (int, float)):
            out[out_key] = val
    return out


def summarize_earnings(rows: object, as_of: str) -> list[dict]:
    """Trailing EPS-surprise rows with period <= as_of, newest first, max 8."""
    if not isinstance(rows, list):
        return []
    clean = [
        {
            "period": r.get("period", ""),
            "actual": r.get("actual"),
            "estimate": r.get("estimate"),
            "surprise_pct": r.get("surprisePercent"),
        }
        for r in rows
        if isinstance(r, dict) and str(r.get("period", "")) <= as_of
    ]
    clean.sort(key=lambda r: str(r["period"]), reverse=True)
    return clean[:8]


def summarize_insider(resp: object, as_of: str) -> list[dict]:
    """Insider MSPR rows with (year, month) <= as_of, oldest first."""
    rows = resp.get("data", []) if isinstance(resp, dict) else []
    as_of_dt = datetime.strptime(as_of, "%Y-%m-%d")
    clean = []
    for r in rows:
        if not isinstance(r, dict):
            continue
        year, month = r.get("year"), r.get("month")
        if not (isinstance(year, int) and isinstance(month, int)):
            continue
        if datetime(year, month, 1) > as_of_dt:
            continue
        clean.append({
            "year": year,
            "month": month,
            "mspr": r.get("mspr"),
            "change": r.get("change"),
        })
    clean.sort(key=lambda r: (r["year"], r["month"]))
    return clean


def summarize_news(articles: object, as_of: str) -> list[dict]:
    """Catalyst stack: headlines at/<= as_of, newest first, max MAX_NEWS."""
    if not isinstance(articles, list):
        return []
    as_of_epoch = int(datetime.strptime(as_of, "%Y-%m-%d").timestamp()) + 86400
    clean = []
    for a in articles:
        if not isinstance(a, dict):
            continue
        ts = a.get("datetime")
        if isinstance(ts, (int, float)) and ts > as_of_epoch:
            continue
        clean.append({
            "_ts": int(ts) if isinstance(ts, (int, float)) else -1,
            "datetime": (
                datetime.fromtimestamp(int(ts), tz=timezone.utc).strftime("%Y-%m-%d %H:%M")
                if isinstance(ts, (int, float)) else None
            ),
            "headline": a.get("headline", ""),
            "source": a.get("source", ""),
            "summary": (a.get("summary", "") or "")[:280],
            "url": a.get("url", ""),
        })
    clean.sort(key=lambda a: a["_ts"], reverse=True)
    for a in clean:
        del a["_ts"]
    return clean[:MAX_NEWS]


def next_earnings_date(resp: object, as_of: str) -> str | None:
    """Earliest scheduled earnings date >= as_of from /calendar/earnings."""
    cal = resp.get("earningsCalendar", []) if isinstance(resp, dict) else []
    dates = sorted(
        str(e.get("date", "")) for e in cal
        if isinstance(e, dict) and str(e.get("date", "")) >= as_of
    )
    return dates[0] if dates else None


def assess(metrics: dict, earnings: list[dict], insider: list[dict],
           earnings_date: str | None, as_of: str) -> dict:
    """Compute direction-agnostic fundamentals signals + bull/bear/caution buckets."""
    bullish: list[str] = []
    bearish: list[str] = []
    caution: list[str] = []

    # --- earnings-surprise trend (last 4 reported quarters) ---
    recent = [e["surprise_pct"] for e in earnings[:4] if isinstance(e.get("surprise_pct"), (int, float))]
    beats = sum(1 for s in recent if s > 0)
    misses = sum(1 for s in recent if s < 0)
    if recent and beats >= 3:
        earnings_trend = "beat_streak"
        bullish.append(f"{beats}/{len(recent)} recent EPS beats")
    elif recent and misses >= 3:
        earnings_trend = "miss_streak"
        bearish.append(f"{misses}/{len(recent)} recent EPS misses")
    else:
        earnings_trend = "mixed" if recent else "unknown"

    # --- imminent earnings (event risk) ---
    days_to_earnings = None
    if earnings_date:
        try:
            days_to_earnings = (
                datetime.strptime(earnings_date, "%Y-%m-%d")
                - datetime.strptime(as_of, "%Y-%m-%d")
            ).days
            if 0 <= days_to_earnings <= 10:
                caution.append(f"earnings in {days_to_earnings}d ({earnings_date}) — event risk")
        except ValueError:
            days_to_earnings = None

    # --- insider MSPR (last 3 reported months) ---
    msprs = [r["mspr"] for r in insider[-3:] if isinstance(r.get("mspr"), (int, float))]
    mspr_avg = round(sum(msprs) / len(msprs), 2) if msprs else None
    if mspr_avg is None:
        insider_signal = "unknown"
    elif mspr_avg >= 20:
        insider_signal = "buying"
        bullish.append(f"insider MSPR +{mspr_avg} (net buying)")
    elif mspr_avg <= -20:
        insider_signal = "selling"
        bearish.append(f"insider MSPR {mspr_avg} (net selling)")
        if mspr_avg <= -30:
            caution.append(f"strong insider selling (MSPR {mspr_avg})")
    else:
        insider_signal = "neutral"

    # --- leverage ---
    dte = metrics.get("debt_to_equity")
    if isinstance(dte, (int, float)):
        if dte > 200:
            leverage_flag = "elevated"
            caution.append(f"high leverage (D/E {dte})")
        elif dte > 100:
            leverage_flag = "moderate"
        else:
            leverage_flag = "low"
    else:
        leverage_flag = "unknown"

    # --- growth / margins ---
    rev_growth = metrics.get("rev_growth_yoy")
    if isinstance(rev_growth, (int, float)):
        if rev_growth < 0:
            bearish.append(f"negative revenue growth ({rev_growth}% YoY)")
        elif rev_growth > 15:
            bullish.append(f"strong revenue growth (+{rev_growth}% YoY)")
    net_margin = metrics.get("net_margin_ttm")
    if isinstance(net_margin, (int, float)) and net_margin < 0:
        bearish.append(f"unprofitable (net margin {net_margin}%)")

    return {
        "earnings_trend": earnings_trend,
        "insider_signal": insider_signal,
        "insider_mspr_3mo_avg": mspr_avg,
        "leverage_flag": leverage_flag,
        "next_earnings_date": earnings_date,
        "days_to_earnings": days_to_earnings,
        "bullish_factors": bullish,
        "bearish_factors": bearish,
        "caution_flags": caution,
    }


# ---------- orchestration ----------------------------------------------------


def _try(label: str, fn, errors: list[str]):
    """Run fn(); record premium/error and return None on failure."""
    try:
        return fn()
    except FinnhubPremiumError:
        errors.append(f"{label}: requires paid plan")
    except FinnhubError as exc:
        errors.append(f"{label}: {exc}")
    return None


def enrich(ticker: str, as_of: str, lookback: int, key: str, getter=_http_get_json) -> dict:
    """Fetch all endpoints and assemble the enrichment payload for one ticker."""
    sym = ticker.upper()
    errors: list[str] = []

    metric_resp = _try("metrics", lambda: finnhub_get("/stock/metric", {"symbol": sym, "metric": "all"}, key, getter), errors)
    earnings_resp = _try("earnings", lambda: finnhub_get("/stock/earnings", {"symbol": sym, "limit": 8}, key, getter), errors)
    insider_resp = _try("insider", lambda: finnhub_get("/stock/insider-sentiment", {"symbol": sym, "from": _from(as_of, 365), "to": as_of}, key, getter), errors)
    news_resp = _try("news", lambda: finnhub_get("/company-news", {"symbol": sym, "from": _from(as_of, lookback), "to": as_of}, key, getter), errors)
    cal_resp = _try("earnings_calendar", lambda: finnhub_get("/calendar/earnings", {"symbol": sym, "from": as_of, "to": _from(as_of, -90)}, key, getter), errors)

    metrics = summarize_metrics(metric_resp) if metric_resp is not None else {}
    earnings = summarize_earnings(earnings_resp, as_of) if earnings_resp is not None else []
    insider = summarize_insider(insider_resp, as_of) if insider_resp is not None else []
    news = summarize_news(news_resp, as_of) if news_resp is not None else []
    earnings_date = next_earnings_date(cal_resp, as_of) if cal_resp is not None else None

    return {
        "ticker": sym,
        "as_of": as_of,
        "available": True,
        "metrics": metrics,
        "earnings_surprises": earnings,
        "insider_mspr": insider,
        "news": news,
        "assessment": assess(metrics, earnings, insider, earnings_date, as_of),
        "errors": errors,
    }


def _from(curr_date: str, lookback_days: int) -> str:
    """YYYY-MM-DD ``lookback_days`` before curr_date (negative = after)."""
    dt = datetime.strptime(curr_date, "%Y-%m-%d") - timedelta(days=lookback_days)
    return dt.strftime("%Y-%m-%d")


def main() -> None:
    parser = argparse.ArgumentParser(description="Finnhub fundamentals enrichment as JSON")
    parser.add_argument("--ticker", required=True)
    parser.add_argument("--date", required=True, help="As-of date YYYY-MM-DD")
    parser.add_argument("--lookback", type=int, default=14, help="Days of news history")
    args = parser.parse_args()

    try:
        datetime.strptime(args.date, "%Y-%m-%d")
    except ValueError:
        print(json.dumps({"ticker": args.ticker.upper(), "available": False,
                          "skip_reason": f"invalid --date {args.date!r}, expected YYYY-MM-DD"}))
        return

    if not is_us_ticker(args.ticker):
        print(json.dumps({"ticker": args.ticker.upper(), "as_of": args.date, "available": False,
                          "skip_reason": "non-US ticker not covered by Finnhub free tier"}))
        return

    key = get_key("FINNHUB_API_KEY")
    if not key:
        print(json.dumps({"ticker": args.ticker.upper(), "as_of": args.date, "available": False,
                          "skip_reason": "FINNHUB_API_KEY not set (env, repo .env, or sibling claude-trading-agents/.env)"}))
        return

    print(json.dumps(enrich(args.ticker, args.date, args.lookback, key)))


if __name__ == "__main__":
    main()
