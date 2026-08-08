# Market Scan — 2026-07-29

## Regime & Verdict

- **Regime: PULLBACK** (confirmed downtrend) · ret5 **−2.400%** · ret10 **−3.360%** · dd15 −3.360%
- **Vol-state: vol-AMPLIFYING / short-gamma.** ^VIX 18.21 → **20.66** (+13.5%, intraday 17.45–20.88 — a genuine
  vol-regime-shift day). **GEX FULLY_NEGATIVE on both indices**: SPY total_gex −$2.78B (7/50 strikes positive),
  QQQ −$1.18B (2/50 positive). Zero-gamma level not computable. Dealer hedging flows amplify moves, not dampen them.
- **Breadth: confirming, not diverging.** 32.5% bullish (2,043/6,279), pct_green 36.2%, avg change −0.89%.
  Red tape *and* red breadth — no distribution divergence.
- `directional_tradable` = **TRUE** · `s1_standdown` = **FALSE**
- **Tech-led, not broad:** SPY 729.46 (−1.54% today) ret5 −2.40%; **QQQ ret5 −6.18% / ret10 −7.80%**; IWM ret5 −1.78%.
  The AI-capex repricing that opened 2026-W30 is still the driver.

**Bottom line: no new directional starters.** The one name that cleared every mechanical lane gate (HRI) was
**VETOED on fundamentals**. The book is a single held short (PLNT) carried at unchanged half size on its own
pre-registered exit rule, three sessions from a binding exit. Vol book is thin by design: 0DTE stands aside.

### Why `s1_standdown` is affirmatively FALSE (not merely mechanically silent)
The guard fires on two mirror conditions and neither holds:
- up-thrust / V-rebound leg (ret5 > +2.5%, or > +1.5% off a ≥2% dip) — **N/A**, ret5 is −2.40%.
- unconfirmed-dip leg (ret5 < −2% **AND** ret10 > −2%) — ret5 −2.40% satisfies the first clause, but
  **ret10 −3.36% is not > −2%**, so the downtrend is *confirmed*. This is the regime the guard is designed to
  stay out of and let the short leg work.

The 2026-07-27 near-52w-low squeeze (+2.4% mean excess, 81% positive) was exactly the unconfirmed bounce the
guard exists to catch — and it resolved as a **failed** bounce, not a reversal. It has now been punished for two
straight sessions.

---

## Directional Book (excess-scored)

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| **PLNT** | OI_FADE | short | h10 | +0.70% mean / +1.21% med (n=906, hit 0.56 v 0.38) | 1.0 | **half (HELD, unchanged)** | Earlier of **08-03 close [BINDING]** or first genuinely **negative call_net** print (not fired: 07-29 = +85). Stop $59.50, **confirm tightened 2-day → 1-day** | Regime PASS · Liq PASS ($56.19 / $96.9M ADV) · Cluster PASS (sole position) · Fundamentals **CAUTION** (−1) · Event PASS (earnings 08-06 falls *after* exit) · Tail FLAG (persistence 0.81) |
| **HRI** | OI_FADE | short | h10 | +0.70% mean / +1.21% med | 1.0 | **DROP (0)** | n/a — not entered | Regime PASS · Liq PASS ($143.02 / $77.4M ADV) · Cluster n/a · **Fundamentals VETO** · Event PASS · Tail: −14.6% off 07-28 high in 1.5 sessions = bounce tail |

**No new starters.** One position, unchanged size.

### HRI — the near-miss, and why it was dropped
HRI was the **only** name in the OI_FADE top-15 to clear every mechanical gate, and it cleared them cleanly:
`oi_net_5d` **+6,673** (call +6,742 / put +69), `persistence_ratio` **0.568** (organic accretion, not a
single-day block), `oi_rel_build` 1.62, liquidity PASS, forward earnings PASS (next print 2026-10-27), and
`catalyst_split` = **LIVE_BUILD** — 41.4% of the 10-day build accrued *on or after* its 07-28 print, i.e. the
call crowd kept adding through and after the report rather than resolving pre-print (the SSNC failure mode).

