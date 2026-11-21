```
OKLO — 2026-11-20 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 570 · hot-chain 21/21 · ADV $252,254,939 · ATM spread +5.1% (tier 1)
B  Earnings 2027-03-15 unknown session 2027-03-16 [confirmed: finnhub 2027-03-15 = screener 2027-03-16 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 99.7 (own pct 95) · rv5_21 76.2 / c2c 113.2 · spread +23.5 / -13.5 · slope —
   prior prints: 4, median realized/implied 0.94 · S-C: fails F6
D  Range  1σ box to 2026-11-27 ±$2.38 (straddle 2.38, daily_contract tier 1) · 1σ 30d ±$5.66 · ATR14 2.20 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.4% (decile 0.3, IBKR 2026-11-20) · SI — / DTC 4.9 (FINRA 2026-10-30, pub 2026-11-12) · beta 3.60
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 22 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -26.5% · ret63 -50.0% · 52w pos 0.01 · flow pct universe 1 / self 10
G  Structures (expiry 2026-12-18)
   IB              12.5P+ 20P- 20C- 30C+                    credit 4.05  max loss 595.03  BE 15.95–24.05  P(in) 0.59  cost 13.25  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   IC              12.5P+ 15P- 25C- 30C+                    credit 0.74  max loss 426.11  BE 14.26–25.74  P(in) 0.77  cost 13.80  n=1  $426
   SS              20P- 20C-                                credit 4.42  max loss —  BE 15.58–24.42  P(in) 0.64  cost 7.86  n=0  $0  (ALLOW_UNDEFINED=0: measurement only)
H  Ledger: sheet-1.0 exploration IB [F6] written
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'OKLO': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), events.ex_div (screener next_dividend_date is not a date: 'NaT'), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'OKLO': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'OKLO': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
