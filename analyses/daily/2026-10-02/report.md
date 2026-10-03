# S-A daily — 2026-10-02 (S3)

Preflight: WARN — prices.parquet ends 2026-09-25, BEFORE the 2026-10-02 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-09-25, BEFORE the 2026-10-02 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-09-25, BEFORE the 2026-10-02 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (0)
_no event tonight clears the filters._

## Suppressed (0)
_none_

## Graded today (0)
_none due_

## Season to date (forward ledger)
_ledger empty_

Ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0; ledger open.

## S-B state
Gate (2026-10-02, from 2026-10-01 closes): SPY ON (VIX 16.39, VIX3M 18.58, X 16.39 vs median 15.695) · QQQ ON (VIX 16.39, VIX3M 18.58, X 22.51 vs median 21.155)

Next session (2026-10-05, from 2026-10-02 closes): SPY OFF:G2 (VIX 15.31, VIX3M 18.01, X 15.31 vs median 15.780000000000001) · QQQ OFF:G2 (VIX 15.31, VIX3M 18.01, X 21.2 vs median 21.475)

CBOE refresh: ok through 2026-10-02; index-vol through 2026-10-02

Entry day: yes.

### S-B positions tonight (4)
| underlying | structure | expiry | k_p1 | k_p2 | k_c1 | k_c2 | credit_entry | max_loss_usd | contracts | entry_tier_max |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY | PS | 2026-10-23 | 741.00 | 715.00 | — | — | 1.21 | 2,479.13 | 1 | 1 |
| SPY | IC | 2026-10-23 | 741.00 | 715.00 | 798.00 | 825.00 | 1.82 | 2,518.42 | 1 | 1 |
| QQQ | PS | 2026-10-23 | 712.00 | 675.00 | — | — | 1.97 | 3,502.95 | 1 | 1 |
| QQQ | IC | 2026-10-23 | 712.00 | 675.00 | 790.00 | 830.00 | 3.00 | 3,699.52 | 1 | 1 |

### S-B exploration book tonight (4; one contract per sleeve, gate ignored, gate verdict recorded)
| underlying | structure | expiry | k_p1 | k_p2 | k_c1 | k_c2 | credit_entry | max_loss_usd | gate_verdict |
|---|---|---|---|---|---|---|---|---|---|
| SPY | PS | 2026-10-23 | 741.00 | 715.00 | — | — | 1.21 | 2,479.13 | ON |
| SPY | IC | 2026-10-23 | 741.00 | 715.00 | 798.00 | 825.00 | 1.82 | 2,518.42 | ON |
| QQQ | PS | 2026-10-23 | 712.00 | 675.00 | — | — | 1.97 | 3,502.95 | ON |
| QQQ | IC | 2026-10-23 | 712.00 | 675.00 | 790.00 | 830.00 | 3.00 | 3,699.52 | ON |

### S-B graded at expiry today (6)
| underlying | structure | entry | expiry | settle_close | net_usd | ror | role |
|---|---|---|---|---|---|---|---|
| SPY | PS | 2026-09-11 | 2026-10-02 | 769.75 | 155.40 | +5.47% | champion |
| QQQ | PS | 2026-09-11 | 2026-10-02 | 749.59 | 224.53 | +5.26% | champion |
| QQQ | IC | 2026-09-11 | 2026-10-02 | 749.59 | 321.63 | +7.72% | champion |
| SPY | PS | 2026-09-11 | 2026-10-02 | 769.75 | 155.40 | +5.47% | exploration |
| QQQ | PS | 2026-09-11 | 2026-10-02 | 749.59 | 224.53 | +5.26% | exploration |
| QQQ | IC | 2026-09-11 | 2026-10-02 | 749.59 | 321.63 | +7.72% | exploration |

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

S-B ledger: emitted 4 (skipped 0), exploration 4 (skipped 0), graded 6; ledger open.


## S-C state
Entry day: yes; ledger open.

Stopped at: F1 2637 · F2 1072 · F3 993 · F4 757 · F7 671 · F5 37 · F6 19 · F8 100 · F9 6; C1:selected 5 · C2:C2_sector 1 · C2:selected 4

