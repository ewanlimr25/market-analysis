# Market Scan — 2026-07-06

## Regime & Verdict
- **Regime:** CHOP / REBOUND-THRUST · SPY +0.61% (10d) vs QQQ **−2.40%** (10d) — mega-tech/index divergence
- **Vol-state:** SPY positive-gamma **fragile** (spot ~751.1 pinned on ZGL 751.1) · QQQ **negative-gamma** (vol-amplifying, spot well below ZGL 749.5) · VIX 15.57 (−20%/2wk, complacent) — *2nd-moment conditioner only, no direction read*
- **Breadth:** 43.74% green, 37.4% bullish-flow on a green tape — soft, **distribution tell**
- `directional_tradable` = **TRUE** · `s1_standdown` = **TRUE** (V-rebound crash guard: SPY 5d +3.06% / QQQ +2.31% off a −3.4%/−5.0% 15d dip)
- **Event risk:** CPI **2026-07-14** + PPI **2026-07-15** — both Tier-1, both **inside** the h10 window opened this week

> **Bottom line: 1 sized directional call.** A half-capped standdown day. One clean OI-fade short (GFL, defined-risk through the prints), a thin advisory vol note (PEP, confirm-before-entry), and a broad watch list. The robust lane (OI_FADE) is live and not standdown-gated; every other lane resolved to watch/advisory after gating. This is the correct, expected shape for a CHOP + crash-guard tape.

## Directional Book (excess-scored)
| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | Size | Invalidation | Gates |
|---|---|---|---|---|---|---|---|---|
| **GFL** | OI_FADE | short | h10 | **+0.88%** mean (hit 0.61 vs 0.41, +20.5pp; n=640) | 0.70 | **starter** (defined-risk put spread) | Reclaims $44–45 supply zone on a real catalyst, **or** the 5d call-OI build fully unwinds without downside follow-through into CPI/PPI | Fund **CONFIRM** (collapsing EPS, JPM UW $40 PT) · liquidity PASS ($40.49, $138.6M ADV) · **isolated** (not clustered w/ CRWD/NRG) · event: defined-risk **through** 07-14/07-15, no naked exposure |

**Why only GFL:** it is the one OI-fade short whose fundamentals *corroborate* the fade (deteriorating EPS + sell-side underweight), whose relative call-OI build (1.10× own base) is high enough to be signal but not so extreme it carries squeeze-tail risk, and which sits in its own sector (waste/industrials — no shared factor channel with the tech/utility shorts). Sized `starter`, never single-name HIGH/half — OI_FADE is a dispersion edge, not a conviction call.

## Vol Book (non-directional)
- **PEP** earnings-crush (reports 2026-07-09 premarket, 3 sessions out) — IV-rank 81.5, implied move **3.46%**. **Advisory / confirm-before-entry:** 2025 Q2 realized **+7.45%** (a 2×+ blow-through of today's implied move), so a tight IV-crush strangle sized to the implied move is *not* sized for that tail. Only structure worth considering is **small size, WIDE wings** (defined-risk, short strikes well beyond 3.46%). Net-of-cost expectancy on the wide-wing structure was **not** independently recomputed — do not enter until it prices net-positive.
- **0DTE-VRP (SPY/QQQ): STAND ASIDE both.** SPY VRP FAIR under a fragile long-gamma pin (no edge); QQQ negative-gamma + front backwardation is net-of-cost **negative** for premium selling.

## Watch / Stood-down
- **OI_FADE, gated to watch (real signal, real gate):** **CRWD** — highest rel-build on the board (2.57×, 525k) but CAUTION (informed-flow) + QQQ-neg-gamma squeeze tail both cap it; **NRG** — insider **buying** (+62 MSPR) + AI-power demand narrative contradicts the fade; **DLO, MSM** — **VETO** (accelerating fundamentals / 4-of-4 beat streak — the crowded calls are likely right).
- **S2 dark-pool reversion:** **KVUE cut** — live $48.7B Kimberly-Clark takeover bid voids the reversion mechanism (it's merger-arb now); **PTCT VETO** (rev −53% YoY + insider selling); **MNST** advisory only. Others (SW/KRG/OTIS/DOCN/…) advisory/watch, not sized. **SUNC dropped** (fails $50M liquidity floor, ~$30.5M ADV).
- **S4 PCR-fade:** **ITT cut** (07-06 ex-dividend contaminates the PCR signal); LFUS/GTES held at watch (fundamentals verdict pending).
- **MOM_LONG basket** (PTRN/TENB/ILMN/GD/NTRS): tail-driven, hit−base **−9.3pp** → factor tilt / watch only under CHOP + macro overhang, never per-name sized.
- **MOM_SHORT** (OLLI/ORLY/BCE/MAT/…): **fully stood down** by `s1_standdown` → re-entry watch when the guard lifts.
- **Canadian-financials cluster** (TD/RY/BMO/CP): collapsed to one, held at watch (corr≥0.70 assumed on peer/country beta; note these ADRs are outside the truth-set panel — data gap).

## Risk
- **Event overhang:** CPI (07-14) and PPI (07-15) both land inside any h10 window opened this week. The single sized name (GFL) is expressed as a **defined-risk put spread**, not a naked short, specifically to cap gap risk through the prints. No other h10 directional exposure is on.
- **Gamma asymmetry:** SPY moves get dampened (long-gamma pin ~751), QQQ moves get amplified (negative gamma). A stall in the mega-cap-led bounce accelerates downside in tech — this is *why* CRWD is watch not sized despite the best OI-fade signal.
- **Distribution tell:** green index prints on sub-50% breadth + net-bearish flow-name count. Consistent with a narrow, single-name-driven bounce (MU/SPCX/NVDA/TSLA/AMD dark-pool concentration) — not broad participation.
- **Correlation:** the three OI-fade shorts (GFL/CRWD/NRG) were checked as cross-sector dispersion (CRWD↔NRG measured corr −0.11), not one theme — but only GFL is sized, so no live cluster exposure.

---
*Envelope: `decision.json` (schema v2, validated). Conviction write-back (30 names) persisted for next run's adverse-flow exit check. Regression gate not run — no lane/threshold changes tonight.*
