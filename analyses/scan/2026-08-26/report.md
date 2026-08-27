# Market Scan — 2026-08-26

## Regime & Verdict
- **Regime: CHOP** · ret5 −0.390% · ret10 −0.830% · dd15 −1.280% (trough-anchor distance, *not* drawdown-from-highs)
- **Vol-state:** VIX **15.21** (from 15.45) — LOW tercile, falling. SPY realized(30d) 12.30%. SPY VRP +0.0038 (fair); QQQ VRP −0.0279 (IV30d 18.88% *below* realized 21.66%).
- **Dealer gamma (hand-derived; the CLI `regime` field is corrupted):** **SPY SHORT gamma at the money** — cumulative net-GEX ≈ **−$964M** at spot 766.71, the 742–791 band never crosses zero. Header `zero_gamma_level` 364.22 is structurally impossible → discarded. **QQQ SHORT at spot** (−$225.8M at 711.9), flipping positive ~+0.6% above. A *fragile-quiet* tape: low VIX, short gamma.
- **Breadth:** 927 adv / 939 dec, **48.97% green** on the 2,428-name spine; 50.5% > 20dma, 56.0% > 50dma. SPY +0.02%. Flow bullish_pct 34.7%. Breadth matches the flat tape — **no distribution tell tonight** (it *did* fire on 08-25).
- `directional_tradable` = **true** (cohorts exist in all four lanes) · `s1_standdown` = **false**
- **Bottom line: NO DIRECTIONAL EDGE. Zero sized calls — a 13th consecutive flat session.** Not one lane has a positive, significant excess in tonight's regime cell.

## Directional Book (excess-scored)
**Empty — zero sized calls.** No lane in this repo sizes at all since OI_FADE's 2026-08-22 demotion to advisory. **Phase D (`risk-sizer`) was vacuous and `fundamentals-gate` was correctly not spawned** — it runs only on names about to be sized.

### Phase C — the applicable regime cell, exit-day-clustered
Tonight is **plain CHOP with `s1_standdown=FALSE`**. The pooled "CHOP" row must **not** be used: it collapses plain CHOP with CHOP/REBOUND-THRUST, and **OI_FADE's sign flips between them** (−0.0010 plain vs +0.0098 thrust; collapsed reads a misleading +0.0023). The correct cell, with `t` clustered on **exit-days**, not rows:

| Lane | n rows | exit-days | mean excess | t (exit-day) | p | verdict |
|---|---|---|---|---|---|---|
| MOM_LONG | 356 | 24 | **−0.0256** | −2.41 | **0.016** | significantly NEGATIVE |
| MOM_SHORT | 282 | 24 | −0.0177 | −1.93 | 0.054 | negative |
| OI_FADE | 344 | 23 | −0.0009 | −0.13 | 0.898 | indistinguishable from zero |
| S2_dp_revert | 380 | 26 | +0.0014 | +0.31 | 0.755 | indistinguishable from zero |
| S4_pcr_fade | 387 | 26 | +0.0068 | +1.39 | 0.165 | not significant |

