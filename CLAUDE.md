# CLAUDE.md — market-analysis

Excess-scored, regime-first market analysis. Built from the hindsight-validated clean-room research in
`research/` (panel 2026-03-13→06-26) — **read `research/00-orientation.md` before changing any lane's
logic or gates.** Full doc index, including the history behind every rule below: [`docs/README.md`](docs/README.md).

## What this repo is (and is NOT)
- **IS:** a lean engine that scores only the handful of signals that beat SPY out-of-sample, on a conditional
  benchmark, regime-stratified. Price-structure (momentum) + one OI-fade + mean-reversion/sentiment + a
  non-directional vol book. Daily `/market-scan`, weekly `/weekly-review`, forward `/calibration-audit`.
- **IS NOT:** a microstructure flow engine. Raw options flow measured as **beta** here (`research/20`, `70`);
  it is cut, not scored. (That product is `~/Development/uw-daily-analysis`.)

## Non-negotiable invariants
1. **Excess-vs-SPY (conditional same-day benchmark) is the only scoring currency.** Never raw win-rate — the
   tape is long-biased (SPY up 58/63/68/71% at h1/3/5/10), so raw WR is beta in disguise.
2. **No additive confluence.** A name scores on ONE lane's measured excess × regime-fit. Orthogonal lanes that
   agree are noted, never summed (additive confluence produced a −8.2% / 0-for-6 book — `research/50`).
3. **Most days have no directional edge — say so.** The modal output is regime + vol book + watch list.
4. **Half-cap, no auto-full.** No call sizes full until a cross-year edge validates.
5. **Pre-registered ≠ scored.** Weekly technicals and all PR-* items are documented, never sized, until their
   bar clears on data that postdates registration.
6. **Regression gate is law:** `python3 scripts/retro_harness.py --all` must show no lane **below its
   recorded baseline** after any lane/threshold change. **Current baseline** (adopted 2026-08-08 on the
   FULL liquid universe, panel→08-07, 83 days, 2,471-ticker spine): **MOM_LONG −0.0108 (n=1066) ·
   MOM_SHORT −0.0128 (n=803) · OI_FADE +0.0059 (n=1087) · S2 +0.0009 (n=1123) · S4 +0.0035 (n=1145).** A
   baseline is only meaningful against the universe it was measured on — state the spine size whenever you
   record one, and a below-baseline lane is not automatically a regression (panel growth and universe
   changes move the pooled mean independent of code). MOM_SHORT is the **one** recorded exception to "no
   lane negative-excess" (knowingly negative, watch-only capped); don't add another without the same
   written rationale. Full history, the isolation-check protocol, and the 2026-08-08 worked example:
   [`docs/regression-gate.md`](docs/regression-gate.md).
7. **Path-aware outcomes from the Yahoo chart API**, never the close-only `mcp__yahoo-finance__*` tools.

## The validated lanes (priors from research/20, 50, 70)
Historical-panel priors, harness-measured (2026-08-08 baseline, full 2,471-ticker universe). The forward
book is graded separately by `/calibration-audit` and can disagree — no lane has cleared BH(0.10) forward
yet. Full per-lane notes and the 785-spine comparison: [`docs/lanes.md`](docs/lanes.md).

| Lane | Dir | Horizon | Realized (harness) | Status |
|---|---|---|---|---|
| `oi-flow-fade` (OI_FADE) | short | h10 | +0.59% mean / +0.95% median, hit 0.55 vs 0.38, n=1087 | **Sizes — most robust lane** |
| `momentum` MOM_SHORT (near-52w-low) | short | h10 | −1.28% mean, n=803 | Watch-only, crash-gated, never sizes |
| `momentum` MOM_LONG (near-52w-high) | long | h10 | −1.08% mean, n=1066 | Basket/watch only, never sizes |
| `liquidity-reversion` (S2) | long | h3–5 | +0.09%, n=1123 | Advisory-only |
| `sentiment-contrarian` (S4) | long | h5–10 | +0.35%, n=1145 | Advisory-only |
| `vol-book` | non-dir | event/0DTE | VOL-ONLY | Net-of-cost, delta-neutral |
| `fundamentals-gate` | veto | — | risk filter | Finnhub = veto, not alpha (`research/80`) |

## Data & tools
- Panel: `~/Documents/Stocks/{All Options, Dark pool, Hot Option Chains, OI changes, Stock Screener}` (read via `uw` CLI / DuckDB).
- Truth set: `data/{prices,returns,features,weekly_features}.parquet` (built by `scripts/truthset/*`). `edge.py` = the conditional-benchmark resolver.
- `retro_harness.py` = the standing regression gate. `factor_scan.py` = the cross-sectional factor zoo.
- `fz` (Finviz) advisory; `mcp__yahoo-finance__*` NOT for path-aware outcomes.

## Cadence
Nightly `/market-scan` (post-8PM-EST export). Weekend `/weekly-review`. Weekly/per-~10-resolved
`/calibration-audit`. **Next audit due 2026-08-15.** 41 open rows (17 OI_FADE, 12 MOM_SHORT, 11 S4) mature
08-10→08-21, and the 08-03→08-07 crash-guard block matures 08-18→08-22 — the first cohort spanning
non-overlapping windows. Count distinct **exit-days**, not rows, when judging any cohort
([`docs/regression-gate.md`](docs/regression-gate.md#exit-day-counting-companion-rule)).

## Git
- Name: Ewan · Email: liyuxuan66@hotmail.com. Branch before non-trivial changes; never commit `data/*.parquet`, `analyses/audit/`, or `.env`. **`analyses/weekly/` IS tracked** — the weekly-review journal is versioned (policy changed 2026-07-04). **`analyses/scan/` IS tracked** — the nightly scan journal is versioned and public (policy changed 2026-08-08); commit each night's `report.md` / `decision.json` / `conviction_*.json` with the scan. `analyses/audit/` stays local-only (working files, not a journal).
- **The repo is public** (`github.com/ewanlimr25/market-analysis`). `README.md` is the public-facing entry point — keep the required-data-layout section true if panel paths, filename patterns, or truth-set build order change. Nothing written into `analyses/` should contain a credential or an absolute local path.
