# Market Scan — 2026-08-25

## Regime & Verdict
- **Regime: CHOP** · ret5 **−0.200%** · ret10 **−0.600%** · dd15 **−1.030%** (`regime_check.py`; truth set rebuilt tonight to 2026-08-25, preflight CLEAR on all five panel groups, full 2,471-ticker spine / 2,446 priced). Live Yahoo chart-API reads reproduce it to 3dp — SPY ret5 −0.201%, ret10 −0.603% — so no arbitration was needed.
- **Tape:** SPY **765.91 (+0.32%)**, QQQ **710.72 (+0.62%)**, IWM 299.23. Both indices printed outright up days.
- **Vol-state:** VIX **15.45** (−0.40 pts, −2.52%) → **LOW tercile**, bounds `[15.86, 17.28]`, **0.41 below the cut**. This is the first night in four with real buffer: 08-20 printed +0.02 *above* the cut and 08-24 printed −0.01 below it. The bucket is still re-cut nightly off a 60-session trailing window, so "LOW" is a live classification, not a stable one.
- **Dealer gamma — SPY SHORT, QQQ AT ITS FLIP.** Derived from the cumulative per-strike profile, not from any CLI header field (see below):
  - **SPY:** cumulative net-GEX at spot = **−$503M**; first zero-cross at strike **785**, i.e. **+2.5% above** spot 765.91. Unambiguously short gamma.
  - **QQQ:** cumulative is **−$167.6M at strike 710** and **+$9.3M at strike 711**, with spot at **710.72** — the flip sits *inside* that one-strike interval. The entire crossing is a single strike (711 carries +$176.9M). QQQ is **on its flip, marginally short**, not comfortably long.
- **Breadth: 207 advancers / 294 decliners, 41.15% green**, against options-flow `bullish_pct` **35.7%** (2,239 bullish / 4,041 bearish). **SPY closed GREEN on sub-50% breadth — the distribution tell FIRES tonight.** It did *not* fire on 08-24, when the tape was 60.4% green. Sector premium also flipped: **Technology +$122.4M inflow** tonight versus a −$346M outflow last night.
- `directional_tradable` **TRUE** · `s1_standdown` **FALSE** (both crash-guard conditions fail outright: ret5 −0.200% is nowhere near either the +2.5% up-thrust or the −2% unconfirmed-dip trigger).
- **Bottom line: No actionable directional edge today. Book stays FLAT for a 12th consecutive session.**

**The binding reason is measurement, not caution.** Tonight is **plain CHOP** (`s1_standdown` FALSE) — a different stratum from `CHOP/REBOUND-THRUST`, which must not be pooled with it. No lane clears the **+0.3% starter floor** on that cell:

| Lane (plain-CHOP, 95-day panel) | n | mean excess | **exit-days** | clustered mean | **t (exit-day clustered)** | hit − base | Band |
|---|---|---|---|---|---|---|---|
| MOM_LONG | 356 | −0.0257 | 24 | −0.0256 | **−2.41** | −0.360 | below floor → watch |
| MOM_SHORT | 282 | −0.0220 | 24 | −0.0177 | −1.93 | +0.064 | below floor → watch |
| OI_FADE | 344 | −0.0010 | 23 | −0.0009 | −0.13 | +0.235 | below floor → watch |
| S2_dp_revert | 366 | +0.0011 | 25 | +0.0012 | 0.26 | −0.030 | advisory → watch |
| S4_pcr_fade | 372 | **+0.0076** | 25 | +0.0075 | 1.49 | +0.013 | advisory lane → watch regardless |

S4 is the only lane whose plain-CHOP mean exceeds the floor, and it does not size for three independent reasons: it is an advisory lane by fixed mapping, its clustered t is **1.49** (not significant), and **25 exit-days is under 30**, so it carries the standing correlated-draw caveat and cannot graduate on this evidence.

### Three corrections to figures the lanes handed back
All three were caught by re-deriving from the harness rather than accepting the lane's own arithmetic. None changes tonight's verdict — every lane involved is advisory or watch-only — but each would have misstated the record.

1. **S4's regime cell was computed on the wrong horizon basis.** The lane reported plain-CHOP n=507 / 34 exit-days / +0.39% / hit−base −0.036. The harness measures S4 at **h5 only** (all 1,334 rows); the lane pooled h5+h10. On the gate's own basis the cell is **n=372, 25 exit-days, +0.76%, hit−base +0.013**. The distinction matters: the lane's 34 exit-days would have *waived* the correlated-draw caveat, and the gate's 25 does not.
2. **Momentum's regime statistics do not reconcile at all.** It reported MOM_SHORT n=42 / −1.89% and MOM_LONG n=25 / −7.76% with base 92%, and declined to produce exit-day clustering ("the audit provides row-level statistics but not explicitly distinct exit-day counts"). The harness gives **MOM_SHORT n=282 / −2.20%** and **MOM_LONG n=356 / −2.57% / base 0.71**, both across 24 exit-days. The harness figures are used throughout; the lane's are discarded.
3. **Momentum's `pct_52w_range` column is not `pct_52w_range`.** Every MOM_SHORT value printed >1.0 (1.0042, 1.0003, 1.0128…), which is impossible for a metric bounded on [0,1] — those are `close/w52l` ratios. Spot-checked against the chart API, the *cohort* is nonetheless correct (LII 0.8%, FDXF 0.1%, LHX 1.0%, NKE 1.5%, PEG 5.0%, CMS 6.7% of true range), so the selection stands and only the reported column is wrong.

