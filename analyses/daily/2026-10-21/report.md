# S-A daily — 2026-10-21 (S3)

Preflight: WARN — prices.parquet ends 2026-10-16, BEFORE the 2026-10-21 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-10-16, BEFORE the 2026-10-21 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-10-16, BEFORE the 2026-10-21 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (2)
| ticker | variant | structure | expiry | k | k_up | k_dn | credit_entry | credit_net_pct | risk_usd | contracts | entry_tier_max | cap_pass |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LUV | A1 | SS | 2026-10-23T00:00:00.000 | 40.00 | — | — | 2.28 | +5.44% | 801.18 | 1 | 1 | yes |
| LUV | A2 | SS | 2026-10-23T00:00:00.000 | 40.00 | — | — | 2.28 | +5.44% | 801.18 | 1 | 1 | yes |

## Suppressed (218)
| ticker | variant | first_fail |
|---|---|---|
| AAL | A1 | F6 |
| AAL | A2 | F6 |
| ALLE | A1 | F5 |
| ALLE | A2 | F5 |
| AMAL | A1 | F3 |
| AMAL | A2 | F3 |
| ARGX | A1 | F3 |
| ARGX | A2 | F3 |
| BANR | A1 | F4 |
| BANR | A2 | F4 |
| BBT | A1 | F4 |
| BBT | A2 | F4 |
| BCS | A1 | F3 |
| BCS | A2 | F3 |
| BFH | A1 | F5 |
| BFH | A2 | F5 |
| BMI | A1 | F5 |
| BMI | A2 | F5 |
| BPOP | A1 | F5 |
| BPOP | A2 | F5 |
| BX | A1 | F3 |
| BX | A2 | F3 |
| CACI | A1 | F5 |
| CACI | A2 | F5 |
| CASH | A1 | F3 |
| CASH | A2 | F3 |
| CATY | A1 | F4 |
| CATY | A2 | F4 |
| CBRE | A1 | F5 |
| CBRE | A2 | F5 |
| CCI | A1 | F6 |
| CCI | A2 | F6 |
| CIVB | A1 | F3 |
| CIVB | A2 | F3 |
| CMCSA | A1 | F3 |
| CMCSA | A2 | F3 |
| CNOB | A1 | F3 |
| CNOB | A2 | F3 |
| COCO | A1 | F5 |
| COCO | A2 | F5 |
| CRS | A1 | F5 |
| CRS | A2 | F5 |
| CSX | A1 | F3 |
| CSX | A2 | F3 |
| CURB | A1 | F4 |
| CURB | A2 | F4 |
| CVBF | A1 | F4 |
| CVBF | A2 | F4 |
| DGX | A1 | F5 |
| DGX | A2 | F5 |
| DOV | A1 | F5 |
| DOV | A2 | F5 |
| DOW | A1 | F6 |
| DOW | A2 | F6 |
| EFSC | A1 | F4 |
| EFSC | A2 | F4 |
| EGBN | A1 | F3 |
| EGBN | A2 | F3 |
| EGP | A1 | F5 |
| EGP | A2 | F5 |
| EPRT | A1 | F5 |
| EPRT | A2 | F5 |
| ESI | A1 | F5 |
| ESI | A2 | F5 |
| FAF | A1 | F5 |
| FAF | A2 | F5 |
| FBP | A1 | F4 |
| FBP | A2 | F4 |
| FR | A1 | F5 |
| FR | A2 | F5 |
| FRME | A1 | F4 |
| FRME | A2 | F4 |
| FSV | A1 | F4 |
| FSV | A2 | F4 |
| FULT | A1 | F4 |
| FULT | A2 | F4 |
| GGG | A1 | F5 |
| GGG | A2 | F5 |
| GL | A1 | F5 |
| GL | A2 | F5 |
| GSBC | A1 | F3 |
| GSBC | A2 | F3 |
| GTY | A1 | F3 |
| GTY | A2 | F3 |
| HBAN | A1 | F5 |
| HBAN | A2 | F5 |
| HBNC | A1 | F3 |
| HBNC | A2 | F3 |
| HFWA | A1 | F3 |
| HFWA | A2 | F3 |
| HON | A1 | F3 |
| HON | A2 | F3 |
| HXL | A1 | F5 |
| HXL | A2 | F5 |
| IBM | A1 | F3 |
| IBM | A2 | F3 |
| IIIN | A1 | F3 |
| IIIN | A2 | F3 |
| KALU | A1 | F4 |
| KALU | A2 | F4 |
| KMI | A1 | F3 |
| KMI | A2 | F3 |
| KNX | A1 | F5 |
| KNX | A2 | F5 |
| KRNY | A1 | F2 |
| KRNY | A2 | F2 |
| LAZ | A1 | F5 |
| LAZ | A2 | F5 |
| LBRT | A1 | F5 |
| LBRT | A2 | F5 |
| LMT | A1 | F3 |
| LMT | A2 | F3 |
| LNN | A1 | F3 |
| LNN | A2 | F3 |
| LOB | A1 | F3 |
| LOB | A2 | F3 |
| LRCX | A1 | F3 |
| LRCX | A2 | F3 |
| LVS | A1 | F6 |
| LVS | A2 | F6 |
| MEDP | A1 | F5 |
| MEDP | A2 | F5 |
| META | A1 | F3 |
| META | A2 | F3 |
| MOH | A1 | F5 |
| MOH | A2 | F5 |
| MSM | A1 | F5 |
| MSM | A2 | F5 |
| NDAQ | A1 | F3 |
| NDAQ | A2 | F3 |
| NOK | A1 | F2 |
| NOK | A2 | F2 |
| NSC | A1 | F3 |
| NSC | A2 | F3 |
| NTST | A1 | F3 |
| NTST | A2 | F3 |
| OII | A1 | F4 |
| OII | A2 | F4 |
| ORI | A1 | F5 |
| ORI | A2 | F5 |
| OSBC | A1 | F3 |
| OSBC | A2 | F3 |
| PCG | A1 | F6 |
| PCG | A2 | F6 |
| PG | A1 | F3 |
| PG | A2 | F3 |
| PHM | A1 | F5 |
| PHM | A2 | F5 |
| PKG | A1 | F5 |
| PKG | A2 | F5 |
| PNFP | A1 | F5 |
| PNFP | A2 | F5 |
| POOL | A1 | F5 |
| POOL | A2 | F5 |
| R | A1 | F5 |
| R | A2 | F5 |
| ROL | A1 | F5 |
| ROL | A2 | F5 |
| ROP | A1 | F5 |
| ROP | A2 | F5 |
| RS | A1 | F5 |
| RS | A2 | F5 |
| SAP | A1 | F3 |
| SAP | A2 | F3 |
| SEIC | A1 | F5 |
| SEIC | A2 | F5 |
| SLG | A1 | F4 |
| SLG | A2 | F4 |
| SNA | A1 | F5 |
| SNA | A2 | F5 |
| SON | A1 | F5 |
| SON | A2 | F5 |
| SPOT | A1 | F3 |
| SPOT | A2 | F3 |
| SSB | A1 | F5 |
| SSB | A2 | F5 |
| STBA | A1 | F3 |
| STBA | A2 | F3 |
| STC | A1 | F3 |
| STC | A2 | F3 |
| TCBI | A1 | F5 |
| TCBI | A2 | F5 |
| TCBX | A1 | F3 |
| TCBX | A2 | F3 |
| TFIN | A1 | F3 |
| TFIN | A2 | F3 |
| THRM | A1 | F3 |
| THRM | A2 | F3 |
| TRST | A1 | F3 |
| TRST | A2 | F3 |
| TSCO | A1 | F6 |
| TSCO | A2 | F6 |
| TSLA | A1 | F3 |
| TSLA | A2 | F3 |
| TTMI | A1 | F5 |
| TTMI | A2 | F5 |
| TXN | A1 | F3 |
| TXN | A2 | F3 |
| UNP | A1 | F3 |
| UNP | A2 | F3 |
| URI | A1 | F3 |
| URI | A2 | F3 |
| VC | A1 | F4 |
| VC | A2 | F4 |
| VLO | A1 | F3 |
| VLO | A2 | F3 |
| VLY | A1 | F5 |
| VLY | A2 | F5 |
| WCN | A1 | F6 |
| WCN | A2 | F6 |
| WDFC | A1 | F4 |
| WDFC | A2 | F4 |
| WH | A1 | F5 |
| WH | A2 | F5 |
| WSBC | A1 | F4 |
| WSBC | A2 | F4 |
| ZGN | A1 | F4 |
| ZGN | A2 | F4 |

