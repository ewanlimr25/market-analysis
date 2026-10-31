```
INTC — 2026-10-30 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,963 · hot-chain 21/21 · ADV $10,615,319,761 · ATM spread +3.3% (tier 1)
B  Earnings 2027-01-20 post session 2027-01-21 [NOT CONFIRMED (X1 for 45d): finnhub 2027-01-20 = screener 2027-01-28 = yfinance 2027-01-28] · ex-div — · expiries 2026-11-06, 2026-11-13 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 59.4 (own pct 7) · rv5_21 41.9 / c2c 120.9 · spread +17.5 / -61.5 · slope -6.6
   prior prints: 1, median realized/implied 0.76 · S-C: fails F3; F6 passes at 0.594 · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-06 ±$5.33 (straddle 5.33, cboe_chain 2026-10-30) · 1σ 30d ±$11.14 · ATR14 6.97 · GEX -, ZGL — (cboe_chain 2026-10-30)
E  Flags  borrow +0.3% (decile 0.3, IBKR 2026-10-30) · SI +3.3% / DTC 1.5 (FINRA 2026-10-15, pub 2026-10-28) · beta 3.37
          analyst: 26 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 19.4 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -45.2% · ret63 -27.7% · 52w pos 0.30 · flow pct universe 0 / self 1
G  Structures (expiry 2026-11-27)
   IB              45P+ 65P- 65C- 87C+                      credit 8.13  max loss 1,386.50  BE 56.87–73.14  P(in) 0.38  cost 30.34  n=0  $0  [X1]
   IC              45P+ 55P- 75C- 87C+                      credit 1.68  max loss 1,032.00  BE 53.32–76.68  P(in) 0.52  cost 19.54  n=0  $0  [X1]
   SS              65P- 65C-                                credit 8.72  max loss —  BE 56.27–73.72  P(in) 0.40  cost 23.20  n=0  $0  [X1]
H  Ledger: sheet-1.0 exploration IB [X1] written
nulls: events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2027-01-20 amc, screener 2027-01-28 unknown, yfinance 2027-01-28 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
