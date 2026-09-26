```
BE — 2026-09-25 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,449 · hot-chain 21/21 · ADV $4,350,059,370 · ATM spread +5.0% (tier 1)
B  Earnings 2026-10-26 post session 2026-10-27 [confirmed: finnhub 2026-10-26 = screener 2026-10-27 = yfinance 2026-10-27] · ex-div — · expiries 2026-10-02, 2026-10-09 · FOMC 2026-10-28
C  Premium FAIR   iv30d 75.1 (own pct 1) · rv5_21 63.3 / c2c 73.9 · spread +11.8 / +1.2 · slope +0.3
   prior prints: 2, median realized/implied 1.13 · S-C: fails F3; F6 passes at 0.751
D  Range  1σ box to 2026-10-02 ±$23.92 (straddle 23.92, cboe_chain 2026-09-25) · 1σ 30d ±$62.13 · ATR14 19.20 · GEX +, ZGL 285.00 (cboe_chain 2026-09-25)
E  Flags  borrow +0.3% (decile 0.3, IBKR 2026-09-24) · SI +6.9% / DTC 1.6 (FINRA 2026-08-31, pub 2026-09-14) · beta 4.21
          analyst: 1 changes last 10 sessions · Form 4: 0 buys / 4 sells 30d · VIX 14.9 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 +32.3% · ret63 +14.6% · 52w pos 0.78 · flow pct universe 100 / self 71
G  Structures (expiry 2026-10-23)
   IB              170P+ 290P- 290C- 410C+                  credit 46.16  max loss 7,384.50  BE 243.84–336.15  P(in) 0.41  cost 167.00  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   IC              170P+ 230P- 350C- 410C+                  credit 9.18  max loss 5,082.00  BE 220.82–359.18  P(in) 0.58  cost 75.02  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   SS              290P- 290C-                              credit 48.45  max loss —  BE 241.55–338.45  P(in) 0.43  cost 141.46  n=0  $0  (ALLOW_UNDEFINED=0: measurement only)
H  Ledger: sheet-1.0 exploration IB [F3] written
nulls: events.ex_div (screener next_dividend_date is not a date: 'NaT')
```
