```
PDD — 2026-10-23 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L3)   contracts 258 · hot-chain 21/21 · ADV $423,995,501 · ATM spread — (tier —)
B  Earnings 2026-11-16 pre session 2026-11-16 [NOT CONFIRMED (X1 for 45d): finnhub 2026-11-16 = screener 2026-11-17 = yfinance 2026-11-18] · ex-div — · expiries 2026-10-30, 2026-11-06 · FOMC 2026-10-28
C  Premium FAIR   iv30d 38.7 (own pct 63) · rv5_21 21.0 / c2c 26.1 · spread +17.7 / +12.6 · slope -7.8
   prior prints: 4, median realized/implied 1.86 · S-C: fails F3; F6 passes at 0.387 · S-A A1: F3 (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-10-30 ±$3.15 (straddle 3.15, cboe_chain 2026-10-23) · 1σ 30d ±$8.75 · ATR14 2.00 · GEX -, ZGL — (cboe_chain 2026-10-23)
E  Flags  borrow +0.4% (decile 0.4, IBKR 2026-10-23) · SI +2.1% / DTC 5.2 (FINRA 2026-09-30, pub 2026-10-13) · beta 0.85
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 19.4 contango, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 +1.1% · ret63 -6.8% · 52w pos 0.11 · flow pct universe 4 / self 45
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: liquidity.atm_spread (no ATM pair within 2.5% of 78.861 at 2026-11-20 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-11-16 bmo, screener 2026-11-17 unknown, yfinance 2026-11-18 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
