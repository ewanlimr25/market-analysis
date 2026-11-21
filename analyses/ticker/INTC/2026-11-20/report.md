```
INTC — 2026-11-20 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,407 · hot-chain 21/21 · ADV $9,682,945,940 · ATM spread +2.6% (tier 1)
B  Earnings 2027-01-20 post session 2027-01-21 [NOT CONFIRMED (X1 for 45d): finnhub 2027-01-20 = screener 2027-01-28 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 89.3 (own pct 82) · rv5_21 60.3 / c2c 136.6 · spread +29.0 / -47.3 · slope —
   prior prints: 2, median realized/implied 1.58 · S-C: fails F3; F6 fails at 0.893 · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-27 ±$5.86 (straddle 5.86, daily_contract tier 1) · 1σ 30d ±$13.10 · ATR14 5.24 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.2% (decile 0.1, IBKR 2026-11-20) · SI — / DTC 1.2 (FINRA 2026-10-30, pub 2026-11-12) · beta 3.10
          analyst: 0 changes last 10 sessions · Form 4: 1 buys / 0 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -40.0% · ret63 -41.2% · 52w pos 0.17 · flow pct universe 0 / self 10
G  Structures (expiry 2026-12-18)
   IB              25P+ 50P- 50C- 77.5C+                    credit 10.10  max loss 1,740.44  BE 39.90–60.10  P(in) 0.55  cost 14.44  n=0  $0  [X1]
   IC              25P+ 38P- 65C- 77.5C+                    credit 1.74  max loss 1,125.93  BE 36.26–66.74  P(in) 0.74  cost 10.13  n=0  $0  [X1]
   SS              50P- 50C-                                credit 10.50  max loss —  BE 39.50–60.50  P(in) 0.57  cost 8.91  n=0  $0  [X1]
H  Ledger: sheet-1.0 exploration IB [X1] written
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'INTC': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2027-01-20 amc, screener 2027-01-28 unknown), events.ex_div (screener next_dividend_date is not a date: 'NaT'), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'INTC': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'INTC': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
