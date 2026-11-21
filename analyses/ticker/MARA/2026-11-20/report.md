```
MARA — 2026-11-20 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L2)   contracts 542 · hot-chain 21/21 · ADV $272,746,953 · ATM spread +2.1% (tier 1)
B  Earnings 2027-02-24 pre session 2027-02-24 [NOT CONFIRMED (X1 for 45d): finnhub 2027-02-24 = screener 2027-02-25 = yfinance ?] · ex-div — · expiries 2026-11-27, 2026-12-04 · FOMC 2026-12-09
C  Premium FAIR   iv30d 126.0 (own pct 100) · rv5_21 85.4 / c2c 117.8 · spread +40.6 / +8.2 · slope —
   prior prints: 4, median realized/implied 0.52 · S-C: fails F2; F6 fails at 1.260 · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-27 ±$0.75 (straddle 0.75, daily_contract tier 1) · 1σ 30d ±$1.83 · ATR14 0.70 · GEX —, ZGL — (none 2026-11-20)
E  Flags  borrow +0.4% (decile 0.4, IBKR 2026-11-20) · SI — / DTC 3.1 (FINRA 2026-10-30, pub 2026-11-12) · beta 3.34
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 1 sells 30d · VIX 35.9 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -29.8% · ret63 -54.5% · 52w pos 0.00 · flow pct universe 2 / self 6
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: chain (cboe fetch failed: cboe_chain fetch failed for 'MARA': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), short_interest.short_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), earnings_dates.yfinance (yfinance calendar: Too Many Requests. Rate limited. Try after a while.), analyst (yfinance upgrades_downgrades: Too Many Requests. Rate limited. Try after a while.), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2027-02-24 bmo, screener 2027-02-25 unknown), events.ex_div (screener next_dividend_date is not a date: 'NaT'), premium.slope (no live chain to read ATM IV from), range.gex_total (cboe fetch failed: cboe_chain fetch failed for 'MARA': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), range.zero_gamma (cboe fetch failed: cboe_chain fetch failed for 'MARA': HTTP Error 403: Forbidden; yfinance option_chain: Too Many Requests. Rate limited. Try after a while.), flags.si.pct_float (fz is not on PATH; yfinance info shortPercentOfFloat: Too Many Requests. Rate limited. Try after a while.), flags.x5 (X5 cannot fire on a missing short float: it is unevaluated, not passed)
```
