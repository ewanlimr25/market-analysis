```
ADBE — 2026-11-20 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 859 · hot-chain 21/21 · ADV $957,547,765 · ATM spread +5.6% (tier 1)
B  Earnings 2026-12-08 post session 2026-12-09 [NOT CONFIRMED (X1 for 45d): finnhub 2026-12-08 = screener 2026-12-09 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium FAIR   iv30d 63.2 (own pct 100) · rv5_21 30.7 / c2c 28.8 · spread +32.5 / +34.4 · slope —
   prior prints: 2, median realized/implied 0.53 · S-C: fails F3; F6 passes at 0.632 · S-A A1: F3 (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-27 ±$12.90 (straddle 12.90, daily_contract tier 2) · 1σ 30d ±$39.43 · ATR14 8.94 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.4% (decile 0.3, IBKR 2026-11-20) · SI — / DTC 4.2 (FINRA 2026-10-30, pub 2026-11-12) · beta 0.21
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -19.5% · ret63 -21.2% · 52w pos 0.16 · flow pct universe 3 / self 36
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'ADBE': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-12-08 amc, screener 2026-12-09 postmarket), events.ex_div (screener next_dividend_date is not a date: 'NaT'), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'ADBE': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'ADBE': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
