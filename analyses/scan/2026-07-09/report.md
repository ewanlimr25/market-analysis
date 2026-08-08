# Market Scan — 2026-07-09

## Regime & Verdict
- **Regime:** UPTREND (SPY 10d +2.52%, 5d +0.80%; QQQ 10d +1.78%, 5d −0.26%) · `directional_tradable` = **TRUE** ·
  `s1_standdown` = **FALSE** (both momentum legs live, no crash cap)
- **Vol-state:** SPY sitting **ON the zero-gamma flip** (spot $751.32 vs flip $751.74) — regime-transitional,
  a 2nd-moment conditioner only, no direction read. VIX 15.84, declining.
- **Breadth:** price breadth 59.84% green vs. options-flow breadth **soft-dissenting** at 36.8% bullish — the
  uw market-regime composite calls for **book-wide HALF position sizing** on this divergence. This is a
  ceiling on top of (not a replacement for) the excess-implied size — it is a **no-op tonight**: every sized
  name already caps at or below half from its own lane ceiling (OI_FADE HIGH-lane names cap at half by
  construction; S2/S4 never clear starter).
- **Event risk:** June CPI **2026-07-14** + PPI **2026-07-15** (both Tier-1) fall inside the h10 window opened
  by any short taken this week and inside the S2 h3–5 window. Big-bank earnings (JPM/BAC/C/WFC) also land
  7/14, inside h10, but don't touch any sized name — banks fail the vol-book IV-rank≥80 gate this run. A
  separate OI_FADE earnings cluster (EQR/TMHC/CSX/RJF 7/22, STLD 7/20) lands inside h10 and — combined with
  missing fundamentals verdicts on all five names — is held at watch, not sized. FOMC (7/28–29) is ~13
  trading days out, just **outside** every h10 window this week.
- On a beta-heavy tape the gate stack matters **more**, not less (`RESEARCH/50 §5.1`: ungated
  additive-confluence HIGH book realized −8.2%, 0-for-6).

> **Bottom line: 5 sized names (3 half, 2 starter), all in OI_FADE — the only lane clearing the +1% HIGH bar
> tonight.** UDR, MAT, and NKTR are clean CONFIRM cases with no event risk inside h10 and no cluster/tail
> flags — sized at the HIGH-lane half ceiling. FROG is tail-adjusted to starter on a genuine CAUTION
> fundamentals tension (beats + 25% growth vs. insider selling). MARA is the most interesting case tonight:
> CONFIRM fundamentals and same-day OI-print corroboration make it look like the cleanest setup, but beta
> 5.38 plus a live bullish TX-power catalyst is an **extreme, explicitly-flagged squeeze tail** — capped at
> starter with a mandatory defined-risk structure (no naked short), regardless of signal quality (no
> additive confluence). CPRX is a clean **VETO**: 4/4 beats, +11.65% revenue, zero debt fight the short, and
> the flow is a dated S&P SmallCap600 removal (technical, not thesis). Five more OI_FADE candidates
> (EQR/TMHC/CSX/RJF/STLD) sit at watch on missing fundamentals verdicts stacked with earnings inside h10.
> MUR/BP (Energy cluster pair) and NVDA/MSFT (S2) also sit at watch — S2's MSFT is independently cut by its
> own same-day-negative-news tail-cap rule regardless of its CAUTION verdict. All ten S4 names are
> advisory-lane and missing fundamentals verdicts — held at watch across the board. MOM_SHORT/MOM_LONG fired
> no named tickers this run (aggregate cohort stats only) — flagged back to the orchestrator to emit names
> next run.

