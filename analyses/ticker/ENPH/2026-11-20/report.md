```
ENPH — 2026-11-20 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 464 · hot-chain 21/21 · ADV $235,725,726 · ATM spread — (tier —)
B  Earnings 2027-02-01 post session 2027-02-02 [confirmed: finnhub 2027-02-01 = screener 2027-02-02 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 83.9 (own pct 67) · rv5_21 62.9 / c2c 95.7 · spread +21.0 / -11.8 · slope —
   prior prints: 3, median realized/implied 0.73 · S-C: fails F6
D  Range  1σ box to 2026-11-27 ±$2.37 (straddle 2.37, daily_contract tier 2) · 1σ 30d ±$4.72 · ATR14 2.03 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.2% (decile 0.1, IBKR 2026-11-20) · SI — / DTC 3.4 (FINRA 2026-10-30, pub 2026-11-12) · beta 2.41
          analyst: 0 changes last 10 sessions · Form 4: 2 buys / 4 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -37.4% · ret63 -47.2% · 52w pos 0.00 · flow pct universe 3 / self 7
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'ENPH': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), liquidity.atm_spread (no ATM pair within 2.5% of 19.6095 at 2026-12-18 with 5+ lots on both legs), events.ex_div (screener next_dividend_date is not a date: 'NaT'), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'ENPH': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'ENPH': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
