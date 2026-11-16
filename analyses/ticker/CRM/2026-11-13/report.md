```
CRM — 2026-11-13 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L6)   contracts 472 · hot-chain 21/21 · ADV $1,568,765,511 · ATM spread — (tier —)
B  Earnings 2026-12-01 post session 2026-12-02 [NOT CONFIRMED (X1 for 45d): finnhub 2026-12-01 = screener 2026-12-02 = yfinance 2026-12-02] · ex-div — · expiries 2026-11-20, 2026-11-27 · FOMC 2026-12-09
C  Premium FAIR   iv30d 54.5 (own pct 93) · rv5_21 30.7 / c2c 30.6 · spread +23.8 / +23.9 · slope -1.4
   prior prints: 2, median realized/implied 1.91 · S-C: fails F3; F6 passes at 0.545 · S-A A1: F3 (measurement only; S-A closed at execution) · X1: no premium structure on this sheet
D  Range  1σ box to 2026-11-20 ±$9.77 (straddle 9.77, cboe_chain 2026-11-13) · 1σ 30d ±$34.03 · ATR14 8.06 · GEX -, ZGL — (cboe_chain 2026-11-13)
E  Flags  borrow +0.3% (decile 0.3, IBKR 2026-11-13) · SI +3.3% / DTC 3.6 (FINRA 2026-10-30, pub 2026-11-12) · beta 0.37
          analyst: 0 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 19.3 contango, CHOP/REBOUND-THRUST
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -11.7% · ret63 +14.1% · 52w pos 0.58 · flow pct universe 99 / self 75
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: liquidity.atm_spread (no ATM pair within 2.5% of 217.795 at 2026-12-11 with 5+ lots on both legs), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2026-12-01 amc, screener 2026-12-02 postmarket, yfinance 2026-12-02 None), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
