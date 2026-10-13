"""UW's Stock Screener export, read under the column names the engine was written against.

The export changed on 2026-10-12 (findings market-analysis D37): `is_index` was folded into `issue_type`
(index rows now carry 'Index'), `total_volume`, the session's share volume, became `stock_volume`, and about
150 columns were added. Readers keep asking for the old names; these helpers answer them from whichever form
the files hold. Every older row reads as it did: across the 127 exports from 2026-03-13 to 10-09 no row has a
null `is_index` with an 'Index' type, so `COALESCE(is_index, issue_type = 'Index')` returns the stored flag.
A scan that spans both formats needs `read_parquet(..., union_by_name=true)`.
"""
from __future__ import annotations

import duckdb
import pandas as pd

RENAMED = {"total_volume": "stock_volume"}      # old name -> its name from 2026-10-12
INDEX_TYPE = "Index"                            # `is_index` from 2026-10-12: `issue_type = 'Index'`


def _coalesce(name: str, forms: list[str]) -> str:
    if not forms:
        return f"NULL AS {name}"
    return f"{forms[0]} AS {name}" if len(forms) == 1 else f"COALESCE({', '.join(forms)}) AS {name}"


def _column(name: str, present: set[str]) -> str:
    if name in RENAMED:
        return _coalesce(name, [f for f in (name, RENAMED[name]) if f in present])
    if name == "is_index":
        return _coalesce(name, (["is_index"] if "is_index" in present else [])
                         + ([f"issue_type = '{INDEX_TYPE}'"] if "issue_type" in present else []))
    return name


def select_list(con: duckdb.DuckDBPyConnection, source: str, columns) -> str:
    """The SQL select list for `columns` over `source` (a `read_parquet(...)` call), each old name
    answered from whichever of its forms the files hold."""
    present = {row[0] for row in con.execute(f"DESCRIBE SELECT * FROM {source}").fetchall()}
    return ", ".join(_column(c, present) for c in columns)


def with_old_names(df: pd.DataFrame) -> pd.DataFrame:
    """A screener frame read whole (`SELECT *`) with the old names filled in from the new format; a new
    frame, and the old-format frame itself when there is nothing to fill."""
    extra = {}
    if "total_volume" not in df.columns and RENAMED["total_volume"] in df.columns:
        extra["total_volume"] = df[RENAMED["total_volume"]]
    if "is_index" not in df.columns and "issue_type" in df.columns:
        extra["is_index"] = df["issue_type"].eq(INDEX_TYPE)
    return df.assign(**extra) if extra else df
