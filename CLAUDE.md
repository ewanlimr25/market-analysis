# CLAUDE.md — market-analysis

Excess-scored, regime-first market analysis. Built from the hindsight-validated clean-room research in
`research/` (panel 2026-03-13→06-26). **Read `research/README`-equivalents and `PLAN.md` before changing anything.**

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
6. **Regression gate is law:** `python3 scripts/retro_harness.py --all` must show no lane **below its recorded
   baseline** after any lane/threshold change. **Baseline (2026-07-24, commit `2b32bad`, panel→07-24):**
   MOM_LONG +0.0018 · **MOM_SHORT −0.0003** · OI_FADE +0.0070 · S2 +0.0006 · S4 +0.0044.
   MOM_SHORT is *knowingly* negative: `2b32bad` fixed the **measuring instrument** (calendar→trading-day
   earnings window on all lanes; OI_FADE had no ETP/earnings hygiene at all), exposing a lane that was always
   ≈−0.0003 behind a polluted universe. **A red MOM_SHORT is the expected baseline, not a new regression** —
   it is capped watch-only for new starters, so no live sizing depends on it. This is the ONE recorded
   exception to "no lane negative-excess"; do not add another without the same written rationale.
7. **Path-aware outcomes from the Yahoo chart API**, never the close-only `mcp__yahoo-finance__*` tools.

## The validated lanes (priors from research/20, 50, 70)
**Harness column re-baselined 2026-07-24 (`2b32bad`).** Every pre-07-24 figure here was measured on a
universe with a calendar-day earnings gate and, for OI_FADE, no ETP exclusion at all — see invariant #6.
The old numbers are kept in parentheses to show the size of the correction, not as live priors.

| Lane | Dir | Horizon | Realized (harness, 2026-07-24 baseline) | Note |
|---|---|---|---|---|
| `oi-flow-fade` (OI_FADE) | short | h10 | hit 0.56 vs 0.38, **+1.21% median / +0.70% mean, n=906** *(was +2.1% med, n=640)* | **most robust**; heavy 5d call-OI build → underperform. Old figure inflated ~2× by leveraged/thematic ETFs (SOXS 3× inverse semis et al.) the live lane never trades |
| `momentum` MOM_SHORT (near-52w-low) | short | h10 | **−0.03% mean**, hit 0.48 vs 0.27 *(was +0.81% / +9.5pp)* | crash-gated (`s1_standdown`) + **watch-only cap for new starters**; wins often, loses big — the negative mean is the binding read, not the +20.6pp hit-base |
| `momentum` MOM_LONG (near-52w-high) | long | h10 | +0.18% mean, median −1.06%, **tail-driven** *(was +2.35%)* | basket only, never per-name HIGH |
| `liquidity-reversion` (S2) | long | h3–5 | +0.06% *(was +0.47%)* | DP one-sided concentration, news-gated; advisory-only |
| `sentiment-contrarian` (S4) | long | h5–10 | +0.44% *(was +0.71%)* | PCR-high fade; + ivrank_chg_5d h3 tilt (advisory) |
| `vol-book` | non-dir | event/0DTE | VOL-ONLY | earnings IV-crush + 0DTE-VRP, net-of-cost |
| `fundamentals-gate` | veto | — | risk filter | Finnhub = veto, not alpha (`research/80`) |

## Data & tools
- Panel: `~/Documents/Stocks/{All Options, Dark pool, Hot Option Chains, OI changes, Stock Screener}` (read via `uw` CLI / DuckDB).
- Truth set: `data/{prices,returns,features,weekly_features}.parquet` (built by `scripts/truthset/*`). `edge.py` = the conditional-benchmark resolver.
- `retro_harness.py` = the standing regression gate. `factor_scan.py` = the cross-sectional factor zoo.
- `fz` (Finviz) advisory; `mcp__yahoo-finance__*` NOT for path-aware outcomes.

## Cadence
Nightly `/market-scan` (post-8PM-EST export). Weekend `/weekly-review`. Weekly/per-~10-resolved `/calibration-audit`.

## Git
- Name: Ewan · Email: liyuxuan66@hotmail.com. Branch before non-trivial changes; never commit `data/*.parquet`, `analyses/scan/`, `analyses/audit/`, or `.env`. **`analyses/weekly/` IS tracked** — the weekly-review journal is versioned (policy changed 2026-07-04).
