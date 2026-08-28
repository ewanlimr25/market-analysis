# Market Scan — 2026-08-27

## Regime & Verdict
- **Regime: CHOP** · ret5 **+1.110%** · ret10 **−0.870%** · dd15 **−1.960%** (trough-anchor distance, *not* drawdown-from-highs — the 15d low sits below the c10 anchor and price has already recovered above it)
- **Vol-state:** VIX **14.51**, −4.60% on the day and **−9.37% over 5 sessions** — LOW tercile and falling. SPY VRP −0.44% (IV30d 11.84% vs realized30d 12.29%) — **FAIR, no premium-selling edge from VRP alone.**
- **Dealer gamma (hand-derived from the per-strike ladder — see correction below): SPY is sitting ON its zero-gamma flip, QQQ is cleanly LONG gamma and pinned.**
- **Breadth: the median stock fell while the index rose.** Full 5,931-name spine 49.28% green (2,923 adv / 2,919 dec); **top-500 by market cap only 35.60% green, median −0.565%**; top-2000 42.20% green, median −0.31%. SPY +0.655%, QQQ +1.369%, IWM +0.294%. **A narrow, earnings-gap-led advance — this is a genuine distribution tell.**
- `directional_tradable` = **true** (non-empty cohorts in all four lanes) · `s1_standdown` = **false**, but a **double near-miss**: ret5 +1.11% vs the 1.5% leg and dd15 −1.96% vs the −2% leg. A slightly stronger thrust tomorrow flips this to REBOUND-THRUST.
- **Bottom line: NO DIRECTIONAL EDGE. Zero sized calls — a 14th consecutive flat session.** No lane has a positive, significant excess in tonight's regime cell.

## Directional Book (excess-scored)
**Empty — zero sized calls.** No lane in this repo sizes at all since OI_FADE's 2026-08-22 demotion to advisory. **Phase D (`risk-sizer`) was vacuous and `fundamentals-gate` was correctly not spawned** — it runs only on names about to be sized.

### Phase C — the applicable regime cell, exit-day-clustered
Tonight is **plain CHOP with `s1_standdown=FALSE`**. The pooled "CHOP" row must **not** be used: it collapses plain CHOP with CHOP/REBOUND-THRUST, and **OI_FADE's sign flips between them** — measured again tonight: **collapsed +0.0023 (n=492) vs plain −0.0010 (n=344) vs REBOUND-THRUST +0.0098 (n=148)**. The correct cell, with `t` clustered on **exit-days**, not rows:

| Lane | n rows | exit-days | mean excess | t (exit-day) | p | hit − base | verdict |
|---|---|---|---|---|---|---|---|
| MOM_LONG | 356 | 24 | **−0.0257** | −2.41 | **0.024** | −0.360 | significantly NEGATIVE |
| MOM_SHORT | 282 | 24 | −0.0220 | −1.93 | 0.066 | +0.064 | negative |
| OI_FADE | 344 | 23 | −0.0010 | −0.13 | 0.900 | +0.235 | indistinguishable from zero |
| S2_dp_revert | 395 | 27 | +0.0011 | +0.26 | 0.795 | −0.038 | indistinguishable from zero |
| S4_pcr_fade | 402 | 27 | +0.0067 | +1.40 | 0.173 | +0.012 | not significant |

