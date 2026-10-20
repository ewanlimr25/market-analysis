# S-A daily — 2026-10-19 (S3)

Preflight: WARN — prices.parquet ends 2026-10-16, BEFORE the 2026-10-19 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-10-16, BEFORE the 2026-10-19 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-10-16, BEFORE the 2026-10-19 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (10)
| ticker | variant | structure | expiry | k | k_up | k_dn | credit_entry | credit_net_pct | risk_usd | contracts | entry_tier_max | cap_pass |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| KEY | A1 | IC | 2026-11-20T00:00:00.000 | 20.00 | 22.00 | 18.00 | 1.17 | +5.20% | 499.69 | 6 | 2 | yes |
| HAL | A1 | IC | 2026-10-23T00:00:00.000 | 33.00 | 38.00 | 28.00 | 1.71 | +4.91% | 328.84 | 1 | 1 | yes |
| STLD | A1 | SS | 2026-11-20T00:00:00.000 | 240.00 | — | — | 24.77 | +9.84% | 3,398.61 | 1 | 1 | no |
| KEY | A1 | SS | 2026-11-20T00:00:00.000 | 20.00 | — | — | 1.38 | +6.59% | 834.92 | 4 | 1 | yes |
| HAL | A1 | SS | 2026-10-23T00:00:00.000 | 33.00 | — | — | 1.77 | +5.14% | 595.16 | 1 | 1 | yes |
| KEY | A2 | IC | 2026-11-20T00:00:00.000 | 20.00 | 22.00 | 18.00 | 1.17 | +5.20% | 499.69 | 6 | 2 | yes |
| HAL | A2 | IC | 2026-10-23T00:00:00.000 | 33.00 | 38.00 | 28.00 | 1.71 | +4.91% | 328.84 | 1 | 1 | yes |
| STLD | A2 | SS | 2026-11-20T00:00:00.000 | 240.00 | — | — | 24.77 | +9.84% | 3,398.61 | 1 | 1 | no |
| KEY | A2 | SS | 2026-11-20T00:00:00.000 | 20.00 | — | — | 1.38 | +6.59% | 834.92 | 4 | 1 | yes |
| HAL | A2 | SS | 2026-10-23T00:00:00.000 | 33.00 | — | — | 1.77 | +5.14% | 595.16 | 1 | 1 | yes |

## Suppressed (70)
| ticker | variant | first_fail |
|---|---|---|
| AERO | A1 | F4 |
| AERO | A2 | F4 |
| AGNC | A1 | F2 |
| AGNC | A2 | F2 |
| ALLY | A1 | F6 |
| ALLY | A2 | F6 |
| AUB | A1 | F4 |
| AUB | A2 | F4 |
| BOKF | A1 | F4 |
| BOKF | A2 | F4 |
| CBSH | A1 | F5 |
| CBSH | A2 | F5 |
| CCBG | A1 | F3 |
| CCBG | A2 | F3 |
| CCK | A1 | F6 |
| CCK | A2 | F6 |
| DCOM | A1 | F3 |
| DCOM | A2 | F3 |
| EFX | A1 | F5 |
| EFX | A2 | F5 |
| FNB | A1 | F5 |
| FNB | A2 | F5 |
| GE | A1 | F3 |
| GE | A2 | F3 |
| GM | A1 | F3 |
| GM | A2 | F3 |
| GPC | A1 | F5 |
| GPC | A2 | F5 |
| HAS | A1 | F6 |
| HAS | A2 | F6 |
| HBCP | A1 | F3 |
| HBCP | A2 | F3 |
| MBWM | A1 | F3 |
| MBWM | A2 | F3 |
| MMM | A1 | F3 |
| MMM | A2 | F3 |
| MSCI | A1 | F5 |
| MSCI | A2 | F5 |
| NOC | A1 | F3 |
| NOC | A2 | F3 |
| PEBO | A1 | F3 |
| PEBO | A2 | F3 |
| RBB | A1 | F3 |
| RBB | A2 | F3 |
| RLI | A1 | F5 |
| RLI | A2 | F5 |
| RTX | A1 | F3 |
| RTX | A2 | F3 |
| SFBS | A1 | F4 |
| SFBS | A2 | F4 |
| SMBK | A1 | F3 |
| SMBK | A2 | F3 |
| SYF | A1 | F5 |
| SYF | A2 | F5 |
| UCB | A1 | F4 |
| UCB | A2 | F4 |
| VICR | A1 | F6 |
| VICR | A2 | F6 |
| VMI | A1 | F5 |
| VMI | A2 | F5 |
| WAL | A1 | F5 |
| WAL | A2 | F5 |
| WASH | A1 | F3 |
| WASH | A2 | F3 |
| WRB | A1 | F5 |
| WRB | A2 | F5 |
| WTFC | A1 | F5 |
| WTFC | A2 | F5 |
| ZION | A1 | F5 |
| ZION | A2 | F5 |

