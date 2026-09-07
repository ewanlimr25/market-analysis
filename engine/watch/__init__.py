"""The watch-basket exploration book (`findings/market-analysis/DESIGN/110-watch-basket.md`).

A pre-registered, paper-only book of 20 stacked technical/flow conditions computed nightly across
the screener universe. Nothing here sizes a trade or touches a frozen parameter; see `DESIGN/110`
for the full contract (conditions in §2, stacks/baskets in §3, the episode rule in §4, the
retrospective in §5).

R1 (this package): `bars.py` (cached daily OHLCV), `indicators.py` (RSI, ATR, zigzag, anchored
VWAP, volume profile), `conditions.py` (the 17 rules, null-safe; C-DIV-D and C-POC-A/C-POC-A-LOSS
added 2026-09-07 evening make 20), `basket.py` (stacks, baskets, episodes), `retro.py` (the
descriptive retrospective run once at build, DESIGN/110 §5).
"""
