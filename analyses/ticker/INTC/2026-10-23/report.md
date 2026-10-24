```
INTC — 2026-10-23 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,581 · hot-chain 21/21 · ADV $10,165,399,130 · ATM spread +2.0% (tier 1)
B  Earnings 2027-01-20 post session 2027-01-21 [NOT CONFIRMED (X1 for 45d): finnhub 2027-01-20 = screener 2026-10-29 = yfinance 2026-10-29] · ex-div — · expiries 2026-10-30, 2026-11-06 · FOMC 2026-10-28
C  Premium FAIR   iv30d 66.1 (own pct 25) · rv5_21 40.2 / c2c 49.3 · spread +25.9 / +16.8 · slope -13.0
   prior prints: 1, median realized/implied 0.76 · S-C: fails F3; F6 passes at 0.661 · X1: no premium structure on this sheet
D  Range  1σ box to 2026-10-30 ±$8.62 (straddle 8.62, cboe_chain 2026-10-23) · 1σ 30d ±$16.45 · ATR14 5.61 · GEX -, ZGL — (cboe_chain 2026-10-23)
E  Flags  borrow +0.2% (decile 0.1, IBKR 2026-10-23) · SI +3.7% / DTC 1.4 (FINRA 2026-09-30, pub 2026-10-13) · beta 3.03
          analyst: 3 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 19.4 contango, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -31.7% · ret63 -5.1% · 52w pos 0.49 · flow pct universe 99 / self 60
G  Structures (expiry 2026-11-20)
   IB              55P+ 87P- 87C- 120C+                     credit 12.32  max loss 2,068.00  BE 74.68–99.32  P(in) 0.56  cost 20.12  n=0  $0  [X1]
   IC              55P+ 70P- 103C- 120C+                    credit 2.20  max loss 1,480.00  BE 67.80–105.20  P(in) 0.76  cost 10.19  n=0  $0  [X1]
   SS              87P- 87C-                                credit 12.95  max loss —  BE 74.05–99.95  P(in) 0.58  cost 15.90  n=0  $0  [X1]
H  Ledger: sheet-1.0 exploration IB [X1] written
nulls: events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2027-01-20 amc, screener 2026-10-29 postmarket, yfinance 2026-10-29 None), events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
