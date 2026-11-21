```
RDDT — 2026-11-20 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 866 · hot-chain 21/21 · ADV $835,224,938 · ATM spread +4.6% (tier 1)
B  Earnings 2027-02-03 post session 2027-02-04 [confirmed: finnhub 2027-02-03 = screener 2027-02-04 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 73.9 (own pct 71) · rv5_21 54.7 / c2c 131.3 · spread +19.2 / -57.4 · slope —
   prior prints: 3, median realized/implied 1.84 · S-C: passes F1..F9
D  Range  1σ box to 2026-11-27 ±$7.10 (straddle 7.10, daily_contract tier 1) · 1σ 30d ±$18.02 · ATR14 7.33 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.3% (decile 0.3, IBKR 2026-11-20) · SI — / DTC 2.7 (FINRA 2026-10-30, pub 2026-11-12) · beta 2.08
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 7 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -43.2% · ret63 -44.1% · 52w pos 0.00 · flow pct universe 1 / self 7
G  Structures (expiry 2026-12-18)
   IB              50P+ 85P- 85C- 120C+                     credit 13.41  max loss 2,159.33  BE 71.59–98.41  P(in) 0.48  cost 28.53  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   IC              50P+ 70P- 100C- 120C+                    credit 3.56  max loss 1,643.90  BE 66.44–103.56  P(in) 0.63  cost 16.76  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   SS              85P- 85C-                                credit 13.78  max loss —  BE 71.22–98.78  P(in) 0.49  cost 19.79  n=0  $0  (ALLOW_UNDEFINED=0: measurement only)
H  Ledger: sheet-1.0 champion IB [PASS] written
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'RDDT': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), events.ex_div (screener next_dividend_date is not a date: 'NaT'), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'RDDT': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'RDDT': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
