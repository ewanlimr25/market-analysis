# Deterministic S-A engine (DESIGN/70). `make daily DATE=2026-10-14` after the 8 PM export lands.
PY ?= python3
DATE ?= $(shell date +%F)

.PHONY: daily validate mart backtest report test test-unit test-integration

daily:            ## preflight, append mart, candidates, grade, signals.json + report.md
	$(PY) -m engine.daily --date $(DATE)

validate:         ## check analyses/daily/$(DATE)/signals.json against schemas/signals.schema.json
	$(PY) scripts/validate_signals.py --file analyses/daily/$(DATE)/signals.json

mart:             ## rebuild both materialized tables (daily_contract ~3 min, earnings_events ~5 s)
	$(PY) -m engine.mart.daily_contract --rebuild
	$(PY) -m engine.mart.earnings_events --rebuild --force

backtest:         ## run S-A on the whole mart -> data/backtest/{trades,suppressed,dropped}.parquet
	$(PY) -m engine.backtest_sa

report:           ## season-split tables, BH, DSR, PBO, tail, robustness, go/no-go -> stdout
	$(PY) -m engine.validation.run_report

test-unit:
	$(PY) -m pytest -q -m unit

test-integration:
	$(PY) -m pytest -q -m integration

test: test-unit

# ---- S-B (DESIGN/80) ---------------------------------------------------------------------------
.PHONY: index-vol backtest-sb report-sb

index-vol:        ## refresh data/mart/index_vol/index_vol.parquet from the CBOE public CSVs
	$(PY) -m engine.mart.index_vol --refresh

backtest-sb:      ## proxy (3y) + marked (panel) S-B runs -> data/backtest/sb_*.parquet  (add REFRESH=1 to refetch inputs)
	$(PY) -m engine.backtest_sb $(if $(REFRESH),--refresh,)

report-sb:        ## sleeve tables, BH, DSR, PBO, month rule, tail, overlap, gate modes, go/no-go -> data/backtest/sb_report.md
	$(PY) -m engine.validation.run_sb_report

# ---- G8: CBOE full option chain (RESEARCH/47 §2 G8) -------------------------------------------
# Standalone, not part of `make daily`: a full chain is a multi-MB fetch per symbol and the nightly
# must stay fast and never touch S-A/S-B numbers. Run by hand, or on your own cron, after the close.
.PHONY: cboe-chain

cboe-chain:        ## fetch+store the full CBOE option chain for SPY, QQQ and SYMBOLS=... -> data/mart/cboe_chain/
	$(PY) -m engine.mart.cboe_chain --symbols SPY QQQ $(SYMBOLS)
# ---- G9: short interest, borrow, Reg SHO (RESEARCH/47 §2 G9; standalone, not part of `make daily`) --
.PHONY: short-interest

short-interest:    ## refresh FINRA short interest (full universe) + Reg SHO + IBKR borrow for DATE
	$(PY) -m engine.mart.short_interest --refresh --universe data/universe.json
	$(PY) -m engine.mart.regsho --refresh --date $(DATE)
	$(PY) -m engine.mart.borrow --refresh --date $(DATE)
# ---- G10: S-B challengers from the CBOE vol-index family (findings/market-analysis RESEARCH/47 §2) --
.PHONY: index-vol-ext sb-challengers

index-vol-ext:    ## refresh data/mart/index_vol_ext/index_vol_ext.parquet (VVIX, SKEW, two vol-index ratios)
	$(PY) -m engine.mart.index_vol_ext --refresh

sb-challengers:   ## proxy challenger table -> data/backtest/g10_sb_challengers.*  (add DRAFTS=1 for registration drafts)
	$(PY) scripts/sb_challengers.py $(if $(DRAFTS),--drafts,)
# ---- S-G (findings/market-analysis DESIGN/91, backtest-only research spec) ---------------------
.PHONY: backtest-sg report-sg

backtest-sg:      ## pre-earnings ramp (day -3 / -5 long straddle/strangle) -> data/backtest/g3_*.parquet
	$(PY) -m engine.backtest_sg

report-sg:        ## season table, BH, DSR, PBO, tail, spread halves, ramp decomposition, go/no-go -> data/backtest/g3_report.md
	$(PY) -m engine.validation.run_report_sg


# ---- G2: intraday flow event study (findings/market-analysis RESEARCH/47 §2 G2) ---------------
.PHONY: intraday-flow

intraday-flow:    ## whole-panel G2 build + analysis -> data/backtest/g2_*/, findings/.../g2/results.{md,json}
	$(PY) scripts/intraday_flow.py $(if $(DAYS),--days $(DAYS),) $(if $(FORCE),--force,)

# ---- Improvement process (findings/market-analysis DESIGN/100, D22) ---------------------------
.PHONY: power adjudicate

power:            ## n_required for a challenger: make power ARGS='--strategy sb --min-effect 0.01'
	$(PY) scripts/power.py $(ARGS)

adjudicate:       ## register / run / champion / gate: make adjudicate ARGS='champion --strategy sb --n-required 26'
	$(PY) scripts/adjudicate.py $(ARGS)

# ---- G6: expiration-day pinning (findings/market-analysis RESEARCH/47 §2 G6) -------------------
.PHONY: expiry-pinning

expiry-pinning:   ## build g6_pins.parquet + rate tables/verdict -> findings artifacts/edge-gaps/g6
	$(PY) scripts/expiry_pinning.py build
	$(PY) scripts/expiry_pinning.py report
# ---- G1: fill-price model from the panel's own NBBO (findings/market-analysis RESEARCH/47 §2) --
.PHONY: g1-fills g1-remark

g1-fills:         ## fill-quality over 103 days of All Options -> data/backtest/g1_fills.parquet + summary.md
	$(PY) scripts/fills.py

g1-remark:        ## re-mark the frozen S-A rows (a / b1 / b2 / ab1 / ab2) -> data/backtest/g1_remarked.parquet
	$(PY) scripts/g1_remark.py