**Every cell carries the correlated-draw caveat** (all exit-day counts < 30, invariant #6). The only statistically real number in the table is **MOM_LONG's negative excess in CHOP** — an argument *against* the near-52w-high basket tonight, not for anything. Score = `validated_excess × regime_fit` = **0 or negative for every candidate**; nothing reaches a sizing band.

## Correction — the dealer-gamma read (both Phase-A and Phase-B agents got this partly wrong)
I summed the per-strike ladder myself rather than accept either agent's conclusion.

| | SPY | QQQ |
|---|---|---|
| Spot | 770.55 | 720.00 |
| CLI `regime` field | NEGATIVE | POSITIVE |
| CLI `zero_gamma_level` | 774.33 | 719.16 |
| CLI header `total_gex` | +690.0M | +1,153.0M |
| **My sum of the published ladder** | **+881.5M** | +1,221.8M |
| **Cumulative net-GEX UP TO SPOT** | **+21.7M ≈ zero** | **+736.7M** |
| Net-GEX above spot | +859.8M | +485.1M |
| My cumulative zero-crossing | **strike 770** (spot 770.55 — *on* it) | strike 717 (spot 720 is above it) |
| Dominant wall at spot | 770: **+359.9M** | 720: **+601.0M** |
| **Hand-derived truth** | **AT THE FLIP — neutral at spot; long gamma above 770, short below** | **LONG gamma, strongly pinned at 720** |

- **The `regime` field was NOT corrupted tonight** — SPY's "NEGATIVE" is consistent with spot sitting fractionally below the flip. The standing bug did not fire; what misled Phase A was reading the **sign of `total_gex`** as if it were the spot-relative gamma sign. It is not: `total_gex` sums the whole ladder regardless of where spot sits, and tonight **97% of SPY's positive gamma is above spot**. Phase A concluded "SPY POSITIVE, dealers net long gamma" from that — overstated. The spot-relative sign needs the **cumulative at spot**, which is +21.7M on an ±$880M ladder, i.e. **zero**.
- Phase B (`vol-book`) reached the right operational answer (stand aside on SPY) for the right structural reason (its own cumsum flip landed at ~770, ambiguously at spot), even while mis-describing the field as corrupt.
- **A second, separate discrepancy worth recording:** the header `total_gex` (+690.0M) is **not** the sum of the published per-strike ladder (+881.5M) — a $191M gap, presumably a truncation to 50 strikes / `dte_max` 45. **Neither header field reproduces the ladder; only the ladder is trustworthy.**
- **Operationally:** SPY pinned at 770 with dealers amplifying *below* it and damping above — an asymmetry, not calm. QQQ genuinely pinned at 720.

## Regression gate — OI_FADE is below baseline again; it is DATA, not code
`retro_harness.py --all`, 97 panel days (2026-03-13 → 08-27), 20/97 stand-down days:

| Lane | recorded baseline | tonight pooled | Δ |
|---|---|---|---|
| MOM_LONG | −0.0118 (n=1213) | −0.0111 (n=1270) | +0.0007 ✓ |
| MOM_SHORT | −0.0138 (n=830) | −0.0131 (n=868) | +0.0007 ✓ |
| **OI_FADE** | **+0.0013 (n=1177)** | **−0.0017 (n=1237)** | **−0.0030 ✗** |
| S2_dp_revert | +0.0018 (n=1269) | +0.0014 (n=1323) | −0.0004 |
| S4_pcr_fade | +0.0024 (n=1304) | +0.0023 (n=1364) | −0.0001 |

**Isolation check (`analyses/audit/2026-08-27/harness_split.py`):**

**(a) The baseline cohort reproduces.** Pinning `BASELINE_EDGE=2026-08-21` returns **MOM_LONG −0.0118/n=1213**, **OI_FADE +0.0013/n=1177**, **S4 +0.0024/n=1304** — bit-identical to the record. (MOM_SHORT n=828 vs 830 and S2 n=1264 vs 1269 — the known non-idempotent vendor feed, the same Yahoo-retraction class that un-resolved EQR; means move ≤0.0002.) **OI_FADE's baseline is fully intact — the pooled crossing is entirely new rows.**

**(b) No code changed tonight.** Lane logic and thresholds untouched; the panel grew by one day.

**(c) The increment is 4 exit-days with `base` PINNED, and it is ONE cohort.** Every lane's increment resolves on **08-24, 08-25, 08-26, 08-27** only. OI_FADE's increment is n=60, mean **−0.0602**, with per-day means of **−0.0633 / −0.0611 / −0.0607 / −0.0557** and **hit 0.33 on all four days** — that uniformity is the signature of one cohort resolving on four consecutive days, not 60 independent draws. The signal dates are 08-10/11/12/13 and the *same names recur on 3–4 of them* (NFLX, TSLA, PCG, AAPL, DKNG, SPCX, ACHR, META, AMZN). `base` is **pinned at 1.00 for OI_FADE on all four exit-days** — SPY was down in 100% of the new windows. **Note the shape again: the benchmark fell in every one of these windows and a short lane still lost 6%.**

**Verdict: NO REGRESSION. Do not re-baseline.** Re-pointing the reference onto four pinned-base exit-days would bake a single draw into it — the error the 08-22 cycle pre-registered against. This is the same cohort flagged on 08-24/25/26, now one day deeper. The lane has been advisory since 08-22; **nothing operational changes.**

## Lane detail

### Momentum (both legs watch-only, never size)
Spine: 6,284 → 3,666 (issue_type Common Stock/ADR, **2,618 ETPs cut at source**) → 3,066 (price ≥$5) → 1,466 ($-ADV ≥$50M) → **1,413** (no earnings in 10d).

- **MOM_SHORT — 22 names.** I Yahoo-verified the five nearest the low: **all five printed a genuine NEW 52-week low today** — TJX 134.22 (pct_range 0.1%), APTV 45.44 (0.4%), MCD 260.06 (0.3%), VICI 25.77 (0.2%), HDB 22.46 (0.1%). **No stale-`w52h` false shorts.**
- ⚠️ **I am correcting the lane's own table.** It printed closes *below* their 52w lows ("TJX 134.22 vs w52l 135.90") and MOM_LONG closes *above* their 52w highs ("OKTA 172.91 vs w52h 157.00, −10.13% off high"). That is not the stale-split artifact — **UW's `w52h`/`w52l` exclude the current session**, so every name that set a fresh extreme today reads as outside its own range. Yahoo confirms all ten I checked are genuine extremes. The classifications stand; the lane's *proximity ranking* and its sign labels do not.
- **MOM_LONG — 207 names.** ⚠️ **Earnings-gap contamination, and it is material.** **9 of 207 gapped ≥7% today**: OKTA **+28.63%**, CRWD +20.50%, FROG +12.10%, SLS +10.78%, TEAM +10.18%, FTNT +9.67%, NVDA +8.74%, FIVN +8.03%, ZETA +7.05%. These names entered the near-52w-high cohort *because of a print that already landed* — and `earnings_gate.py` is **forward-only**, so it passed every one of them (lane reported "earliest next print 09-09"). Meanwhile **the median MOM_LONG name was −0.07% today and only 47.3% of the basket closed green**: the leg's apparent strength is a handful of earnings gaps, not breadth. This is the lane with a **significantly negative** excess in tonight's regime (−2.57%, p=0.024).
- Deal-pinned watch (near-zero realized vol at the high — cut if a cash acquisition is announced): **APGE** (0.017%/day, 134.96 vs 134.99 high), ACA, CRNX.

### OI_FADE (advisory — never sizes)
1,341-name floored universe ranked by `oi_rel_build` + persistence (the live rule). Cuts: UHALB (partial 5-day window, fail-closed), **DKS** (persistence 0.986 — last night's strongest name, now a single-day block), IRD (0.912), FTEC (0.975 *and* an ETF), HONA (0.985, also IPO'd 06-16, under the listing-age floor), 7 on liquidity (**DYN $48.1M ADV — was "at the floor" at $50.8M last night, now below it**), ETH (an ETF, and `last_call_net` went negative).

| Ticker | rel_build rank | RAW `oi_net_5d` rank | persistence | catalyst split | gates |
|---|---|---|---|---|---|
| BZ | 6 (1.913) | **398** of 1,341 | 0.683 | 75.9% post-print (`>=`) / **62.7% strict (`>`)** — LIVE either way | pass; next ER 11-17 |
| FRT | 14 (1.461) | **417** of 1,341 | 0.390 | no catalyst in window | pass; next ER 10-30 |

- **Neither name sits in both rankings**, so **neither inherits the historical +0.0013 prior** (which grades top-15-by-RAW). They are graded only by the live rel_build rule, whose own forward measurement is **−0.81% (24 exit-days, p=0.080)**. Raw top-15 was again all ETPs/mega-caps (SPY, EWZ, SLV, IBIT, USO, TLT, VIX, INTC, BABA, NVDA…) — the QQQ-beta degenerate case, correctly excluded.
- ⚠️ **I am correcting the lane's characterisation of BZ as "organic, not single-block."** Its daily split is +632 / +464 / +802 / −93 / **+3,884** — **68.3% of the 5-day net landed in today's session alone**. It clears the 0.85 persistence cut on the number, but a build that is two-thirds one day old is not a persistent multi-day build, which is the premise the lane exists to fade. Treat as the weaker of the two.
- **FRT is the cleaner build** (+1,629 / +784 / +2,058 / +535 / +271, persistence 0.39) — but it is **decaying**: today's +271 is one-eighth of the 08-25 peak. A fading build is arguably the wrong end of the setup.
- Neither shows M&A/tender/scheme language on the news tape (the AZN rumor-gate gap).

### S4 PCR-fade (advisory) — **ETP gate clean tonight; I verified all 30 myself**
Gates: 6,284 spine → 1,466 base screen → **842 (call-volume floor ≥250 cut 624 names, 42.6%)** → 839 → 657 → 33 (PCR top-5%, p95=2.445) → **30** after the earnings gate cut BURL/HRL (report today) and LULU (09-03, inside the trading-day h5 window ending 09-04).

- **Last night three ETPs leaked (SPYM, XRT, LABD). That did not recur.** I queried `issue_type` directly for all 30: **25 Common Stock, 5 ADR (HSBC, INFY, SAP, STM, YPF), 0 ETFs.**
- **The call-volume floor holds:** minimum call_volume among survivors is **PAYC at 254**, then FOXA 289 and YPF 347. No NWG-class denominator artifacts.
- Slate by PCR: CAR 21.75, EIX 11.22, ECHO 10.59, YPF 8.68, MGM 7.51, PAYC 7.31, WMB 6.84, CPNG 6.74, URBN 6.21, INFY 6.10, HBAN 6.02, M 4.94, NLY 4.66, ISRG 4.36, KKR 4.35, WY 4.21, HSBC 4.04, CME 3.83, FOXA 3.17, RCL 2.97, HUT 2.92, DXCM 2.88, EXPE 2.84, BAX 2.62, SAP 2.60, QURE 2.59, WYNN 2.58, STM 2.56, CDNA 2.53, GH 2.44.
- ⚠️ Framing: S4's `hit − base` is **negative** (−0.028 baseline cohort, −0.016 pooled). This lane has **never had a hit-rate edge** — its excess is right-tail only. Not a high-probability setup.

### S2 dark-pool reversion (advisory)
98 Common-Stock names cleared DP ≥$10M + oneside ≥90%. Top-10 by DP premium; all 10 pass liquidity and the h5 trading-day earnings gate (window ends 09-04). ETP filter working — ~10 ETFs (GOVT, SSO, SPTM, QUAL, ACWI, IXUS, VBR, XNTK, ARKG) correctly absent from the top 30.

| Ticker | DP premium | oneside | buy-skew | side |
|---|---|---|---|---|
| BAC | $1,076.1M | 0.913 | −0.825 | SELL |
| C | $834.1M | 0.976 | +0.952 | BUY |
| CVX | $563.1M | 0.915 | +0.830 | BUY |
| TGT | $256.1M | 0.911 | +0.822 | BUY |
| EQIX | $253.4M | 0.942 | −0.883 | SELL |
| TER | $227.4M | 0.934 | +0.867 | BUY |
| CAI | $193.5M | 0.997 | −0.993 | SELL |
| MAR | $157.4M | 0.941 | −0.882 | SELL |
| MDLZ | $140.1M | 0.918 | −0.835 | SELL |
| ADP | $138.2M | 0.975 | +0.951 | BUY |

5 buy-skewed / 5 sell-skewed. The lane tilts **long on both**; the sell-side half (BAC, EQIX, CAI, MAR, MDLZ) is the weaker leg of that claim. Concentration magnitude has IC ≈ 0 — the ranking is a visibility filter, not conviction.

## Vol Book (non-directional, net-of-cost, advisory)
**0DTE-VRP — SPY STAND ASIDE; QQQ marginal at best.**
- **SPY: stand aside, fail-closed.** Spot sits *on* the zero-gamma flip (cumulative +21.7M ≈ zero); there is no sign to trade around and the two header fields disagree with the ladder.
- **QQQ: long gamma at spot, +601M wall at 720.** But `mean_pnl_by_vix_state` is **gross** and its LOW tercile is bounded `[15.8, 17.3]` — **tonight's VIX of 14.51 is BELOW the backtest's own low-tercile floor**, i.e. colder than anything in the 60-day sample. LOW-state gross +0.223% − 0.10% round-trip = **+0.12% net**, and that is an **upper bound on an out-of-sample vol regime**. Thin enough to skip.

**Earnings IV-crush — 2 advisory candidates, none sized.** Straddles hand-built on the expiry that **brackets** the print, median NBBO, not the CLI's `implied_move_perc`.

| Ticker | Print | Bracketing expiry | IV rank | Term structure | CLI `implied_move_perc` | **Hand ATM straddle** | Spread cost |
|---|---|---|---|---|---|---|---|
| **ZS** | 09-03 | **09-04 (8 DTE)** | 82.3 | backwardation 1.535 | **2.14% — WRONG EXPIRY** | **14.0% of spot** | 6.9% |
| NTAP | 09-02 | 09-18 (22 DTE, no weekly) | 98.1 | raw term backwardation 67.4→56.6% | 10.8% (understated) | 13.1% of spot | **14.8%** |

- **The bracketing-expiry trap fired hard on ZS and I verified it independently.** ZS's nearest expiry is **08-28 (1 DTE), which is BEFORE the 09-03 print** — the CLI's 2.14% is computed off a no-catalyst window. The correct 09-04 straddle: 187.5 call mid 13.21 + put mid 13.23 = **26.44 on a ~189 spot = 14.0%**, i.e. **~6.5× the CLI number**. Spread (0.78 + 1.05)/26.44 = **6.9%**, matching the lane.
- ⚠️ **ZS's bracketing expiry IS the NFP release date (09-04)** — the crush thesis is conflated with a Tier-1 macro print landing on expiry day. NTAP's 22-DTE bracket spans **both NFP and CPI (09-11)** if held to expiry.
- Per the TPR precedent (realized −16.5% vs a 12.2% raw-IV read), treat every implied move as a **wing FLOOR, not an estimate** — wings 1.3–1.5× the straddle.
- Dropped: **VSXY** (no live two-sided ATM put quote, 92 contracts name-wide; bracket 15 days past the print), **SPWH** (only a 141-DTE expiry exists — nothing brackets the print), **ZGN** (no IV data), **ZUMZ** (464.2% avg IV on 26 contracts — a quote artifact, not a market).

## Watch / Stood-down
- **OI_FADE (2):** FRT (cleaner build, but decaying), BZ (68% of the build is one day old). Neither inherits the RAW prior. **DKS**, last night's strongest name, cut tonight on persistence 0.986.
- **MOM_SHORT (22):** TJX, APTV, MCD, VICI, HDB + 17 — all watch-only by permanent policy; the five checked are genuine fresh 52w lows.
- **MOM_LONG (207):** basket/watch only; **significantly negative in CHOP** and contaminated by 9 post-earnings-gap entrants.
- **S4 (30):** CAR, EIX, ECHO, YPF, MGM, PAYC, WMB, CPNG, URBN, INFY + 20 — ETP-clean, right-tail only.
- **S2 (top 10 of 98):** BAC, C, CVX, TGT, EQIX, TER, CAI, MAR, MDLZ, ADP.
- **Cross-lane overlap: CDNA** appears in both MOM_LONG (pct_range 96.8%) and S4 (PCR 2.53). Noted as **evidence-type diversification only — never summed** (invariant #2). It sizes nothing either way.

## Risk
- **Correlation clusters:** none to collapse — nothing is sized. Standing note: OI_FADE's mega-cap/speculative cluster (NFLX, TSLA, AAPL, PCG, DKNG, ACHR, SPCX) is what produced the −6% increment across four exit-days; it is **one theme resolving repeatedly**, not 60 independent names.
- **Event calendar:** Jackson Hole **08-27→29** (Warsh keynote 08-28) · **Aug NFP 09-04** (Tier-1 — *and the ZS straddle's expiry date*) · Labor Day 09-07 · PPI 09-10 · **CPI 09-11**, one trading day past the h10 window · FOMC 09-15/16 · Core PCE 09-30.
- **Tail caps:** not applicable — no position.
- **Hedge note:** SPY pinned on its flip means dealers **damp above 770 and amplify below it** — a downside-asymmetric pin, not calm. With VIX at 14.51 and below the backtest's own low-tercile floor, long premium remains structurally favoured over short premium.
- **`s1_standdown` is a double near-miss** (ret5 1.11% vs 1.5%; dd15 −1.96% vs −2%). Re-check tomorrow — a modestly stronger thrust flips the regime cell to CHOP/REBOUND-THRUST, where **OI_FADE's sign inverts to +0.0098**.
- **Data hygiene:** truth-set parquets rebuilt tonight to reach 2026-08-27 (preflight clear, 5/5 panel groups). 27 tickers unpriced by the Yahoo fetch — failed closed downstream. Screener `prev_close` verified against Yahoo on SPY/QQQ/IWM to the basis point.

## Envelope note
`decision.json` validates against `schemas/decision_envelope.v2.schema.json`. Its `lane_status[]` enum admits only the three sizing-capable lanes (MOM_SHORT / MOM_LONG / OI_FADE), so **S2 and S4 are documented in this report only** — the same convention as the 08-26 envelope. `calls[]` is empty.
