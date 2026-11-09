```
NBIS — 2026-11-06 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,680 · hot-chain 21/21 · ADV $4,132,286,026 · ATM spread +4.8% (tier 1)
B  Earnings 2026-11-09 unknown session 2026-11-09 [NOT CONFIRMED (X1 for 45d): finnhub 2026-11-09 = screener 2026-11-12 = yfinance 2026-11-12] · ex-div — · expiries 2026-11-13, 2026-11-20 · FOMC 2026-12-09
C  Premium FAIR   iv30d 118.9 (own pct 78) · rv5_21 72.4 / c2c 112.5 · spread +46.5 / +6.4 · slope -28.8
   prior prints: 2, median realized/implied 2.25 · S-C: fails F3; F6 fails at 1.189 · S-A A1: F7 (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-13 ±$24.85 (straddle 24.85, cboe_chain 2026-11-06) · 1σ 30d ±$44.19 · ATR14 16.47 · GEX -, ZGL — (cboe_chain 2026-11-06)
E  Flags  borrow +0.6% (decile 0.4, IBKR 2026-11-06) · SI +21.4% / DTC 2.4 (FINRA 2026-10-15, pub 2026-10-28) · beta 3.79
          analyst: 1 changes last 10 sessions · Form 4: 11 buys / 2 sells 30d · VIX 25.6 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -41.1% · ret63 -29.7% · 52w pos 0.25 · flow pct universe 100 / self 90
G  Structures (expiry 2026-12-04)
   IB              60P+ 130P- 130C- 215C+                   credit 32.91  max loss 5,208.50  BE 97.08–162.91  P(in) 0.61  cost 225.98  n=0  $0  [X1]
   IC              60P+ 85P- 170C- 215C+                    credit 6.02  max loss 3,898.50  BE 78.98–176.01  P(in) 0.81  cost 141.30  n=0  $0  [X1]
   SS              130P- 130C-                              credit 34.85  max loss —  BE 95.15–164.85  P(in) 0.64  cost 188.18  n=0  $0  [X1]
H  Ledger: sheet-1.0 exploration IB [X1] written
nulls: events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-11-09 None, screener 2026-11-12 premarket, yfinance 2026-11-12 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
