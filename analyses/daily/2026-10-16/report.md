# S-A daily — 2026-10-16 (S3)

Preflight: WARN — prices.parquet ends 2026-10-09, BEFORE the 2026-10-16 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-10-09, BEFORE the 2026-10-16 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-10-09, BEFORE the 2026-10-16 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (4)
| ticker | variant | structure | expiry | k | k_up | k_dn | credit_entry | credit_net_pct | risk_usd | contracts | entry_tier_max | cap_pass |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CLF | A1 | SS | 2026-10-23T00:00:00.000 | 12.00 | — | — | 1.53 | +12.01% | 760.50 | 2 | 1 | yes |
| FITB | A1 | SS | 2026-11-20T00:00:00.000 | 50.00 | — | — | 3.55 | +6.86% | 924.89 | 2 | 1 | yes |
| CLF | A2 | SS | 2026-10-23T00:00:00.000 | 12.00 | — | — | 1.53 | +12.01% | 760.50 | 2 | 1 | yes |
| FITB | A2 | SS | 2026-11-20T00:00:00.000 | 50.00 | — | — | 3.55 | +6.86% | 924.89 | 2 | 1 | yes |

## Suppressed (2)
| ticker | variant | first_fail |
|---|---|---|
| DX | A1 | F5 |
| DX | A2 | F5 |

## Exploration book tonight (2; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| CLF | SS | 2026-10-23T00:00:00.000 | 12.00 | 1.53 | +12.01% | 380.25 | PASS |
| FITB | SS | 2026-11-20T00:00:00.000 | 50.00 | 3.55 | +6.86% | 462.44 | PASS |

## Graded today (4)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| AA | A1 | SS | exploration | -2.28% | -91.96 | 2 | no |
| CFG | A1 | SS | exploration | -0.64% | -40.36 | 1 | no |
| CFG | A1 | IC | exploration | -1.12% | -71.22 | 2 | no |
| IBKR | A1 | SS | exploration | +0.67% | 57.84 | 1 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 2 | 2 | +2.69% | 3.42 | 232.76 |
| sa-1.0 | champion | A1 | SS | 2 | 2 | +3.83% | 3.98 | 328.86 |
| sa-1.0 | champion | A2 | IC | 2 | 2 | +2.69% | 3.42 | 232.76 |
| sa-1.0 | champion | A2 | SS | 2 | 2 | +3.83% | 3.98 | 328.86 |
| sa-1.0 | exploration | A1 | IC | 10 | 8 | -0.56% | -0.65 | -1,053.14 |
| sa-1.0 | exploration | A1 | SS | 18 | 9 | +0.26% | 0.48 | -162.39 |

Ledger: emitted 4 (skipped 0), exploration 2 (skipped 0), graded 4; ledger open.

## S-B state
Gate (2026-10-16, from 2026-10-15 closes): SPY ON (VIX 16.46, VIX3M 18.49, X 16.46 vs median 15.29) · QQQ ON (VIX 16.46, VIX3M 18.49, X 22.89 vs median 21.145)

Next session (2026-10-19, from 2026-10-16 closes): SPY ON (VIX 19.99, VIX3M 20.5, X 19.99 vs median 15.29) · QQQ ON (VIX 19.99, VIX3M 20.5, X 27.13 vs median 21.174999999999997)

CBOE refresh: ok through 2026-10-16; index-vol through 2026-10-16

Entry day: yes.

### S-B positions tonight (3)
| underlying | structure | expiry | k_p1 | k_p2 | k_c1 | k_c2 | credit_entry | max_loss_usd | contracts | entry_tier_max |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY | PS | 2026-11-06 | 727.00 | 690.00 | — | — | 1.69 | 3,531.15 | 1 | 1 |
| QQQ | PS | 2026-11-06 | 665.00 | 615.00 | — | — | 3.14 | 4,686.22 | 1 | 1 |
| QQQ | IC | 2026-11-06 | 665.00 | 615.00 | 756.00 | 800.00 | 4.44 | 4,556.31 | 1 | 1 |

### S-B skipped (1)
| underlying | structure | reason |
|---|---|---|
| SPY | IC | no_tier1_c2 |

