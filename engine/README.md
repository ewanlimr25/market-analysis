# engine/ — the deterministic options-premium engine

Operator's guide (what to run nightly, how to read the report, the calendar): [`../docs/OPERATING.md`](../docs/OPERATING.md).

Built 2026-09-05 from `~/Development/findings/market-analysis/DESIGN/70-backtest-spec.md`. No model
call anywhere; every number comes from a query or a pure function, and the S-A parameters are frozen
(`tests/test_frozen_params.py` fails if one moves before the Season 3 read).

```
make daily DATE=2026-10-14   # preflight, append mart, tonight's S-A candidates, grade yesterday, report
make mart                    # rebuild data/mart/{daily_contract,earnings_events} (about 3 min)
make backtest                # S-A over the whole mart -> data/backtest/{trades,suppressed,dropped}.parquet
make report                  # season table, BH, DSR, PBO, tail, robustness, go/no-go -> data/backtest/report.md
make test                    # the unit suite (no panel needed)
make validate DATE=2026-10-14 # check that night's signals.json against schemas/signals.schema.json (make daily does this itself)
make backtest-sb             # S-B: three-year proxy + marked panel run -> data/backtest/sb_*.parquet (REFRESH=1 refetches inputs)
make report-sb               # S-B: sleeve tables, BH, DSR, PBO, month rule, tail, overlap, go/no-go -> data/backtest/sb_report.md
make index-vol               # refresh data/mart/index_vol/ from the CBOE public CSVs (the nightly does this itself)
make cboe-chain               # fetch+store the full SPY/QQQ (+ SYMBOLS=...) CBOE option chain -> data/mart/cboe_chain/ (RESEARCH/47 G8; standalone, not part of `make daily`)
```

| module | what |
|---|---|
| `config.py` | paths, session windows, marking constants, `SAParams` / `SizingParams` (frozen), seasons, the go/no-go bar |
| `calendar.py` | NYSE calendar 2026–2027 (`next_session`, `prev_session`, `trading_days_between`) |
| `mart/daily_contract.py` | one row per (contract, day) from All Options + Hot Chains; integer-scaled sums so a rebuild is bit-for-bit |
| `mart/earnings_events.py` | one row per (ticker, print), E1's construction reproduced exactly (3,260 events) |
| `mart/vix.py` | VIX closes via `scripts/chart.py`, cached in `data/mart/vix/` |
| `mart/store.py` | `data/mart/<table>/date=YYYY-MM-DD/part.parquet` helpers |
| `bs.py`, `marking.py` | Black-Scholes fallback; the four-tier `mark()`; `leg_cost` (half-spread + $0.65) |
| `strategies/sa_filters.py` | F1..F8, A2 sector cut, expiry / ATM / wing selection |
| `strategies/sa_structures.py` | SS and IC legs, pricing, stress / max loss, sizing |
| `strategies/sa.py` | `evaluate_event` / `run`: trades, suppressed (first failing filter), dropped |
| `strategies/sa_data.py`, `backtest_sa.py` | mart access, model-input closure, the two-pass backtest driver |
| `portfolio.py` | book caps (8 events, 3 per sector, 40% of the night's risk budget) |
| `validation/stats.py` | clustered t, BH, Sharpe deflation, CSCV PBO |
| `validation/harness.py`, `validation/run_report.py` | season split, tail, robustness, go/no-go, §4.3 reproduction; the markdown report |
| `ledger.py`, `daily.py`, `report.py` | forward ledger (`ledger/`, committed, never re-derived), `make daily`, templated `report.md` |
| `schema.py` | the `signals.json` contract: `schema_version` / `report_kind` stamp, strict JSON (no NaN), validation against `schemas/signals.schema.json` (`d1.0`); `scripts/validate_signals.py` wraps it |
| `mart/index_vol.py` | CBOE VIX / VIX3M / VXN / VIX9D closes, cached in `data/mart/index_vol/`, artifact fallback (S-B, DESIGN/80 §1.1) |
| `strategies/sb_gate.py` | the S-B gate: contango and level above the 20-session median, read at the prior close (DESIGN/80 §2) |
| `strategies/sb_structures.py` | Friday-type expiry nearest 21 days, σ unit, tier-1 strike band, PS / IC legs, max loss, sizing, open cap (DESIGN/80 §3-§4) |
| `strategies/sb_proxy.py`, `strategies/sb.py`, `strategies/sb_data.py`, `backtest_sb.py` | the three-year proxy at the panel's smile multipliers; the marked run on `daily_contract`; the driver |
| `validation/sb_harness.py`, `validation/run_sb_report.py` | NW and expiry-clustered t, BH, deflated Sharpe (two benchmarks), PBO, month rule, tail, overlap, gate modes, go/no-go (DESIGN/80 §6) |
| `sb_daily.py` | the S-B nightly step: CBOE refresh (fail-soft), gate tonight and next session, entries on the last session of the week, grading at expiry into `ledger/sb/` (DESIGN/80 §7) |
| `mart/cboe_chain.py`, `mart/cboe_chain_derived.py` | the full option chain from CBOE's free delayed API, stored write-once at `data/mart/cboe_chain/symbol=<SYM>/date=<date>/`; GEX, 25-delta skew, ATM IV, put-call OI ratio (RESEARCH/47 G8; `make cboe-chain`, standalone) |

The S-A forward ledger opens 2026-10-01 and the S-B ledger (`ledger/sb/`) on 2026-09-11; before those dates
`make daily` writes `analyses/daily/<date>/` but does not touch `ledger/` unless `--force-ledger` is passed.
The backtest write-ups live in `~/Development/findings/market-analysis/RESEARCH/45-sa-backtest.md` (S-A) and
`RESEARCH/46-sb-backtest.md` (S-B); the S-B parameters are frozen by `tests/test_sb_frozen_params.py`.
