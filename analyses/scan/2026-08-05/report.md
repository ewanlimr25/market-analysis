# Market Scan — 2026-08-05

## Regime & Verdict
- **Regime:** UPTREND/REBOUND-THRUST · ret5 **+5.530%** · ret10 +2.990% · dd15 −2.400%
- **Vol-state:** **VOL-ACCELERATION-PRONE — the dealer book FLIPPED since last night.** SPY GEX regime reads
  **NEGATIVE** (dealers net short gamma), spot 771.34 vs zero-gamma flip **775.97** — spot now sits *below*
  the flip. On 08-04 it was the reverse (spot 772.17 vs flip 767.91, long gamma). Spot barely moved; the
  **flip level rose 767.91 → 775.97** and crossed over it. QQQ GEX regime POSITIVE (long gamma) — sign
  trusted, but its printed `zero_gamma_level` 249.5 is an implausible artifact against per-strike data
  clustering at 698–720, so the level is not. VIX 15.81, falling steadily through the thrust
  (20.66 → 17.09 → 15.99 → 15.86 → 16.50 → 15.81).
- **Breadth:** 48.71% green on the day (245 adv / 257 dec), matching SPY's own −0.20% — no divergence.
  The **5-day thrust itself was BROAD**, not junk-led: 08-04 71.4% green (359/141), 08-03 67.6% green.
- `directional_tradable` = **TRUE** · `s1_standdown` = **TRUE** (leg a, ret5 +5.530% vs the +2.5% trigger —
  a **+3.03pp margin**, the most decisive firing of this streak; 1.61pp on 08-04, 0.0139pp on 08-03)
- **Bottom line: no directional edge today — ZERO new starters across all five lanes, and the vol book is
  EMPTY too.** Book was flat coming in and stays flat. This is the **sixth consecutive zero-starter session**
  — but tonight it is empty for a *different* reason than the previous five, which matters (below).

## Directional Book (excess-scored)

*(empty — no name in any lane reached a sizeable tier)*

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — |

### What changed tonight: OI_FADE stopped failing on mechanism

For five straight sessions (07-29 → 08-04) OI_FADE produced no starter because **every candidate died on a
mechanism gate** — single-day blocks, earnings, liquidity, ETPs. Tonight is the first session in the streak
where names **clear the entire mechanical stack**: `EXLS` and `UCTT` pass all seven mandatory gates plus the
catalyst-split check. Independently re-verified by the orchestrator rather than taken on the lane's word:

| Name | Liquidity | Earnings (h10) | rel_build | persistence | catalyst_split | issue_type |
|---|---|---|---|---|---|---|
| EXLS | PASS $33.68 / $88.8M ADV | PASS (reports 10-27) | 1.344 | 0.833 | LIVE — 91.2% of build post 07-28 print | Common Stock |
| UCTT | PASS $80.20 / $125.7M ADV | PASS (reports 10-27) | 1.109 | 0.591 | LIVE — 36.1% of build post 08-03 print | Common Stock |

**They are still not sized.** The block is now *regime*, not mechanism: the lane's Hard Rule #2 stands the
lane down on a REBOUND-THRUST, and tonight's label is literally `.../REBOUND-THRUST` with `s1_standdown=TRUE`
on the widest margin of the streak. Under a CHOP or PULLBACK tape either would be a legitimate starter at the
lane's baseline. Both go to **watch**, carrying a `long_caution` flag — they remain top relative-build names,
so they are not long candidates either.

### Why each lane is out

| Lane | Disposition | Binding reason (sourced) |
|---|---|---|
| **MOM_LONG** | BASKET_WATCH (78 names) | **Two independent bars, unchanged.** (1) Lane excess **+0.23% < +0.30%** starter bar, with median **−0.91%** — the mean is tail-carried. (2) `risk-sizer.md` bars this lane from starter sizing outright until a **DURABLE-N (≥30) forward window re-clears positive excess** via a `/calibration-audit` recommendation, not ad hoc. Sector concentration OK (Industrials 23.1%, inside the 1/3 cap). |
| **MOM_SHORT** | STOOD_DOWN | `s1_standdown` fired on a **+3.03pp margin** — the most decisive of the streak. Plus the invariant-#6 watch-only cap for new starters and a knowingly negative baseline (−0.0008). Triply out. Cohort corrected from 3 names to **2** (see data-quality note). |
| **OI_FADE** | NO_NAME_CLEARED | Sixth consecutive zero-starter, but **first one blocked by regime rather than mechanism.** EXLS + UCTT clean → watch. |
| **S2_dp_revert** | ADVISORY_WATCH (55 names) | **Advisory lane → watch** by the sizing map, regardless of measured excess. |
| **S4_pcr_fade** | ADVISORY_WATCH (57 names) | **Advisory lane → watch.** Still the only lane positive **forward** as well as historically (+0.51% hist). |

