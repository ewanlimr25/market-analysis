# S-A daily — 2026-11-24 (S3)

Preflight: WARN — prices.parquet ends 2026-11-20, BEFORE the 2026-11-24 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-11-20, BEFORE the 2026-11-24 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-11-20, BEFORE the 2026-11-24 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (0)
_no event tonight clears the filters._

## Suppressed (28)
| ticker | variant | first_fail |
|---|---|---|
| ADSK | A1 | F3 |
| ADSK | A2 | F3 |
| AMBA | A1 | F3 |
| AMBA | A2 | F3 |
| BBAR | A1 | F2 |
| BBAR | A2 | F2 |
| BZ | A1 | F5 |
| BZ | A2 | F5 |
| DE | A1 | F3 |
| DE | A2 | F3 |
| DELL | A1 | F3 |
| DELL | A2 | F3 |
| GASS | A1 | F2 |
| GASS | A2 | F2 |
| GDS | A1 | F6 |
| GDS | A2 | F6 |
| HPQ | A1 | F6 |
| HPQ | A2 | F6 |
| LI | A1 | F4 |
| LI | A2 | F4 |
| NOAH | A1 | F2 |
| NOAH | A2 | F2 |
| NTNX | A1 | F6 |
| NTNX | A2 | F6 |
| URBN | A1 | F6 |
| URBN | A2 | F6 |
| WDAY | A1 | F6 |
| WDAY | A2 | F6 |

## Exploration book tonight (10; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| ADSK | SS | 2026-11-27T00:00:00.000 | 255.00 | 20.30 | +7.26% | 5,804.46 | F3 |
| DELL | SS | 2026-11-27T00:00:00.000 | 295.00 | 39.16 | +13.24% | 13,373.88 | F3 |
| DELL | IC | 2026-11-27T00:00:00.000 | 295.00 | 38.58 | +13.02% | 7,642.49 | F3 |
| GDS | SS | 2026-12-18T00:00:00.000 | 14.00 | 3.00 | +20.58% | 491.21 | F6 |
| HPQ | SS | 2026-11-27T00:00:00.000 | 28.00 | 2.73 | +9.31% | 757.19 | F6 |
| HPQ | IC | 2026-11-27T00:00:00.000 | 28.00 | 2.64 | +8.79% | 435.90 | F6 |
| LI | SS | 2026-11-27T00:00:00.000 | 10.50 | 0.70 | +5.75% | 253.88 | F4 |
| NTNX | SS | 2026-12-18T00:00:00.000 | 55.00 | 7.92 | +13.66% | 1,272.38 | F6 |
| URBN | SS | 2026-11-27T00:00:00.000 | 86.00 | 9.09 | +8.92% | 2,199.74 | F6 |
| WDAY | SS | 2026-11-27T00:00:00.000 | 180.00 | 17.52 | +8.96% | 4,913.55 | F6 |

## Graded today (14)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| BBY | A1 | SS | champion | +3.22% | 312.59 | 1 | no |
| BBY | A2 | SS | champion | +3.22% | 312.59 | 1 | no |
| A | A1 | SS | exploration | -1.57% | -276.42 | 1 | no |
| BBY | A1 | SS | exploration | +3.22% | 312.59 | 1 | no |
| BILI | A1 | SS | exploration | +1.43% | 15.57 | 1 | no |
| BURL | A1 | SS | exploration | -0.75% | -177.43 | 1 | no |
| DKS | A1 | SS | exploration | -5.64% | -752.92 | 1 | no |
| DLTR | A1 | SS | exploration | -4.54% | -631.65 | 1 | no |
| HPE | A1 | SS | exploration | -3.54% | -170.42 | 1 | no |
| KSS | A1 | SS | exploration | -2.75% | -58.20 | 1 | no |
| SMTC | A1 | SS | exploration | -2.54% | -264.18 | 1 | no |
| SYM | A1 | SS | exploration | +2.89% | 101.17 | 1 | no |
| ZM | A1 | SS | exploration | +1.53% | 131.63 | 1 | no |
| ZM | A1 | IC | exploration | +1.19% | 102.87 | 1 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 10 | 7 | +0.68% | 1.50 | 440.76 |
| sa-1.0 | champion | A1 | SS | 38 | 19 | -0.50% | -0.73 | -788.13 |
| sa-1.0 | champion | A2 | IC | 9 | 6 | +0.71% | 1.38 | 428.45 |
| sa-1.0 | champion | A2 | SS | 30 | 17 | -0.29% | -0.34 | 238.82 |
| sa-1.0 | exploration | A1 | IC | 66 | 28 | -0.97% | -1.66 | -9,071.99 |
| sa-1.0 | exploration | A1 | SS | 328 | 34 | -0.91% | -3.59 | -26,120.19 |

