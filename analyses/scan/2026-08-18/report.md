# Market Scan — 2026-08-18

## Regime & Verdict

- **Regime: CHOP** · vol-state **LOW** (VIX 15.84, **14.2nd pct** of trailing 6mo, **+4.3%** on the day off 15.19, −4.0% on 10d) · breadth **817 adv / 1,599 dec, 33.6% green** (priced spine, n=2,431) · `directional_tradable` **TRUE** · `s1_standdown` **FALSE**
- SPY 767.45 (**−0.68%**), 1.5% off the 52w high (779.37, set 08-13), RSI14 56.6. QQQ 717.51 (**−1.69%**), IWM 300.23 (−1.26%).
- ret5 **−0.404%** · ret10 **−0.503%** · dd15 **−5.428%**
- **The UPTREND→CHOP decay flagged on 08-14 and 08-17 landed today**, on schedule and for the mechanical reason given: the ret10 anchor rolled up to 08-04's 771.33 while price went nowhere.
- **Bottom line: No directional edge today. ZERO new starters — the book stays FLAT for a 7th consecutive session.**

---

## What actually happened today (the headline number is misleading)

"SPY −0.68%, 33.6% green" reads as a broad decline. It was not. It was a **single-complex de-risking event with rotation into defensives and value**:

| | |
|---|---|
| SOXX **−4.96%** · SMH **−4.09%** · XLK −2.47% · ARKK −3.18% | semis / AI-hardware crushed |
| IGV **−0.03%** | software *flat* — so this is not "tech", it is semis specifically |
| XLE **+1.76%** · XLV **+1.60%** · XLP **+1.06%** · XLF **+0.45%** | defensives and value **green** |
| **RSP −0.45%** vs **SPY −0.68%** | equal-weight **beat** cap-weight |
| MU −7.02% · META −4.45% · AMD −4.27% · AVGO −3.17% · NVDA −2.34% | the complex |
| AAPL +1.45% · NFLX +2.30% · MSFT +0.27% · GOOGL +0.06% | mega-cap *ex-semis* fine |

**Median constituent −0.689% vs SPY −0.676%** on the full priced spine — dead in line. On the **liquid** universe (mcap >$2B, $-ADV >$50M, n=1,741) the **median stock −0.598% actually beat SPY**. So there is no index-vs-internals divergence in the median.

**Where the damage really is — the left tail, not the median.** p10 of the liquid universe went **−2.98% (08-17) → −4.56% (08-18)**; on the full spine, **−3.11% → −5.74%**, with mean (−1.458%) far below median (−0.689%). The worst names are down 20–30% (AAOX −30.2%, AXTX −28.4%, CRDU −26.0%, CBRG −25.7%). **Dispersion widened sharply while the median held.** That is a risk-appetite contraction concentrated in speculative names and the AI-hardware complex, not a broad decline — and it is the honest read of a −0.68% index day.

This is the same class of correction as 08-17's: the advancer/decliner ratio (2:1 negative) invites a "broad selloff" story that the median refutes.

### dd15 is not a drawdown (standing misread guard) — and it rolls out **tomorrow**
dd15 = min(last 15 closes)/close_10_back − 1. Tonight's −5.43% is the **07-29 low (729.46)** against the **08-04 anchor (771.33)**. The minimum sits *before* the anchor: it measures the tail of a completed +5.7% rally leg, not a live drawdown. SPY's actual distance off its trailing-15-session high (777.88) is **−1.35%**.

**07-29 is the oldest bar in the 15-close window — it rolls out at tomorrow's close.** Holding the tape flat, dd15 mechanically collapses:

| exit-day | min15 | on | anchor | dd15 |
|---|---|---|---|---|
| 08-18 (now) | 729.46 | 07-29 | 771.33 | **−5.43%** |
| 08-19 | 741.69 | 07-30 | 769.79 | −3.65% |
| 08-20 | 747.03 | 07-31 | 768.56 | −2.80% |
| 08-21 | 757.67 | 08-03 | 773.26 | −2.02% |
| 08-24 | 767.45 | 08-18 | 773.03 | **−0.72%** |

**Consequence for the crash guard:** arm (b) of `s1_standdown` fires on `ret5 > +1.5% AND dd15 < −2%`. From **08-24 that arm is mechanically dead** — a 1.5–2.5% five-day up-thrust next week would *not* trigger the standdown it triggered in W32. Only arm (a) (`ret5 > +2.5%`) and arm (c) (`ret5 < −2%` with `ret10 > −2%`) remain live. Flagged now because the guard's suppression history is a known confounder in the calibration audit.

