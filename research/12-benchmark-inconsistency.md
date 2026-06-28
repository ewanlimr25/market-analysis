# 12 — Method finding: the single-leg-whale "+22pp" uses an UNCONDITIONAL benchmark (selection-inflated)

_A code-reading + truth-set finding, independent of the Phase-2 fan-out. This is the first concrete independent-vs-audit disagreement, and it resolves in the truth set's favour._

## The claim under audit
The repo's C19 single-leg-whale promotion gate rests on `scripts/single_leg_whale.py:backtest()`:
> Tier-1 `OPENING_PUT_PRIME` WR 63.5% **+26pp vs SPY**, p<0.001 (n=266); `FLOOR_PUT_BLOCK` 61.0% **+23.5pp** (n=328).

## The bug: the benchmark is unconditional
`single_leg_whale.py` lines 388–398 build the SPY baseline as:
```python
for (d0, d1) in pairs:          # pairs = ALL consecutive trading-day pairs in the panel (not signal days)
    if s1 < s0: spy_put_wins += 1
spy_put_wr = spy_put_wins / spy_n     # fraction of ALL day-pairs where SPY fell
...
put_excess = put_win_rate - spy_put_wr   # signal WR minus the UNCONDITIONAL SPY-down rate
```
So `excess` subtracts the **unconditional** SPY-down rate (over every day in the window) from a win-rate measured **only on the days the signal fired**. The put signal **clusters in down-tape** (truth-set pilot: 226 of 451 Tier-1 opening-put ticker-days fall in the 11-day March selloff, Regime A). On those clustered days SPY fell far more often than on an average day, so the unconditional baseline is biased *low* and the "excess" is inflated by exactly the signal's selection into falling markets.

## Why this is internally inconsistent
The repo's own `/calibration-audit` **C21** defines the honest benchmark differently and correctly:
> realised benchmark-excess = realised WR − **SPY same-window same-direction WR**, where `spy_benchmark_win` = the fraction of **that class's rows** whose same-day SPY bet won.

C21 is **per-row / conditional-on-signal-day** — it nets out the down-tape clustering. The standalone `single_leg_whale.py` ignores C21 and uses an unconditional baseline. **Two benchmarks in the same repo disagree, and the live C19 gate cites the inflated one.**

## Truth-set replication (conditional benchmark = correct)
Our `edge.py` uses the conditional same-day SPY benchmark (the C21-correct one). Pooled Tier-1 `OPENING_PUT_PRIME` (short), n≈395–468:
| h | hit P(underperform SPY) | base = conditional SPY-down rate | hit−base | mean_exc | p |
|---|---|---|---|---|---|
| 1 | 0.54 | 0.55 | −0.01 | +0.0012 | 0.53 |
| 3 | 0.53 | 0.68 | −0.15 | +0.0005 | 0.87 |
| 5 | 0.55 | 0.68 | −0.13 | +0.0021 | 0.58 |
| 10 | 0.54 | 0.63 | −0.08 | −0.0042 | 0.43 |

Against the **conditional** benchmark the pooled signal has **~0 mean excess and a hit-rate at/below base** — i.e. shorting these names did **no better (often worse) than just shorting SPY on the same days**. The "+22–26pp" is substantially a **down-tape selection artifact**, not a tradable edge, *as pooled*.

## What is NOT yet resolved (handed to the Phase-2 flow agent)
The pooled refutation does **not** kill the signal outright. Still open and being measured by `sig_flow`:
1. Does the edge concentrate in a **sub-tier** (FLOOR_PUT_BLOCK vs PRIME; OTM-only delta∈[−0.35,−0.05])?
2. Does it survive in a **single regime** (B1 uptrend showed hit−base **+0.186** at h=5 even as mean_exc went negative — a few squeezes blew up the mean; asymmetric)?
3. Does the **opening (size/OI≥2) CALL** side carry long edge (Pan-Poteshman: opening *buys* of either type predict)?
4. Does conditioning on **hard-to-borrow / high short-interest** (Johnson-So channel, via `fz`) isolate a real put edge?

## Implications for the redesign (preliminary)
- **Any edge claim must use the conditional (C21) benchmark.** Adopt `edge.py`'s `base`/`hit_x_base` everywhere; never quote a raw WR or an unconditional excess. → Phase-4 design rule.
- **Fix or retire `single_leg_whale.py`'s benchmark** before its number is ever cited again (it gates C19). → MIGRATION item.
- The redesign should **not** promote the pooled single-leg-put line on the strength of the inflated +22pp. Whether a *conditioned* version earns a line depends on the flow agent's sub-tier/regime breakdown (Phase 2) + external validation (Phase 3).

> Cross-check status vs `/calibration-audit`: the audit's C21 **agrees with our truth set** (conditional benchmark); the standalone backtest script disagrees with both. The audit's *prose* still repeats the script's inflated headline in the C19 section — that headline is the thing to correct.
