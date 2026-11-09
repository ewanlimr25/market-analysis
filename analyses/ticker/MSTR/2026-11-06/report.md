```
MSTR — 2026-11-06 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 1,383 · hot-chain 21/21 · ADV $2,552,951,710 · ATM spread — (tier —)
B  Earnings 2027-02-03 post session 2027-02-04 [NOT CONFIRMED (X1 for 45d): finnhub 2027-02-03 = screener 2027-02-04 = yfinance 2026-10-29] · ex-div — · expiries 2026-11-13, 2026-11-20 · FOMC 2026-12-09
C  Premium FAIR   iv30d 74.3 (own pct 63) · rv5_21 55.5 / c2c 77.1 · spread +18.8 / -2.8 · slope -2.4
   prior prints: 2, median realized/implied 0.54 · S-C: fails F3; F6 passes at 0.743 · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-13 ±$11.82 (straddle 11.82, cboe_chain 2026-11-06) · 1σ 30d ±$27.48 · ATR14 9.65 · GEX -, ZGL — (cboe_chain 2026-11-06)
E  Flags  borrow +0.4% (decile 0.3, IBKR 2026-11-06) · SI +7.2% / DTC 1.5 (FINRA 2026-10-15, pub 2026-10-28) · beta 3.05
          analyst: 2 changes last 10 sessions · Form 4: 0 buys / 11 sells 30d · VIX 25.6 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -14.9% · ret63 +32.5% · 52w pos 0.28 · flow pct universe 0 / self 23
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: liquidity.atm_spread (no ATM pair within 2.5% of 129.01 at 2026-12-04 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2027-02-03 amc, screener 2027-02-04 unknown, yfinance 2026-10-29 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
