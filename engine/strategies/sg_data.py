"""Data access for the S-G backtest (DESIGN/91 §1, §4).

Reuses `engine.strategies.sa_data`'s loaders by import wherever they are already generic enough:
`load_events`, `load_pre_rows` (called once at the entry day, once at the exit day — S-G's exit
day is literally S-A's own entry day, `pre`), `load_spread_history`, `load_prices`, `load_iv30d`.
The only new piece is a synthetic entry-day events frame (so the `pre`-keyed S-A loaders apply
unmodified at a different date) and a small tier-3 model-input closure.

Simplification versus S-A's wing model-input closure (documented, not a filter change): tier-3 IV
uses the day's own screener `iv30d` directly, without S-A's per-contract smile-ratio adjustment,
which needs a per-contract IV history lookback (`sa_data._latest_contract_iv`). This is expected to
matter little: F5's `size_late >= 10` guarantees a tier-1 mark on every ATM and strangle *entry*
leg (DESIGN/91 §2), so tier 3 is reached only on the exit leg, and `results.md` reports how often.
"""
from __future__ import annotations

from datetime import date

import pandas as pd

from engine import marking as M
from engine.strategies import sa_data
from engine.strategies import sg_filters as G


def load_events(con) -> pd.DataFrame:
    return sa_data.load_events(con)


def with_entry_pre(events: pd.DataFrame, offset: int) -> pd.DataFrame:
    """`events` with `pre` replaced by `entry_day(E, offset)` (DESIGN/91 §1), so `sa_data`'s
    `pre`-keyed loaders (`load_pre_rows`, `load_spread_history`) apply unmodified at the entry day."""
    df = events.copy()
    df["pre"] = df["E"].map(lambda e: G.entry_day(e, offset))
    return df


def load_entry_rows(con, events: pd.DataFrame, offset: int, mcap_lo: float, mcap_hi: float) -> pd.DataFrame:
    """`daily_contract` rows on `entry_day(E, offset)` for every event (DESIGN/91 §1's F5/F6 site)."""
    return sa_data.load_pre_rows(con, with_entry_pre(events, offset), mcap_lo, mcap_hi)


def load_exit_rows(con, events: pd.DataFrame, mcap_lo: float, mcap_hi: float) -> pd.DataFrame:
    """`daily_contract` rows on `pre` (= exit_day, DESIGN/91 §1) — the identical call S-A makes
    for its own entry rows, since S-G's exit day is S-A's entry day."""
    return sa_data.load_pre_rows(con, events, mcap_lo, mcap_hi)


def spread_history(con, events: pd.DataFrame, offset: int) -> dict[tuple[str, date], float]:
    """Median late spread history keyed by (ticker, pre) for the entry day, reusing
    `sa_data.load_spread_history` unmodified on the synthetic entry-day frame."""
    return sa_data.load_spread_history(con, with_entry_pre(events, offset))


def build_model_inputs(prices: dict, iv30d: dict, spreads: dict):
    """Closure for `MarkResolver`: (contract, date, when) -> ModelInputs or None. G3 marks only
    at `late` (the close proxy, DESIGN/91 §2), so the underlying price is always the day's close;
    unlike `sa_data.build_model_inputs` there is no early/late spot branch to reproduce."""
    def inputs(contract: M.Contract, d: date, when: str) -> M.ModelInputs | None:
        px = prices.get((contract.underlying, d))
        if px is None:
            return None
        iv = M.model_iv(iv30d.get((contract.underlying, d)), None, None)
        return M.ModelInputs(spot=px[1], iv=iv, rel_spread=spreads.get((contract.underlying, d)))
    return inputs
