# RUN PROMPT — paste into a fresh Claude Code session opened in `~/Development/market-analysis`

---

You are standing up `~/Development/market-analysis` as a working, standalone, excess-scored market-analysis
repo. The design is already complete and validated — your job is to WIRE and PROVE it end-to-end, then run a
first live cycle. **Read `CLAUDE.md` and `PLAN.md` first; they are the contract.** Do NOT touch
`~/Development/uw-daily-analysis` or `~/Development/findings`.

## Founding facts (already established in `research/`, do not re-derive — verify if you doubt)
- This is an EXCESS-scored, regime-first product. Raw options FLOW measured as BETA; the durable edges are
  price-momentum (52-week-range, both legs), an OI-build FADE (`oi_net_5d`, the most robust), DP one-sided-
  concentration mean-reversion, a PCR contrarian fade, and a non-directional vol book. Finnhub = risk veto, not alpha.
- The old additive-confluence system's HIGH book realized −8.2% excess, 0-for-6 (`research/50`). That is the
  failure mode this repo exists to avoid.

## Non-negotiable invariants (from CLAUDE.md — enforce them in everything you build)
1. Excess-vs-SPY (conditional same-day benchmark) is the ONLY scoring currency. Never raw win-rate.
2. No additive confluence — score on ONE lane's measured excess × regime-fit; orthogonal lanes are noted, not summed.
3. Most days have NO directional edge — say so; that is the correct modal output.
4. Half-cap, no auto-full. 5. Pre-registered ≠ scored (weekly technicals + all PR-* are documented, never sized).
6. Regression gate is law: `python3 scripts/retro_harness.py --all` must show NO lane negative-excess after any change.
7. Path-aware outcomes from the Yahoo chart API, never the close-only `mcp__yahoo-finance__*` tools.

## Execute PLAN.md stages 0→6, gating at each (report the gate result before moving on)
- **Stage 0 — Verify scaffold + env.** `find . -type f`; confirm duckdb/jsonschema import, `uw --help`, `fz --version`,
  and `_env.get_key("FINNHUB_API_KEY")`. Report anything missing.
- **Stage 1 — Data + regression gate.** Confirm `data/*.parquet` load; run `python3 scripts/truthset/build_returns.py`
  (expect SPY self-excess = 0.000); run `python3 scripts/retro_harness.py --all` and confirm every lane is
  positive-excess (OI_FADE hit−base ≈ +0.205, MOM_SHORT +0.095, etc.). **If any lane is negative, STOP and report.**
- **Stage 2 — Schemas.** `python3 scripts/validate_decision.py --file research/sample_decision.v2.json` → VALID.
- **Stage 3 — Config + git.** Confirm `.claude/settings.local.json`, `.gitignore`; add `.env` (or document the
  `_env` fallback) and a `.mcp.json` only if you wire a UW MCP; `git init` + an initial commit (exclude data/analyses/.env).
- **Stage 4 — Dry-run `/market-scan`** on the latest available panel date (`uw historical available-dates`). Produce
  `analyses/scan/<date>/{report.md,decision.json}`; validate the envelope; confirm the printed regime/verdict matches
  `python3 scripts/retro_harness.py --date <date>`. THIS IS A DRY RUN — generate and document, do not place real trades.
  A "no directional edge today" result is a correct, common outcome.
- **Stage 5 — Dry-run `/weekly-review`** for the most recent complete ISO week. Build the diary from
  `data/weekly_features.parquet` (regenerate via `scripts/truthset/weekly_features.py` if needed) + WebSearch the
  week's catalysts and anchor the price reaction + regime trajectory. Emit `analyses/weekly/<iso-week>/{report.md,decision.json}`.
  **CRITICAL: Layer-3 weekly technicals (candles/reversals) must carry `conviction_points: 0, status: PRE-REGISTERED`
  and must NOT appear in `calls[]`. Only the Layer-2 momentum/oi-fade weekly lanes are sized.** Validate the envelope.
- **Stage 6 — Dry-run `/calibration-audit`.** With <10 resolved forward calls it should report INSUFFICIENT and fall
  back to `retro_harness --all` as the standing gate. Confirm it runs and writes a SUMMARY without false STOP flags.

## Deliverable
A green checklist of Stages 0–6 with each gate's result, a first `analyses/scan/<date>/` and
`analyses/weekly/<iso-week>/` produced and schema-valid, an initial git commit, and a short note of anything that
needs my decision. Then tell me the nightly/weekly cadence to run going forward.

If a gate fails, STOP at that stage, show me the exact failure, and propose the fix — do not paper over it.
