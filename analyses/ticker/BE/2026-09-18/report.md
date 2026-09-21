```
BE — 2026-09-18 — sheet-1.0 — E $100,000
A  CAN_PRICE   contracts 1,241 · hot-chain 21/21 · ADV $2,633,532,502 · ATM spread +6.2% (tier 1)
B  Earnings 2026-10-26 post session 2026-10-27 [confirmed: finnhub 2026-10-26 = screener 2026-10-27 = yfinance 2026-10-27] · ex-div — · expiries 2026-09-25, 2026-10-02 · FOMC 2026-10-28
C  Premium FAIR   iv30d 75.4 (own pct 1) · rv5_21 68.5 / c2c 71.5 · spread +6.9 / +3.9 · slope +0.8
   prior prints: 2, median realized/implied 1.13 · S-C: fails F3; F6 passes at 0.754
D  Range  1σ box to 2026-09-25 ±$21.30 (straddle 21.30, cboe_chain 2026-09-18) · 1σ 30d ±$57.43 · ATR14 18.96 · GEX +, ZGL 290.00 (cboe_chain 2026-09-18)
E  Flags  borrow +0.3% (decile 0.3, IBKR 2026-09-18) · SI +6.9% / DTC 1.6 (FINRA 2026-08-31, pub 2026-09-14) · beta 4.30
          analyst: 1 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 14.8 contango, CHOP
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 +28.6% · ret63 -19.2% · 52w pos 0.70 · flow pct universe 0 / self 4
G  Structures (expiry 2026-10-16)
   IB              155P+ 270P- 270C- 380C+                  credit 42.21  max loss 7,278.50  BE 227.78–312.21  P(in) 0.37  cost 116.77  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   IC              155P+ 210P- 320C- 380C+                  credit 7.89  max loss 5,211.00  BE 202.11–327.89  P(in) 0.55  cost 86.11  n=0  $0  (max loss exceeds 0.5% of E at one contract)
   SS              270P- 270C-                              credit 44.70  max loss —  BE 225.30–314.70  P(in) 0.39  cost 68.46  n=0  $0  (ALLOW_UNDEFINED=0: measurement only)
H  Ledger: sheet-1.0 exploration IB [F3] written
nulls: events.ex_div (screener next_dividend_date is not a date: 'NaT')
```
