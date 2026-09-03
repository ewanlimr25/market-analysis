# Market Scan — 2026-09-02

## Regime & Verdict

- **Regime: CHOP** (plain, *not* CHOP/REBOUND-THRUST) · ret5 **−0.120%** · ret10 **−0.510%** · dd15 −0.950% · `directional_tradable=true` · `s1_standdown=false`
  — `scripts/regime_check.py --date 2026-09-02`, cross-verified against a live Yahoo read (`chart.py --rets 5,10`: ret5 −0.1201%, ret10 −0.5071%, matching to 3dp, so no stale-date fallback).
- **Tape:** SPY 765.16 (**+0.44%**) · QQQ 709.24 (**+0.23%**) · IWM 294.01 (**+1.18%**). Green across the board, reversing 09-01's −0.69%/−1.27%/−1.14%. Ten-session dispersion still negative and still small-cap-led: QQQ −0.96%, SPY −0.51%, **IWM −2.56%**.
- **Vol-state:** VIX **15.20, −6.98% on the day** — a full round-trip of 09-01's +9.52% pop to 16.34. **LOW tercile** on `zerodte_setup.py`'s trailing-60 bounds [15.8, 17.1]; yesterday was MID. VRP: SPY +0.46pp (FAIR), QQQ −2.64pp (IV underpricing realized). **Both SPY and QQQ dealer SHORT gamma** — hand-derived twice independently, and the QQQ label is corrupted again tonight (see Risk).
- **Breadth:** 4,126 adv / 1,711 dec (n=5,932 non-index), median **+0.54%**, mean +0.88% — **69.6% green**; `fz breadth` reads 59.8% green on the narrower S&P-500 universe. Two universes, not a contradiction. The median stock rose harder than SPY: broad-based buying.
- **Bottom line: No directional edge today. Eighteenth consecutive flat session.** No lane in this repo sizes; the directional book is empty by construction, not by failure to find names.

## Directional Book (excess-scored)

**EMPTY.** No lane sizes. `risk-sizer` was not spawned — with zero sized candidates Phase D is vacuous — and `fundamentals-gate` was correctly not spawned, since it runs only on names about to be sized.

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — |

## Open call rows — all five now matured

**AS (OI_FADE, entered 2026-08-19) matured at h10 today.** Verified against the SPY trading calendar rather than assumed: the ten sessions after 08-19 are 08-20, 08-21, 08-24, 08-25, 08-26, 08-27, 08-28, 08-31, 09-01, **09-02**. With FDX/GEN/BSY/ITRI having matured 08-28, **all 5 open call rows are now resolvable at the 2026-09-05 audit** and the open-call count goes to zero. Held-book reconciliation off the 09-01 conviction file read 0 open / 0 closed, verified against `book_state.positions == 0` in the source file rather than trusting the bare empty result (the known EXIT-substring bug).

## Regression gate & the OI_FADE_LIVE re-check

**No lane or threshold changed tonight**, so the gate is a data-only re-read. `retro_harness.py --all --oi-variant both`, 101 panel days:

| lane | n | mean_exc | hit | base | hit−base |
|---|---|---|---|---|---|
| MOM_LONG | 1314 | −0.0122 | 0.43 | 0.57 | −0.134 |
| MOM_SHORT | 909 | −0.0127 | 0.41 | 0.42 | −0.007 |
| OI_FADE | 1297 | −0.0012 | 0.53 | 0.41 | +0.118 |
| **OI_FADE_LIVE** | **475** | **−0.0077** | 0.49 | 0.56 | −0.067 |
| OI_FADE_RAWPOOL | 480 | −0.0136 | 0.48 | 0.56 | −0.085 |
| S2_dp_revert | 1369 | +0.0008 | 0.50 | 0.52 | −0.018 |
| S4_pcr_fade | 1416 | +0.0016 | 0.50 | 0.52 | −0.025 |

Four lanes read below the recorded baseline. **Isolation check by EXIT date** (the signal-date cut is inert on this panel — nothing signalled after 08-21 has matured):

