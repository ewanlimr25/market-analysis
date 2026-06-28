---
description: Regime-first, excess-validated market scan that supersedes /daily-analysis and /weekly-analysis. Classifies the regime, then fires only the handful of edges that survived an independent, conditional-benchmark, regime-stratified backtest (52-week-range momentum long+short, OI-flow fade, dark-pool liquidity-reversion, PCR contrarian fade) plus a non-directional vol book — scored in forward EXCESS-vs-SPY, never additive confluence. Emits report.md + decision.json (envelope v2). Invoke for any post-market or multi-day directional/vol scan, an EOD briefing, or `/market-scan`. Honest default: most days have NO directional edge. Do NOT trigger for single-ticker deep dives or single-tool queries.
model: opus
defaults:
  horizon_map: { "0DTE": same-day, swing3: 3D, swing10: 10D, weekly5: 5D, weekly10: 10D }
  scoring_currency: excess_vs_spy_conditional   # NEVER raw win-rate (the tape is long-biased)
  out_of_regime_cap: half
---

# /market-scan — regime-first, excess-validated

Supersedes `/daily-analysis` + `/weekly-analysis`. Built from the clean-room evidence in
`findings/RESEARCH/*` and `findings/DESIGN/40-improved-workflow.md`. **Three commitments
override everything below** (each cites the evidence):

1. **Excess is the only currency.** Score, gate, and size in **excess-vs-SPY on the conditional
   (same-day) benchmark** — never raw win-rate. The tape is steeply long-biased (SPY up 58/63/68/71%
   at h=1/3/5/10), so raw WR is beta in disguise (`RESEARCH/10-truth-set.md §1.4`; the inflated
   single-leg-whale "+22pp" was an unconditional-benchmark artifact, `RESEARCH/12`).
2. **No additive confluence.** Stacking correlated flow signals manufactures conviction out of beta —
   it produced a HIGH-tier book that realized **−8.2% excess, 0-for-6** (`RESEARCH/50-retro-validation.md`).
   A candidate scores on its own lane's *measured* excess, regime-conditioned. Two lanes flagging the
   same name is noted, never multiplied.
3. **Most days have no directional edge — say so.** "No actionable directional edge; here is the regime,
   the vol book, and the watch list" is a valid, common output (`RESEARCH/20 §2.0`: 0 durable directional
   edges across 45 raw signals).

## Data access
All UW data via the `uw` CLI (`uw <group> <sub> --json --quiet`, `--date YYYY-MM-DD`). `fz` (Finviz)
advisory only. OHLC/excess outcomes for the live calibration loop come from the Yahoo **chart API**
(path-aware), never the close-only `mcp__yahoo-finance__*` tools.

## When to invoke
- Post-market / multi-day directional or vol scan; EOD briefing; `/market-scan`.
## When NOT to invoke
- "What's NVDA doing?" → `uw insights deep-dive`. "Show me sweeps" → `uw options-flow sweeps`
  (and remember: sweeps are a 0-point relative-strength *tell*, not conviction — `RESEARCH/20 §2.1 S5`).

---

## Phase A — Regime & beta context (the master gate)
Spawn **`regime-classifier`**. It returns the regime label, vol-state, breadth, event calendar, and two
gating verdicts every later phase consumes:
- `directional_tradable` — is there a regime in which any directional lane has validated excess today?
- `s1_standdown` — the **momentum-crash / V-rebound / junk-rally / squeeze** guard (strong 5d up-thrust,
  esp. off a recent dip). When true, **all S1 shorts stand down and sizing is capped** — this is the one
  regime the literature says inverts S1 (`RESEARCH/30 §3.1`, Daniel-Moskowitz momentum crashes).
GEX/DEX feed **only** the vol-state here (dealer gamma is a 2nd-moment conditioner, not directional —
`RESEARCH/30 §3.0` STRONG). Never read a direction off GEX/DEX/vanna.

## Phase B — The edge scan (orthogonal lanes, parallel)
Spawn only the lanes their regime makes appropriate. They are orthogonal by construction (price-momentum /
liquidity-event / sentiment / vol) — the opposite of the old fleet's four correlated flow agents.