## Exploration book tonight (17; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| AAL | SS | 2026-10-23T00:00:00.000 | 12.00 | 0.74 | +5.59% | 296.33 | F6 |
| BX | SS | 2026-10-23T00:00:00.000 | 110.00 | 4.54 | +3.99% | 2,079.52 | F3 |
| CCI | SS | 2026-11-20T00:00:00.000 | 80.00 | 6.51 | +7.82% | 981.81 | F6 |
| CCI | IC | 2026-11-20T00:00:00.000 | 80.00 | 5.87 | +6.89% | 662.58 | F6 |
| CMCSA | SS | 2026-10-23T00:00:00.000 | 22.00 | 1.39 | +6.05% | 344.20 | F3 |
| CMCSA | IC | 2026-10-23T00:00:00.000 | 22.00 | 1.34 | +5.66% | 216.02 | F3 |
| CSX | SS | 2026-10-23T00:00:00.000 | 48.50 | 2.26 | +4.30% | 571.05 | F3 |
| DOW | SS | 2026-10-23T00:00:00.000 | 30.50 | 1.67 | +5.06% | 562.91 | F6 |
| HON | SS | 2026-10-23T00:00:00.000 | 215.00 | 11.04 | +4.78% | 3,080.72 | F3 |
| KMI | SS | 2026-10-23T00:00:00.000 | 34.00 | 1.11 | +3.09% | 449.90 | F3 |
| LUV | SS | 2026-10-23T00:00:00.000 | 40.00 | 2.28 | +5.44% | 801.18 | PASS |
| LVS | SS | 2026-10-23T00:00:00.000 | 37.50 | 2.15 | +5.37% | 718.48 | F6 |
| NDAQ | SS | 2026-10-23T00:00:00.000 | 96.00 | 3.60 | +3.41% | 1,227.18 | F3 |
| PCG | SS | 2026-10-23T00:00:00.000 | 13.00 | 0.48 | +3.27% | 327.07 | F6 |
| TSCO | SS | 2026-10-23T00:00:00.000 | 32.50 | 2.27 | +6.19% | 587.97 | F6 |
| TSCO | IC | 2026-10-23T00:00:00.000 | 32.50 | 2.16 | +5.76% | 334.13 | F6 |
| WCN | SS | 2026-11-20T00:00:00.000 | 170.00 | 10.58 | +5.61% | 1,772.90 | F6 |

