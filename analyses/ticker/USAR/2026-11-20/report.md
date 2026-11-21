```
USAR — 2026-11-20 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L2)   contracts 393 · hot-chain 21/21 · ADV $149,863,629 · ATM spread — (tier —)
B  Earnings ?  session 2027-03-29 [NOT CONFIRMED (X1 for 45d): finnhub ? = screener 2027-03-29 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium FAIR   iv30d 118.4 (own pct 100) · rv5_21 88.2 / c2c 114.0 · spread +30.2 / +4.4 · slope —
   prior prints: 5, median realized/implied 1.12 · S-C: fails F2; F6 fails at 1.184 · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-27 ±$0.84 (straddle 0.84, daily_contract tier 1) · 1σ 30d ±$2.11 · ATR14 0.87 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +5.1% (decile 0.7, IBKR 2026-11-20) · SI — / DTC 4.8 (FINRA 2026-10-30, pub 2026-11-12) · beta 3.61
          analyst: 0 changes last 10 sessions · Form 4: 3 buys / 0 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -34.9% · ret63 -65.7% · 52w pos 0.00 · flow pct universe 6 / self 28
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'USAR': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.finnhub (finnhub /calendar/earnings: no print scheduled on or after 2026-11-20), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), liquidity.atm_spread (no ATM pair within 2.5% of 6.225 at 2026-12-18 with 5+ lots on both legs), events.earnings.date (finnhub /calendar/earnings: no print scheduled on or after 2026-11-20), events.ex_div (screener next_dividend_date is not a date: 'NaT'), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'USAR': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'USAR': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
