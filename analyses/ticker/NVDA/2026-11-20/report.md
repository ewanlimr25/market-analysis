```
NVDA — 2026-11-20 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 3,495 · hot-chain 21/21 · ADV $48,161,636,320 · ATM spread +0.9% (tier 1)
B  Earnings 2027-02-23 post session 2027-02-24 [confirmed: finnhub 2027-02-23 = screener 2027-02-24 = yfinance ?] · ex-div 2026-12-02 · expiries 2026-11-27, 2026-11-30 · FOMC 2026-12-09
C  Premium RICH   iv30d 73.9 (own pct 100) · rv5_21 44.0 / c2c 66.0 · spread +29.9 / +7.9 · slope —
   prior prints: 3, median realized/implied 0.35 · S-C: fails F3; F6 passes at 0.739
D  Range  1σ box to 2026-11-27 ±$14.43 (straddle 14.43, daily_contract tier 1) · 1σ 30d ±$26.65 · ATR14 10.71 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.3% (decile 0.3, IBKR 2026-11-20) · SI — / DTC 2.8 (FINRA 2026-10-30, pub 2026-11-12) · beta 1.94
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -40.8% · ret63 -39.8% · 52w pos 0.01 · flow pct universe 0 / self 2
G  Structures (expiry 2026-12-18)
   IB              74P+ 126P- 126C- 177C+                   credit 20.78  max loss 3,121.79  BE 105.22–146.78  P(in) 0.75  cost 14.09  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   IC              74P+ 100P- 152C- 177C+                   credit 3.66  max loss 2,233.51  BE 96.34–155.66  P(in) 0.90  cost 10.77  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   SS              126P- 126C-                              credit 22.04  max loss —  BE 103.96–148.04  P(in) 0.78  cost 7.32  n=0  $0  (ALLOW_UNDEFINED=0: measurement only)
H  Ledger: sheet-1.0 exploration IB [F3] written
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'NVDA': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'NVDA': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'NVDA': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
