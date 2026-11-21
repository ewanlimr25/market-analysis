```
SMR — 2026-11-20 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L2)   contracts 307 · hot-chain 20/21 · ADV $156,812,581 · ATM spread — (tier —)
B  Earnings 2027-02-24 post session 2027-02-25 [confirmed: finnhub 2027-02-24 = screener 2027-02-25 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium FAIR   iv30d 108.3 (own pct 97) · rv5_21 79.5 / c2c 107.2 · spread +28.8 / +1.1 · slope —
   prior prints: 2, median realized/implied 0.07 · S-C: fails F2; F6 fails at 1.083
D  Range  1σ box to 2026-11-27 ±$0.41 (straddle 0.41, daily_contract tier 1) · 1σ 30d ±$1.03 · ATR14 0.47 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.4% (decile 0.4, IBKR 2026-11-20) · SI — / DTC 3.6 (FINRA 2026-10-30, pub 2026-11-12) · beta 3.64
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -37.5% · ret63 -62.9% · 52w pos 0.00 · flow pct universe 5 / self 12
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'SMR': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), liquidity.atm_spread (no ATM pair within 2.5% of 3.33 at 2026-12-18 with 5+ lots on both legs), events.ex_div (screener next_dividend_date is not a date: 'NaT'), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'SMR': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'SMR': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