## Exploration book tonight (15; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| AGNC | SS | 2026-10-23T00:00:00.000 | 8.50 | 0.31 | +3.27% | 118.46 | F2 |
| ALLY | SS | 2026-11-20T00:00:00.000 | 37.00 | 3.02 | +7.66% | 451.47 | F6 |
| CCK | SS | 2026-11-20T00:00:00.000 | 115.00 | 8.37 | +6.53% | 1,264.40 | F6 |
| CCK | IC | 2026-11-20T00:00:00.000 | 115.00 | 7.26 | +5.31% | 774.11 | F6 |
| GM | SS | 2026-10-23T00:00:00.000 | 83.00 | 4.78 | +5.67% | 1,332.37 | F3 |
| GM | IC | 2026-10-23T00:00:00.000 | 83.00 | 4.69 | +5.50% | 730.84 | F3 |
| HAL | SS | 2026-10-23T00:00:00.000 | 33.00 | 1.77 | +5.14% | 595.16 | PASS |
| HAL | IC | 2026-10-23T00:00:00.000 | 33.00 | 1.71 | +4.91% | 328.84 | PASS |
| HAS | SS | 2026-11-20T00:00:00.000 | 97.50 | 9.49 | +9.13% | 1,384.16 | F6 |
| KEY | SS | 2026-11-20T00:00:00.000 | 20.00 | 1.38 | +6.59% | 208.73 | PASS |
| KEY | IC | 2026-11-20T00:00:00.000 | 20.00 | 1.17 | +5.20% | 83.28 | PASS |
| MMM | SS | 2026-10-23T00:00:00.000 | 162.50 | 9.27 | +5.60% | 2,383.58 | F3 |
| STLD | SS | 2026-11-20T00:00:00.000 | 240.00 | 24.77 | +9.84% | 3,398.61 | PASS |
| VICR | SS | 2026-11-20T00:00:00.000 | 190.00 | 47.42 | +23.35% | 6,989.74 | F6 |
| VICR | IC | 2026-11-20T00:00:00.000 | 190.00 | 40.61 | +18.52% | 3,939.06 | F6 |

## Graded today (6)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| CLF | A1 | SS | champion | -4.21% | -101.87 | 1 | no |
| FITB | A1 | SS | champion | -0.39% | -39.56 | 1 | no |
| CLF | A2 | SS | champion | -4.21% | -101.87 | 1 | no |
| FITB | A2 | SS | champion | -0.39% | -39.56 | 1 | no |
| CLF | A1 | SS | exploration | -4.21% | -50.94 | 1 | no |
| FITB | A1 | SS | exploration | -0.39% | -19.78 | 1 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 2 | 2 | +2.69% | 3.42 | 232.76 |
| sa-1.0 | champion | A1 | SS | 4 | 3 | +0.76% | 0.33 | 187.43 |
| sa-1.0 | champion | A2 | IC | 2 | 2 | +2.69% | 3.42 | 232.76 |
| sa-1.0 | champion | A2 | SS | 4 | 3 | +0.76% | 0.33 | 187.43 |
| sa-1.0 | exploration | A1 | IC | 10 | 8 | -0.56% | -0.65 | -1,053.14 |
| sa-1.0 | exploration | A1 | SS | 20 | 10 | +0.00% | 0.00 | -233.11 |

Ledger: emitted 10 (skipped 0), exploration 15 (skipped 0), graded 6; ledger open.

## S-B state
Gate (2026-10-19, from 2026-10-16 closes): SPY ON (VIX 19.99, VIX3M 20.5, X 19.99 vs median 15.29) · QQQ ON (VIX 19.99, VIX3M 20.5, X 27.13 vs median 21.174999999999997)

Next session (2026-10-20, from 2026-10-19 closes): SPY UNKNOWN:null input at 2026-10-19 · QQQ UNKNOWN:null input at 2026-10-19

CBOE refresh: ok through 2026-10-19; index-vol through 2026-10-19

Entry day: no.

### S-B positions tonight (0)
_none_

### S-B graded at expiry today (0)
_none due_

Open positions: QQQ-IC 2, QQQ-PS 3, SPY-IC 1, SPY-PS 2

### S-B forward ledger to date
| policy_id | role | sleeve | n | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|---|
| sb-1.0 | champion | QQQ-IC | 2 | — | — | 683.87 |
| sb-1.0 | champion | QQQ-PS | 2 | — | — | 413.48 |
| sb-1.0 | champion | SPY-IC | 1 | — | — | 198.73 |
| sb-1.0 | champion | SPY-PS | 2 | — | — | 283.48 |
| sb-1.0 | exploration | QQQ-IC | 2 | — | — | 683.87 |
| sb-1.0 | exploration | QQQ-PS | 3 | +5.84% | 28.91 | 625.67 |
| sb-1.0 | exploration | SPY-IC | 2 | — | — | 369.55 |
| sb-1.0 | exploration | SPY-PS | 3 | +5.23% | 56.31 | 407.80 |

S-B ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0; ledger open.


## S-C state
Entry day: no; ledger open.

### S-C graded at expiry (0)
_none due_

