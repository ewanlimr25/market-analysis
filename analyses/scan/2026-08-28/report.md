# Market Scan — 2026-08-28

## Regime & Verdict
- **Regime: CHOP** · ret5 **+0.470%** · ret10 **−0.900%** · dd15 **−1.770%** (trough-anchor distance, *not* a drawdown-from-highs)
- **Vol-state:** VIX **14.43**, −0.55% on the day and **−4.63% over 5 sessions** — a 10-day low. SPY VRP **−0.27pp** (IV30d 11.63% vs realized30d 11.90%) — **FAIR, no premium-selling edge from VRP alone.**
- **Dealer gamma FLIPPED tonight: SPY and QQQ are now BOTH net SHORT gamma at spot.** Last night SPY sat *on* its flip (cumulative +21.7M) and QQQ was cleanly long-gamma and pinned (+736.7M). Tonight SPY's cumulative net-GEX up to spot is **−615.8M** (crossing ~789.6 vs spot 769.30) and QQQ's is **−218.9M**, single-signed negative across the whole sampled ladder. Vol-state only — never a direction.
- **Breadth: broad and red, and NOT last night's divergence.** Full 5,935-name spine **31.47% green**, median **−0.463%**; top-500 by market cap 38.00% green, median −0.281%; top-2000 33.15%, median −0.376%. SPY **−0.227%**, QQQ **−0.649%**, IWM **−1.354%**. Index and breadth agree this time — but the median stock fell about **2× SPY's own move** and small-caps led down. A mild risk-off/quality tell, not a distribution-under-a-rally tell.
- `directional_tradable` = **true** (raw cohort existence only) · `s1_standdown` = **false**, and unlike last night this is a **clean miss on both legs**: ret5 +0.470% is 2.03pts short of the 2.5% up-thrust bar, dd15 −1.77% fails the ≥2% dip precondition for the lower 1.5% bar, and the dip leg (ret5 < −2%) is the wrong sign entirely. Last night's double near-miss has receded.
- **Bottom line: NO DIRECTIONAL EDGE. Zero sized calls — a 15th consecutive flat session.** No lane has a positive, significant excess in tonight's regime cell, and **OI_FADE returned zero surviving candidates for the first time this cycle.**

## Directional Book (excess-scored)
**Empty — zero sized calls.** No lane in this repo sizes at all since OI_FADE's 2026-08-22 demotion to advisory. **Phase D (`risk-sizer`) was vacuous and `fundamentals-gate` was correctly not spawned** — it runs only on names about to be sized, and tonight there were none to run it on.

### Phase C — the applicable regime cell, exit-day-clustered
Tonight is **plain CHOP with `s1_standdown=FALSE`**. The pooled "CHOP" row must **not** be used: it collapses plain CHOP with CHOP/REBOUND-THRUST, and **OI_FADE's sign flips between them** — re-measured tonight: **collapsed +0.0023 (n=492) vs plain −0.0010 (n=344) vs REBOUND-THRUST +0.0098 (n=148)**. The correct cell, with `t` clustered on **exit-days**, not rows:

| Lane | n rows | exit-days | mean excess | t (exit-day) | p | hit − base | verdict |
|---|---|---|---|---|---|---|---|
| MOM_LONG | 354 | 24 | **−0.0266** | −2.51 | **0.012** | −0.359 | significantly NEGATIVE |
| MOM_SHORT | 282 | 24 | −0.0220 | −1.93 | 0.054 | +0.064 | negative, marginal |
| OI_FADE | 344 | 23 | −0.0010 | −0.13 | 0.898 | +0.235 | indistinguishable from zero |
| S2_dp_revert | 410 | 28 | +0.0007 | +0.18 | 0.859 | −0.059 | indistinguishable from zero |
| S4_pcr_fade | 417 | 28 | +0.0061 | +1.30 | 0.192 | −0.012 | not significant |

