# 00 — Orientation (Phase 0 checkpoint)

_Clean-room redesign of `uw-daily-analysis`. Working dir `~/Development/findings`. Hindsight window **2026-03-13 → 2026-06-26** (54 sessions). Nothing here touches the live repo._

## 0.1 Environment verified

| Asset | Status | Notes |
|---|---|---|
| Panel `~/Documents/Stocks/{5 sources}` | ✅ 54 parquet files each | 2026-03-13 → 2026-06-26 |
| `uw` CLI (`~/.local/bin/uw`) | ✅ responds | DuckDB over the panel; 11 groups |
| `fz` CLI (`~/.local/bin/fz`) | ✅ responds | Finviz; advisory only |
| Yahoo **chart** API (OHLC via `urllib`) | ✅ real O/H/L/C | NVDA 76 bars 2026-03-10→06-26; **truth-set price source** |
| `mcp__yahoo-finance__*` | close-only in this env | NOT used for path-aware outcomes (per audit C20) |
| System `python3` | duckdb 1.5.2 ✅, no pyarrow | use duckdb for parquet |

### Panel schema (row counts as of 2026-06-26 file)
- **All Options** (`bot-eod-report`, 12.2M rows/day, 30 cols): trade-level option prints — `underlying_symbol, side, strike, option_type, expiry, underlying_price, price, size, premium, volume, open_interest, implied_volatility, delta/gamma/theta/vega, sector, report_flags, upstream_condition_detail` (OPRA condition codes → single-leg vs multileg), `executed_at`. The substrate for sweeps, single-leg whale, GEX/DEX (greeks×OI), premium trades.
- **Dark pool** (`dp-eod`, 654k rows, 16 cols): `ticker, executed_at, nbbo_bid/ask(+qty), size, volume, premium, price, sale_cond_codes, trade_code, ext_hour_sold_codes`. Block stratification = size tiers; buy/sell pressure = price vs NBBO mid.
- **Hot Option Chains** (`hot-chains`, 30k rows, 33 cols): per-contract daily aggregate — `option_symbol, volume, open_interest, premium, ask_side_volume, bid_side_volume, floor_volume, sweep_volume, cross_volume, multileg_volume, iv, next_earnings_date, sector`. Sweep ratio, smart-money (ask−bid), multileg.
- **OI changes** (`chain-oi-changes`, 294k rows, 31 cols): `oi_diff_plain, underlying_symbol, strike, last_oi, curr_oi, oi_change, dte, stock_price, prev_ask/bid/mid volume, next_earnings_date`. OI buildup, rolls, smart positioning.
- **Stock Screener** (`stock-screener`, 6.2k rows/day, 52 cols): per-ticker daily — `call/put_volume, call/put_premium, put_call_ratio, bullish/bearish_premium, net_call/put_premium, total/call/put_open_interest, avg_{3,7,30}_day_*, iv30d(+1d/1w/1m), iv_rank, implied_move, week_52_high/low, close/high/low, marketcap, sector, next_earnings_date`. The top-of-funnel screen + the IV/PCR/52w context.

