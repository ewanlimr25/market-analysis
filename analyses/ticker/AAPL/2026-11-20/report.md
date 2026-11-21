```
AAPL — 2026-11-20 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,894 · hot-chain 21/21 · ADV $17,237,663,755 · ATM spread +2.5% (tier 1)
B  Earnings 2027-01-27 unknown session 2027-01-27 [NOT CONFIRMED (X1 for 45d): finnhub 2027-01-27 = screener 2027-02-04 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-11-30 · FOMC 2026-12-09
C  Premium FAIR   iv30d 29.3 (own pct 93) · rv5_21 20.0 / c2c 26.6 · spread +9.3 / +2.7 · slope —
   prior prints: 3, median realized/implied 1.01 · S-C: fails F3; F6 fails at 0.293 · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-27 ±$12.40 (straddle 12.40, daily_contract tier 1) · 1σ 30d ±$28.76 · ATR14 8.18 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.2% (decile 0.1, IBKR 2026-11-20) · SI — / DTC 3.4 (FINRA 2026-10-30, pub 2026-11-12) · beta 0.59
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 6 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -1.6% · ret63 +10.4% · 52w pos 0.84 · flow pct universe 0 / self 29
G  Structures (expiry 2026-12-18)
   IB              285P+ 340P- 340C- 400C+                  credit 22.30  max loss 3,769.61  BE 317.70–362.30  P(in) 0.71  cost 21.58  n=0  $0  [X1]
   IC              285P+ 315P- 370C- 400C+                  credit 4.57  max loss 2,542.93  BE 310.43–374.57  P(in) 0.87  cost 12.51  n=0  $0  [X1]
   SS              340P- 340C-                              credit 23.34  max loss —  BE 316.66–363.34  P(in) 0.74  cost 19.21  n=0  $0  [X1]
H  Ledger: sheet-1.0 exploration IB [X1] written
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'AAPL': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2027-01-27 None, screener 2027-02-04 unknown), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'AAPL': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'AAPL': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
