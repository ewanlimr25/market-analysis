# Market Scan — 2026-06-30

> Live post-market scan (fresh 2026-06-30 panel export, ~20:15 EDT). Scoring currency = **excess-vs-SPY (conditional)**, never raw win-rate. Regime is path-aware (Yahoo chart API + live `uw` 06-30), **not** the stale harness fallback (see note). Phase A/B run directly in the foreground this session — the background sub-agent channel was failing (dying after one tool call), so all lane data was gathered via direct DuckDB reads of the panel parquets.

## Regime & Verdict
- **Regime: UPTREND_RESUMPTION / TRANSITIONAL** · SPY **746.77 (+0.78%)**, now back **above** 20dma (742.24) AND 50dma (735.87), −1.79% from 90d high · QQQ **736.40 (+1.70%)**, ret5 **+3.19%** (tech-led) · ret5(SPY) **+1.80%**, ret10 −1.07%.
- **The V-rebound has EXTENDED and CONFIRMED.** The 06-22→06-26 dip (SPY 744→729, −2%) is now fully round-tripped by a **two-day snapback** (06-29 +1.65%, 06-30 +0.78%); SPY sits *above* the pre-dip level. Yesterday's PULLBACK_IN_UPTREND has resolved to the upside.
- **vol-state** (2nd-moment, NOT a direction): VIX **16.45, −6.8% today / ret5 −15.6% / −36% off 90d high / near 90d low** (below both MAs). Front-end **flipped BACKWARDATION→CONTANGO** (0.903) — the fear structure normalized. SPY GEX still **NEGATIVE** but spot **746.55 right at the ZGL flip** (749.07; gap 0.34% vs 3.2% yesterday) → dealers short-gamma yet **on the cusp of flipping to stabilizing**. 1y skew TAIL_HEDGING (1.44). **Rapidly normalizing toward complacency.**
- **breadth: WEAK / DIVERGENT (persists).** 38% bullish (2372 bullish vs 3873 bearish flow tickers, n=6245) on an up day → a **narrow, mega-cap/tech-led** rebound. Sector rotation: Technology +$257M (dominant), Industrials, Utilities in; Financials, Healthcare, Comm-Services out.
- `directional_tradable: true` (**half-cap** — TRANSITIONAL + weak breadth; uw guidance "half sizes, defined-risk") · `s1_standdown: **true** (persisting / strengthening)`.

> **⚠ Harness/truth-set staleness (unchanged):** `retro_harness.py --date 2026-06-30` falls back to the **06-26** regime because `data/{returns,prices,features}.parquet` max at 2026-06-26 — it **cannot classify 06-30**. The numbers above are the **live path-aware read** and are authoritative for this scan. Lane *priors* are cross-year backtested constants and remain valid.

- **Bottom line:** Low-conviction, tape-fighting environment. The one robust regime-agnostic lane (**OI-fade short**) is live → **3 starter/half OI-fade shorts** after correlation-collapse, sector-diversified and confined to **mid-range** names (near-52w-low reflexive builds are deferred as squeeze-prone). **`s1_standdown` suppresses the entire MOM_SHORT leg** — day-2 of a confirmed snapback with VIX collapsing is peak momentum-crash risk. MOM_LONG is a WATCH-only near-52w-high **semis** basket (weak breadth). As on 06-29, the **richest actionable menu is the VOL BOOK** (early-July earnings IV-crush into a shortened holiday week); **0DTE-VRP stands aside** under negative gamma + NFP + holiday.

## Directional Book (excess-scored)
| Ticker | Lane | Dir | H | validated_excess | regime_fit | size | tier | gates / why |
|---|---|---|---|---|---|---|---|---|
| **WEN** | OI_FADE | short | 10 | +0.0088 (hit−base +0.205, n=640) | 1.0 | **starter** | MEDIUM | Cleanest genuine crowded-call extreme: 5d call-OI build = **1.13× its own 30d-avg** (vs ~0.12–0.16× for megas); pct52 0.37 (no squeeze); ER 08-14 outside h10; consumer-diversifying; fund CAUTION |
| **TSLA** | OI_FADE | short | 10 | +0.0088 | 1.0 | **starter** | MEDIUM | Heavy call-dominated build (+605k, net +115k), pct52 0.63 mid-upper (fade strength, not near-low); ER 07-22 outside h10; auto-independent; fund CAUTION |
| **AMZN** | OI_FADE | short | 10 | +0.0088 | 1.0 | **starter** | MEDIUM | Mega-cap-internet cluster **rep** (AMZN/GOOGL/META → sized once); build +409k net +233k, pct52 0.51; ER 07-30 outside h10; fund CAUTION |

