"""G1: fill-quality classification from the panel's own NBBO (`findings/market-analysis/RESEARCH/47`
§2 G1). Pure functions for bucket assignment plus the matching SQL fragments the driver
(`scripts/fills.py`) runs over 103 days of All Options prints — one source of truth for each
threshold so the SQL and the tested Python logic cannot drift apart.

Scope (RESEARCH/20 §2.2): the "clean single-leg lane" only (`auto`, `isoi`, `slan`, `slai`,
`slft`, `slcn`) — the six codes where `side` carries unambiguous directional meaning. `no_side`
prints (RESEARCH/20 §2.1: 0.02% of trades, 6.6% of premium, cabinet/negotiated blocks with no
assignable aggressor) are excluded outright rather than folded into `mid`, per that section's
explicit warning.

Fill-quality classes, defined relative to the print's own NBBO and its aggressor side (`side`
bid/ask), within `TOL_FRAC` of the half-spread:
  AT_OR_BETTER_MID  the aggressor paid/received at least as well as the midpoint
  BETWEEN_MID_TOUCH strictly between the midpoint and its own touch
  AT_TOUCH          at the bid (sell aggressor) or the ask (buy aggressor)
  OUTSIDE           beyond the touch on either side (stale quote, late report, crossed print)
`side == 'mid'` prints have no aggressor to sign the improvement against, so they are classified
by unsigned distance to the midpoint and touches instead (documented caveat: RESEARCH/20 §2.1
notes 11.2% of trades print at `mid`; this class answers "how close to the touch", not
"who was skewed").
"""
from __future__ import annotations

from dataclasses import dataclass

from engine.config import EARLY_END, LATE_START, SESSION_END_EXCL, SESSION_START, TIER1_MIN_SIZE

SINGLE_LEG_CODES = ("auto", "isoi", "slan", "slai", "slft", "slcn")
SIDE_EXCLUDED = "no_side"

CLASS_AT_OR_BETTER_MID = "at_or_better_mid"
CLASS_BETWEEN_MID_TOUCH = "between_mid_touch"
CLASS_AT_TOUCH = "at_touch"
CLASS_OUTSIDE = "outside"
CLASSES = (CLASS_AT_OR_BETTER_MID, CLASS_BETWEEN_MID_TOUCH, CLASS_AT_TOUCH, CLASS_OUTSIDE)

TOL_FRAC = 0.05     # fraction of the half-spread treated as "at" a boundary (float/rounding slop)

BUCKET_MINUTES = 30

WINDOW_EARLY, WINDOW_LATE, WINDOW_B1, WINDOW_B2 = "early", "late", "b1", "b2"
# Candidate marking windows for the re-marking crosswalk (RESEARCH/47 §2 G1 item 2): `early` and
# `late` are the windows the marking engine already uses (`config.EARLY_END`/`LATE_START`,
# inclusive at the boundary they name); `b1`/`b2` are the two pre-registered later-exit variants
# ("10:30 to 11:30" and "14:30 to 15:30") tested for treatment (b). Windows may overlap (`late`
# and `b2` share 15:00-15:30) — each is graded independently, not as a session partition.
CANDIDATE_WINDOWS: dict[str, tuple[str, str]] = {
    WINDOW_EARLY: (SESSION_START, EARLY_END),
    WINDOW_LATE: (LATE_START, SESSION_END_EXCL),
    WINDOW_B1: ("10:30:01", "11:30:00"),
    WINDOW_B2: ("14:30:00", "15:30:00"),
}

# (upper bound, inclusive, on calendar DTE; label) — evaluated in order, first match wins.
DTE_BUCKET_EDGES: tuple[tuple[int, str], ...] = (
    (0, "0dte"), (2, "1-2d"), (7, "3-7d"), (21, "8-21d"), (45, "22-45d"),
)
DTE_BUCKET_LAST = "46d+"


# ----------------------------------------------------------------------------- pure functions


def dte_bucket(dte_cal: int) -> str:
    """Calendar-day DTE bucket (same units as `mart/daily_contract.py`'s `dte_cal`)."""
    for hi, label in DTE_BUCKET_EDGES:
        if dte_cal <= hi:
            return label
    return DTE_BUCKET_LAST


