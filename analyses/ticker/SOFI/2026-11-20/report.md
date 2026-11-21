```
SOFI — 2026-11-20 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 747 · hot-chain 21/21 · ADV $941,583,865 · ATM spread — (tier —)
B  Earnings 2027-01-28 post session 2027-01-29 [confirmed: finnhub 2027-01-28 = screener 2027-01-29 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium CHEAP   iv30d 64.2 (own pct 84) · rv5_21 45.5 / c2c 71.6 · spread +18.7 / -7.4 · slope —
   prior prints: 3, median realized/implied 1.16 · S-C: fails F8; F6 passes at 0.642
D  Range  1σ box to 2026-11-27 ±$0.99 (straddle 0.99, daily_contract tier 1) · 1σ 30d ±$2.29 · ATR14 0.81 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.3% (decile 0.2, IBKR 2026-11-20) · SI — / DTC 3.7 (FINRA 2026-10-30, pub 2026-11-12) · beta 2.22
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -15.5% · ret63 -31.6% · 52w pos 0.00 · flow pct universe 1 / self 2
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'SOFI': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), liquidity.atm_spread (no ATM pair within 2.5% of 12.445 at 2026-12-18 with 5+ lots on both legs), events.ex_div (screener next_dividend_date is not a date: 'NaT'), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'SOFI': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'SOFI': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
