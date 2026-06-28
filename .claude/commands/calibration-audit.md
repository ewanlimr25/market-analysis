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

## Step 1 — Resolve to realized excess (per call)
For each resolved call: entry = the session after `report_date`; realized excess = ticker forward return − SPY
same-window return at `horizon_validated`; record `realized_excess_pct`, win = excess>0, and the same-window SPY
base. Write back into the envelope's `realized_excess_pct` field (closes the loop). INCONCLUSIVE if data
unavailable — never a loss.

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
- Propose-only; never edit outside `analyses/audit/<date>/`.
- Never recommend removing a risk gate on thin (<10 decided) effectiveness data — a gate's value is insurance
  against the regime not yet in the data.
- Stratify every number by regime; never pool; an edge that flips sign across regimes is beta.