| Lane | Agent | Edge (measured) | Horizon | Confidence |
|---|---|---|---|---|
| **Momentum (both legs)** | `momentum` | 52w-range factor (rank-IC t=+6.8): SHORT near-low (+0.81% / +9.5pp hit) + LONG near-high (+2.35% mean, **tail-driven**), h10 | **swing10/weekly10** | **HIGH** (short crash-gated; long=basket/tail) |
| **OI-flow fade (NEW)** | `oi-flow-fade` | heavy 5-day call-OI build → underperformance; short **hit 0.61 vs 0.41 base, +2.1% median, n=640** — most robust edge; orthogonal to momentum (corr −0.17) | swing10 | **HIGH for this panel** (provisional) |
| Liquidity reversion | `liquidity-reversion` | DP one-sided-concentration → 3–5d reversal (S2; long-tilted, news-gated) | swing3/weekly5 | MODERATE |
| Sentiment contrarian | `sentiment-contrarian` | PCR-high fade-long (S4) + `ivrank_chg_5d` rising-IV tilt (h3, the only 3-regime-stable factor) | swing5–10 / h3 | LOW-MOD (advisory) |
| Vol book (non-dir) | `vol-book` | earnings IV-crush SELL-VOL (vs implied move) + 0DTE-VRP premium-selling | event / 0DTE | MODERATE, net-of-cost |

There is **no ≥2-agent confluence gate** — confluence of correlated betas was the defect. A name enters
the book if it lands in a regime-appropriate lane and clears the **liquidity floor** (price ≥ $5 AND
20-day $-ADV ≥ $50M, fail-closed).

## Phase C — Scoring (excess-as-currency)
For each candidate, the score is **not** a sum of points:
```
score = validated_excess(lane, horizon, regime)   # from the truth-set tables, stratified by regime
        × regime_fit                              # 1.0 if regime-appropriate; →0 otherwise
        × (1 − fundamental_contradiction)         # veto channel only (Phase D)
```
- `validated_excess` is the lane's measured forward excess for this horizon/regime (the numbers in
  `RESEARCH/20` / `50`). **A lane in a regime where it has no validated excess scores 0** (e.g. S1 short
  under `s1_standdown`).
- **Tiers describe measured edge, not a confluence count:** HIGH = validated excess ≥ +1% with
  sign-stability across the available regimes; MEDIUM = +0.3–1%; else watch-only.
- If two orthogonal lanes flag the same name, note it as evidence-type diversification — do **not** add.

## Phase D — Gates & sizing (`risk-sizer`)
Spawn **`risk-sizer`** (hardened `risk-monitor`). In order:
1. **Regime/crash gate** — S1 off when `s1_standdown`; out-of-regime tape caps all sizing at half.
2. **Liquidity floor** (fail-closed).
3. **Correlation cluster** — corr ≥ 0.70 = one position (load-bearing: S1 cohorts are often a single
   theme, e.g. the China complex on 2026-06-23 — `RESEARCH/50 §5.3`).
4. **Fundamentals veto** — spawn `fundamentals-gate` only on names about to be sized (CONFIRM/CAUTION/VETO).
5. **Event-risk** — Tier-1 macro / earnings inside the horizon.
6. **Tail caps** — S1 short sized for the momentum-crash tail; S2 cut on news/earnings; vol-short sized
   for the unsampled left tail and quoted **net of cost** (`RESEARCH/30 §3.1`, Vilkov: 0DTE flips
   negative gross→net once costs charged).
Final size = `f(score) × tail_cap × regime_cap`. Optionally spawn a bounded `bull/bear` debate on the
1–2 HIGH-tier names (rarely more).

## Phase E — Report, envelope, calibration, write-back
1. `mkdir -p analyses/scan/YYYY-MM-DD`; write `report.md` (structure below) + `decision.json`
   (envelope **v2**, `schemas/decision_envelope.v2.schema.json`), validate, fix the envelope until it passes.
2. Persist the top conviction names to `conviction_<date>`; next run pulls adverse-flow exits.
3. The `/calibration-audit` loop now grades **forward excess per lane per regime** (not raw WR).
4. **Regression gate:** after any lane/threshold change, run `python3 artifacts/retro_harness.py --all` —
   ship the change only if no lane/tier goes negative-excess (`RESEARCH/50 §5.4`).

### report.md structure
```markdown
# Market Scan — YYYY-MM-DD
## Regime & Verdict
- Regime: <label> · vol-state · breadth · `directional_tradable` · `s1_standdown`
- Bottom line: <"No directional edge today" | "N regime-appropriate calls">
## Directional Book (excess-scored)   # empty is a valid, common section
| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
## Vol Book (non-directional)
- Earnings IV-crush SELL-VOL (vs implied move) · 0DTE-VRP (net-of-cost) — delta-neutral, advisory
## Watch / Stood-down
- S1 cohort if `s1_standdown`; single-lane advisory names; correlation-clustered duplicates
## Risk
- correlation clusters, event calendar, tail caps applied, hedge note
```
Print only the **Regime & Verdict** + the directional book to chat; the user opens the file for the rest.

## Failure modes
- A lane returns nothing → that section is explicitly empty (not a failure).
- No lane is regime-appropriate → "No directional edge today" + vol book + watch list. **This is the
  modal output and is correct.**
- Stale UW data → abort and ask for a re-export.
