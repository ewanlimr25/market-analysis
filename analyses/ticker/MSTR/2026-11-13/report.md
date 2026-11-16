```
MSTR — 2026-11-13 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 1,575 · hot-chain 21/21 · ADV $2,311,086,445 · ATM spread — (tier —)
B  Earnings 2027-02-03 post session 2027-02-04 [NOT CONFIRMED (X1 for 45d): finnhub 2027-02-03 = screener 2027-02-04 = yfinance 2026-10-29] · ex-div — · expiries 2026-11-20, 2026-11-27 · FOMC 2026-12-09
C  Premium FAIR   iv30d 74.7 (own pct 60) · rv5_21 56.9 / c2c 74.7 · spread +17.8 / -0.0 · slope -4.8
   prior prints: 3, median realized/implied 0.59 · S-C: fails F3; F6 passes at 0.747 · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-20 ±$9.57 (straddle 9.57, cboe_chain 2026-11-13) · 1σ 30d ±$23.92 · ATR14 8.83 · GEX -, ZGL — (cboe_chain 2026-11-13)
E  Flags  borrow +0.3% (decile 0.3, IBKR 2026-11-13) · SI +6.7% / DTC 1.4 (FINRA 2026-10-30, pub 2026-11-12) · beta 2.92
          analyst: 2 changes last 10 sessions · Form 4: 0 buys / 6 sells 30d · VIX 19.3 contango, CHOP/REBOUND-THRUST
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -26.2% · ret63 +14.3% · 52w pos 0.21 · flow pct universe 1 / self 48
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: liquidity.atm_spread (no ATM pair within 2.5% of 111.67 at 2026-12-11 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2027-02-03 amc, screener 2027-02-04 unknown, yfinance 2026-10-29 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
