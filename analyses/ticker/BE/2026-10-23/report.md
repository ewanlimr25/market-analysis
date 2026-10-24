```
BE — 2026-10-23 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,703 · hot-chain 21/21 · ADV $3,816,275,880 · ATM spread +0.6% (tier 1)
B  Earnings 2026-10-26 post session 2026-10-27 [NOT CONFIRMED (X1 for 45d): finnhub 2026-10-26 = screener 2027-02-04 = yfinance 2026-10-22] · ex-div — · expiries 2026-10-30, 2026-11-06 · FOMC 2026-10-28
C  Premium CHEAP   iv30d 79.0 (own pct 12) · rv5_21 56.6 / c2c 96.4 · spread +22.4 / -17.4 · slope -3.0
   prior prints: 2, median realized/implied 1.13 · S-C: fails F3; F6 passes at 0.790 · S-A A1: F3 (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-10-30 ±$18.47 (straddle 18.47, cboe_chain 2026-10-23) · 1σ 30d ±$43.97 · ATR14 20.28 · GEX -, ZGL — (cboe_chain 2026-10-23)
E  Flags  borrow +0.2% (decile 0.1, IBKR 2026-10-23) · SI +7.6% / DTC 1.0 (FINRA 2026-09-30, pub 2026-10-13) · beta 4.45
          analyst: 8 changes last 10 sessions · Form 4: 0 buys / 1 sells 30d · VIX 19.4 contango, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -27.5% · ret63 +2.7% · 52w pos 0.43 · flow pct universe 1 / self 21
G  Structures (expiry 2026-11-20)
   IB              110P+ 195P- 195C- 280C+                  credit 32.79  max loss 5,221.00  BE 162.21–227.79  P(in) 0.47  cost 21.29  n=0  $0  [X1]
   IC              110P+ 150P- 237.5C- 280C+                credit 5.98  max loss 3,652.00  BE 144.02–243.48  P(in) 0.67  cost 17.20  n=0  $0  [X1]
   SS              195P- 195C-                              credit 34.30  max loss —  BE 160.70–229.30  P(in) 0.49  cost 10.06  n=0  $0  [X1]
H  Ledger: sheet-1.0 exploration IB [X1] written
nulls: events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-10-26 amc, screener 2027-02-04 unknown, yfinance 2026-10-22 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
