---
description: Weekly market review — the whole-week picture on the weekly timeframe. THREE layers, sharply separated: (1) a DOCUMENTATION diary (weekly candle structure vs prior weeks, catalysts anchored to price, regime trajectory, sector leadership, notable flow) that ships every week as a journal; (2) the VALIDATED momentum/OI-fade lanes expressed at the weekly horizon (scored in excess); (3) event-conditioned weekly-technical features (candle structure, reversal-after-catalyst) that are PRE-REGISTERED and explicitly NOT scored until the extended panel validates them. Emits report.md + weekly decision.json. Invoke on a weekend / post-Friday-close, or `/weekly-review`.
model: opus
defaults:
  scoring_currency: excess_vs_spy_conditional
  weekly_technical_status: PRE-REGISTERED   # documented, 0 points, until cross-year validation
---

# /weekly-review — the week in review (documentation + validated weekly lanes + pre-registered technicals)

This is the weekly companion to `/market-scan`. It exists because the daily scan optimizes for *tonight's*
decision and can miss the **whole-week structure** — how the weekly candle closed relative to prior weeks,
how the week digested its catalysts (a CPI-Wednesday reversal, an outside/inside week, a weekly hanging-man),
and how the regime trajected Mon→Fri. **Three layers, never blended:**

## The honesty contract (the whole point of this command)
- **Layer 1 — DIARY (always ships, 0 points).** Pure documentation/situational-awareness. Never sized on.
- **Layer 2 — VALIDATED WEEKLY LANES (scored in excess).** The same factors that survived the daily backtest
  (momentum 52w-range, OI-flow fade), expressed at the **weekly horizon** (2–4 week hold). These carry the
  validated-excess priors; they are scored exactly like `/market-scan`.
- **Layer 3 — WEEKLY TECHNICALS (PRE-REGISTERED, 0 points).** Candle-structure and event-conditioned features.
  **These are documented and what-if'd but earn ZERO conviction and are never sized.** Rationale: the
  candlestick literature is weak-to-null on liquid names (Marshall-Young-Rose 2006), and this panel has only
  ~11–23 weeks — statistically meaningless for a weekly-pattern claim. They graduate to Layer 2 ONLY through
  the pre-registration bar below.

## When to invoke
- Weekend / post-Friday-close weekly recap; "review the week"; `/weekly-review`.
- NOT for a daily post-market scan (use `/market-scan`) or a single ticker (use `uw insights deep-dive`).

## Phase A — Build the week's bars + structure (documentation substrate)
1. `python3 scripts/truthset/weekly_features.py` → `data/weekly_features.parquet` (weekly OHLC + candle anatomy:
   `close_pos, body_frac, upper/lower_wick, inside_week, outside_week, higher_high, lower_low,
   hammer_or_hanging, star_or_inverted, follow_through`).
2. **Catalyst anchoring:** WebSearch the week's Tier-1 macro prints (CPI/PPI/PCE/FOMC/NFP) with their weekday,
   and tag the daily price reaction (e.g. "CPI Wed → SPY gapped +0.8%, faded to close red = intraweek reversal").
   This is the event-conditioning layer; record it, don't score it.
3. **Regime trajectory:** run `regime-classifier` for Mon and Fri of the week; report how the label/vol-state moved.

## Phase B — Layer 2: validated lanes at the weekly horizon (SCORED)
Run the **`momentum`** and **`oi-flow-fade`** lanes on the weekly timeframe (hold 2–4 weeks ≈ daily h10–h21):
- Momentum: weekly 52w-range position (long near-high / short near-low) — same factor, longer hold.
- OI-flow fade: the trailing multi-week net call-OI build fade.
These carry their validated-excess priors and are scored/sized by `risk-sizer` exactly as in `/market-scan`
(regime gate, crash guard, correlation cluster, fundamentals veto, tail caps, half-cap). The liquidity-reversion
(S2) and PCR (S4) lanes are daily-horizon and are **not** re-run weekly.

## Phase C — Layer 3: weekly technicals (PRE-REGISTERED, 0 POINTS)
For SPY/QQQ/IWM and any Layer-2 candidate, surface from `weekly_features.parquet`:
- **Weekly candle structure**: `close_pos`, `body_frac`, `inside/outside_week`, `higher_high/lower_low`,
  `hammer_or_hanging` / `star_or_inverted`, vs the prior 1–4 weeks.
