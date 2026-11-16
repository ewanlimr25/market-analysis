```
PATH — 2026-11-13 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L3)   contracts 282 · hot-chain 15/21 · ADV $305,297,847 · ATM spread — (tier —)
B  Earnings 2026-12-01 post session 2026-12-02 [NOT CONFIRMED (X1 for 45d): finnhub 2026-12-01 = screener 2026-12-03 = yfinance 2026-12-03] · ex-div — · expiries 2026-11-20, 2026-11-27 · FOMC 2026-12-09
C  Premium FAIR   iv30d 73.6 (own pct 71) · rv5_21 40.4 / c2c 37.3 · spread +33.2 / +36.3 · slope -13.5
   prior prints: 2, median realized/implied 0.69 · S-C: fails F5; F6 passes at 0.736 · S-A A1: passes (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-20 ±$0.85 (straddle 0.85, cboe_chain 2026-11-13) · 1σ 30d ±$2.80 · ATR14 0.53 · GEX +, ZGL 14.50 (cboe_chain 2026-11-13)
E  Flags  borrow +0.4% (decile 0.3, IBKR 2026-11-13) · SI +24.5% / DTC 3.8 (FINRA 2026-10-30, pub 2026-11-12) · beta 0.96
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 2 sells 30d · VIX 19.3 contango, CHOP/REBOUND-THRUST
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -3.2% · ret63 -17.0% · 52w pos 0.38 · flow pct universe 4 / self 48
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: liquidity.atm_spread (no ATM pair within 2.5% of 13.275 at 2026-12-11 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-12-01 amc, screener 2026-12-03 postmarket, yfinance 2026-12-03 None), events.ex_div (screener next_dividend_date is not a date: 'NaT')
```
