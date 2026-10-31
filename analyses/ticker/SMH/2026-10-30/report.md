```
SMH — 2026-10-30 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 2,368 · hot-chain 21/21 · ADV $5,237,050,490 · ATM spread +3.0% (tier 1)
B  Earnings ?  session ? [NOT CONFIRMED (X1 for 45d): finnhub ? = screener ? = yfinance ?] · ex-div — · expiries 2026-11-06, 2026-11-09 · FOMC 2026-12-09
C  Premium FAIR   iv30d 42.0 (own pct 46) · rv5_21 24.4 / c2c 42.8 · spread +17.6 / -0.8 · slope -4.7
   prior prints: 0, median realized/implied — · S-C: fails F1; F6 passes at 0.420
D  Range  1σ box to 2026-11-06 ±$28.10 (straddle 28.10, cboe_chain 2026-10-30) · 1σ 30d ±$62.96 · ATR14 19.25 · GEX -, ZGL 130.00 (cboe_chain 2026-10-30)
E  Flags  borrow +0.5% (decile 0.4, IBKR 2026-10-30) · SI — / DTC 1.7 (FINRA 2026-10-15, pub 2026-10-28) · beta 2.46
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 19.4 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -15.4% · ret63 -4.2% · 52w pos 0.58 · flow pct universe 1 / self 37
G  Structures (expiry 2026-11-27)
   IB              400P+ 525P- 525C- 645C+                  credit 46.82  max loss 7,817.50  BE 478.18–571.83  P(in) 0.61  cost 212.55  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   IC              400P+ 460P- 582.5C- 645C+                credit 9.05  max loss 5,345.00  BE 450.95–591.55  P(in) 0.81  cost 82.61  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   SS              525P- 525C-                              credit 49.10  max loss —  BE 475.90–574.10  P(in) 0.63  cost 182.34  n=0  $0  (ALLOW_UNDEFINED=0: measurement only)
H  Ledger: sheet-1.0 exploration IB [F1] written
nulls: earnings_events (no earnings_events rows for SMH), earnings_history (no earnings_history rows for SMH), short_interest.short_float (Short Float/Short Ratio/Short Interest absent from fz quote's fundamentals grid (known fz regression, see module docstring); yfinance info shortPercentOfFloat: shortPercentOfFloat absent), earnings_dates.finnhub (finnhub /calendar/earnings: no print scheduled on or after 2026-10-30), earnings_dates.yfinance (yfinance calendar: no Earnings Date in the calendar block), events.earnings.date (finnhub /calendar/earnings: no print scheduled on or after 2026-10-30), events.ex_div (screener next_dividend_date is not a date: 'NaT'), flags.si.pct_float (Short Float/Short Ratio/Short Interest absent from fz quote's fundamentals grid (known fz regression, see module docstring); yfinance info shortPercentOfFloat: shortPercentOfFloat absent), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