### Regime trajectory — CHOP is stable, unlike last night's UPTREND
Holding SPY flat at 767.45, ret10 across the whole h10 window (→ 09-01):

| exit-day | anchor | anchor px | ret10 @ flat | UPTREND needs | PULLBACK needs |
|---|---|---|---|---|---|
| 08-19 | 08-05 | 769.79 | −0.30% | >781.34 | <758.24 |
| 08-21 | 08-07 | 773.26 | −0.75% | >784.86 | <761.66 |
| 08-26 | 08-12 | 772.49 | −0.65% | >784.08 | <760.90 |
| **08-27** | **08-13** | **777.88** | **−1.34%** | >789.55 | **<766.21** |
| 09-01 | 08-18 | 767.45 | 0.00% | >778.96 | <755.94 |

All anchors sit in a tight 768–778 band, so **CHOP is stable, not decaying** — the opposite of last night's mechanically-decaying UPTREND. The one pinch point is **08-27**, where the anchor rolls onto the 777.88 local high: PULLBACK triggers at **766.21, only 0.16% below today's close**. A further ~1% decline flips the label to PULLBACK exactly as PCE + NVDA + Jackson Hole land.

`uw risk market-regime` independently reads **TRANSITIONAL / half-size** — consistent in substance with CHOP. Its separate `trend: UPTREND` field is a 30-day/SMA read (different horizon, not a contradiction). Its options-flow `bullish_pct` is 31.5% (2.2:1 bearish-skewed) with price within 1.5% of a 52w high — a mild under-the-surface hedging tell, carried as context, not a veto.

---

## Directional Book (excess-scored)

**EMPTY — no name cleared any lane's bar tonight.**

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — |

Seventh consecutive flat session. Per-lane disposition against the **2026-08-17 baseline** (full 2,471-ticker spine, 89 days):

| Lane | Baseline | Disposition tonight |
|---|---|---|
| **OI_FADE** | +0.0038 (n=1176) | **NO_NAME_CLEARED** — see the structural finding below |
| **MOM_SHORT** | **−0.0137** (n=830) | Watch-only, never sizes (knowingly negative) — 17 names |
| **MOM_LONG** | **−0.0127** (n=1154) | Basket/watch only, never sizes (knowingly negative) — 236 names |
| **S2** | +0.0014 (n=1210) | Advisory-only, never sizes — 56 candidates, none news-verified |
| **S4** | +0.0025 (n=1241) | Advisory-only, never sizes — 29 names |

---

## FINDING 1 — the OI_FADE baseline grades a rule the live lane no longer runs

This is the most important thing in tonight's scan and it is a **measurement-validity** problem, not a market call.

`retro_harness.py`'s OI_FADE selection is, verbatim: **raw `oi_net_5d`, top 15**, after price ≥ $5, $-ADV ≥ $50M, earnings-clear-of-h10, `issue_type IN ('Common Stock','ADR')`, `is_index=false`. Nothing else — no `rel_build`, no `persistence`, no `catalyst_split`, no news gate.

The live lane ranks by **`oi_rel_build`** and applies persistence + catalyst + news gates on top. Reproducing the harness's exact query per session:

| session | harness rule | live lane |
|---|---|---|
| 08-06 → 08-18 (9 sessions) | **135 calls** (15/session, every session) | **0 calls** |

`n=1176` over 89 days ≈ 13.2 calls/session, consistent with the harness firing ~15/day throughout. **So the +0.0038 baseline — the number that gives OI_FADE its "most robust lane / sizes" status — describes a strategy the live engine has not executed once in nine sessions.** The regression gate is green on a rule the engine isn't trading.

Neither side is obviously wrong. The live lane's extra gates have repeatedly caught real defects (COKE's put-covering mechanism failure on 08-17; GEN's fired invalidation; tonight's RKT — below). But **those incremental gates have never themselves been measured** — there is no harness variant implementing them, so their claimed value is asserted, not validated. Two possibilities, and the panel cannot currently distinguish them:

1. the live gates add edge, and the harness baseline **understates** the live lane; or
2. the live gates are over-fitted to individually-diagnosed names, and the lane is **declining a real +0.38%/call edge** 15 times a session.

