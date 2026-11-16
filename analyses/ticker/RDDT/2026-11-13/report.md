```
RDDT — 2026-11-13 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 580 · hot-chain 21/21 · ADV $850,460,581 · ATM spread — (tier —)
B  Earnings 2027-02-03 post session 2027-02-04 [NOT CONFIRMED (X1 for 45d): finnhub 2027-02-03 = screener 2027-02-04 = yfinance 2026-10-29] · ex-div — · expiries 2026-11-20, 2026-11-27 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 60.1 (own pct 30) · rv5_21 53.1 / c2c 129.8 · spread +7.0 / -69.7 · slope -6.6
   prior prints: 3, median realized/implied 1.84 · S-C: fails F8; F6 passes at 0.601 · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-20 ±$6.76 (straddle 6.76, cboe_chain 2026-11-13) · 1σ 30d ±$16.95 · ATR14 8.07 · GEX -, ZGL — (cboe_chain 2026-11-13)
E  Flags  borrow +0.2% (decile 0.1, IBKR 2026-11-13) · SI +15.6% / DTC 2.7 (FINRA 2026-10-30, pub 2026-11-12) · beta 2.17
          analyst: 6 changes last 10 sessions · Form 4: 0 buys / 3 sells 30d · VIX 19.3 contango, CHOP/REBOUND-THRUST
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -38.2% · ret63 -40.2% · 52w pos 0.05 · flow pct universe 99 / self 67
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: liquidity.atm_spread (no ATM pair within 2.5% of 98.39 at 2026-12-11 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2027-02-03 amc, screener 2027-02-04 unknown, yfinance 2026-10-29 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
