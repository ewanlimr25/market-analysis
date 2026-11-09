```
BE — 2026-11-06 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 1,509 · hot-chain 21/21 · ADV $3,808,864,601 · ATM spread — (tier —)
B  Earnings 2027-02-03 post session 2027-02-04 [NOT CONFIRMED (X1 for 45d): finnhub 2027-02-03 = screener 2027-02-04 = yfinance 2026-10-22] · ex-div — · expiries 2026-11-13, 2026-11-20 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 97.4 (own pct 49) · rv5_21 74.5 / c2c 110.4 · spread +22.9 / -13.0 · slope -9.9
   prior prints: 3, median realized/implied 0.65 · S-C: fails F3; F6 fails at 0.974 · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-13 ±$23.12 (straddle 23.12, cboe_chain 2026-11-06) · 1σ 30d ±$48.46 · ATR14 21.53 · GEX -, ZGL — (cboe_chain 2026-11-06)
E  Flags  borrow +0.3% (decile 0.2, IBKR 2026-11-06) · SI +6.2% / DTC 1.3 (FINRA 2026-10-15, pub 2026-10-28) · beta 4.32
          analyst: 4 changes last 10 sessions · Form 4: 0 buys / 2 sells 30d · VIX 25.6 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -36.5% · ret63 -17.8% · 52w pos 0.35 · flow pct universe 99 / self 60
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: liquidity.atm_spread (no ATM pair within 2.5% of 173.545 at 2026-12-04 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2027-02-03 amc, screener 2027-02-04 unknown, yfinance 2026-10-22 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