**Every cell carries the correlated-draw caveat** (all exit-day counts < 30, invariant #6). The only statistically real number in the table is **MOM_LONG's negative excess in CHOP** — an argument *against* the near-52w-high basket, not for anything. Score = `validated_excess × regime_fit` = **0 or negative for every candidate**; nothing reaches a sizing band.

## Regression gate — OI_FADE below baseline for a 6th session; still DATA, not code
`retro_harness.py --all`, **98 panel days** (2026-03-13 → 08-28), 20/98 stand-down days:

| Lane | recorded baseline | tonight pooled | Δ |
|---|---|---|---|
| MOM_LONG | −0.0118 (n=1213) | −0.0117 (n=1279) | +0.0001 ✓ |
| MOM_SHORT | −0.0138 (n=830) | −0.0130 (n=874) | +0.0008 ✓ |
| **OI_FADE** | **+0.0013 (n=1177)** | **−0.0018 (n=1252)** | **−0.0031 ✗** |
| S2_dp_revert | +0.0018 (n=1269) | +0.0013 (n=1338) | −0.0005 |
| S4_pcr_fade | +0.0024 (n=1304) | +0.0021 (n=1379) | −0.0003 |

**Isolation check (`analyses/audit/2026-08-28/harness_split.py`):**

**(a) The baseline cohort reproduces.** Pinning `BASELINE_EDGE=2026-08-21` returns **OI_FADE +0.0013/n=1177** and **S4 +0.0024/n=1304** — bit-identical to the record. MOM_SHORT −0.0137/n=828 (vs −0.0138/830) and S2 +0.0016/n=1264 (vs +0.0018/1269) drift within the known non-idempotent-vendor-feed tolerance. **MOM_LONG reads −0.0122/n=1209 tonight against a recorded −0.0118/n=1213 — it reproduced bit-identically last night and has since lost 4 rows**, the same Yahoo-retraction class that un-resolved EQR. **OI_FADE's baseline is fully intact — the pooled crossing is entirely new rows.**

**(b) No code changed.** `git log scripts/` last touches `6cceae8` (the 08-22 OI_FADE fix); working tree clean. Lane logic and thresholds untouched; the panel grew by one day.

**(c) The increment is now 5 exit-days with `base` PINNED, and it is still ONE cohort.** Every lane's increment resolves on **08-24 → 08-28** only. OI_FADE's increment is n=75, mean **−0.0500**, `base` **pinned at 1.00 on all five exit-days** — SPY was down in 100% of the new windows. Per-day means: −0.0633 / −0.0611 / −0.0607 / −0.0557 / **−0.0095**. The same names recur across 3–5 of the signal dates (META ×5, ACHR ×4, AMZN ×4, TTD ×3, SPCX ×3, NVDA, DKNG, PCG, WULF) — the signature of one cohort resolving repeatedly, not 75 independent draws. **Note the shape again: the benchmark fell in every one of these windows and a short lane still lost 5%.**

**The new exit-day is the first sign of the unwind.** 08-28 reads **−0.0095 with hit 0.53**, against −0.056 to −0.063 and hit 0.33 on the prior four — it dilutes the increment from −0.0602 (n=60) to −0.0500 (n=75) rather than deepening it.

**Verdict: NO REGRESSION. Do not re-baseline.** Re-pointing the reference onto five pinned-base exit-days would bake a single draw into it — the error the 08-22 cycle pre-registered against. The lane has been advisory since 08-22; **nothing operational changes.**

## Lane detail

### Momentum (both legs watch-only, never size)
Spine: 6,286 → 3,664 (issue_type Common Stock/ADR, **2,618 ETPs cut at source**) → 3,056 (price ≥$5) → 1,450 ($-ADV ≥$50M) → **1,395** (no earnings in 10 trading days).

- **MOM_SHORT — 23 reported, but only 21 are valid. I cut two, and they fail for *different* reasons.** This is the `pct_52w_range` trap firing in two distinct classes on one night:

  | Name | Screener 52w range | Yahoo truth | True pct_range | Class |
  |---|---|---|---|---|
  | **MIDD** | 110.82 – 180.13 | **89.16 – 148.55** | **39.7%** (off_high −24.1%) | **Data artifact — in-range-but-wrong.** Both legs are ~1.22× Yahoo's, the signature of an **unadjusted corporate action**, not a one-sided stale print. A mid-range name screened as a near-low short. **FALSE SHORT.** |
  | **TECH** | 43.195 – 72.62 | 43.20 – 72.62 | **99.1%** (off_high −0.4%) | **Not a data problem at all — the screener is correct.** TECH sits at 99.1% of its range, i.e. near its 52-week **HIGH**. The lane filed the same ticker into *both* its near-low short list and its deal-pinned near-high watch. **Lane bookkeeping error.** |

  ⚠️ I am correcting the lane on MIDD's diagnosis as well: it reported "NOT a split artifact but stale UW panel data." The ~1.22× ratio on **both** legs says otherwise. The operational conclusion (cut it) is the same, but the cause matters for whether it self-heals.
  - The other four nearest the low verify **exactly** against Yahoo: MLM 522.19, LII 387.45, MCD 259.85, LHX 258.54. **TJX (low 133.55) and APTV (low 44.88) both set genuine fresh 52-week lows today** — pct_range 4.3% and 2.0%.
- **MOM_LONG — 181 names, and the earnings contamination is much smaller than last night: 1 gapper, not 9.** **ESTC +19.31%** (08-27 post-market print) is the only name that gapped ≥7%; `earnings_gate.py` is **forward-only** and passed it, reporting next print 09-09.
  - ⚠️ **ESTC also exposes the exclusion artifact changing cohort *membership*, not just labels.** Its screener `pct_52w_range` prints **1.0712 — outside [0,1]**, because UW's `w52h` (96.065) excludes the session in which ESTC printed a 108.00 high. On Yahoo's range ESTC is at **87.7% and closed 7.5% off a high it set today** — a gap-up that faded hard, which would **not** clear the 0.95×w52h rule on current-session data. It is in the cohort only because the high it set today is invisible to the screen.
  - **The cohort has no breadth: median day-move +0.02%, only 51.9% green.** Half the basket fell. This is the lane with a **significantly negative** excess in tonight's cell (−2.66%, p=0.012).
  - Deal-pinned watch (near-zero realized vol pinned at the high — cut if a cash acquisition is announced): **APGE** (0.033%/day, 134.97 vs a 134.99 high), **CRNX** (0.035%/day, 84.84 vs 84.885), **TECH** (0.221%/day, 72.35 vs 72.62).

### OI_FADE (advisory — never sizes)
**Zero survivors. All 15 `oi_rel_build`-ranked candidates cut** — the first empty night this cycle.

| Cut reason | Names |
|---|---|
| **Liquidity / price floor** (8) | MBUU ($5.3M ADV), MNRO ($17.4M), ZURA ($7.4M), **DYN ($44.7M)**, UHALB ($20.6M), EYPT ($4.48 close), TUYA ($1.88 close), IRD ($3.69 close) |
| **Persistence — single-day block** (3) | DCI (0.991), IRD (0.910), **DKS (1.143** — 08-26 alone printed +38,754 = 114% of the 5d net, then 08-27 reversed −11,233) |
| **ETF** (3) | FTEC, NBIZ (2× short single-stock), BTCZ (2× inverse bitcoin) |
| **Listing age** (1) | HONA (IPO 2026-06-16, 53 trading days < 60-day floor) |
| **Concentration + invalidation** (1) | BZ — 80.3% of the 5d net landed on 08-27 alone (68.3% last night), **and `last_call_net` went negative today (−20)**: calls genuinely closing |
| **Partial 5d window** (1) | UHALB (only 2 of 5 panel days present) — fail-closed |

- **I verified all seven liquidity/price cuts independently** via `liquidity.py`. **DYN's decay through the floor is real and now unambiguous: $50.8M (08-26) → $48.1M (08-27) → $44.7M (08-28).**
- **None of the 15 sits in the RAW `oi_net_5d` top-15**, so none would have inherited the historical +0.0013 prior even before the gates — that prior grades top-15-by-RAW and is dead on arrival tonight regardless.
- RAW top-15 is again the **degenerate ETP/mega-cap case**: EWZ, SPY, SLV, IBIT, USO, TLT (ETFs), VIX (an index, not tradeable), then BABA, SPCX, INTC, NVDA, PBR, SOFI, META, WULF. Zero overlap with the rel_build ranking — exactly why the lane never ranks on raw.
- `catalyst_split.py` correctly not run: with zero survivors there is no live `>=`/`>` boundary question. Next prints for the four names that cleared liquidity before their other cuts (DCI 12-03, DKS 11-24, HONA 11-04, BZ 11-17) all sit outside the 5-day build window anyway.
- ⚠️ Tool limitation recorded: `fz news` returned only generic market-wide headlines, not ticker-specific, so the M&A/rumor-gate check is **not a clean bill** tonight — it is an absence of evidence. Moot, since every name is cut on other grounds.

### S4 PCR-fade (advisory) — gates clean, verified
Funnel: 6,286 → 3,664 (issue_type) → 1,450 (liquidity) → **667 (call-volume floor ≥250)** → 34 (PCR top-5%, p95 = **2.2538**) → **33**.

- **The call-volume floor binds: minimum `call_volume` among survivors is PAYC-class at 285.** No NWG-style denominator artifacts (PCR 682 on three calls).
- **`issue_type` queried directly for all 33: 29 Common Stock, 4 ADR (EQNR, XPEV, BNTX, TTE), 0 ETFs.** Last week's SPYM/XRT/LABD leak did not recur.
- Earnings gate (trading-day h5, 08-29 → 09-05): **0 names blocked.**
- **TAP dropped on a same-day ex-dividend** — dividend-capture flow contaminates the ratio. I confirmed this is a **documented lane rule**, not an ad-hoc cut (`sentiment-contrarian.md:41`, precedent ITT 2026-07-06).
- Slate by PCR: FAST 8.45, ORLY 7.53, GH 6.97, LTH 6.17, EQNR 5.90, WBD 5.80, IMAX 5.49, NXT 5.48, APH 5.05, VICI 4.52, NLY 4.44, ARCC 4.06, PAYC 3.99, BKR 3.92, GPN 3.79, BTU 3.67, ARES 3.35, XPEV 3.28, BNTX 3.07, SFM 3.05, TLN 2.85, MPC 2.84, BSX 2.75, IP 2.68, FROG 2.61, TTE 2.58, WHR 2.57, QXO 2.55, CAR 2.49, CAKE 2.44, FDX 2.43, BURL 2.41, RUN 2.29.
- ⚠️ Framing: S4's `hit − base` is **negative** (−0.028 baseline, −0.012 in tonight's cell). This lane has **never had a hit-rate edge** — its excess is right-tail only. Not a high-probability setup.

