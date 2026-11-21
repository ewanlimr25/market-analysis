```
BE — 2026-11-20 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,669 · hot-chain 21/21 · ADV $3,352,649,711 · ATM spread +0.6% (tier 1)
B  Earnings 2027-02-03 post session 2027-02-04 [confirmed: finnhub 2027-02-03 = screener 2027-02-04 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 120.3 (own pct 77) · rv5_21 85.8 / c2c 128.9 · spread +34.5 / -8.6 · slope —
   prior prints: 3, median realized/implied 0.65 · S-C: fails F3; F6 fails at 1.203
D  Range  1σ box to 2026-11-27 ±$21.03 (straddle 21.03, daily_contract tier 1) · 1σ 30d ±$48.95 · ATR14 21.13 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.2% (decile 0.1, IBKR 2026-11-20) · SI — / DTC 1.1 (FINRA 2026-10-30, pub 2026-11-12) · beta 4.19
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 5 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -34.6% · ret63 -30.2% · 52w pos 0.24 · flow pct universe 100 / self 93
G  Structures (expiry 2026-12-18)
   IB              45P+ 140P- 140C- 240C+                    —  max loss —  BE —  P(touch) —  cost —  n=0  $—  (unpriced: 2026-12-18 45P)
   IC              45P+ 95P- 190C- 240C+                     —  max loss —  BE —  P(touch) —  cost —  n=0  $—  (unpriced: 2026-12-18 45P)
   SS              140P- 140C-                              credit 37.69  max loss —  BE 102.31–177.69  P(in) 0.67  cost 7.53  n=0  $0  (ALLOW_UNDEFINED=0: measurement only)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'BE': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), events.ex_div (screener next_dividend_date is not a date: 'NaT'), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'BE': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'BE': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
