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
make short-interest DATE=2026-09-07  # FINRA short interest (full universe) + Reg SHO + IBKR borrow (RESEARCH/47 G9; standalone, not part of `make daily`)
make sb-challengers           # G10: VIX-family challenger table on the S-B proxy -> data/backtest/g10_sb_challengers.* (DRAFTS=1 for registration drafts)
make backtest-sg             # S-G: pre-earnings ramp, day -3/-5 long straddle/strangle -> data/backtest/g3_*.parquet (backtest-only research spec)
make report-sg                # S-G: season table, BH, DSR, PBO, tail, spread halves, ramp decomposition, go/no-go -> data/backtest/g3_report.md
make intraday-rv             # build data/mart/intraday_rv (IRV_DATE=<d> for one day, else the whole panel; DAYS=N caps it)
make earnings-history        # build data/mart/earnings_history/{events,summary}.parquet (LIMIT=N caps the ticker set)
make cross-section           # weekly IV-spread/skew/O-S cross-section -> data/backtest/g4_factors.parquet, g4_results.json (RESEARCH/47 G4/G5; standalone, not part of `make daily`)
make watch-retro              # watch-basket R1 retrospective: 17 conditions x panel -> data/backtest/wb_conditions.parquet, wb_retro.json (DESIGN/110; standalone, not part of `make daily`)
make adjudicate ARGS="basket --policy wb-1.0 [--basket LONG|SHORT|VOL]"   # the wb-1.0 read (DESIGN/110 §6, R3); NOT_DUE before the later of 2026-12-01 and 100 episodes
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
| `mart/short_interest.py` | FINRA consolidated short interest, one POST per symbol (full history), write-once at `data/mart/short_interest/settlement=<date>/`; `load_short_interest(as_of)` applies a conservative 9-trading-day publication lag (RESEARCH/47 G9; `make short-interest`, standalone) |
| `mart/borrow.py` | IBKR stock-loan availability (`usa.txt` via `ftp2.interactivebrokers.com`, user `shortstock`), daily snapshots at `data/mart/borrow/date=<date>/`, fail-soft `load_borrow` (RESEARCH/47 G9) |
| `mart/regsho.py` | FINRA Reg SHO daily short volume, `data/mart/regsho/date=<date>/`; facilitation volume, control variable only, never a signal (RESEARCH/30 §5, RESEARCH/47 G9) |
| `mart/finviz_short.py` | `short_float(ticker)`, a thin fail-soft wrapper on `fz quote --agent`, on-demand single-ticker use only (RESEARCH/47 G9) |
| `features/short_side.py` | `join_short_side`: attaches `short_interest`, `days_to_cover`, `si_change_pct` (point-in-time) and `borrow_fee` onto a screener spine -- the control column G4 needs (RESEARCH/47 G4/G9) |
| `mart/index_vol_ext.py`, `improve/sb_challengers.py` | G10: CBOE VVIX/SKEW + VIX9D/VIX and VIX/VIX3M ratios (`data/mart/index_vol_ext/`); the CBOE vol-index family as additional conditions on the frozen S-B gate, backtested on the proxy; registration drafts (RESEARCH/47-edge-gaps.md §2) |
| `strategies/sg_filters.py` | entry/exit day arithmetic (`engine.calendar`), one-strike-out strangle selection; F1..F4, F7, F8 reused from `sa_filters.cheap_filters`, F5/F6 reused at the entry day (DESIGN/91 §1) |
| `strategies/sg_structures.py` | LS / LG legs as `sa_structures.Leg` with `side=LONG`, premium-paid sizing (DESIGN/91 §2-§3) |
| `strategies/sg_decomposition.py` | finite-difference delta/vega off `bs.price`; the gross ramp decomposition (delta vs vega vs residual, DESIGN/91 §4) |
| `strategies/sg.py`, `strategies/sg_data.py`, `backtest_sg.py` | `evaluate_event` / `run` over both pre-registered entry offsets; entry-day/exit-day mart access reusing `sa_data`'s loaders |
| `validation/sg_harness.py`, `validation/run_report_sg.py` | entry-day-clustered t, BH, ten-trial deflated Sharpe, PBO, tail, spread halves, decomposition summary, go/no-go (DESIGN/91 §4) |
| `mart/intraday_rv.py` | one row per (underlying, day): RV5, Parkinson and Garman-Klass from the 5-minute `underlying_price` path, open/close and close-to-close returns, quality flag (G7, `findings/RESEARCH/47-edge-gaps.md` §2 G7) |
| `mart/earnings_history.py` | per-name realized earnings-move history: Yahoo 10y bars joined to `earnings_events`' dates on its AMC/BMO alignment, plus a point-in-time trailing summary; a **verified blocker** limits Finnhub's own historical depth, see the module docstring (G7) |
| `scripts/g7_rv_comparison.py` | the S-C-universe comparison of RV5 / close-to-close / Parkinson realized vol and the implied-minus-realized premium under each (G7 task 2; not consumed anywhere until `DESIGN/90` is edited) |
| `research/xs_factors.py` | pure factor construction: delta matching/interpolation (`match_iv_at_delta`), the nearest-30-day expiry, `iv_spread`, `put_skew`, `os_ratio` (RESEARCH/47 G4/G5) |
| `research/xs_stats.py` | per-week Spearman rank-IC and decile spread, cross-sectional OLS residualisation, NW/BH-style aggregation across formations (mean IC, sign consistency, half split, BH q-values) |
| `research/cross_section.py` | the G4/G5 orchestrator: builds the weekly universe from `daily_contract` (hot-chains coverage) + the screener spine (marketcap, sector, volume) + `join_short_side`, attaches next-week excess (`data/returns.parquet`) and the one-week `d_iv_spread`, runs the 8 pre-registered tests (4 factors x raw/residual) with BH q-values, the power/projected-date read (`engine.improve.power`) and the CBOE-chain-vs-hot-chains skew data-quality check; `make cross-section` -> `data/backtest/g4_factors.parquet` / `g4_results.json` |
| `strategies/xs.py` | the G4/G5 exploration-row generator: top/bottom-decile paper rows per factor, ten names a side, `policy_id="xs-1.0"`, `role="exploration"`, direction from the pre-registered hypothesis sign; `scripts/xs_rows.py --date` is a dry run (prints rows, writes nothing to `ledger/`) |

