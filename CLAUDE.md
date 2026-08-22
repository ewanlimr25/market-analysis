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
   ⚠️ **That correlated draw UNWOUND on 2026-08-22, exactly as pre-registered — and the pre-registration
   is what made the cycle readable.** Increments 08-08 and 08-15 were the *same* one-way rally (317 rows,
   5 exit-days, `base` pinned 1.00 long / 0.00 short); the 08-22 increment is its **mirror** (4 exit-days,
   base pinned 0.00 long / 1.00 short, SPY down in 100% of new windows). So **MOM_LONG's and S2's rise is
   not a fix working, and OI_FADE's −9bp is not decay** — its baseline cohort reproduces exactly. The
   baseline above is deliberately **not** re-pointed to the 93-day panel: re-baselining on a 4-exit-day
   reversal would bake one draw into the reference. When an increment's `base` is pinned, write down what
   the unwind will look like ([`docs/regression-gate.md`](docs/regression-gate.md#worked-example-2026-08-22-the-pre-registered-unwind-arrived)). A
   baseline is only meaningful against the universe it was measured on — state the spine size whenever you
   record one, and a below-baseline lane is not automatically a regression (panel growth and universe
   changes move the pooled mean independent of code). **This applies to gate-effectiveness figures too,
   not just lanes:** any measured number carries the spine it was measured on, so re-run isolation check
   (c) before citing one across a universe change. The 2026-08-15 audit is the worked example — the crash
   guard's DURABLE p=0.010 was a 785-spine artifact and reads p=0.237 on the full spine. **A STOP flag is governed by the `cluster_id` unit** (else the name) — the
   risk-sizer's own unit — with the **exit-day** view reported alongside it every cycle, and a lane whose
   distinct exit-day count is <30 carries a correlated-draw caveat and cannot graduate to sizing on that
   evidence alone. Declared 2026-08-22, when the three units first disagreed on the whole book (−0.60% /
   −0.97% / −2.20%); never report one unit alone
   ([`docs/regression-gate.md`](docs/regression-gate.md#which-clustering-unit-governs-a-stop-flag)).
   MOM_SHORT is the
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
| `oi-flow-fade` (OI_FADE) | short | h10 | +0.38% mean / +0.79% median, hit 0.54 vs 0.36, n=1176 | **Sizes** — ⚠️ but this prior grades the **raw `oi_net_5d`** rule, not the `oi_rel_build` rule the live lane runs. On an identical pool the live rule measures **−0.0076** vs raw's −0.0004, and ~half the +0.38% is a **partial-window artifact** (6.1% of rows, mean +0.0277). `--oi-variant both`; [`docs/regression-gate.md`](docs/regression-gate.md#oi_fade-the-baseline-and-the-live-lane-grade-different-rules-2026-08-22) |
| `momentum` MOM_SHORT (near-52w-low) | short | h10 | −1.37% mean, n=830 | Watch-only, crash-gated, never sizes |
| `momentum` MOM_LONG (near-52w-high) | long | h10 | −1.27% mean, n=1154 | Basket/watch only, never sizes |
| `liquidity-reversion` (S2) | long | h3–5 | +0.14%, n=1210 | Advisory-only |
| `sentiment-contrarian` (S4) | long | h5–10 | +0.25%, n=1241 (post call-volume-floor fix) | Advisory-only; **hit − base negative (−0.056) — no hit-rate edge, right-tail only** |
| `vol-book` | non-dir | event/0DTE | VOL-ONLY | Net-of-cost, delta-neutral |
| `fundamentals-gate` | veto | — | risk filter | Finnhub = veto, not alpha (`research/80`) |

## Data & tools
- Panel: `~/Documents/Stocks/{All Options, Dark pool, Hot Option Chains, OI changes, Stock Screener}` (read via `uw` CLI / DuckDB).
- Truth set: `data/{prices,returns,features,weekly_features}.parquet` (built by `scripts/truthset/*`). `edge.py` = the conditional-benchmark resolver.
- `retro_harness.py` = the standing regression gate (`--oi-variant both` grades the raw vs the live OI_FADE rule). `factor_scan.py` = the cross-sectional factor zoo.
- `resolved_ledger.py` = the durable record of matured calls. Re-deriving realized excess from the live vendor feed is **not idempotent** — EQR resolved at the 08-15 audit and was un-resolvable a week later after Yahoo retracted 11 sessions — so the audit book is not append-only unless the ledger restores it. `chart.py` exposes `gaps()`/`bars_grid()` for the same reason; never index a lookback by position.
- `fz` (Finviz) advisory; `mcp__yahoo-finance__*` NOT for path-aware outcomes.

## Cadence
Nightly `/market-scan` (post-8PM-EST export). Weekend `/weekly-review`. Weekly/per-~10-resolved
`/calibration-audit`. **Next audit due 2026-08-29.** **11 open call-rows (all OI_FADE, 7 distinct names)**
and **215 open suppressed candidates** — the suppressions are the real cohort now: they crossed into
PROVISIONAL this cycle (21 lane-periods, −1.74%, p=0.008), while the call book added only **11 rows over
2 exit-days** and the sized book gained **zero**. **Stop scheduling "the first non-overlapping OI_FADE
cohort" as a matter of waiting** — re-signal dedup caps that lane at ~2 cluster-units per runner, however
long it runs, which is why it has been deferred three cycles
([`docs/regression-gate.md`](docs/regression-gate.md#re-signal-dedup-caps-a-lanes-forward-n-structural-not-bad-luck)).
Count distinct **exit-days**, not rows, when judging any cohort
([`docs/regression-gate.md`](docs/regression-gate.md#exit-day-counting-companion-rule)).

## Git
- Name: Ewan · Email: liyuxuan66@hotmail.com. Branch before non-trivial changes; never commit `data/*.parquet`, `analyses/audit/`, or `.env`. **`analyses/weekly/` IS tracked** — the weekly-review journal is versioned (policy changed 2026-07-04). **`analyses/scan/` IS tracked** — the nightly scan journal is versioned and public (policy changed 2026-08-08); commit each night's `report.md` / `decision.json` / `conviction_*.json` with the scan. `analyses/audit/` stays local-only (working files, not a journal).
- **The repo is public** (`github.com/ewanlimr25/market-analysis`). `README.md` is the public-facing entry point — keep the required-data-layout section true if panel paths, filename patterns, or truth-set build order change. Nothing written into `analyses/` should contain a credential or an absolute local path.
