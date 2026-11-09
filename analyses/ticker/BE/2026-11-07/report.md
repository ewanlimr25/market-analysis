```
BE — 2026-11-07 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L1)   contracts — · hot-chain 21/21 · ADV $3,808,864,601 · ATM spread — (tier —)
B  Earnings 2027-02-03 post session 2027-02-04 [NOT CONFIRMED (X1 for 45d): finnhub 2027-02-03 = screener ? = yfinance 2026-10-22] · ex-div — · expiries 2026-11-20, 2026-11-27 · FOMC 2026-12-09
C  Premium CANNOT_MEASURE   iv30d — (own pct —) · rv5_21 74.5 / c2c 110.4 · spread — / — · slope +0.4
   prior prints: 3, median realized/implied 0.65 · S-C: fails F1; F6 fails at — · X1: no premium structure on this sheet
D  Range  1σ box to ? ±$— (straddle —, —) · 1σ 30d ±$— · ATR14 21.53 · GEX —, ZGL — (yfinance 2026-11-07)
E  Flags  borrow +0.3% (decile 0.2, IBKR 2026-11-06) · SI +6.2% / DTC 1.3 (FINRA 2026-10-15, pub 2026-10-28) · beta 4.32
          analyst: 2 changes last 10 sessions · Form 4: 0 buys / 2 sells 30d · VIX 25.6 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -36.5% · ret63 -17.8% · 52w pos 0.35 · flow pct universe — / self 60
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: screener (no screener export for 2026-11-07), universe_today (no screener export for 2026-11-07), contracts_today (no daily_contract partition for 2026-11-07), earnings_dates.screener (no screener row), liquidity.screener (no screener row for BE on 2026-11-07), liquidity.contracts (no daily_contract rows for BE on 2026-11-07), liquidity.atm_spread (no close), events.earnings.confirmed (the earnings sources disagree on the session: finnhub 2027-02-03 amc, yfinance 2026-10-22 None), events.ex_div (screener next_dividend_date is null), premium.iv30d (screener iv30d is null), premium.iv_pct_own (screener iv30d is null), range.straddle_front (no ATM call/put pair at 2026-11-20 carries a quote or a tier <= 2 print (the stored chain is yfinance 2026-11-07)), range.box_1s_front (no front straddle to measure), range.box_1s_21 (no screener row), range.gex_total (no strike on the chain carries positive gamma and open interest), range.zero_gamma (cumulative GEX never changes sign over the listed strikes), context.flow_pct_universe (no universe rows on the date), context.vol_pct_universe (no universe rows on the date)
```
