#!/usr/bin/env python3
"""Next-session 0DTE premium-selling setup for SPX/SPY (and QQQ, weaker) — the
validated stack from the 2026-05-24 0DTE exploration.

WHAT IS VALIDATED (and what FAILED, so we don't re-introduce it):
  * WHETHER  — the front-expiry implied 1-day move systematically EXCEEDS the
    realized next-day OPEN->CLOSE move (a variance risk premium). An open-entry
    0DTE short straddle ran ~+0.45%/day at 83-97% win; an EOD/overnight entry
    LOSES (the overnight gap eats it). So: sell, but enter at the open.
  * HOW MUCH — EOD 0-45d net GEX predicts next-day intraday RANGE (Barbon &
    Buraschi gamma vol-suppression): long-gamma quieter, short-gamma wider.
    This sets WING WIDTH, not direction.
  * SIZE     — the edge scales with VIX LEVEL (~2x from the low- to high-VIX
    tercile). Scale size up when VIX rich, down/skip when VIX low.
  * WHEN     — enter at/after the open once the gap resolves; never carry
    overnight; hold the 0DTE to the close.
  * DIRECTION — nothing reliable (GEX walls as magnets, charm, vanna, the
    intraday gamma-reversal, and intraday momentum ALL backtested NO_GO). The
    product is DELTA-NEUTRAL premium selling, NOT a directional bet.

ADVISORY, NOT A GUARANTEE. The validation window (2026 Mar-May) contains NO vol
shock, so the short-vol LEFT TAIL is unsampled. Treat the rolling verdict as a
floor, not a promise, and size for the gap-and-trend day that is not in this data.
Rising VIX and front-end backwardation are kept as principled STAND-ASIDE gates
even though this benign sample rewarded selling into them.

DATA: reads the UW EOD parquet directly via duckdb (the intraday tape + per-contract
IV + VIX level it needs are not exposed by the uw-pp CLI). duckdb is an OPTIONAL
dependency — the pure-math core and the unit tests run on stdlib alone; only live
reconstruction needs it (graceful ``available: false`` if absent), like fred_macro.py.

Usage:
    python3 scripts/zerodte_setup.py --symbols SPY,QQQ --days 60 --json
Exit 0 always (see ``available``); 2 = usage error.
"""

from __future__ import annotations

import argparse
import json
import math
import os
from pathlib import Path
from typing import Any

TRADING_DAY = 1.0 / 252.0
DEFAULT_PARQUET_DIR = Path.home() / "Documents" / "Stocks" / "All Options"
# VIX-level → premium-selling size multiplier (edge ~doubles low→high tercile).
SIZE_BY_STATE = {"LOW": 0.5, "MID": 1.0, "HIGH": 1.5}
# front-0DTE-IV / VIX ratio at/above this = front-end backwardation → caution gate.
BACKWARDATION_RATIO = 1.25
# overnight VIX jump (points) at/above this = spiking → stand-aside gate.
VIX_SPIKE = 2.0

# 2026-06-12 audit P1.8 — net-of-cost discipline.
# All PnL in this module is in PERCENT OF UNDERLYING SPOT NOTIONAL (0.8×1σ premium
# captured minus the realized open-to-close move), NOT premium-collected and NOT
# margin-relative. A "+0.30%/day" gross figure is therefore tiny in absolute terms
# and is BEFORE transaction costs. Vilkov (2024) found an unconditional 0DTE iron
# condor flips from +0.77 to −0.20 net Sharpe once a half-spread + fees is charged,
# so the gross win-rate is the wrong promotion metric — net expectancy with a tail
# prior is. ROUND_TRIP_COST_PCT is an ASSUMED round-trip cost (both legs, half-spread
# + fees) in % of underlying for a liquid SPY/QQQ 0DTE ATM straddle; it is a
# placeholder to be calibrated against real fills, not a measured constant.
ROUND_TRIP_COST_PCT = 0.10
PNL_BASIS = (
    "percent-of-underlying-spot-notional, GROSS of transaction costs "
    "(0.8x1sigma premium captured minus realized |open-close|); not premium-collected, not margin-relative"
)