Sizing map (`risk-sizer.md:45`): `≥+1% & sign-stable → half` · `+0.3–1% → starter` ·
`< +0.3% **or advisory lane** → watch`. An advisory lane never sizes regardless of measured excess.

## Vol Book (non-directional)

**EMPTY tonight.** Delta-neutral, advisory, quoted net of cost. All three candidates stand aside:

| Symbol | Verdict | Reason |
|---|---|---|
| **SPY 0DTE** | STAND ASIDE | Dealers **short gamma** (CLI-verified) + VRP essentially **FAIR** (iv30d 13.46% vs realized 13.37%, +0.09pp). Fair gross VRP goes negative net of the half-spread before any premium for the short-gamma acceleration tail. Worst configuration for a 0DTE seller: no edge to pay for the tail. |
| **QQQ 0DTE** | STAND ASIDE | Gamma sign genuinely positive, but VRP is **NEGATIVE** — iv30d 22.01% vs realized 25.68%, **−3.67pp**. IV is *underpricing* realized: sellers are paid less than the vol that shows up, before costs. Plus NFP two trading days out. |
| **YELP earnings** | **CUT by orchestrator** | The lane proposed it as the one live trade (confirmed backwardation, front 76.9% / back 63.4%, ratio 1.212, 11.07% implied move into an 08-06 print). It **fails the liquidity floor: $-ADV $24.7M vs the $50M floor**, fail-closed, with only 192 contracts front-month OI. A defined-risk iron fly there pays the entire theoretical crush edge away in spread. The lane flagged the thin chain as a caveat; it is a floor breach, not a caveat. |

### `zerodte_setup.py` gamma-sign bug BIT tonight — fourth session, first actual miss
The three prior sessions recorded "script and CLI agreed, the bug did not bite." Tonight they **disagreed**:
the script emitted SPY as `GO_PREMIUM_SELL_INTRADAY` labelled *"long-gamma: quieter, mean-reverting"* while
`uw options-structure gex` reads **NEGATIVE / short gamma, "expect trend acceleration."** Per the standing
rule the CLI wins. **Absence of symptom was not a fix** — the bug produced a live premium-sell recommendation
into a short-gamma tape, which is exactly the documented failure. This should now be fixed, not just noted.

## Watch / Stood-down
- **OI_FADE watch:** EXLS, UCTT (mechanically clean, regime-blocked, `long_caution`)
- **MOM_SHORT watch (corrected):** FLUT (pct_range 1.4%), XPEV (pct_range 0.1%, low set today) — both
  Yahoo-verified genuine. **CCI CUT — false short.**
- **MOM_LONG basket watch (78):** top by proximity to 52w-high incl. ETN, JCI, NUE, SWK, PH, ITW
- **S2 advisory (55):** largest DP prints VZ ($580M), NXPI ($407M), ABT ($342M), TER ($298M), TFC ($195M)
- **S4 advisory (57):** highest PCR HGV (417.0), ITRI (332.4), XPO (103.2), EXR (90.7), TYL (39.0)
- **AZN — new failure mode, cut:** cleared liquidity, earnings and catalyst_split, but **81% of the 5-day
  call-OI build (+21,964 of +27,148) landed on 08-04, the same day as Bristol-Myers deal-talk headlines** —
  then −7.7% on the report and +6% today on a denial. That is binary M&A-headline risk driving the OI, not
  organic crowded conviction. Cut under the merger-arb gate's spirit (pre-announcement rumor, not a signed
  deal). **The 7-gate checklist does not currently catch this class** — worth adding.

## Risk
- **Event calendar inside the horizon:** **NFP 2026-08-07 (2 trading days out)**, then **CPI 08-12** and
  **PPI 08-13** back-to-back. Nothing directional is open, so this binds only anything opened from here.
- **Correlation clusters:** not applicable — zero positions.
- **Tail caps applied:** none needed (nothing sized).
- **Hedge note:** flat book into a short-gamma index tape with Tier-1 macro in 2 sessions. Being flat *is*
  the hedge; no overlay warranted.
