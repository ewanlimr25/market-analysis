# Weekly Review — 2026-W36 (Mon 2026-08-31 → Fri 2026-09-04)

**Book: FLAT.** No lane sizes. `calls[]` is empty for the second consecutive week and the 21st consecutive
session. That is the correct output of invariant #1, not a defect.

Preflight clear, and verified beyond its global-max check: SPY/QQQ/IWM each reach 2026-09-04 individually and
ticker coverage is uniform (2,425–2,428 across the week), so the `preflight max-date false clear` class did not
fire. Full 5-session week (`n_days=5` on all three indices).

---

## 1. The Week in Pictures (DIARY — documentation, 0 signal)

### Weekly candles

| | O | H | L | C | w_ret | close_pos | body_frac | structure vs prior |
|---|---|---|---|---|---|---|---|---|
| SPY | 767.33 | 774.03 | 759.48 | 770.19 | **+0.37%** | 0.74 | 0.20 | lower_low, hammer/hanging, follow_through |
| QQQ | 715.17 | 721.86 | 704.66 | 718.96 | **+0.53%** | 0.83 | 0.22 | **inside week**, hammer/hanging, follow_through |
| IWM | 295.09 | 296.18 | 289.97 | 296.01 | **+0.31%** | 0.97 | 0.15 | lower_low, hammer/hanging, no follow_through |

Three near-identical small-bodied candles with long lower wicks. SPY's lower wick (7.85) is 2.7× its body
(2.86); IWM closed at the very top of its range. SPY and IWM both undercut the prior week's low and then closed
**above** the prior week's close — an undercut-and-reclaim. **QQQ did not**: it held both of 08-24's extremes
and printed an inside week. That divergence is the one genuinely notable structural fact of the week.

### Catalysts, anchored to the reaction

A **jobs week, not a CPI week** — no CPI/PPI/PCE/FOMC print landed, so the macro pre-registration arm accrues
nothing from an inflation event.

| Date | Print | Reaction |
|---|---|---|
| Wed 09-02 | **ISM Mfg (Aug) 54.6**, −1.0pt from 55.6, 8th straight expansion | SPY +0.44%, QQQ +0.23%, IWM +1.18% — first up-day, off Tuesday's low |
| Wed 09-02 | **ADP (Aug) +38K**, weakest since January, vs +47K expected | Soft labour read dovish; turned the tape and set up Thursday |
| Fri 09-04 | **NFP (Aug) +162K vs +53K expected** — 3× consensus. U-3 4.1% unchanged, Jun/Jul revised **up** | **Reversal-after-catalyst.** SPY −0.39%, Dow −0.51%, Nasdaq −0.29%. Yields jumped; Sept **rate-HIKE** odds reset to ~63% |

The shape of the week is one trade being put on and partly taken off: Wednesday's soft ADP bought a dovish
rally (+1.49% Wed+Thu on SPY), and Friday's NFP — three times consensus — contradicted the premise and took
back 26% of it. **The week's high was made Thursday, the day before the print.** The market still closed green
on a labour report that pushed the Fed toward a hike, which is the honest oddity to carry forward.

### Regime trajectory

**CHOP all five sessions.** ret10 −0.730% (Mon) → +0.580% (Fri); dd15 −1.300% → −0.510%; `s1_standdown=False`
every day, so the crash guard never armed. Path: down Mon–Tue (weekly low 759.48 Tue), up Wed–Thu (weekly high
774.03 Thu), fade Fri.

**Vol state:** VIX 14.53. Term structure in clean contango (VIX9D 11.97 < VIX 14.53 < VIX3M 17.61 < VIX6M
19.89). A *path* for the term structure is **not re-derivable** — Yahoo serves a single snapshot for
^VIX9D/^VIX3M/^VIX6M — so no weekly trajectory is claimed. VRP: SPY −0.11pt (fair), QQQ −2.72pt (realized
running hotter than implied; no premium-selling edge).

**Dealer gamma — the known field-corruption defect fired again.** SPY total_gex −1.170B with the field
correctly reading `FULLY_NEGATIVE`. QQQ total_gex **−237M** while the CLI's `regime` field reported
**"POSITIVE"** ("expect mean-reversion"). Sign derived by hand from the per-strike profile: the largest single
print is strike 718 at −242M sitting on spot 718.32, with strikes below ~713 uniformly negative. **Derived: net
short gamma at the money — vol-amplifying, the opposite of the reported field.** QQQ's reported
`zero_gamma_level` of 243.37 against a 718 spot is a further artifact of the same corrupt output. This is the
third recorded instance of the `regime` field disagreeing with its own `total_gex`.

