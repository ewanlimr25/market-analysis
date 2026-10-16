# S-A daily — 2026-10-15 (S3)

Preflight: WARN — prices.parquet ends 2026-10-09, BEFORE the 2026-10-15 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-10-09, BEFORE the 2026-10-15 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-10-09, BEFORE the 2026-10-15 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (0)
_no event tonight clears the filters._

## Suppressed (24)
| ticker | variant | first_fail |
|---|---|---|
| AA | A1 | F6 |
| AA | A2 | F6 |
| CFG | A1 | F6 |
| CFG | A2 | F6 |
| CNS | A1 | F4 |
| CNS | A2 | F4 |
| IBKR | A1 | F6 |
| IBKR | A2 | F6 |
| INDB | A1 | F4 |
| INDB | A2 | F4 |
| JBHT | A1 | F5 |
| JBHT | A2 | F5 |
| LADR | A1 | F2 |
| LADR | A2 | F2 |
| MTB | A1 | F5 |
| MTB | A2 | F5 |
| RF | A1 | F5 |
| RF | A2 | F5 |
| SFNC | A1 | F4 |
| SFNC | A2 | F4 |
| TFC | A1 | F3 |
| TFC | A2 | F3 |
| TRV | A1 | F3 |
| TRV | A2 | F3 |

## Exploration book tonight (4; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| AA | SS | 2026-10-23T00:00:00.000 | 40.50 | 2.87 | +6.66% | 861.59 | F6 |
| CFG | SS | 2026-11-20T00:00:00.000 | 62.50 | 4.83 | +7.18% | 697.67 | F6 |
| CFG | IC | 2026-11-20T00:00:00.000 | 62.50 | 4.29 | +5.94% | 571.23 | F6 |
| IBKR | SS | 2026-10-23T00:00:00.000 | 86.00 | 5.54 | +6.04% | 1,458.64 | F6 |

## Graded today (3)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| CMC | A1 | SS | exploration | -0.29% | -19.01 | 1 | no |
| PNC | A1 | SS | exploration | +0.40% | 86.03 | 1 | no |
| USB | A1 | SS | exploration | +0.36% | 20.52 | 1 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 2 | 2 | +2.69% | 3.42 | 232.76 |
| sa-1.0 | champion | A1 | SS | 2 | 2 | +3.83% | 3.98 | 328.86 |
| sa-1.0 | champion | A2 | IC | 2 | 2 | +2.69% | 3.42 | 232.76 |
| sa-1.0 | champion | A2 | SS | 2 | 2 | +3.83% | 3.98 | 328.86 |
| sa-1.0 | exploration | A1 | IC | 9 | 7 | -0.50% | -0.52 | -981.92 |
| sa-1.0 | exploration | A1 | SS | 15 | 8 | +0.46% | 0.72 | -87.91 |

Ledger: emitted 0 (skipped 0), exploration 4 (skipped 0), graded 3; ledger open.

## S-B state
Gate (2026-10-15, from 2026-10-14 closes): SPY ON (VIX 16.87, VIX3M 18.79, X 16.87 vs median 15.29) · QQQ ON (VIX 16.87, VIX3M 18.79, X 22.7 vs median 21.145)

Next session (2026-10-16, from 2026-10-15 closes): SPY ON (VIX 16.46, VIX3M 18.49, X 16.46 vs median 15.29) · QQQ ON (VIX 16.46, VIX3M 18.49, X 22.89 vs median 21.145)

CBOE refresh: ok through 2026-10-15; index-vol through 2026-10-15

Entry day: no.

### S-B positions tonight (0)
_none_

### S-B graded at expiry today (0)
_none due_

Open positions: QQQ-IC 2, QQQ-PS 3, SPY-IC 2, SPY-PS 2

