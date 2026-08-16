---
description: Lean, forward calibration for the excess-scored lanes. Resolves accumulating /market-scan and /weekly-review decision.json calls to realized forward EXCESS, checks each lane is still positive-excess per regime (the regression gate), recalibrates the per-lane excess priors, grades whether the regime/crash gate helped, and accrues pre-registered features toward their bars. Propose-only. Replaces the old 7-phase rubric audit — there is no additive rubric to police here. Invoke as `/calibration-audit` weekly or after ~10 new resolved calls.
model: opus
defaults:
  durable_n: 30
  provisional_n: 10
  disposition: propose-only
---

# /calibration-audit — forward excess calibration (lean)

This repo has **no additive rubric, no tier-cut zoo, no 20-tool attribution** — so it needs none of the old
437-line machinery. It has a handful of **excess-validated lanes** and one job: confirm, forward and out of
sample, that each lane is still earning positive excess — and stop any lane that isn't. The engine is
`scripts/retro_harness.py` run over the **accumulating real envelopes**, not a synthetic backtest.

## Operating principle
Every claim traces to a resolved call's realized **excess vs SPY** (conditional benchmark), computed path-aware
from the Yahoo **chart API** (not the close-only MCP) — identical to the truth set. Propose-only: emit findings,
never auto-edit an agent/command/schema.

## Step 0 — Inventory
- `date +%F` → audit id; `mkdir -p analyses/audit/<date>`.
- Collect `analyses/scan/*/decision.json` + `analyses/weekly/*/decision.json`. Validate each
  (`scripts/validate_decision.py`); skip + flag malformed.
- A call is **resolved** when its `horizon_validated` window has fully matured against today's data.
- **Only `calls[]` rows are resolvable calls.** Weekly `lane_status[]` rows (BASKET_WATCH / STOOD_DOWN /
  NO_NAME_CLEARED) are lane-level dispositions, NOT sized calls — never resolve them as P&L. Read them in
  Step 4 (gate effectiveness): a STOOD_DOWN entry's `candidates[]` are the would-be shorts the gate
  suppressed. (Pre-2026-07 weekly files encoded these as synthetic tickers `MOM_LONG_BASKET` /
  `MOM_SHORT_STANDDOWN` inside `calls[]`; those have been migrated to `lane_status[]`.)

## Step 1 — Resolve to realized excess (per call)
For each resolved call: entry = the session after `report_date`; realized excess = ticker forward return − SPY
same-window return at `horizon_validated`; record `realized_excess_pct`, win = excess>0, and the same-window SPY
base. **STAGE these in `analyses/audit/<date>/resolved_calls.json` — do NOT write them back into the scan or
weekly envelope.** The Hard rule ("never edit outside `analyses/audit/<date>/`") wins over closing the loop
in place: an envelope is the immutable record of what was decided with the information available on
`report_date`, and an audit that edits it destroys the very evidence the next audit re-reads. This is what
the 07-18, 07-25 and 08-01 cycles all did in practice; the instruction previously said "write back into the
envelope" and contradicted the Hard rules. [reconciled 2026-08-01]

A call is INCONCLUSIVE if data is unavailable — never a loss. Distinguish three non-resolved states, because
pooling them overstates data failure: **OPEN** (window not yet matured), **PENDING** (no entry session has
traded yet — the whole final Friday book on a weekend run), and **INCONCLUSIVE** (genuinely unresolvable,
e.g. the name was delisted mid-window in a cash merger).

