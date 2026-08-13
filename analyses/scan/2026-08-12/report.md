# Market Scan — 2026-08-12

## Regime & Verdict

- **Regime: UPTREND** · ret5 +0.350% · ret10 +5.900% · dd15 +0.000% · VIX 14.55 (LOW tercile, contango)
  · breadth 51.9% green vs 33.9% bullish flow (**~18pt divergence**) · `directional_tradable=true` · `s1_standdown=false`
- **Bottom line: no directional edge tonight. Book stays FLAT for a third session.** Two OI_FADE names
  (COO, NRG) cleared the full mechanical stack and are held at WATCH — each overdetermined by
  independently-sufficient gates. Vol book stands aside on 0DTE.

### The label is right; the story behind it is not what it looks like

The mechanical read is UPTREND and it is correct. The qualitative overlay is the opposite of a breakout,
and tonight a Phase-A read got this backwards in a way worth recording:

- **`dd15 = 0.000%` does not mean "at the highs."** Per [`scripts/_regime.py:13`](../../../scripts/_regime.py)
  it is `min(last 15 closes) / close_10_sessions_back - 1` — explicitly **not** a peak-to-trough drawdown,
  with a docstring warning that a peak-based re-derivation "silently changes which arm of the crash guard
  fires." It reads 0 here because the window **low** (729.46, 07-29) **is** the 10-session anchor. So
  ret10 +5.9% is a **trough-anchored rebound measurement**, not a continuation measurement.
- **Today is not a fresh high.** 772.49 is the **3rd-highest** of the last 15 closes, −0.10% under the
  08-07 max (773.26). Not a fresh intraday high either (774.87 vs 776.85 on 08-05).
