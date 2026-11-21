```
GOOG — 2026-11-20 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,534 · hot-chain 21/21 · ADV $8,386,524,248 · ATM spread +3.1% (tier 1)
B  Earnings 2027-02-02 post session 2027-02-03 [confirmed: finnhub 2027-02-02 = screener 2027-02-03 = yfinance ?] · ex-div 2026-12-07 · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 44.9 (own pct 100) · rv5_21 26.8 / c2c 51.1 · spread +18.1 / -6.2 · slope —
   prior prints: 3, median realized/implied 1.66 · S-C: fails F3; F6 passes at 0.449
D  Range  1σ box to 2026-11-27 ±$15.35 (straddle 15.35, daily_contract tier 1) · 1σ 30d ±$33.95 · ATR14 11.02 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.2% (decile 0.1, IBKR 2026-11-20) · SI — / DTC 2.2 (FINRA 2026-10-30, pub 2026-11-12) · beta 1.20
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -17.7% · ret63 -23.4% · 52w pos 0.01 · flow pct universe 0 / self 10
G  Structures (expiry 2026-12-18)
   IB              200P+ 265P- 265C- 330C+                  credit 25.42  max loss 3,958.36  BE 239.58–290.42  P(in) 0.67  cost 29.89  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   IC              200P+ 230P- 295C- 330C+                  credit 5.13  max loss 2,987.42  BE 224.87–300.13  P(in) 0.86  cost 20.14  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   SS              265P- 265C-                              credit 26.60  max loss —  BE 238.40–291.60  P(in) 0.69  cost 25.41  n=0  $0  (ALLOW_UNDEFINED=0: measurement only)
H  Ledger: sheet-1.0 exploration IB [F3] written
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'GOOG': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'GOOG': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'GOOG': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
