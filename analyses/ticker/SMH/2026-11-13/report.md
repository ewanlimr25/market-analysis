```
SMH — 2026-11-13 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 2,250 · hot-chain 21/21 · ADV $5,951,627,567 · ATM spread — (tier —)
B  Earnings ?  session ? [NOT CONFIRMED (X1 for 45d): finnhub ? = screener ? = yfinance ?] · ex-div — · expiries 2026-11-20, 2026-11-23 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 47.0 (own pct 59) · rv5_21 35.0 / c2c 64.9 · spread +12.0 / -17.9 · slope -5.2
   prior prints: 0, median realized/implied — · S-C: fails F1; F6 passes at 0.470
D  Range  1σ box to 2026-11-20 ±$30.27 (straddle 30.27, cboe_chain 2026-11-13) · 1σ 30d ±$65.59 · ATR14 24.22 · GEX -, ZGL — (cboe_chain 2026-11-13)
E  Flags  borrow +0.5% (decile 0.4, IBKR 2026-11-13) · SI — / DTC 1.3 (FINRA 2026-10-30, pub 2026-11-12) · beta 2.45
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 19.3 contango, CHOP/REBOUND-THRUST
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -12.9% · ret63 -18.1% · 52w pos 0.48 · flow pct universe 0 / self 6
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: earnings_events (no earnings_events rows for SMH), earnings_history (no earnings_history rows for SMH), short_interest.short_float (Short Float/Short Ratio/Short Interest absent from fz quote's fundamentals grid (known fz regression, see module docstring); yfinance info shortPercentOfFloat: shortPercentOfFloat absent), earnings_dates.finnhub (finnhub /calendar/earnings: no print scheduled on or after 2026-11-13), earnings_dates.yfinance (yfinance calendar: no Earnings Date in the calendar block), liquidity.atm_spread (no ATM pair within 2.5% of 486.77 at 2026-12-11 with 5+ lots on both legs), events.earnings.date (finnhub /calendar/earnings: no print scheduled on or after 2026-11-13), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes), flags.si.pct_float (Short Float/Short Ratio/Short Interest absent from fz quote's fundamentals grid (known fz regression, see module docstring); yfinance info shortPercentOfFloat: shortPercentOfFloat absent), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
