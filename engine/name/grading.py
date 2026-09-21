"""The nightly grading step for `ledger/name/` (findings/stock-deep-dive DESIGN/70 §6, R5/R6):
called from `make daily`, grades every `sheet-1.0` / `disc-1.0` signal whose `post` is tonight.

  * option rows (`IB`, `DEBIT_VERTICAL`, ...): intrinsic at the underlying's close on `post`
    (S-C's settlement rule) through `engine.name.grade.grade_vertical` -> `ror`, `pnl_per_share`;
  * share rows (`SHARES`): the ±1R walk `engine.name.grade.walk_shares` from `E` over the horizon
    with `fill = next_open` (§6: entry = next open) -> `r_share`, `outcome`, `event_date`.

Rows are written once through `engine.ledger.grade`; a row whose bars are missing is left pending
(reported in `dropped`) and retried the next night. The bars loader is injectable so the step is
unit-tested on synthetic frames and, in `make daily`, reads the Yahoo cache the watch basket keeps.
"""
from __future__ import annotations

import json
from datetime import date
from typing import Callable

import pandas as pd

from engine import ledger as L
from engine.name import grade as G
from engine.name.ledger_rows import SHARES, DISC_HORIZON_SESSIONS

BarsLoader = Callable[[str, date], pd.DataFrame]
FILL_RULE = "next_open"


def _default_bars(ticker: str, as_of: date) -> pd.DataFrame:
    from engine.watch import bars as B
    return B.load_daily_bars(ticker, as_of=as_of)


def _close_on(bars: pd.DataFrame, d: date) -> float | None:
    if bars is None or bars.empty:
        return None
    on = bars[pd.to_datetime(bars["date"]).dt.date == d]
    return float(on["close"].iloc[-1]) if len(on) else None


def _to_date(v) -> date:
    return v if isinstance(v, date) else date.fromisoformat(str(v)[:10])


def grade_option_row(row: dict, close_post: float) -> dict:
    legs = json.loads(row["legs_json"])
    g = G.grade_vertical([{"right": l["right"], "strike": float(l["strike"]), "side": int(l["side"]), "mark": float(l["mark"])}
                          for l in legs], close_post)
    return {**row, "close_post": close_post, "pnl_per_share": g["payoff_per_share"], "ror": g["ror"],
            "full_credit": g["full_credit"], "at_max_loss": g["at_max_loss"], "outcome": "EXPIRED",
            "r_share": None, "event_date": None, "fill_date": None}


def grade_share_row(row: dict, bars: pd.DataFrame) -> dict:
    w = G.walk_shares(bars, entry_after=_to_date(row["E"]), direction=str(row["direction"]), entry=float(row["entry"]),
                      stop=float(row["stop"]), target=float(row["target"]), horizon_sessions=DISC_HORIZON_SESSIONS,
                      fill=FILL_RULE, through=_to_date(row["post"]))
    return {**row, "outcome": w["outcome"], "r_share": w["r"], "event_date": w["event_date"], "fill_date": w["fill_date"],
            "mfe_r": w["mfe_r"], "mae_r": w["mae_r"], "close_post": w["last_close"], "ror": None,
            "pnl_per_share": None, "full_credit": None, "at_max_loss": None}


def grade_rows(due: pd.DataFrame, d: date, bars_for: BarsLoader) -> tuple[pd.DataFrame, pd.DataFrame]:
    """`(graded, dropped)`: one graded row per due signal with bars through `d`; the rest dropped with a reason."""
    graded, dropped = [], []
    cache: dict[str, pd.DataFrame] = {}
    for row in due.to_dict("records"):
        t = str(row["ticker"])
        bars = cache.setdefault(t, bars_for(t, d))
        if row["structure"] == SHARES:
            if bars is None or bars.empty:
                dropped.append({**row, "reason": "no bars"})
                continue
            graded.append(grade_share_row(row, bars))
            continue
        close_post = _close_on(bars, _to_date(row["post"]))
        if close_post is None:
            dropped.append({**row, "reason": f"no close on {row['post']}"})
            continue
        graded.append(grade_option_row(row, close_post))
    return pd.DataFrame(graded), pd.DataFrame(dropped)


def grade_due(d: date, ledger_dir: str, bars_for: BarsLoader = _default_bars) -> dict:
    """Grade tonight's due rows and append them to `forward_ledger.parquet`; returns counts."""
    due = L.pending(ledger_dir, d)
    if due.empty:
        return {"due": 0, "graded": 0, "skipped": 0, "dropped": 0}
    graded, dropped = grade_rows(due, d, bars_for)
    written, skipped = L.grade(ledger_dir, graded, d) if len(graded) else (0, 0)
    return {"due": int(len(due)), "graded": int(written), "skipped": int(skipped), "dropped": int(len(dropped)),
            "dropped_reasons": [str(r.get("reason")) for r in dropped.to_dict("records")] if len(dropped) else []}
