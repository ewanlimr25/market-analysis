```
RDDT — 2026-09-25 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 568 · hot-chain 21/21 · ADV $729,079,148 · ATM spread — (tier —)
B  Earnings 2026-10-28 unknown session 2026-10-29 [confirmed: finnhub 2026-10-28 = screener 2026-10-29 = yfinance 2026-10-29] · ex-div — · expiries 2026-10-02, 2026-10-09 · FOMC 2026-10-28
C  Premium RICH   iv30d 57.2 (own pct 17) · rv5_21 39.6 / c2c 50.8 · spread +17.7 / +6.4 · slope +2.1
   prior prints: 2, median realized/implied 1.63 · S-C: fails F3; F6 passes at 0.572
D  Range  1σ box to 2026-10-02 ±$8.62 (straddle 8.62, cboe_chain 2026-09-25) · 1σ 30d ±$24.58 · ATR14 7.70 · GEX -, ZGL — (cboe_chain 2026-09-25)
E  Flags  borrow +0.4% (decile 0.4, IBKR 2026-09-24) · SI +14.1% / DTC 2.6 (FINRA 2026-08-31, pub 2026-09-14) · beta 1.96
          analyst: 1 changes last 10 sessions · Form 4: 0 buys / 19 sells 30d · VIX 14.9 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -3.6% · ret63 -10.2% · 52w pos 0.21 · flow pct universe 1 / self 31
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: liquidity.atm_spread (no ATM pair within 2.5% of 149.84 at 2026-10-23 with 5+ lots on both legs), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
