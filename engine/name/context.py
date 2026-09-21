"""R3 section F of the ticker sheet: context, and the one sentence that stands in for a forecast
(DESIGN/70 §7 `context`, §8 line F, DECISIONS D3).

Five numbers and a fixed sentence. The numbers -- 21- and 63-session returns, position in the
52-week range, and where today's net option premium and share volume sit in the cross-section and
in the name's own history -- are the trailing facts a reader would otherwise look up by hand. None
of them is a signal: `RESEARCH/30 §15` grades no input above D for direction at 1 to 4 weeks, the
old book's trailing-trend label hit 36% forward, and `market-analysis/RESEARCH/41 §41.0` killed
0 of 128 flow tests into survival. So the section prints `SENTENCE` verbatim and the engine emits
no direction; a direction reaches the sheet only as the owner's `DIRECTION=`, and it is ledgered
(D3). Changing that sentence is a decision, not an edit.

Percentiles use the mid-rank convention -- `(below + half the ties) / n` -- so a value is neither
above nor below itself and a one-row universe reads 50, not 0 or 100.

Pure: frames are read, never mutated; the returned dict is strict JSON (`engine.schema.clean`).
"""
from __future__ import annotations

from datetime import date

import pandas as pd

from engine.config import NAME_ISSUE_TYPES, NAME_PARAMS, NameParams
from engine.name.data import NameInputs
from engine.schema import clean

SENTENCE = ("Direction: no input on this sheet has a measured directional edge at 1–4 weeks; "
            "the engine emits none.")

RET_SESSIONS = (21, 63)           # §7 `ret_21`, `ret_63`: close / close(-n) - 1
W52_WINDOW = 252                  # `w52_pos` over the trailing 252 bars ..
W52_MIN_BARS = 200                # .. and null under 200 of them (a half-listed year has no range)
SELF_WINDOW = 63                  # `flow_pct_self` / `vol_pct_self` over the name's last 63 sessions
BARS_MART = "earnings_history/bars"


def _num(value) -> float | None:
    try:
        out = float(value)
    except (TypeError, ValueError):
        return None
    return None if out != out else out


# ---- the percentile rule -------------------------------------------------------------------------

def percentile_rank(values, x: float | None) -> float | None:
    """`100 x (values below x + half the ties) / n`, the mid-rank convention; `None` on an empty
    pool or a null `x`. A value is neither above nor below itself, so a one-row pool reads 50."""
    if x is None:
        return None
    pool = [v for v in (_num(v) for v in values) if v is not None]
    if not pool:
        return None
    below = sum(1 for v in pool if v < x)
    ties = sum(1 for v in pool if v == x)
    return 100.0 * (below + 0.5 * ties) / len(pool)


# ---- bars: the two returns and the 52-week position ----------------------------------------------

def bars_to(bars: pd.DataFrame, d: date) -> pd.DataFrame | None:
    """The name's bars on or before `d`, ascending; `None` when there are none."""
    if bars is None or bars.empty or "date" not in bars.columns or "close" not in bars.columns:
        return None
    sub = bars[bars["date"] <= d].dropna(subset=["close"]).sort_values("date")
    return None if sub.empty else sub


def trailing_return(closes: list[float], n: int) -> float | None:
    """`close / close(-n) - 1`; `None` without `n + 1` closes or on a non-positive base."""
    if len(closes) <= n:
        return None
    base = closes[-1 - n]
    return None if not base else closes[-1] / base - 1.0


def w52_position(frame: pd.DataFrame, window: int = W52_WINDOW,
                 min_bars: int = W52_MIN_BARS) -> float | None:
    """`(close - low) / (high - low)` over the trailing `window` bars, using each bar's own high
    and low. `None` under `min_bars` bars or on a flat range (which has no position in it)."""
    if frame is None or len(frame) < min_bars or not {"high", "low"} <= set(frame.columns):
        return None
    sub = frame.tail(window)
    high, low = _num(sub["high"].max()), _num(sub["low"].min())
    close = _num(sub["close"].iloc[-1])
    if high is None or low is None or close is None or high == low:
        return None
    return (close - low) / (high - low)


