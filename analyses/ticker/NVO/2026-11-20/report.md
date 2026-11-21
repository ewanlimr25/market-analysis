```
NVO — 2026-11-20 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 436 · hot-chain 21/21 · ADV $540,088,057 · ATM spread +3.4% (tier 1)
B  Earnings 2027-02-01 post session 2027-02-02 [NOT CONFIRMED (X1 for 45d): finnhub 2027-02-01 = screener 2027-02-03 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium FAIR   iv30d 37.1 (own pct 52) · rv5_21 20.6 / c2c 34.6 · spread +16.5 / +2.5 · slope —
   prior prints: 3, median realized/implied 0.33 · S-C: fails F3; F6 passes at 0.371 · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-27 ±$1.26 (straddle 1.26, daily_contract tier 1) · 1σ 30d ±$4.02 · ATR14 1.13 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.3% (decile 0.3, IBKR 2026-11-20) · SI — / DTC 4.0 (FINRA 2026-10-30, pub 2026-11-12) · beta 0.97
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -4.1% · ret63 -19.4% · 52w pos 0.09 · flow pct universe 3 / self 23
G  Structures (expiry 2026-12-18)
   IB              30P+ 37.5P- 37.5C- 45C+                  credit 2.88  max loss 461.91  BE 34.62–40.38  P(in) 0.58  cost 7.96  n=0  $0  [X1]
   IC              30P+ 35P- 42.5C- 45C+                    credit 0.52  max loss 447.57  BE 34.48–43.02  P(in) 0.74  cost 7.71  n=0  $0  [X1]
   SS              37.5P- 37.5C-                            credit 3.06  max loss —  BE 34.44–40.56  P(in) 0.61  cost 4.50  n=0  $0  [X1]
H  Ledger: sheet-1.0 exploration IB [X1] written
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'NVO': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2027-02-01 amc, screener 2027-02-03 unknown), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'NVO': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'NVO': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