## Directional Book (excess-scored)
**Empty — zero sized calls.** No candidate reached a sizing band, so **Phase D (`risk-sizer`) was vacuous and `fundamentals-gate` was correctly not spawned** — it runs only on names about to be sized. This matches the standing state: **no lane in this repo sizes at all** since OI_FADE's 2026-08-22 demotion.

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — |

## Regression gate — OI_FADE crossed below zero, and it is DATA, not code
`retro_harness.py --all` on 95 panel days versus the recorded baseline (93d, adopted 2026-08-22):

| Lane | Baseline | Tonight (95d) | Δ |
|---|---|---|---|
| MOM_LONG | −0.0118 (n=1213) | −0.0116 (n=1241) | +0.0002 ✓ |
| MOM_SHORT | −0.0138 (n=830) | −0.0134 (n=848) | +0.0004 ✓ |
| OI_FADE | +0.0013 (n=1177) | **−0.0003 (n=1207)** | **−0.0016 ✗** |
| S2_dp_revert | +0.0018 (n=1269) | **+0.0014 (n=1294)** | **−0.0004 ✗** |
| S4_pcr_fade | +0.0024 (n=1304) | +0.0024 (n=1334) | 0.0000 ✓ |

No lane or threshold code changed tonight, so the isolation check ran before either drop was read as a regression. **All three legs resolve cleanly.**

**(a) The baseline cohort reproduces exactly.** Re-running `harness_split.py` with `BASELINE_EDGE` pinned to 2026-08-21 returns **OI_FADE +0.0013 / n=1177**, **MOM_LONG −0.0118 / n=1213** and **S4 +0.0024 / n=1304** — bit-identical to the record. OI_FADE's baseline is fully intact; its pooled crossing below zero is entirely new rows.

**(b) The two shortfalls are vendor retraction, proven row-exact.** MOM_SHORT's baseline returned n=828 against 830, and S2's n=1264 against 1269. Six rows vanished from last night's stored set — **AVB ×3** (2026-03-19 and 03-20 MOM_SHORT h10; 05-08 and 06-01 S2 h5) and **EQR ×2** (05-19, 06-15 S2 h5) — on top of LBRDK's row lost on 08-24. Removing exactly those keys from last night's cohort gives **S2 +0.001614 vs tonight's +0.001614** and **MOM_SHORT −0.013735 vs −0.013735**, with a **symmetric difference of zero row keys**. Cause: AVB, EQR and LBRDK have all been truncated by the vendor to start **2026-07-17**, so their spring windows no longer resolve. EQR's last bar is 08-21 — it is not even current.

**(c) The increment is 2 exit-days with `base` pinned.** Every lane's increment resolves on just **2 exit-days (08-24, 08-25)**, and `base` is pinned — **1.00 for both short lanes, 0.00 for all three long lanes**, i.e. **SPY was down in 100% of the new windows**. OI_FADE's increment is n=30, mean **−0.0622**, split almost evenly across the two days (exit 08-24 −0.0633, exit 08-25 −0.0611). These are not 30 independent observations; they are two draws of the same event. The composition is the same one already documented: the lane was short **CELH, MSTR and MARA** into a speculative squeeze while its mega-cap shorts (META, AMZN, NVDA) supplied its only gains. Note the shape of the loss — the benchmark *fell* in every one of these windows and a short lane still lost 6%.

**Verdict: no regression. Do not re-baseline.** Re-pointing the reference onto two pinned-base exit-days would bake a single draw into it — precisely the error the 08-22 cycle pre-registered against. Also worth stating plainly: **OI_FADE's pooled figure is now negative, but that is the arithmetic of one squeeze, not evidence of decay**; the lane was already demoted to advisory on 08-22 and nothing operational changes.

### New finding — the recorded baseline is eroding, and the harness has no ledger protection
This is the **third consecutive instance** of the documented non-idempotency class, and it is now compounding rather than isolated. Two of the five recorded baselines (**S2 and MOM_SHORT**) can no longer be reproduced from live data at all — the cohorts they were measured on have partly ceased to exist. Panel-wide, **62 tickers now have bars starting after 2026-04-01** and **18 have no bar for 2026-08-25**.