## Graded today (6)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| UAL | A1 | SS | champion | +0.61% | 60.13 | 1 | no |
| UAL | A2 | SS | champion | +0.61% | 60.13 | 1 | no |
| ALK | A1 | SS | exploration | -1.01% | -34.95 | 1 | no |
| ALK | A1 | IC | exploration | -2.24% | -77.31 | 2 | no |
| NLY | A1 | SS | exploration | -0.48% | -8.86 | 1 | no |
| UAL | A1 | SS | exploration | +0.61% | 60.13 | 1 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 2 | 2 | +2.69% | 3.42 | 232.76 |
| sa-1.0 | champion | A1 | SS | 8 | 5 | +0.39% | 0.37 | 252.16 |
| sa-1.0 | champion | A2 | IC | 2 | 2 | +2.69% | 3.42 | 232.76 |
| sa-1.0 | champion | A2 | SS | 8 | 5 | +0.39% | 0.37 | 252.16 |
| sa-1.0 | exploration | A1 | IC | 13 | 10 | -0.93% | -1.40 | -1,595.26 |
| sa-1.0 | exploration | A1 | SS | 33 | 12 | -0.26% | -0.76 | -699.55 |

Ledger: emitted 2 (skipped 0), exploration 17 (skipped 0), graded 6; ledger open.

## S-B state
Gate (2026-10-21, from 2026-10-20 closes): SPY ON (VIX 17.31, VIX3M 18.99, X 17.31 vs median 15.465) · QQQ ON (VIX 17.31, VIX3M 18.99, X 25.22 vs median 21.47)

Next session (2026-10-22, from 2026-10-21 closes): SPY UNKNOWN:null input at 2026-10-21 · QQQ UNKNOWN:null input at 2026-10-21

