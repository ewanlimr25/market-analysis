```
MARA — 2026-10-16 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L2)   contracts 534 · hot-chain 21/21 · ADV $404,231,808 · ATM spread +1.9% (tier 1)
B  Earnings 2026-11-02 unknown session 2026-11-02 [NOT CONFIRMED (X1 for 45d): finnhub 2026-11-02 = screener 2026-11-03 = yfinance 2026-11-04] · ex-div — · expiries 2026-10-23, 2026-10-30 · FOMC 2026-10-28
C  Premium FAIR   iv30d 95.1 (own pct 83) · rv5_21 56.3 / c2c 72.7 · spread +38.8 / +22.4 · slope -3.2
   prior prints: 2, median realized/implied 0.67 · S-C: fails F2; F6 fails at 0.951 · S-A A1: F2 (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-10-23 ±$0.80 (straddle 0.80, cboe_chain 2026-10-16) · 1σ 30d ±$2.06 · ATR14 0.76 · GEX -, ZGL — (cboe_chain 2026-10-16)
E  Flags  borrow +0.6% (decile 0.4, IBKR 2026-10-16) · SI +26.6% / DTC 2.2 (FINRA 2026-09-30, pub 2026-10-13) X5 defined-risk preferred · beta 3.34
          analyst: 1 changes last 10 sessions · Form 4: 0 buys / 4 sells 30d · VIX 20.0 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -35.3% · ret63 -35.5% · 52w pos 0.05 · flow pct universe 98 / self 72
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-11-02 None, screener 2026-11-03 unknown, yfinance 2026-11-04 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
