```
MSTR — 2026-11-20 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 1,826 · hot-chain 21/21 · ADV $2,222,641,412 · ATM spread — (tier —)
B  Earnings 2027-02-03 post session 2027-02-04 [confirmed: finnhub 2027-02-03 = screener 2027-02-04 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium RICH   iv30d 109.6 (own pct 100) · rv5_21 61.3 / c2c 68.8 · spread +48.3 / +40.8 · slope —
   prior prints: 3, median realized/implied 0.59 · S-C: fails F3; F6 fails at 1.096
D  Range  1σ box to 2026-11-27 ±$10.64 (straddle 10.64, daily_contract tier 1) · 1σ 30d ±$24.46 · ATR14 8.69 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.4% (decile 0.4, IBKR 2026-11-20) · SI — / DTC 1.4 (FINRA 2026-10-30, pub 2026-11-12) · beta 3.01
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 6 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -46.6% · ret63 -36.6% · 52w pos 0.00 · flow pct universe 0 / self 7
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'MSTR': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), liquidity.atm_spread (no ATM pair within 2.5% of 77.84 at 2026-12-18 with 5+ lots on both legs), events.ex_div (screener next_dividend_date is not a date: 'NaT'), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'MSTR': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'MSTR': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
