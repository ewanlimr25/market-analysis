```
BL — 2026-09-18 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L3)   contracts 15 · hot-chain 0/21 · ADV $32,722,014 · ATM spread — (tier —)
B  Earnings 2026-11-04 post session 2026-11-05 [NOT CONFIRMED (X1 for 45d): finnhub 2026-11-04 = screener 2026-11-05 = yfinance 2026-11-03] · ex-div — · expiries 2026-10-16, 2026-11-20 · FOMC 2026-10-28
C  Premium CANNOT_MEASURE   iv30d 60.6 (own pct 22) · rv5_21 — / c2c 53.1 · spread — / +7.5 · slope +4.4
   prior prints: 2, median realized/implied 0.65 · S-C: fails F4; F6 passes at 0.606 · X1: no premium structure on this sheet
D  Range  1σ box to 2026-10-16 ±$3.75 (straddle 3.75, cboe_chain 2026-09-18) · 1σ 30d ±$4.89 · ATR14 1.45 · GEX +, ZGL 27.50 (cboe_chain 2026-09-18)
E  Flags  borrow +0.4% (decile 0.3, IBKR 2026-09-18) · SI +12.6% / DTC 6.1 (FINRA 2026-08-31, pub 2026-09-14) · beta 0.69
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 2 sells 30d · VIX 14.8 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -10.5% · ret63 +5.1% · 52w pos 0.10 · flow pct universe 24 / self 31
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: liquidity.atm_spread (no ATM pair within 2.5% of 28.14 at 2026-10-16 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-11-04 amc, screener 2026-11-05 unknown, yfinance 2026-11-03 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), premium.rv5_21 (0 quality intraday_rv sessions, fewer than 15)
```
