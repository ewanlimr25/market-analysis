```
LRCX — 2026-11-20 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,137 · hot-chain 21/21 · ADV $2,974,733,968 · ATM spread +3.0% (tier 1)
B  Earnings 2027-01-26 unknown session 2027-01-27 [confirmed: finnhub 2027-01-26 = screener 2027-01-27 = yfinance ?] · ex-div 2026-12-02 · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 84.6 (own pct 82) · rv5_21 53.8 / c2c 97.9 · spread +30.8 / -13.3 · slope —
   prior prints: 2, median realized/implied 1.65 · S-C: fails F3; F6 fails at 0.846
D  Range  1σ box to 2026-11-27 ±$19.61 (straddle 19.61, daily_contract tier 1) · 1σ 30d ±$44.48 · ATR14 16.26 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.2% (decile 0.1, IBKR 2026-11-20) · SI — / DTC 2.2 (FINRA 2026-10-30, pub 2026-11-12) · beta 3.27
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 3 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -20.4% · ret63 -40.9% · 52w pos 0.16 · flow pct universe 1 / self 9
G  Structures (expiry 2026-12-18)
   IB              98P+ 185P- 185C- 270C+                    —  max loss —  BE —  P(touch) —  cost —  n=0  $—  (unpriced: 2026-12-18 98P)
   IC              98P+ 140P- 230C- 270C+                    —  max loss —  BE —  P(touch) —  cost —  n=0  $—  (unpriced: 2026-12-18 98P)
   SS              185P- 185C-                              credit 35.16  max loss —  BE 149.84–220.16  P(in) 0.65  cost 34.62  n=0  $0  (ALLOW_UNDEFINED=0: measurement only)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'LRCX': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'LRCX': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'LRCX': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
