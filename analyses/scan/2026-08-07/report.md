# Market Scan — 2026-08-07

## Regime & Verdict

- **Regime:** UPTREND/**REBOUND-THRUST** · ret5 **+3.510%** · ret10 **+4.650%** · dd15 −1.280%
- **Vol-state:** **REGIME CHANGE vs the prior two sessions.** VIX **14.90**, a fresh cycle low
  (15.86 → 16.50 → 15.81 → 15.15 → 14.90), LOW tercile (cuts 16.35 / 18.43). Dealers are now net
  **LONG gamma in both indices**: SPY spot 772.84 vs zero-gamma flip 772.36 (**+0.06% above**),
  QQQ spot 722.39 vs flip 721.08 (**+0.18% above**). Aggregate GEX positive in both (SPY +$1.85B,
  QQQ +$853M) — that sign sets range/wing-width only; **spot-vs-flip sets the regime**, and tonight
  it says long gamma, where on 08-05/08-06 it said short. SPY's cushion is razor-thin: a ~0.5pt
  give-back flips it back to short gamma while QQQ holds.
- **Breadth:** **321 adv / 180 decl**, pct_green **63.82%**, avg +0.70% — a genuinely green tape.
  But options-flow bullish is only **37.7%** (2,368 of 6,281). **Breadth-vs-flow divergence: YES** —
  flow is not confirming the price breadth. Rotation is into Technology/Industrials/Consumer Defensive,
  out of Communication Services/Consumer Cyclical/Healthcare. `uw risk market-regime` reads
  TRANSITIONAL/reduce-size.
- `directional_tradable` = **TRUE** (regime admits lanes) · `s1_standdown` = **TRUE**
- **Stand-down margin:** ret5 +3.510% vs the +2.5% trigger → **+1.01pp**. Trajectory:
  08-03 +0.01pp → 08-04 +1.61pp → 08-05 **+3.03pp (peak)** → 08-06 +1.12pp → 08-07 **+1.01pp**.
  **The decay has FLATTENED — this is the change from yesterday.** Last session's −1.91pp collapse
  became −0.11pp tonight, and ret10 kept *rising* (+4.12% → +4.65%). Yesterday's read was "roughly
  1.1pp more decay ends the stand-down"; tonight that no longer looks imminent. The thrust stopped
  decelerating.

**Bottom line: no directional edge today. ZERO new starters for an EIGHTH consecutive session
(07-29 → 08-07); the book stays FLAT for a fifth. The vol book is EMPTY for a third — but tonight
it stands down on ECONOMICS, not mechanics.**

Two things genuinely changed tonight, and they point in opposite directions:

1. **OI_FADE recovered to two mechanically-clean names** (USFD, UTHR) after 08-06's pure zero. Both
   cleared the entire mandatory stack and are blocked *only* by the lane's Hard Rule #2 regime
   stand-down. UTHR is the strongest single candidate on file in over a week — CONFIRM fundamentals,
   clean catalyst survival, no M&A confound. **Regime-blocked, not mechanism-blocked.**
2. **The 0DTE mechanical gate flipped GREEN for the first time in three sessions** (dealers rotated
   long gamma) — and the sleeve still stands aside, because conditioned on tonight's LOW VIX tercile
   the net-of-cost expectancy is *negative*. The mechanics finally cooperated; the economics did not.

## Directional Book (excess-scored)

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | **none** | — | — |

*Empty is a valid and common output (`RESEARCH/20 §2.0`). Nothing scored; nothing sized.*

## Vol Book (non-directional)

**EMPTY — third consecutive session, but for a NEW reason.**

- **0DTE-VRP — mechanical gate GREEN, stood down on net-of-cost economics.** `sell_premium=true`,
  `size_scalar=0.5` for both SPY and QQQ — dealers are long gamma (spot above flip in both), no VIX
  spike, and no front-end backwardation on the near-ATM basis the gate actually uses. **The binding
  read is the state-conditioned expectancy:** tonight's VIX 14.90 sits in the LOW tercile, where the
  gross mean is **SPY −0.059%** and **QQQ +0.016%** — charge the 0.10% round-trip and both go **net
  negative** (SPY ≈ −0.16%/day, QQQ ≈ −0.08%/day). The headline full-sample net-positive figure
  (+0.123% / +0.26%) is carried entirely by the MID/HIGH-VIX buckets. Selling cheap vol into a
  suppressed tape is exactly the trade that pays gross and loses net.
  *Methodology note:* the raw `iv-term-structure` full-0DTE average shows SPY 1.34× / QQQ 2.09× VIX,
  which looks backwardated, but that metric is contaminated by deep-OTM 0DTE contracts. The near-ATM
  6-strike calc on the next tradeable expiry is under the 1.25× gate. This is **not** a repeat of
  08-06's QQQ 1.54× flag on the metric the gate uses.
  *Gamma-sign discipline held per `5b3daec`* — aggregate sign drove the wing width, spot-vs-flip drove
  the sell decision, kept separate.
- **Earnings IV-crush — ENVX examined at contract level and REJECTED.** This corrects yesterday's
  provisional flag. Pulled the raw trade tape (the hot-chains file is missing the ATM put leg):
  spot $4.70, ATM straddle ≈ $0.93–0.94 → **implied move ≈ 19.9%** for the 08-14 expiry, term
  structure genuinely backwardated (193% front vs 118–155% back). But the underlying is *chronically*
  fat-tailed — trailing realized vol ~93–102% annualized (daily 1σ ≈ 6.3%), with at least three
  >9–15% single-day non-event moves in the trailing 90 sessions. Independently corroborated: ENVX ran
  **+14.9% in 5 days / +19.0% in 10**. Wings sized off a 20% implied move get blown through by
  ordinary chop, not just the print. **Rich IV here is paid-for tail, not free premium.**
  Yesterday's "mean abs 3.3%, no >13% print in 10 quarters" characterization does not survive contact
  with the panel.
- **TRMB** — adequate flow ($472k combined), iv_rank 91.4, **not deep-dived**. Explicitly held at
  watch rather than silently dropped; candidate for tomorrow.
- 10 of ~15 screened names excluded on liquidity (premium in the tens/hundreds of dollars).

## Watch / Stood-down

### OI_FADE — two clean names, both REGIME-blocked (the session's most important item)

| Ticker | Price | 20d $-ADV | rel_build | persist | catalyst_split | Fundamentals | Binding constraint |
|---|---|---|---|---|---|---|---|
| **UTHR** | $538.84 | $240.9M | 1.31 | 1.031 | LIVE (67.2% post-08-05 print) | **CONFIRM** | Hard Rule #2 (regime) |
| **USFD** | $108.88 | $276.8M | 2.42 | 1.074 | LIVE (94.5% post-08-06 print) | CAUTION (−1) | Hard Rule #2 (regime) |

**UTHR is the cleanest short on file in over a week.** Fundamentals actively *support* the fade: Q2
revenue missed on flagship Tyvaso against competitive pressure, the stock fell ~7.5% on the print, and
insider MSPR is −31.76 with net selling in 19 of 20 months. The crowd is building calls into a name
whose growth driver just cracked.

**USFD is the weaker of the two** despite the larger build: its Q2 was a genuine beat with FY guidance
reaffirmed and three same-day price-target raises. That makes the call-OI build partly *justified*
rather than pure crowd-chasing — CAUTION, −1 tier.

- **NXPI — cut on MECHANISM, not regime.** Cleared every scripted gate (rel_build 1.61, earnings 10-26
  clear, catalyst_split LIVE 98.6%) but the build is 98.6% single-day, coincident with a market-wide
  rally, while NXPI is named in *unresolved* M&A speculation as the acquirer of Ambarella (FT, 07-31).
  This is the AZN precedent from 08-05 — the 7-gate stack passes rumor-driven builds and
  `catalyst_split` reads them LIVE. Cut.
- **Phase A's mega-cap pre-screen was invalid and was discarded.** NVDA/AAPL/AMZN/META/PLTR et al. show
  rel_build 0.04–0.26 against a top-15 cohort floor of ~1.3 — 2–20× below the bar. Huge absolute call
  OI, trivial relative build: the mega-cap beta trap CLAUDE.md warns about. None should have been
  candidates.
- **EXLS / UCTT re-checked** (both were the 08-05 near-misses): EXLS rel_build decayed 0.964 → 0.956
  and never re-inflated — mechanism dead. UCTT collapsed 0.982 → **0.28** — decayed out of the cohort
  entirely. Neither is a live candidate.

### MOM_LONG — 3-name basket, blocked on TIER MATH

ABNB ($178.07, 99.4% of 52w range, Consumer Cyclical) · NTRA ($322.10, 99.5%, Healthcare) ·
FIVN ($33.99, 99.5%, Technology). Sector cap (gate #7) satisfied at 33% each; HALO dropped to enforce it.

**Binding constraint is arithmetic, not regime:** MOM_LONG's measured excess is **+0.23%**, below the
**+0.30%** MEDIUM-tier bar — watch-only before any other gate is consulted. Reinforced by the negative
median (tail-driven distribution) and the risk-sizer's DURABLE-N bar, which a 3-name basket does not clear.

All three catalysts are real, which is worth recording even though nothing sizes:
- **ABNB** (+17.43% today, the tape's top mover) — a genuine re-rating, not a squeeze: Q2 beat +7.29%,
  bookings accelerating, FY26 raised. But insider MSPR **−70.98**, worst in the batch, selling in 17 of
  20 months, into a 42.6× P/E at a fresh high. CAUTION (−1).
- **NTRA** — revenue +37.7% YoY on record oncology volumes, 7 same-day PT hikes; but insider MSPR
  −61.28 and still unprofitable (net margin −9.05%). CAUTION (−1).
- **FIVN** — beat, raised sales guide, S&P SmallCap 600 inclusion as mechanical demand, insider neutral.
  **CONFIRM (0)** — the only clean long. Caveat: GAAP EPS guidance was *cut*, and part of the move is
  index flow whose durability past the inclusion window is unproven.

### MOM_SHORT — TTD only, triple-blocked

TTD ($13.80, 2.2% of 52w range, −21.90% today) is blocked by (1) `s1_standdown`, (2) the invariant-#6
watch-only cap on new starters, and (3) the negative −0.0008 baseline. POST excluded on a prior VETO
(07-29); **PLTD excluded as an inverse leveraged ETP** — the ETP leak the `issue_type` filter exists to
catch.

### Advisory lanes — surfaced, structurally never size

- **S2 (liquidity-reversion):** **TXN** (DP $980.8M, 96.2% buy-side, ADV $2.25B) and **RTX** ($529.5M,
  95.1%, ADV $1.14B). Both passed the full gate stack including the trading-day earnings window.
- **S4 (sentiment-contrarian):** 26 names post-gate, led by LPX (PCR 25.59), BRZE (25.21), TENB (17.18),
  HUBB (16.26), URBN (15.88). 11 ETFs cut, 1 on earnings, 6 on prior verdicts. Plus a separate
  18-name `ivrank_chg_5d` h3 tilt list (AEO, RBRK, PL, CM, HPQ…). S4 remains the only lane positive
  **forward as well as historically**.
  *Data-quality flag:* the lane returned hallucinated company-name annotations (e.g. "SN — Snap Inc",
  actually SharkNinja; "MTZ — Mitsubishi UFJ", actually MasTec; "CPRT — Carpetright", actually Copart).
  The PCR figures come from the panel and are sound; **the name labels are not** and have been stripped.

## Risk

- **Correlation clusters:** trailing-3-month pairwise (2026-05-01→08-07, n=68) — ABNB–NTRA **0.55**,
  everything else ≤0.32. Nothing clears the 0.70 collapse threshold.
  **FAIL-CLOSED FLAG: USFD and FIVN are absent from `data/prices.parquet`** (the frozen 785-name
  universe — `prices-parquet-coverage-gap`). The USFD↔UTHR pair and FIVN's exposure to ABNB/NTRA are
  **unverified, not confirmed-independent**. Moot tonight since neither lane sizes, but this must be
  resolved before either is ever promoted.
- **Event calendar inside the h10 window:** **CPI 2026-08-12** and **PPI 2026-08-13** (both Tier-1),
  plus FOMC minutes 08-19 at day 8 of 10. Any h5/h10 position opened tonight would carry both prints —
  worth an additional −1 tier on anything sized. NFP landed this morning and is already in the tape.
- **Tail caps applied:** MOM_LONG's negative median (tail-driven, basket-only, never per-name HIGH);
  OI_FADE's short-on-an-up-biased-tape starter cap; the vol sleeve's unsampled left tail, which is what
  the net-of-cost LOW-VIX read is protecting against.
- **Hedge note:** book is flat — nothing to hedge. The breadth-vs-flow divergence (63.8% green tape vs
  37.7% bullish flow) is a distribution tell carried into sizing discipline, not a veto.
- **What to watch tomorrow:** (1) whether the stand-down margin resumes decaying or holds near +1.0pp —
  it flattened tonight, which *delays* rather than accelerates OI_FADE's re-opening; (2) whether USFD
  and UTHR hold their builds through another session; (3) SPY's spot-vs-flip cushion, thin enough that
  the vol regime could flip back overnight.

---

*Standing note: tomorrow is the due date for `/calibration-audit` (2026-08-08). The post-hygiene-fix
OI_FADE h10 cohort matured 08-03→08-07 — that audit is the first that can grade the current engine, and
the test of the −3.73% forward-decay signal. Because the lane produced zero starters across that entire
window, neither USFD nor UTHR adds a resolvable row to it.*
