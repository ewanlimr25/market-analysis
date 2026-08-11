# Market Scan — 2026-08-10

## Regime & Verdict

- **Regime: UPTREND** · ret5 **+2.030%** · ret10 **+4.590%** · dd15 −1.300%
  (`regime_check.py`, arbitration exit 0 — Phase A's claim reproduced against the panel)
- **vol-state:** VIX 15.46 (LOW tercile), normal contango VIX9D 12.77 < VIX 15.46 < VIX3M 18.98.
  SPY dealer gamma **NEGATIVE**, spot 772.87 pinned at the 773.02 zero-gamma flip — whipsaw risk at
  this level, not suppression. (Aggregate GEX nets +$1.84B; the *regime* call is spot-vs-flip. The two
  stay separate.)
- **breadth:** pct_green 45.7% (230 adv / 270 decl), options-flow bullish 34.9%. **Divergence flagged** —
  a firm UPTREND tape with sub-50% breadth and net-bearish flow. Rotation OUT of Technology (−$279.9M),
  INTO Financials / Healthcare / Energy. Advisory, not a veto.
- **`directional_tradable` = True** · **`s1_standdown` = False**
  The crash guard was live all five sessions 08-03→08-07 (thrust peaked ret5 +5.53% on 08-05) and expired
  only today as ret5 decayed +5.53% → +3.51% → +2.03%. **The guard lifting is not a green light** — the
  deceleration is recent and shallow.
- **Event risk inside the h10 window:** **CPI 2026-08-12**, **PPI 2026-08-13** — both Tier-1, both landing
  on days 2–3 of any window opened this week. FOMC 09-16/17 is outside.

> **Bottom line: no directional edge sized tonight — a NINTH consecutive zero-starter session, and the
> book stays flat for a sixth.** One name (COO) survived the entire mechanical stack and was cut to WATCH
> on tier math. Two others died on hygiene, one of them via a boundary defect this scan found and fixed
> the read on.

## Directional Book (excess-scored)

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| COO | OI_FADE | short | h10 | +0.0055 mean / +0.0091 med (hit 0.55 vs 0.38, n=1102) | 0.35 | **watch** | n/a — no live entry. Reference if promoted: reclaim above ~$80.50, or an upgrade reversing the UBS Neutral thesis | regime PASS · liquidity PASS ($76.32, $-ADV $148.5M) · cluster PASS · **fundamentals CAUTION (−1 tier)** · **event-risk CAUTION (CPI/PPI)** · tail-cap N/A |

**Tier math, stated plainly:** OI_FADE's measured excess is +0.55% mean, which sits in the **MEDIUM** band
(+0.3–1%), not HIGH (≥ +1%). MEDIUM implies a *starter*. The fundamentals **CAUTION** takes one tier off →
**WATCH**. The event-risk CAUTION would have imposed the same −1 independently. COO was never reachable for
a half-cap HIGH size; it did not clear the +1% bar. Invariant #4 was not the binding constraint — tier math was.

COO's mechanical case was genuinely clean, which is why it got this far: 5d net call-OI build **+4,619**
(call +4,615 / put −4), `rel_build` 1.029, `persistence` 0.549, and a build that is really multi-day rather
than one block — dailies **+148 / +2,534 / +1,002 / +13 / +18 / +1,052** across 08-03→08-10, re-derived
directly rather than taken from the lane. Next print 2026-09-09, clear of the whole window.

The countervailing read is real: 4/4 EPS beat streak and insider MSPR +40.33 (net buying) both *contradict*
a short, while −42.6% YoY EPS growth on a ~63× trailing P/E and UBS initiating **Neutral at a $75 PT below
the $76.32 spot** both *confirm* it. Short float 4.08% / 2.82 days-to-cover — no squeeze fighting an entry.
A split verdict, correctly resolved as CAUTION rather than VETO. Healthcare being tonight's rotation-IN
sector is a further headwind for a Healthcare short (carried in `regime_fit` 0.35, not as a gate).

### Killed upstream — recorded so they are not re-proposed

- **EWTX — CUT.** `catalyst_split.py` reported **"LIVE 83.0%"**, and that number is an artifact. See Data
  Quality below. Genuine post-print continuation is **+387 of +8,490 = 4.6%** — the build **died at its
  catalyst**. This is the SSNC pattern the script exists to catch, and it very nearly passed. EWTX also
  carried a prior blocking verdict and a documented `next_earnings_date` staleness flag from the 08-06 scan.
- **AVT — VETOED (fundamentals).** The full triad fights the short: 4/4 *accelerating* beats
  (+2.26% → +9.15% → +11.01% → +27.50%), revenue +24.5% YoY, EPS +46.1% YoY, insider MSPR +52.37, Truist
  PT raised to $110 (+13% above spot) the same day as the beat, and the stock −2.6% off its 52-week high
  *printing fresh highs rather than fading*. The OI lane flagged this itself as the AVTR pattern —
  shorting a completed gap that held, with fundamentals confirming the new level — and held it out of
  sizing before the gate confirmed the kill.

## Vol Book (non-directional)

**0DTE-VRP — STAND ASIDE, both legs, on economics rather than mechanics.**

| | gamma read | LOW-tercile conditional (gross) | net of 0.1% RT cost |
|---|---|---|---|
| SPY | dealer gamma **SHORT**, spot pinned at flip 773.03 | −0.019% | **−0.119%** |
| QQQ | sources **disagree** (CLI positive vs local flip short) → fail closed | +0.043% | **−0.057%** |

The pooled headline (`mean_pnl_open_net_pct` +0.26%) is a MID/HIGH-VIX artifact. Tonight's actual bucket is
LOW (VIX 15.46, tercile cuts 16.4/17.9), and the conditional expectancy is **negative net of cost on both
names**. Two independent reasons converge on each leg — gamma regime *and* conditional economics.

**Earnings IV-crush — advisory only, never sized** (no backtested crush harness in this repo; the case rests
on structure alone):

| Name | Print | IV rank | Implied move | Term structure | Note |
|---|---|---|---|---|---|
| CSCO | 08-12 | 90.6 | 6.81% ($8.35 on $122.57) | backwardation 2.06× | deepest book of the four |
| CAVA | 08-11 | 85.9 | 11.03% ($6.79 on $61.58) | backwardation 2.03× | genuinely fat tail — do not narrow wings for premium |
| CAH | 08-11 | 81.3 | 5.69% ($13.50 on $237.18) | backwardation 2.14× | adequate liquidity |
| ENVX | 08-12 | 84.3 | 14.94% ($0.69 on $4.64) | **noisy calc — data-quality flag** | thin book, sub-$5 strike granularity; skip or fractional |

**Macro overlap caveat:** CSCO and ENVX print *on CPI day*; CAVA and CAH have PPI inside their exit window.
Single-name IV will not fully revert to a quiet post-print baseline while a Tier-1 macro print is still
pending — that argues for **wider wings and lower size**, not tighter ones.

## Watch / Stood-down

- **MOM_LONG — BASKET_WATCH, never sizes.** 240-name near-52w-high basket; top sector Financial Services
  70 names (29.2%), inside the 1/3 cap. Lane at **−1.12% mean, n=1081** tonight. The full-universe refresh
  turned this lane outright negative, corroborating the forward BH(0.10)-negative read; 0 of 52 resolved
  forward calls have ever sized.
- **MOM_SHORT — watch-only capped.** 7 Yahoo-verified near-52w-low names: **PEG, AMRZ, CMS, VICI, GME,
  AGCO, RBA** (POST and GPI dropped on split/adjustment artifacts — exactly the false-short class the
  verification step exists for). Lane at **−1.26% mean, n=805, hit−base only +0.031**. First session since
  07-29 that `s1_standdown` is not the binding reason — the standing invariant-#6 cap is. Note the utilities
  pair (PEG, CMS) plus RBA/AGCO industrials for correlation if this lane ever promotes.
- **S2 — advisory only.** 48 clean survivors. Lane **+0.0007, n=1138, hit−base −0.058** — winning *less*
  often than its own base rate. Regime is actively unfavourable: S2 wants weak tapes and flight-to-liquidity,
  and this is a strong uptrend.
- **S4 — advisory only.** 17 clean survivors: LYG, GGG, RHP, ACA, LH, INCY, IMAX, VSNT, LBRT, BWA, EXEL,
  JXN, GFI, LNC, QSR, CSGP, MDLN. Lane **+0.0039, n=1160** — the only lane positive both historically and
  forward, and still advisory. The extreme PCR tail is real (LYG 1023.6 on 8,189 puts vs 8 calls).

## Risk

- **Correlation clusters:** none live — the book is flat and COO is unsized. Nothing to collapse.
- **Held book:** `analyses/scan/2026-08-07/conviction_2026-08-07.json` → **0 open positions**, verified by
  reading the file directly rather than trusting the tool's empty result (the `held_book` EXIT-substring
  false-empty was explicitly ruled out).
