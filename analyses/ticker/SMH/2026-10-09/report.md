```
SMH — 2026-10-09 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 1,913 · hot-chain 21/21 · ADV $3,836,383,497 · ATM spread — (tier —)
B  Earnings ?  session ? [NOT CONFIRMED (X1 for 45d): finnhub ? = screener ? = yfinance ?] · ex-div — · expiries 2026-10-16, 2026-10-19 · FOMC 2026-10-28
C  Premium RICH   iv30d 32.6 (own pct 8) · rv5_21 19.0 / c2c 30.3 · spread +13.6 / +2.4 · slope -3.0
   prior prints: 0, median realized/implied — · S-C: fails F1; F6 passes at 0.326
D  Range  1σ box to 2026-10-16 ±$20.80 (straddle 20.80, cboe_chain 2026-10-09) · 1σ 30d ±$56.43 · ATR14 14.93 · GEX -, ZGL — (cboe_chain 2026-10-09)
E  Flags  borrow +0.6% (decile 0.4, IBKR 2026-10-09) · SI — / DTC 1.9 (FINRA 2026-09-15, pub 2026-09-28) · beta 2.35
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 14.8 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 +7.7% · ret63 +3.0% · 52w pos 0.81 · flow pct universe 96 / self 48
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: earnings_events (no earnings_events rows for SMH), earnings_history (no earnings_history rows for SMH), short_interest.short_float (Short Float/Short Ratio/Short Interest absent from fz quote's fundamentals grid (known fz regression, see module docstring); yfinance info shortPercentOfFloat: shortPercentOfFloat absent), earnings_dates.finnhub (finnhub /calendar/earnings: no print scheduled on or after 2026-10-09), earnings_dates.yfinance (yfinance calendar: no Earnings Date in the calendar block), liquidity.atm_spread (no ATM pair within 2.5% of 603.33 at 2026-11-06 with 5+ lots on both legs), events.earnings.date (finnhub /calendar/earnings: no print scheduled on or after 2026-10-09), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes), flags.si.pct_float (Short Float/Short Ratio/Short Interest absent from fz quote's fundamentals grid (known fz regression, see module docstring); yfinance info shortPercentOfFloat: shortPercentOfFloat absent), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