**Breadth divergence.** The index closed green on the week while only **34.8%** of S&P names were green (fz;
`uw` independently reads 35.4% bullish). Strength was concentrated in a narrow Technology/semis slice while the
median name fell — a distribution tell worth naming, not scoring.

### Sector leadership and flow

Leaders **SMH +2.51%**, XLE +2.20%, XLK +0.86%, XLU +0.82%. Laggards XLY −1.96%, XLB −1.39%, XLRE −1.24%,
XLI −1.06%. Semis and energy led; consumer discretionary and rate-sensitive real estate lagged, which fits the
rate-hike repricing — **but XLU +0.82% does not**, so the rate story only partly explains the cross-section.
All 12 sector series and SPY verified to reach 2026-09-04, so no series spans a different window than the ones
beside it.

Dark-pool premium (0 signal): SPY $44.7B, NVDA $40.8B, **SNDK $32.0B**, **MU $30.7B**, QQQ $29.1B. The memory
complex printed 3rd and 4th, ahead of QQQ — consistent with SMH's sector lead.

---

## 2. Validated Weekly Setups (SCORED — excess)

**Nothing sized. `calls[]` is empty.** No lane in this repo sizes: all four directional lanes are advisory or
watch-only, and OI_FADE — the last lane that ever sized — has been stood down to diary-only since 2026-08-29.

I rebuilt every lane's cohort independently. **All three lanes returned output that failed verification**, and
two of the three failures repeat a defect flagged within the last two sessions.

### MOM_SHORT — BASKET_WATCH, 18 verified names (the lane returned 15)

Funnel reproduced from `stock-screener-2026-09-04.parquet`: 6,293 rows → 1,824 past the $50M ADV floor → 1,410
after `issue_type ∈ (Common Stock, ADR)` → **20** at `close ≤ 1.02 × week_52_low`. (11 liquid rows carry NULL
`issue_type` and were dropped fail-closed; none was near a 52-week low, so the drop cost nothing.)

> **Lane defect, repeated one day after it was flagged.** The lane again applied a top-15 truncation *and* an
> invented 33% sector cap — neither is in the lane specification, and the 2026-09-04 scan recorded the identical
> pair. Its reported "sector concentration breach: 40% Utilities" is also simply false: Utilities are **2 of 18
> (11%)**. MOM_SHORT is a full-cohort watch list.

All 20 were Yahoo-verified individually with `chart.py --52w`. **Two cut, for different reasons — and the
distinction is the whole point:**

- **MIDD — genuine data artifact / false short.** Screener range 109.68–180.13 vs Yahoo 89.16–148.55, both legs
  ~1.22×: un-split-adjusted. True `pct_52w_range` is **38.0%**, not 2.94%. It is nowhere near its low. Same
  false short caught on 2026-08-28.
- **LULU — *not* an artifact.** It made a real new 52-week low (97.99) on 09-04 during a −17.4% earnings
  collapse, but closed at 100.61, **2.7% above it**, failing the 2% proximity gate on true data. Bad data and a
  real fresh low that closed too far off it are different failures with different fixes.

**MCD and LHX belong in the cohort, not beside it.** Both printed fresh 52-week lows on 09-04 (Yahoo 255.49,
256.05) — the out-of-range class that **validates** a short tag; the screener's `week_52_low` merely lags a day.
They are the two names *nearest* their lows in the entire cohort (0.2% and 0.3% of range).
`prior_verdicts.py` flags both as **PRIOR BLOCKING** — reading the matched passages, this is the known
false-blocking defect: the passages are the 09-03/09-04 scans recording that the momentum lane *wrongly cut*
these names. They exonerate rather than block.

**KRMN** kept and flagged as a boundary case: fails `close ≤ 1.02 × low` by 0.0011 (39.980 vs 39.9789) while
sitting at 1.0% of its true range.

Watch list (nearest-to-low first): **MCD, LHX, VICI, XYL, KRMN, ROL, NKE, TXT, AMTM, STZ, TJX, ONON, PEG, TSN,
GLPI, CCL, CMS, JOBY.** Crash guard **not fired** (`s1_standdown=False` all week). Never sizes — the one
recorded invariant-6 exception (knowingly negative, −0.0138, n=830).

### MOM_LONG — BASKET_WATCH, 182-name cohort

1,410 liquid Common/ADR → **182** at `close ≥ 0.95 × week_52_high`. The lane reported 179; the 3-name gap is
unexplained and **the lane's figure is the one that does not reproduce.**

