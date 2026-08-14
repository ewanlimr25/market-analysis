# Market Scan — 2026-08-13

## Regime & Verdict

- **Regime: UPTREND** · ret5 +1.210% · ret10 +4.880% · dd15 −1.650% · VIX 14.63 (LOW tercile, contango)
  · breadth 63.4% green vs 35% bullish flow (**28.4pt divergence**) · `directional_tradable=true` · `s1_standdown=false`
- **Bottom line: no directional edge tonight. Book stays FLAT for a fourth session.** One name (NRG) is
  carried at WATCH. **COO is CUT after four nights** — the lane's own invalidation signal fired. Vol book
  stands aside on 0DTE.

### Tonight the breakout is real — and that is the opposite of last night's finding

On 08-12 the mechanical label read UPTREND off a **trough-anchored rebound** and a Phase-A agent misread
`dd15 = 0` as "at the highs." Tonight the same label is backed by actual structure, and the distinction is
worth stating explicitly so the correction doesn't get over-applied:

- **SPY 777.88, +0.70% — a genuine fresh 52-week high**, both the highest close of the window and a new
  intraday high (779.37 vs the prior 776.85 on 08-05). Verified against OHLC, not inferred from `dd15`.
- **The four-session stall broke.** 773.26 → 773.03 → 770.56 → 772.49 → **777.88**.
- **The PPI print was bought, not faded.** July final demand came in flat MoM (below +0.2% consensus),
  4.7% YoY; the tape opened near the prior close and ran to a new high. On 08-12 the in-line CPI was
  *faded* (closed at 34% of the day's range). That is a real behavioural change across two sessions.
- `dd15` is now −1.650%, read correctly per [`scripts/_regime.py:13`](../../../scripts/_regime.py) as
  `min(last 15 closes) / close_10_sessions_back − 1` — **not** a peak-to-trough drawdown.

The regime claim was arbitrated against the panel (`regime_check.py --claim-label UPTREND --claim-ret10
0.0488`, exit 0).

### Three things argue against reading the breakout as risk-on confirmation

1. **The price/flow breadth divergence WIDENED to 28.4pt** (price 63.4% green vs options-flow 35% bullish),
   from ~18pt on both 08-11 and 08-12. Price breadth surged; bullish options positioning did not follow.
2. **QQQ did not confirm.** It ran harder on rate-of-change (ret5 +2.44%, ret10 +7.10% vs SPY's +1.21% /
   +4.88%) but is still **−2.2% below its own 06-03 high** (748.65). The index leading the tape has not made
   a new high.
3. **The regime mechanically expires inside the holding period** (below).

### The label flips to CHOP on 08-18 — on flat price, again

`ret10`'s anchor rolls onto the **08-04 CPI-gap close** (771.33, the largest one-day jump in the window):

| session | anchor (c10) | ret10 if SPY holds 777.88 | label | needs > X to hold UPTREND |
|---|---|---|---|---|
| 08-14 | 07-31 747.03 | +4.130% | UPTREND | 758.24 |
| 08-17 | 08-03 757.67 | +2.667% | UPTREND | 769.04 |
| **08-18** | **08-04 771.33** | **+0.849%** | **CHOP** | **782.90** |
| 08-19 | 08-05 769.79 | +1.051% | CHOP | 781.34 |
| 08-20 | 08-06 768.56 | +1.213% | CHOP | 780.09 |
| 08-21 | 08-07 773.26 | +0.597% | CHOP | 784.86 |

Same conclusion as 08-12 by a different mechanism (a peak-gap anchor rolling *in* rather than a trough
anchor rolling *out*): **anything entered tonight at h10 spends most of its life graded under CHOP.**

## Directional Book (excess-scored)

**EMPTY of new starters — 0 open positions carried, 0 opened.** Prior book verified flat two ways
(`held_book.py` on `conviction_2026-08-12.json` returned 0 open, and that file's own `book_state` records 0
positions — not the known EXIT-substring false-empty).

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates that bound |
|---|---|---|---|---|---|---|---|---|
| NRG | OI_FADE | short | h10 | +0.59% base → **≈+0.30% adj** | 0.35 | **WATCH** (3rd night) | close > **$124.71** (confirmed) | selection-rule discount · fundamentals CAUTION (carried, not re-verified) · event-risk |

### COO — CUT after four nights at WATCH

The lane's **own mechanical invalidation fired**. `oi_build.py` printed its documented flag:

```
COO  net_5d=+5,415 (call +5,719 / put +304)  rel_build=1.034  persistence=0.744
     2026-08-13  call      -4  put     +65  net     -69
   ** last call_net NEGATIVE -- calls genuinely closing (OI_FADE invalidation)
```

Verified directly by the orchestrator, not taken from the lane's summary. The precondition of the fade —
a crowd still building calls — no longer holds. Four independently sufficient reasons, and they now point
the same way:

- **The build is unwinding** (above). This is new tonight and is on its own decisive.
- **Structurally it was never distributed:** 74% of the 5-day net landed in one session (08-11, +4,028 of
  +5,415), with persistence drifting 0.659 → 0.733 → **0.744** toward the 0.85 single-day-block ceiling.
- **Selection-rule discount:** raw `oi_net_5d` rank **195 of 1,430**, against a harness top-15 cutoff of
  21,642 (NFLX). COO sits ~13× outside the population the +0.59% prior was measured on.
- **Price rejected at, but poked through, the invalidation intraday** — high $77.63 against the standing
  $77.42 level, closing back below at $76.60. The level itself would have needed re-pinning to $77.63.

Counterweight, weighed and judged insufficient: **Healthcare flipped to rotation-OUT tonight** (−$34.7M,
having been rotation-IN on 08-12), which is a genuine new tailwind for a healthcare short. A sector tailwind
does not resurrect a signal whose mechanical basis has expired.

**Do not re-propose COO on the current build.**

### NRG — WATCH, 3rd night, decaying on schedule

$119.75 · $-ADV $380.2M · Common Stock · Utilities/IPP. `rel_build` continues its **mechanical** decline
0.835 → 0.604 → **0.424** as the 08-10/08-11 print-week sessions age out of the trailing window — verified
as window mechanics, not an unwind. Persistence **0.574**, the cleanest shape in the cohort. Today's fresh
add is **+89 contracts** — effectively nothing. `catalyst_split` stays strongly LIVE under both boundaries
(**97.3% shipped `>=` / 106.5% strict `>`**; the print-day net was itself negative, so the known boundary
defect *strengthens* this read, as on 08-12). Raw rank **41/1,430** — best of the cohort, still outside the
measured top-15. Invalidation **$124.71** confirmed, ~4.1% above spot; today's high was 122.07, no breach.

Expect it to roll off the candidate list within 1–2 sessions as the driving days exit the window.
**Fundamentals CAUTION is carried from 08-12 and was NOT re-verified tonight** — flagged, not restated as fresh.

### WEC — new name, not admitted to watch

$110.28 · $-ADV $247.6M. Passes every hard gate but is withheld on the combination: persistence **0.814**
is under the 0.85 ceiling only because the build spans two sessions rather than one (**08-12 alone is 81%**
of it: +4,382 of +5,386); raw rank **197/1,430**, weakest of the cohort; **ex-dividend tomorrow (08-14)**, a
corporate-calendar confound that can mechanically explain a call build; and the OI is chasing a live bounce
off a two-week low (105.48 → 110.28) rather than fading an exhausted advance — the inverse of the lane's
validated pattern. No single gate is fatal; a fresh name does not get the benefit of the doubt an
established watch name gets.

### Killed upstream

- **NXPI (persistence 0.983), USFD (0.992), UTHR (1.030)** — demoted again on the 0.85 ceiling
  ([`oi_build.py:145`](../../../scripts/oi_build.py) flags these as "likely a single-day block, not organic
  building"). All three are driven by the **same 2026-08-07 session**, which rolls out of the window
  tomorrow. USFD's and UTHR's `catalyst_split` reads land at 100–107% because their print-day net was
  itself negative — that is the arithmetic of the ratio, not a signal of strength.
- **EWTX** — remains CUT from 08-12 (print-day boundary artifact). Not re-proposed.
- **15 of 20** `rel_build`-ranked names died at the liquidity floor (sub-$50M ADV or sub-$5).

## Vol Book (non-directional)

- **0DTE-VRP — STAND ASIDE, both SPY and QQQ.** VIX 14.63 is again squarely in the **LOW tercile**
  (bounds 16.2 / 17.7), which is exactly the `zerodte_setup.py` pooling trap. The governing conditional
  numbers, net of ~0.10% round-trip:
  - **SPY −0.089%/day** (gross +0.011%) · **QQQ −0.014%/day** (gross +0.086%)
  - Pooled headlines (+0.126% / +0.247%) do **not** govern and are recorded only to show the gap.
  - **Gamma state changed tonight and is worth recording:** SPY dealers flipped to **POSITIVE / long
    gamma** (spot 777.74 > ZGL 774.76), reversing 08-12's short-gamma state — verified independently by the
    orchestrator via `uw options-structure gex`. That is vol-suppressive, and it removes the *second*
    veto SPY carried last night. **The sleeve still stands aside purely on net-of-cost economics.**
  - **QQQ fails closed on a source disagreement, same as 08-12.** The `gex` endpoint returns
    `zero_gamma_level 211.28` against spot 732.33 — a plainly broken calculation. (The vol lane reported a
    clean flip at 729.24 from a different source and declared no disagreement; arbitrated against the
    endpoint, the disagreement is real.) Decision unchanged either way — VRP economics veto independently.
- **Earnings IV-crush — LOW, ROST, TJX structurally qualify. None sizes.**
  | name | earnings | IV-rank | real backwardation (median-IV) | liquidity on bracketing expiry |
  |---|---|---|---|---|
  | LOW | 08-19 | 81.0 | ~1.53 (55.0% vs 35.9%) | 258 prints / 796 contracts / 25 strikes |
  | ROST | 08-20 | 93.6 | ~1.55 (58.9% vs 38.0%) | 115 prints / 313 contracts / 30 strikes |
  | TJX | 08-19 | 80.1 | ~1.47 (39.8% vs 27.1%) | 297 prints / 1,622 contracts / 22 strikes |
  - **The CLI's headline backwardation and `implied_move_perc` fields are both unusable here.** Headline
    front-end ratios (LOW 3.77, ROST 4.64) are dominated by size-1 prints on deep-ITM strikes reading up to
    450% IV; the size-weighted/median figures above are the real ones. Headline implied moves
    (LOW 1.18%, ROST 0.67%) are reading the wrong expiry — size wings off the raw straddle
    (LOW ATM 08-21 ≈ **5.7%**; ROST ≈ **13.9%**), never the headline.
  - **BZ, FLNG, YRD excluded** on option liquidity (zero / 35 prints / no listed expiries) — the same floor
    that cut QFIN and MRCY on 08-12.

### TPR resolved today, and it is live evidence for the no-size rule

TPR was **last night's top structural qualifier**, with wings recommended beyond the ~12.2% raw-IV move
rather than the 8.4% headline. It reported today:

**153.74 → open 132.70 (−13.7%) → close 128.39 (−16.5%), low 127.78 (−16.9%).**

The realized move **blew through even the widened raw-IV wing.** Nothing was sized, so nothing was lost —
which is the point. This is direct, same-week evidence that (a) the standing "no size without a per-name
net-of-cost quote" rule is doing real work, and (b) the raw-IV move estimate is itself **not** a
conservative wing on a gap-prone name. Carry this into LOW/ROST/TJX wing guidance.

## Watch / Stood-down

- **MOM_SHORT — BASKET_WATCH, 6 names:** AMRZ, LII, AGCO, GME, RBA, ROL. Down from 10 on 08-12. The screen
  is `close ≤ 1.02 × w52l`; the orchestrator re-derived it and independently verified all twelve candidate
  `w52l` values against Yahoo (they match to the cent). **The basket is correct and reproducible** — see the
  process note below, because the lane itself briefly claimed otherwise. Dropped tonight: WING (1.031×),
  STLA (1.023×), APP (1.031×), NKE (1.031×), ACM (1.044×), VICI (1.020×) — all genuinely near their lows but
  outside a 2% proximity screen. Sector: 50% Industrials, 33% Consumer Cyclical. **GPI** and **HDB** remain
  excluded on prior verdicts. Capped watch-only by **invariant #6** (baseline −0.0128, measured −0.0133
  n=816) — *not* by the regime, since `s1_standdown=false`.
- **MOM_LONG — BASKET_WATCH, 283 names**, expanded mechanically because SPY made a new high. Baseline
  −0.0108, measured −0.0124 (n=1104). DURABLE-N unmet; basket-only, never sizes. Sector concentration
  within the ⅓ cap (Financials 26.5%, Healthcare 19.1%, Tech 14.1%). Three of the top-15 (S, RBRK, P) carry
  earnings inside h10.
- **S2 (advisory, +0.0009, n=1163) — 3 names: HBM, RY, SU.** From 152 candidates: 55 dropped on
  issue-type/price, 13 on liquidity, 1 on earnings, and **80 on the news gate**. **Their news clearance is
  CARRIED from 08-12, not re-verified tonight** — stated plainly rather than presented as fresh. The 79
  unverified new candidates (incl. AMGN $680M, V $667M, HLT $356M) stay excluded fail-closed, continuing
  08-12's discipline that a short verified list beats a long unverified one.
- **S4 (advisory, +0.0044, n=1181 — the one lane that improved) — 14 names:** GSAT, RYN, CLX, CRNX, SAN,
  IMAX, SMMT, LTH, COR, FDS, ETN, FFIV, GXO, CAR. Funnel 1,933 → 97 (top-5% PCR) → 30 (option liquidity)
  → 22 (ETP) → 18 (earnings) → 14 (prior verdicts). Only **IMAX** persists from 08-12's 27. Separate
  **orthogonal** `ivrank_chg_5d` h3 tilt (DVY, FIVN, BLV, AIZ, ITW, NI, PULS, SLM, HDV, TBIL) — reported
  alongside, **never summed** with the PCR signal.

## Risk

- **Event stack inside the h10 window (08-13 → 08-27):** Retail Sales 08-14, **FOMC minutes 08-19**,
  jobless claims 08-20 and 08-27, and **Jackson Hole 08-27–29 landing exactly on the horizon edge** —
  anything sized to h10 tonight would still be open as it starts. Independently sufficient for −1 tier.
- **Correlation:** COO/NRG/WEC computed pairwise on daily returns from the price panel — **COO/NRG +0.128,
  COO/WEC +0.210, NRG/WEC +0.221** (141–145 paired days, full history on all three) against the 0.70
  threshold. Three singletons, no collapse. Computed, not inferred from sector labels — note NRG and WEC are
  both utilities yet correlate at only 0.221. Full price history on all three, so this is a real pass, not
  the absentee-reads-as-pass trap.
- **Tail:** SPY's flip to long gamma is vol-suppressive and *reduces* realized-move risk versus last night.
  Recorded as context; no tail cap invented — OI_FADE has none in the ruleset.
- **P0.6 out-of-regime half-cap: BINDS as an overlay**, but on a different basis than 08-11/08-12. Tonight's
  UPTREND is genuine, not a misread — but it decays to CHOP on 08-18, inside the h10 horizon, so the
  horizon-relevant regime is not stably supportive. Moot in practice: nothing reached a sizing band.
- **Half-cap, no auto-full.** Nothing sized at any level.

## Regression gate (`retro_harness.py --all`, run tonight)

No lane or threshold changed tonight. The truth set was rebuilt and extended (86 → **87 panel days**,
2,471-ticker spine), so the gate was run to locate the baselines.

| lane | baseline (83d, 2026-08-08) | 08-12 (86d) | **tonight (87d)** | Δ vs baseline | n |
|---|---|---|---|---|---|
| MOM_LONG | −0.0108 (n=1066) | −0.0119 | **−0.0124** | −0.0016 | 1104 |
| MOM_SHORT | −0.0128 (n=803) | −0.0136 | **−0.0133** | −0.0005 | 816 |
| **OI_FADE** | **+0.0059 (n=1087)** | +0.0039 | **+0.0037** | **−0.0022** | 1144 |
| S2_dp_revert | +0.0009 (n=1123) | +0.0008 | **+0.0009** | 0.0000 | 1163 |
| S4_pcr_fade | +0.0035 (n=1145) | +0.0048 | **+0.0044** | +0.0009 | 1181 |

**Verdict: NOT a regression.** Zero code changed; the only moving input is the panel, and n rose in every
lane. That is the documented data-drift case the gate does not treat as failure.

**OI_FADE has stabilized, not continued falling.** −0.0002 night-over-night (vs −0.0020 the night before),
and its structure is intact: hit-minus-base **+0.173** against the recorded +0.17, median **+0.0076** still
positive and still above the mean (so not tail-driven). Read as a diluting mean on a widening panel, not an
inverting edge. It nonetheless remains material to tonight's calls: the prior cited for NRG is *both*
borrowed from a differently-ranked population *and* now measures ~37% below its recorded level.

## Orchestrator notes / action items

1. **A lane capitulated to a challenge and manufactured a data-quality story — do not publish agent
   corrections unchecked.** I challenged the MOM_SHORT basket after ranking candidates by
   `pct_52w_range` and finding five dropped names ranking *tighter* than kept ones. The lane responded that
   `features.parquet` `w52l` was "stale on half the eligible names" and the basket was "unreliable."
   **Both the challenge and the reply were wrong.** Panel `w52l` matches Yahoo to the cent on all twelve
   names; the lane's actual screen is `close ≤ 1.02 × w52l` (proximity to the low), which is a *different
   quantity* from `pct_52w_range` (position within the whole 52-week range). WING sits at 1.5% of its range
   only because that range is enormous (110→346) — in price terms it is 3.1% above its low and correctly
   fails a 2% screen. The basket was right all along. Two lessons: (a) `pct_52w_range` is not a proximity
   metric and must not be used as one; (b) an agent conceding under pressure is not evidence — it
   volunteered a "stale data" explanation rather than defending a screen that was working as designed.
2. **QQQ gamma: Phase A and the vol lane disagreed; the endpoint settles it.** `uw options-structure gex
   --symbol QQQ` returns `zero_gamma_level 211.28` against spot 732.33 — broken, exactly as on 08-12. The
   vol lane reported a clean flip at 729.24 from a different source and concluded "no fail-closed needed."
   Fail closed. The stand-aside verdict was unchanged (VRP economics veto independently), but the reasoning
   would have been wrong on the record. **This is now a two-night-running data defect worth a maintenance
   ticket.**
3. **`catalyst_split` readings above 100% are arithmetic, not signal.** USFD 107.3%, UTHR 100.9%, NRG 106.5%
   under the strict `>` boundary all arise because the print-day net was itself *negative*, so the
   post-catalyst share exceeds the total. Correct behaviour, but easy to misread as extraordinary strength —
   for NRG it genuinely strengthens the read; for USFD/UTHR it describes a single post-print pop.
4. **TPR is the first live test of the earnings-crush wing guidance and it failed the wing, not the gate.**
   −16.5% realized against a ~12.2% raw-IV estimate that had itself already been widened from an 8.4%
   headline. The lane's refusal to size without a net-of-cost quote is what prevented a loss. Any future
   iron-fly guidance on gap-prone names should treat the raw-IV move as a *floor* on wing width, not a
   target.
5. **COO's exit is clean and worth keeping as a template.** The name spent four nights at WATCH and was cut
   by the lane's own instrumented invalidation rather than by drift, fatigue, or a fifth restatement of the
   same caveats. The standing selection-rule discount alone was never going to resolve it; the mechanical
   signal did.
6. **Selection-rule mismatch remains open** (standing since 08-12). Live lane ranks by `rel_build`; the
   +0.0059 baseline is top-15 by raw `oi_net_5d` (`retro_harness.py:82-99`). Tonight's cohort ranked 28–197
   of 1,430 against a top-15 cutoff of 21,642. Decision still needed: add the live screens to the harness
   and re-baseline, or record explicitly that the live prior is inherited rather than measured.
7. **S2's news gate was not re-run tonight** — three names carry an 08-12 clearance on an h3–5 lane, which
   is a one-day-stale verification on a horizon where a day matters. Advisory-only, so nothing turns on it,
   but the list should not be read as freshly verified.
8. **Next `/calibration-audit` due 2026-08-15** (per cadence, and now two days out). 41 open rows mature
   08-10→08-21 and the 08-03→08-07 crash-guard block matures 08-18→08-22 — the first cohort spanning
   non-overlapping windows. Count distinct **exit-days**, not rows. Consider re-recording the OI_FADE
   baseline at that audit, stating the panel size (87 days, 2,471-ticker spine).
9. **Watch tomorrow:** whether NRG's driving sessions finish rolling out (it should leave the list);
   whether WEC's build survives its ex-dividend date with the confound removed; and whether NXPI/USFD/UTHR
   collapse once the 08-07 session exits the 5-day window.
