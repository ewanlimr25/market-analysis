```
PDD — 2026-10-30 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L3)   contracts 295 · hot-chain 21/21 · ADV $412,974,963 · ATM spread — (tier —)
B  Earnings 2026-11-16 pre session 2026-11-16 [NOT CONFIRMED (X1 for 45d): finnhub 2026-11-16 = screener 2026-11-17 = yfinance 2026-11-18] · ex-div — · expiries 2026-11-06, 2026-11-13 · FOMC 2026-12-09
C  Premium FAIR   iv30d 40.4 (own pct 74) · rv5_21 21.4 / c2c 26.3 · spread +19.0 / +14.1 · slope +3.5
   prior prints: 4, median realized/implied 1.86 · S-C: fails F3; F6 passes at 0.404 · S-A A1: F3 (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-06 ±$2.64 (straddle 2.64, cboe_chain 2026-10-30) · 1σ 30d ±$9.11 · ATR14 1.98 · GEX -, ZGL — (cboe_chain 2026-10-30)
E  Flags  borrow +0.2% (decile 0.1, IBKR 2026-10-30) · SI +2.3% / DTC 5.7 (FINRA 2026-10-15, pub 2026-10-28) · beta 0.82
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 19.4 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 +2.8% · ret63 -12.8% · 52w pos 0.10 · flow pct universe 99 / self 79
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: liquidity.atm_spread (no ATM pair within 2.5% of 78.63 at 2026-11-27 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-11-16 bmo, screener 2026-11-17 unknown, yfinance 2026-11-18 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
