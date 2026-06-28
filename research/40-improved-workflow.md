# 40 — The Redesigned Workflow (Phase 4 / DESIGN)

_Every design choice cites a Phase-1/2/3 finding. The redesign is a **reduction**, not a re-weighting: from a 16–17-agent additive-confluence machine that mostly scores beta, to a lean, regime-first engine built on the handful of edges that survived an independent, conditional-benchmark, regime-stratified, look-ahead-safe truth set._

## 4.1 Design philosophy (the three things the evidence forces)
1. **Excess is the only currency.** Raw win-rate is a trap on a long-biased tape (Phase 1 §1.4: SPY up 58/63/68/71% at h=1/3/5/10). Every score, gate, and size is denominated in **excess-vs-SPY on the conditional (same-day) benchmark** — the C21-correct benchmark our truth set uses, *not* the unconditional one that inflated single-leg-whale by ~22pp (`12-benchmark-inconsistency.md`).
2. **Stop paying for beta.** 26/45 raw flow signals are beta; the literature says this is structural at EOD-aggregate granularity (Phase 3 §3.0, STRONG: Lakonishok-Lee-Pearson-Poteshman; Ge-Lin-Pearson; only signed/opening/intraday flow carries alpha). Additive confluence of correlated flow signals **manufactures conviction out of beta**. It is removed.
3. **Most days have no directional edge — say so.** The default output is "no actionable directional edge; here is the regime, the vol book, and the watch list." This is a feature (Phase 2: 0 durable directional edges), not a failure.

## 4.2 What is CUT — and the evidence that kills it
| Cut | Was | Evidence |
|---|---|---|
| `dealer-positioning-strategist` (agent) + **+1 mechanized DEX-flip** line | swing DEX/vanna | P2: DEX level BETA, DEX flip **anti-predictive** (−1.5%/h10, p=0.003, n=277). P3 STRONG: dealer gamma is 2nd-moment; daily-horizon flips mean-revert (Baltussen 2021, Barbon-Buraschi). |
| `gamma-flip-tracker` **directional** role | 0DTE GEX advisory | P2 H7 + P3 STRONG: GEX sign ⊥ signed return; "neg-gamma=wider range" was an ETF-vs-stock composition artifact. → kept only as a **vol-state input** to the 0DTE stack. |
| `multileg-strategist` (agent) + **+2 multileg** line | 2nd-heaviest rubric weight | P2: `MULTILEG_HEAVY` **NOISE** in both directions. The heaviest non-accumulation weight is unearned. |
| `leap-positioning-radar` (agent) + **+1 conviction-matrix** line | LEAP directional | P2: LEAP OI builds BETA. P1 §1.5: 90D horizon **unverifiable** on this panel (only Block A resolves). |
| **+3 accumulation conjunction** line | LOAD-BEARING in audit | P2: DP block-accum + OI build both BETA; block-stratification moves IC only 0.031→0.042. The real DP edge (S2) is **non-directional mean-reversion**, a different signal. |
| **+1 multi-day OI build** line — **SIGN CORRECTED** | scored bullish | P2: `OI_TREND_CALL` BETA. **P7 (`RESEARCH/70`): the sign was BACKWARDS** — heavy 5-day net call-OI build (`oi_net_5d`) → **under**performance (rank-IC t=−7.1). Re-spec as the **`oi-flow-fade`** lane (short), §4.4. |
| **+1 cum-premium-flow** line | scored | P2: BETA (`NET_PREM_BULL/BEAR`). P3 STRONG (flow-is-beta). Retained only as a liquidity/context screen, 0 points. |
| `sweep-tracker` **directional scoring** | sweeps as conviction | P2: `SWEEP_CALL` beta; `SWEEP_PUT` is **contrarian** (negative IC). P3 STRONG. → repurposed to a 0-point relative-strength/hedging **tell**. |
| **single-leg-whale C19 promotion path** | advisory→scored pending | P2: beta in **every** tier; `12-benchmark-inconsistency.md`: the +22pp is an unconditional-benchmark **selection artifact**. → **close the promotion path**; keep only the "don't score puts as bearish" lesson. |
| `/weekly-analysis` as a separate command | 614-line twin | Edges are horizon-specific; one **horizon-aware** flagship supersedes the daily/weekly split (§4.6). |

**Net agent roster: 16–17 → 7.** This is the single biggest change and it is entirely subtractive-with-evidence.