- **The CPI print was faded.** Opened 774.71 (the day's high), closed 772.49 at **34% of the day's range**,
  −0.29% from the open. Up +0.25% vs the prior close, but the gap was given back.
- **Four-session stall:** 773.26 → 773.03 → 770.56 → 772.49.

So: the V-rebound off the 07-29 trough completed by 08-07 and the tape has gone nowhere for four sessions,
fading a benign macro print, on ~18pt price/flow breadth divergence, defensive rotation, SPY dealer **short**
gamma (spot below the 779.01 flip), with VIX at the bottom of its 90-day range. Treated as
**regime-transitional**, same as 08-11. The P0.6 out-of-regime half-cap **binds** — non-binding in practice
only because nothing reached a sizing band.

### The label will flip on its own inside the horizon

`ret10` is anchored on the 07-29 trough. As that rolls out of the window, **flat price alone** re-labels the tape:

| session | anchor (c10) | ret10 if SPY holds 772.49 | label |
|---|---|---|---|
| 08-13 | 07-30 741.69 | +4.15% | UPTREND |
| 08-14 | 07-31 747.03 | +3.41% | UPTREND |
| 08-17 | 08-03 757.67 | +1.96% | UPTREND |
| **08-18** | 08-04 771.33 | **+0.15%** | **CHOP** |
| 08-19 | 08-05 769.79 | +0.35% | CHOP |

Anything entered tonight at h10 is scored under a regime that will not survive its own holding period.

## Directional Book (excess-scored)

**EMPTY — zero new starters, zero open positions carried.** Prior book confirmed genuinely flat
(`conviction_2026-08-11.json` records a positive zero-count, not the held-book EXIT-substring bug).

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates that bound |
|---|---|---|---|---|---|---|---|---|
| COO | OI_FADE | short | h10 | +0.59% base → **<+0.3% adj** | 0.40 | **WATCH** | close > **$77.42** (confirmed) | selection-rule discount · fundamentals CAUTION · event-risk — **3 independently sufficient** |
| NRG | OI_FADE | short | h10 | +0.59% base → **≈+0.30–0.35% adj** | 0.35 | **WATCH** | close > **$124.71** (confirmed) | fundamentals CAUTION · event-risk — **2 independently sufficient** |

### Why the lane prior is discounted tonight — a standing methodological gap

The live lane ranks candidates by **`rel_build`** (build relative to the name's own base). The harness that
produced the **+0.59% mean / n=1087** baseline selects **top-15 by *raw* `oi_net_5d`** with only
liquidity/earnings/ETP gates — no persistence, `catalyst_split`, or `rel_build` filter at all
([`retro_harness.py:82-99`](../../../scripts/retro_harness.py)).

All five candidates pass every harness gate. But on tonight's raw-ranked list of **1,359** gated names they sit at:

| name | raw rank | | name | raw rank |
|---|---|---|---|---|
| NXPI | 28 | | EWTX | 145 |
| NRG | **29** | | USFD | 158 |
| UTHR | 127 | | **COO** | **192** |

The top-15 cutoff tonight is 19,000 (TTD). *(The lane's 5-day **sum** and features' `oi_net_5d` are the same
metric exactly 5× apart — mean vs sum — so ranking is preserved. This is a selection-rule difference, not a
data bug.)* The harness's own top-15 is dominated by mega-cap and crypto-beta names (SPCX, MSTR, PCG, DKNG,
META, AAPL, MARA, TSLA, NFLX, AMZN…) — the "raw = mega-cap beta short" artifact the relative screen exists
to avoid.

**Consequence:** the +0.59% prior is being **borrowed for a differently-ranked population, not measured for
this selection rule.** NRG (rank 29) retains most of the claim; COO (rank 192, ~13× outside the measured
population) is **effectively unvalidated for this selection rule** — sufficient on its own to cap it at WATCH.
This is a standing gap between the live lane and the instrument that grades it, not a tonight-only issue.

### Candidate detail

- **COO** $76.73 · $-ADV $149.3M · Common Stock · Healthcare/Medical Instruments. 5d net call-OI build
  +5,497, `rel_build` 1.115, **persistence 0.733** (organic; positive net three straight sessions — the
  distributed shape is genuine). Earnings gate PASS (next print 09-09). `catalyst_split`
  NO_CATALYST_IN_WINDOW — the 08-26 date was a stale preliminary estimate; the current field has been
  stable at 09-09 since 08-05. **3rd consecutive WATCH night** (08-10, 08-11, 08-12).
  - **Invalidation corrected tonight.** Last night carried "~$80.50." Verified against OHLC: COO's max high
    since 06-01 is **$77.42**; the $84 area is from **February 2026**, six months stale. An $80.50 stop sat
    ~4.9% above spot with no anchor in recent structure. Operative level is the confirmed **$77.42** (08-11
    high), ~0.9% above spot.
  - **Fundamentals CAUTION (−1), flagged ELEVATED / borderline-VETO.** 2 of 3 mechanical legs contradict the
    short with *hard first-party evidence*: a 4-for-4 EPS beat streak and insider net **buying** (MSPR
    +40.33, real dollar purchases). Only growth confirms (−42.61% YoY EPS on 63× P/E). D/E 0.3041 —
    genuinely low, and here the `leverage_flag` is **correct**. The UBS Neutral $75 PT carried from
    08-10/08-11 was **not** re-verified tonight; treat as unconfirmed.
- **NRG** $120.66 · $-ADV $379.1M · Common Stock · Utilities/IPP. 5d net +49,909, `rel_build` 0.604 (down
  from 0.835 — **mechanical**, the large 08-05 session rolled out of the trailing window; not an unwind),
  **persistence 0.419 — the cleanest, most-distributed build tonight.** Earnings gate PASS (next print
  11-05). `catalyst_split`: 08-04 print confirmed; shipped `>=` 74.2% vs **strict `>` 81.3%** — the strict
  boundary *raises* the post-catalyst share, so the known print-day defect **strengthens** this read (the
  opposite of EWTX). News tape tonight: *"Red-Hot Power Stocks Are Losing Steam"* — sector rotation out,
  supports the fade. Invalidation **$124.71** confirmed (08-05 swing high), ~3.4% above spot. 2nd WATCH night.
  - **Fundamentals CAUTION (−1), but a structurally weaker contradiction than COO's.** Insider **selling**
    (MSPR −60.91) and a two-quarter miss trend both *confirm* the short; only growth contradicts. The
    loud-looking 62–75% analyst-target gap is sell-side opinion whose targets were just **cut** post-gap
    (Scotiabank $226→$211, Evercore $215→$195) — bulls marking down conviction, against insiders selling
    into the same catalyst stack. **D/E 9.78 is genuinely HIGH** — the `finnhub_enrich` `leverage_flag`
    "low" is the known bug reproducing.
  - This **inverts last night's asymmetry note**, which read NRG's CAUTION as the louder of the two. On
    first-party evidence COO is the more dangerous short; NRG's contradiction is a single soft leg amplified
    by a sell-side narrative that is itself losing conviction.

### Killed upstream

- **USFD** (persistence **1.053**), **NXPI** (**1.022**), **UTHR** (**1.057**) — all exceed the 0.85 ceiling
  that [`oi_build.py:145`](../../../scripts/oi_build.py) itself flags as *"likely a single-day block, not
  organic building."* The lane had ranked USFD #1 and NXPI #2 by `rel_build`; demoted. Name-specific notes:
  USFD's price has risen every session since its print (crowd validated, not faded, no confirmed resistance
  above spot); NXPI's single 08-07 block is of unconfirmed origin (possibly an institutional roll); UTHR is
  already −5.0% off its 08-07 post-print high, so much of the fade may be realized.
