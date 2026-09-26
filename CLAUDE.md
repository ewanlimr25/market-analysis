# CLAUDE.md — market-analysis

A deterministic options-premium engine (`engine/`, driven by `make`) and its public, append-only record.
No model call sits in the decision path: every number comes from a query or a pure function.

- **Operator's guide:** [`docs/OPERATING.md`](docs/OPERATING.md) — the nightly and weekend routine, how to read
  every report, the calendar, failure handling. Read it before running or changing anything.
- **Module map:** [`engine/README.md`](engine/README.md).
- **Why, and every decision:** `~/Development/findings/market-analysis/` — design specs (`DESIGN/70` S-A,
  `80` S-B, `90` S-C, `100` the improvement process, `110` the watch basket, `stock-deep-dive/DESIGN/70` the
  ticker sheet), backtests (`RESEARCH/45`–`49`), `DECISIONS.md`, and the hand-off note `NEXT-SESSION.md`.
  Findings, plans and decisions are written there, not here.
- **`legacy/`** is the frozen Claude Code fleet (`/market-scan`, `/weekly-review`, `/calibration-audit`, the
  lane agents, their scripts, docs and June research). History only: do not run it, edit it, or cite its lane
  numbers as live (`legacy/README.md`).

## Non-negotiable rules

1. **No parameter moves before its read.** Every strategy value lives in `engine/config.py` and is pinned by a
   test (`tests/test_frozen_params.py`, `test_sb_frozen_params.py`, `test_sc_frozen_params.py`, the name
   specs). If a change makes one fail, the change is wrong, not the test. New ideas go to the strategy's idea
   ledger; a strategy changes only through one registered challenger, run in shadow and adjudicated once on
   its date (`DESIGN/100`, `docs/OPERATING.md §6a`).
2. **Ledgers are append-only.** A graded row is the record of that day's marks. Never re-derive, rewrite or
   delete a row in `ledger/`, and never edit a published `analyses/` report; a wrong number is recorded in
   findings' `DECISIONS.md`.
3. **Nothing trades real money before the read** (S-B 2026-12-01; S-C at 40 graded forward entry-weeks per
   pair). Sizing lines show what one contract would risk.
4. **Rows are never pooled across `policy_id` or `role`** (`champion`, `challenger`, `exploration`).
5. **The engine emits no direction on a single name.** The ticker sheet describes; a direction is the owner's
   `DIRECTION=` call, priced into its own book.
6. **Refresh the truth set before running past it.** `prices` / `returns` / `features` and `intraday_rv` are
   manual rebuilds (`docs/OPERATING.md §4`); a stale truth set silently ages every regime label and pushes
   settlement onto the last-print fallback.
7. **Owner decisions stay the owner's.** When a spec leaves a choice open, propose a default in findings'
   `DECISIONS.md` and wait; do not pick one in code.

## Commands

```
make daily DATE=YYYY-MM-DD       # the nightly; ~2 s plus the watch basket
make test                        # the unit suite; must stay green
make backtest-sb REFRESH=1 && make report-sb     # weekend, S-B scorecard -> data/backtest/sb_report.md
make backtest-sc && make report-sc               # weekend, S-C scorecard -> data/backtest/sc_report.md
make ticker T=NVDA [DATE=] [DIRECTION=long|short] # one-name sheet
make adjudicate ARGS="..."       # challenger / champion / gate / basket reads; NOT_DUE before their dates
```

Never run on your own: `make mart` (full rebuild), `make index-vol`, `--force-ledger`, `make seed-name`.

## Data

- Panel: `~/Documents/Stocks/{All Options, Dark pool, Hot Option Chains, OI changes, Stock Screener}`
  (`UW_STOCKS_DIR` overrides). Read-only; never modify it.
- Truth set: `data/{prices,returns,features}.parquet` from `scripts/truthset/build_*.py`; `edge.py` is the
  conditional-benchmark resolver. Marts: `data/mart/`, appended by the nightly and the launchd loaders.
- Keys: `FINNHUB_API_KEY` from the environment or a repo-root `.env`. Read keys by name only; never write a
  key value into any file.

## Git

- Name: Ewan · Email: liyuxuan66@hotmail.com.
- **The repo is public** (`github.com/ewanlimr25/market-analysis`). Nothing in `analyses/`, `ledger/` or a
  commit may contain a credential or an absolute local path. Never commit `data/*.parquet`, `data/mart/`,
  `analyses/audit/`, `analyses/ticker/*/*/inputs/`, `legacy/local/` or `.env`.
- Tracked and committed each night: `analyses/daily/`, `ledger/`. Each weekend: `data/backtest/*.md`.
  `analyses/scan/` and `analyses/weekly/` are the frozen journal (read-only).
- `README.md` is the public entry point: keep its data-layout section true when panel paths, filename
  patterns or the truth-set build order change.
