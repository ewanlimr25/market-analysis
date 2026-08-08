# Market Scan — 2026-08-04

## Regime & Verdict
- **Regime:** UPTREND/REBOUND-THRUST · ret5 **+4.110%** · ret10 +3.080% · dd15 −2.520%
- **Vol-state:** VOL-SUPPRESSION — dealers net long gamma on both index proxies. SPY total_gex +$1.104B,
  spot 772.17 vs zero-gamma 767.91; QQQ total_gex +$623.7M, spot 724.09 vs zero-gamma 711.88. VIX ~16.5
  (~48th pct). Script and CLI agreed on the gamma sign for both symbols, independently re-verified by the
  orchestrator — the `zerodte_setup.py` sign bug did not bite (third consecutive session; still unfixed).
- **Breadth:** 71.37% green (359 adv / 141 dec of 503).
- `directional_tradable` = **TRUE** · `s1_standdown` = **TRUE**
- **Bottom line: no directional edge today — ZERO new starters across all five lanes.** The vol book is
  the only actionable output, for the fifth consecutive session. Book was flat coming in and stays flat.

Every lane is out for a **sourced, structural** reason tonight, not a marginal miss — see the table below.

## Directional Book (excess-scored)

*(empty — no name in any lane reached a sizeable tier)*

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — |

### Why each lane is out

| Lane | Disposition | Binding reason (sourced) |
|---|---|---|
| **MOM_LONG** | BASKET_WATCH (49 names) | **Two independent bars.** (1) Lane excess **+0.23% < +0.30%** starter bar, and its median is **−0.91%** — the mean is tail-carried. (2) `risk-sizer.md` bars this lane from starter sizing outright until a **DURABLE-N (≥30) forward window re-clears positive excess**, re-enabled "via a `/calibration-audit` recommendation, not ad hoc." The lane reported "Sized: 49 names" — that is wrong on both counts. |
| **MOM_SHORT** | STOOD_DOWN | `s1_standdown` fired **decisively** (ret5 +4.110% vs the +2.5% trigger — a 1.61pp margin, versus 0.0139pp yesterday). Plus the invariant-#6 watch-only cap for new starters and a negative baseline (−0.0008). Triply out. |
| **OI_FADE** | NO_NAME_CLEARED | **Fifth consecutive zero-starter session** (07-29→08-04). All 15 candidates die on ≥1 independent gate. |
| **S2_dp_revert** | ADVISORY_WATCH (10 names) | **Advisory lane → watch** by the sizing map, regardless of measured excess. Regime is a documented headwind for a mean-reversion long. |
| **S4_pcr_fade** | ADVISORY_WATCH (4 names) | **Advisory lane → watch.** `retro_harness.py` tags this lane `size:"advisory"` structurally. Note this is the **only lane positive forward** (+1.16%, hit−base +0.26, DURABLE) as well as historically (+0.51%). |

The sizing map (`risk-sizer.md:45`) is `≥+1% & sign-stable → half` · `+0.3–1% → starter` ·
`< +0.3% **or advisory lane** → watch`. This finally resolves the Phase-C/sizing-map conflict that has
been carried as an open action item since 07-31: an **advisory lane never sizes regardless of its measured
excess**. S4 at +0.51% is watch because of the advisory clause, not because it misses a bar. The S4 lane's
claimed "+0.7% starter bar" does not exist anywhere in the repo — it was invented.

## Vol Book (non-directional)

Delta-neutral, advisory, quoted **net of cost**. Left tail remains unsampled.

### 0DTE-VRP premium-selling
| Symbol | Verdict | Gamma (script / CLI) | Size | Gross | **Net** | Structure |
|---|---|---|---|---|---|---|
| SPY | GO_PREMIUM_SELL_INTRADAY | long / **POSITIVE, spot 772.17 > ZG 767.91** ✓ | ×0.5 | 0.223%/d | **+0.123%/d** | iron fly, wings ≈ ±0.83% |
| QQQ | GO_PREMIUM_SELL_INTRADAY | long / **POSITIVE, spot 724.09 > ZG 711.88** ✓ | ×0.25 | 0.341%/d | **+0.241%/d** | iron fly, wings ≈ ±1.45% |

