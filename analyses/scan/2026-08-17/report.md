# Market Scan — 2026-08-17

## Regime & Verdict

- **Regime: UPTREND** · vol-state **LOW** (VIX 15.19, ~5th pct of trailing 6mo, **+6.6% on the day** off Friday's 14.25, −4.2% on 10d) · breadth **672 adv / 1,234 dec, 35.0% green** · `directional_tradable` **TRUE** · `s1_standdown` **FALSE`
- SPY 772.67 (**−0.47%** on the day), 0.9% off the 52w high (779.37, set 08-13), RSI14 61.8. QQQ notably stronger on the 10-day (+4.26% vs SPY +1.98%).
- ret5 **−0.05%** · ret10 **+1.98%** · dd15 **−3.72%**
- **Bottom line: No directional edge today. ZERO new starters — the book stays FLAT for a 6th consecutive session.**

### dd15 is not a drawdown (standing misread guard)
dd15 = min(last 15 closes)/close_10_back − 1. Tonight's −3.72% is the **07-29 low (729.46)** measured against the **08-03 anchor (757.67)** — a 13-session-stale excursion the tape already rallied out of, not a live drawdown. Confirmed independently.

### Breadth — corrected framing
Phase A framed today as a narrow-leadership / distribution divergence. On the full 1,920-name spine the honest read is different: **median stock −0.443%** against **SPY −0.47%** — the median constituent fell essentially *in line with* the index. This was a **broad-based weak day, not an internals-vs-index divergence**. (Friday: 52.7% green, median +0.08%.) The 2.6:1 near-high/near-low skew (192 vs 65, plus 44 stale-52w exclusions) is a longer-horizon structural fact and does not make today's tape narrow.

### Regime trajectory (load-bearing for anything with an h10 window)
The ret10 anchor currently sits at 08-03's 757.67 and rolls forward into the 771–773 range over the next 3–5 sessions. Absent fresh highs above ~785, **ret10 compresses toward 0% and UPTREND mechanically decays to CHOP well inside the h10 window** (→ 09-01). Same decay flagged on 08-14. `uw risk market-regime` independently reads **TRANSITIONAL / half-size**, disagreeing in emphasis with the mechanical UPTREND label.

---

## Directional Book (excess-scored)

**EMPTY — no name cleared any lane's bar tonight.**

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — |

Six consecutive flat sessions. The reasons are per-lane and independent:

| Lane | Baseline (2026-08-15, 2,471-spine) | Disposition tonight |
|---|---|---|
| **OI_FADE** | +0.0037 (n=1159) | **NO_NAME_CLEARED** — every candidate fails the raw-rank selection discount |
| **MOM_SHORT** | **−0.0140** (n=828) | Watch-only, never sizes (knowingly negative) |
| **MOM_LONG** | **−0.0122** (n=1121) | Basket/watch only, never sizes (knowingly negative) |
| **S2** | +0.0011 (n=1185) | Advisory-only, never sizes |
| **S4** | +0.0041 (n=1202) | Advisory-only, never sizes |

### OI_FADE — the only lane that could have sized, and it didn't
Population after floors: 1,166. The raw `oi_net_5d` top-15 is again pure ETP/mega-cap beta (GLD, NVDA, SLV, TLT, GOOGL, AAPL, META, SQQQ) — not tradeable candidates. Ranking by the live rule (`oi_rel_build`) produces a cohort whose **best raw rank is AS at 50–61 of 1,166–1,896**, and AS is separately **earnings-blocked (reports 08-18, tomorrow)**. Every remaining name sits at raw rank 125–798 — mid-pack by build size, not "heaviest."

Independently verified by the orchestrator: AS rank 50/1896 (blocked), FDX 125, SPHR 195, XYL 197, GEN 216, BSY 264, ITRI 308, AAON 312, DK 346, KNSA 431. The lane's "cleanest mechanically" name (KNSA) is at rank 431.

This is the **sixth consecutive night** the selection-rule discount has held (COO, NRG, STUB, INSW, WEC, FDX, GEN, BSY, ITRI). The +0.37%/+0.77% prior was measured on the raw top-15 population; a rel_build-ranked mid-pack name does not inherit it.

Two further mechanism catches worth recording:
- **COKE** — headline net +1,314 is a **mechanism failure**: call OI over 5 days is only **+73 contracts**; the positive net is entirely put-OI closing (−1,241). That is put-covering, not a call crowd to fade.
- **ALC** — dominant build day is 08-11, one day after its 08-10 print: an earnings-reaction block, not organic accretion. Strict `>` boundary reads 104.5% vs 93.3% shipped.

---

## Vol Book (non-directional)

### 0DTE-VRP — **STAND ASIDE, both symbols**
| | SPY | QQQ |
|---|---|---|
| VIX tercile | LOW | LOW |
| Conditional `mean_pnl_by_vix_state[LOW]` | **−0.003%** | **+0.072%** |
| Less ~0.10% round-trip cost | **≈ −0.10%** | **≈ −0.03%** |
| Aggregate gamma sign | NEGATIVE (−368.0M) | POSITIVE (+582.2M) |
| Spot vs flip | 773.01, **flip unresolvable (null)** | 730.13 vs 734.54 → **0.60% below flip** |
| `sell_premium` / `size_scalar` | False / 0.0 | False / 0.0 |

The pooled headline verdict prints `GO_PREMIUM_SELL_INTRADAY` for both — **that is the tercile-pooling artifact**, and it does not apply tonight. Verified directly: the LOW-bucket conditional is ~0 before cost and negative after it. Both symbols are additionally in a dealer-**short-gamma** regime at the money (the vol-amplifying, wide-range state this sleeve is not sized to sell into). QQQ is the textbook trap case — aggregate GEX positive while spot sits below the flip; **range/wing-width keys off the aggregate sign, the sell decision keys off spot-vs-flip**, and they are kept distinct here.

### Earnings IV-crush — ADVISORY ONLY, never sized (no harness validates this lane)
Implied moves recomputed off the **bracketing** expiry using **median** ATM IV. Every figure is a **LOWER BOUND** on the realized move (TPR precedent: realized −16.5% vs a ~12.2% raw-IV estimate) — size wings wider than these, not to them.

| Ticker | Print | Bracket expiry | ATM straddle | Net-of-cost credit | Backwardation |
|---|---|---|---|---|---|
| OKTA | 08-26 | 08-28 (11d) | 13.02% | **11.93%** | 1.45× |
| HPQ | 08-26 | 08-28 (11d) | 10.77% | **10.49%** | 1.32× (tightest cost, 2.6% of straddle) |
| ADSK | 08-27 | 08-28 (11d) | 9.40% | **8.42%** | 1.20× |
| ROST | 08-20 | 08-21 (4d) | 6.09% | 5.72% | 2.29× |
| JKHY | 08-18 | 08-21 (4d) | 6.20% | 5.32% | cost 14.2% of straddle — wide |
| TJX | 08-19 | 08-21 (4d) | 4.34% | 3.99% | 1.98× |
| DE | 08-20 | 08-21 (4d) | 5.18% | 4.99% | 1.64× |
| COTY | 08-19 | 08-21 (4d) | 17.40% | *(excluded)* | cost 15.8% of straddle |

**COTY excluded** — sub-$3 stock, 160%+ median ATM IV, ~1–2 contracts per side at the ATM strike. A liquidity/data-quality outlier; the credit number is not trustworthy at that spread width.

**New generic trap recorded:** any earnings candidate whose print falls *after* the front expiry has its true implied move invisible to a naive `implied_move_perc` read. OKTA/HPQ/ADSK all report *after* the front 4dte expiry — the naive read misprices OKTA as CONTANGO and understates HPQ/ADSK's implied move by ~3×. Always identify the first expiry ≥ print date before declaring backwardation.

---

## Watch / Stood-down

### Prior watch cohort — continuity (orchestrator's job; no lane carries these)
| Name | 5d net | Last session | Status |
|---|---|---|---|
| **GEN** | +5,619 | **call −352, net −577** | **CUT — mechanical invalidation FIRED** (calls genuinely closing) |
| FDX | +13,537 | call +912, net +277 | Retained WATCH — still building but decaying (rel_build 0.657) |
| BSY | +3,959 | call +167, net +162 | Retained WATCH — build stalled to near-zero fresh adds |
| ITRI | +2,845 | call +18, net +10 | Retained WATCH — build effectively dead |

GEN's cut is the same rule that cut COO (08-13) and NRG (08-14). Nothing was sized on any of them; no realized loss.

### MOM_SHORT — watch-only (14 names, never sizes)
Top by 52w-range: RBA, NKE, STLA, AMRZ, CPRI, ESAB, ROL, GPI, GME, HDB, BKNG, TTD, KLAC, ZTS.

**Yahoo-verified.** The UW `pct_52w_range` for the leaders prints *negative* (RBA −4.11%, NKE −2.27%, STLA −1.87%) — that is stale `w52l` not yet including today's new low, **not** a false signal. Yahoo confirms all are genuinely at 52w lows **set today**: STLA 0.3% of range, RBA 0.2%, AMRZ 0.4%, NKE 0.6%, CPRI 0.8%. 44 of 1,920 names carry out-of-range values tonight and only the detectable class is visible — the in-range-but-wrong class (un-split-adjusted `w52h`) is what manufactures false shorts, so this verification is not optional.

### MOM_LONG — basket/watch only (30 names, never sizes)
Verified genuinely at highs: PSX 99.9% of range, PTGX 99.7%, RVMD 97.8%, ARGX 95.9%, IESC 95.5%.

### S4 sentiment-contrarian — **lane output corrected before use**
The lane returned 15 names ranked by raw PCR with **no call-volume floor**, and its top names are **denominator artifacts, not sentiment**: NWG's PCR of 682 is *three* call contracts against 2,046 puts. TNGX (32 calls), SAN (66), AMRZ (68), HST (90), JAZZ (63) are the same failure.

Applying `call_volume ≥ 500` drops the population 1,920 → 917 and collapses max PCR from 682 to 33; adding the `issue_type = 'Common Stock'` cut removes a fresh ETP leak (XRT, JETS, XLI, XLY, ARKK, IYR all rank top-15 without it). **Only 2 of the lane's 15 names survive** (CARR, EXE — which it had ranked 8th and 10th).

Corrected advisory list: **CARR, EXE, APO, CHYM, XEL, VLO, RYN, BKR, FSLR, BURL, EQT, EIX, WM, SMMT, ARE.**

Note this dissolves an apparent cross-lane contradiction: AMRZ appeared as both a MOM_SHORT (short) and an S4 (long) candidate. AMRZ's S4 entry is a 68-contract artifact and drops out, so there is no live directional conflict.

### S2 liquidity-reversion — advisory, zero starters
194 DP candidates → 106 after Common Stock + liquidity → 103 after the h5 **trading-day** earnings gate.

Excluded as **catalyst-informed flow** (the lane's hard rule — this is informed positioning, not mean-reversion): **RDDT** ($2.6B DP — S&P 500 inclusion announced today + Form 144 insider sales), **GH** ($609M — post-Q2 upgrades), **COF** ($396M — ex-dividend today), **COP** ($378M — ex-dividend today + CEO retirement).

Blocked on prior policy: **V**, **KLAC** (weekly standdowns), **RTX** (basket-only), **NXPI** (OI_FADE demotion 08-12/13).

Watch-only, news **UNVERIFIED** (10 of 15 unchecked — labeled, not silently passed): LYB, TWLO, EQIX, ROKU, AME, MFC, IDXX.

*(KLAC appears in both the MOM_SHORT watch list and S2's blocked set. Noted as evidence-type diversification only — never summed.)*

---

## Risk

- **Correlation clusters:** not binding — nothing sized, so no cluster can collapse.
- **Event calendar — the entire Tier-1 cluster sits inside the h10 window (08-18 → 09-01):**
  - 08-20 FOMC minutes (July)
  - **08-21 Jackson Hole opens** (Powell) — Tier-1
  - **08-26 Core PCE, 8:30am ET** — Tier-1
  - **08-26 AH NVDA Q2 FY27** — index-moving, especially QQQ
  - 08-18→08-21 HD / WMT / LOW / TJX / ADI (consumer read-through)
- **Tail caps:** vacuous tonight — nothing reached a sizing band, so Phase D had nothing to gate. `fundamentals-gate` was not spawned for the same reason (it runs only on names about to be sized).
- **Vol left tail:** 0DTE stood aside on two independent grounds (negative LOW-tercile conditional net **and** short-gamma regime). Earnings-crush implied moves are floors, not estimates.
- **Hedge note:** no book, no hedge required.

---

## Data integrity (Phase 0)

The truth-set parquets were **stale on arrival** — all three ended 2026-08-14 against a 2026-08-17 trade date. Rebuilt before any lane ran: `prices` (352,331 rows / 2,448 of 2,471 tickers priced; 23 unpriced fail closed downstream), `returns` (SPY self-excess 0.0 at every horizon), `features` (172,300 rows / 2,484 tickers / 89 dates). Preflight re-run clean. Panel 5/5 complete for 08-17.

Had this not been caught, every lane would have scored a Friday tape against a Monday date.
