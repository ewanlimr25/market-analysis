```
NBIS — 2026-11-20 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 2,098 · hot-chain 21/21 · ADV $4,020,354,438 · ATM spread +2.7% (tier 1)
B  Earnings 2027-02-10 unknown session 2027-02-11 [confirmed: finnhub 2027-02-10 = screener 2027-02-11 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 141.3 (own pct 90) · rv5_21 90.5 / c2c 148.1 · spread +50.8 / -6.8 · slope —
   prior prints: 3, median realized/implied 1.65 · S-C: fails F6
D  Range  1σ box to 2026-11-27 ±$14.07 (straddle 14.07, daily_contract tier 1) · 1σ 30d ±$32.86 · ATR14 16.85 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.4% (decile 0.4, IBKR 2026-11-20) · SI — / DTC 2.2 (FINRA 2026-10-30, pub 2026-11-12) · beta 4.00
          analyst: 0 changes last 10 sessions · Form 4: 6 buys / 10 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -48.9% · ret63 -61.4% · 52w pos 0.03 · flow pct universe 99 / self 67
G  Structures (expiry 2026-12-18)
   IB              23P+ 80P- 80C- 145C+                     credit 24.28  max loss 4,072.33  BE 55.72–104.28  P(in) 0.71  cost 30.20  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   IC              23P+ 50P- 115C- 145C+                    credit 4.26  max loss 2,573.62  BE 45.74–119.26  P(in) 0.89  cost 23.17  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   SS              80P- 80C-                                credit 25.24  max loss —  BE 54.76–105.24  P(in) 0.73  cost 21.31  n=0  $0  (ALLOW_UNDEFINED=0: measurement only)
H  Ledger: sheet-1.0 exploration IB [F6] written
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'NBIS': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), events.ex_div (screener next_dividend_date is not a date: 'NaT'), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'NBIS': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'NBIS': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
