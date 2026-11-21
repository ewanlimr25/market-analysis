```
PYPL — 2026-11-20 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 467 · hot-chain 21/21 · ADV $624,132,706 · ATM spread +9.9% (tier 1)
B  Earnings 2027-02-01 post session 2027-02-02 [confirmed: finnhub 2027-02-01 = screener 2027-02-02 = yfinance ?] · ex-div 2026-12-04 · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium RICH   iv30d 37.7 (own pct 66) · rv5_21 25.8 / c2c 34.3 · spread +11.9 / +3.4 · slope —
   prior prints: 3, median realized/implied 0.56 · S-C: fails F3; F6 passes at 0.377
D  Range  1σ box to 2026-11-27 ±$2.28 (straddle 2.28, daily_contract tier 2) · 1σ 30d ±$5.75 · ATR14 1.63 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.3% (decile 0.2, IBKR 2026-11-20) · SI — / DTC 2.2 (FINRA 2026-10-30, pub 2026-11-12) · beta 0.90
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 2 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -7.4% · ret63 -13.6% · 52w pos 0.58 · flow pct universe 9 / self 26
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'PYPL': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'PYPL': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'PYPL': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
