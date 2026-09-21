```
KWEB — 2026-09-18 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L3)   contracts 274 · hot-chain 21/21 · ADV $473,568,636 · ATM spread +1.4% (tier 1)
B  Earnings ?  session ? [NOT CONFIRMED (X1 for 45d): finnhub ? = screener ? = yfinance ?] · ex-div — · expiries 2026-09-25, 2026-10-02 · FOMC 2026-10-28
C  Premium RICH   iv30d 28.6 (own pct 25) · rv5_21 12.0 / c2c 19.9 · spread +16.6 / +8.7 · slope -5.1
   prior prints: 0, median realized/implied — · S-C: fails F1; F6 fails at 0.286
D  Range  1σ box to 2026-09-25 ±$0.83 (straddle 0.83, cboe_chain 2026-09-18) · 1σ 30d ±$2.03 · ATR14 0.44 · GEX +, ZGL 27.00 (cboe_chain 2026-09-18)
E  Flags  borrow +0.6% (decile 0.4, IBKR 2026-09-18) · SI — / DTC 2.4 (FINRA 2026-08-31, pub 2026-09-14) · beta 1.11
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 14.8 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -8.8% · ret63 -1.6% · 52w pos 0.08 · flow pct universe 97 / self 64
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: earnings_events (no earnings_events rows for KWEB), earnings_history (no earnings_history rows for KWEB), short_interest.short_float (Short Float/Short Ratio/Short Interest absent from fz quote's fundamentals grid (known fz regression, see module docstring); yfinance info shortPercentOfFloat: shortPercentOfFloat absent), earnings_dates.finnhub (finnhub /calendar/earnings: no print scheduled on or after 2026-09-18), earnings_dates.yfinance (yfinance calendar: no Earnings Date in the calendar block), events.earnings.date (finnhub /calendar/earnings: no print scheduled on or after 2026-09-18), events.ex_div (screener next_dividend_date is not a date: 'NaT'), flags.si.pct_float (Short Float/Short Ratio/Short Interest absent from fz quote's fundamentals grid (known fz regression, see module docstring); yfinance info shortPercentOfFloat: shortPercentOfFloat absent), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