## Directional Book (excess-scored)
| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | Size | Invalidation | Gates |
|---|---|---|---|---|---|---|---|---|
| **UDR** | OI_FADE | short | h10 | +2.1% median (hit 0.61 vs 0.41, n=640) | 0.65 | **half** | Close > $42.00, or the 5d build fully unwinds without downside follow-through | CONFIRM (miss streak, insider selling, Truist downgrade) · liquidity PASS ($39.69, $159.4M ADV) · cluster: REIT pair w/ EQR flagged, EQR not live (event-risk + missing verdict), UDR stands alone · event: earnings 7/27 outside h10; CPI/PPI defined-risk-through-print · tail cap: HIGH-lane half ceiling, no squeeze flag |
| **MAT** | OI_FADE | short | h10 | +2.1% median (hit 0.61 vs 0.41, n=640) | 0.60 | **half** | Close > $16.50, or the 5d build fully unwinds without downside follow-through | CONFIRM (neg. rev. growth + same-day Goldman downgrade to Sell) · liquidity PASS ($13.18, $62.9M ADV) · cluster: standalone · event: earnings 8/04 outside h10; CPI/PPI defined-risk-through-print · tail cap: HIGH-lane half ceiling |
| **NKTR** | OI_FADE | short | h10 | +2.1% median (hit 0.61 vs 0.41, n=640) | 0.55 | **half** | Close > $85, or the 5d build fully unwinds without downside follow-through | CONFIRM (insider MSPR −100, revenue −36%) · liquidity PASS ($72.92, $94.9M ADV) · cluster: standalone · event: earnings 8/06 outside h10; CPI/PPI defined-risk-through-print · tail cap: HIGH-lane half ceiling, low IV rank (5.8) argues no imminent vol tail |
| **FROG** | OI_FADE | short | h10 | +2.1% median (hit 0.61 vs 0.41, n=640) | 0.35 | **starter** | Close > $105, build unwinds, or another beat confirms growth over flow | **CAUTION** (beats + 25% growth genuinely fight the short vs. insider MSPR −68.66) → −1 tier off the half ceiling · liquidity PASS ($95.50, $354.3M ADV) · cluster: standalone · event: earnings 8/06 outside h10 |
| **MARA** | OI_FADE | short | h10 | +2.1% median (hit 0.61 vs 0.41, n=640) | 0.30 | **starter** (defined-risk structure mandatory) | Close > $16.50, or the TX-power catalyst headline escalates | CONFIRM (miss streak, insider MSPR −100) + same-day OI print corroboration · liquidity PASS ($13.22, $556.2M ADV) · cluster: standalone · event: earnings 8/04 outside h10 · **EXTREME tail cap: beta 5.38 + live bullish TX-power catalyst = squeeze risk — capped at starter regardless of signal quality (no additive confluence)** |

**Cut to watch/dropped (not sized, detail below):** OI_FADE — CPRX (VETO), EQR/TMHC/CSX/RJF/STLD (earnings
inside h10 + missing verdicts), MUR/BP (Energy cluster, missing verdicts). S2 — NVDA (CAUTION, −1 tier),
MSFT (same-day negative news tail-cap cut, independent of its CAUTION verdict). S4 — all ten names
(BCE/AMRZ/SYY/BKD/EXE/KD/RARE/LYB/SPG/VALE) held at watch, missing fundamentals verdicts (advisory lane).
MOM_SHORT/MOM_LONG — no named tickers surfaced this run.

## Vol Book (non-directional)
- **NFLX** (primary) — earnings 2026-07-16 postmarket, IVR 98.7, implied move **1.47%**. Liquidity PASS
  ($75.47, $3.73B ADV). Crush survives cost. Small size, wide wings, two-sided tail; net-of-cost expectancy
  not independently recomputed — do not enter until it prices net-positive.
- **TSM** (primary) — earnings 2026-07-16 premarket, IVR 94.5, implied move **1.94%**. Liquidity PASS
  ($436.96, $6.56B ADV). Crush survives cost. Same structure discipline as NFLX.
- **ASML / JNJ / ABT / CTAS / CAG** (secondary, half-size wide-wing advisory) — IVR 93.9 / 84.5 / 96.3 /
  95.1 / 83.5 respectively, earnings 7/15–7/16, all premarket. Implied moves 2.50% / 1.17% / 1.01% / 1.47% /
  1.71%. All clear the $50M liquidity floor comfortably (thinnest is CAG at $317.7M ADV). CTAS/CAG/ASML/JNJ
  report on PPI day (7/15) — the print itself doesn't gate a delta-neutral book, but expect wider realized
  ranges into the print.
