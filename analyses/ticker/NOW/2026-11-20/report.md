```
NOW — 2026-11-20 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,176 · hot-chain 21/21 · ADV $2,344,986,849 · ATM spread +1.8% (tier 1)
B  Earnings 2027-01-26 post session 2027-01-27 [confirmed: finnhub 2027-01-26 = screener 2027-01-27 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 62.0 (own pct 67) · rv5_21 40.1 / c2c 109.4 · spread +21.9 / -47.4 · slope —
   prior prints: 2, median realized/implied 1.27 · S-C: fails F3; F6 passes at 0.620
D  Range  1σ box to 2026-11-27 ±$5.77 (straddle 5.77, daily_contract tier 2) · 1σ 30d ±$15.55 · ATR14 5.96 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.4% (decile 0.3, IBKR 2026-11-20) · SI — / DTC 1.2 (FINRA 2026-10-30, pub 2026-11-12) · beta 0.79
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 3 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -44.2% · ret63 -31.6% · 52w pos 0.07 · flow pct universe 98 / self 56
G  Structures (expiry 2026-12-18)
   IB              55P+ 88P- 88C- 118C+                      —  max loss —  BE —  P(touch) —  cost —  n=0  $—  (unpriced: 2026-12-18 55P)
   IC              55P+ 72P- 102C- 118C+                     —  max loss —  BE —  P(touch) —  cost —  n=0  $—  (unpriced: 2026-12-18 55P)
   SS              88P- 88C-                                credit 11.69  max loss —  BE 76.31–99.69  P(in) 0.45  cost 7.64  n=0  $0  (ALLOW_UNDEFINED=0: measurement only)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'NOW': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), events.ex_div (screener next_dividend_date is not a date: 'NaT'), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'NOW': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'NOW': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
