# Market Scan — 2026-08-24

## Regime & Verdict
- **Regime: CHOP** · ret5 −1.190% · ret10 −1.240% · dd15 −1.350% (`regime_check.py`, truth set rebuilt tonight to 2026-08-24; preflight CLEAR on all five panel groups). Live-Yahoo SPY closes reproduce ret5/ret10 to 3dp — no arbitration needed.
- **Vol-state:** VIX **15.85** (+0.72 pts, +4.76%) → **LOW tercile by 0.05** (actual bounds `[15.9, 17.3]`). This is the third consecutive night the VIX has printed within 0.05–0.01 of its own tercile boundary; do not read "LOW" as comfortably low. **Both SPY and QQQ are SHORT gamma** (SPY `total_gex` −1.284B, empirical flip ≈765.5 vs spot 763.70; QQQ −548M, flip ≈712.5 vs spot 706.72). DEX net-negative on both — public put-heavy, dealer hedge pro-cyclical.
- **Breadth:** 304 advancers / 196 decliners, **60.4% green**, but options-flow `bullish_pct` **34.6%** (2,183 bullish vs 4,118 bearish) — a ~26pt gap, with Technology the dominant sector outflow (−$346M). The literal "green tape + pct_green<50" distribution tell does **not** fire; read as a hedging undertone, not a signal.
- `directional_tradable` **TRUE** · `s1_standdown` **FALSE**
- **Bottom line: No actionable directional edge today. Book stays FLAT for an 11th consecutive session.**

**The binding reason is measurement.** Tonight's cell is **plain CHOP** (`s1_standdown` FALSE), and no lane clears the +0.3% starter floor on it:

| Lane (plain-CHOP, 94-day panel) | n | mean excess | **exit-days** | clustered mean | **t (exit-day clustered)** | Band |
|---|---|---|---|---|---|---|
| MOM_LONG | 356 | −0.0257 | 24 | −0.0256 | **−2.41** | below floor → watch |
| MOM_SHORT | 282 | −0.0220 | 24 | −0.0177 | −1.93 | below floor → watch |
| OI_FADE | 344 | **−0.0010** | 23 | −0.0009 | −0.13 | below floor → watch |
| S2_dp_revert | 352 | +0.0014 | 24 | +0.0014 | 0.29 | advisory → watch |
| S4_pcr_fade | 357 | +0.0081 | 24 | +0.0080 | **1.52** | advisory lane → watch regardless |

### Two corrections to how this table was read last night
1. **The CHOP cell must exclude the crash-guard suffix.** Last night's table folded `CHOP/REBOUND-THRUST` rows into "CHOP". Tonight is plain CHOP, and the two strata disagree materially — **OI_FADE reads −0.0010 on plain CHOP but +0.0098 on CHOP/REBOUND-THRUST** (n=148, 10 exit-days). Conditioning on the wrong one flips OI_FADE's sign. MOM_SHORT is unaffected by construction (it never fires during a stand-down), which is what confirms the diagnosis: its n is identical (282) under both groupings while every other lane's n moves ~40%.
2. **S4's CHOP cell is not t=2.38.** That figure was row-level. Clustered on the **exit-day** — the unit CLAUDE.md mandates — the same +0.0081 carries **t=1.52 across 24 exit-days**. Under 30 exit-days it also carries the standing correlated-draw caveat and cannot graduate on this evidence. S4's `hit − base` remains **negative (−0.021 pooled)**: no hit-rate edge, right tail only. It is advisory-only and does not size.

## Directional Book (excess-scored)
**Empty — zero sized calls.** No candidate reached a sizing band; Phase D produced no sized output. Consistent with the standing state: **no lane in this repo sizes at all** since OI_FADE's 2026-08-22 demotion.

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — |

## Regression gate — two lanes below baseline, and it is DATA, not code
`retro_harness.py --all` (94 panel days) vs the recorded baseline:

| Lane | Baseline (93d, adopted 08-22) | Tonight (94d) | Δ |
|---|---|---|---|
| MOM_LONG | −0.0118 (n=1213) | −0.0117 (n=1228) | +0.0001 ✓ |
| MOM_SHORT | −0.0138 (n=830) | −0.0137 (n=839) | +0.0001 ✓ |
| OI_FADE | +0.0013 (n=1177) | **+0.0004 (n=1192)** | **−0.0009 ✗** |
| S2_dp_revert | +0.0018 (n=1269) | **+0.0015 (n=1283)** | **−0.0003 ✗** |
| S4_pcr_fade | +0.0024 (n=1304) | +0.0025 (n=1319) | +0.0001 ✓ |