**Why these three (the discipline):**
- **No additive confluence** — each scores on the OI-fade lane alone at its measured +0.88% h10 excess (MEDIUM). Nothing is summed.
- **Relative-build, not absolute.** The fade signal is a *crowded-call extreme*, so ranking is by 5d call build ÷ 30d-avg call OI — which promotes **WEN (1.13×)** and demotes the mega-caps (~0.14×), whose huge absolute builds are normal for their OI base. **CG** is the single most extreme (**4.58×**) but sits at pct52 ~0.08 with near-pure-call PCR (0.045) → a classic **M&A/catalyst-speculation** profile you must **not** fade blindly → **WATCH pending a news gate.**
- **Correlation-cluster collapse (corr ≥ 0.70 = one position):** mega-cap-internet (AMZN/GOOGL/META) → 1 (AMZN); mega-cap-semi (NVDA/AVGO) → watch (NVDA is *leading* the tape → times poorly); crypto (MSTR/MARA/BMNR) → 1 watch. Sized book kept sector-diverse: **consumer (WEN) / auto (TSLA) / internet-mega (AMZN)**.
- **V-rebound squeeze overlay → near-52w-low reflexive builds deferred:** MSTR/BMNR/MARA (crypto), PLTR/SOFI, BABA (China) are heavy builds **at 52w lows** = exactly what squeezes on a confirmed rebound → **WATCH, not sized.** Sized names are all mid-range pct52.
- **Half-cap, no auto-full** (invariant #4): everything caps at starter/MEDIUM.
- **Structural note:** short crowded-call mega-caps + WATCH-long near-52w-high **semis** basket ≈ a roughly **tech-neutral RV** posture, which suits a no-clear-direction, weak-breadth TRANSITIONAL tape.

## Vol Book (non-directional) — *the meat again*
Delta-neutral, quoted **net-of-cost**, 0 directional points. Rich early-July earnings cluster into a shortened holiday week:

| Symbol | ER | IVR | implied move | note |
|---|---|---|---|---|
| **FDS** | 07-01 AM | 88 | 9.9% | Richest near-dated liquid large-cap → condor, harvest crush if realized < implied |
| **GIS** | 07-01 AM | 85 | 6.1% | Liquid consumer-defensive |
| **PENG** | 07-07 PM | 97 | 23.7% | Richest IV but wide move + small-cap gap → **MINIMAL, defined-risk only** |
| **AZZ** | 07-08 PM | 87 | 7.5% | Mid-cap, small size |
| **PEP** | 07-09 AM | 84 | 1.3% | Liquid mega-cap, tiny move → tight condor |
| **JNJ** | 07-15 AM | 83 | 1.5% | Post-holiday mega-cap; Q2 kickoff |
| **BNY** | 07-15 AM | 79 | 5.2% | Q2 bank-earnings kickoff |

- **0DTE-VRP → STAND ASIDE this week.** SPY GEX still NEGATIVE (spot 746.55 < ZGL 749.07) + NFP 07-02 + Jul-3 holiday thin tape → premium-selling less safe net-of-cost (realized can spike, dealer hedging amplifies). *Watch item:* a SPY close above ~749 flips dealer gamma positive (stabilizing) and would re-open 0DTE-VRP — not there yet.

## Watch / Stood-down
- **MOM_SHORT — ENTIRE LEG STOOD DOWN** (`s1_standdown`): genuine near-52w-low cohort (CME/ICE/T/TMUS/BSX/AMT/NKE…). *Data note:* the raw near-low screen is partly polluted by **split artifacts** (NFLX/BKNG/ISRG/INTU/KLAC carry unadjusted 52w-highs → spurious pct52≈0); the names listed are genuine.
- **MOM_LONG — WATCH/basket only:** near-52w-high, **semis-heavy** basket (AMD/AMAT/LRCX/GLW/ALAB/TER/SNDK/INTC/PANW + CAT/GEV/LLY/UNH). Tail-driven, never per-name; capped to watch by weak (38%) breadth.
- **OI-fade WATCH:** NVDA/AVGO (semi cluster, leading the tape), GOOGL/META (internet dup via AMZN), MSTR/MARA/BMNR (crypto squeeze), BABA (China), PLTR/SOFI (near-low high-beta), **CG (news-gate)**, ASTS (high-flyer).
- **S2 dark-pool reversion (advisory long-tilted):** **COST** (SELL-heavy extreme, buy_frac 0.093 on $484M directional; ER far) · **XOM** (BUY-heavy extreme 0.940, energy-diversifying). News-gate is a manual check.
- **S4 PCR-fade (advisory long):** **SHW** (PCR 8.1, most liquid, mid-range, ER clear); secondary FERG/EXPE. Never sized. The mirror (short the call-heavy crowd) measured negative and is not fired.

## Risk
- **Correlation clusters:** mega-cap-internet (AMZN·GOOGL·META), mega-cap-semi (NVDA·AVGO), crypto (MSTR·MARA·BMNR), semis-long-basket. Each collapses to one position; sized book deliberately spans consumer/auto/internet.
- **Event calendar:** ISM 07-01 (T2) · **NFP 07-02 (T1, moved up)** · **market HOLIDAY 07-03** (thin) · CPI + Q2 banks begin ~07-14/15 (at/just past h10). NFP is inside all horizons → a market-wide gap risk absorbed via half-cap.
- **Tail caps applied:** OI-fade shorts sized for the squeeze tail on a risk-on, negative-gamma tape (starter, not half); crypto/high-flyer/near-low builds deferred; vol-shorts defined-risk & net-of-cost; 0DTE stood aside.
- **Hedge note:** dealers short gamma amplifies intraday moves until SPY clears ~749; the short-OI-fade / long-semis-basket pairing is intentionally tech-neutral to limit directional beta into NFP + the holiday.