**Every cell carries the correlated-draw caveat** (all exit-day counts < 30, invariant #6). The only statistically real number in the table is **MOM_LONG's negative excess in CHOP** — an argument *against* the near-52w-high basket tonight, not for anything. Score = `validated_excess × regime_fit` = **0 or negative for every candidate**; nothing reaches a sizing band.

## Regression gate — OI_FADE is below baseline and negative; it is DATA, not code
`retro_harness.py --all`, 96 panel days (2026-03-13 → 08-26), 20/96 stand-down days:

| Lane | recorded baseline | tonight pooled | Δ |
|---|---|---|---|
| MOM_LONG | −0.0118 (n=1213) | −0.0113 (n=1256) | +0.0005 ✓ |
| MOM_SHORT | −0.0138 (n=830) | −0.0133 (n=860) | +0.0005 ✓ |
| **OI_FADE** | **+0.0013 (n=1177)** | **−0.0011 (n=1222)** | **−0.0024 ✗** |
| S2_dp_revert | +0.0018 (n=1269) | +0.0015 (n=1308) | −0.0003 |
| S4_pcr_fade | +0.0024 (n=1304) | +0.0023 (n=1349) | −0.0001 |

**Isolation check (`analyses/audit/2026-08-26/harness_split.py`):**

**(a) The baseline cohort reproduces.** Pinning `BASELINE_EDGE=2026-08-21` returns **MOM_LONG −0.0118/n=1213**, **OI_FADE +0.0013/n=1177**, **S4 +0.0024/n=1304** — bit-identical to the record. (MOM_SHORT reads n=828 vs 830 and S2 n=1264 vs 1269 — 7 rows lost to the known non-idempotent vendor feed, the same Yahoo-retraction class that un-resolved EQR. Means move ≤0.0002; immaterial.) **OI_FADE's baseline is fully intact — the pooled crossing is entirely new rows.**

**(b) No code changed tonight.** Lane logic and thresholds are untouched; only the panel grew by one day.

**(c) The increment is 3 exit-days with `base` PINNED.** Every lane's increment resolves on just **08-24, 08-25, 08-26**, and `base` is pinned on all three — **1.00 for both short lanes, 0.00 for all three long lanes**, i.e. **SPY was down in 100% of the new windows**. OI_FADE's increment is n=45, mean **−0.0617**, and near-identical on each day (−0.0633 / −0.0611 / −0.0607, hit 0.33 on all three). That uniformity is the signature of **one cohort resolving on three consecutive days, not three independent draws** — signal dates 08-10/11/12 on the *same names*. The left tail is entirely the crypto/speculative squeeze already documented on 08-25: MSTR −30.7%, CELH −30.0%/−28.4%/−26.4%, MSTR −27.2%, MARA −22.8%/−18.2%/−17.2%. Its mega-cap shorts (META, AMZN, NVDA) again supplied the only gains. Note the shape: **the benchmark fell in every one of these windows and a short lane still lost 6%.**

**Verdict: NO REGRESSION. Do not re-baseline.** Re-pointing the reference onto three pinned-base exit-days would bake a single draw into it — exactly the error the 08-22 cycle pre-registered against. OI_FADE's pooled figure is now negative, but that is the arithmetic of one squeeze, not decay. The lane was already advisory since 08-22; **nothing operational changes.**

## Lane detail

### OI_FADE (advisory — never sizes)
1,364 names cleared the floors. Ranked by `oi_rel_build` + persistence (the live rule). Three survivors after liquidity/ETP/earnings/catalyst/M&A gates:

| Ticker | rel_build rank | RAW `oi_net_5d` rank | persistence | catalyst split (strict `>`) | gates |
|---|---|---|---|---|---|
| DKS | **1** (4.687) | 67 | 0.765 | **73.9% post-print** — LIVE_BUILD | all pass; next ER 11-24 |
| DYN | 6 (2.011) | 535 | 0.601 | no catalyst in window | pass; ADV $50.8M — *at* the floor |
| FRT | 13 (1.403) | 443 | 0.411 | no catalyst in window | pass; next ER 10-30 |

- **No name sits in BOTH rankings tonight**, so **none inherits the historical top-15-by-RAW prior**. They are graded only by the live rel_build rule, whose own forward measurement is **−0.81% (24 exit-days, p=0.080)** — a negative point estimate.
- **DKS** is the cleanest mechanical read: rank-1 rel_build, calls building *into* a falling tape (52-week-low headlines, Nike fallout, Truist downgrade) — the crowded-contrarian-long setup the lane exists to fade. The build **survives a strict `>` recompute** (73.9% post-print vs the script's `>=` 84.2%), so it is not a pre-print artifact. Still watch-only.
- **ASST** (last night's only ESTABLISHED name) has **fallen out of both rankings** — raw #25, rel #60 on tonight's full floored universe. Not a cut for cause; its rel_build compressed to 0.698. Standing crypto-beta caution retained.
- Raw top-15 was, as usual, all ETPs/mega-caps (EWZ, SPY, IBIT, SLV, USO, VIX, TLT, GLD, BABA, INTC…) — the QQQ-beta-short degenerate case, correctly excluded from selection.

### Momentum (both legs watch-only, never size)
- **MOM_SHORT — 10 names:** CRUS, FRVO, TJX, TTD, TLN, LII, WING, MLM, CMS, STLA. **I independently Yahoo-verified six** (chart API): CRUS 0.7% off its low, TJX 2.7%, TTD 0.5%, STLA 1.4%, FRVO 0.8%, TLN 3.2% — all genuine near-lows, **no stale-`w52h` false shorts**. (Lane's low for TJX read $134.75 vs Yahoo $135.90 and FRVO $15.31 vs $15.22 — small drift, classification unaffected.) 70 ETPs cut at source via `issue_type`.
- **MOM_LONG — 13 names:** WT, RVTY, AXGN, VCTR, NTRA, BNS, EXPD, APGE, IVZ, DBRG, REPL, IQV, DGX. **Basket/watch only.** Note this leg is the one lane with a *significantly negative* excess in tonight's regime (−2.56%, p=0.016).
- Minor: the lane reported "CUT (7 names)" for MOM_LONG but listed only 6 (SRRK, CRNX, V, TECH, FBRX, CDNA). Cosmetic; no candidate is affected.

### S4 PCR-fade (advisory) — **ETP leak found and corrected**
The lane shipped an 11-name slate claiming its ETP gate cut only EWJ/RSP/XLY. **Three ETPs remained in it.** I checked `issue_type` on the screener directly:

- **SPYM → ETF**, **XRT → ETF**, **LABD → ETF** (Direxion Daily S&P Biotech Bear 3X — a **leveraged inverse**, the exact SOXS artifact class).
- **Corrected slate = 8 names:** BX (PCR 11.65), GLXY (11.01), TNGX (9.65), WRBY (9.06), STNG (7.57), WBD (6.25), BHF (6.03), TEL (4.86).
- The call-volume floor **is** working: it cut 78 of 95 pre-gate names (82%) as manufactured PCRs — e.g. EMB (PCR 682 on 4 calls), BKD (267 on 2). Every surviving name has call_volume ≥ 264.
- Two lane block-reasons were misread and are corrected here: **BLDR**'s prior verdict (weekly W31) stands it down by **standing policy invariant #6**, and explicitly records `s1_standdown=FALSE` — the lane attributed the block to the crash guard, which is not firing tonight. **CARR**'s "blocking verdict" is just the standard *"S4 advisory-only, never sizes"* lane-status tag from 08-21, not a name-specific veto. Both stay out regardless; only the reasoning changes.
- ⚠️ Framing: S4's `hit − base` is **negative** (−0.010 pooled, −0.028 baseline cohort). This lane has **never had a hit-rate edge** — its excess is right-tail only.

### S2 dark-pool reversion (advisory)
82 names cleared the gates from a ~468-name `dp_oneside ≥ 0.8` cohort — **too broad to be a useful watch list**; treated as diary. Top by DP premium, which I recomputed independently and which matches the lane: **PEP** ($677M, oneside 0.965, buy-skew **+**0.931), **TER** ($391M, 0.962, **−**0.924), **DIS** ($378M, 0.946, **+**0.891), **TPR** ($352M, 0.987, **−**0.975), **ADI** ($247M, 0.929, **−**0.859). The lane **did** cut ETPs correctly — GOVT is #1 by premium ($2,191M) and is properly absent, as are XLF and EWT. Earnings gate blocked 5 names reporting 08-27 (BIPC, CM, PURR, RY, TD); liquidity blocked 9. Note the lane tilts **long on both** buy- and sell-side concentration; the sell-side names (TER, TPR, ADI, LOW, HDB) are the weaker half of that claim.

## Vol Book (non-directional, net-of-cost, advisory)
**0DTE-VRP — STAND ASIDE on both SPY and QQQ.**
- **Trap #1 fired on SPY tonight.** `zerodte_setup.py` reported `dealer_gamma_regime: "LONG"` with `zero_gamma_level: 364.19` and recommended `sell_premium=True` — reading the **same corrupted CLI field**, with a flip level far below a spot of 766.71. Hand-derived truth: **SPY is SHORT gamma at the money.** The recommendation is **overridden, fail-closed.**
- QQQ's script read (`SHORT`, `sell_premium=False`) agrees with the hand derivation; already standing aside.
- **Trap #2 (VIX-tercile pooling) corrected:** `mean_pnl_by_vix_state` is **gross**. Tonight's LOW bucket: SPY +0.132%/day gross → **+0.032% net** of the 0.10% round-trip; QQQ +0.233% → **+0.133% net**. Both are moot — the gamma sign fails closed first. Selling premium into a short-gamma tape at a low, falling VIX is the setup the validation sample never priced.

**Earnings IV-crush — 3 advisory candidates, none sized.** Straddles built on the expiry that **brackets** the print, median (not mean) near-ATM IV:

| Ticker | Print | Bracketing expiry | IV rank | Term structure | Implied move | Note |
|---|---|---|---|---|---|---|
| BURL | 08-27 | 08-28 (1 DTE) | 88.4 | backwardation **3.01×** | **9.11%** | ~9% half-spread on the straddle — very wide |
| ADSK | 08-27 | 08-28 (1 DTE) | 80.7 | backwardation 1.56× | **8.50%** | tighter than BURL, still ~$0.90–1.60/leg |
| MDB | 09-01 | 09-04 (8 DTE) | 81.7 | backwardation 1.13× (weakest) | **15.98%** | history of double-digit earnings gaps |

Per the TPR precedent (realized −16.5% vs a 12.2% raw-IV read), **treat these as wing FLOORS, not estimates** — wings ≥1.3–1.5× the straddle read. Dropped: NTAP, MNSO (**no expiry brackets the print** — nearest is 22+ DTE, so any implied-move read is not an earnings bracket); SPWH, YRD (illiquid, no computable straddle). Spread cost of 6–9% of straddle notional eats most of the crush edge before the tail is even considered.

## Watch / Stood-down
- **OI_FADE:** DKS (strongest), DYN, FRT — watch only, none inheriting the RAW prior. ASST dropped off both rankings.
- **MOM_SHORT (10):** CRUS, FRVO, TJX, TTD, TLN, LII, WING, MLM, CMS, STLA — watch-only by permanent policy.
- **MOM_LONG (13):** WT, RVTY, AXGN, VCTR, NTRA, BNS, EXPD, APGE, IVZ, DBRG, REPL, IQV, DGX — basket/watch; significantly negative in CHOP.
- **S4 (8, ETP-corrected):** BX, GLXY, TNGX, WRBY, STNG, WBD, BHF, TEL.
- **S2 (top 5 of 82):** PEP, TER, DIS, TPR, ADI.
- **Cross-lane overlap: none.** No name appears in two lanes tonight, so no confluence question arises. (Had one, it would be noted as evidence-type diversification and never summed.)

## Risk
- **Correlation clusters:** none to collapse — nothing is sized. Standing note: OI_FADE's crypto-beta cluster (ASST/BTCZ/ETH class) is what produced the −6% increment; it is a single theme, not n independent names.
- **Event calendar:** Jackson Hole **08-27→29** (Warsh keynote 08-28) · **Aug NFP 09-04** (Tier-1) · Labor Day 09-07 · PPI 09-10 · **CPI 09-11**, one trading day past the h10 window — carry it into next cycle, and it bites any straddle bracketing it. FOMC 09-15/16.
- **Tail caps:** not applicable — no position.
- **Hedge note:** both index names short gamma at the money with VIX at 15.21 and falling. Low VIX here is *fragility*, not calm: dealers amplify rather than dampen. Any long premium is structurally favoured over short premium tonight.
- **Data hygiene:** truth-set parquets rebuilt tonight to reach 2026-08-26 (preflight clear, 5/5 panel groups). 27 tickers unpriced by the Yahoo fetch — failed closed downstream.