No lane or threshold code changed tonight, so the isolation check was run before reading either drop as a regression. **Both resolve cleanly:**

**(a) The baseline cohort reproduces.** Re-running the 08-22 audit's own `harness_split.py` with `BASELINE_EDGE` re-pointed to 2026-08-21 returns the recorded figures **bit-identically for four of five lanes** — MOM_LONG −0.0118/1213, MOM_SHORT −0.0138/830, **OI_FADE +0.0013/1177**, S4 +0.0024/1304. OI_FADE's baseline is intact; its pooled drop is entirely new rows.

**(b) S2's one-row shortfall is a vendor retraction, not code.** S2's baseline came back n=**1268** against a recorded 1269. The missing row is **LBRDK 2026-07-23** (h5, excess **+0.1181** — a large winner). `prices.parquet` now has LBRDK bars stopping **2026-07-17** and not resuming until 2026-08-21, so that window no longer resolves. Removing exactly that row from the 08-22 audit's stored rows gives **+0.001660** against tonight's **+0.001641** — agreement to float noise (49 rows differ, all at the 1e-9…1e-6 level, from the Yahoo refetch). This is the **second instance of the documented EQR non-idempotency class**: realized excess re-derived from the live vendor feed is not reproducible unless the ledger restores it.

**(c) The increment is ONE exit-day, with `base` pinned.** Every lane's increment has **exit-days = 1**: entry **2026-08-10**, exit **2026-08-24**, 15 rows each (9 for MOM_SHORT). `base` is pinned — **1.00 for the short lanes, 0.00 for the long lanes** — i.e. **SPY was down in 100% of the new windows** (−1.24% over 08-10→08-24). These are not 15 independent observations; they are one draw.

OI_FADE's increment mean is **−0.0633**, and its composition says exactly what happened: a speculative rally ran *against* a falling index. Over that window **CELH +28.7%, MSTR +26.0%, MARA +17.0%** (the lane was short all three), while the mega-caps it was also short — **META −6.0%, AMZN −5.8%, NVDA −4.2%** — supplied its only gains. Fading crowded call-OI is structurally short exactly the complex that squeezed.

**Verdict: no regression. Do not re-baseline** — re-pointing the reference onto a single pinned-base exit-day would bake one draw into it, the error the 08-22 cycle pre-registered against.

## Vol Book (non-directional)
Both sleeves **STAND ASIDE**. Zero directional points, delta-neutral, quoted net-of-cost.

- **0DTE-VRP — SPY:** LOW-tercile conditional gross +0.113%/day → **+0.013%/day net** of the 0.10% round-trip, which is inside noise. Moot regardless: dealers are **SHORT gamma**, a hard stand-aside. `sell_premium=false`.
- **0DTE-VRP — QQQ:** LOW-tercile gross +0.207% → **+0.107%/day net**, genuinely positive, but **overridden by the same short-gamma gate**. `sell_premium=false`. The gate, not the economics, is binding on both.
- **Earnings IV-crush — ADSK, HPQ, OKTA: ADVISORY_NOT_SIZED.** Straddles recomputed off the raw parquet on the correctly bracketing **2026-08-28** expiry using median IV (not the CLI mean): **ADSK ≈10.93%, HPQ ≈12.02%, OKTA ≈16.05%** — all **lower bounds**, so wings sized at floor×1.35 (≈15% / 16% / 22%). Not sized because that single expiry stacks **PCE + NVDA (08-26), Jackson Hole (08-27→29), the Warsh keynote landing on expiry day itself (08-28), and the payrolls benchmark revision (08-28)** on top of the idiosyncratic earnings binary — the unsampled-left-tail cap stays unsatisfiable. This was re-derived from tonight's term structure, not inherited from 08-21. NVDA is excluded on its own merits (`iv_rank` 42.7, fails the ≥80 screen). RY, CM, A, QFIN, DCI, EH, TRMD excluded — nearest listed expiry 25+ DTE, so no contract brackets their print.

