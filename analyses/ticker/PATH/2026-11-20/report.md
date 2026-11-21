```
PATH — 2026-11-20 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 327 · hot-chain 15/21 · ADV $295,996,636 · ATM spread — (tier —)
B  Earnings 2026-12-01 post session 2026-12-02 [NOT CONFIRMED (X1 for 45d): finnhub 2026-12-01 = screener 2026-12-03 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium FAIR   iv30d 85.9 (own pct 92) · rv5_21 42.4 / c2c 38.0 · spread +43.5 / +47.9 · slope —
   prior prints: 2, median realized/implied 0.69 · S-C: fails F5; F6 fails at 0.859 · S-A A1: F7 (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-27 ±$0.67 (straddle 0.67, daily_contract tier 2) · 1σ 30d ±$2.70 · ATR14 0.59 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.4% (decile 0.4, IBKR 2026-11-20) · SI — / DTC 3.8 (FINRA 2026-10-30, pub 2026-11-12) · beta 0.96
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 2 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -21.4% · ret63 -33.9% · 52w pos 0.17 · flow pct universe 95 / self 80
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'PATH': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), liquidity.atm_spread (no ATM pair within 2.5% of 10.95 at 2026-12-18 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-12-01 amc, screener 2026-12-03 postmarket), events.ex_div (screener next_dividend_date is not a date: 'NaT'), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'PATH': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'PATH': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
