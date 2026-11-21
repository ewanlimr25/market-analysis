```
IREN — 2026-11-20 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,409 · hot-chain 21/21 · ADV $1,553,245,232 · ATM spread +2.5% (tier 1)
B  Earnings 2027-02-03 unknown session 2027-02-04 [confirmed: finnhub 2027-02-03 = screener 2027-02-04 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium RICH   iv30d 148.5 (own pct 100) · rv5_21 95.6 / c2c 144.2 · spread +52.9 / +4.3 · slope —
   prior prints: 3, median realized/implied 0.71 · S-C: fails F6
D  Range  1σ box to 2026-11-27 ±$2.05 (straddle 2.05, daily_contract tier 1) · 1σ 30d ±$5.02 · ATR14 2.52 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.5% (decile 0.4, IBKR 2026-11-20) · SI — / DTC 1.7 (FINRA 2026-10-30, pub 2026-11-12) · beta 3.97
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -53.7% · ret63 -70.3% · 52w pos 0.00 · flow pct universe 95 / self 53
G  Structures (expiry 2026-12-18)
   IB              3P+ 12P- 12C- 21C+                       credit 3.65  max loss 534.93  BE 8.35–15.65  P(in) 0.70  cost 6.30  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   IC              3P+ 7P- 17C- 21C+                        credit 0.62  max loss 337.54  BE 6.38–17.62  P(in) 0.90  cost 4.49  n=1  $338
   SS              12P- 12C-                                credit 3.85  max loss —  BE 8.15–15.85  P(in) 0.73  cost 4.16  n=0  $0  (ALLOW_UNDEFINED=0: measurement only)
H  Ledger: sheet-1.0 exploration IB [F6] written
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'IREN': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), events.ex_div (screener next_dividend_date is not a date: 'NaT'), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'IREN': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'IREN': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
