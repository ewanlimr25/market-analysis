```
SMH — 2026-10-23 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,869 · hot-chain 21/21 · ADV $4,792,157,324 · ATM spread +2.9% (tier 1)
B  Earnings ?  session ? [NOT CONFIRMED (X1 for 45d): finnhub ? = screener ? = yfinance ?] · ex-div — · expiries 2026-10-30, 2026-11-02 · FOMC 2026-10-28
C  Premium RICH   iv30d 40.9 (own pct 44) · rv5_21 22.8 / c2c 33.1 · spread +18.1 / +7.8 · slope -5.1
   prior prints: 0, median realized/implied — · S-C: fails F1; F6 passes at 0.409
D  Range  1σ box to 2026-10-30 ±$26.12 (straddle 26.12, cboe_chain 2026-10-23) · 1σ 30d ±$61.94 · ATR14 17.47 · GEX -, ZGL — (cboe_chain 2026-10-23)
E  Flags  borrow +0.5% (decile 0.4, IBKR 2026-10-23) · SI — / DTC 1.9 (FINRA 2026-09-30, pub 2026-10-13) · beta 2.40
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 19.4 contango, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -12.2% · ret63 -3.9% · 52w pos 0.59 · flow pct universe 0 / self 15
G  Structures (expiry 2026-11-20)
   IB              410P+ 527.5P- 527.5C- 650C+              credit 45.79  max loss 7,671.00  BE 481.71–573.29  P(in) 0.59  cost 198.24  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   IC              410P+ 470P- 590C- 650C+                  credit 8.99  max loss 5,101.00  BE 461.01–598.99  P(in) 0.79  cost 87.28  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   SS              527.5P- 527.5C-                          credit 47.90  max loss —  BE 479.60–575.40  P(in) 0.61  cost 164.82  n=0  $0  (ALLOW_UNDEFINED=0: measurement only)
H  Ledger: sheet-1.0 exploration IB [F1] written
nulls: earnings_events (no earnings_events rows for SMH), earnings_history (no earnings_history rows for SMH), short_interest.short_float (Short Float/Short Ratio/Short Interest absent from fz quote's fundamentals grid (known fz regression, see module docstring); yfinance info shortPercentOfFloat: shortPercentOfFloat absent), earnings_dates.finnhub (finnhub /calendar/earnings: no print scheduled on or after 2026-10-23), earnings_dates.yfinance (yfinance calendar: no Earnings Date in the calendar block), events.earnings.date (finnhub /calendar/earnings: no print scheduled on or after 2026-10-23), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes), flags.si.pct_float (Short Float/Short Ratio/Short Interest absent from fz quote's fundamentals grid (known fz regression, see module docstring); yfinance info shortPercentOfFloat: shortPercentOfFloat absent), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
