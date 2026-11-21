```
SMH — 2026-11-20 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 3,011 · hot-chain 21/21 · ADV $6,095,913,306 · ATM spread +2.1% (tier 1)
B  Earnings ?  session ? [NOT CONFIRMED (X1 for 45d): finnhub ? = screener ? = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-11-30 · FOMC 2026-12-09
C  Premium FAIR   iv30d 69.3 (own pct 100) · rv5_21 41.7 / c2c 71.8 · spread +27.6 / -2.5 · slope —
   prior prints: 0, median realized/implied — · S-C: fails F1; F6 passes at 0.693
D  Range  1σ box to 2026-11-27 ±$37.34 (straddle 37.34, daily_contract tier 1) · 1σ 30d ±$79.30 · ATR14 26.13 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.4% (decile 0.3, IBKR 2026-11-20) · SI — / DTC 1.3 (FINRA 2026-10-30, pub 2026-11-12) · beta 2.47
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -23.6% · ret63 -26.8% · 52w pos 0.24 · flow pct universe 100 / self 93
G  Structures (expiry 2026-12-18)
   IB              245P+ 400P- 400C- 550C+                   —  max loss —  BE —  P(touch) —  cost —  n=0  $—  (unpriced: 2026-12-18 245P)
   IC              245P+ 325P- 475C- 550C+                   —  max loss —  BE —  P(touch) —  cost —  n=0  $—  (unpriced: 2026-12-18 245P)
   SS              400P- 400C-                              credit 61.74  max loss —  BE 338.26–461.74  P(in) 0.73  cost 39.95  n=0  $0  (ALLOW_UNDEFINED=0: measurement only)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: earnings_events (no earnings_events rows for SMH), earnings_history (no earnings_history rows for SMH), chain (cboe fetch failed: cboe_chain fetch failed for 'SMH': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.finnhub (finnhub /calendar/earnings: no print scheduled on or after 2026-11-20), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), events.earnings.date (finnhub /calendar/earnings: no print scheduled on or after 2026-11-20), events.ex_div (screener next_dividend_date is not a date: 'NaT'), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'SMH': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'SMH': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
