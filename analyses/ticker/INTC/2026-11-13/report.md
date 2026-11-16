```
INTC — 2026-11-13 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,390 · hot-chain 21/21 · ADV $10,062,394,947 · ATM spread +3.5% (tier 1)
B  Earnings 2027-01-20 post session 2027-01-21 [NOT CONFIRMED (X1 for 45d): finnhub 2027-01-20 = screener 2027-01-28 = yfinance 2027-01-28] · ex-div — · expiries 2026-11-20, 2026-11-27 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 65.3 (own pct 28) · rv5_21 53.0 / c2c 136.9 · spread +12.3 / -71.6 · slope -7.9
   prior prints: 2, median realized/implied 1.58 · S-C: fails F3; F6 passes at 0.653 · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-20 ±$4.96 (straddle 4.96, cboe_chain 2026-11-13) · 1σ 30d ±$11.16 · ATR14 5.72 · GEX -, ZGL — (cboe_chain 2026-11-13)
E  Flags  borrow +0.2% (decile 0.1, IBKR 2026-11-13) · SI +3.3% / DTC 1.2 (FINRA 2026-10-30, pub 2026-11-12) · beta 3.24
          analyst: 3 changes last 10 sessions · Form 4: 1 buys / 0 sells 30d · VIX 19.3 contango, CHOP/REBOUND-THRUST
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -37.4% · ret63 -42.4% · 52w pos 0.24 · flow pct universe 100 / self 67
G  Structures (expiry 2026-12-11)
   IB              40P+ 60P- 60C- 81C+                      credit 8.15  max loss 1,285.00  BE 51.85–68.15  P(in) 0.39  cost 25.96  n=0  $0  [X1]
   IC              40P+ 49P- 70C- 81C+                      credit 1.54  max loss 946.00  BE 47.46–71.54  P(in) 0.56  cost 21.29  n=0  $0  [X1]
   SS              60P- 60C-                                credit 8.62  max loss —  BE 51.38–68.62  P(in) 0.41  cost 17.36  n=0  $0  [X1]
H  Ledger: sheet-1.0 exploration IB [X1] written
nulls: events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2027-01-20 amc, screener 2027-01-28 unknown, yfinance 2027-01-28 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