## Watch / Stood-down
- **OI_FADE — NO_NAME_CLEARED, 15 advisory candidates:** DK, ULS, VIK, NXPI, FRT, VIRT, SAN, CBRS, PTEN, FN, VIAV, WSC, CAKE, ACMR, BIDU. **Overlap with the raw `oi_net_5d` top-15 is ZERO tonight** (population 1,313), so the standing ranking gap is total again and **every candidate's `validated_excess` is UNESTABLISHED** — none can inherit the +0.0013 prior. No `last_call_net` invalidation fired; `catalyst_split` produced **no boundary-driven sign flip** (all five in-window builds stay LIVE_BUILD under the strict `>` convention). Sector spread is healthy (Technology 5/15 at the ⅓ cap; median mcap ≈$10B).
  - **AS re-entry FAILS and stays cut** — leg 1 clears (`last_call_net` +436) and fundamentals now look favorable (4/4 beat streak, raised FY guide), but **leg 2 fails outright: raw rank 38 of 1,313**, nowhere near top-15.
  - **BIDU is the name to watch** — raw rank **16 of 1,313**, one place outside, the same way AS crossed on 08-20.
- **The measured population is itself the argument against the prior.** Tonight's raw top-15 — META, AMZN, TSLA, BABA, INTC, WMT, SPCX + the crypto complex (WULF, CIFR, MARA, SBET) — is mega-cap/crypto beta (median mcap ≈$47B vs ≈$10B for the live rule). That is the population the +0.0013 was measured on, and it is the same complex that produced tonight's −6.33% increment.
- **MOM_SHORT — BASKET_WATCH, 15 candidates, all Yahoo-verified genuine:** FRVO, BWXT, FDXF, OLN, LII, NRG, ONON, LHX, APP, CMS, CPRI, JBTM, PEG, TLN, CRUS. **13 of 15 made a fresh 52-week low ON 2026-08-24** (pct_range 0.1–4.2%) while SPY fell only 0.29% — no false shorts from the `pct_52w_range` corruption tonight. `issue_type` cut **2,624 ETPs** at source. Notable cluster: **4 of 15 are power/utility names (NRG, PEG, CMS, TLN)** — the AI-datacenter-power complex breaking down together. Never sizes.
- **MOM_LONG — BASKET_WATCH.** 233 raw near-52w-high names; canonical top-15 TGT, V, VMRK, SOLV, WEX, WT, ILMN, EXPE, SCHW, SEIC, MTCH, SXT, FCX, SSRM, ABNB. Worst cell in the table (−2.57%, t=−2.41). Never sizes.
- **S2 — 14 advisory names** (rebuilt by the orchestrator; see defect below): COF, BSX, RTX, SCHW, BLK, MNST, GRMN, PNC, CI, REGN, TKO, CVS, PSX, ICE. TWO cut on liquidity ($-ADV $40.8M < $50M); 15/15 cleared the h5 earnings gate. Ranking treated as **non-informative** (`dp_oneside` is a binary timing tag, IC ≈ 0). Heavy financials cluster (COF, SCHW, BLK, PNC, ICE) — one theme, not five names. Never sizes.
- **S4 — 15 advisory names:** XEL, TSEM, FLEX, INFY, MDLN, HSBC, EMBJ, TXT, LNC, MCK, WPM, FROG, BBIO, CNK, OMF. Call-volume floor **verified biting** — cohort minimum `call_volume` **263** (MCK) against the 250 threshold, with 73 names rejected below it including the artifact class this floor exists for (CHE: PCR 314.9 on 8 calls; FBND: PCR 250 on 2 calls). Never sizes.

## Risk
- **Correlation clusters:** power/utilities 4-of-15 in MOM_SHORT; financials 5-of-14 in S2; crypto 4-of-15 in the OI_FADE *measured* population. Nothing is sized, so no cluster collapse was needed — but the OI_FADE cluster is the one that just cost the lane 6.33% on a single exit-day.
- **Event calendar (next 10 sessions):** PCE **08-26**, NVDA earnings **08-26**, Jackson Hole **08-27→29**, Warsh keynote **08-28**, payrolls benchmark revision **08-28**, NFP **09-04**, Labor Day **09-07** (closed). No CPI/PPI/FOMC in window.
- **Tail caps:** short-gamma on both indices is a trend-acceleration regime — it is why both 0DTE sleeves stand aside rather than sell a positive-net-expectancy QQQ premium.
- **Hedge note:** book is flat; nothing to hedge.

