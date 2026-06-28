#!/usr/bin/env python3
"""FRED macro snapshot for the daily / weekly Step-0 shared context.

Pulls the last N observations of ~12 core macro series from the FRED JSON
API (``api.stlouisfed.org`` — the chart-CSV hosts are CDN-blocked) and emits
a compact JSON block on stdout: latest prints, recent deltas, and derived
regime signals (yield-curve sign, inflation trend, USD direction).

The orchestrator feeds this into the Step-0 context as ``macro_snapshot`` and
pairs it with a reasoning/WebSearch-built forward catalyst calendar to derive
``event_risk``. FRED has no forward-calendar endpoint, so this script reports
the macro *state* only — forward event *timing* is assembled upstream.

Usage:
    python3 scripts/fred_macro.py [--limit 14]

Exit code: always 0. Without ``FRED_API_KEY`` it prints ``available=false``
plus a ``skip_reason`` so Step 0 can fall back to WebSearch / risk_market_regime.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from _env import get_key  # noqa: E402

BASE_URL = "https://api.stlouisfed.org/fred/series/observations"
TIMEOUT_SECONDS = 30

# (series_id, label, cadence, transform)
#   transform ∈ {yoy, mom_level, level, level_sign, delta30}
SERIES: list[tuple[str, str, str, str]] = [
    ("CPIAUCSL", "CPI (all urban)", "monthly", "yoy"),
    ("CPILFESL", "Core CPI", "monthly", "yoy"),
    ("PCEPI", "PCE", "monthly", "yoy"),
    ("PCEPILFE", "Core PCE", "monthly", "yoy"),
    ("PAYEMS", "Nonfarm payrolls (000s)", "monthly", "mom_level"),
    ("UNRATE", "Unemployment rate", "monthly", "level"),
    ("DFF", "Fed funds (effective)", "daily", "level"),
    ("DGS10", "10Y Treasury yield", "daily", "delta30"),
    ("DGS2", "2Y Treasury yield", "daily", "delta30"),
    ("T10Y2Y", "10Y-2Y spread", "daily", "level_sign"),
    ("DTWEXBGS", "Broad USD index", "daily", "delta30"),
    ("SOFR", "SOFR", "daily", "level"),
]


class FredError(RuntimeError):
    """Non-transient FRED API failure."""


def _http_get_json(url: str) -> dict:
    """One HTTP GET returning parsed JSON. Raises FredError on failure.

    Isolated so tests can monkeypatch it without touching the network.
    """
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "uw-daily-analysis/1.0"})
        with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:  # pragma: no cover - network path
        raise FredError(f"HTTP {exc.code} from FRED: {exc.reason}") from exc
    except (urllib.error.URLError, ValueError, TimeoutError) as exc:  # pragma: no cover
        raise FredError(f"FRED request failed: {exc}") from exc


def fetch_series(series_id: str, key: str, limit: int, getter=_http_get_json) -> list[dict]:
    """Fetch the latest ``limit`` observations for one FRED series (desc order)."""
    params = urllib.parse.urlencode(
        {
            "series_id": series_id,
            "api_key": key,
            "file_type": "json",
            "sort_order": "desc",
            "limit": limit,
        }
    )
    payload = getter(f"{BASE_URL}?{params}")
    obs = payload.get("observations", []) if isinstance(payload, dict) else []
    return [o for o in obs if isinstance(o, dict)]


def _valid_points(observations: list[dict]) -> list[tuple[str, float]]:
    """Return ``[(date, value)]`` skipping FRED's ``"."`` missing marker, desc order."""
    points: list[tuple[str, float]] = []
    for o in observations:
        raw = str(o.get("value", "")).strip()
        if raw in ("", "."):
            continue
        try:
            points.append((str(o.get("date", "")), float(raw)))
        except ValueError:
            continue
    return points


def _value_n_days_back(points: list[tuple[str, float]], days: int) -> tuple[str, float] | None:
    """First (date, value) at least ``days`` calendar days before the latest point."""
    if not points:
        return None
    latest_date = datetime.strptime(points[0][0], "%Y-%m-%d")
    cutoff = latest_date - timedelta(days=days)
    for date_str, value in points[1:]:
        if datetime.strptime(date_str, "%Y-%m-%d") <= cutoff:
            return date_str, value
    return None


