# ledger/ — the S-A forward ledger (opens 2026-10-01)

`forward_signals.parquet`: one row per (ticker, E, variant, structure) that `make daily` emitted on the
pre-print night, with the entry marks, tiers, size and the legs needed to grade it.
`forward_ledger.parquet`: one row per graded signal, written once at `post`. Rows are never re-derived
from the vendor feed (DESIGN/70 §6). A Season 3 trade that is not in this ledger was never a signal.
