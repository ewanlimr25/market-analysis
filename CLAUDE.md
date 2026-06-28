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
6. **Regression gate is law:** `python3 scripts/retro_harness.py --all` must show no lane negative-excess after
   any lane/threshold change. No exceptions.
7. **Path-aware outcomes from the Yahoo chart API**, never the close-only `mcp__yahoo-finance__*` tools.

## The validated lanes (priors from research/20, 50, 70)
| Lane | Dir | Horizon | Realized (harness) | Note |
|---|---|---|---|---|
| `oi-flow-fade` (OI_FADE) | short | h10 | hit 0.61 vs 0.41, +2.1% median, n=640 | **most robust**; heavy 5d call-OI build → underperform |
| `momentum` MOM_SHORT (near-52w-low) | short | h10 | +0.81% / +9.5pp hit | crash-gated (`s1_standdown`) |
| `momentum` MOM_LONG (near-52w-high) | long | h10 | +2.35% mean, **tail-driven** | basket only, never per-name HIGH |
| `liquidity-reversion` (S2) | long | h3–5 | +0.47% | DP one-sided concentration, news-gated |
| `sentiment-contrarian` (S4) | long | h5–10 | +0.71% | PCR-high fade; + ivrank_chg_5d h3 tilt (advisory) |
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
- Name: Ewan · Email: liyuxuan66@hotmail.com. Branch before non-trivial changes; never commit `data/*.parquet`, `analyses/`, or `.env`.
