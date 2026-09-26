```
SOFI — 2026-09-25 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 675 · hot-chain 21/21 · ADV $765,650,947 · ATM spread +2.8% (tier 1)
B  Earnings 2026-10-26 pre session 2026-10-26 [NOT CONFIRMED (X1 for 45d): finnhub 2026-10-26 = screener 2026-10-27 = yfinance 2026-10-27] · ex-div — · expiries 2026-10-02, 2026-10-09 · FOMC 2026-10-28
C  Premium FAIR   iv30d 43.1 (own pct 1) · rv5_21 34.2 / c2c 41.9 · spread +8.9 / +1.3 · slope +0.7
   prior prints: 2, median realized/implied 1.44 · S-C: fails F3; F6 passes at 0.431 · X1: no premium structure on this sheet
D  Range  1σ box to 2026-10-02 ±$0.75 (straddle 0.75, cboe_chain 2026-09-25) · 1σ 30d ±$2.05 · ATR14 0.70 · GEX -, ZGL — (cboe_chain 2026-09-25)
E  Flags  borrow +0.3% (decile 0.3, IBKR 2026-09-24) · SI +14.9% / DTC 4.1 (FINRA 2026-08-31, pub 2026-09-14) · beta 2.68
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 2 sells 30d · VIX 14.9 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -12.0% · ret63 -7.3% · 52w pos 0.10 · flow pct universe 98 / self 66
G  Structures (expiry 2026-10-23)
   IB              13P+ 16.5P- 16.5C- 20.5C+                credit 1.46  max loss 253.50  BE 15.04–17.96  P(in) 0.46  cost 5.81  n=0  $0  [X1]
   IC              13P+ 14.5P- 18.5C- 20.5C+                credit 0.26  max loss 174.00  BE 14.24–18.76  P(in) 0.66  cost 4.94  n=0  $0  [X1]
   SS              16.5P- 16.5C-                            credit 1.57  max loss —  BE 14.93–18.07  P(in) 0.49  cost 3.34  n=0  $0  [X1]
H  Ledger: sheet-1.0 exploration IB [X1] written
nulls: events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-10-26 bmo, screener 2026-10-27 unknown, yfinance 2026-10-27 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
