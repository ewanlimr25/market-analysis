```
CRM — 2026-11-20 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 767 · hot-chain 21/21 · ADV $1,566,944,702 · ATM spread — (tier —)
B  Earnings 2026-12-01 post session 2026-12-02 [NOT CONFIRMED (X1 for 45d): finnhub 2026-12-01 = screener 2026-12-02 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium FAIR   iv30d 67.3 (own pct 100) · rv5_21 33.4 / c2c 40.7 · spread +33.9 / +26.6 · slope —
   prior prints: 2, median realized/implied 1.91 · S-C: fails F3; F6 passes at 0.673 · S-A A1: F3 (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-27 ±$11.42 (straddle 11.42, daily_contract tier 1) · 1σ 30d ±$34.78 · ATR14 9.14 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.3% (decile 0.2, IBKR 2026-11-20) · SI — / DTC 3.6 (FINRA 2026-10-30, pub 2026-11-12) · beta 0.45
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -27.8% · ret63 -13.6% · 52w pos 0.28 · flow pct universe 2 / self 36
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'CRM': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), liquidity.atm_spread (no ATM pair within 2.5% of 180.265 at 2026-12-18 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-12-01 amc, screener 2026-12-02 postmarket), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'CRM': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'CRM': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
