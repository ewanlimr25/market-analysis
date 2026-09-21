```
SMH — 2026-09-18 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,919 · hot-chain 21/21 · ADV $3,856,605,669 · ATM spread +1.6% (tier 1)
B  Earnings ?  session ? [NOT CONFIRMED (X1 for 45d): finnhub ? = screener ? = yfinance ?] · ex-div — · expiries 2026-09-25, 2026-09-28 · FOMC 2026-10-28
C  Premium FAIR   iv30d 30.8 (own pct 1) · rv5_21 22.2 / c2c 32.7 · spread +8.5 / -1.9 · slope -1.2
   prior prints: 0, median realized/implied — · S-C: fails F1; F6 passes at 0.308
D  Range  1σ box to 2026-09-25 ±$16.15 (straddle 16.15, cboe_chain 2026-09-18) · 1σ 30d ±$50.58 · ATR14 16.44 · GEX +, ZGL 615.00 (cboe_chain 2026-09-18)
E  Flags  borrow +0.5% (decile 0.4, IBKR 2026-09-18) · SI — / DTC 1.9 (FINRA 2026-08-31, pub 2026-09-14) · beta 2.36
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 14.8 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 +2.2% · ret63 -13.2% · 52w pos 0.72 · flow pct universe 1 / self 34
G  Structures (expiry 2026-10-16)
   IB              475P+ 575P- 575C- 670C+                  credit 37.80  max loss 6,219.50  BE 537.20–612.80  P(in) 0.40  cost 152.98  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   IC              475P+ 525P- 620C- 670C+                  credit 7.81  max loss 4,219.50  BE 517.20–627.80  P(in) 0.56  cost 91.66  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   SS              575P- 575C-                              credit 39.95  max loss —  BE 535.05–614.95  P(in) 0.42  cost 121.02  n=0  $0  (ALLOW_UNDEFINED=0: measurement only)
H  Ledger: sheet-1.0 exploration IB [F1] written
nulls: earnings_events (no earnings_events rows for SMH), earnings_history (no earnings_history rows for SMH), short_interest.short_float (Short Float/Short Ratio/Short Interest absent from fz quote's fundamentals grid (known fz regression, see module docstring); yfinance info shortPercentOfFloat: shortPercentOfFloat absent), earnings_dates.finnhub (finnhub /calendar/earnings: no print scheduled on or after 2026-09-18), earnings_dates.yfinance (yfinance calendar: no Earnings Date in the calendar block), events.earnings.date (finnhub /calendar/earnings: no print scheduled on or after 2026-09-18), events.ex_div (screener next_dividend_date is not a date: 'NaT'), flags.si.pct_float (Short Float/Short Ratio/Short Interest absent from fz quote's fundamentals grid (known fz regression, see module docstring); yfinance info shortPercentOfFloat: shortPercentOfFloat absent), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
