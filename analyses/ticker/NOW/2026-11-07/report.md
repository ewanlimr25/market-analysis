```
NOW — 2026-11-07 — sheet-1.0 — E $100,000
A  CANNOT_PRICE (L1)   contracts — · hot-chain 21/21 · ADV $2,534,719,753 · ATM spread — (tier —)
B  Earnings 2027-01-26 post session 2027-01-27 [confirmed: finnhub 2027-01-26 = screener ? = yfinance 2027-01-27] · ex-div — · expiries 2026-11-20, 2026-11-27 · FOMC 2026-12-09
C  Premium CANNOT_MEASURE   iv30d — (own pct —) · rv5_21 39.8 / c2c 115.1 · spread — / — · slope -1.5
   prior prints: 2, median realized/implied 1.27 · S-C: fails F1; F6 fails at —
D  Range  1σ box to ? ±$— (straddle —, —) · 1σ 30d ±$— · ATR14 7.32 · GEX —, ZGL — (yfinance 2026-11-07)
E  Flags  borrow +0.4% (decile 0.4, IBKR 2026-11-06) · SI +2.7% / DTC 2.6 (FINRA 2026-10-15, pub 2026-10-28) · beta 0.78
          analyst: 16 changes last 10 sessions · Form 4: 0 buys / 0 sells 30d · VIX 25.6 backwardation, PULLBACK
F  Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none.
   context: ret21 -27.0% · ret63 -20.0% · 52w pos 0.22 · flow pct universe — / self 37
G  Structures: none (CANNOT_PRICE)
H  Ledger: no row (CANNOT_PRICE or unpriced)
nulls: screener (no screener export for 2026-11-07), universe_today (no screener export for 2026-11-07), contracts_today (no daily_contract partition for 2026-11-07), earnings_dates.screener (no screener row), liquidity.screener (no screener row for NOW on 2026-11-07), liquidity.contracts (no daily_contract rows for NOW on 2026-11-07), liquidity.atm_spread (no close), events.ex_div (screener next_dividend_date is null), premium.iv30d (screener iv30d is null), premium.iv_pct_own (screener iv30d is null), range.straddle_front (no ATM call/put pair at 2026-11-20 carries a quote or a tier <= 2 print (the stored chain is yfinance 2026-11-07)), range.box_1s_front (no front straddle to measure), range.box_1s_21 (no screener row), range.gex_total (no strike on the chain carries positive gamma and open interest), range.zero_gamma (cumulative GEX never changes sign over the listed strikes), context.flow_pct_universe (no universe rows on the date), context.vol_pct_universe (no universe rows on the date)
```
