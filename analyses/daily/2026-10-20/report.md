# S-A daily — 2026-10-20 (S3)

Preflight: WARN — prices.parquet ends 2026-10-16, BEFORE the 2026-10-20 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-10-16, BEFORE the 2026-10-20 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-10-16, BEFORE the 2026-10-20 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (2)
| ticker | variant | structure | expiry | k | k_up | k_dn | credit_entry | credit_net_pct | risk_usd | contracts | entry_tier_max | cap_pass |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| UAL | A1 | SS | 2026-10-23T00:00:00.000 | 98.00 | — | — | 5.66 | +5.54% | 2,201.02 | 1 | 1 | yes |
| UAL | A2 | SS | 2026-10-23T00:00:00.000 | 98.00 | — | — | 5.66 | +5.54% | 2,201.02 | 1 | 1 | yes |

## Suppressed (84)
| ticker | variant | first_fail |
|---|---|---|
| ABT | A1 | F3 |
| ABT | A2 | F3 |
| ADC | A1 | F5 |
| ADC | A2 | F5 |
| ALK | A1 | F6 |
| ALK | A2 | F6 |
| AMX | A1 | F3 |
| AMX | A2 | F3 |
| BKU | A1 | F4 |
| BKU | A2 | F4 |
| BWB | A1 | F3 |
| BWB | A2 | F3 |
| CB | A1 | F3 |
| CB | A2 | F3 |
| CME | A1 | F3 |
| CME | A2 | F3 |
| COF | A1 | F3 |
| COF | A2 | F3 |
| DHR | A1 | F3 |
| DHR | A2 | F3 |
| ELS | A1 | F5 |
| ELS | A2 | F5 |
| ELV | A1 | F3 |
| ELV | A2 | F3 |
| EWBC | A1 | F5 |
| EWBC | A2 | F5 |
| HCSG | A1 | F3 |
| HCSG | A2 | F3 |
| HWC | A1 | F5 |
| HWC | A2 | F5 |
| IART | A1 | F3 |
| IART | A2 | F3 |
| ISRG | A1 | F3 |
| ISRG | A2 | F3 |
| LAD | A1 | F5 |
| LAD | A2 | F5 |
| LRN | A1 | F5 |
| LRN | A2 | F5 |
| MCB | A1 | F3 |
| MCB | A2 | F3 |
| MCO | A1 | F3 |
| MCO | A2 | F3 |
| MHO | A1 | F4 |
| MHO | A2 | F4 |
| NEE | A1 | F3 |
| NEE | A2 | F3 |
| NFLX | A1 | F3 |
| NFLX | A2 | F3 |
| NLY | A1 | F6 |
| NLY | A2 | F6 |
| NP | A1 | F4 |
| NP | A2 | F4 |
| NTRS | A1 | F5 |
| NTRS | A2 | F5 |
| OFG | A1 | F4 |
| OFG | A2 | F4 |
| ONB | A1 | F5 |
| ONB | A2 | F5 |
| ORRF | A1 | F3 |
| ORRF | A2 | F3 |
| OZK | A1 | F5 |
| OZK | A2 | F5 |
| PEGA | A1 | F5 |
| PEGA | A2 | F5 |
| PM | A1 | F3 |
| PM | A2 | F3 |
| QCRH | A1 | F3 |
| QCRH | A2 | F3 |
| SF | A1 | F5 |
| SF | A2 | F5 |
| T | A1 | F3 |
| T | A2 | F3 |
| TDY | A1 | F5 |
| TDY | A2 | F5 |
| TMO | A1 | F3 |
| TMO | A2 | F3 |
| UNF | A1 | F5 |
| UNF | A2 | F5 |
| WAB | A1 | F5 |
| WAB | A2 | F5 |
| WFRD | A1 | F5 |
| WFRD | A2 | F5 |
| WGO | A1 | F3 |
| WGO | A2 | F3 |