- **EWTX — CUT.** Repeat of the 2026-08-10 boundary artifact: shipped `>=` reads **85.3%** LIVE, strict `>`
  reads **15.6%** — the build is almost entirely the print day. Do not re-propose.

## Vol Book (non-directional)

- **0DTE-VRP — STAND ASIDE, both SPY and QQQ.** Two independent vetoes.
  - The LOW-VIX **conditional** net is negative once cost is charged: **SPY −0.095%/day**, **QQQ −0.037%/day**
    (gross 0.005% / 0.063% less 0.10% round-trip). The pooled headline (+0.13% / +0.25%) is *not* the
    governing number — VIX 14.55 puts us squarely in the LOW tercile, which is exactly the pooling trap.
  - Gamma gate vetoes independently: SPY dealers **short gamma** (spot 772.82 < flip 779.01), a
    trend-acceleration regime this sleeve's unsampled left tail cannot survive. QQQ sits *at* its flip
    (724.04 vs 723.64) with the CLI and the local flip level disagreeing — regime not reliably known, so
    fail closed.
- **Earnings IV-crush — 2 structural qualifiers, neither sized.**
  - **TPR** — IV-rank 87.7, front IV 165.6% (2DTE) vs back-month 52.9%, backwardation **3.13**. Defined-risk
    iron fly, wings set beyond the **~12.2% raw-IV** move rather than the 8.4% headline (TPR gaps hard).
  - **LOW** — IV-rank 83.2, backwardation 1.16 (weakest of the survivors), tightest execution. Size smaller.
  - **QFIN / MRCY** excluded — 33 and 41 front-expiry contracts, spreads would eat the crush edge.
  - **No per-name net-of-cost backtest exists for this lane.** Structural qualification only; the vol-short
    tail cap requires a net-of-cost quote, so neither sizes tonight. Net expectancy must be verified against
    the live iron-fly credit at entry.

## Watch / Stood-down

- **MOM_SHORT — BASKET_WATCH, 10 names:** APP, ACM, RBA, GME, ROL, AMRZ, VICI, NKE, WING, STLA. All
  Yahoo-verified as genuine near-52w-lows (the `pct_52w_range` artifact breaks both ways and the in-range
  class manufactures false shorts), all liquidity/earnings/ETP gated. `s1_standdown=false`, so the crash
  guard is *not* what caps this — invariant #6 does (baseline −0.0128, n=803, knowingly negative).
  **GPI** and **HDB** excluded on prior blocking verdicts.
- **MOM_LONG — BASKET_WATCH, 50 names** (top-10 spot-verified). Baseline −0.0108, n=1066. DURABLE-N bar
  unmet; basket-only, never sizes.
- **S2 (advisory, +0.09%, n=1123) — 15 names fully news-verified**, out of 80 that cleared
  liquidity/earnings: WFC, WDAY, FICO, SU, APO, CG, DBX, FISV, HBM, LBRDK, RY, MAR, TOST, NSC, MDLZ.
  **AVB VETOED** (AVB-EQR merger shareholder vote *same day*) and **BAH VETOED** (Treasury contract
  cancellation, −1 day). NTRA/RBLX/ROKU flagged. **The other 60 names stay excluded, fail-closed** — last
  night this lane shipped 80 names with an incomplete news gate; tonight it was cut to what could actually
  be verified.
- **S4 (advisory, +0.35%, n=1145) — 27 names post-gate**, led by PPL, EFX, JXN, IMAX, COKE, LEN, IRM.
  Separate **orthogonal** `ivrank_chg_5d` h3 tilt (10 names: BSP, TBIL, ASO, WKC, VOD, DVY, NI, CHWY, KR,
  EWH) — reported alongside, **never summed** with the PCR signal.

## Regression gate (`retro_harness.py --all`, run tonight)

No lane or threshold changed tonight — but the truth set was **rebuilt and extended** (83 → 86 panel days),
so the gate was run to see where the baselines now sit.

| lane | baseline (83d, 2026-08-08) | tonight (86d) | Δ | n |
|---|---|---|---|---|
| MOM_LONG | −0.0108 (n=1066) | −0.0119 (n=1091) | −0.0011 | +25 |
| MOM_SHORT | −0.0128 (n=803) | −0.0136 (n=813) | −0.0008 | +10 |
| **OI_FADE** | **+0.0059 (n=1087)** | **+0.0039 (n=1132)** | **−0.0020** | **+45** |
| S2_dp_revert | +0.0009 (n=1123) | +0.0008 (n=1154) | −0.0001 | +31 |
| S4_pcr_fade | +0.0035 (n=1145) | +0.0048 (n=1169) | +0.0013 | +24 |