## 4.3 What is KEPT or REPURPOSED (the genuinely good parts)
- **The decision-envelope + schema-validation + `/calibration-audit` loop** — the only validated edge-measurement infrastructure in the set; *hardened*, not removed. Now tracks **forward excess**, not raw WR.
- **Conditional-benchmark / excess discipline (C21/C2)** — promoted from a gate to **the scoring currency**.
- **Liquidity floor (C12)** — kept; reinforced by P3 (S2/S4 contamination risk in small/illiquid names).
- **`risk-monitor`** — regime + correlation-cluster gating is *more* important on a beta-heavy tape; kept and made the master sizer.
- **`fundamentals-gate`** — cheap veto on the few names actually sized; kept (now even cheaper — fewer names).
- **0DTE-VRP premium-selling stack** (`zerodte_setup.py`) — P3 STRONG (real but cost/tail-fragile); kept delta-neutral, advisory, 0 directional points.
- **Bull/bear debate** — kept but **shrunk** to the 1–2 real-edge names (there are rarely more).

## 4.4 The new architecture — `/market-scan` (supersedes `/daily-analysis` + `/weekly-analysis`)
A regime-first, horizon-aware pipeline. Five phases:

### Phase A — Regime & beta context (the master gate)
One agent, `regime-classifier`, builds the context every later phase consumes (absorbs `uw risk market-regime` + VRP + breadth + dealer-gamma **vol-state** + event calendar). It outputs a **regime label AND a "directional-edge-tradable?" verdict**, and critically a **momentum-crash / V-rebound / junk-rally / squeeze detector** (P3 §3.1: the unsampled regime that *inverts* S1). If that detector fires, **all S1 shorts stand down** and sizing is capped. GEX/DEX feed *only* the vol-state here (P3 STRONG), never a direction.

### Phase B — The edge scan (small, orthogonal, parallel — 4 directional lanes + 1 vol lane)
> **Updated by Phase 7 (`RESEARCH/70-factor-zoo.md`):** an exhaustive cross-sectional factor sweep across ALL 5 sources reconfirmed flow=beta on the full column set, **upgraded** the momentum lane to both legs, and **added** the `oi-flow-fade` lane (the most robust directional edge found).
| Lane | Agent | Edge | Horizon | Confidence | Cite |
|---|---|---|---|---|---|
| **Momentum (both legs)** | `momentum` (**NEW**, was `relative-weakness`) | 52w-range factor (rank-IC **t=+6.8**): SHORT near-low (+0.81% / +9.5pp hit) + LONG near-high (+2.35% mean, **tail-driven**) | **h≥10** | **HIGH** (short crash-gated; long=basket/tail) | P2 §2.1 S1; **P7 §7.2/§7.5b**; P3 §3.1 STRONG (George-Hwang) |
| **OI-flow fade** | `oi-flow-fade` (**NEW**) | heavy 5-day net call-OI build → underperformance; short **hit 0.61 vs 0.41, +2.1% median, n=640**; orthogonal to momentum (corr −0.17) | **h10** | **HIGH for this panel** (provisional) | **P7 §7.2/§7.5b** (rank-IC t=−7.1); corrects the old +1 OI-build sign |
| Liquidity reversion | `liquidity-reversion` (repurposed `accumulation-hunter`) | S2: DP one-sided-concentration → reversal | **h3–5** | MODERATE | P2 S2; P3 MODERATE (Nagel; long-tilted, news-gated) |
| Sentiment contrarian | `sentiment-contrarian` (narrowed `contrarian-scanner`) | S4: PCR-high fade-long + `ivrank_chg_5d` rising-IV tilt (h3) | h3 / h5–10 | LOW-MOD (advisory) | P2 S4; **P7** (ivrank_chg t=+5.2, 3-regime-stable); P3 MIXED |
| Vol book (non-dir) | `vol-book` (merged `earnings-scout`+`vol-surface-scout`+0DTE) | IV-crush SELL-VOL + 0DTE-VRP | event / 0DTE | MODERATE | P2 VOL-ONLY; P3 STRONG-but-fragile |

These lanes are **orthogonal by construction** (price-momentum / liquidity-event / sentiment / vol) — the opposite of the old fleet's 4 correlated flow agents (P2 H9). A name is a candidate if it lands in a lane that is **regime-appropriate**; there is no ≥2-agent confluence requirement (confluence of correlated betas was the bug, P2 §2.0).

### Phase C — Scoring (excess-as-currency, no additive stacking)
A candidate's score is **not** a sum of signal points. It is:
```
score = validated_excess(lane, horizon, regime)        # the measured edge magnitude for that lane/horizon/regime
        × regime_fit                                    # 1.0 if regime-appropriate, →0 if not
        × (1 − fundamental_contradiction)               # veto channel only
```
- `validated_excess` is read from the **truth-set tables** (`data/returns.parquet` + the per-lane calibration), stratified by regime. A lane in a regime where it has **no validated excess scores 0** (e.g. S1 short in a V-rebound).
- **No correlated-signal addition.** If two lanes flag the same name, that is *diversification of evidence type*, noted, but it does **not** multiply the score (the lanes are orthogonal; double-counting beta is the failure mode we removed).
- **Conviction tiers are excess-based**, e.g. HIGH = validated excess ≥ +1% with sign-stability across the available regimes; MEDIUM = +0.3–1%; else watch-only. Tiers are *descriptive of measured edge*, not a manufactured confluence count.

