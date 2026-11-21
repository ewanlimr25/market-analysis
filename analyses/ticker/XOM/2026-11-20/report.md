```
XOM — 2026-11-20 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 458 · hot-chain 21/21 · ADV $2,563,845,303 · ATM spread — (tier —)
B  Earnings 2027-01-28 unknown session 2027-01-29 [confirmed: finnhub 2027-01-28 = screener 2027-01-29 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium FAIR   iv30d 32.0 (own pct 90) · rv5_21 20.7 / c2c 33.0 · spread +11.3 / -1.0 · slope —
   prior prints: 3, median realized/implied 0.46 · S-C: fails F3; F6 passes at 0.320
D  Range  1σ box to 2026-11-27 ±$5.69 (straddle 5.69, daily_contract tier 1) · 1σ 30d ±$14.62 · ATR14 4.23 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.4% (decile 0.3, IBKR 2026-11-20) · SI — / DTC 3.5 (FINRA 2026-10-30, pub 2026-11-12) · beta -0.51
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -10.2% · ret63 -2.5% · 52w pos 0.62 · flow pct universe 98 / self 56
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'XOM': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), liquidity.atm_spread (no ATM pair within 2.5% of 159.41 at 2026-12-18 with 5+ lots on both legs), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'XOM': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'XOM': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
