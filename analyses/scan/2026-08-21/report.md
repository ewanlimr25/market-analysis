# Market Scan — 2026-08-21

## Regime & Verdict
- **Regime: CHOP** · ret5 −1.370% · ret10 −0.980% · dd15 −2.020% (`regime_check.py`, truth set rebuilt tonight to 2026-08-21)
- **Vol-state:** VIX **15.13** (−0.88 pts, −5.5%) → **LOW** tercile (actual `vix_tercile_bounds [16.0, 17.3]`; last night's 16.01 was MID by 0.01). SPY dealers decisively **SHORT** gamma (`total_gex` −894.8M, no flip in range). QQQ book weakly short / near-flat.
- **Breadth divergence (advisory):** green price tape — 332 advancers / 169 decliners, 66% green — but options flow `bullish_pct` **39.2%** (2,479 bullish vs 3,837 bearish). Quiet distribution into a still-green tape.
- `directional_tradable` **TRUE** · `s1_standdown` **FALSE`
- **Bottom line: No actionable directional edge today. Book stays FLAT for a 10th consecutive session.**

**The binding reason is measurement, not gates.** In tonight's CHOP regime, **no lane clears the +0.3% starter floor** on the regime-conditional excess that Phase C actually specifies:

| Lane (CHOP-conditional, 93-day panel) | n | mean excess | t | 95% CI | Band |
|---|---|---|---|---|---|
| OI_FADE | 359 | **+0.0014** | 0.28 | [−0.0088, +0.0117] | below floor → watch |
| MOM_LONG | 356 | −0.0257 | −4.30 | [−0.0374, −0.0140] | below floor → watch |
| MOM_SHORT | 282 | −0.0220 | −4.36 | [−0.0318, −0.0121] | below floor → watch |
| S2_dp_revert | 352 | +0.0014 | 0.46 | [−0.0046, +0.0074] | advisory → watch |
| S4_pcr_fade | 357 | +0.0081 | 2.38 | [+0.0014, +0.0147] | advisory lane → watch regardless |

OI_FADE's CHOP excess is **statistically indistinguishable from zero**. Note this is a stricter and more correct input than the *pooled* figure prior sessions cited: pooled OI_FADE reads **+0.0029** tonight, which is *also* below the +0.3% floor (by 1bp). Both readings land on watch, so tonight's disposition does not rest on the methodology refinement — but the regime-conditional number is the one Phase C mandates ("validated_excess … for this horizon/regime"), and it should be the standing input going forward.

S4's CHOP bucket (+0.81%, t=2.38) is the only positive-and-above-floor cell in the table. It is **advisory-only by rule and does not size**; treat it as an observation for `/calibration-audit`, not a signal — it is one nominal result among ~30 lane×regime cells, with no multiple-testing correction, and S4's `hit − base` is negative (right-tail only).

## Directional Book (excess-scored)
**Empty — zero sized calls.** No candidate reached a sizing band; Phase D produced no sized output.

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — |

### AS — the standing carry item is CUT (overdetermined, three independent grounds)
AS was the pre-registered two-leg trigger from the 2026-08-20 conviction file.

- **Leg 1 (rank durability) — PASSED, and improved.** AS's raw `oi_net_5d` rank inside the harness's exact measured population went **17 (08-19) → 15 (08-20, marginal) → 12 of 15 tonight**, with a clear buffer to rank 16 (AAPL). Verified independently by the orchestrator by reproducing `retro_harness.py:94–111` verbatim (population 1,399 names), then confirmed separately by the lane. `validated_excess` ESTABLISHED for a second night.
- **Leg 2 (fundamentals CONFIRM required) — FAILED.** `fundamentals-gate` re-run: **VETO restated, nothing material since 08-20.** Every substantive news item (Q2 print, Q3 guide miss, Truist $50→$42, Barclays $49→$50) is dated 08-18/08-19; the single 08-20-stamped item does not mention AS (feed-tagging artifact). None of the three pre-registered CONFIRM triggers occurred. Correctly restated rather than re-litigated into a different answer. *(Known-broken tools handled: `leverage_flag` verified by hand — D/E 0.3022 is genuinely low here, so the mislabel bug did not misfire; the `fz` Recom/PT leg does not exist in this CLI build and was skipped without penalty rather than fabricated.)*
- **NEW tonight and decisive — the mechanical OI_FADE invalidation FIRED.** `oi_build.py`: last session `call_net` **−5,956**, net −3,446 — calls genuinely closing against a 5d build of +101,641. Daily: 08-17 +55,187 / 08-18 +8,200 / 08-19 +33,349 / 08-20 +8,351 / **08-21 −3,446**. This is the same rule that cut COO (08-13), NRG (08-14) and GEN (08-17) — **AS is the 4th**. The crowd this lane exists to fade started leaving today.
- Supporting context: AS is already **−11.4% over 10 days** (RSI14 39.8, 26.8% of 52w range) — a fade arriving late. `catalyst_split` still reads LIVE_BUILD on the 08-18 print under both boundaries (inclusive 54.7% / **strict 45.1%**), so the build was real through 08-20; it is the reversal, not the build, that kills it.

The trigger resolved cleanly: one leg passed, the other failed, and the name died on its own mechanics regardless. AS drops off the watch list — re-entry requires `last_call_net` to turn positive again **and** a fundamentals CONFIRM.

## Vol Book (non-directional)
Both sleeves **STAND ASIDE**. Zero directional points.

- **0DTE-VRP — SPY:** LOW-tercile conditional gross +0.06%/day → **−0.04%/day net** of the 0.10% round-trip. Negative *before* the gamma gate even applies. Dealers decisively short gamma. `sell_premium=false`.
- **0DTE-VRP — QQQ:** tool's `sell_premium=true` **overridden**. The CLI's `zero_gamma_level` printed **207.89 against spot 713.23** — a "flip" 71% below spot, the identical artifact class seen on 08-20 (208.83 vs 710.77), now **two nights running**. Its own `total_gex_0_45d` (−18.7M) and the 24 strikes bracketing spot (−9.0M) both read **SHORT** gamma, contradicting the CLI's LONG label. Net edge +0.051%/day is razor-thin and rests on a disputed regime read. Stand aside.
- **Earnings IV-crush — ADSK, HPQ: ADVISORY_NOT_SIZED, unchanged.** Bracketing-expiry trap fired again; straddles recomputed off the raw parquet at the 08-28 bracket (median IV, not CLI mean): **ADSK ≈ 8.8–9.2%** (CLI 2.28%), **HPQ ≈ 9.7–9.8%** (CLI 1.72%). Treat both as **lower bounds**, not targets. Not sized because the 08-28 expiry still stacks a macro-vol binary (PCE + NVDA 08-26, Jackson Hole 08-27–29, Warsh keynote 08-28) on top of the idiosyncratic earnings binary at the same expiration — the unsampled-left-tail cap remains unsatisfiable. MNSO / GOTU / EH excluded (no clean bracketing expiry); KTCC excluded (untradeable).

## Watch / Stood-down
- **MOM_SHORT — BASKET_WATCH, 12 Yahoo-verified genuine near-52w-lows:** APP, AZO, BWXT, CMS, CPRI, FRVO, GXO, LHX, LII, NRG, ONON, PEG. From 82 raw candidates; the `issue_type` filter cut **70 ETF/ETN** at source (AGG, BIL, VXX, UVXY, UVIX, RWM …), and every survivor was re-verified against Yahoo 52w data per the `pct_52w_range` corruption defect. Never sizes (PROVISIONAL cap, 0-for-9 / −5.3% forward). Carry-over: only **APP, CMS, PEG** persist from last night's 9; ALHC, AMRZ, APTV, MLM, **QXO**, ROL dropped out. Blocking priors on APP, FRVO, PEG unchanged.
- **MOM_LONG — BASKET_WATCH.** 455 raw near-52w-high names. CHOP-conditional excess −2.57% — the worst cell in the table. Never sizes.
- **OI_FADE — NO_NAME_CLEARED.** raw-vs-rel_build overlap is **1 of 15** (AS alone); the standing ranking gap continues. All 14 other rel_build candidates carry UNESTABLISHED `validated_excess` (best raw rank among the mechanically clean ones is VIK at 153/1,399) and cannot inherit the lane prior.
- **S2 — 68 advisory names**, never sizes. Ranking treated as **non-informative** (IC ≈ 0; `dp_oneside` is a binary timing tag, not a magnitude signal). Sell-side names carry the same long-tilted reversion; no short conviction.
- **S4 — 8 advisory names:** CARR, UTHR, MRCY, WOLF, SYM, FORM, ECL, DAVE. Call-volume floor **verified biting** — cohort minimum `call_volume` **254** vs the 250 threshold, so no PCR is being manufactured off a handful of contracts (the NWG-682-on-3-calls artifact class). 11 ETFs cut, WDAY earnings-blocked. UTHR and MRCY carry blocking priors.

### New findings recorded tonight
1. **Merger-arb gate — first live catch since it shipped 2026-08-01.** PSNL (rel_build rank 12) is under an announced **$1.5B all-stock acquisition by Tempus AI** disclosed 08-20; essentially its entire 5-day build accrued in the two sessions after the deal broke. Deal/spread hedging, not fadeable crowd froth. Gate remains "cheap insurance, still not validated" until this resolves.
2. **Print-day boundary trap fired on TJX** — `catalyst_split` reads **132.6% inclusive vs 15.8% strict `>`**: opposite verdicts from the same data, the exact EWTX failure mode. Cut.
3. **QQQ `zero_gamma_level` artifact recurred for a second consecutive night** (207.89 vs 208.83). This is now a pattern, not a one-off — worth a standing override rather than a nightly manual catch.
4. NXPI carries forward its 08-07 mechanism-cut (unresolved Ambarella rumor); RKT carries its ValueAct activist-stake exclusion. Nothing changed on either.

## Risk
- **Correlation clusters (gate 3, corr ≥ 0.70 → one position):** a tight crypto-miner cluster in the raw top-15 — **WULF/MARA/CIFR/CORZ** (0.726–0.872) collapses to a single slot; **INTC–NOK** 0.759 is a second pair. AS is genuinely uncorrelated with the rest (max 0.509 vs RKT), so gate 3 was never AS's binding constraint.
- **Event stack inside any h10 window opened tonight (ends 2026-09-05):** PCE + NVDA earnings 08-26 · Jackson Hole 08-27–29 · **Warsh's first keynote as Fed Chair 08-28** · **August NFP 09-04**, landing on the final trading day of the window. Any short opened tonight eats all four.
- **Crash-guard proximity.** Arm (a) unconfirmed-dip (ret5 < −2% & ret10 > −2%): ret5 −1.370%, now **63bp away and receding** (it was 4bp last night). Arm (b) up-thrust/rebound: its dd15 < −2% leg is **already satisfied** at −2.020%, needing only ret5 > +1.5% — a **+2.87pt swing**. Arm (b) is the live risk, and a dovish PCE/Warsh or a strong NVDA print is precisely what completes it, which would retroactively zero the MOM_SHORT basket.
- Hedge note: no directional exposure, so no hedge required. The book's risk tonight is entirely opportunity cost.

## Regression gate — read as data, not code
`retro_harness.py --all` on the rebuilt panel: **93 days, 2,488-ticker spine** (baseline was 89 days, 2,471). **No lane or threshold code changed tonight**, so per `docs/regression-gate.md` this is panel growth + universe change, not a regression.

| Lane | Baseline (08-17, 89d/2471) | Tonight (93d/2488) | Δ | new rows | increment mean |
|---|---|---|---|---|---|
| MOM_LONG | −0.0127 (n=1154) | −0.0118 (n=1213) | **+0.0009** | 59 | +0.0058 |
| MOM_SHORT | −0.0137 (n=830) | −0.0138 (n=830) | −0.0001 | **0** | n/a |
| OI_FADE | +0.0038 (n=1176) | +0.0029 (n=1237) | **−0.0009** | 61 | **−0.0145** |
| S2_dp_revert | +0.0014 (n=1210) | +0.0018 (n=1269) | +0.0004 | 59 | +0.0100 |
| S4_pcr_fade | +0.0025 (n=1241) | +0.0024 (n=1304) | −0.0001 | 63 | +0.0004 |

**OI_FADE's −0.0009 is one correlated draw, not decay.** The increment is 61 rows across only **4 distinct entry-days** (08-04 +0.0295 / 08-05 −0.0151 / 08-06 −0.0305 / **08-07 −0.0433**), three of them sharply negative. Per the exit-day counting rule, that is a single window, not 61 independent observations. And SPY was **down** 0.1–1.0% across those h10 windows (08-04→08-18 −0.50%, 08-07→08-21 −0.98%) — so this was **not** a beta rally: the *crowded* names outperformed a soft tape, which is exactly the environment that punishes a call-OI-build fade, while MOM_LONG (+0.58%) and S2 (+1.00%) gained on the same draw. MOM_SHORT added **zero** new rows.

**Do not re-baseline on this.** That is `/calibration-audit`'s call, and a recovery next window would not be evidence any fix worked.

## Calibration-audit readiness (due 2026-08-22)
The long-deferred non-overlapping cohort has **finally arrived**: **all 85 sized calls (56 OI_FADE, 22 MOM_SHORT, 7 S2) have matured — zero open.** Plus **528 matured suppressed observations** (389 `calls[]` watch/skip + 139 `lane_status` candidates) to feed the gate-effectiveness test. Standing item for the audit: AS is the first name in this repo's run to cross to established-positive `validated_excess` on a rank change alone and then die on its own mechanical invalidation — grade both the rank trigger and the invalidation rule against it.
