```
SMH — 2026-11-06 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 2,478 · hot-chain 21/21 · ADV $6,070,973,295 · ATM spread — (tier —)
B  Earnings ?  session ? [NOT CONFIRMED (X1 for 45d): finnhub ? = screener ? = yfinance ?] · ex-div — · expiries 2026-11-13, 2026-11-16 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 52.2 (own pct 71) · rv5_21 31.9 / c2c 59.1 · spread +20.3 / -6.9 · slope -5.6
   prior prints: 0, median realized/implied — · S-C: fails F1; F6 passes at 0.522
D  Range  1σ box to 2026-11-13 ±$32.65 (straddle 32.65, cboe_chain 2026-11-06) · 1σ 30d ±$69.52 · ATR14 23.08 · GEX -, ZGL — (cboe_chain 2026-11-06)
E  Flags  borrow +0.4% (decile 0.3, IBKR 2026-11-06) · SI — / DTC 1.7 (FINRA 2026-10-15, pub 2026-10-28) · beta 2.43
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 25.6 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -23.6% · ret63 -18.5% · 52w pos 0.42 · flow pct universe 99 / self 69
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: earnings_events (no earnings_events rows for SMH), earnings_history (no earnings_history rows for SMH), short_interest.short_float (Short Float/Short Ratio/Short Interest absent from fz quote's fundamentals grid (known fz regression, see module docstring); yfinance info shortPercentOfFloat: shortPercentOfFloat absent), earnings_dates.finnhub (finnhub /calendar/earnings: no print scheduled on or after 2026-11-06), earnings_dates.yfinance (yfinance calendar: no Earnings Date in the calendar block), liquidity.atm_spread (no ATM pair within 2.5% of 464.539 at 2026-12-04 with 5+ lots on both legs), events.earnings.date (finnhub /calendar/earnings: no print scheduled on or after 2026-11-06), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes), flags.si.pct_float (Short Float/Short Ratio/Short Interest absent from fz quote's fundamentals grid (known fz regression, see module docstring); yfinance info shortPercentOfFloat: shortPercentOfFloat absent), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
