```
MSTR — 2026-10-30 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,631 · hot-chain 21/21 · ADV $2,757,767,575 · ATM spread +2.6% (tier 1)
B  Earnings 2027-02-03 post session 2027-02-04 [NOT CONFIRMED (X1 for 45d): finnhub 2027-02-03 = screener 2027-02-04 = yfinance 2026-10-29] · ex-div — · expiries 2026-11-06, 2026-11-13 · FOMC 2026-12-09
C  Premium FAIR   iv30d 75.4 (own pct 66) · rv5_21 49.7 / c2c 70.4 · spread +25.7 / +5.0 · slope -3.8
   prior prints: 2, median realized/implied 0.54 · S-C: fails F3; F6 passes at 0.754 · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-06 ±$12.45 (straddle 12.45, cboe_chain 2026-10-30) · 1σ 30d ±$28.18 · ATR14 9.49 · GEX -, ZGL — (cboe_chain 2026-10-30)
E  Flags  borrow +0.2% (decile 0.1, IBKR 2026-10-30) · SI +7.2% / DTC 1.5 (FINRA 2026-10-15, pub 2026-10-28) · beta 3.17
          analyst: 1 changes last 10 sessions · Form 4: 0 buys / 5 sells 30d · VIX 19.4 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -18.7% · ret63 +37.6% · 52w pos 0.25 · flow pct universe 0 / self 29
G  Structures (expiry 2026-11-27)
   IB              75P+ 130P- 130C- 185C+                   credit 20.56  max loss 3,444.00  BE 109.44–150.56  P(in) 0.50  cost 57.50  n=0  $0  [X1]
   IC              75P+ 105P- 160C- 185C+                   credit 3.90  max loss 2,610.50  BE 101.11–163.90  P(in) 0.70  cost 38.52  n=0  $0  [X1]
   SS              130P- 130C-                              credit 21.62  max loss —  BE 108.38–151.62  P(in) 0.53  cost 34.88  n=0  $0  [X1]
H  Ledger: sheet-1.0 exploration IB [X1] written
nulls: events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2027-02-03 amc, screener 2027-02-04 unknown, yfinance 2026-10-29 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
