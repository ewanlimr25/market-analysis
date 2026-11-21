```
ELF — 2026-11-20 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L4)   contracts 330 · hot-chain 1/21 · ADV $179,256,121 · ATM spread — (tier —)
B  Earnings 2027-02-02 unknown session 2027-02-03 [confirmed: finnhub 2027-02-02 = screener 2027-02-03 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium FAIR   iv30d 56.8 (own pct 39) · rv5_21 51.4 / c2c 44.5 · spread +5.4 / +12.3 · slope —
   prior prints: 3, median realized/implied 0.40 · S-C: fails F8; F6 passes at 0.568
D  Range  1σ box to 2026-11-27 ±$6.00 (straddle 6.00, daily_contract tier 2) · 1σ 30d ±$16.84 · ATR14 5.48 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.4% (decile 0.3, IBKR 2026-11-20) · SI — / DTC 3.4 (FINRA 2026-10-30, pub 2026-11-12) · beta 1.26
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 3 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -10.0% · ret63 -2.3% · 52w pos 0.74 · flow pct universe 6 / self 23
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'ELF': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), liquidity.atm_spread (no ATM pair within 2.5% of 103.395 at 2026-12-18 with 5+ lots on both legs), events.ex_div (screener next_dividend_date is not a date: 'NaT'), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'ELF': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'ELF': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
