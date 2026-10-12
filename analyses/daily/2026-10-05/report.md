# S-A daily — 2026-10-05 (S3)

Preflight: WARN — prices.parquet ends 2026-10-02, BEFORE the 2026-10-05 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-10-02, BEFORE the 2026-10-05 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-10-02, BEFORE the 2026-10-05 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (0)
_no event tonight clears the filters._

## Suppressed (6)
| ticker | variant | first_fail |
|---|---|---|
| APOG | A1 | F3 |
| APOG | A2 | F3 |
| LW | A1 | F6 |
| LW | A2 | F6 |
| RPM | A1 | F6 |
| RPM | A2 | F6 |

## Exploration book tonight (4; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| LW | SS | 2026-10-16T00:00:00.000 | 45.00 | 4.35 | +9.22% | 661.56 | F6 |
| LW | IC | 2026-10-16T00:00:00.000 | 45.00 | 3.93 | +8.10% | 356.88 | F6 |
| RPM | SS | 2026-10-16T00:00:00.000 | 95.00 | 6.71 | +6.30% | 957.02 | F6 |
| RPM | IC | 2026-10-16T00:00:00.000 | 95.00 | 5.52 | +4.87% | 448.17 | F6 |

## Graded today (0)
_none due_

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 1 | 1 | +1.91% | — | 66.98 |
| sa-1.0 | champion | A1 | SS | 1 | 1 | +2.87% | — | 100.79 |
| sa-1.0 | champion | A2 | IC | 1 | 1 | +1.91% | — | 66.98 |
| sa-1.0 | champion | A2 | SS | 1 | 1 | +2.87% | — | 100.79 |
| sa-1.0 | exploration | A1 | IC | 1 | 1 | +1.91% | — | 66.98 |
| sa-1.0 | exploration | A1 | SS | 1 | 1 | +2.87% | — | 100.79 |

Ledger: emitted 0 (skipped 0), exploration 4 (skipped 0), graded 0; ledger open.

## S-B state
Gate (2026-10-05, from 2026-10-02 closes): SPY OFF:G2 (VIX 15.31, VIX3M 18.01, X 15.31 vs median 15.780000000000001) · QQQ OFF:G2 (VIX 15.31, VIX3M 18.01, X 21.2 vs median 21.475)

Next session (2026-10-06, from 2026-10-05 closes): SPY OFF:G2 (VIX 15.52, VIX3M 18.0, X 15.52 vs median 15.780000000000001) · QQQ ON (VIX 15.52, VIX3M 18.0, X 21.7 vs median 21.475)

CBOE refresh: ok through 2026-10-09; index-vol through 2026-10-09

Entry day: no.

### S-B positions tonight (0)
_none_

### S-B graded at expiry today (0)
_none due_

Open positions: QQQ-IC 2, QQQ-PS 2, SPY-IC 2, SPY-PS 2

### S-B forward ledger to date
| policy_id | role | sleeve | n | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|---|
| sb-1.0 | champion | QQQ-IC | 1 | — | — | 321.63 |
| sb-1.0 | champion | QQQ-PS | 1 | — | — | 224.53 |
| sb-1.0 | champion | SPY-PS | 1 | — | — | 155.40 |
| sb-1.0 | exploration | QQQ-IC | 1 | — | — | 321.63 |
| sb-1.0 | exploration | QQQ-PS | 1 | — | — | 224.53 |
| sb-1.0 | exploration | SPY-PS | 1 | — | — | 155.40 |

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
| C2-SS | 4 | 6,032.94 | 8,000.00 | 3 |
| C2-IB | 4 | 3,571.32 | 4,000.00 | 3 |

### S-C forward ledger to date (entry-week series)
_ledger empty_

Progress to the read: graded entry-weeks 0 of 40 (C1-SS), 0 of 40 (C1-IB), 0 of 40 (C2-SS), 0 of 40 (C2-IB)

S-C ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0.


