```
OKLO — 2026-10-23 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 630 · hot-chain 21/21 · ADV $311,498,816 · ATM spread — (tier —)
B  Earnings 2026-11-09 unknown session 2026-11-09 [NOT CONFIRMED (X1 for 45d): finnhub 2026-11-09 = screener 2026-11-10 = yfinance 2026-11-06] · ex-div — · expiries 2026-10-30, 2026-11-06 · FOMC 2026-10-28
C  Premium FAIR   iv30d 85.1 (own pct 44) · rv5_21 47.9 / c2c 57.6 · spread +37.2 / +27.5 · slope +23.2
   prior prints: 3, median realized/implied 0.71 · S-C: fails F5; F6 fails at 0.851 · S-A A1: F7 (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-10-30 ±$2.22 (straddle 2.22, cboe_chain 2026-10-23) · 1σ 30d ±$6.38 · ATR14 2.02 · GEX -, ZGL — (cboe_chain 2026-10-23)
E  Flags  borrow +0.5% (decile 0.4, IBKR 2026-10-23) · SI +20.0% / DTC 3.5 (FINRA 2026-09-30, pub 2026-10-13) · beta 4.08
          analyst: 4 changes last 10 sessions · Form 4: 0 buys / 18 sells 30d · VIX 19.4 contango, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -31.2% · ret63 -37.0% · 52w pos 0.00 · flow pct universe 0 / self 4
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: liquidity.atm_spread (no ATM pair within 2.5% of 26.15 at 2026-11-20 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-11-09 None, screener 2026-11-10 unknown, yfinance 2026-11-06 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
