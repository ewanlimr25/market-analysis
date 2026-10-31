```
NOW — 2026-10-30 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,442 · hot-chain 21/21 · ADV $2,311,033,991 · ATM spread +1.6% (tier 1)
B  Earnings 2027-01-26 post session 2027-01-27 [confirmed: finnhub 2027-01-26 = screener 2027-01-27 = yfinance 2027-01-27] · ex-div — · expiries 2026-11-06, 2026-11-13 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 49.3 (own pct 2) · rv5_21 38.1 / c2c 113.9 · spread +11.2 / -64.6 · slope -2.8
   prior prints: 1, median realized/implied 0.37 · S-C: fails F3; F6 passes at 0.493
D  Range  1σ box to 2026-11-06 ±$6.47 (straddle 6.47, cboe_chain 2026-10-30) · 1σ 30d ±$14.86 · ATR14 8.39 · GEX -, ZGL — (cboe_chain 2026-10-30)
E  Flags  borrow +0.3% (decile 0.3, IBKR 2026-10-30) · SI +2.7% / DTC 2.6 (FINRA 2026-10-15, pub 2026-10-28) · beta 0.74
          analyst: 19 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 19.4 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -23.7% · ret63 -7.9% · 52w pos 0.21 · flow pct universe 1 / self 13
G  Structures (expiry 2026-11-27)
   IB              75P+ 105P- 105C- 134C+                   credit 10.88  max loss 1,911.50  BE 94.11–115.89  P(in) 0.36  cost 9.90  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   IC              75P+ 90P- 120C- 134C+                    credit 1.92  max loss 1,308.50  BE 88.08–121.92  P(in) 0.53  cost 6.40  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   SS              105P- 105C-                              credit 11.40  max loss —  BE 93.60–116.40  P(in) 0.37  cost 7.14  n=0  $0  (ALLOW_UNDEFINED=0: measurement only)
H  Ledger: sheet-1.0 exploration IB [F3] written
nulls: events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
