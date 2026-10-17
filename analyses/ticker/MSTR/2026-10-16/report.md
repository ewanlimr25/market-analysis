```
MSTR — 2026-10-16 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,525 · hot-chain 21/21 · ADV $3,266,762,298 · ATM spread +3.2% (tier 1)
B  Earnings 2026-10-28 unknown session 2026-10-28 [NOT CONFIRMED (X1 for 45d): finnhub 2026-10-28 = screener 2026-10-29 = yfinance 2026-10-29] · ex-div — · expiries 2026-10-23, 2026-10-30 · FOMC 2026-10-28
C  Premium CHEAP   iv30d 72.8 (own pct 58) · rv5_21 47.5 / c2c 83.6 · spread +25.3 / -10.8 · slope +4.2
   prior prints: 2, median realized/implied 0.54 · S-C: fails F3; F6 passes at 0.728 · S-A A1: F8 (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-10-23 ±$11.15 (straddle 11.15, cboe_chain 2026-10-16) · 1σ 30d ±$28.54 · ATR14 9.73 · GEX -, ZGL — (cboe_chain 2026-10-16)
E  Flags  borrow +0.4% (decile 0.3, IBKR 2026-10-16) · SI +7.3% / DTC 1.2 (FINRA 2026-09-30, pub 2026-10-13) · beta 3.18
          analyst: 2 changes last 10 sessions · Form 4: 0 buys / 9 sells 30d · VIX 20.0 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 +3.5% · ret63 +39.9% · 52w pos 0.25 · flow pct universe 100 / self 93
G  Structures (expiry 2026-11-13)
   IB              80P+ 135P- 135C- 190C+                   credit 20.18  max loss 3,482.50  BE 114.83–155.18  P(in) 0.48  cost 63.63  n=0  $0  [X1]
   IC              80P+ 110P- 165C- 190C+                   credit 3.83  max loss 2,617.50  BE 106.17–168.82  P(in) 0.68  cost 28.59  n=0  $0  [X1]
   SS              135P- 135C-                              credit 21.60  max loss —  BE 113.40–156.60  P(in) 0.51  cost 53.86  n=0  $0  [X1]
H  Ledger: sheet-1.0 exploration IB [X1] written
nulls: events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-10-28 None, screener 2026-10-29 postmarket, yfinance 2026-10-29 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
