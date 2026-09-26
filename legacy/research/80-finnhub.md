# 80 — Finnhub fundamentals: can it add an honest edge? (Phase 8)

_Tested whether Finnhub data (the feed `stock-deep-dive` and the `fundamentals-gate` use) can give a standalone directional edge in `/market-scan`, beyond its current veto role. Point-in-time, look-ahead-safe (`finnhub_enrich.py` already filters records to ≤ date), measured in forward EXCESS with the same n≥30 / regime discipline. Why Finnhub is worth testing: PEAD and insider-clustering are **documented cross-sectional anomalies** — unlike options flow, which was beta._

## 8.1 What was tested (the two strongest, cleanly-dated anomalies)
- **PEAD** via `/calendar/earnings` (one call → every dated earnings surprise in the window; 446 events, 186 with usable estimate+actual). Priced the **full** earnings-reporter set (not just my funnel) so the test isn't selection-thin.
- **Insider sentiment (MSPR + 3-mo net share change)** via `/stock/insider-sentiment` for ~930 names (`fetch_insider.py`, throttled). Point-in-time: a month's insider data used only after that month ends.

## 8.2 PEAD — classic drift is ABSENT (sell-the-news), thin
Entry the day **after** the announcement (isolates drift, not the reaction); beat=long / miss=short; forward excess.
| Cut | h | n | mean_dir_exc | hit | median |
|---|---|---|---|---|---|
| ALL (beat-long/miss-short) | 5 | 149 | +0.0077 | 0.50 | −0.0014 |
| strong BEAT >5% (long) | 5 | 80 | +0.0020 | 0.47 | −0.0061 |
| strong BEAT >5% (long) | 10 | 63 | **−0.0100** | **0.44** | −0.0119 |
| MISS <−2% (short) | 5 | 47 | +0.0142 | 0.53 | +0.0018 |
| MISS <−2% (short) | 10 | 41 | +0.0034 | 0.54 | +0.0039 |

**Read:** textbook PEAD (beats drift up) **does not replicate** here — strong beats are flat-to-**negative** (−1.0% at h10, hit 0.44): a "sell-the-news / already-priced" regime. The only hint is an asymmetric **miss-side** drift (misses keep underperforming, +1.4% h5), but n≈47 — **below the durability floor.** h21 is unresolved (most earnings are April–June; +21 trading days runs off the panel). **No clean tradable PEAD edge on this window.**

## 8.3 Insider MSPR — NO edge, slightly wrong-signed, sparse
Cross-sectional rank-IC of trailing MSPR / 3-mo net insider change vs forward excess:
| Factor | h | IC | t | days |
|---|---|---|---|---|
| mspr | 10 | −0.026 | −2.4 | 44 |
| mspr | 5 | −0.017 | −1.5 | 49 |
| net3m | 21 | −0.013 | −1.8 | 33 |

Event test (h=10 forward excess): insider **BUY** (MSPR>50) long → **+0.002** (hit 0.50, nothing); insider **SELL** (MSPR<−50) short → **−0.013, loses** (the sold names *rose*). All |t| < 3; signs are weak and **opposite** to the Cohen-Malloy-Pomorski expectation. Coverage is also sparse — only **320 of 930** names had any insider transactions in the window. **No edge.**

## 8.4 Why both documented anomalies fail HERE (and what it means)
This is a **power** problem, not a refutation of PEAD/insider in general:
- **Slow anomalies, short window.** PEAD and insider drift play out over weeks-to-months and need **many events across regimes** to measure. A 3.5-month, single-episode panel with ~149 resolvable earnings events and a monthly insider signal has far too few independent observations.
- **Crude signal.** Finnhub MSPR is a monthly aggregate; Cohen-Malloy use an opportunistic-vs-routine insider **classification + clustering**, which MSPR doesn't capture.
- **Regime.** A beats-fade ("sell-the-news") tape is exactly the regime where naive PEAD underperforms.
So: consistent with the whole study's discipline — **I will not dress a thin/absent effect as an edge.** Finnhub does **not** earn a standalone directional alpha lane on this data.

## 8.5 Where Finnhub's value actually IS — the risk veto (keep it)
Finnhub's genuine, defensible contribution is the role the current `fundamentals-gate` (and `stock-deep-dive`) already use it for: a **risk veto**, not an alpha source. Cross-referencing a flow/momentum call against earnings deterioration, insider selling, and the news catalyst stack to **avoid sizing into a deteriorating name** is a *loss-avoidance* (risk) function — and it is exactly the right complement to the momentum lanes, which are tail-risky (S1 squeeze risk, `RESEARCH/30 §3.1`). The redesign **keeps `fundamentals-gate` unchanged** (Phase D veto on sized names).

**Caveat on the veto, too:** even its *effectiveness* can't be validated on this panel — the audit's own C24 needs ≥10 **decided** VETO'd names, which 54 sessions don't provide. So the veto is kept on **mechanism/insurance grounds** (don't trade flow that's actually distribution into a miss), labeled advisory until a longer panel validates it.

## 8.6 Design impact (updates DESIGN/40)
1. **Do NOT add a Finnhub alpha lane** — neither PEAD nor insider clears the bar on this data (§8.2–8.3).
2. **Keep `fundamentals-gate` as the risk veto** on sized names (Phase D) — unchanged; mechanism-justified.
3. **Pre-register PR-7:** re-test PEAD (SUE-standardized) + opportunistic-insider clustering on the **extended panel** (`RESEARCH/60 §6.5` — ≥2 earnings seasons, multiple regimes). These anomalies are real in the literature; this panel just can't see them. The cheapest enabling step is more history, which is already the #1 recommendation.
4. **Analyst revisions** (the third Finnhub/`fz` axis) overlap the existing C17 flow-vs-analyst advisory; not separately promoted (same power limitation).

## 8.7 Net answer
Finnhub was the right place to look — fundamentals/insider/PEAD are real anomalies where flow was beta. But on **this** 3.5-month panel, **neither PEAD nor insider produces an honest standalone edge** (PEAD is sell-the-news and thin; insider is wrong-signed and sparse). Finnhub's honest role here is the **fundamentals-gate risk veto**, kept on mechanism grounds, with a pre-registered re-test once the panel spans multiple earnings seasons. Same rule as everywhere in this project: an edge gets a lane only when the numbers earn it — and these don't, yet.