- **Event-conditioned structure**: did the week **reverse the catalyst-day move** (reversal-after-CPI), and did
  it **confirm or fail** the prior week's direction (`follow_through`)?
- For each, state **what it WOULD signal** and assign `conviction_points: 0, status: PRE-REGISTERED`.
- **Pre-registration acceptance bar (PR-WT, identical discipline to the daily lanes):** a weekly-technical
  feature earns a scored Layer-2 lane only when, on the **extended panel** (≥2 years / ≥30 weekly obs per arm),
  it shows forward **excess** that is cross-regime sign-stable and BH-surviving at FDR 0.10. Until then it is
  diary color, never a sizing input. The `/calibration-audit` accrues these toward the bar.

## Phase D — Gates, sizing, envelope (Layer 2 only)
`risk-sizer` sizes ONLY the Layer-2 scored lanes (same gate stack as `/market-scan`, half-cap). Layers 1 & 3
are documentation. Emit `analyses/weekly/<iso-week>/decision.json` (schema `schemas/weekly_review.schema.json`):
- `week_context` (Layer 1 diary: weekly candles, catalysts+reactions, regime trajectory, sector leadership, notable flow)
- `weekly_technicals[]` (Layer 3: each feature with `conviction_points: 0, status: PRE-REGISTERED, would_signal`)
- `calls[]` (Layer 2: validated weekly-horizon lanes — **real single-name tickers ONLY**. Every entry's
  `ticker` must be an actual market symbol; the schema now enforces `^[A-Z][A-Z0-9.\-]{0,6}$`.)
- `lane_status[]` (Layer 2 lane-level disposition — where a lane fired conceptually but produced **no sized
  single-name call**: MOM_LONG is basket-only, MOM_SHORT may be crash-guard stood-down, OI_FADE may clear no
  name). **Never invent a synthetic ticker** (`MOM_LONG_BASKET`, `MOM_SHORT_STANDDOWN`, …) to force such a
  row into `calls[]` — that was the pre-2026-07 bug. Use `{lane, disposition (BASKET_WATCH|STOOD_DOWN|
  NO_NAME_CLEARED), direction, regime_fit, note, candidates[] (real symbols surfaced but not sized)}`.
Validate with `scripts/validate_decision.py`. Persist nothing to the conviction watchlist that isn't a Layer-2 call.

## Phase E — Report
```markdown
# Weekly Review — <iso-week> (<date range>)
## 1. The Week in Pictures (DIARY — documentation, 0 signal)
- SPY/QQQ/IWM weekly candle: O/H/L/C, w_ret, close_pos, body, vs prior weeks (inside/outside/HH-LL/reversal)
- Catalysts this week (CPI/FOMC/NFP) anchored to the daily reaction; intraweek reversals
- Regime trajectory Mon→Fri; sector leaders/laggards; the week's largest DP/sweep prints
## 2. Validated Weekly Setups (SCORED — excess)
- momentum (weekly 52w-range, long/short) + oi-flow-fade at 2–4wk hold; sizes from risk-sizer
## 3. Weekly Technicals — PRE-REGISTERED (documented, 0 points, NOT sized)
| Feature | This week | Would signal | Status | Pre-reg bar |
|---|---|---|---|---|
| weekly hammer/hanging on SPY | … | … | PRE-REGISTERED | PR-WT (≥2yr) |
| reversal-after-CPI | … | … | PRE-REGISTERED | PR-WT |
## 4. Carry-forward
- How last week's Layer-2 calls did; what rolls into next week
```
Print sections 1–2 to chat; the rest opens from the file.

## Failure modes
- No Layer-2 candidate (no near-extreme momentum / OI-fade name) → `calls[]` is empty; record the lane's
  posture in `lane_status[]` (why it produced nothing), NOT as a placeholder row in `calls[]`. The diary (§1)
  and pre-registered technicals (§3) still ship. A "no scored setup" week is a normal, correct output.
- A basket-only (MOM_LONG) or stood-down (MOM_SHORT) lane is a `lane_status[]` entry, never a `calls[]` row —
  a single ticker under MOM_LONG would misrepresent a basket lane as a per-name call.
- Never let a Layer-3 weekly-technical pattern size a trade. That guard is the entire reason this command is split.