Five of the 13 claimed fresh highs were Yahoo-verified — ITGR 126.80, DHT 21.09, MT 78.78, HPQ 32.78, CNH 14.46
— **all genuine new 52-week highs made 2026-09-04**, `pct_52w_range` 97.9–99.9%. These close *above* the
screener's stale `week_52_high`, the exact mirror of the fresh-low class on the short leg, and they validate the
long tag.

> **Lane error.** It again surfaced **ESTC** and called it a "FALSE LONG" data artifact. It is neither. ESTC's
> screener `week_52_high` (108.00) matches Yahoo **exactly** — there is no data defect. ESTC is 15.0% off its
> high (`pct_52w_range` 75.4%) and never enters the cohort under the canonical filter at all. That is a lane
> **filter leak**, not a data artifact, and it needs a different fix.

The lane's regime claim (CHOP −0.0266, t=−2.51) is **not adopted**: the CHOP cell collapses plain CHOP with
CHOP/REBOUND-THRUST, and the t was quoted unclustered. Irrelevant to sizing — this lane cannot size.

Top 15 by proximity: TARS, CNH, MRX, MT, INSW, VOD, DHT, NSIT, FRO, ITGR, HPQ, ING, SBLK, RPRX, JXN.

### OI_FADE — STOOD_DOWN (diary-only)

No watch list, no tradeable names. Ranking unchanged (`oi_rel_build` + persistence). Metric confirmed **net
call-minus-put** against `oi_build.py` per-day (AGX 09-02: 4,652 − 377 = 4,275), not the call-only read that has
sign-flipped prints before.

**The raw-vs-live ranking divergence is still total.** The raw `oi_net_5d` top-25 is EWZ/VIX/TLT/PCG/AMZN/IBIT/
SLV/INTC-style mega-cap and ETF beta and shares **zero** names with the relative-build survivors, whose raw
ranks are #87–#413 of 5,269. The historical raw-rank prior still grades a rule the engine does not run.

Four of eight survivors cut by the gate stack:

- **AGX — the headline data-integrity finding, and it reproduces exactly.** `catalyst_split`'s LIVE `>=` read
  counts the 09-02 print day itself as post-catalyst and returns **87.1%** → LIVE_BUILD (a crowd to fade). The
  strict `>` re-sum returns **679 of 5,688 = 11.9%**, below the 0.15 threshold → RESOLVED_PRE_PRINT (nothing to
  fade). **Opposite verdicts on identical rows.** The 09-02 print day alone is +4,275 of the +5,688 ten-day
  build — **75.2%** — an earnings-day options spike. Cut fail-closed.
- **FRVO — a scope gap, not a boundary bug.** 68% of its build lands on 09-01/09-02, immediately after the
  Fervo–Google 396MW geothermal PPA: a real, already-landed commercial catalyst. `catalyst_split` inspects
  **earnings only**, so it returned `no-cat` and the 7-gate stack saw nothing. Same class as the AZN M&A-rumor
  leak, now generalized beyond M&A.
- **SUNB** — earnings 2026-09-09 inside the hold. **STEP** — persistence 1.014, a single unexplained 09-02
  block rather than organic building.

Clean passes had the lane been live: DLB, RSI, SBLK (+JAN, with a near-floor OI base of 1,011 and an early
unwind tail, `last_call_net` −65). The deal-pinning gate found no cash-acquisition target among the eight and
remains **untested**.