Fundamentals inverted the thesis:
- Q2 (07-28): adj EPS **$1.43 vs $0.73 est (+94.7%)**, revenue $1.204B vs $1.132B (+6.4% beat, **+20.2% YoY**)
- **FY26 guidance RAISED** (rental rev $4.375–4.475B from $4.275–4.4B; EBITDA $2.05–2.125B from $2.0–2.1B)
- Insider MSPR **+23.89** (buying)
- **The ALLE post-print PT-raise cluster is present:** JPM 07-13 $140→$165, Citi 07-14 $155→$175,
  **Keybanc 07-29 (post-print) $165→$185** — a fresh cycle-high target *after* the print.

That is the precise pattern that vetoed ALLE on 2026-07-24 (beat + guide-raise + multiple post-print PT raises).
Per that precedent a contradiction of this scale is **DROPPED, not watch-listed**. Independently: HRI is already
−14.6% from its 07-28 intraday high ($167.50 → $143.02) in 1.5 sessions, so the entry would also have been
shorting into a completed collapse with a bounce tail — the lane's validated edge is measured on the general
population of heavy-call-build names, not on names that have already dumped 14%.

One thing the veto does *not* resolve: the OI signal itself was clean, and the equipment-rental complex carries
capex-cycle exposure into a tape repricing capex lower. If the analyst tape turns, this name re-qualifies.

### PLNT — held short, honoring the rule
Reconciled against the 07-29 close plus tonight's OI panel.

- Entry **$55.20** (2026-07-20) → close **$56.19**. Gross **−1.79%**.
- **Short excess since entry = −3.50%** (PLNT +1.79% vs SPY −1.70%). *This is the scoring currency and it is
  materially worse than the gross number.* `held_book.py` prints "gross −1.79%" (since entry) beside
  "excess −1.99%" (**today only**) — those are different horizons and must not be conflated.
- Exit rule **NOT triggered**: 07-29 print is call **+341** / put +256 = net **+85**. Calls still net-opening.
- **Signal quality is degrading, materially:** net_5d +1,451 but `persistence_ratio` **0.81** (up from 0.668) —
  **81% of the entire 5-day build is the single 07-28 print (+1,176)**, one point off the **0.85 single-block
  disqualifier**. `oi_rel_build` has collapsed to **0.025**. Screened fresh tonight, this name would likely
  not clear Phase B's own organic-build bar.
- Stock momentum runs against the short: ret5 **+3.96%**, ret10 **+7.56%**, RSI14 62.1.
- Fundamentals **CAUTION** (unchanged from 07-28, no movement). Named soft-invalidation ruled **NOT FIRED** —
  only 2 raises exist (Canaccord $80→$82, JPMorgan $60→$62) and **both are same-day as entry (07-20)**, alongside
  a Deutsche Bank **cut** ($61→$55, also 07-20). **Zero incremental analyst actions in the 7 sessions since.**
  Counting ambiguity flagged: one further raise makes a literal count of 3.
- Squeeze axis benign: short float 11.79%, days-to-cover 3.67. Securities class-action filings 07-21 (short-supportive).

**Decision: HOLD at half — honoring the pre-registered rule, not overriding it.** The rule's early-exit valve is
a *genuinely negative* call_net print, and tonight's decelerated but positive +85 does not cross it. Invariant #5
says a pre-registered rule is not bent mid-hold on discretion, and nothing tonight clears a bar — the decay is a
continuation of the trend the rule was already built to catch. Downside is time-boxed either way: **3 sessions**
(07-30, 07-31, 08-03).

**08-03 is BINDING, not advisory.** `earnings_gate.py` puts **PLNT's next print at 2026-08-06**, three days
*after* the exit. Exiting on schedule clears the print; any drift past 08-03 walks a losing short into earnings
it was never sized for. This is the ORCL/PRMB horizon-drift lesson with a catalyst attached.