# ---------- pure computation (stdlib only; unit-tested) ---------------------


def implied_move_pct(atm_iv: float) -> float:
    """EOD front-expiry ATM IV → expected 1-trading-day move, in percent."""
    return atm_iv * math.sqrt(TRADING_DAY) * 100.0


def straddle_pnl_pct(implied_move: float, realized_oc: float) -> float:
    """Open-entry 0DTE short straddle held to the close: collect ~0.8×1σ of
    premium, pay the realized |close-open|. Positive = the seller wins."""
    return 0.8 * implied_move - realized_oc


def _mean(xs: list[float]) -> float | None:
    return sum(xs) / len(xs) if xs else None


def _corr(xs: list[float], ys: list[float]) -> float | None:
    pairs = [(x, y) for x, y in zip(xs, ys) if x is not None and y is not None]
    n = len(pairs)
    if n < 4:
        return None
    mx = sum(x for x, _ in pairs) / n
    my = sum(y for _, y in pairs) / n
    cov = sum((x - mx) * (y - my) for x, y in pairs)
    sx = math.sqrt(sum((x - mx) ** 2 for x, _ in pairs))
    sy = math.sqrt(sum((y - my) ** 2 for _, y in pairs))
    return cov / (sx * sy) if sx > 0 and sy > 0 else None


def vix_terciles(vix_values: list[float]) -> tuple[float, float]:
    """(low/mid, mid/high) VIX cut points from the trailing window."""
    vs = sorted(v for v in vix_values if v is not None)
    if len(vs) < 3:
        return (float("nan"), float("nan"))
    t = len(vs) // 3
    return (vs[t], vs[2 * t])


def vol_state(vix: float | None, bounds: tuple[float, float]) -> str:
    if vix is None or any(math.isnan(b) for b in bounds):
        return "UNKNOWN"
    lo, hi = bounds
    return "LOW" if vix < lo else ("HIGH" if vix >= hi else "MID")


def _gex_range_corr(done: list[dict[str, Any]]) -> float | None:
    if not all(s.get("gex_sign") is not None for s in done):
        return None
    c = _corr([s["gex_sign"] for s in done], [s["rng"] for s in done])
    return round(c, 2) if c is not None else None