CBOE refresh: ok through 2026-10-21; index-vol through 2026-10-21

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
Universe: 1999 names.
Borrow snapshot: 2026-10-21 (the session's own); fee known for 1993 names.
Bull counts: 0:768, 1:732, 2:369, 3:105, 4:24, 5:1, 6:0, 7:0, 8:0
Bear counts: 0:797, 1:715, 2:329, 3:124, 4:31, 5:3, 6:0, 7:0, 8:0

### LONG (81)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ABM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| ACA | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| ALKT | 3 | 0 | yes |  | x | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| ALRM | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| AMG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMGN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMRX | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| APPN | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| ASB | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ASND | 3 | 0 | no |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| ATMU | 3 | 0 | yes |  | x | x | x |  |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| AVPT | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| AVTR | 4 | 0 | yes | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AWI | 3 | 0 | no |  |  |  | x | x |  | x |  |  |  |  |  |  |  |  |  |  |  |  |  |
| BBY | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| BP | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| BRKB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  | x | x |
| CAH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CBLL | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| CBZ | 3 | 0 | yes | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| CFG | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CHT | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| CNK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CON | 3 | 0 | no | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| CUBI | 4 | 0 | no |  | x |  | x | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DRH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DT | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| E | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| EBAY | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  | x | x |
| ECPG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| EFSC | 3 | 0 | no |  |  |  | x | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| EG | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| EMR | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ENVA | 3 | 0 | no |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| FIZZ | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| GIC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HG | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HLT | 4 | 0 | no | x | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| HRTG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HST | 5 | 0 | no | x | x |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| ILMN | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| JOE | 3 | 0 | no |  |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| JOYY | 4 | 0 | no | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| KNTK | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LXP | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| MAR | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| MAS | 3 | 0 | yes |  | x |  |  | x | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| MD | 4 | 0 | no | x | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| MQ | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  |
| MTD | 3 | 0 | no | x |  |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| NHC | 4 | 0 | no | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| NSSC | 4 | 0 | yes |  | x |  | x | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| NWE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| NWSA | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| PNFP | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PRSU | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PSN | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| RGA | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| RLJ | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| RPRX | 3 | 0 | no | x |  |  | x |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| RS | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RSG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| SN | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| SPNT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| SSL | 3 | 0 | no | x |  |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| SSNC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| SU | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| SXT | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| TAC | 3 | 0 | no |  |  |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| TALO | 3 | 0 | no | x |  |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| TEO | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TTC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| TW | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| UCB | 3 | 0 | no |  |  |  | x | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| USPH | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| VEON | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| VIV | 3 | 0 | yes |  |  |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| WMT | 3 | 0 | no |  | x |  |  | x | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| WOR | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| WSM | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| ZION | 4 | 0 | no |  | x |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |

### SHORT (70)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AA | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| AAOI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| ALB | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  | x |
| ALGT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  |  | x |  |  |  |  |
| ALK | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  |  | x |  |  |  | x |
| ARM | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| ASTS | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  | x | x |
| ATHM | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| AVAV | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| BHP | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| BKNG | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| CC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CDE | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  | x |
| CELH | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  |  |  |  |  |  | x |
| CHTR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  |  |  |  |  |  | x |
| CMG | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| CSWC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| CURB | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| CVNA | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| DAL | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| DELL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| DRS | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  |  |  |  | x | x |  |  |  |  |
| DUOL | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? | x |  |  |  | x |
| ELAN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| FLNG | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| FLS | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  | x |
| FSK | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  |  |
| GLNG | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  | x | ? | x |  |  |  |  |
| GME | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  | x |  |  | x |
| GNTX | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x |  |  |  |  |  | x |
| GPGI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| HIMS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| HL | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  | x |
| INSM | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| IONQ | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| ITRI | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| JBS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  |  |
| KOD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  |  |  |
| KTOS | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| LEU | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  | x |  | x |
| LUNR | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  |  |
| MAIN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| MAT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| META | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| MOS | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| MP | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  |  |  |  |  | x |
| NVAX | 0 | 5 | no |  |  |  |  |  |  | ? |  |  | x | x | x | x |  | ? | x |  |  |  |  |
| OKLO | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  | x |
| OSIS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| PL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| POST | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| PRCT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| QURE | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  |  |
| QXO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| RIO | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| SHAK | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| SHC | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| SIRI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  |  |
| SKHY | 0 | 3 | no |  |  | ? |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  | x | x |
| SLS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| SNDX | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| STEP | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| STRD | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  | x |  | x | x |  |  |  |  |
| THO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| TRIN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| TSCO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| VICI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| WHR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  |  |  | x |  | x |
| WLDN | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| XE | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  | x |  | x |

### VOL (2)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CLF | 0 | 2 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? |  | x |  |  | x |
| GME | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  | x |  |  | x |

CONFLICT (logged only, never a basket, DESIGN/110 §3): 76.

Ledger: emitted 153 (skipped 0), graded 529; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
