```
BE — 2026-11-13 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 1,306 · hot-chain 21/21 · ADV $3,658,350,488 · ATM spread — (tier —)
B  Earnings 2027-02-03 post session 2027-02-04 [NOT CONFIRMED (X1 for 45d): finnhub 2027-02-03 = screener 2027-02-04 = yfinance 2026-10-22] · ex-div — · expiries 2026-11-20, 2026-11-27 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 91.3 (own pct 48) · rv5_21 77.7 / c2c 124.0 · spread +13.6 / -32.7 · slope -9.8
   prior prints: 3, median realized/implied 0.65 · S-C: fails F3; F6 fails at 0.913 · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-20 ±$20.85 (straddle 20.85, cboe_chain 2026-11-13) · 1σ 30d ±$50.24 · ATR14 21.69 · GEX -, ZGL — (cboe_chain 2026-11-13)
E  Flags  borrow +0.2% (decile 0.1, IBKR 2026-11-13) · SI +6.4% / DTC 1.1 (FINRA 2026-10-30, pub 2026-11-12) · beta 4.29
          analyst: 2 changes last 10 sessions · Form 4: 0 buys / 2 sells 30d · VIX 19.3 contango, CHOP/REBOUND-THRUST
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -18.8% · ret63 -17.3% · 52w pos 0.42 · flow pct universe 0 / self 18
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: liquidity.atm_spread (no ATM pair within 2.5% of 191.95 at 2026-12-11 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2027-02-03 amc, screener 2027-02-04 unknown, yfinance 2026-10-22 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
