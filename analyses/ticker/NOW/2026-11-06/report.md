```
NOW — 2026-11-06 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,119 · hot-chain 21/21 · ADV $2,534,719,753 · ATM spread +1.5% (tier 1)
B  Earnings 2027-01-26 post session 2027-01-27 [confirmed: finnhub 2027-01-26 = screener 2027-01-27 = yfinance 2027-01-27] · ex-div — · expiries 2026-11-13, 2026-11-20 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 50.2 (own pct 6) · rv5_21 39.8 / c2c 115.1 · spread +10.4 / -64.9 · slope -0.0
   prior prints: 2, median realized/implied 1.27 · S-C: fails F3; F6 passes at 0.502
D  Range  1σ box to 2026-11-13 ±$6.02 (straddle 6.02, cboe_chain 2026-11-06) · 1σ 30d ±$14.67 · ATR14 7.32 · GEX -, ZGL — (cboe_chain 2026-11-06)
E  Flags  borrow +0.4% (decile 0.4, IBKR 2026-11-06) · SI +2.7% / DTC 2.6 (FINRA 2026-10-15, pub 2026-10-28) · beta 0.78
          analyst: 17 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 25.6 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -27.0% · ret63 -20.0% · 52w pos 0.22 · flow pct universe 2 / self 37
G  Structures (expiry 2026-12-04)
   IB              80P+ 102P- 102C- 130C+                   credit 10.59  max loss 1,741.00  BE 91.41–112.59  P(in) 0.36  cost 12.53  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   IC              80P+ 90P- 116C- 130C+                    credit 2.19  max loss 1,181.00  BE 87.81–118.19  P(in) 0.49  cost 9.02  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   SS              102P- 102C-                              credit 11.32  max loss —  BE 90.67–113.33  P(in) 0.38  cost 8.60  n=0  $0  (ALLOW_UNDEFINED=0: measurement only)
H  Ledger: sheet-1.0 exploration IB [F3] written
nulls: events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
