# PROVENANCE & EVIDENCE AUDIT

_"Is everything backed by actual facts and evidence?" — a scrupulous trace of every input, computation, and claim, with an explicit verification tier for each. Written to be checkable: every number below can be reproduced by the command listed._

## 0. Verdict up front (read this first)
- **All quantitative claims are real and reproducible.** I just **independently re-ran my own `edge.py`** against the sub-agents' signal files and **every headline number reproduced exactly** (§3). The truth-set math is self-checked (SPY self-excess = 0.000). The retro-harness numbers I ran myself.
- **The computations are Tier-1 trustworthy. The external *citations* are Tier-3** — they come from WebSearch sub-agents. The papers are real and the *broad mechanisms* I can corroborate from my own training, but I have **not fetched and line-by-line verified each paper's exact quote/page/statistic.** Treat citations as "well-established direction, attribution not independently audited."
- **No claim in the deliverables is fabricated**, but several rest on a **small sample** (54 sessions, one 3.5-month episode) and a few on **tiny n** (old-system HIGH n=6). Those are disclosed in the docs and re-listed in §7.

### Verification tiers used below
- **T1 — I built it and/or ran it myself in the main loop** (fully verified, reproducible now).
- **T2 — a sub-agent computed it; I re-verified the headline numbers** by re-running my own `edge.py` on the agent's on-disk signal file (number↔file consistency confirmed; the agent's *extraction SQL* I did not line-by-line audit).
- **T3 — external literature via WebSearch sub-agent** (real papers, broad mechanism corroborated from training, exact attribution NOT independently fetched/verified).

---

## 1. DATA FILES USED (inputs)
| File / source | Role | Verification |
|---|---|---|
| `~/Documents/Stocks/{All Options, Dark pool, Hot Option Chains, OI changes, Stock Screener}` — 5×54 parquet | the raw panel | **T1** — schemas read directly via DuckDB; row counts, columns, date range, the 2026-03-27→04-27 gap all confirmed by query (`RESEARCH/00 §0.1`, `10 §1.2`) |
| Yahoo **chart API** (`query1.finance.yahoo.com/v8/finance/chart`) | OHLC for the truth set | **T1** — fetched 783 names myself; SPY self-excess=0.000 proves the join; the audit's own C20 uses the same source |
| `uw` CLI / `fz` CLI | tool availability + spot data | **T1** — `--help`, `available-dates`, schema probes run directly |
| `uw-daily-analysis/` (commands, agents, `AUDIT.md`, `single_leg_whale.py`, `decision.json` files) | the subject being graded | **T1** — read directly; the benchmark bug in `single_leg_whale.py:388-398` I read line-by-line (`RESEARCH/12`) |

## 2. SCRIPTS I WROTE (computation, all T1)
| Script | Computes | Self-check |
|---|---|---|
| `data/build_prices.py` | Yahoo OHLC cache (783 names) | 87,277 rows / 783 tickers; 2 fetch fails logged honestly |
| `data/build_returns.py` | forward return, **excess vs SPY**, MFE/MAE, ATR, path-±1R, 7 horizons | **SPY self-excess = 0.000 at every horizon** (the key correctness proof) |
| `data/edge.py` | the shared conditional-benchmark resolver (mean_exc, hit, base, IC, p) | validated on the slw pilot I built independently; IC bug found & fixed mid-build (visible in the transcript) |
| `artifacts/retro_harness.py` | fires the redesign per day, resolves realized excess, compares to old `decision.json` | I ran `--all --compare-old` myself; numbers in `RESEARCH/50` |
| `data/` PR-1 sector + S1-carry tests | follow-ups | I ran both myself; `RESEARCH/60` |

## 3. RE-VERIFICATION OF THE SUB-AGENT NUMBERS (T2 → upgraded)
I re-ran `edge.py` on the agents' on-disk signal files. **Every headline reproduced exactly:**
| Claim (as written in `RESEARCH/20`) | Re-run result | Match |
|---|---|---|
| S1 `NEAR_52W_LOW` short h10: +0.0092, hit 0.554, base 0.344, hit−base +0.211, p~0 | +0.0092 / 0.554 / 0.344 / +0.211 / p≈0 | ✅ exact |
| S4 `PCR_HIGH_LONG` h5: +0.0059, hit 0.525, base 0.525, p=0.004 | +0.0059 / 0.525 / 0.525 / p=0.0044 | ✅ exact |
| H1 `OPENING_PUT_PRIME` short h5: +0.0021, hit 0.55, base 0.68, hit−base −0.13 | +0.0021 / 0.554 / 0.681 / −0.126 | ✅ exact |
| `FLOOR_PUT_BLOCK` short h5: hit−base −0.11 | −0.111 | ✅ exact |
| `DEX_FLIP_BEAR` short h10 (anti-signal): −0.0151, p=0.0032 | −0.0151 / p=0.0032 | ✅ exact |
| `DEX_LEVEL_POS` long h10 (right-skew beta): +0.0034, hit 0.473, base 0.583, p=0.0004 | exact | ✅ |
| S2 one-sided-90% long h5: +0.0099, hit 0.551, base 0.408, hit−base +0.143, p~0 | exact | ✅ |
| Old system: HIGH n=6 **−8.17%** 0-for-6; MED n=15 −7.36% | re-run by me in `retro_harness` (T1) | ✅ |

**What this proves:** the reported numbers are faithful to the data, not invented. **What it does NOT prove:** that every agent's *signal definition* is the optimal/only-correct one — the extraction SQL embodies threshold choices (e.g. "block ≥ 50k shares", "ask-side") that I specified in the prompts and the agents implemented; I independently re-derived only `OPENING_PUT_PRIME` from scratch (it matched). The other 44 definitions are reasonable and prompt-specified but not each independently re-coded.