## Watch basket (wb-1.0, exploration, paper only)
Universe: 1985 names.
Borrow snapshot: 2026-10-05 (the session's own); fee known for 1980 names.
Bull counts: 0:921, 1:720, 2:278, 3:58, 4:7, 5:1, 6:0, 7:0, 8:0
Bear counts: 0:563, 1:688, 2:492, 3:186, 4:51, 5:3, 6:2, 7:0, 8:0

### LONG (46)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ACA | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| ADI | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x | x |
| AES | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| AME | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMN | 5 | 0 | no | x | x |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| APH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AVPT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| AZTA | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| BHE | 3 | 0 | yes |  | x |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| BPRE | 3 | 0 | yes |  |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| BRZE | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| CEG | 4 | 0 | yes |  | x |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CLBT | 3 | 0 | yes |  |  | x |  | x |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| CNXN | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| DASH | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  |  |  |  |  | x | x |
| E | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| EMR | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| FFIV | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| FTNT | 4 | 0 | no | x | x |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| FTRE | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| FUL | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| GIC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| HNGE | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| JOYY | 4 | 0 | no | x | x |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| KEYS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LAZR | 3 | 0 | no | x |  | ? |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  | ? |  |  |
| LSPD | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| MSM | 4 | 0 | no | x | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  |  |
| MTD | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| NHC | 3 | 0 | yes | x |  |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| NTES | 3 | 0 | yes |  | x |  | x |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| OPY | 3 | 0 | no | x |  |  | x |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| PLUS | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PRLB | 3 | 0 | no | x |  |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| PWR | 3 | 0 | yes |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| RAL | 3 | 0 | yes | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| REYN | 3 | 0 | yes |  | x | x |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| RNG | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SFL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| SNX | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| STNG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TK | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TOST | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| TW | 3 | 0 | no |  |  | x |  | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| VEON | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| WCC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |

### SHORT (135)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ABVX | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  | ? | x |  |  |  |  |
| ACAD | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? | x |  |  |  |  | x |  |  |  |  |
| AEE | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x |  |  |  |  |  | x |
| AEM | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  | x |  | x |  |  |  |  | x |
| AHR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  |  |
| AMT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | x |  |  |  |  | x |
| APLD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| ARCC | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| ASTS | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  |  |  |  |  | x | x |
| ATHM | 0 | 4 | yes |  |  |  |  |  |  |  |  |  | ? |  |  | x | x | x | x |  |  |  |  |
| ATO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x |  |  |  |  |  | x |
| AUB | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| AXGN | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| AYI | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| BCS | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| BILI | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? |  |  |  |  |  |
| BMO | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| BMRN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| CAG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| CALM | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  | x |
| CAR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  |  |  |  |  |  |  |
| CBRE | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  |  | x |
| CCI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | x |  |  |  |  | x |
| CFR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| CLBK | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CLSK | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| CM | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| CMPS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| CRCL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| CTRE | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  | x |
| DAL | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| DAVE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| DG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | x |  |  |  |  | x |
| DUK | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | x |  |  |  |  | x |
| DX | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  |  | x | x |  | x |  | x |
| DYN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| ED | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | x |  |  |  |  | x |
| ENPH | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| EPRT | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  | x |
| ERIE | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| FE | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x |  |  |  |  |  | x |
| FIBK | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| FIG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  |  |  |  |  |  | x |
| FIGR | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| FRT | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| FSLR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| GD | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| GDS | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  |  |
| GFL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| GIL | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| GNTX | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  |  |
| GSK | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| HAPN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| HDB | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| HIMS | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  |  | x |
| HTO | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| HUT | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| IMO | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| INCY | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| INGR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x |  |  |  |  |  | x |
| INSM | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| IP | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| JAZZ | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| JBTM | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| JNJ | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| JPM | 0 | 4 | no |  |  |  |  |  |  |  |  |  |  | x |  |  | x | x | x |  |  |  | x |
| KBR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| KD | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| KHC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| KNSL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | x |  |  |  |  | x |
| LEGN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| LKQ | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  |  |
| LUNR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| MAA | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x |  | x |  |  |  | x |
| MAIN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| MARA | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| MDGL | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x | x |  |  |  |  | x |
| MGM | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  | x |  | x |
| MP | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  |  |  |  |  | x |
| NAMS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| NEE | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x |  |  |  |  |  | x |
| NEM | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  | x |
| NFLX | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| NHI | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  |  |
| NKE | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  |  |  |  | x | x | x |
| NKTR | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  |  |  |  |  | x |
| NN | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  |  |  |
| NTST | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x | ? |  |  |  |  | x |  |  |  |  |
| NVTS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| O | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  | x |  | x |  | x |
| OBDC | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  | x |
| OLN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| OZK | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| PEP | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  | x |  |  |  | x |  | x |
| PLD | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| PNC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| POR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x |  |  |  |  |  | x |
| PRU | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | x |  |  |  |  | x |
| QBTS | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| QSR | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x |  |  | x |  | x |  |  |  | x |
| QURE | 0 | 5 | no |  |  |  |  |  |  | ? |  |  | x | x | x | x |  | ? | x |  |  |  | x |
| RCI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| RKT | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? | x |  |  |  | x |
| ROST | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| RY | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| SAIC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| SBAC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | x |  |  |  |  | x |
| SBRA | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| SBUX | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  | x |
| SF | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x |  | x |  |  |  | x |
| SNEX | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| SNY | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| SOFI | 0 | 6 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  | x | x |  |  | x | x |
| STAG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| SW | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| TEM | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| TKO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? |  |  |  |  | x |
| USAR | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| UUUU | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  | x |  |  |  | x |
| VICI | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x | x |  | x |  | x |
| VKTX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| VMC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| VMRK | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | x |  |  |  |  | x |
| VSAT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| VSEC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| WAL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| WEC | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | x |  |  |  |  | x |
| WELL | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| WHR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  |  |  | x | x | x |
| WLDN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| WLK | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| WPC | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  | x |  |  |  | x |
| WSO | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| WULF | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| ZYME | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | ? |  | x | x |  | ? | x |  |  |  | x |

### VOL (1)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GME | 1 | 2 | yes |  |  |  |  |  |  | ? | x |  |  | x | x |  |  | ? |  | x |  | x | x |

CONFLICT (logged only, never a basket, DESIGN/110 §3): 77.

Ledger: emitted 182 (skipped 0), graded 413; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
