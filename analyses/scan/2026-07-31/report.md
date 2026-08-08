# Market Scan — 2026-07-31

## Regime & Verdict

- **Regime:** CHOP · ret5 **+1.100%** · ret10 **+0.500%** · dd15 −1.860% (`scripts/regime_check.py`, authoritative)
- **Vol-state:** VIX **15.99** (−6.4% d/d; **−22.6%** off the 07-29 spike of 20.66). Forward term structure **CONTANGO** on both indices (VIX3M 19.02 > VIX 15.99; 3–6DTE→30DTE curve rising on both). The 07-30 backwardation has cleared.
- **Dealer gamma is split:** SPY **POSITIVE but pinned on the flip** (spot 747.06 vs zero-gamma 746.93, total_gex +$1.19B) — long-gamma by a coin-flip's width. QQQ **FULLY_NEGATIVE** (short gamma at every sampled strike). Vol-state conditioning only; no direction read from this.
- **Breadth contradicts the tape, second straight night:** pct_green **43.94%** (221 adv / 281 dec), UW bullish_pct **34.1%**, Technology the largest sector outflow (−$187.7M) — while SPY grinds higher and sits above both the 20- and 50-SMA.
- `directional_tradable` = **TRUE** · `s1_standdown` = **FALSE** (mechanical, recorded as measured)
- **Bottom line: No new directional starters. Third consecutive session at zero for OI_FADE.** One held short (PLNT) carried to its binding exit Monday. Vol book active on three earnings-crush names + both 0DTE indices.

### V-rebound caution (recorded, NOT applied as a flag flip)

Phase A independently re-raised it: the week is structurally a V-shape (SPY −2.40% ret5 on 07-29 → +1.68% on 07-30 → +0.72% today). The `s1_standdown` guard mechanically **cooled off one day after** the shape that would have fired it — +1.10% ret5 sits below the +1.5%-off-a-dip trigger. Combined with the breadth divergence, this reads as a narrow, unconfirmed bounce sitting on top of a real V.

Handled exactly as the 07-30 precedent: **the mechanical flag is recorded FALSE and not hand-flipped**, because `regime_check.py` is the field `/calibration-audit` grades the crash gate against, and hand-editing it would corrupt that measurement. The caution is carried as sizing discretion instead. It is moot operationally tonight — nothing new was sized, and MOM_SHORT is already unsized under invariant #6.

---

## Directional Book (excess-scored)

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| PLNT | OI_FADE | short | h10 | +0.70% mean (hit 0.56 vs 0.38, n=906) | 0.50 | **half (held, unchanged)** | **Binding h10 exit = 2026-08-03 close, ONE session left**; leg (b) not strictly triggered; $59.50 stop live | all PASS |

**No new starters.** Zero names cleared the full stack.

### PLNT — HOLD to Monday's close

Entry 2026-07-20 @ $55.20 · mark **$55.91** · gross **−1.29%** · **since-entry SHORT excess −0.53%**.

> Computed directly against SPY. `held_book.py` prints `gross` (since-entry) beside `excess` (**today-only, +0.85%**) on adjacent lines — two different horizons. Do not read that column as since-entry.

- **Signal is decaying but has not crossed.** Pre-registered exit leg (b) is "first genuinely NEGATIVE `call_net`": today `call_net` = **+20**, still nominally positive. But puts opened +355, so **net OI printed −335 — the first negative net-OI print of the hold.**
- **Not exiting early.** Jumping an unconfirmed pre-registered trigger is a discretionary override of a mechanical rule. The h10 timer binds Monday regardless; if leg (b) confirms intraday Monday, both resolve on the same session.
- **$59.50 stop is LIVE, not vestigial.** `held_book.py` flagged it VESTIGIAL (6.42% away, beyond entry). Overridden on the same reasoning as 07-30: the vestigial precedent describes a position that has run **>10% in its favor** so its old stop can no longer bind. PLNT is *adverse* (gross −1.29%) — opposite geometry. With one session left it is near-moot either way.
- **Event-clean:** PLNT reports 08-06, three sessions *after* the 08-03 exit. NFP (08-07) and CPI (08-12) both land after exit.

---

## Vol Book (non-directional, advisory, 0 directional points)

**Earnings IV-crush — SELL VOL, all three carried positions re-confirmed.** Ranked by implied-move vs each name's **own realized post-print history**, not IV rank.