def evaluate(sessions: list[dict[str, Any]]) -> dict[str, Any]:
    """Rolling out-of-sample backtest over sessions that carry next-day realized
    fields. Each needs: implied_move, oc, rng, cc, vix, gex_sign (+1/-1)."""
    done = [s for s in sessions if s.get("oc") is not None]
    n = len(done)
    if n == 0:
        return {"n": 0, "verdict": "INSUFFICIENT_SAMPLE"}

    pnl_open = [straddle_pnl_pct(s["implied_move"], s["oc"]) for s in done]
    pnl_overnight = [straddle_pnl_pct(s["implied_move"], s["cc"]) for s in done]
    win_open = sum(1 for s in done if s["oc"] < s["implied_move"])

    longs = [s["rng"] for s in done if s.get("gex_sign", 0) > 0]
    shorts = [s["rng"] for s in done if s.get("gex_sign", 0) <= 0]

    bounds = vix_terciles([s["vix"] for s in done if s.get("vix") is not None])
    by_state: dict[str, float | None] = {}
    for st in ("LOW", "MID", "HIGH"):
        ps = [straddle_pnl_pct(s["implied_move"], s["oc"]) for s in done
              if vol_state(s.get("vix"), bounds) == st]
        by_state[st] = _mean(ps)

    mean_open = _mean(pnl_open)
    verdict = (
        "INSUFFICIENT_SAMPLE" if n < 20
        else "GO_PREMIUM_SELL_INTRADAY" if (mean_open and mean_open > 0 and win_open / n >= 0.60)
        else "NO_GO_NO_EDGE"
    )
    mean_open_net = (mean_open - ROUND_TRIP_COST_PCT) if mean_open is not None else None
    return {
        "n": n,
        "premium_sell_win_open_pct": round(100 * win_open / n, 1),
        "mean_pnl_open_pct": round(mean_open, 3) if mean_open is not None else None,
        "mean_pnl_open_net_pct": round(mean_open_net, 3) if mean_open_net is not None else None,
        "round_trip_cost_pct_assumed": ROUND_TRIP_COST_PCT,
        "pnl_basis": PNL_BASIS,
        "mean_pnl_overnight_pct": round(_mean(pnl_overnight), 3) if pnl_overnight else None,
        "worst_day_open_pct": round(min(pnl_open), 3),
        "gex_to_range_corr": _gex_range_corr(done),
        "long_gamma_mean_range_pct": round(_mean(longs), 2) if longs else None,
        "short_gamma_mean_range_pct": round(_mean(shorts), 2) if shorts else None,
        "mean_pnl_by_vix_state": {k: (round(v, 3) if v is not None else None) for k, v in by_state.items()},
        "vix_tercile_bounds": [round(b, 1) if not math.isnan(b) else None for b in bounds],
        "verdict": verdict,
        # 2026-06-12 P1.8: the GO/NO_GO verdict is an ADVISORY win-rate read, NOT a
        # promotion criterion. The lane stays advisory (0 rubric points) permanently
        # until BOTH (a) a vol-shock day enters the sample (the short-vol left tail is
        # currently UNSAMPLED) AND (b) net expectancy (mean_pnl_open_net_pct) clears a
        # tail-aware bar — win-rate alone overstates a negatively-skewed seller's edge.
        "promotion_criterion": "expectancy-with-tail-prior on net PnL; win-rate is NOT a promotion metric (P1.8)",
        "tail_caveat": "Validation sample has no vol shock; short-vol left tail is UNSAMPLED. Net-of-cost mean = mean_pnl_open_net_pct; gross win-rate overstates a negatively-skewed short-vol edge.",
    }


def recommend(latest: dict[str, Any], ctx: dict[str, Any]) -> dict[str, Any]:
    """Per-symbol next-session 0DTE setup from EOD-known features only.

    latest needs: symbol, spot, implied_move, vix, vix_prev, gex_sign,
    front_iv, zero_gamma_level, call_wall, put_wall.
    ctx is an ``evaluate`` result (regime expected-ranges + vix bounds).
    """
    vix = latest.get("vix")
    vix_prev = latest.get("vix_prev")
    bounds = tuple(b if b is not None else float("nan") for b in ctx.get("vix_tercile_bounds", [float("nan"), float("nan")]))
    state = vol_state(vix, bounds)
    long_gamma = (latest.get("gex_sign", 0) > 0)

    expected_range = (ctx.get("long_gamma_mean_range_pct") if long_gamma
                      else ctx.get("short_gamma_mean_range_pct"))

    stand_aside = None
    if vix is not None and vix_prev is not None and (vix - vix_prev) >= VIX_SPIKE:
        stand_aside = f"VIX spiking (+{vix - vix_prev:.1f}) — short-vol left-tail regime; stand aside."
    front_ratio = (latest["front_iv"] / (vix / 100.0)) if (vix and latest.get("front_iv")) else None
    caution = None
    if front_ratio is not None and front_ratio >= BACKWARDATION_RATIO:
        caution = f"Front-end backwardation (0DTE IV {front_ratio:.2f}× VIX) — event/gap risk; half size."

    size = SIZE_BY_STATE.get(state, 1.0)
    if caution:
        size *= 0.5
    if stand_aside:
        size = 0.0

    if long_gamma:
        structure = (f"iron fly / short straddle centred at {latest.get('spot')}, "
                     f"wings ≈ ±{expected_range}% (long-gamma: quieter, mean-reverting)")
    else:
        structure = (f"wider iron condor, wings ≈ ±{expected_range}% "
                     f"(short-gamma: wider range / trendier) — or reduce / stand aside")

    return {
        "symbol": latest["symbol"],
        "sell_premium": bool(size > 0 and not stand_aside),
        "vol_state": state,
        "vix": vix,
        "implied_move_pct": round(latest["implied_move"], 2) if latest.get("implied_move") is not None else None,
        "expected_range_pct": expected_range,
        "size_scalar": round(size, 2),
        "suggested_structure": structure,
        "entry_rule": ("Enter at/after the open once the overnight gap resolves; if it gaps beyond "
                       "the wings, stand aside. Hold the 0DTE to the close — never carry overnight."),
        "stand_aside_reason": stand_aside,
        "caution": caution,
    }


