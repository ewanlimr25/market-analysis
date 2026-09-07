"""The wb-1.0 read (`DESIGN/110-watch-basket.md` §6, R3): per-basket (LONG/SHORT/VOL) hit rate at
h21 against the universe base of the same nights, two-sided binomial p, mean SPY excess with
name-clustered t. NOT_DUE before the later of 2026-12-01 and 100 independent episodes; on the
date, `CLEARS` or `FAILS` per the bar: hit rate at least 10 points above the base with two-sided
binomial p < 0.05, and mean SPY excess > 0 with name-clustered t >= 2.

Pure given its ledger frame (`ledger/wb/forward_signals.parquet`, read by the caller):
`read(ledger, basket, as_of)` is the whole read. `scripts/adjudicate.py basket` wires the real
ledger and writes the verdict once via `engine.improve.adjudicate.write_adjudication` (the same
write-once + `LOG.md` contract every other verdict uses).
"""
from __future__ import annotations

import math
from datetime import date

import pandas as pd

from engine import calendar as cal
from engine.validation import stats as S
from engine.watch import live as LV
from engine.watch import universe as U

READ_DATE = date(2026, 12, 1)          # DESIGN/110 §6: the read is on the LATER of this and...
EPISODES_REQUIRED = 100                # ...100 independent episodes
TRAILING_SESSIONS = 30                 # window for the projected-date accrual rate
HIT_RATE_MARGIN = 0.10                 # "at least 10 points above the universe base"
BINOMIAL_ALPHA = 0.05
MEAN_EXCESS_MIN_T = 2.0
CLEARS, FAILS, NOT_DUE = "CLEARS", "FAILS", "NOT_DUE"
BASKETS = ("LONG", "SHORT", "VOL")


def episode_rows(ledger: pd.DataFrame, basket: str) -> pd.DataFrame:
    """Episode rows (DESIGN/110 §4: `episode is True`, i.e. not a re-entry continuation) of
    `basket` with `excess_h21` already resolved -- the unit the read counts, never the row count."""
    if ledger.empty:
        return ledger
    sub = ledger[(ledger["basket"] == basket) & (ledger["episode"].astype(bool))]
    return sub[sub["excess_h21"].notna()]


def projected_date(dates: list[date], as_of: date, n_have: int, n_required: int = EPISODES_REQUIRED,
                    trailing_sessions: int = TRAILING_SESSIONS) -> str | None:
    """The calendar date `n_required` episodes are projected to accrue, at the rate of episodes
    seen in the trailing `trailing_sessions` sessions before `as_of`. `None` when that recent rate
    is zero -- a projection cannot be made, which is different from "never"."""
    if n_have >= n_required:
        return as_of.isoformat()
    if not dates:
        return None
    cutoff = cal.prev_session(as_of, trailing_sessions)
    recent = [d for d in dates if d > cutoff]
    if not recent:
        return None
    rate_per_session = len(recent) / trailing_sessions
    if rate_per_session <= 0:
        return None
    remaining = n_required - n_have
    sessions_needed = math.ceil(remaining / rate_per_session)
    return cal.next_session(as_of, sessions_needed).isoformat()


def universe_base_h21(nights: list[date]) -> dict:
    """Universe base hit rate / mean SPY excess at h21 over exactly `nights` (the nights the
    basket actually had episodes on, DESIGN/110 §6's "universe base of the same nights") --
    computed live from the screener spine (`engine.watch.universe`/`live.load_closes`), never
    from the ledger."""
    if not nights:
        return {"n": 0, "hit_rate": float("nan"), "mean_excess": float("nan")}
    universe = U.build_universe(sorted(set(nights)))
    if universe.empty:
        return {"n": 0, "hit_rate": float("nan"), "mean_excess": float("nan")}
    targets = {d: cal.next_session(d, 21) for d in universe["date"].unique()}
    tickers = set(universe["ticker"]) | {"SPY"}
    dates_needed = set(universe["date"]) | set(targets.values())
    closes = LV.load_closes(tickers, dates_needed)
    excess = []
    for t, d in zip(universe["ticker"], universe["date"]):
        target = targets[d]
        c0, c1 = closes.get((t, d)), closes.get((t, target))
        s0, s1 = closes.get(("SPY", d)), closes.get(("SPY", target))
        if None in (c0, c1, s0, s1) or c0 == 0 or s0 == 0:
            continue
        excess.append(c1 / c0 - 1 - (s1 / s0 - 1))
    if not excess:
        return {"n": 0, "hit_rate": float("nan"), "mean_excess": float("nan")}
    hits = sum(1 for e in excess if e > 0)
    return {"n": len(excess), "hit_rate": hits / len(excess), "mean_excess": sum(excess) / len(excess)}