| Symbol | Reports | Implied | Realized avg / max | Note |
|---|---|---|---|---|
| LDOS | 08-04 BMO | 7.6% (was 8.5%) | 2.70% / **7.23%** | Buffer thinned to **~0.4pp** — keep wings wide, do not let structure creep narrower |
| TRMB | 08-05 BMO | 8.9% | 2.41% / 5.50% | ~3.4pp buffer, best chain liquidity of the group |
| TTMI | 08-05 AMC | 19.3% | 8.64% / 16.63% | ~2.7pp buffer, size stays reduced for chain thinness |

None tripped the UCTT exclusion condition (max-realized > implied). **Zero new genuinely-rich names** from ~27 screened — every one screened IV-*cheap* vs its own history.

**0DTE-VRP.** The 07-30 stand-down rested on a three-condition triad (backwardation + dealer-short-gamma + VIX spike). Only **1 of 3** is present tonight.
- **SPY: GO**, half size. Iron fly/short straddle ≈747, wings ≈ ±0.79% (≈741.4–752.5).
- **QQQ: GO but reduced (≤0.5×) and widened.** Wings ≈ ±2.01% (≈674.2–701.8). Dealer short-gamma confirmed by *both* the CLI and the script tonight — they agree, unlike 07-30.

`net_expectancy` **NULL on all five entries.** The gross figures (SPY +0.248%/day, QQQ +0.382%/day) come from a 60-day sample containing no vol-shock day, and no measured half-spread cost constant exists in this repo. Fabricating a net number would violate the net-of-cost discipline it pretends to satisfy.

> **Caveat on QQQ:** its VRP is **negative (−3.23%)** — realized 25.88% ran *above* implied 22.65%. Options never repriced this week's whip. That is an argument against selling QQQ premium that is independent of the gamma sign, and it is why the size cut matters.

---

## Watch / Stood-down

**OI_FADE** — zero starters, third straight session.
- **AVTR** — cleanest mechanical profile in the panel (rel_build 2.657, persistence 0.416 organic, catalyst LIVE, earnings 11-04 clear). **VETO SUSTAINED.** Re-admit condition re-tested tonight; neither half met. A 07-31-datelined PT-raise item was a **lagged republication** of the same 07-30 actions, not new coverage; FY2026 guidance is still the freshly-raised figure.
- **HRI** — **VETO SUSTAINED**, both halves unmet. Additionally *worsening*: persistence 0.847 sits on the 0.85 fail line, and it printed **+2.89%** today, so the "shorting a completed collapse into a bounce tail" objection is stronger, not weaker.
- **INFY** — WATCH, mechanism fail unchanged. Tonight's +3,568/+2,812 add is noise on a block: the 07-30 print alone is **98.4%** of the 5-day net, persistence still 0.984.
- **OLLI** — **DROPPED.** `call_net` went genuinely **negative (−7)** — calls closing, a real lane invalidation, not just the persistence complaint.
- Cut: QGEN/SOLV/DBX/TPG (earnings inside h10) · KBR (**RESOLVED_PRE_PRINT** — build died at its own 07-30 catalyst) · MTUM (ETF) · APAM ($37.7M ADV) · SHAZ (listing age 41 days post reverse-merger — 30d OI base not meaningful).