## Exploration book tonight (4; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| ALK | SS | 2026-11-20T00:00:00.000 | 35.00 | 4.50 | +12.51% | 676.28 | F6 |
| ALK | IC | 2026-11-20T00:00:00.000 | 35.00 | 3.97 | +10.66% | 352.78 | F6 |
| NLY | SS | 2026-10-23T00:00:00.000 | 18.50 | 0.57 | +2.81% | 245.05 | F6 |
| UAL | SS | 2026-10-23T00:00:00.000 | 98.00 | 5.66 | +5.54% | 2,201.02 | PASS |

## Graded today (18)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| STLD | A1 | SS | champion | +0.30% | 73.95 | 1 | no |
| KEY | A1 | SS | champion | -0.91% | -72.31 | 1 | no |
| HAL | A1 | SS | champion | +0.09% | 2.96 | 1 | no |
| STLD | A2 | SS | champion | +0.30% | 73.95 | 1 | no |
| KEY | A2 | SS | champion | -0.91% | -72.31 | 1 | no |
| HAL | A2 | SS | champion | +0.09% | 2.96 | 1 | no |
| AGNC | A1 | SS | exploration | -0.48% | -4.09 | 1 | no |
| ALLY | A1 | SS | exploration | -1.33% | -49.95 | 1 | no |
| CCK | A1 | SS | exploration | -2.49% | -285.90 | 2 | no |
| CCK | A1 | IC | exploration | -3.42% | -392.86 | 2 | no |
| GM | A1 | SS | exploration | -0.72% | -59.44 | 1 | no |
| GM | A1 | IC | exploration | -0.87% | -71.95 | 1 | no |
| HAL | A1 | SS | exploration | +0.09% | 2.96 | 1 | no |
| HAS | A1 | SS | exploration | -3.50% | -344.19 | 1 | no |
| KEY | A1 | SS | exploration | -0.91% | -18.08 | 1 | no |
| MMM | A1 | SS | exploration | +1.81% | 293.42 | 1 | no |
| STLD | A1 | SS | exploration | +0.30% | 73.95 | 1 | no |
| VICR | A1 | SS | exploration | -0.48% | -91.45 | 1 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 2 | 2 | +2.69% | 3.42 | 232.76 |
| sa-1.0 | champion | A1 | SS | 7 | 4 | +0.36% | 0.29 | 192.03 |
| sa-1.0 | champion | A2 | IC | 2 | 2 | +2.69% | 3.42 | 232.76 |
| sa-1.0 | champion | A2 | SS | 7 | 4 | +0.36% | 0.29 | 192.03 |
| sa-1.0 | exploration | A1 | IC | 12 | 9 | -0.82% | -1.13 | -1,517.95 |
| sa-1.0 | exploration | A1 | SS | 30 | 11 | -0.26% | -0.67 | -715.87 |

Ledger: emitted 2 (skipped 0), exploration 4 (skipped 0), graded 18; ledger open.

## S-B state
Gate (2026-10-20, from 2026-10-19 closes): SPY ON (VIX 18.44, VIX3M 19.6, X 18.44 vs median 15.36) · QQQ ON (VIX 18.44, VIX3M 19.6, X 25.56 vs median 21.22)

Next session (2026-10-21, from 2026-10-20 closes): SPY UNKNOWN:null input at 2026-10-20 · QQQ UNKNOWN:null input at 2026-10-20

