```
BE — 2026-10-16 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 1,339 · hot-chain 21/21 · ADV $3,772,929,685 · ATM spread — (tier —)
B  Earnings 2026-10-26 post session 2026-10-27 [NOT CONFIRMED (X1 for 45d): finnhub 2026-10-26 = screener 2026-10-22 = yfinance 2026-10-22] · ex-div — · expiries 2026-10-23, 2026-10-30 · FOMC 2026-10-28
C  Premium FAIR   iv30d 90.2 (own pct 34) · rv5_21 59.1 / c2c 82.5 · spread +31.1 / +7.7 · slope -10.7
   prior prints: 2, median realized/implied 1.13 · S-C: fails F3; F6 fails at 0.902 · S-A A1: F3 (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-10-23 ±$27.23 (straddle 27.23, cboe_chain 2026-10-16) · 1σ 30d ±$57.20 · ATR14 19.82 · GEX -, ZGL — (cboe_chain 2026-10-16)
E  Flags  borrow +0.3% (decile 0.3, IBKR 2026-10-16) · SI +7.6% / DTC 1.0 (FINRA 2026-09-30, pub 2026-10-13) · beta 4.40
          analyst: 4 changes last 10 sessions · Form 4: 0 buys / 1 sells 30d · VIX 20.0 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -21.2% · ret63 +12.3% · 52w pos 0.53 · flow pct universe 3 / self 44
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: liquidity.atm_spread (no ATM pair within 2.5% of 221.2001 at 2026-11-13 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-10-26 amc, screener 2026-10-22 postmarket, yfinance 2026-10-22 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
