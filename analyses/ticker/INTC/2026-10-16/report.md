```
INTC — 2026-10-16 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,749 · hot-chain 21/21 · ADV $11,796,452,971 · ATM spread +3.6% (tier 1)
B  Earnings 2026-10-21 post session 2026-10-22 [NOT CONFIRMED (X1 for 45d): finnhub 2026-10-21 = screener 2026-10-29 = yfinance 2026-10-29] · ex-div — · expiries 2026-10-23, 2026-10-30 · FOMC 2026-10-28
C  Premium FAIR   iv30d 67.0 (own pct 32) · rv5_21 40.7 / c2c 62.3 · spread +26.3 / +4.7 · slope +14.1
   prior prints: 1, median realized/implied 0.76 · S-C: fails F3; F6 passes at 0.670 · S-A A1: F3 (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-10-23 ±$6.27 (straddle 6.27, cboe_chain 2026-10-16) · 1σ 30d ±$17.25 · ATR14 5.85 · GEX -, ZGL — (cboe_chain 2026-10-16)
E  Flags  borrow +0.2% (decile 0.1, IBKR 2026-10-16) · SI +3.7% / DTC 1.4 (FINRA 2026-09-30, pub 2026-10-13) · beta 3.00
          analyst: 1 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 20.0 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -17.4% · ret63 -7.4% · 52w pos 0.52 · flow pct universe 0 / self 23
G  Structures (expiry 2026-11-13)
   IB              55P+ 90P- 90C- 123C+                     credit 12.78  max loss 2,222.00  BE 77.22–102.78  P(in) 0.54  cost 27.71  n=0  $0  [X1]
   IC              55P+ 75P- 106C- 123C+                    credit 2.85  max loss 1,714.50  BE 72.14–108.86  P(in) 0.72  cost 28.00  n=0  $0  [X1]
   SS              90P- 90C-                                credit 13.48  max loss —  BE 76.53–103.47  P(in) 0.57  cost 20.28  n=0  $0  [X1]
H  Ledger: sheet-1.0 exploration IB [X1] written
nulls: events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-10-21 amc, screener 2026-10-29 postmarket, yfinance 2026-10-29 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
