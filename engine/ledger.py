"""Forward ledger (DESIGN/70 §6): what `make daily` emitted, and how each signal graded.

Two files under the ledger directory (default `data/`):
  forward_signals.parquet  one row per (ticker, E, variant, structure) emitted on the pre-print
                           night, with the entry marks and the legs needed to grade it later
  forward_ledger.parquet   one row per graded signal, written once at `post`

Rows are never re-derived once written (the `resolved_ledger.py` lesson): `emit` and `grade`
skip keys that already exist and report how many they skipped.
"""
from __future__ import annotations

import os
from datetime import date

import pandas as pd

SIGNALS_FILE = "forward_signals.parquet"
LEDGER_FILE = "forward_ledger.parquet"
KEY = ["ticker", "E", "variant", "structure"]


def _path(ledger_dir: str, name: str) -> str:
    return os.path.join(ledger_dir, name)


def _read(path: str) -> pd.DataFrame:
    return pd.read_parquet(path) if os.path.exists(path) else pd.DataFrame()


def _write(path: str, df: pd.DataFrame) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    tmp = path + ".tmp"
    df.to_parquet(tmp, index=False)
    os.replace(tmp, path)


def _key_frame(df: pd.DataFrame) -> pd.DataFrame:
    return df[KEY].astype(str)


def _new_rows(existing: pd.DataFrame, incoming: pd.DataFrame) -> pd.DataFrame:
    if existing.empty or incoming.empty:
        return incoming
    seen = set(map(tuple, _key_frame(existing).itertuples(index=False)))
    mask = [tuple(k) not in seen for k in _key_frame(incoming).itertuples(index=False)]
    return incoming[mask]


def _append(path: str, rows: pd.DataFrame, stamp_col: str, stamp: date) -> tuple[int, int]:
    existing = _read(path)
    fresh = _new_rows(existing, rows)
    if fresh.empty:
        return 0, len(rows)
    stamped = fresh.assign(**{stamp_col: stamp.isoformat()})
    merged = stamped if existing.empty else pd.concat([existing, stamped], ignore_index=True)
    _write(path, merged)
    return len(fresh), len(rows) - len(fresh)


def read_signals(ledger_dir: str) -> pd.DataFrame:
    return _read(_path(ledger_dir, SIGNALS_FILE))


def read_ledger(ledger_dir: str) -> pd.DataFrame:
    return _read(_path(ledger_dir, LEDGER_FILE))


def emit(ledger_dir: str, candidates: pd.DataFrame, emitted_on: date) -> tuple[int, int]:
    """Append tonight's candidate rows; returns (written, skipped-as-already-present)."""
    if candidates.empty:
        return 0, 0
    return _append(_path(ledger_dir, SIGNALS_FILE), candidates, "emitted_at", emitted_on)


def grade(ledger_dir: str, graded: pd.DataFrame, graded_on: date) -> tuple[int, int]:
    """Append graded rows; a key already in the ledger is never rewritten."""
    if graded.empty:
        return 0, 0
    return _append(_path(ledger_dir, LEDGER_FILE), graded, "graded_at", graded_on)


def pending(ledger_dir: str, post: date) -> pd.DataFrame:
    """Signals whose `post` is the given date and which have no ledger row yet."""
    sig = read_signals(ledger_dir)
    if sig.empty:
        return sig
    due = sig[pd.to_datetime(sig["post"]).dt.date == post]
    return _new_rows(read_ledger(ledger_dir), due)
