```
PDD — 2026-10-02 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 354 · hot-chain 21/21 · ADV $501,438,211 · ATM spread — (tier —)
B  Earnings 2026-11-16 pre session 2026-11-16 [NOT CONFIRMED (X1 for 45d): finnhub 2026-11-16 = screener 2026-11-17 = yfinance 2026-11-18] · ex-div — · expiries 2026-10-09, 2026-10-16 · FOMC 2026-10-28
C  Premium FAIR   iv30d 29.1 (own pct 5) · rv5_21 17.0 / c2c 20.9 · spread +12.2 / +8.2 · slope +1.3
   prior prints: 4, median realized/implied 1.86 · S-C: fails F3; F6 fails at 0.291 · X1: no premium structure on this sheet
D  Range  1σ box to 2026-10-09 ±$2.13 (straddle 2.13, cboe_chain 2026-10-02) · 1σ 30d ±$6.30 · ATR14 1.81 · GEX -, ZGL — (cboe_chain 2026-10-02)
E  Flags  borrow +0.2% (decile 0.1, IBKR 2026-10-02) · SI +2.1% / DTC 4.1 (FINRA 2026-09-15, pub 2026-09-28) · beta 0.95
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 1 sells 30d · VIX 15.3 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -8.4% · ret63 -10.0% · 52w pos 0.05 · flow pct universe 1 / self 23
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: liquidity.atm_spread (no ATM pair within 2.5% of 75.38 at 2026-10-30 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-11-16 bmo, screener 2026-11-17 unknown, yfinance 2026-11-18 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