Ledger: emitted 0 (skipped 0), exploration 10 (skipped 0), graded 14; ledger open.

## S-B state
Gate (2026-11-24, from 2026-11-23 closes): SPY OFF:G1 (VIX 26.62, VIX3M 25.5, X 26.62 vs median 19.69) · QQQ OFF:G1 (VIX 26.62, VIX3M 25.5, X 36.31 vs median 29.174999999999997)

Next session (2026-11-25, from 2026-11-24 closes): SPY UNKNOWN:null input at 2026-11-24 · QQQ UNKNOWN:null input at 2026-11-24

CBOE refresh: ok through 2026-11-24; index-vol through 2026-11-24

Entry day: no.

### S-B positions tonight (0)
_none_

### S-B graded at expiry today (0)
_none due_

Open positions: QQQ-IC 1, QQQ-PS 1

### S-B forward ledger to date
| policy_id | role | sleeve | n | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|---|
| sb-1.0 | champion | QQQ-IC | 6 | -10.73% | -1.11 | -2,892.74 |
| sb-1.0 | champion | QQQ-PS | 7 | -19.70% | -2.35 | -5,790.26 |
| sb-1.0 | champion | SPY-IC | 3 | -23.56% | -1.24 | -2,411.03 |
| sb-1.0 | champion | SPY-PS | 6 | -10.15% | -0.77 | -2,087.28 |
| sb-1.0 | exploration | QQQ-IC | 6 | -10.73% | -1.11 | -2,892.74 |
| sb-1.0 | exploration | QQQ-PS | 8 | -16.37% | -1.83 | -5,578.07 |
| sb-1.0 | exploration | SPY-IC | 5 | -11.58% | -0.75 | -2,059.26 |
| sb-1.0 | exploration | SPY-PS | 8 | -6.39% | -0.62 | -1,842.87 |

S-B ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0; ledger open.


## S-C state
Entry day: no; ledger open.

### S-C graded at expiry (0)
_none due_

### S-C open book (S-B open: yes; the 40% budget binds only then)
| pair | positions | open_risk_usd | budget_usd | max_sector_positions |
|---|---|---|---|---|
| C1-SS | 5 | 7,539.38 | 8,000.00 | 2 |
| C1-IB | 5 | 3,846.94 | 4,000.00 | 2 |
| C2-SS | 4 | 6,172.04 | 8,000.00 | 2 |
| C2-IB | 4 | 3,034.11 | 4,000.00 | 2 |

### S-C forward ledger to date (entry-week series)
| policy_id | role | pair | n | weeks | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|---|---|
| sc-1.0 | champion | C1-SS | 9 | 4 | -15.22% | -2.49 | -2,831.23 |
| sc-1.0 | champion | C1-IB | 9 | 4 | -29.08% | -2.64 | -3,081.53 |
| sc-1.0 | champion | C2-SS | 8 | 4 | -14.26% | -2.46 | -2,560.19 |
| sc-1.0 | champion | C2-IB | 8 | 4 | -27.55% | -2.62 | -2,798.52 |
| sc-1.0 | exploration | C1-SS | 500 | 5 | -20.16% | -15.31 | -653,580.75 |
| sc-1.0 | exploration | C1-IB | 496 | 5 | -30.88% | -23.29 | -533,174.58 |

