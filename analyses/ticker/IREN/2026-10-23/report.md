```
IREN — 2026-10-23 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,096 · hot-chain 21/21 · ADV $1,675,424,544 · ATM spread +2.0% (tier 1)
B  Earnings 2026-11-04 unknown session 2026-11-04 [NOT CONFIRMED (X1 for 45d): finnhub 2026-11-04 = screener 2026-11-05 = yfinance 2026-11-05] · ex-div — · expiries 2026-10-30, 2026-11-06 · FOMC 2026-10-28
C  Premium FAIR   iv30d 111.9 (own pct 75) · rv5_21 56.2 / c2c 72.6 · spread +55.7 / +39.3 · slope +19.9
   prior prints: 2, median realized/implied 0.99 · S-C: fails F5; F6 fails at 1.119 · S-A A1: F7 (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-10-30 ±$3.06 (straddle 3.06, cboe_chain 2026-10-23) · 1σ 30d ±$8.19 · ATR14 2.63 · GEX -, ZGL — (cboe_chain 2026-10-23)
E  Flags  borrow +0.4% (decile 0.4, IBKR 2026-10-23) · SI +23.0% / DTC 2.3 (FINRA 2026-09-30, pub 2026-10-13) · beta 3.98
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 19.4 contango, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -46.0% · ret63 -31.4% · 52w pos 0.00 · flow pct universe 100 / self 72
G  Structures (expiry 2026-11-20)
   IB              15P+ 26P- 26C- 41C+                      credit 5.82  max loss 918.00  BE 20.18–31.82  P(in) 0.58  cost 18.37  n=0  $0  [X1]
   IC              15P+ 18P- 33.5C- 41C+                    credit 0.92  max loss 658.00  BE 17.08–34.42  P(in) 0.79  cost 20.12  n=0  $0  [X1]
   SS              26P- 26C-                                credit 6.37  max loss —  BE 19.64–32.37  P(in) 0.62  cost 11.52  n=0  $0  [X1]
H  Ledger: sheet-1.0 exploration IB [X1] written
nulls: events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-11-04 None, screener 2026-11-05 postmarket, yfinance 2026-11-05 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
