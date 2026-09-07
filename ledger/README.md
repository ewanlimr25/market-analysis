# ledger/ — the S-A forward ledger (opens 2026-10-01)

Every row in every ledger file carries `policy_id` (the parameter set that produced it; the champion ids
`sa-1.0` / `sb-1.0` are pinned in `engine/config.py` beside the frozen parameters), `role` (`champion`,
`challenger`, `exploration`) and `gate_verdict` (the gate code printed that night; `PASS` for S-A champion
rows). The row key includes `(policy_id, role)`, so two policies never share a row and are never pooled
(`findings/market-analysis/DESIGN/100 §3`).

`forward_signals.parquet`: one row per (ticker, E, variant, structure, policy_id, role) that `make daily` emitted on the
pre-print night, with the entry marks, tiers, size and the legs needed to grade it.
`forward_ledger.parquet`: one row per graded signal, written once at `post`. From 2026-10-01 the S-A files also
hold the **exploration book** (`role = exploration`, `DESIGN/100 §6`): one contract per structure for every
priceable event in the load band, `gate_verdict` = the first failing filter or `PASS`.

## `challengers/` and `adjudications/`

`challengers/<policy_id>.json` is a registered challenger (one open per strategy; `scripts/adjudicate.py register`).
`adjudications/<name>.json` is a verdict written once (`run`, `champion`, `gate`), with `LOG.md` as the running
index. Neither is ever edited by hand. Rows are never re-derived
from the vendor feed (DESIGN/70 §6). A Season 3 trade that is not in this ledger was never a signal.

## `sb/` — the S-B forward ledger (opens 2026-09-11)

Same two files and the same rules for the VIX-gated SPY/QQQ put spread and iron condor (DESIGN/80 §5.3):
one signal row per (underlying, entry session, structure) emitted on the last session of the week when the
gate is ON, graded once at expiry from the underlying's close (tier-4 intrinsic). `E` and `pre` are the entry
session, `post` the expiry, `variant` is `B1`. From 2026-09-11 the same file also holds the **exploration
book** (`role = exploration`): one contract per sleeve on every entry day regardless of the gate, with the
gate's verdict on the row, so the gate is graded at the 12-01 read (`DESIGN/100 §6`).

## `wb/` — the watch-basket forward ledger (opens 2026-09-08)

`findings/market-analysis/DESIGN/110-watch-basket.md`, R2/R3. Exploration-only, paper rows, `policy_id =
"wb-1.0"`, `role = exploration` always -- this book has no champion or gate to compare against. A single
file, `forward_signals.parquet` (row key `ticker, date, basket, policy_id, role`), one row per (name,
night, basket) for LONG/SHORT/VOL that basket-qualified that night (CONFLICT is logged in `signals.json`
only, never written here, DESIGN/110 §3); `gate_verdict` is `"<basket>:<bull>/<bear>:<comma-separated true
condition ids>"`. Unlike every other ledger file, a row here is not append-only end to end: it is written
once with `excess_h5`/`excess_h10`/`excess_h21` all null, and `engine.watch.nightly.grade_open_rows` fills
one of those three cells in place, once, the first night its horizon's session has closed (a filled cell is
never touched again). `episode` is `false` on a re-entry into the same basket within 21 sessions
(DESIGN/110 §4) -- a continuation, still written, but not counted as a new independent unit by the R3 read
(`engine/improve/basket_read.py`, `make adjudicate ARGS="basket --policy wb-1.0"`). The read itself writes
to `ledger/adjudications/wb-1.0-<basket>.json`, same as every other verdict above.