### S-B exploration book tonight (3; one contract per sleeve, gate ignored, gate verdict recorded)
| underlying | structure | expiry | k_p1 | k_p2 | k_c1 | k_c2 | credit_entry | max_loss_usd | gate_verdict |
|---|---|---|---|---|---|---|---|---|---|
| SPY | PS | 2026-11-06 | 727.00 | 690.00 | — | — | 1.69 | 3,531.15 | ON |
| QQQ | PS | 2026-11-06 | 665.00 | 615.00 | — | — | 3.14 | 4,686.22 | ON |
| QQQ | IC | 2026-11-06 | 665.00 | 615.00 | 756.00 | 800.00 | 4.44 | 4,556.31 | ON |

### S-B graded at expiry today (8)
| underlying | structure | entry | expiry | settle_close | net_usd | ror | role |
|---|---|---|---|---|---|---|---|
| SPY | PS | 2026-09-25 | 2026-10-16 | 762.61 | 128.08 | +4.99% | champion |
| SPY | IC | 2026-09-25 | 2026-10-16 | 762.61 | 198.73 | +7.97% | champion |
| QQQ | PS | 2026-09-25 | 2026-10-16 | 709.58 | 188.95 | +5.39% | champion |
| QQQ | IC | 2026-09-25 | 2026-10-16 | 709.58 | 362.24 | +8.77% | champion |
| SPY | PS | 2026-09-25 | 2026-10-16 | 762.61 | 128.08 | +4.99% | exploration |
| SPY | IC | 2026-09-25 | 2026-10-16 | 762.61 | 198.73 | +7.97% | exploration |
| QQQ | PS | 2026-09-25 | 2026-10-16 | 709.58 | 188.95 | +5.39% | exploration |
| QQQ | IC | 2026-09-25 | 2026-10-16 | 709.58 | 362.24 | +8.77% | exploration |

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

S-B ledger: emitted 3 (skipped 0), exploration 3 (skipped 0), graded 8; ledger open.


## S-C state
Entry day: yes; ledger open.

Stopped at: F1 2272 · F2 1125 · F3 1005 · F4 756 · F7 50 · F5 704 · F6 14 · F8 72 · F9 1

### S-C positions tonight (0; paper, before the read)
_none selected_

Exploration book: 149 priceable names at one contract each, by first failing filter: F1 43, F2 15, F3 59, F4 3, F5 27, F6 1, F9 1

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

S-C ledger: emitted 0 (skipped 0), exploration 296 (skipped 0), graded 0.


