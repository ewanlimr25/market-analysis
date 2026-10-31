```
MARA — 2026-10-30 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L2)   contracts 499 · hot-chain 21/21 · ADV $298,142,481 · ATM spread — (tier —)
B  Earnings 2026-11-02 unknown session 2026-11-02 [NOT CONFIRMED (X1 for 45d): finnhub 2026-11-02 = screener 2026-11-03 = yfinance 2026-11-04] · ex-div — · expiries 2026-11-06, 2026-11-13 · FOMC 2026-12-09
C  Premium FAIR   iv30d 105.8 (own pct 100) · rv5_21 61.1 / c2c 62.2 · spread +44.7 / +43.6 · slope -0.7
   prior prints: 2, median realized/implied 0.67 · S-C: fails F2; F6 fails at 1.058 · S-A A1: F2 (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-06 ±$0.86 (straddle 0.86, cboe_chain 2026-10-30) · 1σ 30d ±$2.05 · ATR14 0.65 · GEX -, ZGL — (cboe_chain 2026-10-30)
E  Flags  borrow +0.4% (decile 0.4, IBKR 2026-10-30) · SI +29.6% / DTC 3.2 (FINRA 2026-10-15, pub 2026-10-28) X5 defined-risk preferred · beta 3.36
          analyst: 1 changes last 10 sessions · Form 4: 0 buys / 2 sells 30d · VIX 19.4 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -39.6% · ret63 -42.4% · 52w pos 0.03 · flow pct universe 93 / self 45
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: liquidity.atm_spread (no ATM pair within 2.5% of 6.7422 at 2026-11-27 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-11-02 None, screener 2026-11-03 unknown, yfinance 2026-11-04 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