# ---------- duckdb I/O shell (optional dependency; not unit-tested) ---------


def _reconstruct(parquet_dir: Path, symbols: list[str], days: int) -> dict[str, Any] | None:
    """Build per-session feature dicts from the EOD parquet. Returns None if
    duckdb is unavailable or no data — caller emits available:false."""
    try:
        import duckdb  # optional dep — see module docstring
    except ImportError:
        return None
    files = sorted(parquet_dir.glob("bot-eod-report-*.parquet"))[-(days + 1):]
    if len(files) < 2:
        return None
    con = duckdb.connect()

    def dof(f: Path) -> str:
        return f.name.split("bot-eod-report-")[1].replace(".parquet", "")

    def spot_of(f: Path, sym: str):
        r = con.execute(f"SELECT arg_max(underlying_price, executed_at) FROM '{f}' "
                        f"WHERE underlying_symbol='{sym}' AND underlying_price IS NOT NULL").fetchone()
        return r[0] if r and r[0] else None

    def atm_iv(f: Path, sym: str, d: str, spot: float):
        fr = con.execute(f"SELECT min(expiry) FROM '{f}' WHERE underlying_symbol='{sym}' "
                         f"AND expiry IS NOT NULL AND date_diff('day',DATE '{d}',expiry)>=1 "
                         f"AND implied_volatility>0").fetchone()[0]
        if fr is None:
            return None
        q = (f"WITH b AS (SELECT strike,option_type,implied_volatility iv, "
             f"row_number() OVER (PARTITION BY strike,option_type ORDER BY executed_at DESC) rn "
             f"FROM '{f}' WHERE underlying_symbol='{sym}' AND expiry=DATE '{fr}' AND implied_volatility>0) "
             f"SELECT iv FROM b WHERE rn=1 ORDER BY abs(strike-{spot}) LIMIT 6")
        ivs = [r[0] for r in con.execute(q).fetchall()]
        return sum(ivs) / len(ivs) if ivs else None

    def gex_sign(f: Path, sym: str):
        q = (f"WITH b AS (SELECT option_type,gamma,open_interest, "
             f"row_number() OVER (PARTITION BY strike,option_type,expiry ORDER BY executed_at DESC) rn "
             f"FROM '{f}' WHERE underlying_symbol='{sym}' AND gamma>0 AND open_interest>0 "
             f"AND date_diff('day',(SELECT max(CAST(executed_at AS DATE)) FROM '{f}'),expiry) BETWEEN 0 AND 45) "
             f"SELECT sum(CASE WHEN option_type='put' THEN -gamma*open_interest ELSE gamma*open_interest END) "
             f"FROM b WHERE rn=1")
        r = con.execute(q).fetchone()
        return (1 if r[0] > 0 else -1) if (r and r[0] is not None) else None

    def oc_range(f: Path, sym: str):
        q = (f"WITH r AS (SELECT underlying_price up, executed_at, "
             f"(extract('hour' FROM executed_at AT TIME ZONE 'America/New_York')*60 "
             f"+ extract('minute' FROM executed_at AT TIME ZONE 'America/New_York')) tod "
             f"FROM '{f}' WHERE underlying_symbol='{sym}' AND underlying_price IS NOT NULL) "
             f"SELECT arg_min(up,executed_at) o, arg_max(up,executed_at) c, max(up) hi, min(up) lo "
             f"FROM r WHERE tod>=570 AND tod<960")
        r = con.execute(q).fetchone()
        return dict(o=r[0], c=r[1], hi=r[2], lo=r[3]) if r and r[0] else None

    per_symbol_sessions: dict[str, list[dict]] = {s: [] for s in symbols}
    per_symbol_latest: dict[str, dict] = {}
    for i, f in enumerate(files):
        d = dof(f)
        vix = spot_of(f, "VIX")
        vix_prev = spot_of(files[i - 1], "VIX") if i > 0 else None
        for sym in symbols:
            spot = spot_of(f, sym)
            if not spot:
                continue
            iv = atm_iv(f, sym, d, spot)
            if iv is None:
                continue
            gs = gex_sign(f, sym)
            feat = {"date": d, "symbol": sym, "spot": round(spot, 2), "front_iv": iv,
                    "implied_move": implied_move_pct(iv), "vix": vix, "vix_prev": vix_prev,
                    "gex_sign": gs}
            if i < len(files) - 1:  # has a next session → realized fields for the backtest
                oh = oc_range(files[i + 1], sym)
                if oh:
                    feat.update(oc=100 * abs(oh["c"] - oh["o"]) / oh["o"],
                                rng=100 * (oh["hi"] - oh["lo"]) / oh["o"],
                                cc=100 * abs(oh["c"] - spot) / spot)
                    per_symbol_sessions[sym].append(feat)
            else:
                per_symbol_latest[sym] = feat  # newest EOD → the setup is for ITS next session
    return {"sessions": per_symbol_sessions, "latest": per_symbol_latest,
            "as_of": dof(files[-1])}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--symbols", default="SPY,QQQ")
    ap.add_argument("--days", type=int, default=60)
    ap.add_argument("--parquet-dir", default=str(os.environ.get("UW_PARQUET_DIR", DEFAULT_PARQUET_DIR)))
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    symbols = [s.strip().upper() for s in args.symbols.split(",") if s.strip()]

    data = _reconstruct(Path(args.parquet_dir), symbols, args.days)
    if data is None:
        out = {"available": False, "reason": "duckdb unavailable or no parquet data "
               f"in {args.parquet_dir} (the live reconstruction needs duckdb + the EOD export)"}
        print(json.dumps(out) if args.json else out["reason"])
        return 0

    backtest = {sym: evaluate(sess) for sym, sess in data["sessions"].items()}
    setup = {sym: recommend(data["latest"][sym], backtest.get(sym, {}))
             for sym in symbols if sym in data["latest"] and backtest.get(sym, {}).get("n")}
    payload = {"available": True, "as_of": data["as_of"], "symbols": symbols,
               "backtest": backtest, "setup": setup,
               "note": ("ADVISORY delta-neutral premium-selling. SPY≈SPX (validated identical); "
                        "QQQ weaker (Nasdaq index book unavailable). No vol shock in sample → tail unsampled.")}
    if args.json:
        print(json.dumps(payload, indent=2))
        return 0
    print(f"0DTE premium-selling setup — as of EOD {data['as_of']}")
    for sym in symbols:
        bt = backtest.get(sym, {})
        print(f"\n[{sym}] backtest n={bt.get('n')} verdict={bt.get('verdict')} | "
              f"open-entry win {bt.get('premium_sell_win_open_pct')}% mean {bt.get('mean_pnl_open_pct')}%/day "
              f"(overnight {bt.get('mean_pnl_overnight_pct')}%/day) | "
              f"long-γ range {bt.get('long_gamma_mean_range_pct')}% vs short-γ {bt.get('short_gamma_mean_range_pct')}%")
        s = setup.get(sym)
        if s:
            print(f"   SETUP: sell_premium={s['sell_premium']} vol_state={s['vol_state']} size×{s['size_scalar']} "
                  f"| {s['suggested_structure']}")
            if s["stand_aside_reason"]:
                print(f"   STAND ASIDE: {s['stand_aside_reason']}")
            elif s["caution"]:
                print(f"   CAUTION: {s['caution']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