# ---- flow: the name's number, then the two pools it is ranked in ---------------------------------

def net_premium(row) -> float | None:
    """`bullish_premium - bearish_premium` (DESIGN/70 §1 last row); `None` if either side is null."""
    if row is None:
        return None
    bull, bear = _num(_get(row, "bullish_premium")), _num(_get(row, "bearish_premium"))
    return None if bull is None or bear is None else bull - bear


def volume_ratio(row) -> float | None:
    """`total_volume / avg30_volume`; `None` if either is null or the average is zero."""
    if row is None:
        return None
    volume, avg = _num(_get(row, "total_volume")), _num(_get(row, "avg30_volume"))
    return None if volume is None or not avg else volume / avg


def _get(row, key):
    return row.get(key) if isinstance(row, dict) else row[key] if key in row else None


def name_universe(universe: pd.DataFrame) -> pd.DataFrame | None:
    """The day's screener rows restricted to the sheet's issue types (Common Stock, ADR, ETF) and
    to non-index rows -- L1's universe, which is the only cross-section a name belongs to."""
    if universe is None or universe.empty or "issue_type" not in universe.columns:
        return None
    keep = universe["issue_type"].isin(NAME_ISSUE_TYPES)
    if "is_index" in universe.columns:
        keep = keep & ~universe["is_index"].fillna(False).astype(bool)
    return universe[keep]


def self_history(history: pd.DataFrame, d: date, window: int = SELF_WINDOW) -> pd.DataFrame | None:
    """The name's own trailing `window` screener sessions on or before `d`, ascending."""
    if history is None or history.empty or "date" not in history.columns:
        return None
    sub = history[history["date"] <= d].sort_values("date").tail(window)
    return None if sub.empty else sub


# ---- the section -------------------------------------------------------------------------------

def evaluate(inputs: NameInputs, params: NameParams = NAME_PARAMS) -> dict:
    """The DESIGN/70 §7 `context` dict for one name on one session, `sentence` included verbatim.

    Never raises: a field that cannot be measured is `None` with its reason in `nulls`. `params` is
    accepted for the section signature every `engine.name` module shares; nothing here is tuned.
    """
    d = inputs.date.isoformat()
    nulls: list[dict] = []
    frame = bars_to(inputs.bars, inputs.date)
    bars_end = frame["date"].iloc[-1] if frame is not None else None
    closes = frame["close"].astype(float).tolist() if frame is not None else []
    rets = {n: trailing_return(closes, n) for n in RET_SESSIONS}
    for n, value in rets.items():
        if value is None:
            nulls.append({"field": f"ret_{n}", "reason": _bars_reason(closes, n + 1, inputs.date)})
    w52 = w52_position(frame)
    if w52 is None:
        nulls.append({"field": "w52_pos", "reason": _bars_reason(closes, W52_MIN_BARS, inputs.date)})

    flow = _flow(inputs)
    nulls.extend(flow["nulls"])
    return clean({
        "ret_21": rets[21], "ret_63": rets[63], "w52_pos": w52,
        "flow_pct_universe": flow["flow_pct_universe"], "flow_pct_self": flow["flow_pct_self"],
        "vol_pct_universe": flow["vol_pct_universe"], "vol_pct_self": flow["vol_pct_self"],
        "net_premium": flow["net_premium"], "volume_ratio": flow["volume_ratio"],
        "universe_n": flow["universe_n"], "self_n": flow["self_n"],
        "sentence": SENTENCE,
        "source": {
            "ret_21": f"{BARS_MART} <= {bars_end or d}", "ret_63": f"{BARS_MART} <= {bars_end or d}",
            "w52_pos": f"{BARS_MART} {W52_WINDOW} sessions to {bars_end or d}",
            "net_premium": f"screener {d}", "volume_ratio": f"screener {d}",
            "flow_pct_universe": f"screener universe {d}", "vol_pct_universe": f"screener universe {d}",
            "flow_pct_self": f"screener {SELF_WINDOW} sessions to {flow['self_end'] or d}",
            "vol_pct_self": f"screener {SELF_WINDOW} sessions to {flow['self_end'] or d}",
            "sentence": "DESIGN/70 §4F, DECISIONS D3 (frozen 2026-09-20)",
        },
        "nulls": nulls,
    })