### S2 dark-pool reversion (advisory)
Funnel: 452,157 valid DP records / 5,235 tickers → 1,196 (DP premium ≥$10M) → 129 (oneside ≥0.90) → **75 (issue_type; 54 ETPs correctly cut)** → 29 after gates. BIPC blocked by the earnings gate.

| Ticker | DP premium | oneside | buy-skew | side |
|---|---|---|---|---|
| VEEV | $557.7M | 0.944 | 0.056 | SELL |
| ACN | $389.0M | 0.907 | 0.907 | BUY |
| SU | $269.2M | 0.979 | 0.021 | SELL |
| TENB | $259.1M | 0.979 | 0.979 | BUY |
| MCHP | $254.4M | 0.975 | 0.025 | SELL |
| CME | $237.2M | 0.931 | 0.931 | BUY |
| CI | $218.4M | 0.971 | 0.029 | SELL |
| PM | $207.4M | 0.956 | 0.044 | SELL |
| ADP | $194.1M | 0.964 | 0.964 | BUY |
| MPWR | $193.6M | 0.905 | 0.095 | SELL |

6 sell-skewed / 4 buy-skewed. The lane tilts **long on both**; the sell-side half is the weaker leg of that claim. Concentration magnitude has IC ≈ 0 — the ranking is a visibility filter, not conviction.

