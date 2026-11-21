```
BABA — 2026-11-20 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,023 · hot-chain 21/21 · ADV $1,210,681,535 · ATM spread +2.4% (tier 1)
B  Earnings 2026-11-23 unknown session 2026-11-23 [NOT CONFIRMED (X1 for 45d): finnhub 2026-11-23 = screener 2027-03-18 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium FAIR   iv30d 51.6 (own pct 99) · rv5_21 23.9 / c2c 43.6 · spread +27.7 / +8.0 · slope —
   prior prints: 4, median realized/implied 0.89 · S-C: fails F3; F6 passes at 0.516 · S-A A1: F3 (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-27 ±$4.92 (straddle 4.92, daily_contract tier 1) · 1σ 30d ±$11.99 · ATR14 3.63 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.2% (decile 0.1, IBKR 2026-11-20) · SI — / DTC 4.6 (FINRA 2026-10-30, pub 2026-11-12) · beta 0.92
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -20.4% · ret63 -31.6% · 52w pos 0.00 · flow pct universe 1 / self 28
G  Structures (expiry 2026-12-18)
   IB              60P+ 80P- 80C- 105C+                     credit 8.94  max loss 1,605.93  BE 71.06–88.94  P(in) 0.72  cost 11.73  n=0  $0  [X1]
   IC              60P+ 70P- 95C- 105C+                     credit 1.38  max loss 862.30  BE 68.62–96.38  P(in) 0.90  cost 11.58  n=0  $0  [X1]
   SS              80P- 80C-                                credit 9.32  max loss —  BE 70.68–89.32  P(in) 0.74  cost 7.26  n=0  $0  [X1]
H  Ledger: sheet-1.0 exploration IB [X1] written
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'BABA': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-11-23 None, screener 2027-03-18 unknown), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'BABA': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'BABA': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