Progress to the read: graded entry-weeks 4 of 40 (C1-SS), 4 of 40 (C1-IB), 4 of 40 (C2-SS), 4 of 40 (C2-IB)

S-C ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0.


## Watch basket (wb-1.0, exploration, paper only)
Universe: 1952 names.
Borrow snapshot: 2026-11-24 (the session's own); fee known for 1944 names.
Bull counts: 0:748, 1:724, 2:382, 3:87, 4:10, 5:1, 6:0, 7:0, 8:0
Bear counts: 0:488, 1:762, 2:453, 3:189, 4:53, 5:7, 6:0, 7:0, 8:0

### LONG (42)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ALGN | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ALL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| APPN | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ASND | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CRH | 3 | 0 | yes |  | x |  |  | x | x |  |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| CSGP | 3 | 0 | yes |  |  | x |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CUBE | 4 | 0 | no | x | x |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| DIS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| DOC | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DV | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| EG | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| EPRT | 4 | 0 | no |  | x |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| EXLS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| GFF | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| GILD | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| GSAT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| IR | 4 | 0 | no |  | x |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| JOYY | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| LH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| LNTH | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| MHO | 3 | 0 | yes |  |  | x |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MLM | 3 | 0 | yes |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| NATL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| ONC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RPRX | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RYAAY | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| SIGI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| SKY | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| STE | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| STRC | 3 | 0 | yes | x | x |  |  | x |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| TAK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TOL | 3 | 0 | no |  | x |  |  | x | x |  |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| TSN | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VLTO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VRNS | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| VZ | 3 | 0 | no | x |  |  |  | x |  |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| WDFC | 3 | 0 | no |  | x |  |  | x | x |  |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| WM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WMT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| WRB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| YUMC | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ZBH | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |

### SHORT (89)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AA | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| AAOI | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| AFRM | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| AG | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| AKAM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| ALAB | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| ALB | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? |  |  |  |  | x |
| AMD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| AMZN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  | x | x |
| APLD | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  | x |  | x |
| AUPH | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| AVGO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  | x | x |
| AX | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| BE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| BMA | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  |  | x |  | x |  |  |
| BPRE | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  |  |
| BRKR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| BXSL | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| CELH | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  | x |  | ? | x |  |  |  |  |
| CIGI | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CLF | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| CNX | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| COIN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  | x | x | x |
| CVNA | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x |  | x |  | ? |  |  |  |  | x |
| DLB | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x | ? |  |  |  |  |  |
| DUOL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| ELV | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| ENS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  | x |
| EOG | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| FLUT | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  | x |  | x |
| FLY | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| FRSH | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  |  |
| GDS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  |  |
| GLNG | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| GS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  | x | x |
| HCC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| HL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| HOOD | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| HPQ | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| HUT | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| HYMC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| IIPR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? |  |  |  |  |  |
| IMO | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| INGR | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? |  |  |  |  |  |
| INSP | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| IONQ | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| IREN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  | x | x |
| LMND | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  |  |
| LYFT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| META | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| MFC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| MP | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  |  | x |
| MTDR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  |  |
| NE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| NOG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| NOW | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  | x | x |
| NVCR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| NYT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? |  |  |  |  | x |
| OSIS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| OXY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| PAGP | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  | x | ? | x |  |  |  | x |
| PFG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| POWI | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| PRK | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| RHI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| ROAD | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| SAH | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| SG | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  |  |  |
| SMCI | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| SPCX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| STAA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| STRF | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? |  |  |  |  |  |
| STWD | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  | x |  |  |
| TRGP | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| TTAM | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| UGI | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| UNP | 0 | 4 | yes |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? | x |  |  |  | x |
| VECO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| VG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  |  |
| VVX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| WAL | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? |  |  |  |  |  |
| WDAY | 0 | 5 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  | x | ? | x |  |  |  | x |
| WGS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| WLY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| WRBY | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x | x |  | ? |  |  |  |  | x |
| WSM | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| WSO | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| ZTO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |

### VOL (0)
_none_

CONFLICT (logged only, never a basket, DESIGN/110 §3): 134.

Ledger: emitted 131 (skipped 0), graded 559; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
