```
HOOD — 2026-11-20 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 1,353 · hot-chain 21/21 · ADV $1,723,161,803 · ATM spread — (tier —)
B  Earnings 2027-02-08 post session 2027-02-09 [confirmed: finnhub 2027-02-08 = screener 2027-02-09 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium RICH   iv30d 85.9 (own pct 100) · rv5_21 51.3 / c2c 66.2 · spread +34.6 / +19.7 · slope —
   prior prints: 3, median realized/implied 0.44 · S-C: fails F3; F6 fails at 0.859
D  Range  1σ box to 2026-11-27 ±$6.06 (straddle 6.06, daily_contract tier 1) · 1σ 30d ±$15.23 · ATR14 5.23 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.3% (decile 0.3, IBKR 2026-11-20) · SI — / DTC 1.8 (FINRA 2026-10-30, pub 2026-11-12) · beta 2.78
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 11 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -35.6% · ret63 -40.0% · 52w pos 0.01 · flow pct universe 1 / self 13
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'HOOD': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), liquidity.atm_spread (no ATM pair within 2.5% of 61.86 at 2026-12-18 with 5+ lots on both legs), events.ex_div (screener next_dividend_date is not a date: 'NaT'), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'HOOD': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'HOOD': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
