# legacy/ — the frozen Claude Code fleet (June to 2026-09-05)

Before the engine, this repo was a set of Claude Code workflows: `/market-scan` nightly, `/weekly-review` on
weekends, `/calibration-audit` on the forward book, each fanning out to one sub-agent per directional lane.
The lanes measured −1.2% to +0.14% excess vs SPY gross of costs and could not clear their own bar, so the
fleet was frozen on 2026-09-05 and replaced by the deterministic engine in `../engine/` (`make daily`;
operator's guide `../docs/OPERATING.md`). Why, in full: `~/Development/findings/market-analysis/`
(`RESEARCH/45`, the D-series in `DECISIONS.md`).

Moved here on 2026-09-26 so the repo root shows only the engine path. Nothing in `engine/`, the `Makefile`
or `make test` imports anything below. Git history follows every file (`git log --follow legacy/<path>`).

| Path | Was | What it is |
|---|---|---|
| `claude/agents/` | `.claude/agents/` | the eight lane sub-agents (momentum, oi-flow-fade, liquidity-reversion, sentiment-contrarian, vol-book, fundamentals-gate, regime-classifier, risk-sizer) |
| `claude/commands/` | `.claude/commands/` | `/market-scan`, `/weekly-review`, `/calibration-audit`, each with its FROZEN banner. Outside `.claude/`, Claude Code no longer offers them as slash commands, which is the point |
| `scripts/` | `scripts/` | the fleet's helpers: the regression harness (`retro_harness.py`), the earnings / regime / OI gates, the held-book and suppression resolvers, `resolved_ledger.py`, the Finnhub and FRED enrichers, the 0DTE setup, `validate_decision.py` (schema v2 envelopes) |
| `scripts/truthset/` | `scripts/truthset/` | `weekly_features.py` (weekly candles for `/weekly-review`) and `factor_scan.py` (the factor zoo, `research/70`) |
| `tests/` | `tests/` | the 74 unit tests of those scripts |
| `docs/` | `docs/` | `lanes.md` and `regression-gate.md` (the lane baselines and the isolation-check protocol behind the old CLAUDE.md invariants) and their index |
| `research/` | `research/` | the June clean-room study the lanes were built from (`00-orientation` to `80-finnhub`, `PROVENANCE.md`) |
| `local/` | `archive/`, `data/weekly_features.parquet` | gitignored, this machine only: the repo stand-up plan and its run prompt, and the last weekly-features build |

**What stayed where it was, on purpose:**

- `analyses/scan/` and `analyses/weekly/` — the published journal of what the fleet decided (2026-06-22 to
  2026-09-04). Read-only history; `market-visual` and `self-bio` render it from those paths.
- `analyses/audit/` — the calibration-audit working files (gitignored). `market-visual` reads them in place.
- `schemas/decision_envelope.v2.schema.json`, `schemas/weekly_review.schema.json` — the contract of that
  journal, mirrored by the two downstream sites.
- Live helpers the fleet shared with the engine: `scripts/_calendar.py`, `_env.py`, `_regime.py`,
  `chart.py`, `liquidity.py`, `excess_winrate.py`, `preflight.py`, `scripts/truthset/build_*.py`, `edge.py`.

**Running any of it.** Nothing here is part of the routine, but it still runs from the repo root. Each moved
script puts `../../scripts` on its path for the live helpers, and its repo-relative paths (`ROOT`, `DATA`,
`SCHEMAS`) were deepened by one level:

```
python3 -m pytest legacy/tests                       # the 74 tests (not collected by `make test`)
python3 legacy/scripts/retro_harness.py --all        # the old regression gate
python3 legacy/scripts/validate_decision.py --file analyses/scan/2026-09-04/decision.json
```

`week_context.py` reads `data/weekly_features.parquet`. Rebuild it with
`python3 legacy/scripts/truthset/weekly_features.py`, or copy the one in `local/` back.