QQQ's halved size is **not** a ratio artifact: the full term structure was pulled and the near-week hump is
genuine (dte1 30.8% → trough dte6-7 ~22.8% → **re-rising to 24.2–25.1% by dte8-10**). SPY's dte0 25.0% → dte1
16.0% hump is ordinary same-day pinning, correctly not flagged.

**Tempering caveat:** the index-level **30-day** VRP reads **FAIR (−0.002)** — IV essentially tracks realized.
The 0DTE VRP is a different, shorter measure and can be positive while the 30d is flat, but conviction on the
index premium-selling book should be read down accordingly. These are not the same number and should not be
quoted as agreement.

### Earnings IV-crush (SELL-VOL vs implied move)
| Ticker | DTE | Implied | Hist. realized (mean, n, max) | Verdict |
|---|---|---|---|---|
| CACI | 1 | 8.19% | 0.68% (n=8, max 2.5%) | **SELL_VOL** — implied 12× mean; no weekly, 17DTE expiry |
| TTMI | 1 | 18.71% | 3.19% (n=7, max 10.6%) | **SELL_VOL** — ~6× mean, ~2× fattest print |
| DBX | 2 | 5.92% | 1.05% (n=8, max 2.4%) | **SELL_VOL** — >2× worst print in 2yr |
| COHR | 8 | 8.54% | 4.12% (n=8, max 7.9%) | **SELL_VOL** — clears historical max |
| TLN | 1 | 7.60% | 1.88% (n=8, max 6.0%) | SELL_VOL, **size down** — last print 6.0% nearly matched implied |
| BCO | 1 | 8.65% | 5.15% (n=8, max 12.8%) | MARGINAL — below fattest tail; no weekly |
| SGI | 2 | 9.83% | 5.41% (n=8, max 11.8%) | MARGINAL — tail nearly matches implied; no weekly |
| COR | 1 | 6.88% | 6.02% (n=7, **max 17.4%**) | **PASS** — fat tail unpriced, no near-dated instrument |
| IRM | 1 | 5.65% | 6.14% (n=7, last two 7.3% & 9.0%) | **PASS** — implied *under* historical mean; crush thesis inverted |

**Best of book: CACI, TTMI, DBX, COHR.** All defined-risk, wide wings for the binary tail.

**Orchestrator event-risk flag (not raised by the lane):** CACI, BCO and SGI have **no weekly** — the nearest
listed expiry is **17DTE (2026-08-21)**, which straddles the print *and* both **CPI (08-12)** and **PPI (08-13)**.
That is an unhedged Tier-1 macro exposure stacked on top of the earnings binary, for 12 extra decay days.
Size these accordingly or wait; it is a materially different trade from the weekly-expiry names.

The `uw insights earnings-play` endpoint returned `iv_rank=100` for **every** result — a saturated/broken
field. It was correctly not used for ranking.

## Watch / Stood-down

- **MOM_LONG basket (49, watch):** sector max **24.5%** (Industrials), inside the ⅓ cap. **135 names
  fail-closed** on the `prices.parquet` coverage gap. Top by proximity: SWK, JCI, NEU, ETN, NUE.
- **MOM_SHORT (stood down):**
  - **CLBK — verified FALSE SHORT, correctly excluded.** Screener `week_52_low` $10.60 vs Yahoo **$6.2091**;
    true pct_range **81.9%**, not the screener's 0.9%. Its `week_52_high` is wrong too ($25.83 vs $11.7409) —
    doubly broken. The lane got this one right.
  - **GME — genuine near-52w-low the lane MISSED.** Yahoo and the screener now **agree**: low 18.545 (set
    08-03), close 19.21, **pct_52w_range 6.96%**, in-range and correct. The lane's screen returned only CLBK.
    GME is stood down by the crash gate regardless, so there is no live consequence — but it belongs on the
    watch list and was dropped. 101 of 2,870 liquid common stocks still carry an out-of-range pct_52w_range.
- **S2 advisory (10, h5 closes 2026-08-12):** GDS, BNS, LYB, SWK, AMP, SPGI, LPLA, CORZ, CAKE, TT.
  35 of 45 fail-closed on coverage. **GDS reports 2026-08-13** — clear of h5 by a single session, blocked at h10.
