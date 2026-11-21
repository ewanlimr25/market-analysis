```
MU — 2026-11-20 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 6,317 · hot-chain 21/21 · ADV $25,726,056,301 · ATM spread +4.2% (tier 1)
B  Earnings 2026-12-15 post session 2026-12-16 [NOT CONFIRMED (X1 for 45d): finnhub 2026-12-15 = screener 2026-12-17 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-11-30 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 95.0 (own pct 70) · rv5_21 60.0 / c2c 109.6 · spread +35.0 / -14.6 · slope —
   prior prints: 3, median realized/implied 0.58 · S-C: fails F3; F6 fails at 0.950 · S-A A1: F3 (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-27 ±$69.10 (straddle 69.10, daily_contract tier 1) · 1σ 30d ±$161.34 · ATR14 61.84 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.3% (decile 0.2, IBKR 2026-11-20) · SI — / DTC 1.0 (FINRA 2026-10-30, pub 2026-11-12) · beta 3.36
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -30.6% · ret63 -34.7% · 52w pos 0.38 · flow pct universe 0 / self 28
G  Structures (expiry 2026-12-18)
   IB              280P+ 590P- 590C- 900C+                  credit 121.46  max loss 18,853.61  BE 468.54–711.46  P(in) 0.67  cost 199.13  n=0  $0  [X1]
   IC              280P+ 440P- 750C- 900C+                  credit 22.93  max loss 13,706.59  BE 417.07–772.93  P(in) 0.85  cost 104.65  n=0  $0  [X1]
   SS              590P- 590C-                              credit 126.64  max loss —  BE 463.36–716.64  P(in) 0.70  cost 157.67  n=0  $0  [X1]
H  Ledger: sheet-1.0 exploration IB [X1] written
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'MU': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-12-15 amc, screener 2026-12-17 postmarket), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'MU': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'MU': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