def verdict(episodes: pd.DataFrame, base: dict, alpha: float = BINOMIAL_ALPHA,
            hit_margin: float = HIT_RATE_MARGIN, min_t: float = MEAN_EXCESS_MIN_T) -> tuple[str, str, dict]:
    n = len(episodes)
    x = episodes["excess_h21"].astype(float)
    hits = int((x > 0).sum())
    hit_rate = hits / n if n else float("nan")
    base_hit = base.get("hit_rate", float("nan"))
    binom = S.binomial_test(hits, n, base_hit) if (n and base_hit == base_hit) else {"p": float("nan")}
    ct = S.cluster_t(x, episodes["ticker"])
    stats = {"n_episodes": n, "hit_rate": hit_rate, "base_hit_rate": base_hit, "base_n": base.get("n"),
             "binomial_p": binom.get("p"), "mean_excess": ct["mean"], "clustered_t": ct["t"], "G": ct["G"]}
    clears = (n > 0 and base.get("n", 0) > 0
              and hit_rate == hit_rate and (hit_rate - base_hit) >= hit_margin
              and binom.get("p") == binom.get("p") and binom["p"] < alpha
              and ct["mean"] == ct["mean"] and ct["mean"] > 0
              and ct["t"] == ct["t"] and ct["t"] >= min_t)
    if clears:
        reason = (f"hit {hit_rate:.1%} vs base {base_hit:.1%} (+{(hit_rate - base_hit) * 100:.1f}pt), "
                  f"binomial p {binom['p']:.4f}, mean excess {ct['mean']:+.4f}, t {ct['t']:.2f} (G={ct['G']}) "
                  f"on {n} episodes")
        return CLEARS, reason, stats
    reason = (f"hit {hit_rate:.1%} vs base {base_hit:.1%}, binomial p {binom.get('p')}, "
              f"mean excess {ct['mean']:+.4f}, t {ct['t']:.2f} (G={ct['G']}) on {n} episodes "
              f"-- does not clear DESIGN/110 §6")
    return FAILS, reason, stats


def read(ledger: pd.DataFrame, basket: str, as_of: date) -> dict:
    """The whole R3 read for one basket. Refuses an unknown basket name; never raises otherwise --
    an unresolvable base or a thin episode count simply cannot clear (`verdict` handles NaN)."""
    if basket not in BASKETS:
        raise ValueError(f"basket must be one of {BASKETS}, got {basket!r}")
    eps = episode_rows(ledger, basket)
    n = len(eps)
    dates = sorted(pd.to_datetime(eps["date"]).dt.date.tolist()) if n else []
    proj = projected_date(dates, as_of, n)
    is_due = as_of >= READ_DATE and n >= EPISODES_REQUIRED
    if not is_due:
        reason = (f"{n} of {EPISODES_REQUIRED} episodes; read on the later of {READ_DATE.isoformat()} "
                  f"and {EPISODES_REQUIRED} episodes")
        if proj:
            reason += f"; projected at the trailing-{TRAILING_SESSIONS}-session rate: {proj}"
        return {"basket": basket, "as_of": as_of.isoformat(), "verdict": NOT_DUE, "reason": reason,
                "n_episodes": n, "projected_date": proj}
    base = universe_base_h21(dates)
    v, reason, stats = verdict(eps, base)
    return {"basket": basket, "as_of": as_of.isoformat(), "verdict": v, "reason": reason,
            "n_episodes": n, "projected_date": proj, "stats": stats}
