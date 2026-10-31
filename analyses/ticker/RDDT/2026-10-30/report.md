```
RDDT — 2026-10-30 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,420 · hot-chain 21/21 · ADV $851,416,176 · ATM spread +6.1% (tier 1)
B  Earnings 2027-02-03 post session 2027-02-04 [NOT CONFIRMED (X1 for 45d): finnhub 2027-02-03 = screener 2027-02-04 = yfinance 2026-10-29] · ex-div — · expiries 2026-11-06, 2026-11-13 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 66.4 (own pct 45) · rv5_21 50.1 / c2c 122.1 · spread +16.3 / -55.7 · slope -2.9
   prior prints: 2, median realized/implied 1.63 · S-C: passes F1..F9 · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-06 ±$7.67 (straddle 7.67, cboe_chain 2026-10-30) · 1σ 30d ±$17.45 · ATR14 9.91 · GEX -, ZGL — (cboe_chain 2026-10-30)
E  Flags  borrow +0.3% (decile 0.3, IBKR 2026-10-30) · SI +15.3% / DTC 5.1 (FINRA 2026-10-15, pub 2026-10-28) · beta 2.25
          analyst: 10 changes last 10 sessions · Form 4: 0 buys / 17 sells 30d · VIX 19.4 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -38.7% · ret63 -40.7% · 52w pos 0.01 · flow pct universe 1 / self 6
G  Structures (expiry 2026-11-27)
   IB              80P+ 90P- 90C- 125C+                     credit 10.73  max loss 2,426.50  BE 100.73  P(touch) —  cost 86.40  n=0  $0  [X1]
   IC                                                        —  max loss —  BE —  P(touch) —  cost —  n=0  $—  [X1]  (the strike grid is too coarse for the sigma_hold wings)
   SS              90P- 90C-                                credit 13.30  max loss —  BE 76.70–103.30  P(in) 0.45  cost 62.62  n=0  $0  [X1]
H  Ledger: sheet-1.0 exploration IB [X1] written
nulls: events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2027-02-03 amc, screener 2027-02-04 unknown, yfinance 2026-10-29 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
