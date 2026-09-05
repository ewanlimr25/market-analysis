# Deterministic S-A engine (DESIGN/70). `make daily DATE=2026-10-14` after the 8 PM export lands.
PY ?= python3
DATE ?= $(shell date +%F)

.PHONY: daily mart backtest report test test-unit test-integration

daily:            ## preflight, append mart, candidates, grade, signals.json + report.md
	$(PY) -m engine.daily --date $(DATE)

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
