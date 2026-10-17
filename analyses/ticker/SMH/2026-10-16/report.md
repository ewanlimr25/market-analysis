```
SMH — 2026-10-16 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 2,074 · hot-chain 21/21 · ADV $4,541,749,467 · ATM spread +5.1% (tier 1)
B  Earnings ?  session ? [NOT CONFIRMED (X1 for 45d): finnhub ? = screener ? = yfinance ?] · ex-div — · expiries 2026-10-23, 2026-10-26 · FOMC 2026-10-28
C  Premium RICH   iv30d 38.5 (own pct 37) · rv5_21 21.1 / c2c 30.7 · spread +17.4 / +7.8 · slope -2.8
   prior prints: 0, median realized/implied — · S-C: fails F1; F6 passes at 0.385
D  Range  1σ box to 2026-10-23 ±$25.20 (straddle 25.20, cboe_chain 2026-10-16) · 1σ 30d ±$59.63 · ATR14 16.54 · GEX -, ZGL — (cboe_chain 2026-10-16)
E  Flags  borrow +0.6% (decile 0.4, IBKR 2026-10-16) · SI — / DTC 1.9 (FINRA 2026-09-30, pub 2026-10-13) · beta 2.38
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 20.0 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -3.7% · ret63 -3.4% · 52w pos 0.63 · flow pct universe 1 / self 34
G  Structures (expiry 2026-11-13)
   IB              425P+ 540P- 540C- 655C+                  credit 44.17  max loss 7,083.00  BE 495.83–584.17  P(in) 0.57  cost 148.60  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   IC              425P+ 485P- 597.5C- 655C+                credit 8.72  max loss 5,128.00  BE 476.28–606.22  P(in) 0.75  cost 154.44  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   SS              540P- 540C-                              credit 46.40  max loss —  BE 493.60–586.40  P(in) 0.59  cost 129.78  n=0  $0  (ALLOW_UNDEFINED=0: measurement only)
H  Ledger: sheet-1.0 exploration IB [F1] written
nulls: earnings_events (no earnings_events rows for SMH), earnings_history (no earnings_history rows for SMH), short_interest.short_float (Short Float/Short Ratio/Short Interest absent from fz quote's fundamentals grid (known fz regression, see module docstring); yfinance info shortPercentOfFloat: shortPercentOfFloat absent), earnings_dates.finnhub (finnhub /calendar/earnings: no print scheduled on or after 2026-10-16), earnings_dates.yfinance (yfinance calendar: no Earnings Date in the calendar block), events.earnings.date (finnhub /calendar/earnings: no print scheduled on or after 2026-10-16), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes), flags.si.pct_float (Short Float/Short Ratio/Short Interest absent from fz quote's fundamentals grid (known fz regression, see module docstring); yfinance info shortPercentOfFloat: shortPercentOfFloat absent), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