## Findings recorded tonight
1. **The GEX corruption has escalated from `zero_gamma_level` to the `regime` field, and it has moved from QQQ to SPY.** Verified directly three times tonight: SPY `total_gex` **−1,284,006,949** (negative) while the CLI's own `regime` field reads **"POSITIVE"**, with `zero_gamma_level` **336.67** against spot **763.70** (~56% below). The strikes bracketing spot are decisively negative (764: −314.7M, 765: −226.1M, 760: −250.4M). **This matters because `zerodte_setup.py` trusts the `regime` field as its arbiter** (`cli_gamma_regime()`) — it therefore emitted `sell_premium=true`, `size_scalar=0.5` and framed SPY as "long-gamma: quieter, mean-reverting" tonight, i.e. it recommended selling premium into a short-gamma tape. QQQ escaped only by accident: its label was `"FULLY_NEGATIVE"`, which fails to parse as `"POSITIVE"`/`"NEGATIVE"` and fell through to the local flip. **Third consecutive night requiring a manual override.** Recommended fix: an internal-consistency guard rejecting the CLI as arbiter whenever `sign(regime) != sign(total_gex)` or `|zero_gamma_level − spot| / spot > 0.25`, falling back to the per-strike derivation.
2. **Second instance of the EQR non-idempotency class — LBRDK.** A row that resolved at the 08-22 audit is un-resolvable tonight because the vendor's bar history for LBRDK now gaps 2026-07-17 → 2026-08-21. It cost the S2 baseline one row and 2bp. Reinforces that `resolved_ledger.py`, not a re-derivation, is the durable record.
3. **The plain-CHOP vs CHOP/REBOUND-THRUST distinction is load-bearing and was being collapsed.** OI_FADE's sign flips between the two strata (−0.0010 vs +0.0098). Any regime-conditional prior quoted going forward must state which stratum it is on.
4. **Exit-day clustering materially changes S4's headline.** Last night's "only positive-and-above-floor cell, t=2.38" is **t=1.52 on 24 exit-days** once clustered on the mandated unit. Worth carrying into the 08-29 audit as a check on how the lane×regime table is computed, not just what it says.

## Lane-reliability findings (three of five lanes returned claims that did not survive verification)
Recorded because the orchestrator's re-verification is what caught them, and because two of the three would have changed the written record.

1. **S2 lane was materially wrong and its output was discarded and rebuilt.** It reported 25 raw candidates → 4 survivors (CCO, TBBB, RIGL, BTE) → **0** after the liquidity floor, and concluded the lane was empty. Ground truth, reproduced from `retro_harness.py`'s own S2 block: **105 names clear the full canonical filter** tonight, and the top-15 by DP premium are large, liquid names (COF, BSX, RTX, SCHW, BLK …) of which **14 pass the liquidity floor comfortably**. The lane's four names are micro/illiquid names that do not appear anywhere in the canonical ranking. The correct advisory list above was built by the orchestrator.
   - Related and worth a decision at the audit: **the harness's S2 rule applies no liquidity floor at all**, while the live book requires price ≥$5 and $-ADV ≥$50M. So the S2 prior grades a population that includes names the book could never trade — the same measurement-vs-live gap already catalogued for OI_FADE's ranking.
2. **S4 lane over-claimed blocking priors on three names; all three were restored.** It cut XEL, INFY and SWK as "blocking". Verified: **XEL**'s hits are its own advisory appearances on 08-18 (an S2 one-sided DP tag and an S4 leader entry), explicitly recorded as tags, not vetoes. **SWK**'s are an S2 advisory candidate list and a MOM_LONG basket mention — and SWK is not in the canonical top-15 regardless. **INFY**'s is a genuine flag but a **stale** one: a 2026-08-03 OI_FADE `long_caution`, and INFY is **net put-building tonight** (`net_5d` −2,092, call +14,504 / put +16,596, `rel_build` −0.014), so it is not a crowded-call name any more. The lane's stated rationales ("mechanism persistence >0.85", "failed 5× consecutive zero-starter sessions") were OI_FADE-flavored reasoning applied to an S4 name.
3. **Momentum lane's gate claim was false.** It reported "17 candidates … no VETO/EXCLUDED blocks". `prior_verdicts.py` flags prior blocking verdicts on **APP, FRVO, PEG, NRG and CMS**. Disposition is unchanged (MOM_SHORT never sizes), but the claim did not hold. Its 52-week verification *did* hold: all 15 canonical names Yahoo-verified as genuine, which is the leg that actually protects this lane.