> **Cross-lane contradiction** (noted, never netted — invariant #2): **SBLK** sits in this short-direction diary
> *and* in the MOM_LONG cohort at **100.1%** of its 52-week range on a fresh high made 09-04. Two orthogonal
> lanes point opposite ways on one name. Neither sizes.

---

## 3. Weekly Technicals — PRE-REGISTERED (0 points, NOT sized)

Previous Layer-3 figures lived in prose and could not be re-derived. **These are computed from code** — forward
**excess vs SPY** over the same weeks, cross-sectional, clustered by `wk_start` (every ticker in a week shares
one market shock). Script: `analyses/weekly/2026-W36/layer3.py` (archived with this report so the arms stay re-derivable); source `data/weekly_features.parquet`.

| Arm (predicate) | fwd-2wk excess vs rest | fwd-4wk excess vs rest | t_wk (2/4) |
|---|---|---|---|
| A `hammer_or_hanging` | +0.0003 vs +0.0020 (**−0.0017**) | −0.0030 vs +0.0052 (**−0.0082**) | +0.05 / −0.33 |
| B undercut+reclaim (`lower_low & close_pos≥.7`) | +0.0009 vs +0.0014 (−0.0005) | +0.0017 vs +0.0035 (−0.0018) | +0.15 / +0.17 |
| C `inside_week` | +0.0025 vs +0.0026 (−0.0001) | +0.0043 vs +0.0062 (−0.0019) | +0.73 / +0.82 |
| D `follow_through` | +0.0024 vs +0.0030 (−0.0006) | +0.0052 vs +0.0059 (−0.0007) | +0.90 / +1.59 |
| E `outside_week` | +0.0004 vs +0.0026 (−0.0023) | +0.0045 vs +0.0060 (−0.0016) | +0.09 / +0.78 |
| F `star_or_inverted` | +0.0050 vs +0.0014 (**+0.0036**) | +0.0022 vs +0.0049 (**−0.0027**) | +1.07 / +0.31 |

**Not one arm clears anything.** Every |t_wk| is under 1.6, and **five of six have a negative point estimate
against the rest of the panel at both horizons.** Arm F's sign flips between the two horizons — precisely the
instability PR-WT exists to reject.

The pointed result: **arm A — the hammer/hanging that all three indices printed this week, the most
eye-catching structure of the week — is the worst of the six at four weeks (−0.0082).** It also cannot fix its
own sign, because the panel tag does not distinguish a hammer (bullish, after a decline) from a hanging man
(bearish, after an advance), and SPY sits mid-range, 1.2% off its 08-10 high.

**PR-WT bar (≥2yr / ≥30 weekly obs per arm / cross-regime sign-stable / BH FDR 0.10): NOT MET, and not close.**
The weekly panel is **33 observations** (2026-01-19 → 2026-08-31), ~7.5 months. Nothing graduates. The
reversal-after-catalyst (NFP) arm is **not measurable at all** on this panel — it needs per-event conditioning
across a handful of NFP weeks — and accrues exactly one observation.

---

## 4. Carry-forward

**Last week (W35): no Layer-2 calls to grade** — `calls[]` was empty there too. The book has been flat 21
consecutive sessions and gained zero sized units for a third cycle.

**Open items into W37:**

1. **The 2026-09-05 audit is due today**, and its headline input has already fired. `OI_FADE_LIVE`'s
   pre-registered re-check reached **outcome 2** at 34 `lane-exit-day`: **−0.0065, p_iid=0.0929, Newey-West
   p=0.298 — no longer surviving BH(0.10)**, i.e. reverting to indistinguishable-from-zero. Per the
   pre-registration the lane **returns to advisory**. That is the audit's call to make; this review does not
   re-rate it and has not edited CLAUDE.md. Note the tension to resolve there: CLAUDE.md and the lane agent both
   still quote the stand-down figure (−0.93%, 29 `lane-exit-day`, p=0.028, surviving BH).
2. **Five matured OI_FADE call rows remain resolvable** (FDX/GEN/BSY/ITRI matured 08-28, AS 09-02).
3. **`hz_end` fails OPEN at the weekly horizon — newly quantified at h21, which is this command's own horizon.**
   `earnings_gate.py --horizon 21` printed its window as *"2026-09-05 .. 2026-10-04 (trading days)"*: it
   **starts on a Saturday and ends on a Sunday.** The true window is 2026-09-08 → **2026-10-06** (Labor Day,
   Mon 2026-09-07, is a market holiday inside it). The gate is **two sessions short** and blind to 10-05 and
   10-06. Measured shortfall from 2026-09-04: h3 −1d, h5 −2d, h10 −2d, **h21 −2d**. The docstring promises the
   opposite ("rounds outward... a day long rather than a day short"). **Non-binding this cycle** — every
   surviving name reports 11-03 or later, and SUNB (09-09) is blocked either way — but the weekly hold is
   exactly where this defect bites, and h21 had not been checked before.
4. **Forward event risk, 4-day week:** Labor Day Mon 09-07 (closed) · PPI Thu 09-10 · **CPI Fri 09-11** ·
   **FOMC Tue–Wed 09-15/16 with the dot plot** · PCE Wed 09-30 · NFP Fri 10-02. With Friday's print pushing
   September hike odds to ~63%, the 09-11 CPI and the 09-16 FOMC sit squarely inside a 2–4 week weekly hold.
5. **Dormant, not accruing** — do not re-derive until N moves: crash guard (20/103 guard-days, −0.58%,
   p=0.212; unchanged since 08-07, and no guard-day fired this week either) and the fundamentals veto (VETO
   n=15 −2.28%, CONFIRM n=23 −1.21%; unchanged since 08-15).