`resolved_ledger.json` protects the *forward call book* only: **EQR appears in it** (it was once a forward call), but **AVB and LBRDK do not**, because they were only ever harness panel rows. So the instrument that enforces the regression gate has no durable record behind it, while the book it grades does. Flagged as an audit item for 2026-08-29 — proposal, not a change made tonight: snapshot the baseline cohort's rows to a frozen artifact so the gate can always reproduce its own reference.

## Vol Book (non-directional)
Both 0DTE sleeves **STAND ASIDE**. Zero directional points, delta-neutral, quoted net-of-cost.

- **0DTE-VRP — SPY: `sell_premium=false`.** Binding reason is the **gamma gate** (dealers net short at spot, flip +2.5% away). Economics were immaterial regardless: LOW-tercile conditional gross **+0.113%/day → +0.013% net** of the 0.10% round-trip, inside noise.
- **0DTE-VRP — QQQ: `sell_premium=false` — this reverses the lane's recommendation.** The vol-book lane returned `sell_premium=true` on a "robust LONG gamma" read, having taken the sign from *per-strike* values (noting 707–711 as "already net positive") rather than the cumulative profile. Cumulatively, QQQ does not cross zero until strike 711 and sits at −$167.6M at 710, with spot at **710.72** — it is **on the flip**, with the whole crossing carried by one strike. Fail-closed: stand aside. The economics it would have traded on were gross **+0.201%** → **+0.101% net**, genuinely positive — which is exactly why the gate, not the P&L, has to decide.
- **Earnings IV-crush — BBWI, OKTA, MDB: ADVISORY_NOT_SIZED.** Straddles computed off the raw parquet on the correctly **bracketing** expiry using median IV (not the CLI mean), and treated as **lower bounds**, so wings sit at floor × 1.35: **BBWI ≈18.7% → 25.3%**, **OKTA ≈19.2% → 25.9%**, **MDB ≈21.7% → 29.3%**.
  - **MDB is tonight's clean bracketing-expiry illustration:** the 08-28 contract expires *before* its 09-01 print, so the CLI's headline `implied_move_perc` of **4.1%** prices a no-catalyst window and understates by roughly **5×**. The real bracket is **09-04**.
  - **Re-checked on their own merits, not inherited:** NVDA `iv_rank` **40.15**, ADSK **78.12**, HPQ **73.36** — all fail the ≥80 screen tonight, so last night's ADSK/HPQ/OKTA trio is not carried forward intact. DY, A, DCI, GOTU excluded (nearest expiry 2026-09-18, 24 DTE, no bracketing contract); YRD INSUFFICIENT_DATA; SPWH has only 2027 expiries.
  - **The unsampled-left-tail cap is unsatisfiable for all three.** BBWI and OKTA expire **2026-08-28 — the Warsh keynote day**, which also carries the payrolls benchmark revision, inside Jackson Hole (08-27→29) and the week of NVDA's 08-26 print. MDB holds to 09-04, spanning the entire stack plus its own binary.

