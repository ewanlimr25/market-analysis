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
4. **Half-cap, no auto-full.** No call sizes full until a cross-year edge validates. **As of
   2026-08-22 NO lane sizes at all** — OI_FADE, the last one, was demoted to advisory when its prior
   was re-measured and no variant showed a validated positive edge. A book that sizes nothing is the
   correct output of invariant #1 when nothing clears; it is not a defect to be worked around.
   **As of 2026-08-29 OI_FADE does not emit a watch list either — it is STOOD DOWN to diary-only**,
   because `OI_FADE_LIVE` (the rule the engine runs) now measures **−0.93%, 29 `lane-exit-day`,
   p=0.028, surviving BH(0.10)**, robust to dropping the three crypto names that moved the pooled
   baseline. A ranked nightly list of shorts drawn from a rule measured as losing is an implicit
   suggestion, and there is no such category. The lane still runs and is still written up in the
   journal; `retro_harness.py` fires its own query, so standing the lane down does **not** starve
   its evidence. Re-check at 30 `lane-exit-day` — both outcomes pre-registered in
   [`docs/regression-gate.md`](docs/regression-gate.md#oi_fade_live-is-significantly-negative--lane-stood-down-to-diary-only-2026-08-29).
5. **Pre-registered ≠ scored.** Weekly technicals and all PR-* items are documented, never sized, until their
   bar clears on data that postdates registration.
6. **Regression gate is law:** `python3 scripts/retro_harness.py --all` must show no lane **below its
   recorded baseline** after any lane/threshold change. **Current baseline** (adopted 2026-08-22 on the
   FULL liquid universe, panel→08-21, 93 days, 2,471-ticker spine, post-OI_FADE-full-window fix):
   **MOM_LONG −0.0118 (n=1213) · MOM_SHORT −0.0138 (n=830) · OI_FADE +0.0013 (n=1177) ·
   S2 +0.0018 (n=1269) · S4 +0.0024 (n=1304).** Only OI_FADE moved by code (partial-window artifact
   removal, +0.0029 → +0.0013 — **not decay**; `hit − base` *improved* +0.155 → +0.184); an
   old-code/new-data control on the same 93-day panel reproduced the other four bit-identically. Only S4 moved by code (call-volume floor, +0.0041 → +0.0025 — **artifact removal,
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
   risk-sizer's own unit — with the **`lane-exit-day`** view reported alongside it every cycle, and a lane
   whose `lane-exit-day` count is <30 carries a correlated-draw caveat and cannot graduate to sizing on
   that evidence alone. Declared 2026-08-22, when the three units first disagreed on the whole book
   (−0.60% / −0.97% / −2.20%); never report one unit alone. ⚠️ **The repo has TWO exit-day units and
   used to call both "exit-day"** — `exit-session` (distinct exit sessions pooled across lanes; the
   whole-book figure, e.g. the −2.20% above) and `lane-exit-day` (one lane × exit-day pair; the per-lane
   column, ~3× more observations on the same rows). Named apart 2026-08-29 after an audit spent a cycle
   treating 35-unit and 95-unit figures as a contradiction — both reproduce exactly; they are different
   units. **Use the names, never the bare phrase "exit-day"**
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
yet. **Where a lane's shipped rule differs from the rule its prior was measured on, quote the SHIPPED
rule's number** (rule added 2026-08-29 with OI_FADE, whose two figures have opposite signs). Full
per-lane notes and the 785-spine comparison: [`docs/lanes.md`](docs/lanes.md).

| Lane | Dir | Horizon | Realized (harness) | Status |
|---|---|---|---|---|
| `oi-flow-fade` (OI_FADE) | short | h10 | **−0.93%, n=435, 29 `lane-exit-day`, p=0.028** — `OI_FADE_LIVE`, the rule the engine runs | ⛔ **STOOD DOWN — diary-only since 2026-08-29; advisory 08-22; last sizing lane before that.** The live rule is **significantly negative and survives BH(0.10)**, and unlike the pooled baseline it is not a few names (ex-MSTR/CELH/MARA: −0.70%). **The figure quoted here is deliberately the live rule's, not the raw pool's** — the old headline (`OI_FADE` raw rank, full pool: +0.13% → −0.18% on the 98-day panel) grades a rule the engine does not run, and its *sign* is three crypto names re-signalled across five sessions (drop them and it is +0.11%), so it must not be re-baselined in either direction. Ranking UNCHANGED (`oi_rel_build` + persistence). **No lane sizes; this one no longer emits candidates.** Re-check at 30 `lane-exit-day`. [`docs/regression-gate.md`](docs/regression-gate.md#oi_fade_live-is-significantly-negative--lane-stood-down-to-diary-only-2026-08-29) |
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
`/calibration-audit`. **Next audit due 2026-09-05.** **5 open call-rows (all OI_FADE — FDX/GEN/BSY/ITRI
mature ~08-31, AS ~09-03)** and **355 open suppressed candidates**. The suppressions are the only cohort
that actually grows: the call book gained **2 cluster-units** in the 08-29 cycle and the sized book gained
**zero for the second cycle running**.
- **Do not re-cite the 08-22 suppression result.** "Gate discipline is significantly negative"
  (21 lane-periods, −1.74%, p=0.008) **did not replicate** — at 33 lane-periods it is −0.89%, p=0.054,
  no lane surviving BH
  ([`docs/regression-gate.md`](docs/regression-gate.md#the-2026-08-22-suppression-result-did-not-replicate-2026-08-29)).
- **Stop scheduling "the first non-overlapping OI_FADE cohort" as a matter of waiting** — re-signal dedup
  caps that lane at ~2 cluster-units per runner, however long it runs, which is why it has been deferred
  three cycles
  ([`docs/regression-gate.md`](docs/regression-gate.md#re-signal-dedup-caps-a-lanes-forward-n-structural-not-bad-luck)).
- **Stop scheduling the crash-guard and fundamentals-veto tests as pending, too** (added 2026-08-29).
  Both produced **bit-identical numbers for three consecutive cycles** — crash guard 20 guard-days /
  −0.58% / p=0.212 unchanged since 08-22 because no guard-day has fired since 08-07; fundamentals VETO
  n=15 / −2.28% and CONFIRM n=23 / −1.21% unchanged since **08-15**. Neither is waiting on maturity: they
  are waiting on the gate **firing**, which is a regime event with no schedule. Report them as *dormant*,
  not *accruing*, and spend no cycle time re-deriving them until the underlying N moves.
- Count distinct **`lane-exit-day`** (per lane) / **`exit-session`** (whole book), not rows, when judging
  any cohort — and use the names
  ([`docs/regression-gate.md`](docs/regression-gate.md#exit-day-counting-companion-rule)).

## Git
- Name: Ewan · Email: liyuxuan66@hotmail.com. Branch before non-trivial changes; never commit `data/*.parquet`, `analyses/audit/`, or `.env`. **`analyses/weekly/` IS tracked** — the weekly-review journal is versioned (policy changed 2026-07-04). **`analyses/scan/` IS tracked** — the nightly scan journal is versioned and public (policy changed 2026-08-08); commit each night's `report.md` / `decision.json` / `conviction_*.json` with the scan. `analyses/audit/` stays local-only (working files, not a journal).
- **The repo is public** (`github.com/ewanlimr25/market-analysis`). `README.md` is the public-facing entry point — keep the required-data-layout section true if panel paths, filename patterns, or truth-set build order change. Nothing written into `analyses/` should contain a credential or an absolute local path.
