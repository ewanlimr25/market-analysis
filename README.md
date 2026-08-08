# market-analysis

An excess-scored, regime-first market analysis engine, and the public journal of what it decided.

Most equity "signals" are beta wearing a costume. This repo exists to keep only the handful that
survive being measured against a **conditional same-day SPY benchmark**, and to publish the running
record — including the many days the honest answer was *no edge today*.

> **Not investment advice.** This is a personal research log. Every number here is a measurement on a
> short historical panel, published so the method can be checked, not so it can be followed. Nothing in
> `analyses/` is a recommendation. Past measured excess is not a forecast.

---

## The idea in one section

The tape is steeply long-biased — on the study panel SPY closed up in **58 / 63 / 68 / 71%** of forward
windows at h = 1 / 3 / 5 / 10 trading days. So a strategy reporting a "68% win rate" at h5 has, on the
evidence, demonstrated nothing at all. It matched the coin.

Everything here is therefore scored in one currency:

```
excess = ticker_forward_return − SPY_return_over_the_same_window
```

and the reported statistic is always `hit − base`, never `hit`.

Five commitments follow from that, and they are enforced in code, not just prose:

1. **Excess-vs-SPY on the conditional benchmark is the only scoring currency.** Never raw win rate.
2. **No additive confluence.** A name scores on *one* lane's measured excess × regime fit. Stacking
   correlated flow signals manufactures conviction out of shared beta — the version of this engine that
   did so produced a top-tier book that realized **−8.2% excess, 0-for-6**.
3. **Most days have no directional edge — and the report has to say so.** The modal output is a regime
   read, a non-directional vol book, and a watch list. Long stretches of zero new positions are the
   system working, not the system idling.
4. **Pre-registered ≠ scored.** Candidate features are written down with their bar *before* they are
   tested, and carry zero weight until they clear it on data that postdates registration.
5. **A standing regression gate.** `scripts/retro_harness.py --all` re-measures every lane on the full
   panel. No lane change ships if a lane falls below its recorded baseline — and a below-baseline lane
   must first be proven to be real decay rather than panel growth (see *The regression gate* below).

### The lanes

| Lane | Direction | Horizon | What it fires on |
|---|---|---|---|
| `oi-flow-fade` | short | h10 | heavy multi-day **net call** open-interest build → subsequent underperformance |
| `momentum` (long leg) | long | h10 | near-52-week-high, basket only — **never sizes per-name** |
| `momentum` (short leg) | short | h10 | near-52-week-low, crash-regime-gated, watch-only cap |
| `liquidity-reversion` | long | h3–5 | extreme one-sided dark-pool dollar concentration, news-gated |
| `sentiment-contrarian` | long | h5–10 | fade a put-heavy (high put/call) crowd |
| `vol-book` | non-directional | event / 0DTE | earnings IV crush, 0DTE variance-risk-premium — quoted net of cost |
| `fundamentals-gate` | veto only | — | fundamentals are a risk filter here, not a source of alpha |

Per-lane measured excess, sample sizes, and the caveats attached to each live in `CLAUDE.md` and are
re-baselined on every audit cycle. They are **historical-panel priors**; the forward book is graded
separately and can disagree.

This is deliberately **not** a microstructure options-flow engine. Raw flow was measured here and came
back as beta, so it is used as a filter and cut from scoring.

---

## Required data layout

The engine reads from **two** places: an external end-of-day panel it does not own, and a derived truth
set it builds itself. Neither is committed to this repo.

### 1. The external EOD panel (you must supply this)

Five daily Parquet exports, one directory per group, filenames stamped with the trade date. The default
root is `~/Documents/Stocks`:

```
~/Documents/Stocks/
├── All Options/        bot-eod-report-YYYY-MM-DD.parquet
├── Dark pool/          dp-eod-report-YYYY-MM-DD.parquet
├── Hot Option Chains/  hot-chains-YYYY-MM-DD.parquet
├── OI changes/         chain-oi-changes-YYYY-MM-DD.parquet
└── Stock Screener/     stock-screener-YYYY-MM-DD.parquet
```

The directory names, the filename prefixes, and the `-YYYY-MM-DD.parquet` suffix are all load-bearing —
`scripts/preflight.py` and `scripts/truthset/build_features.py` glob on exactly these patterns.