def _bars_reason(closes: list, needed: int, d: date) -> str:
    if not closes:
        return f"no daily bar on or before {d.isoformat()}"
    return f"{len(closes)} bars on or before {d.isoformat()}, fewer than the {needed} required"


def net_premium_series(frame: pd.DataFrame | None) -> list:
    """`bullish_premium - bearish_premium` down a frame (the pool a percentile ranks against)."""
    if frame is None or not {"bullish_premium", "bearish_premium"} <= set(frame.columns):
        return []
    bull = pd.to_numeric(frame["bullish_premium"], errors="coerce")
    bear = pd.to_numeric(frame["bearish_premium"], errors="coerce")
    return (bull - bear).tolist()


def volume_ratio_series(frame: pd.DataFrame | None) -> list:
    """`total_volume / avg30_volume` down a frame; a zero average yields a null, not an infinity."""
    if frame is None or not {"total_volume", "avg30_volume"} <= set(frame.columns):
        return []
    volume = pd.to_numeric(frame["total_volume"], errors="coerce")
    avg = pd.to_numeric(frame["avg30_volume"], errors="coerce").replace(0, pd.NA)
    return (volume / avg).tolist()


def _flow(inputs: NameInputs) -> dict:
    """Today's net premium and volume ratio, their rank in the day's universe and in the name's own
    63 sessions, and the `nulls` those four ranks earned.

    The name's own two numbers come from its universe row, else the screener row, else the last row
    of its screener history -- three spellings of the same screener row, in the order the sheet
    trusts them.
    """
    pool = name_universe(inputs.universe_today)
    row = _universe_row(pool, inputs.ticker)
    history = self_history(inputs.screener_history, inputs.date)
    own = history.iloc[-1] if history is not None else None
    net = _first(net_premium(row), net_premium(inputs.screener), net_premium(own))
    ratio = _first(volume_ratio(row), volume_ratio(inputs.screener), volume_ratio(own))
    ranks = {
        "flow_pct_universe": (percentile_rank(net_premium_series(pool), net), pool, "universe"),
        "vol_pct_universe": (percentile_rank(volume_ratio_series(pool), ratio), pool, "universe"),
        "flow_pct_self": (percentile_rank(net_premium_series(history), net), history, "63-session history"),
        "vol_pct_self": (percentile_rank(volume_ratio_series(history), ratio), history, "63-session history"),
    }
    nulls = [{"field": field, "reason": _pool_reason(frame, name)}
             for field, (value, frame, name) in ranks.items() if value is None]
    if net is None:
        nulls.insert(0, {"field": "net_premium",
                         "reason": "no screener row for the name on the date"})
    return {"net_premium": net, "volume_ratio": ratio,
            "universe_n": 0 if pool is None else int(len(pool)),
            "self_n": 0 if history is None else int(len(history)),
            "self_end": None if history is None else history["date"].iloc[-1],
            "nulls": nulls, **{field: value for field, (value, _, _) in ranks.items()}}


def _universe_row(pool: pd.DataFrame | None, ticker: str):
    if pool is None or "ticker" not in pool.columns:
        return None
    rows = pool[pool["ticker"] == ticker]
    return None if rows.empty else rows.iloc[0]


def _first(*values):
    for value in values:
        if value is not None:
            return value
    return None


def _pool_reason(frame, name: str) -> str:
    if frame is None or len(frame) == 0:
        return f"no {name} rows on the date"
    return f"the name has no number of its own to rank in the {name}"