### S-B forward ledger to date
| policy_id | role | sleeve | n | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|---|
| sb-1.0 | champion | QQQ-IC | 1 | — | — | 321.63 |
| sb-1.0 | champion | QQQ-PS | 1 | — | — | 224.53 |
| sb-1.0 | champion | SPY-PS | 1 | — | — | 155.40 |
| sb-1.0 | exploration | QQQ-IC | 1 | — | — | 321.63 |
| sb-1.0 | exploration | QQQ-PS | 2 | — | — | 436.72 |
| sb-1.0 | exploration | SPY-IC | 1 | — | — | 170.81 |
| sb-1.0 | exploration | SPY-PS | 2 | — | — | 279.72 |

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
Universe: 2033 names.
Borrow snapshot: 2026-10-15 (the session's own); fee known for 2024 names.
Bull counts: 0:768, 1:798, 2:353, 3:102, 4:12, 5:0, 6:0, 7:0, 8:0
Bear counts: 0:687, 1:724, 2:450, 3:134, 4:33, 5:5, 6:0, 7:0, 8:0

### LONG (60)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ABBV | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| ABM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| ACA | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| ADP | 3 | 0 | yes | x |  |  | x |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| AES | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| AMGN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| ARQT | 3 | 0 | no |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BFA | 3 | 0 | yes |  |  |  |  | x | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| BIIB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CAH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CNK | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CON | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| COO | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DHR | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DRH | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DSGR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| E | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| EBAY | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| FERG | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| FIZZ | 3 | 0 | no |  |  |  |  | x | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| FUL | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| GGG | 3 | 0 | no |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| HALO | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HCA | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| HLF | 4 | 0 | no |  | x |  |  | x |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| HMC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| HNGE | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| HRTG | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| HST | 3 | 0 | yes |  | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| IDXX | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| JOYY | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| KOF | 3 | 0 | no | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| LAUR | 4 | 0 | no | x | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  |  |
| MCK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| MD | 4 | 0 | yes | x | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| MICC | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| MQ | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  |
| MSM | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| MTD | 4 | 0 | no | x | x |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| NHC | 4 | 0 | no | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| NWE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PD | 3 | 0 | no | x |  |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| PLUS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| PRSU | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PSO | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| RGA | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RSG | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| SHEL | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SSL | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| SU | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| SYK | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| TBBB | 3 | 0 | no | x | x |  |  |  |  |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| TR | 3 | 0 | yes |  | x |  | x |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TW | 3 | 0 | no |  |  | x |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| UTZ | 3 | 0 | no | x |  |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  |  |
| UVE | 3 | 0 | no | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| VEON | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| WABC | 3 | 0 | yes | x |  |  | x |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| WS | 3 | 0 | no |  |  |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |

### SHORT (75)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AA | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  | x |
| AAOI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| AG | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| AGI | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  | x |
| ALK | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| AMSC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| ATHM | 0 | 4 | no |  |  |  |  |  |  |  |  |  | ? |  |  | x | x | x | x |  |  |  |  |
| BA | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  | x | x |
| BBVA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| BDC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| BHVN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| BIDU | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| C | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| CAR | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| CDE | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| CELC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| CIEN | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  | x | x |  | ? | x |  |  | x | x |
| CRCL | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| CVNA | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  |  | x |
| ERAS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  | x |  |  |  |  |  |  | x |
| FIBK | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| FLG | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? | x |  |  |  |  |
| FLNG | 0 | 4 | no |  |  |  |  |  |  |  |  |  | ? |  |  | x | x | x | x |  |  |  |  |
| FLS | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| FSK | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  |  |
| GLNG | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  | x | ? | x |  |  |  | x |
| GNK | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | ? |  |  | x | x | ? | x |  |  |  |  |
| GOOGL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  | x | x |
| GPGI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| HTGC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  |  |
| IBRX | 0 | 4 | yes |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  |  | x |
| INSM | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| INTC | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| KEP | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| KLAR | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? | x |  |  |  |  |
| KOD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  |  |
| LEU | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| LIF | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| LNC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| LULU | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  |  |  |  |  |  | x |
| MDB | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  | x | x |
| META | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| MMED | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  | x |
| MTZ | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  | x |  | x |
| MU | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| MWH | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| NEM | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  | x |
| NKE | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  |  |  |  |  | x | x |
| NN | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  |  |  |
| NTRS | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| OSIS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| PFG | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| PPTA | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| PRCT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| QURE | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  |  |
| REPL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| RH | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  |  |  |  |  | x |
| RIVN | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  | x |  |  |  | x |
| RKT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| SAN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| SCCO | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| SKHY | 0 | 3 | no |  |  | ? |  |  |  |  |  |  |  | x | x |  |  | ? | x |  | ? | x | x |
| SNDK | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| SNDX | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| SOFI | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  | x | x |
| SPHR | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  | x |  |  |  | x |  |  |  | x |
| STEP | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| SUPN | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| TCBI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | ? |  |  | x | ? | x |  |  |  |  |
| VSH | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| WDC | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| WHR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  |  |  | x |  | x |
| WLDN | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| WOLF | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| XE | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  | x |  |  |

### VOL (1)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GME | 3 | 2 | no | x | x |  |  |  |  | ? | x |  |  | x | x |  |  | ? |  | x |  | x | x |

CONFLICT (logged only, never a basket, DESIGN/110 §3): 94.

Ledger: emitted 136 (skipped 0), graded 623; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
