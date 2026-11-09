```
SNOW — 2026-11-06 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 828 · hot-chain 21/21 · ADV $1,488,694,165 · ATM spread — (tier —)
B  Earnings 2026-12-01 post session 2026-12-02 [NOT CONFIRMED (X1 for 45d): finnhub 2026-12-01 = screener 2026-12-02 = yfinance 2026-12-02] · ex-div — · expiries 2026-11-13, 2026-11-20 · FOMC 2026-12-09
C  Premium FAIR   iv30d 77.8 (own pct 87) · rv5_21 44.9 / c2c 65.2 · spread +32.9 / +12.6 · slope -1.2
   prior prints: 2, median realized/implied 2.22 · S-C: fails F3; F6 passes at 0.778 · S-A A1: F3 (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-13 ±$19.78 (straddle 19.78, cboe_chain 2026-11-06) · 1σ 30d ±$61.66 · ATR14 16.56 · GEX -, ZGL — (cboe_chain 2026-11-06)
E  Flags  borrow +0.2% (decile 0.1, IBKR 2026-11-06) · SI +5.4% / DTC 4.4 (FINRA 2026-10-15, pub 2026-10-28) · beta 1.42
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 13 sells 30d · VIX 25.6 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -19.7% · ret63 -17.6% · 52w pos 0.59 · flow pct universe 100 / self 93
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: liquidity.atm_spread (no ATM pair within 2.5% of 276.43 at 2026-12-04 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-12-01 amc, screener 2026-12-02 postmarket, yfinance 2026-12-02 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