| lane | recorded baseline | tonight, exit ≤ 08-21 | maturity edge (exit > 08-21) |
|---|---|---|---|
| MOM_LONG | −0.0118 (n=1213) | −0.0122 (n=1209) | −0.0121 (n=105), base **0.00** |
| MOM_SHORT | −0.0138 (n=830) | −0.0137 (n=826) | −0.0022 (n=83), base **1.00** |
| OI_FADE | +0.0013 (n=1177) | **+0.0013 (n=1177) — bit-exact** | −0.0254 (n=120), base **1.00** |
| S2 | +0.0018 (n=1269) | +0.0018 (n=1257) | −0.0096 (n=112) |
| S4 | +0.0024 (n=1304) | +0.0024 (n=1303) | −0.0081 (n=113) |

The baseline cohort's **means** are unchanged to 4dp on every lane. The entire full-panel move is the maturity edge, whose `base` is **pinned** — SPY down in 100% of the new h10 windows (base 1.00 for every short lane, 0.00 for the long lane). That is one correlated draw, exactly the pattern the repo pre-registered. **No regression; do not re-baseline.**

⚠️ **New this cycle: the baseline cohort no longer reproduces bit-exactly on the row COUNTS**, only on the means — MOM_LONG −4, MOM_SHORT −4, S2 −12, S4 −1, against a cohort entirely in the past that should be frozen. OI_FADE alone is bit-exact for a second night. The cause is the documented non-idempotent vendor feed, now visible as a **spine contraction**: `build_prices.py` reported **28 UNPRICED tickers** tonight (2,443 priced vs the baseline's 2,471-ticker spine), and EQR — the name CLAUDE.md already records for exactly this — is again unresolvable inside S2's baseline cohort. Row counts on those 28 tickers per lane (24/2/8/13/9) bound the effect. Means did not move, so this is attrition, not decay.

### OI_FADE_LIVE — the pre-registered re-check now stands at 31 complete `lane-exit-day`

Last night's carry-forward warned that the forming 2026-09-01 exit-day was only 4/15 resolved and must be excluded. **It has now completed at 15/15 and reads +0.0083** — and admitting it barely moved the result, which is the vindication of excluding it while partial:

| cohort | k (`lane-exit-day`) | mean | t | p (iid) |
|---|---|---|---|---|
| **COMPLETE only** | **31** | **−0.0083** | **−2.166** | **0.0303** |
| COMPLETE + tonight's forming day | 32 | −0.0073 | −1.913 | 0.0557 |

**The partial-window trap recurred tonight, one day later**: 2026-09-02 is forming at **10/15 resolved** and reads **+0.0226**, and including it would again push p across the pre-registered 0.05 line (0.0303 → 0.0557). This is not bad luck twice — it is structural. The newest exit-day at the maturity edge is always fractionally resolved, and the resolved fraction is systematically the *fast* half of the cohort. **Exclude forming exit-days by rule, not by nightly judgment.**

Verdict for the 2026-09-05 audit: the stand-down evidence is **CONFIRMED on sign and now above the 30-unit bar at 31 complete lane-exit-days**, p=0.0303 iid. It is **not** DURABLE on significance — the h10 window-overlap defect (9/10 shared days) means Newey-West roughly halves this t, and the same rows read p=0.016 / 0.0297 / 0.0303 on three consecutive nights with no new data. **Do not record this as a BH-surviving formal STOP.**

## Vol Book (non-directional)

Delta-neutral, advisory, quoted net of cost, zero directional points.

### 0DTE-VRP — STAND ASIDE on both SPY and QQQ

| | total_gex | CLI `regime` field | zero_gamma_level | derived |
|---|---|---|---|---|
| SPY | **−233.7M** | "FULLY_NEGATIVE" (agrees) | `null` — flip not computed | **SHORT gamma** |
| QQQ | **−304.9M** | **"POSITIVE" — CORRUPTED** | **256.43** vs spot 709, strikes 686–731 | **SHORT gamma** |

Both indices short gamma. VIX is in the **LOW** tercile, and the LOW-tercile conditional expectancy is the bucket the repo already knows can be negative net of cost — but the binding objection is different and stronger: the 60-day backtest is stratified by **VIX tercile only, not by gamma regime**, so tonight's short-gamma trend-acceleration state has an unsampled left tail whichever tercile it sits in. Quoting its conditional mean would be citing a statistic from a different regime than the live one. **Stand aside both.**

### Earnings IV-crush — 2 tradeable, 3 size-down/skip

NTAP/AGX/OLLI printed today and are correctly off the forward list.

| Ticker | Print | Raw `implied_move_perc` | Variance-isolated | Verdict |
|---|---|---|---|---|
| VSXY | 09-03 | 15.94% | 14.8% (cross-checks) | advisory sell-vol, iron fly on 09-18, wings 22–24%. Book liquid (1,866 contracts) |
| AEO | 09-09 | 2.74% — **discard** | **13.7%** | advisory sell-vol, iron fly on **09-11**, wings 19–20.5%. Both legs liquid |
| SUNB | 09-09 | 10.3% (floor) | 9.0% | advisory, **size down** — front leg 26 contracts |
| SHOE | 09-10 | 13.7% | 23.4% (low-confidence) | **size down materially** — back month 5 contracts; the two figures disagree ~1.7× |
| ODD | 09-09 | 5.7% | ~34% | **SKIP** — 18/9-contract legs; >5× disagreement is a thin-book mean-IV artifact |
| CGNT | 09-09 | — | — | **SKIP** — 6-contract front / 2-contract back |

**AEO is the informative one.** Its nearest listed expiry (09-04) falls **before** the 09-09 print — the genuine documented trap — so the CLI's own front-end IV ratio of 2.41 is reading a no-catalyst window and is unusable. Bracketing correctly on 09-11 and isolating the event variance gives 13.7%, against a raw `implied_move_perc` of **2.74%** that is internally impossible for a 123%-annualized 9-day option (theoretical straddle move ≈19%). Every figure above uses the CLI's **mean**-across-strikes IV, not an ATM/median straddle — no such endpoint exists in this CLI — so all of them are **floors requiring ATM confirmation**, per the TPR (~1.35×) and MDT (~1.44×) precedents.

## Watch / Stood-down

- **OI_FADE — STOOD DOWN, diary-only.** Zero candidates, zero watch list, empty slate to the sizer. Funnel: 6,291 screener → **1,818** liquid → 1,768 (earnings) → 1,351 (`issue_type`: 1,267 Common + 84 ADR; 399 ETFs cut) → 1,278 (full 5-day window, 72 partial-window rows failed closed) → 594 (build floors) → 593 (listing age) → **361** (persistence). Diary-only top ranks by `oi_rel_build`: **RSI 0.981/pers 0.49, VSNT 0.934/0.81, PSNL 0.697/0.24, EMBJ 0.683/0.69, FRVO 0.676/0.62** — **none is a suggestion.**
  - **First live M&A-gate test case since the gate shipped 2026-08-01: PSNL (rank 3).** Tempus AI agreed to acquire Personalis for ~$1.5–1.7B, announced 2026-07-20, **still pending**. It does *not* trip the lane's usual trigger — persistence 0.238 means the build is smooth across all five days, not one-day-dominated — which is itself what sustained merger-arb flow looks like. But the gate as written targets a **cash** deal ("pinned at the deal price"), and this is an **all-stock** deal: PSNL's 5-day realized vol is 1.86%/day, an order of magnitude above the pinned TMHC case, so it is not a clean fail-closed cut under the literal rule. **Recorded as unresolved for the audit: the gate's language may need widening from "cash" to "any definitive agreement."** Not a call made unilaterally tonight.
  - **Re-signal dedup confirmed again, and the gate-of-death is again the informative part.** **CPAY died at build floors** — `net_5d` = **+994**, six contracts under the 1,000 floor (it would also have failed persistence at 0.988, but the floor bites first). **HRI is the exact mirror** — passed the size floor comfortably (net +4,076) but persistence flipped to **1.061** from 0.52 last night. **HONA died at listing age** with `rel_build` **2.206**, the highest raw number on the board: it is the Honeywell Aerospace spinoff, IPO'd 2026-06-16, ~55–57 trading days old against a 60-day floor — killed by age, not by flow shape. **AS re-signals at rank 19 of 361** on the day its 08-19 row matured. Structural forward-N cap, not new evidence.
  - **Soft diary flags:** VSNT (rank 2) has `last_call_net` **−28** — calls genuinely closing — plus 90%+ of its net on 08-31; DK (−20) and SCI (−52) likewise. **SYRE is a wash, not a build**: its 5-day `call_Nd` is only **+103** while `net_Nd` +1,240 is almost entirely `put_Nd` −1,137 (puts closing, −742 on 09-02 alone) — the net-call-minus-put warning in its *positive*-sign form.
  - `catalyst_split.py` — all 15 survivors read `NO_CATALYST_IN_WINDOW` (every next print is November), so the known `>=` print-day boundary bug is **structurally inert tonight** and no strict-`>` re-sum was needed.
  - The **raw-rank** pool for the same date is PCG/PBR/META/AMZN/WULF/MSTR/TSLA/INTC — mega-caps by book size plus a crypto-miner cluster, all with `oi_rel_build` under 0.26 against the relative-ranked #1 at 0.981. Zero overlap with the diary top-15: the documented QQQ/crypto-beta trap the shipped rule exists to avoid.

- **MOM_SHORT — watch-only, never sizes. 33 names, not the 35 the lane returned** (see Lane reliability). All Yahoo-verified by the orchestrator: AS, TJX, LOW, CPRI, XPEV, NKE, ROL, KRMN, BLDR, FDXF, ONON, ESAB, LII, APTV, BEPC, MCD, HONA, AAON, AZO, SARO, LHX, VFC, RBA, VICI, XYL, BYD, QNT, TXT, JMKE, CMS, CRH, AMRZ, PEG. Fourteen made **new 52-week lows today** (AS, TJX, LOW, CPRI, XPEV, ROL, KRMN, FDXF, ONON, ESAB, LII, RBA, VICI, QNT) — the valid class-(b) that *validates* the short tag. Consumer Cyclical 40% / Industrials 37%.
- **MOM_LONG — basket/watch only.** 171 names after filters (VOD cut on the h10 earnings gate). Healthcare 26.3%, Energy 21.1%, Financials 18.7% — no sector above the ⅓ cap.
- **S2 (liquidity-reversion) — advisory. 60 names, not the 0 the lane returned** (see Lane reliability). Full gate: 141 names clear `dp_oneside ≥ 0.90` → 62 also clear `dp_prem ≥ $10M` + Common Stock + price ≥ $5 → **all 62 pass the $50M ADV floor** → 60 after the h5 earnings gate (ASO 09-09, PVH 09-02 blocked). Top by DP premium: UTHR ($248M, 90.1% one-sided), NSC ($148M, 93.0%), WIX ($135M, 93.2%), ITW ($128M, 90.1%), CI ($126M, 91.5%), AIG ($124M, 94.1%), NDAQ ($106M, 92.8%), ACGL ($103M, 97.9%), BMY ($97M, 90.2%), SLAB ($96M, 98.6%). Plain-CHOP cell remains indistinguishable from zero.
- **S4 (sentiment-contrarian) — advisory, right-tail only.** At the **shipped 250-contract call floor**, the top of the pool is WMB (PCR 12.81, 817 calls), **CNM (12.42, 1,302 calls)**, FAST (7.01, 640), EXE (6.73, 2,482), PWR (6.25, 395), EVRG (6.21, 612), ZION (5.32, 440), DBX (5.23, 1,208), UBS (4.33, 634), APH (4.22, 2,034). Six names sit in the **250–350 noise zone** where PCR rank is not meaningful: DT (313), BAM (317), WIX (332), EXPE (331), PNC (313), BUD (291). `hit − base` is **−0.030 in CHOP, −0.056 pooled — the lane has never had a hit-rate edge on this panel.** **AMRZ is on tonight's MOM_SHORT watch list and is simultaneously an S4 long tag** — noted as a cross-lane contradiction, never netted.

## Lane reliability — three of six lanes returned claims that did not survive verification

This is the load-bearing section tonight. Two of the three would have changed the written record.

1. **S2 was materially WRONG — it declared the lane empty.** It reported *"Survivors: 0 names… No name reached the extreme concentration threshold,"* citing NVDA (54.8%), MU (55.6%), SNDK (60.8%), DELL (52.8%). Every one of those is a top name by **dark-pool volume**, not by concentration: the lane ranked the wrong column and inspected four mega-caps instead of screening the panel. Ground truth is **141 names at `dp_oneside ≥ 0.90`** and **60 clearing every gate**. The output was discarded and rebuilt by the orchestrator. This is the second occurrence of the identical failure — 2026-08-24 recorded S2 returning "25 raw → 4 → 0, lane empty" against a ground truth of 105 names.
2. **Momentum's "all 35 Yahoo-verified, no false positives" was false — 2 are hard artifacts.**
   - **POWL**: screener `week_52_low` 171.03 / `week_52_high` **612.50**; Yahoo says low **84.64** / high 328.00. The un-split-adjusted high makes `close/w52_low = 0.997` read as a fresh low when the stock is **2.01× its true 52-week low** (pct_range 35.3%). **This is the same name, with the same defect, that 09-01's scan cut and documented** — the lane re-admitted it and asserted it verified clean.
   - **VMRK**: screener range 63.68–68.62 vs Yahoo 57.57–71.50 — too narrow, so `close/low = 1.019` squeaks through while the true range position is **52.7%**.
   - The other five names my ≤5%-range check flagged (JMKE, CMS, CRH, AMRZ, PEG at 5.2–8.4%) are **not** artifacts — all made genuine 52-week lows on 09-02 or 08-24 and their screener bounds match Yahoo. The correct test is **screener bounds vs Yahoo bounds**, not a `pct_range` threshold; a threshold alone would have wrongly cut five valid names.
3. **S4 raised a shipped threshold on its own authority and dropped a clean name.** It applied a **350**-contract call floor against the repo's shipped **250** (fixed 2026-08-17), presenting it as settled. Separately it omitted **CNM (PCR 12.42 on 1,302 calls)** — the #2 name in the pool, deep book, `prior_verdicts` clean — with no stated reason.

**New tool defect found while checking (3): `prior_verdicts.py` reports false blocking verdicts.** Two distinct heads, both live tonight:
- **Single-letter tickers defeat the word-boundary fix.** The matcher is `re.compile(rf"\b{ticker}\b")`, chosen (per its own comment) to stop `ALLE` matching inside `STALLED`. But ticker **`L`** matches `\bL\b` inside **"P&L"** — `&` is a non-word character, so the L is a standalone token. L (Loews) was flagged `PRIOR BLOCKING VERDICT` off a passage about ROST and implied-move floors that never mentions it.
- **The blocking keyword is scoped to the passage, not the ticker.** `blocking = any(b in s.lower() for b in BLOCKING)` flags the whole free-text passage, so any name appearing in a sentence that vetoes some *other* name inherits a false block. DBX's flag comes from a passage that explicitly **clears** DBX ("FULLY news-verified… and cleared") and vetoes AVB and BAH. ZION's comes from a passage listing it as a clean S4 name while excluding VSXY and BAH.
- Consequence: **S4 dropped 5 of 19 names (ZION, DBX, AMRZ, GXO, INFY) on these false flags.** Only two survive scrutiny on the merits — AMRZ (genuine cross-lane contradiction, it is on tonight's MOM_SHORT list) and INFY (whose real 08-31 flag was a 251-call denominator artifact that **no longer applies**: it has 660 calls tonight).

**Minor:** `earnings_gate.py` has no lower bound (`elif ned.isoformat() <= end`), so a print on or before the signal date blocks with the reason string *"reports 2026-09-02, inside h5 (2026-09-03..2026-09-10)"* — a window that does not contain the date. PVH was correctly excluded (it printed today) but for a mislabeled reason; a **stale** past `next_earnings_date` would over-block silently.

## Risk

- **Correlation clusters:** none sized, so none binding. Worth noting for the diary: MOM_SHORT is 77% Consumer Cyclical + Industrials, and the OI_FADE raw-rank pool is a single crypto-miner cluster (WULF/MSTR/CIFR/MARA/CORZ).
- **Event calendar (next 10 trading days):** **NFP 09-04**, PPI 09-10, **CPI 09-11**, **FOMC + dot-plot 09-16**. Labor Day **09-07** is closed. Four Tier-1 macro events inside a 10-day horizon is a dense calendar — any h10 lane opened today carries all four.
- **Dealer gamma is short on both indices** into that calendar, and the QQQ `regime` field is corrupted for the **second consecutive night** (SPY 08-31 → QQQ 09-01 → QQQ 09-02). `zerodte_setup.py`'s own `gamma_disagreement` check returned **false** while `zero_gamma_level` sat at 256.43 against a 686–731 strike book — the check reads the same corrupted field on both sides, so it cannot catch itself. The range check on `zero_gamma_level` remains the fix worth writing.
- **Tail caps:** not applicable — nothing sized.
- **Hedge note:** book is flat; no hedge required.
