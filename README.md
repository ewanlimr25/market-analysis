# market-analysis

A deterministic options-premium research engine, and the public, append-only record of what it measured.

Most equity "signals" are beta wearing a costume. This repo keeps only what survives being measured
after costs, on real option marks, against a bar written down before the data arrived, and it publishes
the running record, including the long stretches where the honest answer is *nothing clears*.

> **Not investment advice.** This is a personal research log. Every number here is a measurement on a
> short panel, published so the method can be checked, not so it can be followed. Nothing in `analyses/`
> or `ledger/` is a recommendation, and nothing trades real money before the first read on 2026-12-01.

**Running it day to day:** [`docs/OPERATING.md`](docs/OPERATING.md) (what to type, how to read the reports,
the calendar, what to do when something is off). **Module map:** [`engine/README.md`](engine/README.md).
**Why it is built this way:** `~/Development/findings/market-analysis/` (design specs, backtests, decisions).

---

## What the engine does

`make daily DATE=YYYY-MM-DD` runs once per session after the end-of-day export. No model call anywhere:
every number comes from a query or a pure function, every parameter is frozen by a test until its read, and
the ledgers are append-only. On each night it runs:

| Strategy | What | Status |
|---|---|---|
| **S-A** | earnings short-vol on mid-caps (straddle / iron condor through the print) | net negative after costs in Seasons 1 and 2; its Season 3 ledger (from 2026-10-01) is measurement only |
| **S-B** | VIX-gated SPY and QQQ put spreads and iron condors, entered Fridays about 21 days out | paper ledger since 2026-09-11; SPY put spread clears the pre-registered bar in backtest; read 2026-12-01 |
| **S-C** | single-name short premium ($1–20B, 30–80% IV), short straddle and iron butterfly about 28 days out | built 2026-09-26; ledger opens 2026-10-02; read at 40 graded entry-weeks per pair (around 2027-10) |
| **wb-1.0** | the watch basket: 20 stacked technical / flow conditions, graded at h5 / h10 / h21 | exploration only; read at the later of 2026-12-01 and 100 episodes |

Alongside the nightly: `make ticker T=NVDA` prints a one-name sheet (can it be priced, next earnings,
premium label, 1σ ranges, borrow and positioning, a structure menu) and never emits a direction. A
direction is the operator's call, priced and graded in its own book (`DIRECTION=long|short`).

Every ledger row carries a `policy_id`, a `role` (`champion`, `challenger`, `exploration`) and the gate's
verdict, so a filter is graded against what it refused. A strategy changes in one way only: one registered
challenger, run in shadow, adjudicated once on a pre-set date (`docs/OPERATING.md §6a`).

---

## Required data

The engine reads an external end-of-day panel it does not own, and builds everything else itself. None of
the data is committed.

### 1. The external EOD panel (you supply this)

Daily Parquet exports, one directory per group, filenames stamped with the trade date. The root defaults to
`~/Documents/Stocks` (override with `UW_STOCKS_DIR`):

```
~/Documents/Stocks/
├── All Options/        bot-eod-report-YYYY-MM-DD.parquet
├── Dark pool/          dp-eod-report-YYYY-MM-DD.parquet
├── Hot Option Chains/  hot-chains-YYYY-MM-DD.parquet
├── OI changes/         chain-oi-changes-YYYY-MM-DD.parquet
└── Stock Screener/     stock-screener-YYYY-MM-DD.parquet
```

Directory names, filename prefixes and the `-YYYY-MM-DD.parquet` suffix are load-bearing:
`scripts/preflight.py`, the marts and `scripts/truthset/build_features.py` glob on exactly these patterns.
The panel is sourced from [Unusual Whales](https://unusualwhales.com); any provider works if the exports
carry equivalent columns. The screener's `issue_type` separates common stock from ETFs, leveraged ETPs and
SPACs, and skipping it is not cosmetic.

### 2. The truth set and the marts (built locally, gitignored)

```
data/
├── universe.json        ← tracked; the ticker spine
├── watch_names.txt      ← tracked; names the CBOE chain loader fetches nightly
├── prices.parquet       ← daily OHLC + adjclose from the Yahoo chart API
├── returns.parquet      ← forward returns, excess vs SPY
├── features.parquet     ← candidate factors joined across the panel
├── mart/                ← daily_contract, earnings_events, index_vol, intraday_rv, cboe_chain, borrow, ...
└── backtest/            ← backtest outputs; the *.md reports are tracked
```

The truth set is a manual rebuild, not part of `make daily`. Build it in order, and refresh it every weekend:

```bash
python3 scripts/truthset/build_prices.py      # network: Yahoo chart API; end date defaults to today
python3 scripts/truthset/build_returns.py
python3 scripts/truthset/build_features.py    # reads the external panel
```

`make daily` appends the night's marts itself and runs the preflight first (a missing or empty export, or a
truth set that does not reach the trade date, stops the run). The SPY/QQQ chains, Reg SHO, IBKR borrow and
FINRA short interest are fetched by two scheduled loaders (`make loaders`, `make loaders-weekly`; launchd
setup in `docs/OPERATING.md §1`).

