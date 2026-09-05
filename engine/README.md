# engine/ — the deterministic options-premium engine

Built 2026-09-05 from `~/Development/findings/market-analysis/DESIGN/70-backtest-spec.md`. No model
call anywhere; every number comes from a query or a pure function, and the S-A parameters are frozen
(`tests/test_frozen_params.py` fails if one moves before the Season 3 read).

```
make daily DATE=2026-10-14   # preflight, append mart, tonight's S-A candidates, grade yesterday, report
make mart                    # rebuild data/mart/{daily_contract,earnings_events} (about 3 min)
make backtest                # S-A over the whole mart -> data/backtest/{trades,suppressed,dropped}.parquet
make report                  # season table, BH, DSR, PBO, tail, robustness, go/no-go -> data/backtest/report.md
make test                    # the unit suite (no panel needed)
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

The forward ledger opens 2026-10-01; before that `make daily` writes `analyses/daily/<date>/` but does
not touch `ledger/` unless `--force-ledger` is passed. The backtest write-up lives in
`~/Development/findings/market-analysis/RESEARCH/45-sa-backtest.md`.
