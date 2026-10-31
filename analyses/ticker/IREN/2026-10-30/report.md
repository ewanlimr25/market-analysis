```
IREN — 2026-10-30 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 1,149 · hot-chain 21/21 · ADV $1,688,061,082 · ATM spread — (tier —)
B  Earnings 2026-11-04 unknown session 2026-11-04 [NOT CONFIRMED (X1 for 45d): finnhub 2026-11-04 = screener 2026-11-05 = yfinance 2026-11-05] · ex-div — · expiries 2026-11-06, 2026-11-13 · FOMC 2026-12-09
C  Premium FAIR   iv30d 118.8 (own pct 83) · rv5_21 63.0 / c2c 91.2 · spread +55.8 / +27.6 · slope -22.5
   prior prints: 2, median realized/implied 0.99 · S-C: fails F5; F6 fails at 1.188 · S-A A1: F7 (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-06 ±$4.30 (straddle 4.30, cboe_chain 2026-10-30) · 1σ 30d ±$8.17 · ATR14 2.65 · GEX -, ZGL — (cboe_chain 2026-10-30)
E  Flags  borrow +0.5% (decile 0.4, IBKR 2026-10-30) · SI +26.6% / DTC 1.8 (FINRA 2026-10-15, pub 2026-10-28) X5 defined-risk preferred · beta 4.04
          analyst: 1 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 19.4 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -41.1% · ret63 -39.7% · 52w pos 0.02 · flow pct universe 2 / self 39
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: liquidity.atm_spread (no ATM pair within 2.5% of 23.985 at 2026-11-27 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-11-04 None, screener 2026-11-05 postmarket, yfinance 2026-11-05 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
