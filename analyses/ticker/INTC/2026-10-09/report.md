```
INTC — 2026-10-09 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,943 · hot-chain 21/21 · ADV $12,453,244,702 · ATM spread +2.0% (tier 1)
B  Earnings 2026-10-21 post session 2026-10-22 [NOT CONFIRMED (X1 for 45d): finnhub 2026-10-21 = screener 2026-10-29 = yfinance 2026-10-29] · ex-div — · expiries 2026-10-16, 2026-10-19 · FOMC 2026-10-28
C  Premium FAIR   iv30d 64.8 (own pct 23) · rv5_21 39.7 / c2c 66.8 · spread +25.1 / -2.0 · slope +70.7
   prior prints: 1, median realized/implied 0.76 · S-C: fails F3; F6 passes at 0.648 · S-A A1: F3 (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-10-16 ±$6.22 (straddle 6.22, cboe_chain 2026-10-09) · 1σ 30d ±$19.44 · ATR14 5.90 · GEX -, ZGL — (cboe_chain 2026-10-09)
E  Flags  borrow +0.5% (decile 0.4, IBKR 2026-10-09) · SI +3.7% / DTC 1.8 (FINRA 2026-09-15, pub 2026-09-28) · beta 2.97
          analyst: 1 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 14.8 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 +4.4% · ret63 +1.5% · 52w pos 0.66 · flow pct universe 0 / self 12
G  Structures (expiry 2026-11-06)
   IB              65P+ 105P- 105C- 142C+                   credit 14.17  max loss 2,583.00  BE 90.83–119.17  P(in) 0.52  cost 18.37  n=0  $0  [X1]
   IC              65P+ 85P- 123C- 142C+                    credit 2.60  max loss 1,740.00  BE 82.40–125.60  P(in) 0.73  cost 11.36  n=0  $0  [X1]
   SS              105P- 105C-                              credit 15.00  max loss —  BE 90.00–120.00  P(in) 0.55  cost 12.98  n=0  $0  [X1]
H  Ledger: sheet-1.0 exploration IB [X1] written
nulls: events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-10-21 amc, screener 2026-10-29 postmarket, yfinance 2026-10-29 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