- **Banks:** none clear the IV-rank ≥ 80 gate this run — the 7/14–15 bank earnings cluster produces no vol
  candidate tonight (contrast STT last week).
- **SPY-0DTE:** reduced-conviction half-of-half. IVR 14.4 (LOW vol), sitting on the zero-gamma flip — thin
  net-of-cost edge (~+3bps/day). Keep structures small; the flip proximity means a modest spot move can flip
  local gamma sign intraday.
- **QQQ-0DTE: STAND ASIDE.** Front-month backwardation gate fails, 30d signal reads PREMIUM_BUYING (not
  selling), and GEX data is unreliable tonight. No edge to sell premium; the unsampled left tail is not
  compensated.

## Watch / Stood-down
- **OI_FADE VETO (dropped entirely):** **CPRX** — 4/4 EPS beats, +11.65% revenue, 37% margin, zero debt
  directly fight the short; the flow driver is S&P SmallCap600 index-removal effective 2026-07-15, a dated
  mechanical event, not a thesis-relevant positioning signal.
- **OI_FADE earnings-inside-h10 + missing verdict (held at watch, flagged back to orchestrator for
  next-run spawn):** **EQR** (earn 7/22, REIT-cluster partner to UDR — corr≥0.70 pairing noted, moot while
  watch), **TMHC** (earn 7/22), **CSX** (earn 7/22), **RJF** (earn 7/22), **STLD** (earn 7/20). All five
  would additionally require a defined-risk-through-print structure once/if a fundamentals verdict clears,
  given earnings land inside the h10 window.
- **OI_FADE Energy cluster, missing verdict:** **MUR, BP** — corr≥0.70 pair per Phase-B pairing note,
  flagged back to the orchestrator; would collapse to one theoretical position (`oi_fade_energy_cluster_0709`)
  once verdicts clear.
- **S2 — NVDA held at watch (CAUTION, −1 tier):** genuine one-sided DP concentration (98.5% buy-side, $691M)
  with clean earnings/growth fundamentals otherwise, but insider MSPR −98.61 into the accumulation is enough
  of a flag to hold at watch rather than size starter tonight.
- **S2 — MSFT held at watch (independent tail-cap cut):** strong DP concentration (96.6% buy-side, $707M) is
  exactly the S2 setup, but a same-day negative news cluster triggers the lane's own explicit tail-cap rule
  ("cut on any same-day news/catalyst") regardless of flow quality — this is a sufficient cut on its own, and
  compounds with (does not sum with) the separate CAUTION fundamentals verdict (insider MSPR −83.89).
- **S4 sentiment-contrarian — all ten names held at watch, missing fundamentals verdicts (advisory lane,
  flagged back to orchestrator):** **BCE, AMRZ, SYY, BKD, EXE, KD, RARE, LYB, SPG, VALE.** SYY carries an
  extra Phase-B flag — a *real* downgrade requiring diligence, not noise — elevated risk vs. the rest of the
  cohort even once a verdict lands. KD's liquidity is the thinnest of the group ($55.9M ADV) but still
  clears the $50M floor. S4 is advisory-only by lane construction regardless (half-cap ceiling even at full
  conviction), so this cohort was never going to clear starter tonight even with clean verdicts.
- **MOM_SHORT — no named candidates fired.** Phase B reported aggregate cohort stats only (29 liquid
  near-52w-low names, 6 sector cohorts flagged for corr≥0.70 collapse, bond-ETFs deweighted as rate-beta not
  weakness) but no ticker list reached Phase D this run. Not S1-crash-gated (`s1_standdown`=FALSE) — the gap
  here is a data-pipeline one, flagged back to the orchestrator to emit names next run.
- **MOM_LONG — no named candidates fired.** Same gap: 378 liquid near-52w-high names reported in aggregate
  (median≈0, edge outlier-carried; 9/20 top names healthcare, sector-cap noted) but no ticker list reached
  Phase D. Basket-only by construction regardless (never per-name HIGH, tail-driven +2.35% mean) — flagged
  back to the orchestrator.

