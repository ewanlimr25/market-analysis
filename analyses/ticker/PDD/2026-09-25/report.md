```
PDD — 2026-09-25 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 311 · hot-chain 21/21 · ADV $549,068,906 · ATM spread — (tier —)
B  Earnings 2026-11-16 pre session 2026-11-16 [NOT CONFIRMED (X1 for 45d): finnhub 2026-11-16 = screener 2026-11-17 = yfinance 2026-11-18] · ex-div — · expiries 2026-10-02, 2026-10-09 · FOMC 2026-10-28
C  Premium FAIR   iv30d 28.9 (own pct 3) · rv5_21 17.6 / c2c 21.5 · spread +11.3 / +7.4 · slope +4.8
   prior prints: 4, median realized/implied 1.86 · S-C: fails F3; F6 fails at 0.289 · X1: no premium structure on this sheet
D  Range  1σ box to 2026-10-02 ±$2.40 (straddle 2.40, cboe_chain 2026-09-25) · 1σ 30d ±$6.42 · ATR14 1.88 · GEX -, ZGL — (cboe_chain 2026-09-25)
E  Flags  borrow +0.2% (decile 0.1, IBKR 2026-09-24) · SI +2.0% / DTC 4.3 (FINRA 2026-08-31, pub 2026-09-14) · beta 0.97
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 1 sells 30d · VIX 14.9 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -10.6% · ret63 +1.3% · 52w pos 0.08 · flow pct universe 3 / self 52
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: liquidity.atm_spread (no ATM pair within 2.5% of 77.57 at 2026-10-23 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-11-16 bmo, screener 2026-11-17 unknown, yfinance 2026-11-18 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