## Watch / Stood-down
- **ASST — the only ESTABLISHED OI_FADE name tonight.** It is the sole candidate inside *both* rankings: **rel_build #8** of the 329-name gated live pool and **raw `oi_net_5d` #13** (independently confirmed; the lane read #12 on a slightly tighter universe). Mechanics: `oi_net_5d` **+115,821** (call +133,402 / put +17,581), `oi_rel_build` 0.678, persistence 0.654, `last_call_net` +30,775. It therefore inherits the pooled prior — which is **+0.0013, n=1177, p=0.767, indistinguishable from zero**. **Material caution:** ASST (Strive Inc) is a **bitcoin-treasury company**; despite passing the `Common Stock` filter it is effectively a leveraged BTC proxy and belongs to a crypto-beta cluster alongside tonight's excluded BTCZ/ETH and CIFR/WULF/MARA prints — not an idiosyncratic short. This is the same class of trap as the SOXS leveraged-inverse artifact.
- **BIDU — watch framing DOWNGRADED, and the direction of travel is the point.** It did not converge on the top-15; it moved away. Raw rank **16 → 38** (lane read 35 on its universe), `oi_rel_build` **0.302 → 0.206**, call-side build **−23%** while the put side held flat. `last_call_net` stays positive (+6,277) so no mechanical invalidation fired, but the "AS-on-08-20 converging setup" framing from 08-24 is retired.
- **AS — CUT_STANDS, third consecutive night, on a single binding leg.** Legs re-tested: (1) `last_call_net` **+14,813 — CLEARS**; (3) fundamentals **CONFIRM** (4-for-4 EPS beat streak, +29% YoY revenue, raised FY guide, low leverage) — a genuine reversal of the 08-21 VETO; (2) raw rank **36 of 1,480 — FAILS**. Rank is the sole leg still binding, and it has now failed at 38 → 33/36 → 36 across three nights.
- **MOM_SHORT** — 15 verified near-52w-low names (LII, FDXF, AMRZ, LHX, BWXT, WSO, APTV, PEG, CMS, INIO, CRUS, ROL, NKE, MLM, VICI), watch-only and never sizing. **Note on the three dropped names:** CPRI, ONON and OLN were cut for UW-vs-Yahoo 52w mismatch, but the mismatch is stale UW `week_52_low` caused by each making a **new 52-week low today** (CPRI 13.30 vs UW 13.565; ONON 28.83 vs 29.26; OLN 17.37 vs 17.56). On verified Yahoo data they sit at **0.6% / 1.2% / 2.1%** of range — *nearer* the low than kept names PEG (5.0%) and CMS (6.7%). The correct handling is to substitute the verified value, not drop the name; dropping is fail-closed and harmless here only because the lane never sizes.
- **MOM_LONG** — ~93 verified near-52w-high names, basket/watch only, never sized per-name.
- **S2 (advisory)** — **35 clean names**, corrected from the lane's own output: it claimed 36, listed 37, and the list contained **NRIX**, which **fails the fail-closed liquidity floor** ($29.7M 20d $-ADV against the $50M bar), and **TPG**, which the lane itself had listed as prior-excluded. Both removed. Top by dark-pool premium: PG ($409.3M, 91.1% buy), SBUX ($188.7M), RHI ($102.8M), KHC ($95.2M), CTSH ($79.9M). Ranking is treated as non-informative (IC ≈ 0 — this is a binary liquidity-event tag, not a magnitude signal).
- **S4 (advisory)** — 27 candidates passing all mechanical and earnings gates, **19 clean** of prior verdicts (ATI, DLR, HSBC, BHF, JAZZ, CDNA, IP, AMGN, DOCN, FRSH, FTAI, VSAT, OTIS, SEI, BTDR, CRH, RRX, RGLD, ALLY). All 19 independently re-verified against the liquidity floor — all pass. Call-volume floor (250) confirmed applied to the **call leg specifically**, so no small-denominator PCR artifacts survived.
- **No cross-lane overlap.** The S2 and S4 rosters are disjoint, and no OI_FADE name appears in either — so no confluence question arises tonight. (Had one, it would be noted as evidence-type diversification and never summed.)

## Risk
- **GEX CLI corruption has now spread to every header field, and is the fourth consecutive night of manual override.** Tonight, for the first time, it is bidirectional and self-contradicting:

  | Field | SPY | QQQ |
  |---|---|---|
  | `total_gex` | −132,647,317 | +338,944,439 |
  | `regime` field | **"POSITIVE"** (contradicts its own sign) | **"NEGATIVE"** (contradicts its own sign) |
  | `zero_gamma_level` | **332.87** vs ~$766 spot — structurally impossible | 719.65 |
  | Σ(`per_strike`) | **+112,722,410 — opposite sign to the header** | +387,096,587 |
  | `zerodte_setup.py` label | "LONG" (wrong) | "SHORT" (wrong) |

  The `regime` field is now wrong on **both** symbols in **opposite** directions, so it is decoupled rather than merely inverted. Worse, for SPY the header `total_gex` **disagrees in sign with the sum of its own per-strike array** — so the standing advice to "trust `total_gex`, not the label" is no longer sufficient either. **Only the cumulative per-strike reconstruction is trustworthy.** `zerodte_setup.py` inherited the corruption on both symbols tonight and would have shipped a wrong `sell_premium` for each. This needs the standing internal-consistency guard; it has now been carried as a watch item for four nights.
- **Correlation clusters:** ASST sits in a crypto-beta cluster (BTCZ, ETH, CIFR, WULF, MARA) and must not be treated as idiosyncratic. MOM_SHORT retains a regulated-power/utility cluster (PEG, CMS) though it has thinned from last night's four-name bloc.
- **Event calendar (verified live, not inherited):** PCE **08-26 08:30 ET**; **NVDA Q2 FY27 earnings 08-26 after close** — same day as PCE; Jackson Hole **08-27→29**; **Warsh keynote 08-28 ~10:00 ET** (his first as Chair) with the **BLS preliminary CES benchmark revision the same morning**; August NFP **09-04 08:30 ET**.
- **Tail caps applied:** all vol-book earnings sleeves held at ADVISORY_NOT_SIZED on the unsampled left tail; both 0DTE sleeves gated off on dealer gamma.
- **Hedge note:** no directional exposure is open, so no hedge is required. The relevant risk tonight is not position risk but **measurement integrity** — a green tape on 41% breadth, a short-gamma SPY into a stacked macro week, and a baseline quietly eroding underneath the regression gate.
