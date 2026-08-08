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
   baseline** after any lane/threshold change. **Baseline (verified 2026-08-08, panel→08-07, 83 days):**
   MOM_LONG +0.0008 · **MOM_SHORT −0.0043** · OI_FADE +0.0054 · S2 +0.0007 · S4 +0.0039.
   **The baseline is panel-dependent — re-verify it before reading a dip as a regression.** The pooled mean
   moves on its own as the panel grows, because a signal day only enters the aggregate once its h-window
   matures. Two isolation checks, both run 2026-08-08 (`analyses/audit/2026-08-08/harness_split.py`):
   (a) **old code, new data** — `git show <baseline-commit>:scripts/retro_harness.py` run against the current
   panel must reproduce all five lanes. At 2026-08-08 this was stronger than behavior-preserving: `git diff
   de91fe9 HEAD` over `retro_harness.py`, `_regime.py`, `_calendar.py`, `_env.py` is **empty**, so there was no
   refactor to clear at all (the `_regime.py` extraction in `374b20d` and the `hz_end()` → `scripts/_calendar.py`
   move at `4ec89dc` were each cleared this way when they landed);
   (b) **cohort split by maturity edge** — rows that had matured at the old 07-31 edge still reproduce the prior
   baseline to the last digit (+0.0023 · −0.0008 · +0.0071 · +0.0021 · +0.0051 @ `de91fe9`; before that
   +0.0018 · −0.0003 · +0.0070 · +0.0006 · +0.0044 @ `4ec89dc`, first recorded at `2b32bad`).
   Only after BOTH checks is a below-baseline lane a real regression.
   **2026-08-08 is the worked example of why this invariant exists: ALL FIVE lanes fell at once, and it was one
   macro window.** Both checks passed, and the 190-row increment had its `base` column **pinned at 1.00 for
   every long lane and 0.00 for every short** — SPY rose in 100% of the new windows, because signal days
   07-20→07-31 all exit into 08-03→08-07. Five lanes did not independently decay; one rally out-ran all five.
   **Diagnostic:** when an increment's `base` is 0.00/1.00 rather than mid-range, it is a single correlated draw
   and its true N is the count of distinct **exit-days**, not rows. **Corollary — do not read the recovery as a
   fix:** when this artifact unwinds next cycle the lanes will rise on their own, which is not evidence that any
   change worked.
   MOM_SHORT is *knowingly* negative: `2b32bad` fixed the **measuring instrument** (calendar→trading-day
   earnings window on all lanes; OI_FADE had no ETP/earnings hygiene at all), exposing a lane that was always
   negative behind a polluted universe. It went −0.0003 → −0.0008 on 36 mid-July rows (signal days 07-13→17,
   mean −0.0041) whose 52-week lows were Yahoo-verified genuine, then −0.0008 → −0.0043 on the 08-03→07 rally
   above — a short lane measured across windows where SPY rose every time. Both moves are real signal, not
   instrument error. **A red MOM_SHORT is the expected baseline, not a new regression** — it is capped
   watch-only for new starters, so no live sizing depends on it. This is the ONE recorded exception to
   "no lane negative-excess"; do not add another without the same written rationale.
7. **Path-aware outcomes from the Yahoo chart API**, never the close-only `mcp__yahoo-finance__*` tools.

