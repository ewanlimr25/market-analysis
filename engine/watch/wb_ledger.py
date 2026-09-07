"""`ledger/wb/forward_signals.parquet` I/O (DESIGN/110-watch-basket.md §4).

A single file, not the signals/ledger pair `engine.ledger` uses for S-A/S-B: a watch-basket row is
written once with its basket membership and `None` grade columns, then `nightly.grade_open_rows`
fills a grade cell in place once its horizon closes -- so this module's write is a full,
atomic replace of the table (`os.replace` on a temp file, same pattern as `engine.ledger`), never
an append-only file. `WB_KEY` is the ledger key contract DESIGN/110 §4 names: "the ledger key
already includes policy and role."
"""
from __future__ import annotations

import os

import pandas as pd

SIGNALS_FILE = "forward_signals.parquet"
WB_KEY = ["ticker", "date", "basket", "policy_id", "role"]


def ledger_path(ledger_dir: str) -> str:
    return os.path.join(ledger_dir, SIGNALS_FILE)


def read_ledger(ledger_dir: str) -> pd.DataFrame:
    path = ledger_path(ledger_dir)
    return pd.read_parquet(path) if os.path.exists(path) else pd.DataFrame()


def write_ledger(ledger_dir: str, df: pd.DataFrame) -> None:
    path = ledger_path(ledger_dir)
    os.makedirs(ledger_dir, exist_ok=True)
    tmp = path + ".tmp"
    df.to_parquet(tmp, index=False)
    os.replace(tmp, path)