- ⚠️ **ORCHESTRATOR CORRECTION — the lane quoted the wrong lane's numbers.** Its framing section cited S2's baseline as "+0.0013 (n=1177, p=0.767)" with "live lane floors drive realized −0.81% (p=0.080)". **Those are OI_FADE's figures verbatim** — n=1177 is OI_FADE's baseline row count, and −0.81%/p=0.080 is OI_FADE's live floored-selection measurement. **S2's actual baseline is +0.0018 (n=1269)**; tonight's harness reads **+0.0013 (n=1338)** pooled and **+0.0007 (28 exit-days, p=0.859)** in the applicable cell. The lane's operational status (advisory, never sizes) is unchanged, but the evidence it cited for that status was another lane's.

## Vol Book (non-directional, net-of-cost, advisory)
**0DTE-VRP — SPY and QQQ BOTH stand aside, and this is a hard veto, not a marginal call.**
- Both names are **SHORT gamma at spot** — a trend-acceleration regime with an unsampled left tail. This is the script's own verdict (`sell_premium=False`, `gamma_source=local_flip`, `gamma_disagreement=False`) and it was independently reproduced by two agents hand-summing the per-strike ladder. Three derivations agree.
- ⚠️ **The GEX CLI bugs both fired again tonight.** The `regime` field read `FULLY_NEGATIVE` for both names — **wrong**, the ladder carries many positive strikes (SPY 772: +$99.7M; QQQ 730: +$64.9M). And the header `total_gex` again fails to reproduce the ladder sum, this time **with the opposite sign on SPY**: header −$139.8M vs a ladder sum of **+$45.6M**. Only the ladder, cumulated to spot, is trustworthy.
- ⚠️ **Recorded discrepancy I could not resolve:** the two agents quoted different low-VIX-tercile floors — **[15.1, 15.5]** (`--days 20`) and **[15.8, 17.3]**. I could not reproduce either bound from the script's JSON output, so **neither figure should be cited until the field is located.** It does not change tonight's verdict: VIX 14.43 sits below *either* floor, and the gamma sign vetoes the trade outright regardless.