### S-C positions tonight (18; paper, before the read)
| variant | rank | ticker | sector | structure | close | iv30d | expiry | dte_cal | k | k_up | k_dn | credit_entry | max_loss_usd | stress_loss_usd | entry_cost_usd | contracts | sigma_hold | cap_pass | cap_reason |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 | 1 | WULF | Financial Services | IB | 15.49 | 0.75 | 2026-10-30 | 28 | 15.50 | 22.00 | 9.00 | 2.46 | 403.72 | — | 4.57 | 1 | 3.22 | yes | — |
| C1 | 2 | MARA | Financial Services | IB | 11.23 | 0.78 | 2026-10-30 | 28 | 11.50 | 16.00 | 6.50 | 1.83 | 317.34 | — | 4.73 | 1 | 2.42 | yes | — |
| C1 | 3 | QBTS | Technology | IB | 15.77 | 0.65 | 2026-10-30 | 28 | 15.50 | 21.50 | 10.00 | 2.09 | 391.15 | — | 6.36 | 1 | 2.83 | yes | — |
| C1 | 4 | CRCL | Financial Services | IB | 81.25 | 0.63 | 2026-10-30 | 28 | 80.00 | 110.00 | 53.00 | 10.67 | 1,932.82 | — | 23.44 | 1 | 14.24 | yes | — |
| C1 | 5 | OKLO | Utilities | IB | 35.87 | 0.64 | 2026-10-30 | 28 | 35.00 | 49.00 | 23.00 | 4.83 | 917.44 | — | 19.09 | 1 | 6.38 | yes | — |
| C1 | 1 | WULF | Financial Services | SS | 15.49 | 0.75 | 2026-10-30 | 28 | 15.50 | — | — | 2.64 | — | 703.37 | 2.73 | 1 | 3.22 | yes | — |
| C1 | 2 | MARA | Financial Services | SS | 11.23 | 0.78 | 2026-10-30 | 28 | 11.50 | — | — | 1.94 | — | 558.45 | 2.89 | 1 | 2.42 | yes | — |
| C1 | 3 | QBTS | Technology | SS | 15.77 | 0.65 | 2026-10-30 | 28 | 15.50 | — | — | 2.19 | — | 655.75 | 4.54 | 1 | 2.83 | yes | — |
| C1 | 4 | CRCL | Financial Services | SS | 81.25 | 0.63 | 2026-10-30 | 28 | 80.00 | — | — | 11.20 | — | 3,276.59 | 20.02 | 1 | 14.24 | yes | — |
| C1 | 5 | OKLO | Utilities | SS | 35.87 | 0.64 | 2026-10-30 | 28 | 35.00 | — | — | 5.07 | — | 1,494.53 | 16.91 | 1 | 6.38 | yes | — |
| C2 | 1 | WULF | Financial Services | IB | 15.49 | 0.75 | 2026-10-30 | 28 | 15.50 | 22.00 | 9.00 | 2.46 | 403.72 | — | 4.57 | 1 | 3.22 | yes | — |
| C2 | 2 | MARA | Financial Services | IB | 11.23 | 0.78 | 2026-10-30 | 28 | 11.50 | 16.00 | 6.50 | 1.83 | 317.34 | — | 4.73 | 1 | 2.42 | yes | — |
| C2 | 3 | CRCL | Financial Services | IB | 81.25 | 0.63 | 2026-10-30 | 28 | 80.00 | 110.00 | 53.00 | 10.67 | 1,932.82 | — | 23.44 | 1 | 14.24 | yes | — |
| C2 | 4 | OKLO | Utilities | IB | 35.87 | 0.64 | 2026-10-30 | 28 | 35.00 | 49.00 | 23.00 | 4.83 | 917.44 | — | 19.09 | 1 | 6.38 | yes | — |
| C2 | 1 | WULF | Financial Services | SS | 15.49 | 0.75 | 2026-10-30 | 28 | 15.50 | — | — | 2.64 | — | 703.37 | 2.73 | 1 | 3.22 | yes | — |
| C2 | 2 | MARA | Financial Services | SS | 11.23 | 0.78 | 2026-10-30 | 28 | 11.50 | — | — | 1.94 | — | 558.45 | 2.89 | 1 | 2.42 | yes | — |
| C2 | 3 | CRCL | Financial Services | SS | 81.25 | 0.63 | 2026-10-30 | 28 | 80.00 | — | — | 11.20 | — | 3,276.59 | 20.02 | 1 | 14.24 | yes | — |
| C2 | 4 | OKLO | Utilities | SS | 35.87 | 0.64 | 2026-10-30 | 28 | 35.00 | — | — | 5.07 | — | 1,494.53 | 16.91 | 1 | 6.38 | yes | — |