## Watch basket (wb-1.0, exploration, paper only)
Universe: 2073 names.
Borrow snapshot: 2026-10-16 (the session's own); fee known for 2064 names.
Bull counts: 0:688, 1:887, 2:356, 3:121, 4:21, 5:0, 6:0, 7:0, 8:0
Bear counts: 0:751, 1:752, 2:394, 3:131, 4:40, 5:5, 6:0, 7:0, 8:0

### LONG (82)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ABBV | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ABM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| ACA | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| AEM | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMGN | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AWI | 3 | 0 | yes |  |  |  | x | x |  | x |  |  |  |  |  |  |  |  |  |  |  |  |  |
| BBWI | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BBY | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BFA | 3 | 0 | no |  |  |  |  | x | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| BIIB | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CAH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CBC | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  |  |  |  |  |  | x |
| CE | 3 | 0 | yes |  | x | x |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| CFG | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CHT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| CNK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| COLM | 3 | 0 | yes |  |  |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| CON | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| COO | 3 | 0 | no |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CUBI | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DRH | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| DSGR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| E | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| EG | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| EMR | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| FERG | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| FIZZ | 3 | 0 | no |  |  |  |  | x | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| FRHC | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| FUL | 4 | 0 | no |  | x |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| GGG | 4 | 0 | no |  | x |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  |  |
| GIC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| GILD | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  | x | x |
| HALO | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HBT | 3 | 0 | yes | x | x |  | x |  |  | ? |  |  | ? | ? |  |  |  | ? |  |  |  |  |  |
| HCSG | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HG | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HLI | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| HLT | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| HMC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| HONA | 3 | 0 | yes |  | x | ? |  | x |  | ? | x |  |  |  |  |  |  |  |  |  | x | x | x |
| HRTG | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| HST | 4 | 0 | no |  | x |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| JOE | 3 | 0 | no |  |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| KO | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| LQDT | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| MAR | 3 | 0 | yes | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| MCBS | 3 | 0 | yes |  | x |  | x |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| MCK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| MD | 4 | 0 | no | x | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| MO | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| MQ | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  |
| MSM | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| NHC | 4 | 0 | no | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| NVS | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| NWE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| OPLN | 3 | 0 | yes |  | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  |
| OSBC | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PAYP | 4 | 0 | yes |  | x | x | x | x |  | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| PBH | 3 | 0 | no |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PM | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| PRSU | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PSO | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| REYN | 3 | 0 | no |  | x | x |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| RGA | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RSG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| SHEL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| SHO | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? | ? |  |  |  | ? |  |  |  |  | x |
| SHOP | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SSD | 3 | 0 | yes |  | x | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| TALO | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| TDY | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TILE | 3 | 0 | yes |  | x |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| TR | 3 | 0 | no |  | x |  | x |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TRGP | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TW | 3 | 0 | no |  |  | x |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| USPH | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| VTRS | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WABC | 4 | 0 | no | x |  |  | x |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| WMK | 3 | 0 | yes |  |  |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| WS | 3 | 0 | no |  |  |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| WSM | 3 | 0 | yes | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| ZION | 3 | 0 | yes |  | x |  | x |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |

### SHORT (69)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AA | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  |  |  |  |  |  | x |
| AG | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| AI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  |  |
| ALB | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  | x |
| ALK | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| AMSC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| ATHM | 0 | 4 | no |  |  |  |  |  |  |  |  |  | ? |  |  | x | x | x | x |  |  |  |  |
| AVAV | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| BBVA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| BDC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| BEPC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| BHVN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| BIDU | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| CDE | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| CGON | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| CIEN | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  | x | x |  | ? | x |  |  | x | x |
| CPNG | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? | x |  |  |  | x |
| CRSP | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| FLNG | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| FLS | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| FSK | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  | x |  |  |  |  |
| FSLR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  |  |  |  |  | x | x |
| FSLY | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| GEO | 0 | 4 | yes |  |  |  |  |  |  | ? |  |  |  | x | x | x | x | ? |  |  |  |  |  |
| GIL | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| GNTX | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | x |  |  |  |  | x |
| GPGI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| GSL | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | ? |  |  | x | x | ? | x |  |  |  |  |
| HYMC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  |  | x |  |  |  |  |
| IDCC | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| INSM | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  | x |  |  |  | x |
| INTC | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| KEP | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| KOD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  |  |
| LEU | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| LIF | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| LNN | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | ? |  |  | x | x | ? | x |  |  |  |  |
| MAIN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| MC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| META | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| MRCY | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| MRVL | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| MSDL | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  | x |  | x |  | x |  |  |
| MU | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| MWH | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| NAMS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| NVAX | 0 | 5 | yes |  |  |  |  |  |  | ? |  |  | x | x | x | x |  | ? | x |  |  |  | x |
| OMER | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | ? |  | x | x |  | ? | x |  |  |  |  |
| OSIS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| PFG | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| PTGX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| QURE | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  |  |
| REPL | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? | x |  |  |  |  |
| RKT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| SAN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| SIRI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  |  |
| SNDX | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  |  |
| SPCX | 0 | 3 | yes |  |  | ? |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| STRD | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | ? |  |  | x |  | x | x |  |  |  |  |
| SUPN | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| TRIN | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| VERA | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| VKTX | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| WHR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  |  |  | x |  | x |
| WIX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| WLDN | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| WOLF | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? |  |  |  |  |  |
| WRBY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  |  |  |
| XE | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  | x |  |  |

### VOL (0)
_none_

CONFLICT (logged only, never a basket, DESIGN/110 §3): 82.

Ledger: emitted 151 (skipped 0), graded 639; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
