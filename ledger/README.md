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

## `name/` — the ticker-sheet ledger (three policies in one file)

`findings/stock-deep-dive/DESIGN/70-ticker-sheet-spec.md §6`. The same two files and the same
write-once rule, with the row key `(ticker, E, variant, structure, policy_id, role)`. Three policy
ids share the file and are never pooled (`engine.improve.adjudicate.champion_rows` filters on
`policy_id`, and every read goes through it):

- `sheet-1.0` — one row per sheet, `role = champion` on a `CAN_PRICE` name with no X1 and
  `role = exploration` otherwise, with the failing S-C filter or `X1` in `gate_verdict`; the reward
  is `ror` and the unit is `unit_id` (`"<ticker>:<post>"`), so overlapping same-name rows inside 21
  sessions count once. Read at 40 units (`make adjudicate ARGS="gate --strategy sheet"`), NOT_DUE
  before.
- `disc-1.0` — one row per owner call (`DIRECTION=`), `role = exploration` always; the reward is
  `r_share` on the share leg (and `ror` on the chosen vertical), the unit is the decision date `E`,
  and every row carries `context_read ∈ {none, sheet_only, narrate}` (D13). Read at 70 units and no
  earlier than 2027-03-01 (`make adjudicate ARGS="champion --strategy disc --n-required 70"`).
- `sdd-llm-1.0` — the seeded old deep-dive book (D8): 62 decisions, 125 structures, 9 trade plans
  and their 18 option legs, already graded in `findings/stock-deep-dive/artifacts/outcomes/`, loaded
  once by `python3 -m engine.name.seed` into both files (graded history, emitted so `pending` stays
  consistent) and never re-derived from a live feed. `gate_verdict` is the old skill's own bias
  label; rows that never resolved carry a null `r_share` / `ror` rather than being dropped.
