```
IREN — 2026-10-09 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,009 · hot-chain 21/21 · ADV $1,582,510,277 · ATM spread +3.6% (tier 1)
B  Earnings 2026-11-04 unknown session 2026-11-05 [confirmed: finnhub 2026-11-04 = screener 2026-11-05 = yfinance 2026-11-05] · ex-div — · expiries 2026-10-16, 2026-10-23 · FOMC 2026-10-28
C  Premium FAIR   iv30d 73.3 (own pct 2) · rv5_21 54.8 / c2c 55.9 · spread +18.5 / +17.3 · slope +1.4
   prior prints: 2, median realized/implied 0.99 · S-C: fails F5; F6 passes at 0.733 · S-A A1: F7 (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-10-16 ±$2.53 (straddle 2.53, cboe_chain 2026-10-09) · 1σ 30d ±$7.39 · ATR14 2.63 · GEX -, ZGL — (cboe_chain 2026-10-09)
E  Flags  borrow +0.4% (decile 0.4, IBKR 2026-10-09) · SI +23.6% / DTC 2.3 (FINRA 2026-09-15, pub 2026-09-28) · beta 3.87
          analyst: 1 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 14.8 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -19.4% · ret63 -9.7% · 52w pos 0.13 · flow pct universe 1 / self 39
G  Structures (expiry 2026-11-06)
   IB              20P+ 35P- 35C- 49C+                      credit 5.31  max loss 969.00  BE 29.69–40.31  P(in) 0.40  cost 18.95  n=0  $0  [X1]
   IC              20P+ 29P- 42C- 49C+                      credit 1.20  max loss 780.00  BE 27.80–43.20  P(in) 0.56  cost 14.86  n=0  $0  [X1]
   SS              35P- 35C-                                credit 5.68  max loss —  BE 29.32–40.68  P(in) 0.43  cost 11.23  n=0  $0  [X1]
H  Ledger: sheet-1.0 exploration IB [X1] written
nulls: events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
