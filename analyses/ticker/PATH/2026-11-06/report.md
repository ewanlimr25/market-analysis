```
PATH — 2026-11-06 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L3)   contracts 251 · hot-chain 16/21 · ADV $331,776,508 · ATM spread — (tier —)
B  Earnings 2026-12-01 post session 2026-12-02 [NOT CONFIRMED (X1 for 45d): finnhub 2026-12-01 = screener 2026-12-03 = yfinance 2026-12-03] · ex-div — · expiries 2026-11-13, 2026-11-20 · FOMC 2026-12-09
C  Premium FAIR   iv30d 73.2 (own pct 71) · rv5_21 40.6 / c2c 40.7 · spread +32.6 / +32.5 · slope +9.6
   prior prints: 2, median realized/implied 0.69 · S-C: fails F5; F6 passes at 0.732 · S-A A1: passes (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-13 ±$0.73 (straddle 0.73, cboe_chain 2026-11-06) · 1σ 30d ±$2.73 · ATR14 0.57 · GEX +, ZGL 15.00 (cboe_chain 2026-11-06)
E  Flags  borrow +0.4% (decile 0.3, IBKR 2026-11-06) · SI +25.4% / DTC 3.7 (FINRA 2026-10-15, pub 2026-10-28) X5 defined-risk preferred · beta 1.00
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 3 sells 30d · VIX 25.6 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -1.9% · ret63 -16.6% · 52w pos 0.36 · flow pct universe 4 / self 34
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: liquidity.atm_spread (no ATM pair within 2.5% of 12.985 at 2026-12-04 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-12-01 amc, screener 2026-12-03 postmarket, yfinance 2026-12-03 None), events.ex_div (screener next_dividend_date is not a date: 'NaT')
```