### 3. Credentials

One optional key, resolved from the environment first, then a repo-root `.env` (`KEY=VALUE`, never
committed):

| Key | Used by | Needed for |
|---|---|---|
| `FINNHUB_API_KEY` | `engine/name/`, `engine/mart/earnings_history.py` | the ticker sheet's earnings-date cross-check and `make narrate`; the earnings-history mart |

Prices, VIX-family indices, option chains, short interest and borrow come from public endpoints with no key.

---

## Repo layout

```
engine/              the engine: marts, strategies, validation harnesses, ledgers, the nightly and the ticker sheet
scripts/             truth-set builders, preflight, the live helpers the engine imports, one-off research runners
  truthset/          prices / returns / features / universe builders and the conditional-excess resolver
schemas/             signals.json (d1.x), ticker.json, and the frozen journal's decision / weekly-review schemas
tests/               pytest; `make test` runs the unit suite
ledger/              forward ledgers, committed and append-only: sb/, sc/, wb/, name/, challengers/
analyses/
  daily/<date>/      the nightly report.md + signals.json                       (tracked)
  ticker/<T>/<date>/ one ticker sheet: ticker.json, report.md                    (tracked; inputs/ local)
  scan/, weekly/     the frozen journal of the old Claude Code fleet, 2026-06-22 to 2026-09-04 (read-only)
ops/launchd/         the two loader LaunchAgents
docs/OPERATING.md    the operator's guide
legacy/              the frozen Claude Code fleet: agents, commands, scripts, docs, June research (legacy/README.md)
```

### Reading the record

- **`analyses/daily/<date>/report.md`** — one page per session: preflight, S-A candidates and suppressions,
  the S-B gate and any positions (strikes, expiry, credit, max loss), the S-C and watch-basket sections,
  what was graded. `signals.json` beside it is the machine copy, pinned by `schemas/signals.schema.json`.
- **`data/backtest/sb_report.md`, `sc_report.md`** — the weekly scorecards: whether each sleeve still
  clears its pre-registered bar. They score the rule, not individual positions.
- **`ledger/`** — every paper position with its marks and, at expiry, its graded P&L. A graded row is never
  re-derived, even if the vendor later retracts data.

Most nights write nothing to a ledger. That is the method working, and it is published unedited.

---

## Requirements

- Python 3.12+
- `pandas`, `numpy`, `duckdb` (every panel read), `scipy`, `jsonschema`, `pytest`
- The daily panel exports described above

```bash
make test                        # the unit suite; also proves no frozen parameter moved
python3 -m pytest -m integration # touches the panel, the truth set or the network
```

---

## Honest limitations

- **The panel is short.** Real option marks start 2026-03-13. S-B's three-year history is a proxy priced from
  CBOE vol indices with a fixed smile; the marked panel checks it but covers months, not cycles.
- **Backtests are in-sample by construction.** The bars were written before the forward ledgers opened, and
  only the forward ledger can move a verdict. Before the reads, every positive number here is a candidate.
- **Short premium has a fat left tail.** Means are reported beside the worst positions, the worst month,
  and the mean without the worst 1%.
- **Overlapping positions overstate N.** Weekly entries overlap three- to four-deep; t-statistics are
  Newey-West or clustered by expiry, and multiple sleeves are charged through BH and a deflated Sharpe.
- **Paper, not fills.** Entries are marked at late-window prints with a half-spread cost per leg; a live
  fill can be worse.

## License

[MIT](LICENSE) — use, modify, and redistribute freely, keeping the copyright and permission notice.

The license covers the code and the writing. It does not make any measurement here more reliable than
the *Honest limitations* section says it is, and it disclaims all warranty and liability: if you run this
or trade off it, that is entirely your own risk.