CBOE refresh: ok through 2026-10-20; index-vol through 2026-10-20

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
Universe: 2079 names.
Borrow snapshot: 2026-10-20 (the session's own); fee known for 2072 names.
Bull counts: 0:720, 1:815, 2:409, 3:112, 4:21, 5:2, 6:0, 7:0, 8:0
Bear counts: 0:830, 1:741, 2:335, 3:132, 4:36, 5:5, 6:0, 7:0, 8:0

### LONG (84)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ABBV | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| ABM | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| ACA | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| AFG | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| AMG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMGN | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMN | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| APPN | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| ARQT | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| ASB | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ASND | 3 | 0 | yes |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| AVPT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| AWI | 4 | 0 | no |  | x |  | x | x |  | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| BBY | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| BIIB | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BRKB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  | x | x |
| CAH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CFG | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CNK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| COLM | 3 | 0 | no |  |  |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| COO | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CRL | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CUBI | 3 | 0 | no |  |  |  | x | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DINO | 3 | 0 | yes | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| DRH | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| E | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| EFSC | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| EMR | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EQH | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| FIZZ | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| FNB | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| GIC | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HALO | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HG | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HLI | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| HLT | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x | x |
| HMC | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| HRTG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HST | 5 | 0 | no | x | x |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| IDT | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| IOSP | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? | ? |  |  |  | ? |  |  |  |  | x |
| IRM | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| JOE | 3 | 0 | no |  |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| JOYY | 4 | 0 | no | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| KLRA | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| KMI | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| LXP | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  |
| MAR | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| MCK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| MD | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| MPC | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| MQ | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  |
| MTD | 4 | 0 | no | x | x |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| NVS | 3 | 0 | no |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| NWE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| NXPI | 3 | 0 | yes |  | x | x |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| OSBC | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PRSU | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| QSR | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |  |  |  |
| REAL | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| RGA | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RLJ | 3 | 0 | yes | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| RNG | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RPRX | 3 | 0 | yes | x | x |  | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| RS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RSG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| SAFT | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| SHOP | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| SJM | 3 | 0 | yes | x |  |  | x |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| SNY | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| SSD | 3 | 0 | no |  | x | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |  |  |  |
| SSNC | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| SU | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| SVV | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| TALO | 3 | 0 | no | x |  |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| TBBB | 3 | 0 | no | x | x |  |  |  |  |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| TDY | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TIMB | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TW | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| TX | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| UCB | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  | ? | ? |  |  |  | ? |  |  |  |  | x |
| VTRS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WMT | 4 | 0 | yes |  | x |  |  | x | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| ZION | 4 | 0 | no |  | x |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |

### SHORT (59)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AA | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| AAL | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  | x |  |  | x | x |  |  |  | x |
| AAOI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| AI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| ALK | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  |  | x |  |  |  | x |
| AMSC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| BDC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| BE | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| BEPC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| BIDU | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | x | x |  |  |  | x |
| BXSL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| C | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| CC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| CDE | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  | x |
| COIN | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | x |  |  |  |  | x |
| CPNG | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  | x | ? | x |  |  |  | x |
| CRSP | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| CSWC | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| CURB | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| CVNA | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| DELL | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| ELAN | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| FSK | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  |  |
| FSLY | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  |  | x |
| GME | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| GNTX | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x |  |  |  |  |  | x |
| GOOGL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  | x | x |
| GPGI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| GSL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | ? |  |  | x | x | ? | x |  |  |  |  |
| HIMS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| HL | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  | x |
| INSM | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  | x |  |  |  | x |
| IONQ | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| KEP | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| MAT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| META | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| MSTR | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  |  | x | x |
| MWH | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| NVAX | 0 | 5 | no |  |  |  |  |  |  | ? |  |  | x | x | x | x |  | ? | x |  |  |  |  |
| OSIS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| QURE | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  | x |
| RGTI | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| RH | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  |  |  |  |  |  | x |
| RIO | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| SCCO | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| SIRI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  |  |
| SKHY | 0 | 3 | no |  |  | ? |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  | x | x |
| SLS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| SNDX | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| SNOW | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| STEP | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| STNG | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| STRD | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  | x |  | x | x |  |  |  |  |
| THO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| TRIN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| UAL | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  | x |  |  | x | x |  |  | x | x |
| WLDN | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| WOLF | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? |  |  |  |  |  |
| XE | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  | x |  |  |

### VOL (0)
_none_

CONFLICT (logged only, never a basket, DESIGN/110 §3): 89.

Ledger: emitted 143 (skipped 0), graded 521; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