**Propose-only, for the 2026-08-22 calibration audit** (no lane or threshold changed tonight — that would require the regression gate, and this is the audit's call):
- Add a harness variant implementing the **live** selection rule (`rel_build` rank + persistence + catalyst_split) and grade it against the raw-rank rule on the same panel. That is the only way to price the gates.
- Until then, **stop citing +0.0038 as "the OI_FADE lane's" excess** in sizing contexts. It is the raw-rank rule's excess. This extends the recorded caution that the prior belongs to the raw top-15 population — the gap is now nine sessions wide and total, not marginal.

### RKT — the name this actually turned on
RKT is **#6 in the harness's exact top-15 tonight** (`oi_net_5d` +28,759; $13.99, $-ADV $401M). It therefore genuinely *does* inherit the measured prior — the blanket "raw top-15 is all mega-cap/ETP beta" discount that has held for six sessions **does not apply to it**. It also passes every mechanical gate: liquidity PASS, earnings PASS (reports 10-29, clear of h10), `prior_verdicts` clean, persistence 0.349 (organic, no single-day dominance), overwhelmingly call-side (+158,862 calls vs +15,067 puts), and `catalyst_split` reads **LIVE** (66.8% accrued after the 08-06 print).

**It is nonetheless excluded — on the news tape.** ValueAct holds a **9.9% activist stake** in Rocket Companies with board composition, capital allocation and **M&A strategy explicitly in scope**. Their Q2 13F (RKT as top move, 3.76% portfolio impact) hit **08-14**; a further large institutional filing (Diamond Hill, $67.8M) hit **08-17**. The build's two largest days by far are **08-17 (+38,431) and 08-18 (+50,158)** — a 2.3× acceleration immediately behind those disclosures.

That is **catalyst-informed positioning, not a crowd to fade** — the same M&A/rumor gate-gap class recorded for AZN on 08-05, which `catalyst_split` cannot see because there is no earnings print involved. Note also that `fz news --ticker RKT` is **polluted with Rocket *Lab* (RKLB) headlines**; three of the four most recent items are the wrong company. A ticker-name collision defeats a naive news read here — check issuer, not just ticker.

Recording RKT explicitly because it is the first name in seven sessions where the raw-rank discount was *not* the reason for the pass, and because the harness rule **would** have taken it.

---

## FINDING 2 — the momentum lane's 52-week levels are wrong (cohort membership is not)

The lane reported "**NO CORRUPTION DETECTED**" and ranked MOM_LONG by *"% above 52w low"* — the wrong metric for a near-52w-**high** leg. Yahoo-verified against `chart.py`, every one of its top-5 MOM_LONG "52w low" levels is wrong:

| Name | Lane's claimed 52w low | **Actual 52w low (Yahoo)** | Actual pct_range |
|---|---|---|---|
| PSX | $240.67 | **$121.24** (2025-08-19) | 99.9% |
| AMLX | $24.60 | **$7.63** (2025-08-19) | 99.0% |
| HAE | $92.25 | **$47.32** (2025-09-26) | 96.6% |
| CLMT | $49.17 | **$12.94** (2025-08-19) | 99.6% |
| TRGP | $291.04 | **$144.14** (2025-10-17) | 95.5% |

These look like recent swing lows, not 52-week lows. **The cohort membership is correct** — all five are genuinely at 95.5–99.9% of their 52w range per Yahoo — so nothing downstream is mis-selected, and neither leg sizes in any case. But this is exactly the **in-range-but-wrong** corruption class that manufactures false signals, declared absent by the lane that was asked to check for it. A lane's own "verified, no corruption" claim is not evidence; the verification has to be re-run.

**MOM_SHORT membership verified clean.** All top-5 confirmed at genuine new 52w lows *set today* (08-18): STLA 0.0% of range, ESAB 0.1%, GPI 0.2%, GME 0.3%, AMRZ 1.5%. Their negative `pct_52w_range` prints are stale `w52l` not yet including today's low — the detectable, benign class.

---

## Vol Book (non-directional)

### 0DTE-VRP — **STAND ASIDE, both symbols**
| | SPY | QQQ |
|---|---|---|
| VIX tercile (bounds [16.1, 17.3]) | **LOW** (15.84) | **LOW** |
| Conditional `mean_pnl_by_vix_state[LOW]` | — | **+0.07%** |
| Less ~0.10% round-trip cost | — | **−0.03%** |
| Aggregate GEX | **−1.22B** (FULLY_NEGATIVE) | **−524M** (independent per-strike sum −571M) |
| CLI `regime` label | NEGATIVE (coherent) | **POSITIVE — contradicts its own negative total** |
| `sell_premium` / `size_scalar` | False / 0.0 | headline True → **overridden to stand aside** |

- **SPY** stands aside unconditionally: dealers are **short gamma** at the money — the vol-amplifying, trend-accelerating state this sleeve is not sized to sell into. Short-gamma expected range 1.23% vs 0.77% long-gamma.
- **QQQ** stands aside on the **tercile trap**: the pooled `GO_PREMIUM_SELL_INTRADAY` headline is driven by MID/HIGH buckets (+0.431% / +0.493%) that do not apply tonight; tonight's LOW bucket is **+0.07% gross → −0.03% net**. QQQ's GEX read is additionally **data-quality flagged** — the CLI regime string says POSITIVE while its own `total_gex` is negative, and `zero_gamma_level=261.7` against a $717 spot is not a sane number. The `suggested_structure` text also mislabels a short-gamma-bucket wing width as "(long-gamma: quieter, mean-reverting)" — **do not read that as license to size tight.** The underlying math keeps the two readings separate (aggregate sign → range/wing-width; spot-vs-flip → regime/sell decision); only the display conflates them.
- VIX rose two sessions (+11.2% from 14.25 on 08-14) but remains **inside the LOW tercile** — richer, not yet rich.

### Earnings IV-crush — ADVISORY ONLY, never sized (no harness validates this lane)
Implied moves computed off the **bracketing** expiry (first expiry ≥ print) using **median** ATM IV. **Every figure is a LOWER BOUND** on the realized move (TPR precedent: realized −16.5% vs a ~12.2% raw-IV estimate) — size wings **1.3–1.5× wider** than these, not to them.

| Ticker | Print | Bracket exp | ATM straddle | **Implied move (floor)** | Naive CLI read | Cost % straddle | Verdict |
|---|---|---|---|---|---|---|---|
| NVDA | 08-26 AH | 08-28 (10d) | $14.00 | **6.37%** | 2.20% (**2.9× understated**) | **0.7%** | GO — best execution |
| OKTA | 08-26 | 08-28 (10d) | $20.15 | **13.99%** | 3.67% (**3.8× understated**) | 10.7% | GO — wings very wide |
| HPQ | 08-26 | 08-28 (10d) | $3.135 | **10.46%** | 2.82% (**3.7×**) | 2.4% | GO — tight/liquid |
| ADSK | 08-27 | 08-28 (10d) | $21.80 | **8.81%** | 2.95% (**~3×**) | 3.7% | GO |
| ROST | 08-20 | 08-21 (3d) | $15.70 | 6.64% | 5.66% | 5.7% | GO |
| DE | 08-20 | 08-21 (3d) | $33.25 | 5.64% | 4.37% | 8.6% | GO |
| TJX | 08-19 | 08-21 (3d) | $5.85 | 3.88% | 3.48% | 6.0% | GO — iron fly |
| JKHY | 08-18 | 08-21 (3d) | $9.20 | 6.01% | — | **20.7%** | **EXCLUDE** — spreads/OI too thin; no entry window left |
| COTY | 08-19 | 08-21 (3d) | $0.425 | 15.51% | 12.97% | **17.6%** | **EXCLUDE** — sub-$3, 353% ATM IV (same precedent as 08-17) |

- **The bracketing-expiry trap hit all four 08-26/08-27 names, NVDA included** — the naive `implied_move_perc` understated them ~3× by reading a no-catalyst front expiry. This is the second consecutive session it has bitten; it is now a standing check, not a one-off.
- **OKTA is event-kinked, not simply backwardated**: the interior curve peaks at the event expiry (08-21 112.3% → **08-28 133.2%** → 09-04 108.4% → 09-11 96.5%) while the tool reports flat `BACKWARDATION` with `kink_expiry: None`.

---

## Watch / Stood-down

### OI_FADE watch cohort — continuity (orchestrator's job; no lane carries these)
| Name | 5d net | Last session | Raw rank /1,162 | Status |
|---|---|---|---|---|
| **FDX** | +11,813 (was +13,537) | call +228, **net −546** (puts dominated) | 172 | Retained WATCH — build decaying and now choppy; no mechanical invalidation (call leg still +) |
| **BSY** | +4,361 | call +424, net +404 | 341 | Retained WATCH — still building organically (persistence 0.578) |
| **ITRI** | +2,818 | call +5, net ≈0 | 433 | Retained WATCH — build **stalled**, effectively dead two sessions |
| **GEN** | +3,561 | call +460 (recovered) | 374 | **Stays CUT** — one bounce day on a stale 08-12 spike (83.3% of 5d net) is not a fresh organic build |
| **RKT** | +143,795 (sum basis) | call +54,280, net +50,158 | **6** | **Excluded — activist-catalyst build** (see Finding 1) |

Also examined and passed: KNSA (raw 572), NEU (raw 721, all from 08-12, dead since), plus the standing cut list (STUB, INSW, AS — earnings-blocked, reports tomorrow).

### MOM_SHORT — watch-only (17 names, never sizes)
Extremes verified at genuine new 52w lows set today: **STLA** (0.0% of range), **ESAB** (0.1%), **GPI** (0.2%), **GME** (0.3%), **AMRZ** (1.5%). Sector spread: Industrials 5, Consumer Cyclical 5, Basic Materials 3, other 4. **GPI** carries a prior blocking verdict (W31 new-starter standdown).

### MOM_LONG — basket/watch only (236 names, never sizes)
Verified genuinely at highs: PSX 99.9% of range, CLMT 99.6%, AMLX 99.0%, HAE 96.6%, TRGP 95.5%. Concentration: Financials 27.5%, Healthcare 25.0%, Energy 13.6% — within the ⅓-per-sector cap. **Note the alignment with today's rotation**: the MOM_LONG cohort is Financials/Healthcare/Energy-heavy, i.e. precisely the sectors that were green today, while the semis complex that broke is absent from it.

### S4 sentiment-contrarian — 29 advisory names (never sizes)
Population 6,316 → 3,686 (Common Stock/ADR) → 1,479 (price/$-ADV) → 699 (option-liquidity) → 35 (top-5% PCR, threshold 2.487) → 31 (h10 earnings gate) → **29** (prior verdicts: MET VETO, KLAC standdown).

**The `call_volume ≥ 250` floor is confirmed shipped and applied.** Orchestrator-verified against the panel — the extreme-PCR leaders are **real put crowds, not denominator artifacts**: BNY 358 calls vs **30,511 puts** (PCR 85.2), XEL 282 vs **23,862** (PCR 84.6). Both clear the floor and both have genuinely enormous put legs, which is the opposite of 08-17's NWG-class failure (3 calls). Leaders: BNY, XEL, CARR (20.1), LYV (13.4), NVS (12.5), KGS, PWR, KD, CCJ, NTR.

Secondary `ivrank_chg_5d` tilt (h3, the only 3-regime-stable factor), 9 names after ETP cut: FA, TLN, VIRT, TTEK, STWD, PK, RCI, AXTA, NI.

### S2 liquidity-reversion — advisory tag only, zero starters
171 DP candidates (≥$10M premium, ≥90% one-sided) → 89 (Common Stock) → 85 (h5 earnings gate) → 75 (liquidity) → **56** after prior-verdict and catalyst exclusions.

**All 56 are explicitly news-UNVERIFIED and are published as a tag, not a ranked watchlist** — the lane itself reports IC ≈ 0 on concentration magnitude, so ranking them by DP premium would be false precision. Catalyst-informed exclusions: **REGN** (ex-dividend 08-18), **COF** (ex-dividend 08-17), plus 19 prior-verdict blocks (ALL, POST VETO, WEC, LYB, SPGI, SWK, ITRI, ARE, and others).

Largest one-sided prints: TMO $435.6M (93.7% sell-side), ABT $415.5M (91.0% sell), ADP $269.4M (91.8% sell), HON $164.0M (93.0% sell), JBL $87.4M (95.2% sell), XEL $85.6M (95.6% sell). 32 sell-side / 24 buy-side.

**Two cross-lane notes, noted never summed:** (1) **XEL** appears in both S2 (sell-side DP concentration → long-tilted revert) and S4 (PCR 84.6 → long) — same direction from two orthogonal evidence types, which is diversification, not confluence, and both lanes are advisory. (2) The S2 sell-side leaders are heavily **healthcare/defensive** (TMO, ABT, HON) — the sectors that *rallied* today (XLV +1.60%) — so the one-sided prints ran against the tape.

**Data-quality flag:** the S2 lane read `stock-screener-2026-08-17.parquet` while the 08-18 export was present. One session stale, affecting `issue_type`/liquidity fields only, and the lane sizes nothing — but recorded, because a stale-panel read is precisely what preflight exists to prevent.

---

## Risk

- **Correlation clusters:** not binding — nothing sized. Worth recording anyway that the harness's own top-15 tonight is **not 15 independent names**: 6 mega-cap tech (META, GOOGL, INTC, AAPL, TSLA, CSCO) and 5 crypto-miner/AI-datacenter (MARA, WULF, CORZ, RIOT, SMCI) are two correlated clusters. Under the corr ≥ 0.70 rule they collapse to ~2 positions plus NOK/ONDS/RKT/SOFI — i.e. the mechanical rule's 15 slots are ~6 effective bets, most of them QQQ beta.
- **Event calendar — the entire Tier-1 cluster sits inside the h10 window (08-19 → 09-02):**
  - 08-19 FOMC minutes (July) · 08-21 monthly OPEX
  - **08-26 PCE (8:30am ET) + Q2 GDP 2nd est. + NVDA Q2 FY27 AH** — Tier-1, stacked on one day
  - 08-27–29 Jackson Hole; **08-28 Kevin Warsh's first keynote as Fed Chair** — Tier-1, new-chair framework risk
  - 09-01 ISM Manufacturing · 09-04 NFP (just outside)
  - The **08-26→08-28 stack sits exactly on the 08-27 anchor-roll pinch point** where PULLBACK triggers only 0.16% below today's close.
- **Tail caps:** vacuous — nothing reached a sizing band, so Phase D had nothing to gate. `fundamentals-gate` was **not spawned**, correctly: it runs only on names about to be sized, and RKT was excluded upstream of sizing on the catalyst gate.
- **Vol left tail:** 0DTE stood aside on two independent grounds per symbol (SPY short-gamma structural; QQQ negative LOW-tercile net). Earnings-crush implied moves are floors, not estimates. Today's p10 blowout (−4.56% liquid) is a live reminder that the unsampled left tail is not theoretical.
- **Hedge note:** no book, no hedge required.

---

## Verified non-issue (recorded so it is not re-litigated)

`features.parquet.oi_net_5d` and `oi_build.py`'s `net_5d` disagree by ~5× (SOFI: +17,256 vs +86,281). **This is not a bug and not a metric-definition gap.** `build_features.py` computes `avg(oi_net_cp) OVER w` — the **mean** of daily net over 5 sessions; `oi_build.py` reports the **sum**. Ratio is exactly 5 (86,281/5 = 17,256.2; RKT 143,795/5 = 28,759; GME 74,493/5 = 14,898.6 — all exact). **Ranking is identical**, so raw-rank arbitration across the two sources is valid. Checked tonight because a 5× discrepancy between the live lane and the instrument grading it is the exact shape of a real defect.

## Data integrity (Phase 0)

Truth-set parquets were **stale on arrival** — all three ended 2026-08-17 against a 2026-08-18 trade date. Rebuilt in order before any lane ran: `prices` (352,141 rows / **2,447 of 2,471** tickers priced; 24 unpriced fail closed downstream), `returns` (SPY self-excess 0.0 at every horizon), `features` (174,202 rows / 2,485 tickers / 90 dates), `weekly_features`. Preflight re-run **exit 0**. Panel 5/5 complete for 08-18 (All Options 9,898,771 rows · Dark pool 455,873 · Hot Option Chains 26,331 · OI changes 282,299 · Stock Screener 6,316).

Held-book reconciliation: `held_book.py --prior conviction_2026-08-17.json` → **0 open positions**; verified back through 08-04, all conviction files carry 0. The book has been genuinely flat, so no vestigial-invalidation check applies.

## Envelope limitation (recorded for the audit)

The v2 schema's `lane_status.lane` enum admits only `MOM_SHORT` / `MOM_LONG` / `OI_FADE`, and its `disposition`
enum only `BASKET_WATCH` / `STOOD_DOWN` / `NO_NAME_CLEARED`. So tonight's **S2 (56 advisory names) and S4 (29)
have no machine-readable slot at all** and survive only in this report — as was also true on 08-17. RKT's
`EXCLUDED_CATALYST_INFORMED` disposition likewise had to be folded into the OI_FADE note rather than carried
as its own typed record. This compounds the known audit-resolver blindspot in which suppressed `lane_status`
candidates go unresolved and starve the gate-effectiveness test: an advisory lane that never reaches the
envelope can never be graded from the envelope. Flagged for 2026-08-22, not changed tonight.
