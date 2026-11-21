```
FCX — 2026-11-20 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 717 · hot-chain 21/21 · ADV $885,860,131 · ATM spread — (tier —)
B  Earnings 2027-01-20 post session 2027-01-21 [NOT CONFIRMED (X1 for 45d): finnhub 2027-01-20 = screener 2027-01-28 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium FAIR   iv30d 64.0 (own pct 100) · rv5_21 38.0 / c2c 57.6 · spread +26.0 / +6.4 · slope —
   prior prints: 2, median realized/implied 0.32 · S-C: fails F3; F6 passes at 0.640 · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-27 ±$3.32 (straddle 3.32, daily_contract tier 1) · 1σ 30d ±$8.42 · ATR14 3.05 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.2% (decile 0.1, IBKR 2026-11-20) · SI — / DTC 2.6 (FINRA 2026-10-30, pub 2026-11-12) · beta 2.18
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -28.8% · ret63 -40.9% · 52w pos 0.17 · flow pct universe 2 / self 10
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'FCX': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), liquidity.atm_spread (no ATM pair within 2.5% of 45.89 at 2026-12-18 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2027-01-20 amc, screener 2027-01-28 unknown), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'FCX': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'FCX': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