## Step 2 — Per-lane, per-regime calibration (the core table)
For each lane × regime stratum with decided-N ≥ 10:
- realized mean excess, hit, base, **hit−base**, median, N.
- vs the **validated prior** (the number in `research/20`/`70`/`50` the lane was shipped on).
- **Drift flag:** realized materially below prior (esp. mean_exc ≤ 0 or hit−base ≤ 0).
- Confidence: N≥30 DURABLE, 10–29 PROVISIONAL, <10 ANECDOTE (report, don't act).
- BH (FDR 0.10) across the lane set before any 🚩.

## Step 3 — The regression gate (the one hard rule)
**Any lane whose realized excess goes ≤ 0 over a DURABLE-N forward window is flagged STOP** — recommend pausing
new entries on that lane until re-validated. This is the forward version of `retro_harness.py --all` (no lane
negative). Cross-check by re-running `python3 scripts/retro_harness.py --all` and noting any divergence between
the historical backtest and the realized forward book.

## Step 4 — Gate effectiveness (does the discipline help?)
- **Suppressed candidates: run `python3 scripts/suppression_resolve.py` — do NOT resolve them off the audit's
  own bars cache.** That cache is built from `calls[]` tickers, and a suppressed name is by definition one
  that never became a call, so it has no bars and silently prints "unresolved" — indistinguishable from a
  window that has not matured. Every audit through 2026-08-08 under-reported gate evidence this way (fetching
  the missing names recovered ACVA at −3.03%). The script fetches them and reports RESOLVED / OPEN / PENDING /
  INCONCLUSIVE separately, clustered by lane-period. It lives in `scripts/` because `analyses/audit/` is
  gitignored and a fix made only in an audit dir does not survive the cycle. [added 2026-08-08]
- **Crash guard:** on `s1_standdown` days, did suppressed MOM_SHORT names actually rip (gate saved a loss) or
  fall (gate cost edge)? Report downgrade-effectiveness with decided-N; advisory below N=10.
- **Fundamentals veto / correlation cluster / tail caps:** did vetoed/clustered/capped names underperform the
  book? Same C24-style effectiveness, same N floor.

## Step 5 — Pre-registration ledger
Accrue resolved evidence toward each open pre-registration and report progress vs its bar:
- **PR-WT** weekly-technical features (≥2yr / ≥30 weekly obs per arm, cross-regime, BH) — from `/weekly-review` Layer 3.
- **PR-1** sector-flow (decided: beta, `research/60`), **PR-6** momentum×oi_net conjunction, **PR-7** PEAD/insider
  on extended panel (`research/80`), **PR-2** S1 crash guard through a real V-rebound, **PR-5** S1 options-carry.
- A pre-registration graduates to a scored lane ONLY when its bar is cleared on data that postdates its registration.

## Step 6 — Recommendations (propose-only) + SUMMARY
`analyses/audit/<date>/SUMMARY.md` (≤300 words): lane calibration table, any STOP flags, gate-effectiveness,
pre-registration progress, and "what we'd change" — as **proposed** edits (file + one-line rationale + the
resolved-N behind it), never applied. Print SUMMARY to chat.

## Hard rules
- Propose-only; never edit outside `analyses/audit/<date>/`. This governs Step 1 too — realized excess is
  **staged**, never written back into an envelope.
- **A lane below its recorded baseline is not automatically a regression.** The panel grows, and a signal day
  only enters the aggregate once its h-window matures, so the pooled mean drifts on its own. Before flagging
  one, run the isolation checks (CLAUDE.md invariant #6): (a) re-run the *baseline commit's own*
  `retro_harness.py` against the current panel — identical output proves any refactor behavior-preserving;
  (b) split resolved rows by whether they had matured at the old panel edge — the baseline cohort must still
  reproduce the recorded figures; (c) when the spine changed, re-run current code against the PREVIOUS
  ticker list, which must reproduce the previous baseline. Only a lane that fails them is a real
  regression. [added 2026-08-01; (c) added 2026-08-08]
  **Check (c) applies to gate-effectiveness figures too** — see the crash-guard rule below, where skipping
  it left a p=0.010 subset artifact standing as the repo's strongest gate evidence for a full cycle.
  [added 2026-08-15]
- **A cohort's N is its count of distinct EXIT-DAYS, not its count of rows.** Rows whose h-windows overlap
  share one macro draw. The tell is the `base` column: pinned at 1.00 for long lanes / 0.00 for short lanes
  means the benchmark moved one way across every window in the cohort, so the whole cohort is one
  observation. On 2026-08-08 this decided two readings at once — all five harness lanes fell below baseline
  on a 190-row increment that was a single 08-03→08-07 rally, and the long-awaited post-fix h10 cohort
  turned out to span **3 exit-days**, so its 19 rows could not grade the engine at durable N. It also
  dissolved a false positive: MOM_SHORT's per-name p=0.039 became p=0.134 once clustered by exit-day.
  Report exit-day counts next to every cohort N, and never let a single-window print — in either
  direction — change a lane's size or status. [added 2026-08-08]
- **To grade a gate that suppresses its own evidence, force it off.** A stood-down lane emits no calls, so an
  envelope-based effectiveness test is stuck at N<10 forever. Re-fire the harness's own lane query on the
  gate-days with the gate disabled and resolve from the truth set — that is the exact counterfactual book.
  This took the crash guard from N=6/one episode to 220 name-days across three. Cluster by day
  before testing: one gate-day is one correlated observation, not N. [added 2026-08-01]
- **A gate-effectiveness figure carries the universe it was measured on, exactly like a lane baseline.**
  Before citing one across a spine change, re-run it under isolation check (c). The crash-guard
  counterfactual was recorded as **−1.73%, p=0.010 [DURABLE]** (day-clustered −1.86%, p=0.070) — measured
  on the retired 785-ticker spine. On the full 2,471 spine the *same 15 guard-days and the same code* give
  **−0.60%, p=0.237** (day-clustered **−0.68%, p=0.401**); restricting to the old 785 reproduces the
  original −1.64%/p=0.002. The lane query's `LIMIT 15` now binds on days the old subset could barely fill,
  and 12 of 15 guard-days move less-negative. **The retired figure must not be re-cited.** The guard is
  still directionally right (negative on both spines, 10/15 days saves), but it is no longer DURABLE
  evidence and PR-2 has not advanced. This slipped through a whole cycle because the universe refresh
  re-measured every *lane* and no *gate*. [added 2026-08-15]
- Never recommend removing a risk gate on thin (<10 decided) effectiveness data — a gate's value is insurance
  against the regime not yet in the data.
- Stratify every number by regime; never pool; an edge that flips sign across regimes is beta.
- **Audit scripts must COMPUTE every comparison figure, never hardcode one.** Each cycle starts by copying
  the prior cycle's scripts, so any literal baked into a string silently becomes this cycle's answer. Two
  instances on 2026-08-15: `robust.py` printed the prior cycle's `−1.48%, p=0.020` as the "naive per-name
  view" (live value: −1.06%, p=0.037), and `steps345.py` §4b still resolved suppressions off the
  `calls[]`-only bars cache that `suppression_resolve.py` replaced, printing `*unresolved*` for names the
  canonical script resolves. Constants that legitimately pin a prior cycle (`PRIOR`, `PRIOR_AUDIT_EDGE`)
  must be re-pointed as the first step of the cycle and carry the commit they came from. Grep the copied
  scripts for last cycle's numbers before trusting any table. [added 2026-08-15]
- **Verify the price feed before resolving, not after.** Yahoo's chart API silently serves transient
  `close: null` on liquid names (varying per request — 115 tickers / 273 sessions in one 2026-08-15 pass,
  booking 51 false INCONCLUSIVE) and lags split adjustment into `adjclose` on fresh splits (MNST 2:1,
  which would book a fake −50% on any window crossing it). `scripts/chart.py` now self-heals both, so
  resolve through it; if an audit hand-rolls its own fetch, it must re-implement the interior-hole retry
  and the `events.splits` check. A run whose INCONCLUSIVE count jumps is a data bug until proven a
  delisting — the delisting signature is a *trailing* stop, never an interior hole. [added 2026-08-15]