The S-A forward ledger opens 2026-10-01 and the S-B ledger (`ledger/sb/`) on 2026-09-11; before those dates
`make daily` writes `analyses/daily/<date>/` but does not touch `ledger/` unless `--force-ledger` is passed.
The backtest write-ups live in `~/Development/findings/market-analysis/RESEARCH/45-sa-backtest.md` (S-A) and
`RESEARCH/46-sb-backtest.md` (S-B); the S-B parameters are frozen by `tests/test_sb_frozen_params.py`.

| `watch/bars.py` | cached daily OHLCV, reusing `mart/earnings_history/bars/` read-only, falling back to its own cache `data/mart/watch/bars/` via `scripts/chart.py`; weekly resample |
| `watch/indicators.py` | Wilder RSI/ATR series, ATR-zigzag pivots (2x reversal), swing structure, anchored VWAP, crossed-within, 60-session/50-bin volume profile (POC + 70% value area), RSI bullish divergence |
| `watch/conditions.py` | the 17 watch-basket conditions as null-safe pure predicates, thresholds as module constants (DESIGN/110 §2) |
| `watch/basket.py` | `stacks`/`baskets` (LONG/SHORT/VOL/CONFLICT, DESIGN/110 §3) and `assign_episodes`/`episode_count` (the 21-session re-entry rule, §4), generic over baskets, conditions and counts |
| `watch/universe.py` | the nightly universe: `issue_type`, marketcap >= $1B, close >= $10, `daily_contract` coverage (DESIGN/110 §1) |
| `watch/tier1.py` | the tier-1 ATM pair (C-VOL), reusing S-C's F7/F8 verbatim (DESIGN/90-sc-spec.md) |
| `watch/flows.py` | C-LEAP and C-DP as daily DuckDB sums over the raw All Options / Dark Pool exports |
| `watch/series.py` | per-ticker point-in-time evaluation of the bar-derived conditions, built once per ticker over its cached history and evaluated online (no lookahead) at every panel night |
| `watch/retro.py`, `watch/retro_tables.py` | the R1 retrospective panel builder and its five descriptive tables (DESIGN/110 §5); `scripts/watch_retro.py` / `make watch-retro` -> `data/backtest/wb_conditions.parquet`, `wb_retro.json` |
| `watch/live.py` | R2's live replacements for the five conditions R1 read from `features.parquet`: `pct_52w_range` from the screener spine, the 5-day net call-OI build from the OI-changes files, unsigned total-premium/marketcap crowding from the All Options tape, the 5-day IV-rank change from the screener, and `load_closes` (screener-spine closes for h5/h10/h21 grading); `flows.py`/`tier1.py` are already live and unchanged |
| `watch/nightly.py`, `watch/wb_ledger.py` | the R2 nightly step: universe -> 17 conditions -> stacks/baskets -> one row per (name, night, basket) for LONG/SHORT/VOL (CONFLICT logged only, DESIGN/110 §3), the 21-session episode rule, `ledger/wb/forward_signals.parquet` (write-once + in-place grade-cell fill, `wb_ledger.py`), h5/h10/h21 SPY-excess grading; fail-soft (`available: false` + `reason` on any exception); called from `make daily` after the S-B step |
| `improve/basket_read.py` | R3, the wb-1.0 read (DESIGN/110 §6): independent-episode count with `excess_h21` resolved, NOT_DUE before the later of 2026-12-01 and 100 episodes (with a trailing-30-session projected date), hit rate vs the universe base of the same nights (live from the screener spine, never the ledger), two-sided binomial p, name-clustered t; `scripts/adjudicate.py basket --policy wb-1.0 [--basket LONG\|SHORT\|VOL]` writes the verdict once via `engine.improve.adjudicate.write_adjudication` |

S-G (`findings/market-analysis/DESIGN/91-sg-spec.md`) is a **backtest-only research pre-registration**,
not a champion: no `make daily` step, no forward ledger, no book caps, and therefore no frozen-params
test (`tests/test_sg_params.py` pins only the derived DSR trial count). It reuses S-A's filters F1..F4,
F7, F8 unchanged and F5/F6 at the entry day instead of `pre`; its own trial count (4) is added to S-A's
(6) for a 10-trial deflated-Sharpe charge. Results live in
`~/Development/findings/market-analysis/artifacts/edge-gaps/g3/results.md`.
