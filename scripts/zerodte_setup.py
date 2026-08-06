#!/usr/bin/env python3
"""Next-session 0DTE premium-selling setup for SPX/SPY (and QQQ, weaker) — the
validated stack from the 2026-05-24 0DTE exploration.

WHAT IS VALIDATED (and what FAILED, so we don't re-introduce it):
  * WHETHER  — the front-expiry implied 1-day move systematically EXCEEDS the
    realized next-day OPEN->CLOSE move (a variance risk premium). An open-entry
    0DTE short straddle ran ~+0.45%/day at 83-97% win; an EOD/overnight entry
    LOSES (the overnight gap eats it). So: sell, but enter at the open.
  * HOW MUCH — the EOD 0-45d dealer gamma REGIME predicts next-day intraday RANGE
    (Barbon & Buraschi gamma vol-suppression): long-gamma quieter, short-gamma
    wider. This sets WING WIDTH, not direction.

    The regime is spot-vs-zero-gamma-flip, NOT the sign of the aggregate net GEX.
    Those are different quantities: on 2026-08-05 SPY's 0-45DTE aggregate was
    +636,479,709 (positive) while spot sat BELOW the flip, i.e. dealers were SHORT
    gamma. Reading the regime off the aggregate's sign made this script emit
    GO_PREMIUM_SELL labelled "long-gamma: quieter, mean-reverting" into a
    short-gamma tape. `uw options-structure gex` is the arbiter and wins on
    disagreement; an unknown or disputed regime stands the sleeve aside.
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


def zero_gamma_level(per_strike: list[tuple[float, float]]) -> float | None:
    """Dealer zero-gamma flip level from per-strike net GEX.

    `per_strike` is [(strike, net_gex)]. Sweeping strikes upward, the running
    cumulative net GEX crosses zero where the dealer book flips sign; ABOVE that
    level dealers are net long gamma. We take the HIGHEST crossing and linearly
    interpolate it, which is the standard convention and the one that reproduces
    `uw options-structure gex`'s own `regime` field on both index proxies
    (verified 2026-08-05 against the full parquet book: SPY -> 775.96 vs the CLI's own
    775.97, spot 771.34, both NEGATIVE. QQQ does NOT reproduce (local 734.61 vs a CLI
    regime of POSITIVE) -- which is why `recommend` treats a disagreement as a
    stand-aside rather than quietly preferring one source.)

    Returns None when the book never crosses zero -- there is no flip level, so
    there is no regime to report. Callers must fail closed on None rather than
    substitute the aggregate's sign; see `gamma_regime`.
    """
    ordered = sorted((k, g) for k, g in per_strike if k is not None and g is not None)
    if len(ordered) < 2:
        return None
    crossings: list[float] = []
    cum = 0.0
    prev: tuple[float, float] | None = None
    for strike, net in ordered:
        new = cum + net
        if prev is not None and (prev[1] > 0) != (new > 0):
            k0, c0 = prev
            crossings.append(k0 + (strike - k0) * (0.0 - c0) / (new - c0) if new != c0 else strike)
        prev = (strike, new)
        cum = new
    return max(crossings) if crossings else None


def gamma_regime_from_book(spot: float | None, per_strike: list[tuple[float, float]]) -> int | None:
    """Dealer gamma regime from the per-strike book: +1 long, -1 short, None unknown.

    Two cases, and the distinction is the whole point of this module's 2026-08-05 fix:

    * The cumulative curve DOES cross zero -> a flip level exists, and the regime is
      spot-vs-flip. The aggregate's sign is irrelevant here and using it is the bug.
    * The cumulative curve NEVER crosses zero -> the book is one sign across every
      sampled strike, there is no flip, and the aggregate's sign genuinely does
      describe the whole book. Using it in THIS case is sound, not a relapse.

    Without the second case roughly half of all sessions returned None (29/60 on SPY
    for the 60 days to 2026-08-05), which silently emptied the range buckets.
    """
    flip = zero_gamma_level(per_strike)
    if flip is not None:
        return gamma_regime(spot, flip)
    total = sum(g for _, g in per_strike if g is not None)
    return +1 if total > 0 else (-1 if total < 0 else None)


def gamma_regime(spot: float | None, flip: float | None) -> int | None:
    """Dealer gamma regime: +1 long, -1 short, None unknown.

    THE CONVENTION IS SPOT-VS-FLIP, NOT THE SIGN OF THE AGGREGATE. These are
    different quantities and conflating them is what shipped a premium-sell into
    a short-gamma tape on 2026-08-05: SPY's 0-45DTE `total_gex` was +636,479,709
    (positive, "long") while spot 771.34 sat below the 775.97 flip, which is the
    SHORT-gamma, vol-acceleration state the CLI reported.

    Returns None when either input is missing. Never guesses a direction.
    """
    if spot is None or flip is None:
        return None
    return +1 if spot > flip else -1


def _gex_range_corr(done: list[dict[str, Any]]) -> float | None:
    """Correlation of dealer-gamma sign with next-day range, over sessions whose
    regime is KNOWN. Previously bailed to None if any single session lacked a
    sign; now it drops those sessions and reports the rest."""
    known = [s for s in done if s.get("gex_sign") in (1, -1)]
    if len(known) < 4:
        return None
    c = _corr([s["gex_sign"] for s in known], [s["rng"] for s in known])
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

    # A session whose flip level could not be computed has an UNKNOWN regime and
    # belongs in neither bucket. The pre-2026-08-05 code used `<= 0`, which swept
    # every unknown into the short-gamma bucket and quietly biased its mean range.
    longs = [s["rng"] for s in done if s.get("gex_sign") == 1]
    shorts = [s["rng"] for s in done if s.get("gex_sign") == -1]
    unknown_gamma = sum(1 for s in done if s.get("gex_sign") is None)

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
        "sessions_unknown_gamma": unknown_gamma,
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

    latest needs: symbol, spot, implied_move, vix, vix_prev, front_iv,
    zero_gamma_level, net_gex_0_45d, and optionally cli_gamma_regime.
    ctx is an ``evaluate`` result (regime expected-ranges + vix bounds).

    The dealer-gamma regime is taken from `cli_gamma_regime` when present -- the
    CLI is the designated arbiter and WINS on disagreement -- otherwise from
    spot-vs-`zero_gamma_level`. It is NEVER taken from the sign of
    `net_gex_0_45d`, which is a different quantity: that aggregate keeps only the
    job it was validated for (Barbon & Buraschi next-day RANGE / wing width).
    An unknown regime stands the setup aside rather than defaulting to a branch.
    """
    vix = latest.get("vix")
    vix_prev = latest.get("vix_prev")
    bounds = tuple(b if b is not None else float("nan") for b in ctx.get("vix_tercile_bounds", [float("nan"), float("nan")]))
    state = vol_state(vix, bounds)

    local_sign = latest.get("dealer_gamma_sign")
    if local_sign is None:
        local_sign = gamma_regime(latest.get("spot"), latest.get("zero_gamma_level"))
    cli_raw = latest.get("cli_gamma_regime")
    cli_sign = {"POSITIVE": +1, "NEGATIVE": -1}.get(str(cli_raw).upper()) if cli_raw else None
    sign = cli_sign if cli_sign is not None else local_sign
    source = "cli" if cli_sign is not None else ("local_flip" if local_sign is not None else "none")
    disagreement = (cli_sign is not None and local_sign is not None and cli_sign != local_sign)

    regime_name = {1: "LONG", -1: "SHORT"}.get(sign, "UNKNOWN")
    # Wing width is quoted from the bucket basis it was MEASURED on (aggregate sign),
    # not from the dealer regime -- the two are different quantities and the buckets
    # would otherwise be indexed by something they were never stratified by.
    net_gex = latest.get("net_gex_0_45d")
    range_sign = (1 if net_gex > 0 else -1) if net_gex is not None else sign
    expected_range = (ctx.get("long_gamma_mean_range_pct") if range_sign == +1
                      else ctx.get("short_gamma_mean_range_pct"))

    stand_aside = None
    if sign is None:
        stand_aside = ("Dealer gamma regime UNKNOWN (no zero-gamma flip level and no CLI reading) — "
                       "cannot tell the vol-suppressive book from the vol-acceleration one; stand aside. "
                       "Cross-check `uw options-structure gex --symbol <SYM>`.")
    elif sign == -1:
        stand_aside = ("Dealers net SHORT gamma (spot below the zero-gamma flip) — trend-acceleration "
                       "regime, the short-vol left tail this sleeve cannot survive and the sample never "
                       "priced. Premium-selling stands aside.")
    elif disagreement:
        stand_aside = (f"Gamma sources DISAGREE (CLI {str(cli_raw).upper()} vs local flip "
                       f"{'LONG' if local_sign == +1 else 'SHORT'}) — the regime is not reliably known, "
                       f"and this sleeve's left tail is unsampled. Fail closed.")
    if vix is not None and vix_prev is not None and (vix - vix_prev) >= VIX_SPIKE:
        stand_aside = f"VIX spiking (+{vix - vix_prev:.1f}) — short-vol left-tail regime; stand aside."
    front_ratio = (latest["front_iv"] / (vix / 100.0)) if (vix and latest.get("front_iv")) else None
    caution = None
    if front_ratio is not None and front_ratio >= BACKWARDATION_RATIO:
        caution = f"Front-end backwardation (0DTE IV {front_ratio:.2f}× VIX) — event/gap risk; half size."
    if disagreement:
        caution = ((caution + " ") if caution else "") + (
            f"GAMMA DISAGREEMENT: CLI reads {str(cli_raw).upper()} while the local flip level reads "
            f"{'LONG' if local_sign == +1 else 'SHORT'}. The CLI wins; the local level is advisory.")

    size = SIZE_BY_STATE.get(state, 1.0)
    if caution:
        size *= 0.5
    if stand_aside:
        size = 0.0

    if stand_aside:
        # Never describe a tradeable structure next to a stand-aside verdict; the
        # 2026-08-05 failure was read off exactly such a label.
        structure = f"NO PREMIUM SELL — {stand_aside.split('—')[0].strip().rstrip('.')}."
    elif sign == +1:
        structure = (f"iron fly / short straddle centred at {latest.get('spot')}, "
                     f"wings ≈ ±{expected_range}% (long-gamma: quieter, mean-reverting)")
    elif sign == -1:
        structure = (f"NO PREMIUM SELL — dealers short gamma. If overriding, wings ≥ ±{expected_range}% "
                     f"(wider range / trendier) and half size at most.")
    else:
        structure = "NO PREMIUM SELL — dealer gamma regime unverified."

    return {
        "symbol": latest["symbol"],
        "sell_premium": bool(size > 0 and not stand_aside),
        "vol_state": state,
        "dealer_gamma_regime": regime_name,
        "gamma_source": source,
        "gamma_disagreement": disagreement,
        "zero_gamma_level": latest.get("zero_gamma_level"),
        "net_gex_0_45d": latest.get("net_gex_0_45d"),
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


def cli_gamma_regime(symbol: str, timeout: float = 25.0) -> str | None:
    """`uw options-structure gex` regime for `symbol`: 'POSITIVE'/'NEGATIVE'/None.

    The CLI is the designated arbiter for dealer gamma sign and WINS on
    disagreement. Only its `regime` field is read -- its `zero_gamma_level` is
    NOT trusted (2026-08-05: QQQ printed 249.5 against per-strike data clustering
    at 698-720, while the regime itself was correct). Best-effort: any failure
    returns None and the caller falls back to the local flip, or stands aside.
    """
    import subprocess
    try:
        p = subprocess.run(["uw", "options-structure", "gex", "--symbol", symbol, "--json", "--quiet"],
                           capture_output=True, text=True, timeout=timeout)
        if p.returncode != 0:
            return None
        reg = json.loads(p.stdout).get("regime")
        return reg.upper() if isinstance(reg, str) and reg.upper() in ("POSITIVE", "NEGATIVE") else None
    except (OSError, ValueError, subprocess.SubprocessError):
        return None


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

    def gex_book(f: Path, sym: str):
        """(aggregate net GEX, [(strike, net GEX)]) over the 0-45DTE book.

        The aggregate keeps ONLY its validated job -- Barbon & Buraschi next-day
        range / wing width. The per-strike series is what yields the zero-gamma
        flip level, and the flip is what defines the dealer regime. Deriving the
        regime from the aggregate's sign is the 2026-08-05 bug.
        """
        q = (f"WITH b AS (SELECT strike,option_type,gamma,open_interest, "
             f"row_number() OVER (PARTITION BY strike,option_type,expiry ORDER BY executed_at DESC) rn "
             f"FROM '{f}' WHERE underlying_symbol='{sym}' AND gamma>0 AND open_interest>0 "
             f"AND date_diff('day',(SELECT max(CAST(executed_at AS DATE)) FROM '{f}'),expiry) BETWEEN 0 AND 45) "
             f"SELECT strike, sum(CASE WHEN option_type='put' THEN -gamma*open_interest "
             f"ELSE gamma*open_interest END) g FROM b WHERE rn=1 GROUP BY strike ORDER BY strike")
        rows = con.execute(q).fetchall()
        if not rows:
            return None, []
        per_strike = [(r[0], r[1]) for r in rows if r[1] is not None]
        return sum(g for _, g in per_strike), per_strike

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
            net_gex, per_strike = gex_book(f, sym)
            flip = zero_gamma_level(per_strike)
            feat = {"date": d, "symbol": sym, "spot": round(spot, 2), "front_iv": iv,
                    "implied_move": implied_move_pct(iv), "vix": vix, "vix_prev": vix_prev,
                    "net_gex_0_45d": net_gex, "zero_gamma_level": flip,
                    # TWO DISTINCT QUANTITIES, deliberately kept apart (2026-08-05):
                    #  * gex_sign      = sign of the 0-45DTE AGGREGATE. Feeds ONLY the
                    #    next-day RANGE / wing-width buckets. Measured on this panel it is
                    #    the stronger range predictor (corr -0.36 SPY / -0.35 QQQ, vs
                    #    -0.26 / -0.19 for spot-vs-flip), which is the Barbon & Buraschi use.
                    #  * dealer_gamma_sign = spot-vs-flip. The dealer REGIME, matching
                    #    `uw options-structure gex`. Feeds the sell / stand-aside decision.
                    # The two disagree on ~1 session in 3. Using the aggregate for the
                    # REGIME is the bug; using the flip for the RANGE buckets is a
                    # measurable downgrade. Each keeps the job it is better at.
                    "gex_sign": (1 if (net_gex or 0) > 0 else -1) if net_gex is not None else None,
                    "dealer_gamma_sign": gamma_regime_from_book(spot, per_strike)}
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
    ap.add_argument("--no-cli-check", action="store_true",
                    help="skip the `uw options-structure gex` cross-check (offline/testing). "
                         "The local flip level is then the only gamma source.")
    args = ap.parse_args()
    symbols = [s.strip().upper() for s in args.symbols.split(",") if s.strip()]

    data = _reconstruct(Path(args.parquet_dir), symbols, args.days)
    if data is None:
        out = {"available": False, "reason": "duckdb unavailable or no parquet data "
               f"in {args.parquet_dir} (the live reconstruction needs duckdb + the EOD export)"}
        print(json.dumps(out) if args.json else out["reason"])
        return 0

    backtest = {sym: evaluate(sess) for sym, sess in data["sessions"].items()}
    if not args.no_cli_check:
        for sym, feat in data["latest"].items():
            feat["cli_gamma_regime"] = cli_gamma_regime(sym)
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
            lvl = s["zero_gamma_level"]
            print(f"   GAMMA: {s['dealer_gamma_regime']} (source={s['gamma_source']}"
                  f"{', DISAGREEMENT' if s['gamma_disagreement'] else ''}) "
                  f"| flip={lvl if lvl is None else round(lvl, 2)} net_gex_0_45d={s['net_gex_0_45d']}")
            print(f"   SETUP: sell_premium={s['sell_premium']} vol_state={s['vol_state']} size×{s['size_scalar']} "
                  f"| {s['suggested_structure']}")
            if s["stand_aside_reason"]:
                print(f"   STAND ASIDE: {s['stand_aside_reason']}")
            if s["caution"]:
                print(f"   CAUTION: {s['caution']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
