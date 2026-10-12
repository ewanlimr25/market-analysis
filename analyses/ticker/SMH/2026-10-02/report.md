```
SMH — 2026-10-02 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 2,306 · hot-chain 21/21 · ADV $3,769,767,338 · ATM spread — (tier —)
B  Earnings ?  session ? [NOT CONFIRMED (X1 for 45d): finnhub ? = screener ? = yfinance ?] · ex-div — · expiries 2026-10-09, 2026-10-12 · FOMC 2026-10-28
C  Premium RICH   iv30d 33.2 (own pct 11) · rv5_21 19.0 / c2c 29.8 · spread +14.2 / +3.4 · slope -1.8
   prior prints: 0, median realized/implied — · S-C: fails F1; F6 passes at 0.332
D  Range  1σ box to 2026-10-09 ±$17.35 (straddle 17.35, cboe_chain 2026-10-02) · 1σ 30d ±$60.02 · ATR14 15.30 · GEX +, ZGL 625.00 (cboe_chain 2026-10-02)
E  Flags  borrow +0.5% (decile 0.4, IBKR 2026-10-02) · SI — / DTC 1.9 (FINRA 2026-09-15, pub 2026-09-28) · beta 2.36
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 15.3 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 +14.6% · ret63 +4.4% · 52w pos 0.88 · flow pct universe 99 / self 58
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: earnings_events (no earnings_events rows for SMH), earnings_history (no earnings_history rows for SMH), short_interest.short_float (Short Float/Short Ratio/Short Interest absent from fz quote's fundamentals grid (known fz regression, see module docstring); yfinance info shortPercentOfFloat: shortPercentOfFloat absent), earnings_dates.finnhub (finnhub /calendar/earnings: no print scheduled on or after 2026-10-02), earnings_dates.yfinance (yfinance calendar: no Earnings Date in the calendar block), liquidity.atm_spread (no ATM pair within 2.5% of 630.6 at 2026-10-30 with 5+ lots on both legs), events.earnings.date (finnhub /calendar/earnings: no print scheduled on or after 2026-10-02), events.ex_div (screener next_dividend_date is not a date: 'NaT'), flags.si.pct_float (Short Float/Short Ratio/Short Interest absent from fz quote's fundamentals grid (known fz regression, see module docstring); yfinance info shortPercentOfFloat: shortPercentOfFloat absent), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
