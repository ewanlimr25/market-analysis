"""Partition layout and read/write helpers shared by every mart table.

Layout: `data/mart/<table>/date=YYYY-MM-DD/part.parquet`. The `date` column is stored inside
the file as well, and readers pass `hive_partitioning=false`, so the directory name is
organization only and the file is self-describing.
"""
from __future__ import annotations

import glob
import os
import re
from datetime import date

import duckdb
import pandas as pd

from engine import config

_DATE_RE = re.compile(r"date=(\d{4}-\d{2}-\d{2})")


def table_dir(table: str) -> str:
    return os.path.join(config.MART, table)


def partition_path(table: str, d: date | str) -> str:
    d = d if isinstance(d, str) else d.isoformat()
    return os.path.join(table_dir(table), f"date={d}", "part.parquet")


def table_glob(table: str) -> str:
    return os.path.join(table_dir(table), "date=*", "part.parquet")


def available_dates(table: str) -> list[date]:
    out = []
    for p in glob.glob(table_glob(table)):
        m = _DATE_RE.search(p)
        if m:
            out.append(date.fromisoformat(m.group(1)))
    return sorted(out)


def has_partition(table: str, d: date | str) -> bool:
    return os.path.exists(partition_path(table, d))


def write_partition(df: pd.DataFrame, table: str, d: date | str) -> str:
    """Atomically (tmp + rename) write one partition; returns the path written."""
    path = partition_path(table, d)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    df.to_parquet(tmp, index=False)
    os.replace(tmp, path)
    return path


def read_partition(table: str, d: date | str) -> pd.DataFrame:
    return pd.read_parquet(partition_path(table, d))


def scan_sql(table: str) -> str:
    """A `read_parquet(...)` fragment for the whole table, usable inside any DuckDB query."""
    return f"read_parquet('{table_glob(table)}', hive_partitioning=false, union_by_name=true)"


def read_table(con: duckdb.DuckDBPyConnection | None, table: str, where: str = "",
               columns: str = "*") -> pd.DataFrame:
    con = con or duckdb.connect()
    q = f"SELECT {columns} FROM {scan_sql(table)}"
    if where:
        q += f" WHERE {where}"
    return con.execute(q).df()
