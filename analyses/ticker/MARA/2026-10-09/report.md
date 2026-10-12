```
MARA — 2026-10-09 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L2)   contracts 523 · hot-chain 21/21 · ADV $510,018,840 · ATM spread +3.6% (tier 1)
B  Earnings 2026-11-02 unknown session 2026-11-02 [NOT CONFIRMED (X1 for 45d): finnhub 2026-11-02 = screener 2026-11-03 = yfinance 2026-11-04] · ex-div — · expiries 2026-10-16, 2026-10-23 · FOMC 2026-10-28
C  Premium FAIR   iv30d 73.4 (own pct 2) · rv5_21 60.5 / c2c 66.4 · spread +12.9 / +6.9 · slope +1.2
   prior prints: 2, median realized/implied 0.67 · S-C: fails F2; F6 passes at 0.734 · S-A A1: F2 (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-10-16 ±$0.72 (straddle 0.72, cboe_chain 2026-10-09) · 1σ 30d ±$2.03 · ATR14 0.79 · GEX -, ZGL — (cboe_chain 2026-10-09)
E  Flags  borrow +0.2% (decile 0.1, IBKR 2026-10-09) · SI +26.6% / DTC 2.4 (FINRA 2026-09-15, pub 2026-09-28) X5 defined-risk preferred · beta 3.29
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 4 sells 30d · VIX 14.8 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -15.6% · ret63 -20.8% · 52w pos 0.18 · flow pct universe 1 / self 12
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-11-02 None, screener 2026-11-03 unknown, yfinance 2026-11-04 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