def summarize_series(series_id: str, label: str, cadence: str, transform: str,
                     observations: list[dict]) -> dict:
    """Reduce raw observations to one structured reading for the snapshot."""
    points = _valid_points(observations)
    if not points:
        return {"series_id": series_id, "label": label, "available": False}

    latest_date, latest = points[0]
    out: dict = {
        "series_id": series_id,
        "label": label,
        "cadence": cadence,
        "available": True,
        "as_of": latest_date,
        "latest": round(latest, 4),
    }

    if transform == "yoy" and len(points) >= 13:
        year_ago = points[12][1]
        if year_ago:
            out["yoy_pct"] = round((latest - year_ago) / year_ago * 100, 2)
    elif transform == "mom_level" and len(points) >= 2:
        out["mom_change"] = round(latest - points[1][1], 1)
    elif transform == "delta30":
        prior = _value_n_days_back(points, 30)
        if prior:
            out["delta_30d"] = round(latest - prior[1], 4)
            out["value_30d_ago"] = round(prior[1], 4)
    elif transform == "level_sign":
        out["sign"] = "inverted" if latest < 0 else ("flat" if abs(latest) < 0.05 else "normal")

    return out


def derive_signals(readings: dict[str, dict]) -> dict:
    """Compute desk-readable regime signals from the per-series readings."""
    signals: dict = {}

    curve = readings.get("T10Y2Y", {})
    if curve.get("available"):
        signals["yield_curve"] = curve.get("sign", "unknown")
        signals["yield_curve_10y2y"] = curve.get("latest")

    core_cpi = readings.get("CPILFESL", {})
    if "yoy_pct" in core_cpi:
        signals["core_cpi_yoy_pct"] = core_cpi["yoy_pct"]
    core_pce = readings.get("PCEPILFE", {})
    if "yoy_pct" in core_pce:
        signals["core_pce_yoy_pct"] = core_pce["yoy_pct"]

    unrate = readings.get("UNRATE", {})
    if unrate.get("available"):
        signals["unemployment_rate"] = unrate.get("latest")
    payems = readings.get("PAYEMS", {})
    if "mom_change" in payems:
        signals["payrolls_mom_000s"] = payems["mom_change"]

    dgs10 = readings.get("DGS10", {})
    if dgs10.get("available"):
        signals["ten_year_yield"] = dgs10.get("latest")
        if "delta_30d" in dgs10:
            signals["ten_year_30d_direction"] = (
                "rising" if dgs10["delta_30d"] > 0.05
                else "falling" if dgs10["delta_30d"] < -0.05
                else "flat"
            )

    usd = readings.get("DTWEXBGS", {})
    if "delta_30d" in usd:
        signals["usd_30d_direction"] = (
            "strengthening" if usd["delta_30d"] > 0
            else "weakening" if usd["delta_30d"] < 0
            else "flat"
        )

    dff = readings.get("DFF", {})
    if dff.get("available"):
        signals["fed_funds"] = dff.get("latest")

    return signals


def build_snapshot(key: str, limit: int, getter=_http_get_json) -> dict:
    """Fetch all series and assemble the macro snapshot dict."""
    readings: dict[str, dict] = {}
    errors: list[str] = []
    for series_id, label, cadence, transform in SERIES:
        # Daily series need a wider window to compute a 30-day delta.
        n = max(limit, 45) if cadence == "daily" else max(limit, 14)
        try:
            obs = fetch_series(series_id, key, n, getter=getter)
            readings[series_id] = summarize_series(series_id, label, cadence, transform, obs)
        except FredError as exc:
            readings[series_id] = {"series_id": series_id, "label": label, "available": False}
            errors.append(f"{series_id}: {exc}")

    return {
        "source": "FRED",
        "available": True,
        "retrieved": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "signals": derive_signals(readings),
        "series": readings,
        "errors": errors,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch a FRED macro snapshot as JSON")
    parser.add_argument("--limit", type=int, default=14, help="Observations per series")
    args = parser.parse_args()

    key = get_key("FRED_API_KEY")
    if not key:
        print(json.dumps({
            "source": "FRED",
            "available": False,
            "skip_reason": "FRED_API_KEY not set (env, repo .env, or sibling). "
                           "Register a free key at https://fred.stlouisfed.org/docs/api/api_key.html",
        }))
        return

    print(json.dumps(build_snapshot(key, args.limit)))


if __name__ == "__main__":
    main()