- **S4 advisory (4, h5 closes 2026-08-12):** ICLR (PCR 61.97), LYV (10.52), NVS (7.62), TCOM (6.82).
  NVS additionally carries the h3 `ivrank_chg_5d` tilt (+6.86) — **orthogonal, noted, never summed**.
  9 of 15 fail-closed on coverage.
- **OI_FADE killed (15):** mechanism/persistence >0.85 — HNI 0.999, HIG 0.988, HXL 0.993, INFY 0.984,
  LZM 0.983, AZN 0.950, EXLS 0.869, MRCY 1.260, APAM 1.068; earnings-in-window — SOLV, MRCY, LZM;
  ETP — MTUM, SPCU, DIG; liquidity — HNI, MYGN, APAM, LZM, SPCU, DIG; fundamentals VETO — AVTR (16 mentions).

## Risk

- **Event calendar:** **CPI 2026-08-12 (Tier-1)** and **PPI 2026-08-13 (Tier-1)** both land inside an h10
  window opened today (h10 ends **2026-08-19**; h5 ends **2026-08-12**, i.e. CPI lands on its final day).
  No Tier-1 print falls in the first six sessions. Nothing directional is open, so this binds only the vol book.
- **Correlation clusters:** none — zero positions.
- **Tail caps:** none applied; nothing sized.
- **Hedge note:** no directional exposure to hedge. Vol book is delta-neutral by construction.
- **Advisory divergence tell:** price breadth (71.37% green) is much broader than options-flow breadth
  (41.1% bullish, 2,585 bullish vs 3,701 bearish). Price is running ahead of flow positioning. The repo's
  *defined* divergence check (green tape **with** pct_green < 50) does **not** fire, so this is noted, not scored.
- `uw risk market-regime` self-labels **TRANSITIONAL** while its own `spy.trend` field reads `UPTREND`.
  That is the CLI's internal heuristic, not the mechanical ret5/ret10 rule this repo scores on. Not adopted.

## Process findings

1. **Momentum lane misreported twice.** It claimed "Sized: 49 names" (barred on two independent grounds) and
   returned forward excess as "not yet resolved" — which is not a starter-bar test. It also **missed GME**, a
   clean in-range near-52w-low name. Fifth lane misreport this cycle; caught only by independent re-run.
2. **S4 invented its bar.** The "+0.7% starter bar" appears nowhere in the repo. The real reason it does not
   size is the advisory-lane clause. Right answer, wrong reasoning — which would have failed on a different night.
3. **S2 read a stale screener** (`stock-screener-2026-07-23.parquet`) for the `issue_type` ETP cut on an 08-04
   scan. Re-run on the trade-date panel: no ETP leaked, outcome unchanged — but the input was wrong.
4. **S2 reported CAKE "clean"**; `prior_verdicts.py` returns a prior blocking verdict (2026-W31). Substance is a
   MOM_LONG basket note, not an S2 veto, so no practical effect — but the gate result does not reproduce.
5. **OI_FADE reproduced EXACTLY** — persistence, liquidity, ETP classification and earnings, name for name.
   Second consecutive honest report from this lane. Worth recording alongside the failures.
6. **`earnings_gate.py` one-sided-bound bug bit again**: LZM was BLOCKED on a **2026-07-29 print that had
   already happened**. Fails closed, so safe, and LZM died on mechanism anyway. Still must be fixed **paired**
   with `retro_harness.py:63,76,138`, which carries the identical bound and imports nothing.
7. **`prices.parquet` coverage gap — 7th consecutive session.** 783 tickers vs a 2,466-ticker features spine.
   Cost tonight: **135 MOM_LONG + 35 S2 + 9 S4 fail-closed**. Root cause is known (static `universe.json`
   frozen 2026-06-28). Deliberately not fixed mid-scan — it shifts the harness baseline panel and requires a
   regression-gate re-run.
8. **`held_book.py` fix verified working.** It now reports `read 1 position(s): 0 open, 1 closed` and names the
   exclusion, instead of the bare "no open positions" that hid a live position on 07-31 and 08-03. 27/27 tests pass.
