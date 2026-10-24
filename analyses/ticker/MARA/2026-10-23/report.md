```
MARA — 2026-10-23 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L2)   contracts 479 · hot-chain 21/21 · ADV $328,367,218 · ATM spread — (tier —)
B  Earnings 2026-11-02 unknown session 2026-11-02 [NOT CONFIRMED (X1 for 45d): finnhub 2026-11-02 = screener 2026-11-03 = yfinance 2026-11-04] · ex-div — · expiries 2026-10-30, 2026-11-06 · FOMC 2026-10-28
C  Premium FAIR   iv30d 96.5 (own pct 90) · rv5_21 56.8 / c2c 54.7 · spread +39.7 / +41.8 · slope +3.9
   prior prints: 2, median realized/implied 0.67 · S-C: fails F2; F6 fails at 0.965 · S-A A1: F2 (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-10-30 ±$0.76 (straddle 0.76, cboe_chain 2026-10-23) · 1σ 30d ±$1.99 · ATR14 0.71 · GEX -, ZGL — (cboe_chain 2026-10-23)
E  Flags  borrow +0.3% (decile 0.3, IBKR 2026-10-23) · SI +26.6% / DTC 2.2 (FINRA 2026-09-30, pub 2026-10-13) X5 defined-risk preferred · beta 3.39
          analyst: 2 changes last 10 sessions · Form 4: 0 buys / 2 sells 30d · VIX 19.4 contango, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -45.7% · ret63 -40.4% · 52w pos 0.03 · flow pct universe 1 / self 9
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: liquidity.atm_spread (no ATM pair within 2.5% of 7.2099 at 2026-11-20 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-11-02 None, screener 2026-11-03 unknown, yfinance 2026-11-04 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