- **Event calendar:** CPI 08-12, PPI 08-13 inside the horizon; FOMC 09-16/17 outside.
- **Tail caps applied:** none needed — nothing sized. OI_FADE is not in the tail-capped lane list.
- **Hedge note:** no exposure to hedge.
- **Standing forward caveat (informational, not a cap):** OI_FADE's decay question is still unresolved.
  The −3.73% new-evidence flag reversed to +1.99% / hit−base +0.67, but on 9 units across only **3 exit-days**
  — ANECDOTE-level N, durable in neither direction. 17 open h10 rows mature 08-10→08-21.

## Data Quality

**`catalyst_split.py:98` — post-catalyst boundary is inclusive of the print day. Load-bearing tonight.**

```python
post = sum(d["call_net"] - d["put_net"] for d in daily if d["date"] >= cat)
```

The `>=` counts the **print date itself** as post-catalyst. But the OI panel's row dated `D` measures
`last_date = D−1 → curr_date = D` — it is the change settled *into* the morning of D, i.e. positioning
established at or before the print, never after it. Verified against the panel for EWTX: the 08-06 file
carries `last_date 2026-08-05, curr_date 2026-08-06`.

Effect on EWTX: **+6,668 of the +7,047 "post-catalyst" build is the print day itself.**

| boundary | post-catalyst net | share | verdict |
|---|---|---|---|
| `>=` (as the script computes) | +7,047 | 83.0% | LIVE — *build continued* |
| `>` (strict) | **+387** | **4.6%** | **DIED at its catalyst** |

