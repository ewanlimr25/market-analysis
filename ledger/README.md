# ledger/ — the S-A forward ledger (opens 2026-10-01)

`forward_signals.parquet`: one row per (ticker, E, variant, structure) that `make daily` emitted on the
pre-print night, with the entry marks, tiers, size and the legs needed to grade it.
`forward_ledger.parquet`: one row per graded signal, written once at `post`. Rows are never re-derived
from the vendor feed (DESIGN/70 §6). A Season 3 trade that is not in this ledger was never a signal.

## `sb/` — the S-B forward ledger (opens 2026-09-11)

Same two files and the same rules for the VIX-gated SPY/QQQ put spread and iron condor (DESIGN/80 §5.3):
one signal row per (underlying, entry session, structure) emitted on the last session of the week when the
gate is ON, graded once at expiry from the underlying's close (tier-4 intrinsic). `E` and `pre` are the entry
session, `post` the expiry, `variant` is `B1`.
