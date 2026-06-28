# 10 — Independent Truth Set (Phase 1 checkpoint)

_Look-ahead-safe forward-outcome substrate, re-derived from raw OHLC. Everything downstream (Phase 2 edge, Phase 5 retro harness) joins against these three files. Independent of `/calibration-audit`._

## 1.1 Artifacts (in `data/`)
| File | Shape | Contents |
|---|---|---|
| `universe.json` | 785 tickers | activity-ranked candidate funnel ∩ liquid floor + benchmarks/ETFs |
| `prices.parquet` | 87,277 rows · 783 tickers | Yahoo **chart-API** daily OHLC + adjclose + volume, 2026-01-15→06-26 (2 tickers failed fetch) |
| `returns.parquet` | 610,939 rows (long) | per (ticker, date, horizon): `fwd_ret, spy_ret, excess, mfe_pct, mae_pct, atr14, R_pct, resolved, long_R_win, short_R_win` |
| `build_*.py` | — | reproducible builders (stdlib + duckdb; rerun to refresh) |

**Horizons** (trading days): `1, 3, 5, 10, 21, 42, 63` ≈ 0DTE/next-session · swing-3 · weekly-5 · swing/weekly-10 · LEAP-1mo · 2mo · 3mo.
**Excess = fwd_ret − SPY_same-window_ret** (total return, adjclose). Validated: SPY self-excess = 0.000 at every horizon.
**Path-aware ±1R**: `R = 0.5·ATR(14, true-range)` at T; `long_R_win` = MFE≥R ∧ MAE>−R over (T+1…T+h) (approximate — MFE/MAE based, not first-touch-ordered; treat as secondary to continuous excess).

## 1.2 Panel structure — two blocks, one big unsampled month
54 panel sessions, all valid Yahoo trading days, in **two contiguous blocks** split by a data-export gap:
- **Block A:** 2026-03-13 → 2026-03-27 (~11 sessions)
- **GAP:** 2026-03-30 → 2026-04-24 (19 trading days, **no panel data**)
- **Block B:** 2026-04-27 → 2026-06-26 (~43 sessions)

Forward returns are computed on the **real continuous Yahoo calendar**, so block-A signals resolve their forward windows *through* the gap correctly (Yahoo has the April prices). We just can't generate *signals* during April.

## 1.3 Regime map (re-derived from SPY, the H10 test)
| Sub-period | Sampled? | SPY return | Character |
|---|---|---|---|
| Block A 03-13→03-27 | ✅ panel | **−4.3%** | selloff into the March low |
| Gap 03-27→04-27 | ❌ unsampled | **+12.8%** (low 632 → high 715) | violent V-recovery melt-up |
| Block B1 04-27→06-12 | ✅ panel | **+3.7%** | the grind-up **the rubric was fit on** |
| Block B2 06-15→06-26 | ✅ panel | **−3.4%** | TRANSITIONAL pullback (semi/HBM selloff) |
| **Whole window** | — | **+10.1%** | net up, but the up came mostly in the unsampled gap |

So the sampled tape contains **three distinct directional regimes** (down / up / down) — enough to demand every edge survive a cross-regime split, but thin per stratum (A≈11d, B1≈33d, B2≈9d). The biggest up-move (April) is invisible to signal construction, which *reduces* long-side over-fit risk but also means we never see signals fired into the strongest rally.

## 1.4 ⚠ The decisive asymmetry: the SPY base rate is steeply long-biased
Over the **sampled** forward windows, a same-direction SPY bet wins:

| Horizon | SPY **up**-rate (long base rate) | SPY **down**-rate (short base rate) |
|---|---|---|
| h=1 | 0.58 | 0.42 |
| h=3 | 0.63 | 0.37 |
| h=5 | 0.68 | 0.32 |
| h=10 | 0.71 | 0.29 |

**Consequences that govern all of Phase 2:**
1. **Raw hit-rate is a trap on the long side.** A long signal hitting 65% at h=5 is *below* SPY's 68% — **negative edge dressed as a coin-flip-plus.** This is exactly the "calibrated-but-beta" failure the repo's own C21/C2 gates were built to catch; our truth set reproduces the condition that makes it bite.
2. **The short side is scored on a brutal base rate** — SPY fell only 29–32% of the time at swing horizons. A bearish signal that wins **45%** at h=10 is **+16pp of excess hit-rate** over the short base rate. This is precisely why the 2026-06-23 envelope's NVDA short showed `win_rate 0.4519` (looks like a loser) yet `market_excess +0.1852` (is a strong edge) — and why the additive rubric, which scores on raw confluence not excess, **systematically under-rates the short book.** (Direct support for **H1**.)
3. **Therefore the primary edge metric is `excess`, never raw WR**, and every class must be reported with its same-window SPY base rate beside it. Hit-rate is kept only as `P(excess>0)`.

## 1.5 Resolution budget (how much truth we actually have)
Resolved-fraction by horizon, all dates (panel-day-restricted numbers are lower for long h because the last panel day is 06-26):
`h=1: 0.99 · h=3: 0.97 · h=5: 0.96 · h=10: 0.91 · h=21: 0.81 · h=42: 0.62 · h=63: 0.44`.

Practical confidence tiers for Phase 2:
- **h ∈ {1,3,5,10}** — well-resolved across all three regimes → **primary** horizons for edge claims.
- **h = 21 (≈1mo LEAP/swing)** — resolved through ~late May → **secondary**, moderate N.
- **h ∈ {42,63} (2–3mo LEAP)** — only early/mid-window signal-days resolve → **report but flag low-confidence; never a standalone durable-edge claim.** 90D LEAP claims are effectively unverifiable on this panel (only Block A resolves) and will be labeled INCONCLUSIVE.

## 1.6 Look-ahead protocol (enforced in every Phase-2 join)
- A signal on day **T** is constructed from panel rows with `date ≤ T` only (these EOD exports are themselves as-of-close T).
- Its outcome is read from `returns.parquet` at `(ticker, T, horizon)` — all forward bars are `date > T`.
- Unresolved (forward bar missing) → **INCONCLUSIVE**, excluded from win/excess denominators; never a loss.
- Min decided-N ≥ **30** to call an edge *durable*; 10–29 → *provisional*; <10 → *anecdote* (reported, never actioned).
- **FDR control:** Benjamini-Hochberg at 0.10 across the full class/tool sweep before any 🚩.
- **Regime stratify** every headline number across {A, B1, B2}; an edge that flips sign across the 06-12 break is beta, not alpha.

## 1.7 Status
Truth set complete and validated. → **Phase 2**: per-source signal extraction joined to this matrix, ranked by excess / hit-rate-vs-base / IC, then mapped to fleet agents + rubric components. Parallel sub-agents per source; Opus synthesis.