**Stop tightened: $59.50 with confirm cut from 2-day to 1-day.** The level is unchanged; only the confirm window
moves. Reason is arithmetic, not sentiment — with three sessions left, a 2-day confirm can only complete by the
07-31 close, which exits 08-03, **the h10 date the rule already delivers**. As configured the stop was
*decorative*: it could not get you out one session earlier than the rule. At 1-day confirm, a close above $59.50
on 07-30 exits 07-31 — one session of real protection. Adjusting a discretionary overlay added 07-28 is not a
pre-registered-rule change, so invariant #5 is untouched; pulling the *level* in (e.g. to $58.50) was considered
and **rejected**, because substituting a discretionary exit for a live rule with 3 sessions left is exactly what
#5 guards against.

**Vigilance instruction for the remaining sessions (not a rule change):** a flat or negative print on 07-30 or
07-31 is a same-session exit — do not wait for confirmation math.

---

## Vol Book (non-directional, advisory, delta-neutral, 0 directional points)

**0DTE-VRP premium-selling: STAND ASIDE, size_scalar 0.0 (SPY and QQQ).** `zerodte_setup.py` returns
`sell_premium=false` for both on its VIX-spike gate. This overrides a trailing-60d net-of-cost positive mean
(SPY +0.142%/day, QQQ +0.269%/day after a 0.10% cost charge) for good reason: the validation sample contains
**no vol-shock day**, so tonight is plausibly the unsampled left tail itself. Reinforcing this — the SPY VRP
print of +5.11% (iv30d 17.3% vs realized 12.2%, regime PREMIUM_SELLING) rests on a **backward-looking realized-vol
denominator that has not yet absorbed today's spike**; it will compress or flip on the next print. Selling
premium into FULLY_NEGATIVE gamma on a stale VRP read is the textbook worst short-vol setup.

**Earnings IV-crush SELL-VOL (advisory).** All candidates show front-end backwardation, confirming
imminent-event pricing rather than stale IV. Quoted net of a ~0.4–0.6%-of-notional single-name round-trip cost.

| Name | Report | IV %ile | Front ratio | Implied move | VRP (30d) | Net verdict |
|---|---|---|---|---|---|---|
| **AMZN** | 07-30 AMC | 97.3 (z 1.67) | 2.11× | 5.86% | **+12.35pp** | **Cleanest** — richest VRP + highest IV %ile. Standard size |
| **MSFT** | 07-29 AMC | 88.0 (z 1.50) | 2.58× | ~5.5% *(est.)* | +10.2pp | Rich enough; wide wings. Standard size |
| **FSLR** | 07-30 | HIGH_IV | 1.84× | 7.25% | **+44.8pp** | **Best non-mega risk-adjusted**; liquid (ADV $358M) |
| **META** | 07-29 AMC | 85.3 (z 1.49) | 2.26× | ~6.8% *(est.)* | +2.3pp only | **HALF size** — richest headline IV (141.2%) but flat 30d VRP and the fattest historical tail |
| AAPL | 07-30 AMC | 88.0 (z 1.34) | 2.08× | 3.08% | **−3.6pp (negative)** | **SKIP** — smallest implied move on the board, IV already under-prices realized |
| MPWR | ~07-30/31 | HIGH_IV | **1.00× (flat)** | 15.4% | +21.6pp | **SKIP** — no weekly chain; the Aug-21 monthly bleeds ~3wk of non-event theta into the "crush" |
| COHU | 07-30 | 93.4 | — | 18.8% | — | **SKIP** — ADV $43.2M fails the $50M floor |

Structures: short iron fly / wide strangle at **1.1–1.3× the implied move** (not tight-to-the-move — a pre-print
gap on a negative-gamma tape blows through narrow wings). Defined-risk, delta-neutral throughout.

**Caveat on MSFT/META:** `uw insights earnings-play` did not surface either name despite their filters clearing
elsewhere (a coverage gap in that tool this session, not evidence of no event). Their implied moves are
**back-calculated** from the AMZN/AAPL implied-move-to-front-IV ratio (≈0.65× IV×√T). Directionally right, but
confirm against a live ATM straddle before execution — do not size mechanically off those two figures.

---

## Watch / Stood-down