**Verdict: NOT a regression.** Four of five lanes sit marginally below their recorded baseline, but zero code
changed tonight — the only input that moved is the panel, which grew three days with n rising across every
lane. That is the textbook data-drift case the gate explicitly does not treat as a failure. The gate exists
to catch *code* changes that degrade a lane; there was none to catch.

**But OI_FADE's softening is material to tonight's call.** −34% relative (+0.59% → +0.39%) on 45 new
observations is the largest move of any lane. The lane's *structure* is intact — hit-minus-base is
essentially unchanged (+0.172 vs the recorded +0.17) and the median stays positive (+0.0081 vs +0.0095) — so
this reads as the mean softening, not the edge inverting. The consequence compounds with the selection-rule
finding above: the prior cited for COO and NRG was **already** being borrowed from a differently-ranked
population, and now the prior itself measures ~a third lower on its own basis. Citing "+0.59%" tonight was
generous. This strengthens, not weakens, the decision to hold both at WATCH.

## Risk

- **Event stack inside the h10 window (08-13 → 08-27):** **PPI 08-13**, **Retail Sales 08-14**, FOMC minutes
  08-19. CPI cleared today, but two Tier-1 prints land within two sessions — independently sufficient for
  −1 tier on both OI_FADE names, exactly as on 08-11.
- **Correlation:** COO/NRG verified as distinct singletons — **measured** pairwise correlation **0.127**
  (n=141 paired days) against the 0.70 threshold, computed rather than inferred from sector labels. Both had
  full price history, so this is a real pass, not the absentee-reads-as-pass trap.
- **Tail:** dealer short gamma + bottom-tercile VIX is a larger-realized-move environment, which raises the
  cost of being wrong on either short. Noted as a risk, **not** invented as a sizing gate — OI_FADE has no
  named tail cap in the ruleset.
- **Half-cap, no auto-full.** Nothing sized tonight at any level; neither name would have exceeded starter
  even absent every downgrade.

## Orchestrator notes / action items

1. **Phase-A `dd15` misread — recorded so it is not repeated.** The regime agent read `dd15 = 0.000%` as
   "today is the 15-day high" and built a "fundamentally-anchored breakout, genuine trend-continuation"
   conclusion on it, twice asserting a fresh high. OHLC says 3rd-highest close, −0.10% below the 08-07 max.
   This is the exact failure the `_regime.py` docstring warns about. The corrected read (trough-anchored
   rebound, stalled, faded the print) points the opposite way and matches the agent's *own* breadth/rotation
   caveats. **Any figure a lane hands back that carries a directional conclusion needs arbitration against
   the source definition, not just against `regime_check.py`'s numbers** — the numbers here were right; the
   *interpretation* was not, and `--claim-label/--claim-ret10` would not have caught it.
2. **Lane/harness selection-rule mismatch (standing).** Live lane ranks by `rel_build`; the harness baseline
   is top-15 by raw `oi_net_5d`. Candidates at raw rank 29–192 of 1,359 are borrowing a prior measured on a
   different population. This is the ranking-metric sibling of the known "patch the lane, not the harness"
   defect. Worth a maintenance decision: either add the live lane's persistence/`catalyst_split`/`rel_build`
   screens to the harness and re-baseline, or record explicitly that the live lane's prior is inherited
   rather than measured. Any change must clear `retro_harness.py --all` first.
3. **COO invalidation was stale, not merely loose.** "~$80.50" had no anchor in six months of price. Carried
   references should be re-verified against OHLC before reuse — the corrected $77.42 sits ~0.9% above spot,
   which is a materially different trade.
4. **`finnhub_enrich.py` `leverage_flag` bug reproduced again** on NRG (D/E 9.78 reported "low"); it read
   *correctly* on COO (D/E 0.30). So it is not uniformly broken — it mislabels the high end specifically.
   Still needs a fix; until then override by hand on any high-D/E name.
5. **`fz` CLI exposes no Recom/Target Price/Short Float fields** — confirmed again by direct probe on both
   names, in both `--agent` and full `--json` modes. Analyst targets cited tonight came from Finnhub news
   headlines and are attributed as such.
6. **Next `/calibration-audit` due 2026-08-15** per cadence. 41 open rows (17 OI_FADE, 12 MOM_SHORT, 11 S4)
   mature 08-10→08-21; the 08-03→08-07 crash-guard block matures 08-18→08-22 — the first cohort spanning
   non-overlapping windows. Count distinct **exit-days**, not rows.
7. **Watch tomorrow:** whether COO's build stays distributed (persistence has run 0.659 → 0.733) or tips
   into single-day-block territory, and whether NRG's `rel_build` keeps decaying mechanically as older
   sessions roll out.
