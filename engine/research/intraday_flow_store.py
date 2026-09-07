"""Partition read/write for G2's own intermediates under `data/backtest/g2_events/` and
`data/backtest/g2_path/` -- deliberately NOT `engine.mart.store`, whose `table_dir` points at
`data/mart` (a symlink into the shared, gitignored `market-analysis` data directory this worktree
must not write into). Layout mirrors `mart/store.py`: `<table>/date=YYYY-MM-DD/part.parquet`.
"""
from __future__ import annotations

import glob
import os
import re
from datetime import date

import pandas as pd

from engine import config

BACKTEST_DIR = os.path.join(config.DATA, "backtest")
EVENTS_TABLE = "g2_events"
PATH_TABLE = "g2_path"
_DATE_RE = re.compile(r"date=(\d{4}-\d{2}-\d{2})")


def table_dir(table: str) -> str:
    return os.path.join(BACKTEST_DIR, table)


def partition_path(table: str, d: date) -> str:
    return os.path.join(table_dir(table), f"date={d.isoformat()}", "part.parquet")


def has_partition(table: str, d: date) -> bool:
    return os.path.exists(partition_path(table, d))


def write_partition(df: pd.DataFrame, table: str, d: date) -> str:
    """Atomically (tmp + rename) write one day's partition; returns the path written."""
    path = partition_path(table, d)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    df.to_parquet(tmp, index=False)
    os.replace(tmp, path)
    return path


def read_partition(table: str, d: date) -> pd.DataFrame:
    return pd.read_parquet(partition_path(table, d))


def available_dates(table: str) -> list[date]:
    pattern = os.path.join(table_dir(table), "date=*", "part.parquet")
    out = []
    for p in glob.glob(pattern):
        m = _DATE_RE.search(p)
        if m:
            out.append(date.fromisoformat(m.group(1)))
    return sorted(out)


def read_table(table: str, dates: list[date] | None = None) -> pd.DataFrame:
    """Concatenate every available partition (or just `dates`) into one frame; empty if none."""
    want = dates if dates is not None else available_dates(table)
    frames = [read_partition(table, d) for d in want if has_partition(table, d)]
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()