**Earnings IV-crush — 1 tradeable candidate, 1 stand-aside, 2 drops. None sized.**

| Ticker | Print | Bracketing expiry | CLI `implied_move_perc` | **Hand ATM straddle** | Spread cost |
|---|---|---|---|---|---|
| **MDB** | 09-01 | **09-04 (7 DTE — clean)** | **0.6% — WRONG EXPIRY** | **15.6% of spot** | ~12.0% |
| NTAP | 09-02 | 09-18 (21 DTE, no weeklies) | 10.8% | 12.08% of spot | 8.3% |

- **The bracketing-expiry trap fired hard on MDB and I verified the arithmetic myself.** MDB's front expiry is **08-28 — today, 0DTE, and *before* the 09-01 print** — so the CLI's 0.6% prices a no-catalyst window. At the correct 09-04 bracket, spot 446.92: strike 445 straddle = 36.4625 + 33.8250 = **70.2875 (15.73%)**; strike 450 = 34.1375 + 34.4750 = **68.6125 (15.35%)**; distance-weighted **≈15.6%**. That is a **26× understatement** by the CLI.
- ⚠️ **MDB's bracketing expiry, 09-04, IS NFP day** — the crush thesis is conflated with a Tier-1 macro print landing on expiry.
- ⚠️ **An additional caveat I found that the lane did not flag: the put legs are thin.** The 445 put's median NBBO rests on **17 contracts** and the 450 put on 106, against 1,510 on the 450 call. A quote that thin is a weaker input than the call side, and the 445 put's $5.05 bid/ask is 15% of its own mid.
- Per the TPR precedent (realized −16.5% vs a 12.2% raw-IV read), treat every implied move as a **wing FLOOR, not an estimate** — wings 1.3–1.5× → ~20.3–23.4% from spot.
- **NTAP — stand aside on structure, not on data quality.** Its only bracket is 09-18, **16 days past the 09-02 print**; the 12.08% is a 21-day implied move of which just 5 days precede the catalyst, leaving two weeks of un-crushed ambient vega after the thesis resolves.
- Dropped: **SPWH** (only 2027-01-15 and 2027-04-16 listed — nothing within four months brackets the 09-01 print), **YRD** (no option rows at all).

