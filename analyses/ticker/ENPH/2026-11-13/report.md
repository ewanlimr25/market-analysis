```
ENPH — 2026-11-13 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 402 · hot-chain 21/21 · ADV $235,103,519 · ATM spread — (tier —)
B  Earnings 2027-02-01 post session 2027-02-02 [NOT CONFIRMED (X1 for 45d): finnhub 2027-02-01 = screener 2027-02-02 = yfinance 2026-10-27] · ex-div — · expiries 2026-11-20, 2026-11-27 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 64.0 (own pct 20) · rv5_21 61.2 / c2c 89.3 · spread +2.8 / -25.3 · slope +9.6
   prior prints: 3, median realized/implied 0.73 · S-C: fails F8; F6 passes at 0.640 · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-20 ±$1.81 (straddle 1.81, cboe_chain 2026-11-13) · 1σ 30d ±$4.78 · ATR14 2.12 · GEX -, ZGL — (cboe_chain 2026-11-13)
E  Flags  borrow +0.2% (decile 0.1, IBKR 2026-11-13) · SI +21.3% / DTC 3.4 (FINRA 2026-10-30, pub 2026-11-12) · beta 2.31
          analyst: 0 changes last 10 sessions · Form 4: 2 buys / 1 sells 30d · VIX 19.3 contango, CHOP/REBOUND-THRUST
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -15.4% · ret63 -32.5% · 52w pos 0.04 · flow pct universe 96 / self 69
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: liquidity.atm_spread (no ATM pair within 2.5% of 26.075 at 2026-12-11 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2027-02-01 amc, screener 2027-02-02 unknown, yfinance 2026-10-27 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