**MOM_SHORT** — watch-only capped (invariant #6). Clean after the corrected earnings gate: **CRH, LII** (+ CLBK, PATK, both fail-closed on the parquet gap). Earnings-blocked: ECHO (08-03), PEG (08-04), FIGR (08-13), QXO (08-13).

**MOM_LONG** — basket, watch-only. +0.18% mean is below the +0.3% threshold; median −1.06%, tail-driven. 191 names, of which **only 106 pass the h10 earnings gate**.

**S2 liquidity-reversion (advisory, +0.06%)** — 58 names. Top: WFC, VZ, ITW, CMS, TD, CRH, RY, TRP, BNS, TSCO. **CRH appears in both S2 and MOM_SHORT — recorded as evidence-type diversification, never summed** (additive confluence realized −8.2%, 0-for-6).

**S4 sentiment-contrarian (advisory)** — JEF, DKS, DPZ (the only names both correlation-checkable and not premium-harvested) · VMC, EQIX, SWKS (premium already harvested, `ivrank_chg_5d` −30.2/−39.7/−43.6) · PUMP, TENB, VIK, ESI, LBRT, HUBB, CSX, EIX, AGNC, GFI, KMX, NSC, GDDY (**fail-closed**, absent from `prices.parquet`).

QTWO self-excluded cleanly: PCR collapsed **147.00 → 0.30** post-print.

---

## Risk

**Correlation clusters.** Only pairwise corr ≥ 0.70 found: **VMC ↔ CRH**. `risk-sizer` reported **0.77**; my independent recomputation on 62 days of daily returns gives **0.871**. The window/method differs and I did not reconcile them — but both sit above the 0.70 threshold, so the verdict (collapse to one position if both were ever sized) is unchanged either way. Moot tonight; neither is sized. Recorded because the two figures should agree and don't.

**Event calendar.** ISM Mfg **08-03** (Mon) · **NFP 08-07 (Tier-1)** · **CPI 08-12 (Tier-1)** · PPI 08-13. A fresh h10 window opened tonight runs 08-01→08-15 and therefore **captures both NFP and CPI**; an h5 window captures NFP on its boundary. This is a live argument against opening anything tonight, and it applies on top of the lane verdicts. PLNT's exit lands clear of both.

**Tail caps.** MOM_SHORT watch-only cap holds. Vol-short sized for the unsampled left tail with `net_expectancy` NULL rather than fabricated.

**Hedge note.** No net directional exposure beyond one half-size short resolving Monday. No hedge required.

---

## Process findings

1. **`data/prices.parquet` coverage gap is now blocking real decisions — fix this first.** The parquet carries **783 tickers** vs `features.parquet`'s **2,460**, so the correlation-cluster gate is only computable on the narrower panel. Tonight **13 of 19 S4 names** (including top-ranked PUMP) and **2 of 4 clean MOM_SHORT names** were uncomputable. Treated **fail-closed** by both the orchestrator and `risk-sizer` independently. This is the **fifth consecutive session** this class has surfaced (07-28 HOG · 07-29 HRI/PLNT · 07-30 LHX/VICI · tonight the S4 majority) and the **first on which it touched a lane that was a live sizing candidate** — it is no longer moot. The gate does not error when a ticker is missing; it silently returns nothing.

2. **The momentum lane's earnings gate is broken — it reported "0 dropped" and that is false.** Independent re-run: **4 of 8** MOM_SHORT names (ECHO, PEG, FIGR, QXO) and **85 of 191** MOM_LONG names report inside the h10 window. PEG and QXO were *already* earnings-blocked on 07-30, so the lane regressed on names it had previously excluded correctly. Same class as the ROST `prior_verdicts` bug — the lane runs the script and then misreports the result. Nothing live depended on it (both legs watch-only), but this is a measuring-instrument failure and the third consecutive night of a momentum-lane hygiene defect. **The `prior_verdicts` half is genuinely fixed** — 37 blocked names dropped, ROST correctly absent, zero ETP leakage.

3. **`front-end-iv-ratio` needs a `near_dte_actual` check every time it is read.** Tonight it reported backwardation on both indices (SPY 1.61, QQQ 1.70) with `near_dte_actual=0` — that is today's *expiring* 0DTE contract against the 30-day, a same-day-expiry inflation artifact, not a forward signal. The genuine forward curve is in contango. **This casts doubt on the 07-30 0DTE stand-down**, which cited "front-end backwardation on both (1.296× / 1.445×)" as one of its three conditions. I cannot retroactively verify that night's `near_dte_actual`, so I am not claiming the 07-30 call was wrong — but the metric it rested on has a known artifact mode that was not checked. Worth resolving in `/calibration-audit`.

4. **`fundamentals-gate` deliberately NOT spawned on JEF/DKS/DPZ**, against `risk-sizer`'s action item. Phase D rule 4 gates *only names about to be sized*; S4 resolved to advisory/watch, so gating them would contradict the same discipline that correctly left OLLI ungated on 07-30. Recorded as an explicit adjudication rather than an omission. If S4 is ever elevated to starter, these three need the gate first.

5. **S4 tier-vs-confidence conflict resolved on the sizing map, not by re-litigating the rubric.** Phase C names +0.3–1% "MEDIUM", which reads as sizeable; the envelope's actual sizing map reads `+0.3–1% → starter` with **half reserved for ≥+1% sign-stable**, and separately `advisory lane → watch`. So half-cap was never reachable for S4 at +0.44% on magnitude grounds, independent of the LOW-MOD confidence tag. The Phase C tier *names* and the sizing *map* use overlapping language for different things — worth reconciling in the spec so this is not re-derived nightly.

6. **`scripts/zerodte_setup.py` QQQ gamma-sign bug did not bite tonight** — script and CLI agreed on QQQ's negative sign. The bug (summing 0–45DTE net gamma instead of spot-vs-zero-gamma-level) is still unfixed and still logged from 07-30; it simply did not surface. Do not treat this as evidence it is resolved.
