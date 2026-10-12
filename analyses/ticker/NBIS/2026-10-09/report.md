```
NBIS — 2026-10-09 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,061 · hot-chain 21/21 · ADV $3,684,720,895 · ATM spread +6.3% (tier 1)
B  Earnings 2026-11-09 unknown session 2026-11-10 [confirmed: finnhub 2026-11-09 = screener 2026-11-10 = yfinance 2026-11-10] · ex-div — · expiries 2026-10-16, 2026-10-23 · FOMC 2026-10-28
C  Premium RICH   iv30d 69.0 (own pct 1) · rv5_21 55.3 / c2c 64.4 · spread +13.6 / +4.5 · slope -0.1
   prior prints: 2, median realized/implied 2.25 · S-C: fails F3; F6 passes at 0.690
D  Range  1σ box to 2026-10-16 ±$15.57 (straddle 15.57, cboe_chain 2026-10-09) · 1σ 30d ±$43.70 · ATR14 15.88 · GEX -, ZGL — (cboe_chain 2026-10-09)
E  Flags  borrow +0.3% (decile 0.3, IBKR 2026-10-09) · SI +20.0% / DTC 3.6 (FINRA 2026-09-15, pub 2026-09-28) · beta 3.67
          analyst: 2 changes last 10 sessions · Form 4: 0 buys / 27 sells 30d · VIX 14.8 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -3.1% · ret63 +5.0% · 52w pos 0.65 · flow pct universe 98 / self 47
G  Structures (expiry 2026-11-06)
   IB              135P+ 220P- 220C- 305C+                  credit 31.39  max loss 5,361.00  BE 188.61–251.39  P(in) 0.32  cost 236.20  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   IC              135P+ 180P- 265C- 305C+                  credit 4.58  max loss 4,041.50  BE 175.41–269.58  P(in) 0.46  cost 176.92  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   SS              220P- 220C-                              credit 33.62  max loss —  BE 186.38–253.62  P(in) 0.34  cost 148.76  n=0  $0  (ALLOW_UNDEFINED=0: measurement only)
H  Ledger: sheet-1.0 exploration IB [F3] written
nulls: events.ex_div (screener next_dividend_date is not a date: 'NaT'), range.zero_gamma (cumulative GEX never changes sign over the listed strikes)
```
