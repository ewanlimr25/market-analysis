```
MSFT — 2026-11-20 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 2,644 · hot-chain 21/21 · ADV $15,690,495,835 · ATM spread +2.3% (tier 1)
B  Earnings 2027-01-26 unknown session 2027-01-27 [confirmed: finnhub 2027-01-26 = screener 2027-01-27 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-11-30 · FOMC 2026-12-09
C  Premium RICH   iv30d 41.1 (own pct 83) · rv5_21 26.0 / c2c 36.4 · spread +15.1 / +4.7 · slope —
   prior prints: 3, median realized/implied 0.71 · S-C: fails F3; F6 passes at 0.411
D  Range  1σ box to 2026-11-27 ±$24.80 (straddle 24.80, daily_contract tier 1) · 1σ 30d ±$56.97 · ATR14 16.41 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.2% (decile 0.1, IBKR 2026-11-20) · SI — / DTC 2.7 (FINRA 2026-10-30, pub 2026-11-12) · beta 1.00
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 3 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -7.0% · ret63 -0.6% · 52w pos 0.64 · flow pct universe 0 / self 13
G  Structures (expiry 2026-12-18)
   IB              375P+ 485P- 485C- 595C+                  credit 41.76  max loss 6,824.33  BE 443.24–526.76  P(in) 0.73  cost 40.74  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   IC              375P+ 430P- 540C- 595C+                  credit 8.16  max loss 4,683.84  BE 421.84–548.16  P(in) 0.91  cost 29.74  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   SS              485P- 485C-                              credit 43.77  max loss —  BE 441.23–528.77  P(in) 0.75  cost 31.00  n=0  $0  (ALLOW_UNDEFINED=0: measurement only)
H  Ledger: sheet-1.0 exploration IB [F3] written
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'MSFT': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'MSFT': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'MSFT': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
