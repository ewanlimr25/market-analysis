# PLAN.md — stand up `market-analysis` as a standalone repo

> This is the build plan the **RUN_PROMPT** executes in a fresh Claude Code session opened in
> `~/Development/market-analysis`. The design artifacts are **already in place** (scaffolded from the
> validated clean-room work in `~/Development/findings`); this plan wires them into a working repo and
> validates end-to-end. It does **not** touch `~/Development/uw-daily-analysis`.

## Why standalone (not a migration into uw-daily-analysis)
`uw-daily-analysis` is, by identity, the deepest microstructure **flow** engine. This repo's founding
finding (`research/20`, `70`) is that **flow is beta and price-structure is the edge** — the opposite
worldview. Forcing both into one repo creates a schizophrenic codebase with two schemas and a calibration
loop built to police a 16-agent additive rubric this product doesn't have. A clean repo lets the excess-scored,
regime-first product own its surface and evolve independently. The evidence base lives in `research/`.

## What's ALREADY in place (verify in Stage 0)
- `.claude/commands/` — `market-scan.md` (daily), `weekly-review.md` (weekly, 3-layer), `calibration-audit.md` (lean forward).
- `.claude/agents/` — `regime-classifier, momentum, oi-flow-fade, liquidity-reversion, sentiment-contrarian, vol-book, risk-sizer, fundamentals-gate`.
- `scripts/truthset/` — `build_prices, build_returns, build_features, edge, factor_scan, weekly_features`.
- `scripts/` — `retro_harness` (regression gate), `validate_decision` (v2/weekly), ported `_env, finnhub_enrich, zerodte_setup, fred_macro, excess_winrate`.
- `schemas/` — `decision_envelope.v2.schema.json`, `weekly_review.schema.json`.
- `data/` — generated + validated `universe.json, prices.parquet, returns.parquet, features.parquet, weekly_features.parquet`.
- `research/` — the full evidence trail (00→80, PROVENANCE).

## Build stages (each: action → validation gate)

### Stage 0 — Verify scaffold + env
- `find . -type f` matches the inventory above.
- `python3 -c "import duckdb, jsonschema"` OK; `uw --help` and `fz --version` respond; `_env.get_key("FINNHUB_API_KEY")` returns a key (else fundamentals-gate graceful-skips).
- **Gate:** all present; note any missing dependency.

### Stage 1 — Data substrate + regression gate
- The data is copied and current. To prove reproducibility: `python3 scripts/truthset/build_returns.py` → SPY self-excess = 0.000; (optionally `build_prices.py` to refresh OHLC, `build_features.py`, `weekly_features.py`).
- **Gate:** `python3 scripts/retro_harness.py --all` reproduces the lane table (MOM/OI_FADE/S2/S4 all positive-excess; OI_FADE hit−base ≈ +0.205). **No lane negative.**

### Stage 2 — Schema + envelope plumbing
- `python3 scripts/validate_decision.py --file research/sample_decision.v2.json` (copy the sample first) exits 0.
- Confirm `validate_decision.py` routes weekly envelopes to `weekly_review.schema.json`.
- **Gate:** both schemas validate a hand-built sample.

### Stage 3 — Repo config + git
- Write `.claude/settings.local.json` (allow `Bash(python3:*)`, `Bash(uw:*)`, `Bash(fz:*)`, Read/Write/Edit/WebSearch); `.mcp.json` if a UW MCP is used; `.env` with `FINNHUB_API_KEY` (or document the `_env` fallback); `.gitignore` (`data/*.parquet`, `analyses/`, `.env`).
- `git init` + initial commit. **Gate:** clean `git status` after the commit; `CLAUDE.md` present.

### Stage 4 — Dry-run `/market-scan` (no live trade — produce + validate)
- Pick the latest panel date (`uw historical available-dates`). Run the `/market-scan` pipeline end-to-end against it: regime-classifier → lanes → risk-sizer → emit `analyses/scan/<date>/report.md` + `decision.json`.
- **Gate:** `validate_decision.py` passes the envelope; the printed regime/verdict matches `python3 scripts/retro_harness.py --date <date>`; a "no directional edge" day is an acceptable result.

### Stage 5 — Dry-run `/weekly-review`
- Run for the most recent complete ISO week: Phase A diary (weekly candles from `weekly_features.parquet` + catalyst anchoring via WebSearch + regime trajectory) → Layer-2 weekly lanes → Layer-3 pre-registered technicals → emit `analyses/weekly/<iso-week>/{report.md,decision.json}`.
- **Gate:** weekly envelope validates; **Layer-3 technicals carry `conviction_points: 0, status: PRE-REGISTERED` and are NOT in `calls[]`**; only Layer-2 lanes are sized.

### Stage 6 — Dry-run `/calibration-audit`
- Run it; with <10 resolved forward calls it should report INSUFFICIENT and lean on `retro_harness --all` as the standing regression gate.
- **Gate:** runs without error; SUMMARY written; no false STOP flags on thin N.

## Operating cadence (after build)
- **Nightly (post-8PM-EST export):** `/market-scan` → `analyses/scan/<date>/`. Often "no directional edge" — that's the discipline.
- **Weekend:** `/weekly-review` → `analyses/weekly/<iso-week>/` (diary always; scored lanes when present; technicals pre-registered).
- **Weekly / per ~10 resolved calls:** `/calibration-audit` → confirm lanes still positive-excess; STOP any that aren't.

## Hard invariants (carry from the research)
1. **Excess-vs-SPY (conditional) is the only scoring currency** — never raw win-rate (the tape is long-biased).
2. **No additive confluence** — a name scores on one lane's measured excess, regime-conditioned; orthogonal lanes are noted, not summed.
3. **Most days have no directional edge — say so.** The modal `/market-scan` output is the regime + vol book + watch list.
4. **Half-cap, no auto-full** until a cross-year edge validates.
5. **Pre-registered ≠ scored.** Weekly technicals (and PR-1/2/5/6/7) are documented, never sized, until their bar clears on data that postdates registration.
6. **The regression gate is law:** ship no lane/threshold change unless `retro_harness.py --all` shows no lane negative-excess.

## Open pre-registrations (decided by future data)
PR-WT weekly technicals · PR-2 S1 crash guard through a real V-rebound · PR-5 S1 options-carry · PR-6 momentum×oi_net conjunction ·
PR-7 PEAD/insider on the extended panel · (PR-1 sector-flow = decided: beta). The **#1 enabling investment is panel extension**
(`research/60 §6.5`): back-fill the April gap, ≥1 VIX>30 episode, and ≥2 prior years.