- **MOM_SHORT — 11 names, watch-only, zero sizing.** The PROVISIONAL cap (2026-07-18 audit, pending durable-N ≥ 30
  forward revalidation) binds regardless of setup quality. Prior is **−0.03% mean** — the negative mean is the
  binding read, not the +20.6pp hit-base. Notables: FRVO, MIR, INIO, SKHY, CNM, KLAC (high IV-rank caution),
  TSLA (barely inside the screen, 1.26% above its 52w low, RSI 25.4 — ambiguous between continuation and
  mean-reversion). **4 of the 11 were ETFs and should never have been listed** — see Data Integrity below.
- **MOM_LONG — watch-only by the rubric, not by discretion.** Validated prior **+0.18% mean / −1.06% median**,
  tail-driven, basket-only. Phase-C tiering puts HIGH at ≥ +1% and MEDIUM at +0.3–1%, so **+0.18% cannot be sized
  above watch.** This holds *despite* genuinely supportive cohort data (below) — the 1-day cohort excess is not
  the h10 basket statistic, and three good days in a flight-to-quality tape do not establish h10 edge.
  Separately, the lane's proposed basket included **ROST**, which carries a standing fundamentals **VETO/DROP**
  (2026-07-20) — the lane did not run `prior_verdicts.py` against its own basket.
- **S2 (dp-reversion) — nothing advisable.** 12 names cleared all gates (9 failed liquidity, **34 blocked on the
  trading-day earnings gate**, 4 carried blocking prior verdicts). A +0.06% prior cannot carry a long-tilted
  mean-reversion trade through PCE + AMZN/AAPL into amplifying gamma. Three survivors (VC, TXNM, REZI) were
  **>90% one-sided SELL-side** — informed liquidation, not a fadeable overshoot.
- **S4 (pcr-fade) — advisory only, nothing sized.** 12 gate-clean names, earnings gate verified clean 12/12 on
  trading-day windows. The lane's own mechanism caution is the binding read: **a high PCR on a −1.54% day with
  VIX spiking into negative gamma is rational hedging demand, not a fadeable sentiment extreme.** 3 of 12
  (VRSN, CARR, VLY) show **puts net SOLD** — the premium-sign contradiction that held HOG back on 07-28.
- **HOG — WATCH, unchanged.** Re-qualified on tonight's data (vol_PCR 5.52, call_vol 226 clears the 75 floor,
  OI-PCR 1.25 = 86th pctl, earnings 2026-11-03 clear of h10). Still **no fundamentals-gate verdict on record**;
  net_put_premium is now positive (+$15.5K) but on a thin book. Advisory-lane cap binds either way.