## The validated lanes (priors from research/20, 50, 70)
**Harness column re-baselined 2026-08-08 (panel→08-07, 83 days).** Parentheses hold the **immediately prior
(07-31) baseline**, so the pair shows one cycle of drift — not a live prior. Separately, every pre-07-24
figure was measured on a universe with a calendar-day earnings gate and, for OI_FADE, no ETP exclusion at
all; those corrections are now described in the per-lane notes rather than the parentheses (see invariant #6).
**Read this whole column against invariant #6's 2026-08-08 note:** every lane fell vs the 07-31 baseline
because the new rows are one 08-03→08-07 rally, not five independent decays.
**These are HISTORICAL-panel priors.** The forward book is graded separately by `/calibration-audit`; as of
2026-08-08 the forward cluster-unit read is softer on every lane except S4 (see
`analyses/audit/2026-08-08/SUMMARY.md`), but no lane cleared BH(0.10), so none is stopped.

| Lane | Dir | Horizon | Realized (harness, 2026-08-08 baseline) | Note |
|---|---|---|---|---|
| `oi-flow-fade` (OI_FADE) | short | h10 | hit 0.55 vs 0.38, **+0.93% median / +0.54% mean, n=1050** *(was +1.22% med / +0.71% mean, n=979)* | **most robust**; heavy 5d call-OI build → underperform. Pre-07-24 figure was inflated ~2× by leveraged/thematic ETFs (SOXS 3× inverse semis et al.) the live lane never trades. **Forward watch — decay signal NOT confirmed:** the 08-01 audit flagged a −3.73% new-evidence cohort (hit−base −0.53) as possible decay and named the post-fix h10 cohort as the test. That cohort matured and **reversed the sign: +1.99%, hit−base +0.67** (9 units, 3 exit-days, ANECDOTE). Neither read is durable — do not act on either; re-test when the 17 open h10 rows mature |
| `momentum` MOM_SHORT (near-52w-low) | short | h10 | **−0.43% mean**, hit 0.46 vs 0.29, n=351 *(was −0.08%, n=317)* | crash-gated (`s1_standdown`) + **watch-only cap for new starters**; wins often, loses big — the negative mean is the binding read, not the +16.2pp hit-base. The deepening from −0.08% is the 08-03→07 rally (invariant #6), not new decay |
| `momentum` MOM_LONG (near-52w-high) | long | h10 | +0.08% mean, median −1.13%, n=506, **tail-driven** *(was +0.23%, n=483)* | **WATCH/BASKET ONLY — this lane never sizes.** Basket only, never per-name HIGH; sector-concentration capped (gate #7). Enforced by `risk-sizer.md`'s advisory map and confirmed forward: **0 of 52 resolved calls were ever sized**. It is also the one lane clearing BH(0.10) negative on the forward book under day-clustering (−4.65%, p=0.008, 14 basket-days, PROVISIONAL-N — below the DURABLE-N bar a STOP requires) |
| `liquidity-reversion` (S2) | long | h3–5 | +0.07%, n=559 *(was +0.21%)* | DP one-sided concentration, news-gated; advisory-only |
| `sentiment-contrarian` (S4) | long | h5–10 | +0.39%, n=396 *(was +0.51%)* | PCR-high fade; + ivrank_chg_5d h3 tilt (advisory). The only lane positive forward as well as historically |
| `vol-book` | non-dir | event/0DTE | VOL-ONLY | earnings IV-crush + 0DTE-VRP, net-of-cost |
| `fundamentals-gate` | veto | — | risk filter | Finnhub = veto, not alpha (`research/80`) |

## Data & tools
- Panel: `~/Documents/Stocks/{All Options, Dark pool, Hot Option Chains, OI changes, Stock Screener}` (read via `uw` CLI / DuckDB).
- Truth set: `data/{prices,returns,features,weekly_features}.parquet` (built by `scripts/truthset/*`). `edge.py` = the conditional-benchmark resolver.
- `retro_harness.py` = the standing regression gate. `factor_scan.py` = the cross-sectional factor zoo.
- `fz` (Finviz) advisory; `mcp__yahoo-finance__*` NOT for path-aware outcomes.

## Cadence
Nightly `/market-scan` (post-8PM-EST export). Weekend `/weekly-review`. Weekly/per-~10-resolved `/calibration-audit`.
**Next audit due 2026-08-15.** The 2026-08-08 cycle got the first post-fix h10 cohort (34 post-fix rows,
19 at h10) and it answered the OI_FADE decay question in the negative — but **it spans only 3 exit-days
(08-04/05/06) with SPY up in all three**, so its honest N is 3, not 19. The current engine still has not
been graded at durable N. **41 open rows (17 OI_FADE, 12 MOM_SHORT, 11 S4) mature 08-10→08-21**, and the
08-03→08-07 crash-guard block matures 08-18→08-22 — that is the first cohort spanning non-overlapping
windows. When judging any post-fix cohort, count distinct **exit-days**, not rows (invariant #6).

## Git
- Name: Ewan · Email: liyuxuan66@hotmail.com. Branch before non-trivial changes; never commit `data/*.parquet`, `analyses/scan/`, `analyses/audit/`, or `.env`. **`analyses/weekly/` IS tracked** — the weekly-review journal is versioned (policy changed 2026-07-04).