- **Under-the-surface caution (advisory):** `uw risk market-regime` reads TRANSITIONAL — only 35.6% of
  optionable names carry bullish flow (2,234 bullish vs 4,046 bearish), with rotation *out* of
  Technology/Industrials/Consumer Cyclical and *into* Utilities/Consumer Defensive. Flow ≠ price and this
  does **not** override the price-based UPTREND label, but a defensive rotation under a broad up-tape is
  worth carrying into the next session.

## Regression gate — GREEN (proved, not assumed)
`retro_harness.py --all` on the freshly rebuilt 81-day panel shows **every lane below its recorded baseline**,
which reads as a five-lane simultaneous decay. It is not. Both invariant-#6 isolation checks pass:

| Lane | Baseline (08-01, 78d) | Pooled now (81d) | **Baseline-maturity cohort** |
|---|---|---|---|
| MOM_LONG | +0.0023 | +0.0013 | **+0.0023** ✓ (n=483 ✓) |
| MOM_SHORT | −0.0008 | −0.0020 | **−0.0008** ✓ (n=317 ✓) |
| OI_FADE | +0.0071 | +0.0063 | **+0.0071** ✓ (n=979 ✓) |
| S2 | +0.0021 | +0.0008 | **+0.0021** ✓ (n=523 ✓) |
| S4 | +0.0051 | +0.0044 | **+0.0051** ✓ (n=370 ✓) |

- **(a) old code, new data:** stronger than the usual check this time — `retro_harness.py`, `_regime.py` and
  `_calendar.py` are **byte-identical** to baseline commit `374b20d` (verified by diff). HEAD `de91fe9`
  touched only agent/command markdown, `CLAUDE.md` and the schema — **no Python at all**. The code that
  produced the baseline is the code that ran tonight.
- **(b) maturity-edge cohort split:** rows matured at the 07-31 edge reproduce **all five lanes and all five
  n's exactly**. Artifact: `analyses/audit/2026-08-05/harness_split.{py,out}`.
- **The 109-row increment is ONE clustered event, not 109 independent observations.** Its base-rate column
  reads **1.00 for every long lane and 0.00 for every short lane** — i.e. the conditional benchmark was up on
  essentially every resolution window in the increment. That is a single homogeneous up-window: the same rip
  that set `s1_standdown` tonight. Reading it as five lanes decaying at once is precisely the clustering trap
  the calibration skill warns about.

## Process findings
1. **MOM_SHORT's "Yahoo Verified" column was not Yahoo data.** The lane reported closes of CCI $30.18,
   FLUT $18.65, XPEV $20.13 and marked all three verified. Actual chart-API closes: **$73.84, $92.91,
   $11.75**. Re-verification changes the cohort: FLUT (pct_range 1.4%) and XPEV (0.1%) are genuine near-lows,
   but **CCI sits 11.2% up its 52-week range — a false short** that the lane's own ≤2% criterion excludes.
   Caught by the standing rule to re-run a lane's reported gate result rather than trust it. No live harm
   (lane is stood down), but the verification step itself is unreliable and needs hardening.
2. **S2's liquidity claim held up.** It reported 0/99 failures against the $50M floor, which looked
   implausible; spot-checking its own micro-cap flags (TAL $12.09/$56.5M, NWL $6.17/$65.2M, plus DNTH, SPHR,
   GTES) confirmed all genuinely pass. Reported correctly.
3. **`prices.parquet` coverage gap unchanged and still material** — `build_prices.py` wrote 783 of a
   universe frozen at 785 symbols while `features.parquet` spans 2,466 tickers. **211 screened names
   fail-closed tonight (207 of 285 MOM_LONG candidates = 73%, plus 4 MOM_SHORT).** The correlation/coverage
   check returns nothing for absentees, which *looks* like a pass. Basket composition is clean but **not
   complete**.
4. **Possible ETP leak in the harness universe:** `SPCX` appears in the MOM_SHORT increment rows and is its
   largest positive contributor (+0.0654, +0.0906). The screener classifies it `Common Stock`, so the
   `issue_type` filter passes it legitimately — but the name is a space/SPAC thematic vehicle. Worth checking
   whether `issue_type` alone is sufficient hygiene for the harness universe.
5. **`zerodte_setup.py` bug is now demonstrated live, not theoretical** (see vol book). Fix it.