The panel is sourced from [Unusual Whales](https://unusualwhales.com) via a local `uw` CLI. Any provider
works if the exports carry equivalent columns; the screener spine needs at least `date, ticker, sector,
marketcap, close, prev_close, put_call_ratio, iv_rank, iv30d, week_52_high, week_52_low, call_open_interest,
put_open_interest, total_volume, avg30_volume, net_call_premium, net_put_premium, issue_type`.

`issue_type` is what separates common stock from ETFs, leveraged ETPs, and SPACs. Skipping that filter is
not cosmetic — an unfiltered universe inflated one lane's measured edge by roughly 2× with 3× inverse
sector ETFs the live engine would never trade.

### 2. The derived truth set (built locally, git-ignored)

```
data/
├── universe.json           ← tracked; the ticker spine
├── prices.parquet          ← daily OHLC + adjclose from the Yahoo chart API
├── returns.parquet         ← forward returns, excess-vs-SPY, path-aware MFE/MAE, ATR-based R
├── features.parquet        ← ~40 candidate factors joined across all five panel sources
└── weekly_features.parquet ← weekly candle resample + structure features
```

Build in this order — each step depends on the previous:

```bash
python3 scripts/truthset/build_prices.py      # → data/prices.parquet   (network: Yahoo chart API)
python3 scripts/truthset/build_returns.py     # → data/returns.parquet
python3 scripts/truthset/build_features.py    # → data/features.parquet (reads the external panel)
python3 scripts/truthset/weekly_features.py   # → data/weekly_features.parquet
```

`build_prices.py` defaults its end date to **today** rather than a constant, on purpose: a hardcoded end
date once let the panel sit five sessions stale while every lane still read from it and one returned an
inverted regime. Override with `--end YYYY-MM-DD` or `TRUTHSET_END` only when you mean to.

**Always run the preflight before scanning.** It is the check that catches both silent corruptions —
a missing or empty panel export, and a truth set that does not reach the trade date:

```bash
python3 scripts/preflight.py --date YYYY-MM-DD    # exit 0 = clear, 1 = a lane could misread
```

### 3. Credentials

Two optional keys, resolved from the process environment first, then a repo-root `.env`
(`KEY=VALUE`, never committed):

| Key | Used by | Needed for |
|---|---|---|
| `FINNHUB_API_KEY` | `scripts/finnhub_enrich.py` | the fundamentals veto gate |
| `FRED_API_KEY` | `scripts/fred_macro.py` | macro context in the regime classifier |

Price and outcome data come from the public Yahoo chart API and need no key. Environment overrides:
`TRUTHSET_END` (truth-set end date), `UW_PARQUET_DIR` (0DTE chain directory).

---

## Repo layout

```
.claude/
  agents/          one sub-agent per lane, plus the regime classifier and the risk sizer
  commands/        /market-scan, /weekly-review, /calibration-audit
analyses/
  scan/YYYY-MM-DD/     nightly report.md + decision.json + conviction snapshot   (tracked)
  weekly/YYYY-Www/     weekly review report.md + decision.json                   (tracked)
  audit/YYYY-MM-DD/    forward calibration working files                    (local-only)
data/                  the truth set — see above                            (local-only)
research/              the clean-room study the engine was built from
schemas/               JSON Schema for the decision envelope (v2) and the weekly review
scripts/               helper scripts + the regression harness
  truthset/            truth-set builders and the canonical excess resolver
tests/                 pytest; unit and integration markers
```

### Reading the published journal

`analyses/scan/` and `analyses/weekly/` are the point of publishing this repo. Each dated directory holds:

- **`report.md`** — the human read: regime, vol state, breadth, what fired, and what was blocked and why.
- **`decision.json`** — the machine-readable envelope (schema v2, validated by
  `scripts/validate_decision.py`): every call with its lane, direction, horizon, `validated_excess`,
  regime fit, size, invalidation level, and the gates it passed. `lane_status` records the lanes that
  produced *nothing*, and why — which is the part most systems quietly discard.
- **`conviction_*.json`** — the open-position snapshot carried into the next session.

A large fraction of these days record zero new positions. That is the honest output of the method and it
is published unedited, alongside the days that worked and the days that did not.

---

## Cadence

| When | Command | Emits |
|---|---|---|
| Nightly, after the EOD export | `/market-scan` | `analyses/scan/<date>/` |
| Weekend | `/weekly-review` | `analyses/weekly/<iso-week>/` |
| Weekly, or per ~10 resolved calls | `/calibration-audit` | `analyses/audit/<date>/` (propose-only) |

The audit is deliberately **propose-only**: it grades the forward book, recalibrates priors, and writes
proposals. Nothing it finds changes a lane until the change is applied by hand and the regression gate
passes.

### The regression gate

```bash
python3 scripts/retro_harness.py --all
```

Every lane, re-measured on the full panel. A lane below its recorded baseline is *not* automatically a
regression — the pooled mean moves on its own as the panel grows, because a signal day only enters the
aggregate once its forward window matures. Two isolation checks have to run first:

1. **Old code, new data** — run the baseline commit's harness against the current panel. If the old code
   also reproduces the drop, the code is not the cause.
2. **Cohort split by maturity edge** — rows that had already matured at the previous baseline must still
   reproduce the previous numbers to the last digit.

Only when both pass is a below-baseline lane real decay. The worked example is instructive: on one cycle
**all five lanes fell at once**, and it was a single correlated draw — every new row exited into the same
week-long rally, so SPY rose in 100% of the new windows. Five lanes did not independently decay; one rally
out-ran all five. When an increment's benchmark base rate is pinned at 0.00 or 1.00 rather than mid-range,
its true sample size is the number of distinct **exit days**, not the number of rows.

---

## Requirements

- Python 3.12+
- `duckdb` (the query engine for every panel read), `jsonschema` (envelope validation), `pytest` (tests)
- Everything else is standard library — no pandas, no dotenv
- The five daily panel exports described above
- Optional: [Claude Code](https://claude.com/claude-code), which is what drives the `/market-scan`,
  `/weekly-review`, and `/calibration-audit` workflows in `.claude/`

```bash
python3 -m pytest              # all tests
python3 -m pytest -m unit      # fast, no network or panel dependency
```

---

## Honest limitations

- **The panel is short.** The study window is months, not years. Every excess figure here is a
  small-sample estimate and is labeled as such — `ANECDOTE`, `PROVISIONAL-N`, `DURABLE-N`.
- **Overlapping windows overstate N.** Ten signals that all exit on the same day are close to one
  observation. The audit aggregates to clusters before computing means, t-statistics, or false-discovery
  corrections; per-name statistics would fake the sample size and manufacture false stop signals.
- **One lane is knowingly negative.** The momentum short leg carries negative mean excess and is kept
  watch-only and unsized rather than deleted, because it is a real measurement worth continuing to track.
  It is documented as an exception, not hidden in an average.
- **No position sizes full.** Half-cap across the board until a cross-year edge validates.
- **Nothing here is backtested across a full cycle.** The engine has not yet been graded at durable
  sample size on non-overlapping forward windows.

## License

No license is granted. Published for inspection and discussion; not for redistribution or use as a
trading system.
