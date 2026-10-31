```
ENPH — 2026-10-30 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 482 · hot-chain 18/21 · ADV $197,371,248 · ATM spread — (tier —)
B  Earnings 2027-02-01 post session 2027-02-02 [NOT CONFIRMED (X1 for 45d): finnhub 2027-02-01 = screener 2027-02-02 = yfinance 2026-10-27] · ex-div — · expiries 2026-11-06, 2026-11-13 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 64.1 (own pct 19) · rv5_21 51.3 / c2c 75.2 · spread +12.8 / -11.1 · slope +1.3
   prior prints: 2, median realized/implied 0.52 · S-C: fails F8; F6 passes at 0.641 · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-06 ±$1.97 (straddle 1.97, cboe_chain 2026-10-30) · 1σ 30d ±$4.72 · ATR14 1.94 · GEX -, ZGL — (cboe_chain 2026-10-30)
E  Flags  borrow +0.3% (decile 0.3, IBKR 2026-10-30) · SI +22.9% / DTC 6.3 (FINRA 2026-10-15, pub 2026-10-28) · beta 2.49
          analyst: 15 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 19.4 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -21.8% · ret63 -34.8% · 52w pos 0.04 · flow pct universe 10 / self 63
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: liquidity.atm_spread (no ATM pair within 2.5% of 25.675 at 2026-11-27 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2027-02-01 amc, screener 2027-02-02 unknown, yfinance 2026-10-27 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