### Universe & price cache (truth-set substrate)
- Liquid book (avg price ≥ $5 AND avg dollar-ADV ≥ $50M, the repo's C12 floor) = **1,979 names**.
- Priced subset = activity-ranked candidate funnel: top-600 by window options premium ∪ top-300 by DP premium ∪ all single-leg-put-whale underlyings ∪ benchmarks/sector-ETFs ∩ liquid = **785 names** → `data/prices.parquet` (Yahoo OHLC, 2026-01-15→06-27, lead for ATR(14)).

## 0.2 How the current fleet decides (subject under redesign)

`/daily-analysis` (606 lines) is a **two-phase agent fleet** emitting `report.md` + a schema-validated `decision.json` (envelope schema 1.3, rubric_version `2026-06-12`):

**Step 0 — shared macro context** (built once, passed to every agent): date, `fz` health probe, coverage check, `playbook daily-synthesis`, regime (`risk market-regime`), DTE-volume-share, VRP, breadth cross-check (`fz`), GICS sector-flow + persistence, top-of-funnel screens (bullish-bearish, signal-confluence, volume-vs-avg, iv-rank), OPEX guard, FRED macro snapshot + forward event calendar, next-session 0DTE setup (`zerodte_setup.py`). Liquidity floor (C12) applied to every screened name.

**Phase 1 — 11 alpha agents in parallel** (12 in OPEX week): `gamma-flip-tracker` (SPY/QQQ 0DTE GEX advisory), `dealer-positioning-strategist` (DEX/vanna/charm swing), `sector-rotation-strategist` (GICS+ETF tape), `opex-pin-strategist` (conditional), `sweep-tracker`, `accumulation-hunter` (DP+OI), `contrarian-scanner`, `earnings-scout`, `vol-surface-scout`, `multileg-strategist`, `leap-positioning-radar`. Each prefers multi-day persistence tools over single-day.

**Phase 2 — sequential gauntlet:** (2a) `signal-confluence-quant` unions all candidates, scores against the frozen rubric, attaches class win-rate via the "P0.3 clean-query" `signal-backtest` protocol, emits pre-risk size; (2b) `fundamentals-gate` on top-5 (Finnhub: earnings streak, insider MSPR, catalyst, CONFIRM/CAUTION/VETO); (2c) bounded `bull-researcher`/`bear-researcher` debate on top-5 (can only cut size); (2d) `risk-monitor` applies a 9-key gate stack (regime, vrp, panic, cluster, sector, fundamentals, event_risk, debate, rubric_regime) + correlation + watchlist write-back.

**Confluence gate:** a name enters the rubric only with **≥2 distinct agents** flagging it. **HIGH-tier gate:** must cite ≥3 of 4 load-bearing tools (DP block-stratified, cum-premium-flow, institutional-accumulation, DEX).

### The frozen conviction rubric (`2026-06-12`)
```
+1  MECHANIZED DEX flip / vanna-squeeze in trade dir   (was +3; demoted+mechanized 2026-06-12 P0.4)
+3  3+ aligned accumulation (DP+OI+smart-pos+block)    CONJUNCTION: halved →+1 unless cum_flow_30d confirms (sign + |.|≥$50M)
+1  multi-day OI build (oi-trend BUILDING ≥5d)
+1  conviction-matrix DIRECTIONAL_LONG >70             CONDITIONAL: only when dominant_class==leap_directional
+1  cum_premium_flow net accretion 30d                 INTENT-SCREENED (was +3; demoted 2026-06-06 P1.4; NO-INFO ×3 audits)
+1  sector-rotation single-name leader                 CONDITIONAL: persistence≥0.6 ∧ cum_flow aligned ∧ |.|≥$50M
+1  earnings-scout BUY/SELL VOL
+2  multileg-strategist directional structure          (promoted 2026-05-09)
+1  vol-surface KINKED/BACKWARDATION + VRP-aligned
+1  opex-pin top-5 (OPEX week)
-2  contrarian crowded-long + rising PCR z-score        (informed-flow CONTINUATION penalty, not fade)
-3  flow_conflict (cum_flow clearly opposite class)
-1  flow_conflict_lite (cum_flow MIXED)
[TIER GATES, not points]: -1 tier correlation cluster; -1 tier regime conflict
Tiers: ≥9 HIGH(full) · 7–8 MED(half) · 3–6 LOW(watch) · ≤2 drop
```
Sizing ladder: win_rate ≥0.70 full / 0.50–0.70 half / <0.50 starter/skip, **on top of**: out-of-regime half-cap (P0.6, active now), n<10 cap 0.69, market-excess gate (excess≤0 → half; ≤−0.10 → starter), bullish/bearish-flow OI-opening cap.

**Single-leg whale signal** (advisory, **0 rubric points**, criterion C19): Tier-1 `OPENING_PUT_PRIME` (put, size/OI≥2, DTE≤30) WR 63.5% +26pp n=266; `FLOOR_PUT_BLOCK` 61.0% +23.5pp n=328; both p<0.001. Promotion-gated pending ≥60d × ≥2 regimes.

## 0.3 What the repo's own audit already concluded (cross-check, NOT ground truth)
From `AUDIT.md` + the frozen-rubric annotations (to be independently re-derived in Phases 1–2):
1. **Rubric was over-fit & whipsawed.** Six cycles re-weighted *correlated* lines on n=8–31, single-regime, BH-null marginal contributions. cum-flow went +2→+3→+1 (a realized false positive). Rubric now **frozen**; audits grade, don't retune.
2. **Tier inversion out-of-sample.** The ≥9 HIGH cut (set in-sample on UPTREND where ≥9 realized 0.774, n=31) **failed re-confirmation 2026-06-12**: first post-UPTREND window HIGH 0.222 / MED 0.214 / LOW 0.444. Bands inverted. → out-of-regime half-cap now active.
3. **Additive scoring rewards crowding.** Agreeing signals stack with no agent tasked to kill the trade; crowded consensus names score highest and break hardest. (Debate step was the band-aid.)
4. **Tools demoted/removed on evidence:** `signal-confluence` (server re-count of scored quantities, removed), `sweep-persistence` (−22pp ×2 audits, removed), DEX/vanna (no peer-reviewed swing edge; hedging mean-reverts intraday — Baltussen 2021), cum-flow (NO-INFO ×3, ubiquity-confounded n=136).
5. **The one validated, externally-grounded edge is the bearish single-leg put** — yet it scores **0 points**. Live proof in the 2026-06-23 envelope: NVDA carried the strongest bearish signature in the book (Tier-1 opening 220P + $1.29B DP sell print + +18.5pp class excess vs SPY) and was **"structurally under-scored by the rubric"** → forced to starter/relative.

## 0.4 A-priori hypotheses (to test in Phases 1–3)

| # | Hypothesis | Predicted finding | External anchor |
|---|---|---|---|
| H1 | **Bearish single-leg opening-put (Tier-1) is the strongest re-derivable edge and is under-weighted** (0 pts). | High forward excess on short side, hit-rate >55%, survives FDR, holds in both in-sample regimes. | Pan-Poteshman 2006 (only opening flow predicts); Johnson-So 2012 (put informativeness ∝ short-sale cost). |
| H2 | **DP block-stratified accumulation works only as a CONJUNCTION**, not additively. | DP-block ∧ cum_flow ∧ inst-accum beats any single leg; the additive +3 manufactured false HIGH. | Easley-O'Hara-Srinivas 1998 (informed block trades). |
| H3 | **cum_premium_flow is NO-INFO standalone** (belongs as a screen/gate, not a scored line). | ~0 marginal IC; ubiquity-confounded. | López de Prado (multiply-tested WR inflates). |
| H4 | **DEX/vanna/charm flips have ~0 swing directional edge.** | Forward excess indistinguishable from 0; a +DEX level is just beta in an up-tape. | Baltussen et al. 2021 (hedging pressure intraday-mean-reverts). |
| H5 | **Sweep-persistence / single-day sweeps are noise-to-negative.** | Negative or ~0 excess; already −22pp in audit. | Microstructure: sweeps are urgency, not information, ex-opening. |
| H6 | **conviction-matrix DIRECTIONAL_LONG>70 is a mean-reversion *fade* signature ex-LEAP.** | Negative swing excess for top-picks. | Top-pick crowding reverts. |
| H7 | **GEX regime (long/short gamma) conditions *volatility*, not direction.** Useful for sizing/structure, not a directional point. | GEX sign predicts realized-range, not signed return. | Barbon-Buraschi (dealer gamma → vol suppression). |
| H8 | **0DTE VRP premium-selling is real but thin net-of-cost; keep delta-neutral & advisory.** | Positive gross VRP, marginal net. | Vilkov 2024 (0DTE condor flips negative net of costs). |
| H9 | **The 11–12 agent fleet is heavily redundant** — DP/OI/flow agents key off correlated tape. Expect to cut ≥3 agents. | High cross-agent ticker overlap; few agents carry the excess. | — |
| H10 | **Regime stratification is decisive** — the window holds ≥2 regimes (UPTREND through ~06-12, then TRANSITIONAL pullback). Any single-number edge claim must survive both. | Edges that vanish/flip across the 06-12 break are beta, not alpha. | Single-regime fits over-state edge. |

## 0.5 Method commitments for Phases 1–2
- **Look-ahead discipline:** a signal on day T uses only panel data with `date ≤ T`; outcomes use OHLC `> T`. Forward horizons that extend past 2026-06-26 are INCONCLUSIVE (`data_unavailable`), never counted as losses. Long horizons (30D/90D) resolve only for early-window signal-days — N shrinks with horizon; report honestly.
- **Edge = excess vs SPY**, not raw return (the window is net-up → beta masquerades as edge). Primary metrics per signal class: mean forward **excess** return, **hit-rate** (signed-excess>0), and a rank **IC** (Spearman of signal-strength vs forward excess).
- **Multiple-testing humility:** Benjamini-Hochberg (FDR 0.10) across the class/tool sweep; min decided-N ≥ 30 to call an edge "durable" (below that → provisional); stratify every claim by regime.
- **Independent first.** Re-derive numbers from the panel + OHLC; only then reconcile with `/calibration-audit`. Where they disagree, investigate and document which is right.

## 0.6 Phase status — ALL COMPLETE (awaiting migration approval)
- [x] **Phase 0 — Orient.** (this doc)
- [x] **Phase 1 — Independent truth set.** → `10-truth-set.md`, `12-benchmark-inconsistency.md`, `data/{prices,returns}.parquet`, `edge.py`.
- [x] **Phase 2 — Edge by source/agent/rubric.** → `20-edge-by-agent.md` (6-agent fan-out; 0/45 durable edges; 4 provisional survivors).
- [x] **Phase 3 — External validation.** → `30-external-validation.md` (flow-is-beta & gamma-is-vol STRONG; S1 grounded; S2/S4/S5 conditioned).
- [x] **Phase 4 — Redesigned workflow.** → `DESIGN/40-improved-workflow.md` (16→7 agents; excess-currency; reduction not re-weight).
- [x] **Phase 5 — Artifacts + retro harness.** → `artifacts/*` + `50-retro-validation.md` (redesign +excess vs old HIGH −8.2%/0-for-6).
- [x] **Phase 6 — MIGRATION.md.** → staged, reversible plan; **STOPPED for approval** before touching `uw-daily-analysis`.
