```
IREN — 2026-11-13 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,308 · hot-chain 21/21 · ADV $1,557,364,990 · ATM spread +2.1% (tier 1)
B  Earnings 2027-02-03 unknown session 2027-02-04 [confirmed: finnhub 2027-02-03 = screener 2027-02-04 = yfinance 2027-02-04] · ex-div — · expiries 2026-11-20, 2026-11-27 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 112.5 (own pct 72) · rv5_21 89.5 / c2c 138.3 · spread +23.0 / -25.8 · slope -8.6
   prior prints: 3, median realized/implied 0.71 · S-C: fails F6
D  Range  1σ box to 2026-11-20 ±$2.42 (straddle 2.42, cboe_chain 2026-11-13) · 1σ 30d ±$5.87 · ATR14 2.74 · GEX -, ZGL — (cboe_chain 2026-11-13)
E  Flags  borrow +0.8% (decile 0.5, IBKR 2026-11-13) · SI +25.4% / DTC 1.7 (FINRA 2026-10-30, pub 2026-11-12) X5 defined-risk preferred · beta 3.86
          analyst: 6 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 19.3 contango, CHOP/REBOUND-THRUST
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -40.2% · ret63 -59.5% · 52w pos 0.02 · flow pct universe 0 / self 25
G  Structures (expiry 2026-12-11)
   IB              7P+ 18P- 18C- 30C+                       credit 4.20  max loss 780.00  BE 13.80–22.20  P(in) 0.60  cost 6.69  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   IC              7P+ 13P- 24C- 30C+                       credit 0.85  max loss 515.00  BE 12.15–24.85  P(in) 0.79  cost 6.10  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   SS              18P- 18C-                                credit 4.47  max loss —  BE 13.53–22.47  P(in) 0.63  cost 3.64  n=0  $0  (ALLOW_UNDEFINED=0: measurement only)
H  Ledger: sheet-1.0 exploration IB [F6] written
nulls: events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