def bucket30_index(minutes_since_open: float) -> int:
    """0-based 30-minute bucket index from minutes since `SESSION_START`."""
    if minutes_since_open < 0:
        raise ValueError(f"minutes_since_open must be >= 0, got {minutes_since_open}")
    return int(minutes_since_open // BUCKET_MINUTES)


def bucket30_label(idx: int) -> str:
    """`HH:MM-HH:MM` label for a 30-minute bucket index, anchored at `SESSION_START`."""
    start_h, start_m = (int(x) for x in SESSION_START.split(":")[:2])
    start_total = start_h * 60 + start_m
    lo = start_total + idx * BUCKET_MINUTES
    hi = lo + BUCKET_MINUTES
    return f"{lo // 60:02d}:{lo % 60:02d}-{hi // 60:02d}:{hi % 60:02d}"


def in_window(et_time_str: str, window: str) -> bool:
    """Whether a `HH:MM:SS` ET time falls in `window` (both bounds of `CANDIDATE_WINDOWS`
    inclusive). A time can belong to more than one window (`late` and `b2` overlap)."""
    lo, hi = CANDIDATE_WINDOWS[window]
    return lo <= et_time_str <= hi


def tier_from_window_size(window_size: float, tier1_min_size: int = TIER1_MIN_SIZE) -> int:
    """Tier 1 (VWAP-quality) vs tier 2 (thin), mirroring `marking.print_mark`'s `size >= 5` cut."""
    return 1 if window_size >= tier1_min_size else 2


def classify_fill(side: str, price: float, bid: float, ask: float, tol_frac: float = TOL_FRAC) -> str:
    """One print's position in its own NBBO, signed by aggressor side where one exists."""
    if side == SIDE_EXCLUDED:
        raise ValueError("no_side prints must be filtered out before classify_fill (RESEARCH/20 §2.1)")
    if ask < bid or bid <= 0:
        raise ValueError(f"invalid NBBO: bid={bid} ask={ask}")
    mid = (bid + ask) / 2.0
    half_spread = (ask - bid) / 2.0
    if half_spread <= 0:
        return CLASS_AT_TOUCH   # degenerate zero-width quote: touch and mid coincide
    tol = tol_frac * half_spread
    if side == "ask":            # aggressor bought (lifted the offer): lower price is better
        if price > ask + tol or price < bid - tol:
            return CLASS_OUTSIDE
        if price >= ask - tol:
            return CLASS_AT_TOUCH
        if price <= mid + tol:
            return CLASS_AT_OR_BETTER_MID
        return CLASS_BETWEEN_MID_TOUCH
    if side == "bid":            # aggressor sold (hit the bid): higher price is better
        if price < bid - tol or price > ask + tol:
            return CLASS_OUTSIDE
        if price <= bid + tol:
            return CLASS_AT_TOUCH
        if price >= mid - tol:
            return CLASS_AT_OR_BETTER_MID
        return CLASS_BETWEEN_MID_TOUCH
    if side == "mid":            # no aggressor: unsigned distance to mid and to the near touch
        if price < bid - tol or price > ask + tol:
            return CLASS_OUTSIDE
        if abs(price - mid) <= tol:
            return CLASS_AT_OR_BETTER_MID
        if price <= bid + tol or price >= ask - tol:
            return CLASS_AT_TOUCH
        return CLASS_BETWEEN_MID_TOUCH
    raise ValueError(f"unknown side {side!r}")


@dataclass(frozen=True)
class ShareResult:
    """Volume- and premium-weighted share of a cell's rows falling in `at_or_better_mid`."""
    volume: float
    premium: float
    mid_or_better_volume: float
    mid_or_better_premium: float

    @property
    def volume_share(self) -> float:
        return self.mid_or_better_volume / self.volume if self.volume else float("nan")

    @property
    def premium_share(self) -> float:
        return self.mid_or_better_premium / self.premium if self.premium else float("nan")


def mid_or_better_share(rows: list[dict]) -> ShareResult:
    """`rows`: dicts with `class`, `volume`, `premium` (already aggregated by class within one
    cell, e.g. one (tier, window) pair). Pure aggregation, used by both the summary tables and
    the re-marking crosswalk (`g1_remark.build_mid_share_lookup`)."""
    volume = sum(r["volume"] for r in rows)
    premium = sum(r["premium"] for r in rows)
    mv = sum(r["volume"] for r in rows if r["class"] == CLASS_AT_OR_BETTER_MID)
    mp = sum(r["premium"] for r in rows if r["class"] == CLASS_AT_OR_BETTER_MID)
    return ShareResult(volume, premium, mv, mp)


# ----------------------------------------------------------------------------- SQL fragments
# Mirrors of the pure functions above, executed once over the panel instead of row-by-row in
# Python. `tests/test_fills.py::test_sql_classification_matches_python` runs both on the same
# synthetic rows and asserts they agree, so the two cannot silently drift.


def single_leg_codes_sql() -> str:
    codes = ", ".join(f"'{c}'" for c in SINGLE_LEG_CODES)
    return f"upstream_condition_detail IN ({codes})"


def dte_bucket_sql(dte_col: str) -> str:
    clauses = " ".join(f"WHEN {dte_col} <= {hi} THEN '{label}'" for hi, label in DTE_BUCKET_EDGES)
    return f"CASE {clauses} ELSE '{DTE_BUCKET_LAST}' END"


def in_window_sql(et_time_col: str, window: str) -> str:
    lo, hi = CANDIDATE_WINDOWS[window]
    return f"({et_time_col} >= TIME '{lo}' AND {et_time_col} <= TIME '{hi}')"


def classify_fill_sql(side_col: str, price_col: str, bid_col: str, ask_col: str,
                      tol_frac: float = TOL_FRAC) -> str:
    mid = f"(({bid_col} + {ask_col}) / 2.0)"
    hs = f"(({ask_col} - {bid_col}) / 2.0)"
    tol = f"({tol_frac} * {hs})"
    ask_case = (f"CASE WHEN {price_col} > {ask_col} + {tol} OR {price_col} < {bid_col} - {tol} "
               f"THEN '{CLASS_OUTSIDE}' "
               f"WHEN {price_col} >= {ask_col} - {tol} THEN '{CLASS_AT_TOUCH}' "
               f"WHEN {price_col} <= {mid} + {tol} THEN '{CLASS_AT_OR_BETTER_MID}' "
               f"ELSE '{CLASS_BETWEEN_MID_TOUCH}' END")
    bid_case = (f"CASE WHEN {price_col} < {bid_col} - {tol} OR {price_col} > {ask_col} + {tol} "
               f"THEN '{CLASS_OUTSIDE}' "
               f"WHEN {price_col} <= {bid_col} + {tol} THEN '{CLASS_AT_TOUCH}' "
               f"WHEN {price_col} >= {mid} - {tol} THEN '{CLASS_AT_OR_BETTER_MID}' "
               f"ELSE '{CLASS_BETWEEN_MID_TOUCH}' END")
    mid_case = (f"CASE WHEN {price_col} < {bid_col} - {tol} OR {price_col} > {ask_col} + {tol} "
               f"THEN '{CLASS_OUTSIDE}' "
               f"WHEN abs({price_col} - {mid}) <= {tol} THEN '{CLASS_AT_OR_BETTER_MID}' "
               f"WHEN {price_col} <= {bid_col} + {tol} OR {price_col} >= {ask_col} - {tol} "
               f"THEN '{CLASS_AT_TOUCH}' ELSE '{CLASS_BETWEEN_MID_TOUCH}' END")
    return (f"CASE WHEN {hs} <= 0 THEN '{CLASS_AT_TOUCH}' "
            f"WHEN {side_col} = 'ask' THEN {ask_case} "
            f"WHEN {side_col} = 'bid' THEN {bid_case} "
            f"WHEN {side_col} = 'mid' THEN {mid_case} END")


SESSION_WHERE = (f"et::TIME >= TIME '{SESSION_START}' AND et::TIME < TIME '{SESSION_END_EXCL}'")
