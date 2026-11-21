```
SHOP — 2026-11-20 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 751 · hot-chain 21/21 · ADV $1,243,442,519 · ATM spread — (tier —)
B  Earnings 2027-02-09 post session 2027-02-10 [confirmed: finnhub 2027-02-09 = screener 2027-02-10 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium RICH   iv30d 64.0 (own pct 66) · rv5_21 43.2 / c2c 59.4 · spread +20.8 / +4.6 · slope —
   prior prints: 3, median realized/implied 1.47 · S-C: fails F3; F6 passes at 0.640
D  Range  1σ box to 2026-11-27 ±$9.05 (straddle 9.05, daily_contract tier 2) · 1σ 30d ±$22.67 · ATR14 8.37 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.3% (decile 0.3, IBKR 2026-11-20) · SI — / DTC 2.6 (FINRA 2026-10-30, pub 2026-11-12) · beta 1.70
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -26.7% · ret63 -17.4% · 52w pos 0.34 · flow pct universe 99 / self 87
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'SHOP': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), liquidity.atm_spread (no ATM pair within 2.5% of 123.54 at 2026-12-18 with 5+ lots on both legs), events.ex_div (screener next_dividend_date is not a date: 'NaT'), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'SHOP': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'SHOP': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