Exploration book: 81 priceable names at one contract each, by first failing filter: F1 16, F2 2, F3 48, F5 3, F6 1, F9 6, PASS 5

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

S-C ledger: emitted 18 (skipped 0), exploration 162 (skipped 0), graded 0.


## Watch basket (wb-1.0, exploration, paper only)
Universe: 2008 names.
Borrow snapshot: 2026-10-02 (the session's own); fee known for 2003 names.
Bull counts: 0:941, 1:741, 2:264, 3:59, 4:3, 5:0, 6:0, 7:0, 8:0
Bear counts: 0:506, 1:633, 2:541, 3:239, 4:77, 5:10, 6:2, 7:0, 8:0

### LONG (37)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ADI | 3 | 0 | yes | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| AES | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| AME | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMN | 4 | 0 | no | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| AMRX | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| APH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ARW | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AVNT | 3 | 0 | yes |  | x |  | x |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| AZTA | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| BRZE | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| CNXN | 3 | 0 | yes | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| DSGR | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| EME | 3 | 0 | no |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EMR | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| FFIV | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| FTNT | 4 | 0 | no | x | x |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| GIC | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| HNGE | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| KEYS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LAZR | 3 | 0 | no | x |  | ? |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  | ? |  |  |
| MSM | 3 | 0 | yes | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| MTD | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| MTRN | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| NVGS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| OPY | 3 | 0 | no | x |  |  | x |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PLUS | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| PRLB | 3 | 0 | no | x |  |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| SCSC | 3 | 0 | no |  | x |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| SFL | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| SNX | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| STNG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| STRF | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TEN | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TRMD | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| TTC | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| TW | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| WCC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |

### SHORT (182)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ABVX | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  | ? | x |  |  |  |  |
| ACAD | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? | x |  |  |  |  | x |  |  |  |  |
| AEE | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  | x |
| AEM | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  | x |  | x |  |  |  |  | x |
| AG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| AIZ | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| AKAM | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| AMP | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| AMT | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  |  | x |
| APLD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| ARCC | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| ASTS | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  | ? | x |  |  | x | x |
| ATO | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x | x |  |  |  | x |
| AXP | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x |  | x |  |  |  | x |
| BAC | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| BBVA | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  |  |
| BCH | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | ? |  |  | x | x | ? | x |  |  |  |  |
| BDX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| BEPC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  | x |  |  |
| BIDU | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| BILI | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? | x |  |  |  |  |
| BMO | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| BMRN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  |  |
| BRO | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| C | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| CAR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  | x |  |  |  |  |
| CB | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| CBRS | 0 | 4 | no |  |  | ? |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| CCI | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x | x |  | x |  | x |
| CDE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| CDW | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| CFR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| CLSK | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| CM | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| CPB | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  | x |
| CPNG | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  | x |
| CRCL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| CTAS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| CWT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| DECK | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| DG | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  | x |
| DLTR | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  | x |
| DOC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| DOLE | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  | x |  | x |  |  |  |  |
| DTM | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| DYN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  |  |
| ED | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| EIX | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| ENB | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x | x |  |  |  | x |
| ERIE | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| FCNCA | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| FIBK | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | x |  |  |  |  |  |
| FIG | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| FLY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| FOUR | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| FUTU | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| FWONA | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | ? |  |  | x | x | x |  |  |  |  |  |
| FWONK | 0 | 4 | no |  |  |  |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  |  | x |
| GLPI | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x | x |  | x |  | x |
| GLXY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| GNTX | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  |  |
| GPN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  |  | x |
| HD | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  | x | x |
| HESM | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| HMN | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| HROW | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  | x |  |  |  | x |  |  |  |  |
| HSY | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  | x |
| HUT | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| IBN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| IFF | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| INBX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| INCY | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| INOD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? |  |  |  | x |  |
| IRTC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| ITRI | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  | x |
| JAZZ | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| JBTM | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| JPM | 0 | 4 | no |  |  |  |  |  |  |  |  |  |  | x |  |  | x | x | x |  |  |  | x |
| KDP | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? | x |  |  |  | x |
| KLAR | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  |  |  |  |  |  |
| KMB | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| KNSL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | x |  |  |  |  | x |
| KRYS | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | x |  |  |  |  | x |
| KTOS | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| LIVN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  |  |
| LNC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| LUNR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| MAA | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x |  | x |  |  |  | x |
| MARA | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| MCO | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  | x |
| MDGL | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x | x |  |  |  |  | x |
| MDT | 0 | 4 | no |  |  |  |  |  |  |  |  |  |  | x |  | x | x | x |  |  |  |  | x |
| MGM | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? | x |  | x |  | x |
| MNDY | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| MP | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  |  |  |  |  | x |
| NCLH | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  |  |  |  |  |  | x |
| NEE | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? |  |  |  |  | x |
| NFG | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x |  |  |  |  | x |
| NFLX | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| NHI | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  |  |
| NKE | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  | x | x | x |
| NKTR | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| NTST | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| NVO | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  | x |
| OBDC | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  |  |
| OCFC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | x |  |  |  |  |  |
| OGS | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? | x |  |  |  |  |
| OKE | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| OKLO | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| ORCL | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| OTIS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  | x |  | x |
| PCG | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  | x |  | x |
| PDD | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x | x |  |  |  | x |
| PEP | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  | x |  |  |  | x |  | x |
| PFSI | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  |  |
| PGY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| PL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| PLD | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| PLNT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  | x |
| PNC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| POR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | x |  |  |  |  | x |
| POST | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| PRI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  | x |
| PRU | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| PSN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  |  | x | x |  |  |  | x |
| QBTS | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| QCOM | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| QSR | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x |  |  | x |  | x |  |  |  | x |
| QURE | 0 | 5 | no |  |  |  |  |  |  | ? |  |  | x | x | x | x |  | ? | x |  |  |  |  |
| RCI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| RGTI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| RIOT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| RJF | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  | x |
| ROST | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| RRR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| RY | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| SA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | ? |  | x | x |  | ? | x |  |  |  |  |
| SAIC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| SAM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| SAN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| SBAC | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  |  | x |
| SEDG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  |  |
| SF | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x |  | x |  |  |  | x |
| SFM | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| SKYW | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| SLGN | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| SMG | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| SNEX | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| SNY | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| SPGI | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x |  | x |  |  |  | x |
| SR | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x | x |  |  |  |  |
| STAG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| SUPN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| SW | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| SWX | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| SYF | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  | x |
| THO | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  |  |
| TKO | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? | x |  |  |  | x |
| TMUS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| TTE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| UL | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| UPST | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  | x |  |  |  | x |
| USAR | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| UUUU | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  | x |  |  |  | x |
| UVV | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  |  | x | x |  | x |  |  |
| VICI | 0 | 5 | no |  |  |  |  |  |  |  |  | x |  | x |  |  | x | x | x |  | x |  | x |
| VKTX | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x | x |  | ? |  |  |  |  | x |
| VMRK | 0 | 4 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  | x | x | x |  |  |  | x |
| VSAT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| VSEC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| VTR | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| WDAY | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x |  |  |  | x |
| WEC | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x | x |  |  |  | x |
| WHD | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  |  |
| WLDN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| WMT | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| WPC | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  | x |  |  |  |  |
| WRBY | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  |  |
| WSO | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| WULF | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x | x |  |  | x |
| ZBH | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| ZTS | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x |  | x |  | x |  | x |

### VOL (1)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| WULF | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x | x |  |  | x |

CONFLICT (logged only, never a basket, DESIGN/110 §3): 84.

Ledger: emitted 220 (skipped 0), graded 480; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