## Risk
- **Correlation clusters applied:** (1) REIT pair UDR–EQR — EQR isn't live (event-risk + missing verdict),
  so UDR sizes standalone; re-evaluate the pair once EQR clears. (2) Energy pair MUR–BP — both held at
  watch on missing verdicts, would collapse to one position once live. No other pairwise correlations ≥0.70
  identified among today's five sized names — UDR/MAT/NKTR/FROG/MARA span Real Estate, Consumer Cyclical,
  Healthcare, Technology, and Financial Services with no shared theme.
- **Extreme tail cap — MARA:** beta 5.38 is the highest in tonight's book by a wide margin, and the bullish
  TX-power catalyst is a live, ongoing news thread, not a one-off. This is exactly the squeeze-tail case the
  gate stack exists to catch — CONFIRM fundamentals and same-day OI corroboration do not buy back the tail
  risk (no additive confluence). Sized at starter with a mandatory defined-risk (put-spread) structure — no
  naked short on this name under any circumstance tonight.
- **Event overhang:** CPI (7/14) + PPI (7/15) sit inside every h10 window opened this week and inside the S2
  h3–5 window. Applied as defined-risk-through-print on UDR/MAT/NKTR/FROG/MARA (OI_FADE) — not an automatic
  downgrade, since none of these are macro-directional bets. The separate OI_FADE earnings cluster
  (EQR/TMHC/CSX/RJF/STLD, 7/20–22) is a harder gate — earnings inside h10 stacked with a missing fundamentals
  verdict is enough to hold all five at watch outright, not merely defined-risk.
- **Liquidity floor:** every sized name and every vol-book name clears the $50M ADV floor with real margin
  (thinnest sized name is MAT at $62.9M ADV). No liquidity-driven drops tonight — verified directly against
  the Stock Screener parquet (2026-07-09 snapshot) via DuckDB rather than trusting Phase B's pre-applied
  floor.
- **Regime-cap discipline:** the book-wide HALF ceiling from the uw market-regime composite (options-flow
  breadth soft-dissent) is a no-op tonight — every sized name already caps at or below half from its own
  lane ceiling. The hard rule (never up-size above the excess-implied size) held throughout — FROG's and
  MARA's tail-cap downgrades are both reductions, never upgrades.
- **Missing-verdict discipline:** seven OI_FADE names (EQR/TMHC/CSX/RJF/STLD/MUR/BP), both S2 secondary
  candidates, and all ten S4 candidates are sitting on the sideline at least partly because a fundamentals
  verdict hasn't been run yet — flagged back to the orchestrator, not silently dropped or silently sized.
  This is the largest missing-verdict count of any run to date; worth a data-pipeline note for the
  orchestrator (see below).
- **Data-pipeline note (not a gate, a process flag):** MOM_SHORT and MOM_LONG reported only aggregate cohort
  statistics tonight, no ticker lists — Phase D cannot size, cluster, or fundamentals-gate a basket it
  doesn't have names for. Recommend Phase B emit the actual name lists alongside the cohort stats next run.
- **Hedge note:** five shorts (three half, two starter) against zero live longs tonight (both S2 candidates
  held at watch) — net book exposure is short and moderate, concentrated entirely in the OI_FADE lane. In an
  UPTREND regime with no s1_standdown, this is a deliberate short bias built entirely from idiosyncratic
  flow+fundamentals confirmation, not a index-directional bet — consistent with invariant #2 (no additive
  confluence, one lane scores at a time) and invariant #3 (say so when the book is thin/skewed).

---
*Envelope: `decision.json` (schema v2, validated — `python3 scripts/validate_decision.py --file
analyses/scan/2026-07-09/decision.json` → VALID). Conviction write-back persisted to
`conviction_2026-07-09.json` for next run's adverse-flow exit check (UDR, MAT, NKTR, FROG, MARA). Regression
gate not run tonight — no lane/threshold changes made.*