### Phase D — Gates & sizing (the surviving discipline + the new tail caps)
`risk-sizer` (= hardened `risk-monitor`) applies, in order:
1. **Regime/crash gate** (Phase A): S1 shorts off in rebound/squeeze; everything capped in out-of-regime tape (kept P0.6 half-cap discipline).
2. **Liquidity floor** (C12) — fail-closed.
3. **Correlation cluster** (corr ≥ 0.70 = one position).
4. **Fundamentals veto** (`fundamentals-gate`) — only on names about to be sized.
5. **Event-risk** — Tier-1 macro / earnings inside the horizon.
6. **Tail caps (NEW, from P3):** S1 short sized for momentum-crash tail; S2 cut on news/earnings; vol-short sized for the unsampled left tail (Vilkov). 
Sizing = `f(score) × tail_cap × regime_cap`, **net-of-cost** for the vol lane (P3: 0DTE flips negative gross→net once costs charged).

### Phase E — Envelope, calibration, write-back
Emit `decision.json` (extended schema — adds `lane`, `validated_excess`, `regime_fit`, `crash_gate`, `horizon_validated`), validate, write the conviction watchlist, and feed `/calibration-audit` — which now grades **forward excess** per lane per regime, accruing the cross-*year* evidence Phase 3 §3.2 flagged as missing.

## 4.5 The new agent roster (8, down from 16–17)
1. `regime-classifier` — master gate + vol-state + crash detector (absorbs market-regime, VRP, breadth, GEX/DEX-as-vol, event calendar).
2. `momentum` — **NEW** (was `relative-weakness`), the full 52w-range factor: long near-high + short near-low (P7).
3. `oi-flow-fade` — **NEW** (P7), the `oi_net_5d` fade — most robust directional edge; also a long-veto tilt.
4. `liquidity-reversion` — repurposed `accumulation-hunter`, S2.
5. `sentiment-contrarian` — narrowed `contrarian-scanner`, S4 + the `ivrank_chg_5d` h3 tilt (advisory).
6. `vol-book` — merged earnings/vol-surface/0DTE, non-directional.
7. `risk-sizer` — hardened `risk-monitor`: gates, tail caps, correlation, sizing, envelope, write-back.
8. `fundamentals-gate` — cheap veto on sized names (kept ~unchanged; `RESEARCH/80`: Finnhub stays a veto, not an alpha lane).
(+ optional bounded `bull/bear` debate on the 1–2 HIGH-tier names.)

**Cut from the old roster:** dealer-positioning-strategist, gamma-flip-tracker (directional), multileg-strategist, leap-positioning-radar, opex-pin-strategist (→ folded into vol-book/regime as conditional advisory), sector-rotation-strategist (→ advisory pending a test), sweep-tracker (→ a 0-point tell inside liquidity-reversion), signal-confluence-quant (→ replaced by the excess-scoring step in Phase C; the additive rubric it computed is gone).

## 4.6 Horizon honesty (what the panel can and cannot validate)
| Product horizon | Validated edge? | Disposition |
|---|---|---|
| 0DTE (next-session) | VRP premium-selling only (delta-neutral) | keep advisory, net-of-cost |
| swing 3D / weekly 5D | S2 (DP reversion), S4 (h5) | MODERATE/advisory |
| swing 10D / weekly 10D | **S1 (momentum-weakness)** | **the anchor edge**, regime-gated |
| LEAP 30D | thin (h21 resolves to ~late May only) | low-confidence/advisory |
| LEAP 90D | **unverifiable on this panel** (P1 §1.5) | **honest "cannot validate"; advisory only** |

This is why **one horizon-aware flagship supersedes daily+weekly**: each candidate is scored at the horizon where its lane is *validated*, and the product stops claiming directional LEAP conviction it cannot substantiate.

## 4.7 Open pre-registrations (decided by future data, not now)
- **PR-1:** sector-flow excess test (the one untested fleet lane) — promote/cut on cross-regime excess.
- **PR-2:** S1 short under a true momentum-crash regime (needs a panic-V-rebound window) — the tail the sample lacks.
- **PR-3:** S2 directional-vs-nondirectional + news-gating (does excluding news/earnings days sharpen it?).
- **PR-4:** does any signed/opening/intraday-granular flow (if finer data arrives) recover the alpha the EOD aggregate destroys (Pan-Poteshman granularity)?
- **PR-5:** S1 options-carry leakage — is the equity edge already priced into near-low put skew?

## 4.8 Roadmap → Phase 5
Build under `findings/artifacts/`: the `/market-scan` flagship command, the 7 agent files (3 new/repurposed + 4 kept), the extended envelope schema, and the **retrospective harness** that — given any signal-day — replays what `/market-scan` would have fired (entry/horizon/size/invalidation) and validates it against the known outcome in `returns.parquet`. Then Phase 6: MIGRATION.md, stop for approval.
