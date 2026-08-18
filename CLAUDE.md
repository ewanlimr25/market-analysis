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
   recorded baseline** after any lane/threshold change. **Current baseline** (adopted 2026-08-17 on the
   FULL liquid universe, panel→08-17, 89 days, 2,471-ticker spine, post-S4-floor fix): **MOM_LONG −0.0127
   (n=1154) · MOM_SHORT −0.0137 (n=830) · OI_FADE +0.0038 (n=1176) · S2 +0.0014 (n=1210) ·
   S4 +0.0025 (n=1241).** Only S4 moved by code (call-volume floor, +0.0041 → +0.0025 — **artifact removal,
   not decay**; an old-code/new-data control on the same 89-day panel read S4 +0.0048 and the other four
   lanes bit-identical). ⚠️ **Do not read S4's drop as a lane getting worse:** its `hit − base` was already
   negative *before* the fix (−0.041 → −0.056), so S4 has never had a hit-rate edge on this panel — the
   removed names were supplying the right tail. See [`docs/regression-gate.md`](docs/regression-gate.md#s4-re-baseline-00041--00025-2026-08-17--artifact-removal-not-decay).
   ⚠️ **This figure is depressed by a correlated draw.** Two consecutive increments (08-08 and 08-15) have
   been the *same* one-way rally: the 08-15 increment is 317 rows across only **5 exit-days**, with `base`
   pinned at 1.00 for MOM_LONG and 0.00 for both short lanes. When it unwinds the lanes will rise on their
   own — **that recovery is not evidence a fix worked.** A
   baseline is only meaningful against the universe it was measured on — state the spine size whenever you
   record one, and a below-baseline lane is not automatically a regression (panel growth and universe
   changes move the pooled mean independent of code). **This applies to gate-effectiveness figures too,
   not just lanes:** any measured number carries the spine it was measured on, so re-run isolation check
   (c) before citing one across a universe change. The 2026-08-15 audit is the worked example — the crash
   guard's DURABLE p=0.010 was a 785-spine artifact and reads p=0.237 on the full spine. MOM_SHORT is the
   **one** recorded exception to "no
   lane negative-excess" (knowingly negative, watch-only capped); don't add another without the same
   written rationale. Full history, the isolation-check protocol, and the worked examples (2026-08-08
   five-lane drop; 2026-08-15 gate-vs-spine): [`docs/regression-gate.md`](docs/regression-gate.md).
7. **Path-aware outcomes from the Yahoo chart API**, never the close-only `mcp__yahoo-finance__*` tools.

## The validated lanes (priors from research/20, 50, 70)
Historical-panel priors, harness-measured (2026-08-15 baseline, full 2,471-ticker universe). The forward
book is graded separately by `/calibration-audit` and can disagree — no lane has cleared BH(0.10) forward
yet. Full per-lane notes and the 785-spine comparison: [`docs/lanes.md`](docs/lanes.md).

| Lane | Dir | Horizon | Realized (harness) | Status |
|---|---|---|---|---|
| `oi-flow-fade` (OI_FADE) | short | h10 | +0.38% mean / +0.79% median, hit 0.54 vs 0.36, n=1176 | **Sizes — most robust lane** |
| `momentum` MOM_SHORT (near-52w-low) | short | h10 | −1.37% mean, n=830 | Watch-only, crash-gated, never sizes |
| `momentum` MOM_LONG (near-52w-high) | long | h10 | −1.27% mean, n=1154 | Basket/watch only, never sizes |
| `liquidity-reversion` (S2) | long | h3–5 | +0.14%, n=1210 | Advisory-only |
| `sentiment-contrarian` (S4) | long | h5–10 | +0.25%, n=1241 (post call-volume-floor fix) | Advisory-only; **hit − base negative (−0.056) — no hit-rate edge, right-tail only** |
| `vol-book` | non-dir | event/0DTE | VOL-ONLY | Net-of-cost, delta-neutral |
| `fundamentals-gate` | veto | — | risk filter | Finnhub = veto, not alpha (`research/80`) |

## Data & tools
- Panel: `~/Documents/Stocks/{All Options, Dark pool, Hot Option Chains, OI changes, Stock Screener}` (read via `uw` CLI / DuckDB).
- Truth set: `data/{prices,returns,features,weekly_features}.parquet` (built by `scripts/truthset/*`). `edge.py` = the conditional-benchmark resolver.
- `retro_harness.py` = the standing regression gate. `factor_scan.py` = the cross-sectional factor zoo.
- `fz` (Finviz) advisory; `mcp__yahoo-finance__*` NOT for path-aware outcomes.

## Cadence
Nightly `/market-scan` (post-8PM-EST export). Weekend `/weekly-review`. Weekly/per-~10-resolved
`/calibration-audit`. **Next audit due 2026-08-22.** 23 open call-rows (11 OI_FADE, 5 MOM_SHORT, 7 S4),
**174 open suppressed candidates**, and the 08-03→08-07 crash-guard block all mature 08-17→08-22 — the
first genuinely non-overlapping cohort, now deferred twice (08-08 and 08-15 both expected it and both got
a single one-way window instead: 08-15 added only 15 resolved rows across 5 exit-days). Count distinct
**exit-days**, not rows, when judging any cohort
([`docs/regression-gate.md`](docs/regression-gate.md#exit-day-counting-companion-rule)).

## Git
- Name: Ewan · Email: liyuxuan66@hotmail.com. Branch before non-trivial changes; never commit `data/*.parquet`, `analyses/audit/`, or `.env`. **`analyses/weekly/` IS tracked** — the weekly-review journal is versioned (policy changed 2026-07-04). **`analyses/scan/` IS tracked** — the nightly scan journal is versioned and public (policy changed 2026-08-08); commit each night's `report.md` / `decision.json` / `conviction_*.json` with the scan. `analyses/audit/` stays local-only (working files, not a journal).
- **The repo is public** (`github.com/ewanlimr25/market-analysis`). `README.md` is the public-facing entry point — keep the required-data-layout section true if panel paths, filename patterns, or truth-set build order change. Nothing written into `analyses/` should contain a credential or an absolute local path.