The two readings are opposite, and the inclusive one would have put a dead build into the sized book.
Any fix must patch **both** `catalyst_split.py` **and** any inline re-implementation in
`retro_harness.py` — the harness imports nothing and re-implements the gates, so patching only the lane
script makes the live engine more permissive than the instrument grading it.

Carried forward, unfixed tonight (also affects the same class of check):

- **`earnings_gate.py` one-sided bound** — the window check compares `ned.isoformat() <= end` with no
  lower-bound check (first recorded 2026-08-06). Nothing turned on it tonight; both names were
  fail-closed either way.
- **`prices.parquet` unpriced names (22/2,471)** — ACLX, AL, APLS, BK, CFLT, CTRA, CUK, DAWN, EXAS, FOLD,
  HOLX, IAC, NGD, OS, PSTG, SEE, SLNO, TERN, THR, TPH, VRE, VSCO. These **fail closed** downstream.
- **QQQ zero-gamma level field looked stale** in the Phase A read (220.46 against a 721.2 spot); the
  0DTE script's own flip calc disagreed with the CLI. Treated as fail-closed rather than resolved.

## Housekeeping

Truth set was **3 sessions stale** at preflight (parquets ended 08-07) and was rebuilt in order — prices
→ returns → features → weekly_features — before any lane ran. `universe.json` was deliberately **not**
rebuilt: refreshing the spine mid-cycle would change the universe the 2026-08-08 baseline was measured
against, and a baseline compared across two universes is not a comparison. Preflight re-run clean (exit 0).

**Regression gate** (`retro_harness.py --all`, panel now 84 days, 2,471-ticker spine) — no code changed
tonight, only data, so this is panel growth by construction:

| lane | baseline (83d) | tonight (84d) | Δ |
|---|---|---|---|
| MOM_LONG | −0.0108 (n=1066) | −0.0112 (n=1081) | −0.0004 |
| MOM_SHORT | −0.0128 (n=803) | −0.0126 (n=805) | **+0.0002** |
| OI_FADE | +0.0059 (n=1087) | +0.0055 (n=1102) | −0.0004 |
| S2 | +0.0009 (n=1123) | +0.0007 (n=1138) | −0.0002 |
| S4 | +0.0035 (n=1145) | +0.0039 (n=1160) | **+0.0004** |

All five within ±0.0004 on a ~15-row increment, two of them up. **No regression** — and with zero code
delta, the "old code, new data" isolation check is satisfied trivially.
