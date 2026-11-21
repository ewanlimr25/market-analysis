```
FSLR — 2026-11-20 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 642 · hot-chain 21/21 · ADV $636,230,194 · ATM spread +6.7% (tier 1)
B  Earnings 2027-02-22 post session 2027-02-23 [confirmed: finnhub 2027-02-22 = screener 2027-02-23 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium RICH   iv30d 65.4 (own pct 60) · rv5_21 50.8 / c2c 59.1 · spread +14.6 / +6.3 · slope —
   prior prints: 3, median realized/implied 0.38 · S-C: passes F1..F9
D  Range  1σ box to 2026-11-27 ±$9.79 (straddle 9.79, daily_contract tier 2) · 1σ 30d ±$25.68 · ATR14 10.19 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.3% (decile 0.3, IBKR 2026-11-20) · SI — / DTC 5.3 (FINRA 2026-10-30, pub 2026-11-12) · beta 1.55
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -19.7% · ret63 -33.9% · 52w pos 0.00 · flow pct universe 1 / self 4
G  Structures (expiry 2026-12-18)
   IB              100P+ 135P- 135C- 185C+                  credit 19.02  max loss 3,098.12  BE 115.98–154.02  P(in) 0.68  cost 71.06  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   IC              100P+ 110P- 160C- 185C+                  credit 3.09  max loss 2,190.88  BE 106.91–163.09  P(in) 0.85  cost 82.25  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   SS              135P- 135C-                              credit 19.89  max loss —  BE 115.11–154.89  P(in) 0.70  cost 39.10  n=0  $0  (ALLOW_UNDEFINED=0: measurement only)
H  Ledger: sheet-1.0 champion IB [PASS] written
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'FSLR': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), events.ex_div (screener next_dividend_date is not a date: 'NaT'), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'FSLR': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'FSLR': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
