```
SNOW — 2026-11-20 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 865 · hot-chain 21/21 · ADV $1,270,822,372 · ATM spread +0.9% (tier 1)
B  Earnings 2026-12-01 post session 2026-12-02 [NOT CONFIRMED (X1 for 45d): finnhub 2026-12-01 = screener 2026-12-02 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium FAIR   iv30d 93.2 (own pct 100) · rv5_21 44.1 / c2c 57.3 · spread +49.1 / +35.9 · slope —
   prior prints: 2, median realized/implied 2.22 · S-C: fails F3; F6 fails at 0.932 · S-A A1: F3 (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-27 ±$21.06 (straddle 21.06, daily_contract tier 1) · 1σ 30d ±$67.94 · ATR14 16.69 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.2% (decile 0.1, IBKR 2026-11-20) · SI — / DTC 4.1 (FINRA 2026-10-30, pub 2026-11-12) · beta 1.47
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 37 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -18.8% · ret63 -21.1% · 52w pos 0.51 · flow pct universe 95 / self 61
G  Structures (expiry 2026-12-18)
   IB              120P+ 250P- 250C- 390C+                   —  max loss —  BE —  P(touch) —  cost —  n=0  $—  [X1]  (unpriced: 2026-12-18 250C)
   IC              120P+ 190P- 320C- 390C+                   —  max loss —  BE —  P(touch) —  cost —  n=0  $—  [X1]  (unpriced: 2026-12-18 390C)
   SS              250P- 250C-                               —  max loss —  BE —  P(touch) —  cost —  n=0  $—  [X1]  (unpriced: 2026-12-18 250C)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'SNOW': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-12-01 amc, screener 2026-12-02 postmarket), events.ex_div (screener next_dividend_date is not a date: 'NaT'), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'SNOW': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'SNOW': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