- **`ivrank_chg_5d` h3 advisory tilt:** BANC, BBY, ANF, BURL, SHAZ, CCXI, ULTA, NVDA. BURL also appears in S4 —
  **noted as evidence-type diversification, explicitly NOT summed** (invariant #2). This list was **not
  ETF-filtered** — BKLN and JEPQ are ETFs and are struck.

### Corrected 52w-range cohort data (I recomputed this; the momentum lane's table was wrong)
Same-day excess vs SPY, valid `pct_52w_range` ∈ [0,1] only, ETFs excluded, price ≥ $5:

| Date | near-LOW decile | near-HIGH decile | spread |
|---|---|---|---|
| 07-27 | **+2.387%** mean, 81.0% pos (n=100) | +0.716%, 61.5% pos (n=179) | −1.67pp |
| 07-28 | −0.674%, 46.8% pos (n=77) | +1.223%, 73.5% pos (n=185) | +1.90pp |
| 07-29 | **−1.825%**, 32.9% pos (n=82) | **+1.247%**, 82.0% pos (n=150) | **+3.07pp** |

The normal factor sign (higher range percentile → better forward return, rank-IC t=+6.8) has now held **three
consecutive sessions and is widening**. The 07-27 squeeze cohort is being punished hard. **The momentum lane
reported near-low as −0.69% on 07-27 when it was actually +2.387%** — it inverted the single most important
recent data point, so its own regime-fit reasoning was treated as unreliable and this recompute was used instead.

---

## Risk

- **Correlation clusters: none live.** PLNT is the sole position; HRI is dropped, so no multi-name cluster exists.
- **Event calendar inside PLNT's 3 remaining sessions:** FOMC landed 07-29 (priced). **PCE 07-30 8:30am** and
  **AMZN + AAPL 07-30 AMC** both fall inside the window on a vol-amplifying, fully-negative-gamma tape —
  market-wide gap/whipsaw risk rather than a name-specific catalyst. **NFP 08-07** falls after the binding exit
  and is irrelevant to this hold. **PLNT's own 08-06 print is the reason 08-03 admits no drift.**
- **Tail caps applied:** PLNT held at half (no auto-full, invariant #4) with CAUTION already −1 tier; tail FLAG
  logged for persistence 0.81 / rel_build 0.025. Vol book sized for the unsampled left tail — 0DTE zeroed,
  META halved, AAPL/MPWR/COHU excluded. MOM_SHORT capped to zero by the standing PROVISIONAL cap.
- **Hedge note: no hedge warranted.** The book is one half-size short with a time-boxed exit inside three
  sessions and nothing correlated to stack against it. The live tail is idiosyncratic (a squeeze into a decaying
  signal), not systematic; short float 11.79% / DTC 3.67 is not a forcing function.

### Data integrity — three findings from tonight (proposals for `/calibration-audit`, NOT hand-patched)

1. **ETFs are leaking into lane universes, and the fix is already in the panel.** The Stock Screener export
   carries an **`issue_type`** column that labels ETFs cleanly. Tonight: the momentum lane's ETP filter claimed
   to gate on it and still passed **AAPD, ASTX, RAM, IGIB** (4 of its 11 MOM_SHORT names — all `issue_type=ETF`),
   mislabelling two of them as operating companies ("biotech", "Aerospace micro-cap"). S4 passed **EWH**
   (iShares MSCI Hong Kong) through a filter that caught AIQ/COMP/IYR/KIE/KRE/LQD/MDY. The `ivrank_chg_5d` list
   was not filtered at all (**BKLN**, **JEPQ**). This is the same universe pollution that inflated the OI_FADE
   prior ~2× (leveraged/thematic ETPs). Recommend a shared `issue_type IN ('Common Stock','ADR')` helper that
   every lane calls, rather than per-lane re-implementations. *(SKHY was checked and is `issue_type=ADR` —
   legitimately in-universe, not a leak.)*
2. **`pct_52w_range` is out of range for ~3% of names, concentrated exactly at the decile extremes the momentum
   lane trades.** On 07-29, of 1,865 names with a value: **35 have pct > 1** (close above the recorded `w52h`)
   and **28 have pct < 0** (close below `w52l`). Those land in the traded deciles at
   **35/233 (15%) of near-high** and **28/171 (16%) of near-low**. Mechanically this is UW's `w52h`/`w52l`
   lagging names that *just made a new extreme*, so cohort membership is broadly direction-consistent — but the
   values are unusable as a continuous factor and produce the impossible figures the lane reported
   ("−16.81%", "+125.8%"). A harder case exists: **KLAC shows `w52h` 2431.29 with `w52l` 186.75 and close
   170.19** — an internally inconsistent triple, not mere staleness. Recommend clamping to [0,1] against a
   chart-API-derived 52w range and quarantining inconsistent triples.
3. **Truth-set correlation coverage gap, now recurring.** The pairwise HRI/PLNT correlation recompute against
   `data/prices.parquet` returned **n=0 overlapping rows** — the same class of gap flagged for HOG on 07-28.
   Moot tonight (HRI is out on fundamentals, PLNT is a sole position), but gate 3 will fail *silently* the first
   night two names both clear gate 4 and need a live correlation number. Worth fixing before it is load-bearing.

**Regression gate: NOT RUN AND NOT REQUIRED** — no lane logic or threshold was changed tonight. All three findings
above are logged proposals. Any of them that becomes a gate must first clear
`python3 scripts/retro_harness.py --all` against the `4ec89dc` baseline (MOM_LONG +0.0018 · MOM_SHORT −0.0003 ·
OI_FADE +0.0070 · S2 +0.0006 · S4 +0.0044). The PLNT stop-confirm tightening is a discretionary overlay on a
single position, not a lane threshold, and does not trip this requirement.
