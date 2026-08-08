# docs — market-analysis

Deep-dive reference material. `CLAUDE.md` at the repo root stays short and points here; these files carry
the full history, rationale, and worked examples so nothing is lost by keeping the root file lean.

| File | What's in it |
|---|---|
| [`regression-gate.md`](regression-gate.md) | Full baseline history for invariant #6: current + prior lane baselines, the 2026-08-08 universe-expansion story, the three-part isolation-check protocol (old-code/new-data, maturity-edge cohort split, same-code/old-universe), the 2026-08-08 worked example, the MOM_SHORT knowingly-negative rationale, and exit-day counting. |
| [`lanes.md`](lanes.md) | The validated-lanes table with full per-lane notes, the 785-spine vs. full-universe comparison, and forward-audit caveats. |

Other reference material lives outside `docs/`:

- `research/` — the hindsight-validated clean-room research this engine is built from (`00-orientation.md`
  through `80-finnhub.md`, plus `PROVENANCE.md`). Read before changing any lane's logic or gates.
- `archive/PLAN.md` — the original repo-standup plan (local-only, gitignored, historical — the standup it
  describes is already complete).
