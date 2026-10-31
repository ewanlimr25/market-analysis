```
BE — 2026-10-30 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 1,436 · hot-chain 21/21 · ADV $3,530,694,082 · ATM spread — (tier —)
B  Earnings 2027-02-03 post session 2027-02-04 [NOT CONFIRMED (X1 for 45d): finnhub 2027-02-03 = screener 2027-02-04 = yfinance 2026-10-22] · ex-div — · expiries 2026-11-06, 2026-11-13 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 83.4 (own pct 26) · rv5_21 59.8 / c2c 90.2 · spread +23.6 / -6.8 · slope -3.2
   prior prints: 2, median realized/implied 1.13 · S-C: fails F3; F6 fails at 0.834 · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-06 ±$20.95 (straddle 20.95, cboe_chain 2026-10-30) · 1σ 30d ±$48.56 · ATR14 19.71 · GEX -, ZGL — (cboe_chain 2026-10-30)
E  Flags  borrow +0.4% (decile 0.4, IBKR 2026-10-30) · SI +6.2% / DTC 1.3 (FINRA 2026-10-15, pub 2026-10-28) · beta 4.48
          analyst: 9 changes last 10 sessions · Form 4: 0 buys / 1 sells 30d · VIX 19.4 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -26.8% · ret63 -6.9% · 52w pos 0.46 · flow pct universe 0 / self 10
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: liquidity.atm_spread (no ATM pair within 2.5% of 203.08 at 2026-11-27 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2027-02-03 amc, screener 2027-02-04 unknown, yfinance 2026-10-22 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
