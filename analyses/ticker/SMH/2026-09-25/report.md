```
SMH — 2026-09-25 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 1,952 · hot-chain 21/21 · ADV $3,663,832,920 · ATM spread — (tier —)
B  Earnings ?  session ? [NOT CONFIRMED (X1 for 45d): finnhub ? = screener ? = yfinance ?] · ex-div — · expiries 2026-10-02, 2026-10-05 · FOMC 2026-10-28
C  Premium FAIR   iv30d 32.7 (own pct 7) · rv5_21 19.2 / c2c 34.2 · spread +13.4 / -1.6 · slope -2.4
   prior prints: 0, median realized/implied — · S-C: fails F1; F6 passes at 0.327
D  Range  1σ box to 2026-10-02 ±$20.18 (straddle 20.18, cboe_chain 2026-09-25) · 1σ 30d ±$56.81 · ATR14 16.09 · GEX +, ZGL 615.00 (cboe_chain 2026-09-25)
E  Flags  borrow +0.6% (decile 0.4, IBKR 2026-09-24) · SI — / DTC 1.9 (FINRA 2026-08-31, pub 2026-09-14) · beta 2.37
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 14.9 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 +9.1% · ret63 -0.8% · 52w pos 0.82 · flow pct universe 99 / self 45
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: earnings_events (no earnings_events rows for SMH), earnings_history (no earnings_history rows for SMH), short_interest.short_float (Short Float/Short Ratio/Short Interest absent from fz quote's fundamentals grid (known fz regression, see module docstring); yfinance info shortPercentOfFloat: shortPercentOfFloat absent), earnings_dates.finnhub (finnhub /calendar/earnings: no print scheduled on or after 2026-09-25), earnings_dates.yfinance (yfinance calendar: no Earnings Date in the calendar block), liquidity.atm_spread (no ATM pair within 2.5% of 606.56 at 2026-10-23 with 5+ lots on both legs), events.earnings.date (finnhub /calendar/earnings: no print scheduled on or after 2026-09-25), events.ex_div (screener next_dividend_date is not a date: 'NaT'), flags.si.pct_float (Short Float/Short Ratio/Short Interest absent from fz quote's fundamentals grid (known fz regression, see module docstring); yfinance info shortPercentOfFloat: shortPercentOfFloat absent), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