### S-C open book (S-B open: yes; the 40% budget binds only then)
| pair | positions | open_risk_usd | budget_usd | max_sector_positions |
|---|---|---|---|---|
| C1-SS | 5 | 6,688.69 | 8,000.00 | 3 |
| C1-IB | 5 | 3,962.47 | 4,000.00 | 3 |
| C2-SS | 5 | 7,496.64 | 8,000.00 | 3 |
| C2-IB | 4 | 3,571.32 | 4,000.00 | 3 |

### S-C forward ledger to date (entry-week series)
_ledger empty_

Progress to the read: graded entry-weeks 0 of 40 (C1-SS), 0 of 40 (C1-IB), 0 of 40 (C2-SS), 0 of 40 (C2-IB)

S-C ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0.


## Watch basket (wb-1.0, exploration, paper only)
Universe: 2019 names.
Borrow snapshot: 2026-10-19 (the session's own); fee known for 2012 names.
Bull counts: 0:763, 1:801, 2:361, 3:73, 4:19, 5:2, 6:0, 7:0, 8:0
Bear counts: 0:693, 1:759, 2:382, 3:139, 4:38, 5:8, 6:0, 7:0, 8:0

### LONG (52)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ABBV | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ABM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| ACA | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  |
| AMGN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| AVPT | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| AWI | 3 | 0 | no |  |  |  | x | x |  | x |  |  |  |  |  |  |  |  |  |  |  |  |  |
| BBY | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BIIB | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BOBS | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BRKB | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  | x | x |
| CAH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CHT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| CNK | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| COLM | 3 | 0 | no |  |  |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| COO | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CUBI | 3 | 0 | no |  |  |  | x | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DRH | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| E | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| EG | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FIZZ | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| FUL | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HLT | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| HMC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| HST | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| IDT | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| IEX | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| JOE | 3 | 0 | no |  |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| JOYY | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| LNG | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LXP | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| MAR | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| MCK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| MPC | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| MQ | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  |
| NHC | 5 | 0 | no | x | x |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| OCTV | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PRSU | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| REPX | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| RGA | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RL | 3 | 0 | yes |  | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| RNG | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| RS | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RSG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| SAFT | 3 | 0 | yes | x |  |  |  |  | x |  | x |  | ? | ? |  |  |  |  |  |  |  |  |  |
| SU | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  | x | x |
| TALO | 3 | 0 | no | x |  |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| TDY | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TW | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| TX | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| VTRS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WSM | 4 | 0 | no | x | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| ZION | 3 | 0 | no |  | x |  | x |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |

### SHORT (79)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AA | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| AAL | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  | x |  |  | x | x |  |  |  | x |
| AAOI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| AI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  |  |
| ALB | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  | x |
| ALGT | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| ALK | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  | x |  |  |  | x |  |  |  | x |
| AMSC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| ATHM | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| BDC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| BHVN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  |  | x |  |  |  |  |
| BIDU | 0 | 5 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | x | x |  |  |  | x |
| CC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CDE | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  | x |
| CGON | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| COIN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  | x | x |
| CPNG | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  | x | ? | x |  |  |  | x |
| CROX | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  |  |
| CVNA | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| CXW | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? | x |  |  |  |  |
| DUOL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| FLNG | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| FSK | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  |  |
| FSLY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| GBDC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| GLNG | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  | x | ? | x |  |  |  | x |
| GNTX | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | x |  |  |  |  |  |
| GOOGL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  | x | x |
| GPGI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| GSL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | ? |  |  | x | x | ? | x |  |  |  |  |
| HCC | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| HL | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  | x |
| HOOD | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| HTGC | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x | x |  |  |  |  |  |
| IMNM | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | ? |  | x |  |  | ? | x |  |  |  |  |
| INSM | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| IOT | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| KEP | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| LIF | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| LSCC | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| LYFT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  |  |  |  |  |  | x |
| MESO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| META | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| MOS | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| MRK | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| MSGS | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| MU | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| MWH | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| NRG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| NVAX | 0 | 5 | no |  |  |  |  |  |  | ? |  |  | x | x | x | x |  | ? | x |  |  |  |  |
| OMER | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | ? |  | x | x |  | ? | x |  |  |  |  |
| OSIS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| POWL | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| PRCT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| PTGX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| QURE | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  |  |
| QXO | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  |  | x |
| RH | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  |  |  |  |  |  | x |
| RIVN | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  | x |  |  |  | x |
| RKT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| SCCO | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| SIRI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  |  |
| SKHY | 0 | 3 | no |  |  | ? |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  | x | x |
| SLS | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  |  |  |
| SMCI | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| SNDX | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| STAG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  |  |
| STEP | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| STRD | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  | x |  | x | x |  |  |  |  |
| THO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| TRIN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| TSLX | 0 | 4 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  |  |
| UAL | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  | x |  |  | x | x |  |  |  | x |
| VICI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| VKTX | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| VSAT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| WHR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  |  |  | x |  | x |
| WLDN | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| XE | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  | x |  | x |

### VOL (0)
_none_

CONFLICT (logged only, never a basket, DESIGN/110 §3): 64.

Ledger: emitted 131 (skipped 0), graded 596; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