## Watch / Stood-down
- **OI_FADE (0):** empty for the first time this cycle. Every candidate cut; **DYN finally fell through the liquidity floor** after three sessions of decay, and **DKS** failed persistence for a second straight night, worse than before (1.143 vs 0.986).
- **MOM_SHORT (21 valid of 23 reported):** MLM, LII, MCD, LHX, TJX, PEG, ROL, BEPC, APTV, VICI, HDB, MTDR, GERN, DVA, NFLX, CTS, MAC, RCM, VRSN, PSO, LKQ. **MIDD cut (false short, data artifact); TECH cut (at 99.1% of range — misfiled by the lane).**
- **MOM_LONG (181):** basket/watch only; **significantly negative in CHOP** (−2.66%, p=0.012), no breadth (median +0.02%, 51.9% green), and ESTC is in the cohort only via the current-session exclusion artifact.
- **S4 (33):** FAST, ORLY, GH, LTH, EQNR, WBD, IMAX, NXT, APH, VICI + 23 — ETP-clean, floor-verified, right-tail only.
- **S2 (top 10 of 29):** VEEV, ACN, SU, TENB, MCHP, CME, CI, PM, ADP, MPWR.
- **Cross-lane overlaps, noted as evidence-type diversification only — never summed** (invariant #2): **VICI** in both MOM_SHORT and S4; **MPC** in both MOM_LONG and S4; **FROG** in both MOM_LONG and S4. All size nothing either way.

## Risk
- **Correlation clusters:** none to collapse — nothing is sized. Standing note: OI_FADE's mega-cap/speculative cluster (META, ACHR, AMZN, TTD, SPCX, NVDA, DKNG, PCG, WULF) is what produced the −5% increment across five exit-days; it is **one theme resolving repeatedly**, not 75 independent names.
- **Event calendar:** Jackson Hole concludes **08-29** · **Aug NFP 09-04** (Tier-1 — *and MDB's straddle expiry*) · Labor Day **09-07** (closed) · PPI **09-10** · **CPI 09-11** (day 9 of the h10 window) · **FOMC 09-16** — day 11/12, just *outside* h10 but close enough to flag for any position opened tomorrow.
- **Tail caps:** not applicable — no position.
- **Hedge note:** the gamma flip is the night's real change. Dealers short gamma on **both** SPY and QQQ means hedging flows now **amplify** moves in both directions rather than damping them — with VIX at a 10-day low and below its own low-tercile floor, that is a cheap-optionality setup, and long premium remains structurally favoured over short premium.
- **`s1_standdown` is now a clean miss** on both legs (it was a double near-miss last night). The cell is unlikely to flip to CHOP/REBOUND-THRUST — where OI_FADE's sign inverts to +0.0098 — without a substantially stronger thrust than tonight's tape offers.
- **Data hygiene:** truth-set parquets rebuilt tonight to reach 2026-08-28 (preflight clear, 5/5 panel groups, 373,979 price rows / 2,444 of 2,471 tickers). **27 tickers unpriced by the Yahoo fetch — failed closed downstream.** Breadth recomputed independently on the screener spine and reproduces the Phase-A figures exactly.

## Envelope note
`decision.json` validates against `schemas/decision_envelope.v2.schema.json`. Its `lane_status[]` convention admits the three sizing-capable lanes (MOM_SHORT / MOM_LONG / OI_FADE), so **S2 and S4 are documented in this report only** — the same convention as the 08-26/08-27 envelopes. `calls[]` is empty.
