```
PDD — 2026-11-20 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 411 · hot-chain 21/21 · ADV $591,581,319 · ATM spread +7.1% (tier 1)
B  Earnings ?  session 2027-03-24 [NOT CONFIRMED (X1 for 45d): finnhub ? = screener 2027-03-24 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 34.8 (own pct 38) · rv5_21 24.1 / c2c 45.9 · spread +10.7 / -11.1 · slope —
   prior prints: 5, median realized/implied 1.82 · S-C: fails F3; F6 passes at 0.348 · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-27 ±$3.60 (straddle 3.60, daily_contract tier 2) · 1σ 30d ±$8.34 · ATR14 2.88 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.2% (decile 0.1, IBKR 2026-11-20) · SI — / DTC 6.1 (FINRA 2026-10-30, pub 2026-11-12) · beta 0.44
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 +5.7% · ret63 -3.9% · 52w pos 0.22 · flow pct universe 2 / self 25
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'PDD': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.finnhub (finnhub /calendar/earnings: no print scheduled on or after 2026-11-20), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), events.earnings.date (finnhub /calendar/earnings: no print scheduled on or after 2026-11-20), events.ex_div (screener next_dividend_date is not a date: 'NaT'), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'PDD': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'PDD': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