## 4. TECHNIQUES / METHODS — computational vs researched
### Computational (T1, mine)
- **Excess-vs-SPY on a conditional (same-day) benchmark** — the C21-correct method; this is *my* construction, fully in code.
- **Look-ahead discipline** — signals on date ≤ T, outcomes from date > T (enforced by the join in `edge.py`).
- **Regime stratification** A/B1/B2 — date-bucketed in code.
- **Path-aware ±1R** — MFE/MAE-based; **approximate** (not first-touch-ordered) — disclosed in `RESEARCH/10 §1.1`.
- **Normal-approx p-values + BH/FDR humility, n≥30 durability floor** — in `edge.py` + applied in synthesis; the BH correction is *described and applied judgmentally*, not run as a formal FDR table (disclosed in `RESEARCH/20 §2.6`).
- **Spearman IC** — computed via DuckDB rank+corr (the nested-window bug I hit and fixed is in the transcript).

### Researched externally (T3, WebSearch sub-agents — NOT independently fetched)
Every paper named in `RESEARCH/30` (George-Hwang 2004; Pan-Poteshman 2006; Lakonishok-Lee-Pearson-Poteshman 2007; Ge-Lin-Pearson 2016; Baltussen 2021; Barbon-Buraschi; Nagel 2012; Lehmann 1990; Bollen-Whaley 2004; Garleanu-Pedersen-Poteshman 2009; Daniel-Moskowitz 2016; Vilkov 2024; etc.). **These are real papers and the broad findings match my training knowledge** — e.g. George-Hwang's 52-week-high momentum, Pan-Poteshman's "only opening flow predicts", and dealer-gamma-as-vol are genuinely established results. **Caveat:** the precise quotes, journal/page citations, and the exactness of "+X pp / n=Y" attributions to a specific paper were produced by the search agents and **I did not open each PDF to confirm them.** Use them as direction-of-evidence, not as audited citations.

## 5. SUB-AGENT OUTPUTS — how they were obtained
- **Phase 2 (6 agents):** workflow **failed at the final filter** (one agent's StructuredOutput null). I **salvaged all 6 outputs from the transcripts** (`subagents/.../agent-*.jsonl`) and saved them to `data/phase2_*.json`. The signal *parquets* the agents wrote are on disk and I re-ran them (§3). So nothing was lost or invented despite the workflow error.
- **Phase 3 (6 agents):** completed cleanly; saved to `data/phase3_validations.json`.
- I did **not** take any agent's prose at face value for a headline number — the §3 re-runs are why.

## 6. DECISIONS → EVIDENCE TRACE
| Decision | Backed by | Tier |
|---|---|---|
| Cut accumulation +3 / multileg +2 / DEX +1 lines | `RESEARCH/20` (beta/noise) + §3 re-verified | T1/T2 |
| Cut `sector-rotation` | `RESEARCH/60 §6.1` PR-1, I ran it | **T1** |
| Close C19 single-leg-whale path | `RESEARCH/12` — I read the benchmark bug in source | **T1** |
| Excess-as-currency (D4) | `RESEARCH/10 §1.4` SPY base rates, I computed | **T1** |
| Add S1 relative-weakness lane | `RESEARCH/20`+§3 (measured) + `30 §3.1` (mechanism) | T2 num / T3 lit |
| Half-cap sizing (D5) | S1 right-skew/negative-median (`50 §5.3`, I ran) + unsampled crash | **T1** |
| "Redesign beats old system" | `retro_harness.py --all` — I ran it | **T1** |

## 7. HONEST SOFT SPOTS (where to be skeptical)
1. **Sample size.** 54 sessions, one 3.5-month episode; A/B1/B2 are sub-windows, not independent years (`RESEARCH/30 §3.2`). Sign-stability rules out *local* beta, not period-specific factors. **This is the #1 limitation** and is why everything is "provisional" and half-capped.
2. **Old-system comparison n is tiny** (HIGH=6, MED=15), drawn from the `analyses/daily/` folder (~19 days, late-window-weighted). The −8.2% is stark and corroborates the audit's own tier-inversion, but it is small-n.
3. **S1 is right-skew with a negative median** — a basket edge; per-name it's near coin-flip. Disclosed in `50 §5.3` and shown honestly (the 2026-05-18 sample envelope has S1 shorts *losing*).
4. **External citations are T3** (§4) — not independently fetched.
5. **Path-aware win flag is approximate**; BH/FDR applied judgmentally not as a formal table.
6. **Signal definitions embed threshold choices** I specified; only `OPENING_PUT_PRIME` was re-derived from scratch independently.
7. **The unsampled April melt-up + no VIX>30 day** mean the momentum-crash guard (S1) and the short-vol tail are theory-calibrated, not backtested (PR-2; `60 §6.4-6.5`).

## 8. How to reproduce any of this yourself
```bash
cd ~/Development/findings/data
python3 build_returns.py                                   # SPY self-excess == 0.000
python3 edge.py --signals sig_screener_dir.parquet --horizons 5,10 --min-n 30   # S1/S4
python3 edge.py --signals sig_alloptions.parquet  --horizons 5,10 --min-n 30    # H1 refutation
python3 edge.py --signals sig_gex_dex.parquet     --horizons 5,10 --min-n 30    # DEX anti-signal
cd ../artifacts && python3 retro_harness.py --all --compare-old                 # redesign vs old
```
Every table in `RESEARCH/` traces to one of these commands or to a `data/phase2_*.json` / `phase3_validations.json` file on disk.
