```
ENPH — 2026-10-16 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 382 · hot-chain 17/21 · ADV $165,622,949 · ATM spread — (tier —)
B  Earnings 2026-10-26 post session 2026-10-27 [NOT CONFIRMED (X1 for 45d): finnhub 2026-10-26 = screener 2026-10-27 = yfinance 2026-10-27] · ex-div — · expiries 2026-10-23, 2026-10-30 · FOMC 2026-10-28
C  Premium FAIR   iv30d 79.5 (own pct 48) · rv5_21 46.1 / c2c 48.6 · spread +33.4 / +30.9 · slope +26.6
   prior prints: 2, median realized/implied 0.52 · S-C: fails F5; F6 passes at 0.795 · S-A A1: F7 (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-10-23 ±$2.20 (straddle 2.20, cboe_chain 2026-10-16) · 1σ 30d ±$6.98 · ATR14 1.76 · GEX -, ZGL — (cboe_chain 2026-10-16)
E  Flags  borrow +0.3% (decile 0.3, IBKR 2026-10-16) · SI +21.9% / DTC 5.5 (FINRA 2026-09-30, pub 2026-10-13) · beta 2.62
          analyst: 3 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 20.0 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -15.0% · ret63 -22.4% · 52w pos 0.10 · flow pct universe 93 / self 69
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: liquidity.atm_spread (no ATM pair within 2.5% of 30.63 at 2026-11-13 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-10-26 amc, screener 2026-10-27 postmarket, yfinance 2026-10-27 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
