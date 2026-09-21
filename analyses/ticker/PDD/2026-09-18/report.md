```
PDD — 2026-09-18 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 325 · hot-chain 21/21 · ADV $579,727,466 · ATM spread — (tier —)
B  Earnings 2026-11-16 pre session 2026-11-16 [NOT CONFIRMED (X1 for 45d): finnhub 2026-11-16 = screener 2026-11-17 = yfinance 2026-11-18] · ex-div — · expiries 2026-09-25, 2026-10-02 · FOMC 2026-10-28
C  Premium FAIR   iv30d 30.5 (own pct 12) · rv5_21 23.4 / c2c 20.8 · spread +7.1 / +9.8 · slope -1.5
   prior prints: 4, median realized/implied 1.86 · S-C: fails F3; F6 passes at 0.305 · X1: no premium structure on this sheet
D  Range  1σ box to 2026-09-25 ±$2.84 (straddle 2.84, cboe_chain 2026-09-18) · 1σ 30d ±$6.91 · ATR14 2.03 · GEX -, ZGL — (cboe_chain 2026-09-18)
E  Flags  borrow +0.3% (decile 0.3, IBKR 2026-09-18) · SI +2.3% / DTC 4.3 (FINRA 2026-08-31, pub 2026-09-14) · beta 0.97
          analyst: 1 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 14.8 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -12.5% · ret63 -0.8% · 52w pos 0.10 · flow pct universe 1 / self 31
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: liquidity.atm_spread (no ATM pair within 2.5% of 78.9 at 2026-10-16 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-11-16 bmo, screener 2026-11-17 unknown, yfinance 2026-11-18 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
