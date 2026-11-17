# S-A daily — 2026-11-16 (S3)

Preflight: WARN — prices.parquet ends 2026-11-13, BEFORE the 2026-11-16 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-11-13, BEFORE the 2026-11-16 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-11-13, BEFORE the 2026-11-16 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (12)
| ticker | variant | structure | expiry | k | k_up | k_dn | credit_entry | credit_net_pct | risk_usd | contracts | entry_tier_max | cap_pass |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AS | A1 | IC | 2026-11-20T00:00:00.000 | 29.00 | 35.50 | 22.50 | 2.61 | +8.46% | 388.74 | 1 | 2 | yes |
| VIK | A1 | IC | 2026-11-20T00:00:00.000 | 90.00 | 105.00 | 75.00 | 7.38 | +7.68% | 761.97 | 1 | 1 | yes |
| JD | A1 | IC | 2026-11-20T00:00:00.000 | 27.50 | 32.00 | 23.00 | 1.65 | +5.71% | 284.74 | 1 | 1 | yes |
| AS | A1 | SS | 2026-11-20T00:00:00.000 | 29.00 | — | — | 2.81 | +9.21% | 705.40 | 1 | 1 | yes |
| VIK | A1 | SS | 2026-11-20T00:00:00.000 | 90.00 | — | — | 8.08 | +8.61% | 1,679.96 | 1 | 1 | yes |
| JD | A1 | SS | 2026-11-20T00:00:00.000 | 27.50 | — | — | 1.70 | +5.98% | 515.03 | 1 | 1 | yes |
| AS | A2 | IC | 2026-11-20T00:00:00.000 | 29.00 | 35.50 | 22.50 | 2.61 | +8.46% | 388.74 | 1 | 2 | yes |
| VIK | A2 | IC | 2026-11-20T00:00:00.000 | 90.00 | 105.00 | 75.00 | 7.38 | +7.68% | 761.97 | 1 | 1 | yes |
| JD | A2 | IC | 2026-11-20T00:00:00.000 | 27.50 | 32.00 | 23.00 | 1.65 | +5.71% | 284.74 | 1 | 1 | yes |
| AS | A2 | SS | 2026-11-20T00:00:00.000 | 29.00 | — | — | 2.81 | +9.21% | 705.40 | 1 | 1 | yes |
| VIK | A2 | SS | 2026-11-20T00:00:00.000 | 90.00 | — | — | 8.08 | +8.61% | 1,679.96 | 1 | 1 | yes |
| JD | A2 | SS | 2026-11-20T00:00:00.000 | 27.50 | — | — | 1.70 | +5.98% | 515.03 | 1 | 1 | yes |

## Suppressed (56)
| ticker | variant | first_fail |
|---|---|---|
| ACM | A1 | F6 |
| ACM | A2 | F6 |
| DIS | A1 | F3 |
| DIS | A2 | F3 |
| ENR | A1 | F3 |
| ENR | A2 | F3 |
| ESLT | A1 | F5 |
| ESLT | A2 | F5 |
| FIRY | A1 | F3 |
| FIRY | A2 | F3 |
| FUBO | A1 | F2 |
| FUBO | A2 | F2 |
| GFF | A1 | F4 |
| GFF | A2 | F4 |
| GFUZ | A1 | F2 |
| GFUZ | A2 | F2 |
| HD | A1 | F3 |
| HD | A2 | F3 |
| INFQ | A1 | F2 |
| INFQ | A2 | F2 |
| KLAR | A1 | F6 |
| KLAR | A2 | F6 |
| LUXE | A1 | F3 |
| LUXE | A2 | F3 |
| MFP | A1 | F3 |
| MFP | A2 | F3 |
| MNSO | A1 | F4 |
| MNSO | A2 | F4 |
| OCSL | A1 | F3 |
| OCSL | A2 | F3 |
| OMER | A1 | F3 |
| OMER | A2 | F3 |
| ONEW | A1 | F2 |
| ONEW | A2 | F2 |
| OPRA | A1 | F3 |
| OPRA | A2 | F3 |
| PAGS | A1 | F2 |
| PAGS | A2 | F2 |
| POWL | A1 | F6 |
| POWL | A2 | F6 |
| SHAZ | A1 | F3 |
| SHAZ | A2 | F3 |
| SMWB | A1 | F2 |
| SMWB | A2 | F2 |
| SR | A1 | F4 |
| SR | A2 | F4 |
| SUPV | A1 | F2 |
| SUPV | A2 | F2 |
| TME | A1 | F2 |
| TME | A2 | F2 |
| TRAK | A1 | F2 |
| TRAK | A2 | F2 |
| WB | A1 | F2 |
| WB | A2 | F2 |
| YALA | A1 | F2 |
| YALA | A2 | F2 |

## Exploration book tonight (17; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| ACM | SS | 2026-11-20T00:00:00.000 | 72.50 | 5.66 | +7.40% | 1,427.19 | F6 |
| ACM | IC | 2026-11-20T00:00:00.000 | 72.50 | 5.27 | +6.70% | 723.41 | F6 |
| AS | SS | 2026-11-20T00:00:00.000 | 29.00 | 2.81 | +9.21% | 705.40 | PASS |
| AS | IC | 2026-11-20T00:00:00.000 | 29.00 | 2.61 | +8.46% | 388.74 | PASS |
| ENR | SS | 2026-11-20T00:00:00.000 | 25.00 | 2.13 | +6.99% | 636.02 | F3 |
| INFQ | SS | 2026-11-20T00:00:00.000 | 8.00 | 1.03 | +12.20% | 334.26 | F2 |
| INFQ | IC | 2026-11-20T00:00:00.000 | 8.00 | 0.93 | +10.74% | 206.64 | F2 |
| JD | SS | 2026-11-20T00:00:00.000 | 27.50 | 1.70 | +5.98% | 515.03 | PASS |
| JD | IC | 2026-11-20T00:00:00.000 | 27.50 | 1.65 | +5.71% | 284.74 | PASS |
| KLAR | SS | 2026-11-20T00:00:00.000 | 13.50 | 1.85 | +12.78% | 462.06 | F6 |
| KLAR | IC | 2026-11-20T00:00:00.000 | 13.50 | 1.75 | +11.83% | 274.86 | F6 |
| OMER | SS | 2026-11-20T00:00:00.000 | 17.00 | 2.62 | +14.52% | 652.57 | F3 |
| PAGS | SS | 2026-11-20T00:00:00.000 | 8.00 | 0.56 | +5.73% | 168.42 | F2 |
| POWL | SS | 2026-11-20T00:00:00.000 | 150.00 | 23.58 | +14.69% | 6,134.90 | F6 |
| TME | SS | 2026-11-20T00:00:00.000 | 9.00 | 0.75 | +7.06% | 168.81 | F2 |
| VIK | SS | 2026-11-20T00:00:00.000 | 90.00 | 8.08 | +8.61% | 1,679.96 | PASS |
| VIK | IC | 2026-11-20T00:00:00.000 | 90.00 | 7.38 | +7.68% | 761.97 | PASS |

## Graded today (4)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| BIDU | A1 | SS | champion | +1.00% | 78.46 | 1 | no |
| BIDU | A1 | SS | exploration | +1.00% | 78.46 | 1 | no |
| TSN | A1 | SS | exploration | -2.50% | -147.24 | 1 | no |
| XPEV | A1 | SS | exploration | +0.14% | 1.33 | 1 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 8 | 6 | +0.63% | 1.12 | 245.49 |
| sa-1.0 | champion | A1 | SS | 33 | 16 | -0.71% | -0.93 | -1,399.42 |
| sa-1.0 | champion | A2 | IC | 7 | 5 | +0.66% | 1.00 | 233.18 |
| sa-1.0 | champion | A2 | SS | 25 | 14 | -0.53% | -0.54 | -372.47 |
| sa-1.0 | exploration | A1 | IC | 58 | 23 | -1.11% | -1.67 | -9,252.44 |
| sa-1.0 | exploration | A1 | SS | 289 | 29 | -0.97% | -3.42 | -25,498.22 |

Ledger: emitted 12 (skipped 0), exploration 17 (skipped 0), graded 4; ledger open.

## S-B state
Gate (2026-11-16, from 2026-11-13 closes): SPY ON (VIX 19.3, VIX3M 20.62, X 19.3 vs median 18.865000000000002) · QQQ ON (VIX 19.3, VIX3M 20.62, X 29.38 vs median 27.715)

Next session (2026-11-17, from 2026-11-16 closes): SPY ON (VIX 22.91, VIX3M 23.02, X 22.91 vs median 18.865000000000002) · QQQ ON (VIX 22.91, VIX3M 23.02, X 32.9 vs median 28.4)

CBOE refresh: ok through 2026-11-16; index-vol through 2026-11-16

Entry day: no.

### S-B positions tonight (0)
_none_

### S-B graded at expiry today (0)
_none due_

Open positions: QQQ-IC 2, QQQ-PS 2, SPY-IC 1, SPY-PS 1

### S-B forward ledger to date
| policy_id | role | sleeve | n | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|---|
| sb-1.0 | champion | QQQ-IC | 5 | +1.18% | 0.35 | 243.94 |
| sb-1.0 | champion | QQQ-PS | 6 | -11.12% | -1.35 | -2,499.87 |
| sb-1.0 | champion | SPY-IC | 2 | — | — | 372.65 |
| sb-1.0 | champion | SPY-PS | 5 | +4.97% | 34.99 | 755.37 |
| sb-1.0 | exploration | QQQ-IC | 5 | +1.18% | 0.35 | 243.94 |
| sb-1.0 | exploration | QQQ-PS | 7 | -8.55% | -1.02 | -2,287.68 |
| sb-1.0 | exploration | SPY-IC | 4 | +6.91% | 31.77 | 724.42 |
| sb-1.0 | exploration | SPY-PS | 7 | +4.94% | 29.94 | 999.78 |

S-B ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0; ledger open.


## S-C state
Entry day: no; ledger open.

### S-C graded at expiry (0)
_none due_

### S-C open book (S-B open: yes; the 40% budget binds only then)
| pair | positions | open_risk_usd | budget_usd | max_sector_positions |
|---|---|---|---|---|
| C1-SS | 5 | 6,592.89 | 8,000.00 | 3 |
| C1-IB | 4 | 3,051.64 | 4,000.00 | 3 |
| C2-SS | 4 | 5,906.04 | 8,000.00 | 3 |
| C2-IB | 5 | 3,405.73 | 4,000.00 | 3 |

### S-C forward ledger to date (entry-week series)
| policy_id | role | pair | n | weeks | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|---|---|
| sc-1.0 | champion | C1-SS | 6 | 2 | — | — | -1,362.15 |
| sc-1.0 | champion | C1-IB | 6 | 2 | — | — | -1,519.19 |
| sc-1.0 | champion | C2-SS | 5 | 2 | — | — | -1,091.11 |
| sc-1.0 | champion | C2-IB | 5 | 2 | — | — | -1,236.18 |
| sc-1.0 | exploration | C1-SS | 197 | 3 | -12.29% | -3.69 | -237,221.66 |
| sc-1.0 | exploration | C1-IB | 197 | 3 | -21.29% | -3.98 | -211,937.98 |

Progress to the read: graded entry-weeks 2 of 40 (C1-SS), 2 of 40 (C1-IB), 2 of 40 (C2-SS), 2 of 40 (C2-IB)

S-C ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0.


## Watch basket (wb-1.0, exploration, paper only)
Universe: 2003 names.
Borrow snapshot: 2026-11-16 (the session's own); fee known for 1997 names.
Bull counts: 0:827, 1:692, 2:329, 3:136, 4:19, 5:0, 6:0, 7:0, 8:0
Bear counts: 0:563, 1:803, 2:432, 3:154, 4:44, 5:7, 6:0, 7:0, 8:0

### LONG (71)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ACGL | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ADP | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AFG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AIZ | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ALL | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMTB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| ASND | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| BRKB | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  | x | x |
| BUD | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CAH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CHD | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CL | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CME | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CNC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CNI | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| COST | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| CRBG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| DEO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ECL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EHC | 3 | 0 | no | x |  |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| EW | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| FTV | 4 | 0 | yes | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| GDYN | 3 | 0 | yes | x | x |  |  |  |  |  | x |  |  |  |  |  |  |  |  |  |  |  |  |
| GSAT | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| HG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| HLT | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HMN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| HST | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HUM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| HZO | 3 | 0 | no | x |  |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  |  |
| IBN | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| ICE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| J | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| KO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| KOF | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| LH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LNTH | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  |
| MA | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MCK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MDLZ | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MRSH | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MSCI | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| MSI | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PFGC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PGR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| R | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RHP | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| RLJ | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| RNR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RSG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RTO | 3 | 0 | no |  | x |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| SAFT | 3 | 0 | no | x |  |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  |  |
| SEIC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SIGI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SJM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| STE | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| STT | 3 | 0 | no |  |  | x | x |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TAK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| THG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| UVE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| V | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VLTO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VRNS | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| WAB | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WCN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WRB | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WTRG | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |

### SHORT (97)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| ADEA | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  |  |
| ADNT | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| AI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  | ? |  |  |  |  |  |
| AMAT | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| AMBA | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  |  |
| AMR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| ARWR | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  | x |  |  |
| AX | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| AXON | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| AXTI | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| BBWI | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| BDC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| BLLN | 0 | 4 | yes |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? | x |  |  |  | x |
| BRKR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| BTU | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  |  | x |  |  |  | x |
| CAMT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CAT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| CBRS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  |  |  |  |  | x | x |
| CELC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CIGI | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CLMT | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  |  |
| CMC | 0 | 4 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  | x |
| COIN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  | x | x |
| CORZ | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? |  |  |  |  | x |
| CPNG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? |  |  |  |  | x |
| CRWV | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| CYTK | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? | x |  |  |  | x |
| DLO | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| DOX | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? |  |  |  |  | x |
| DRTS | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  | x | x |  | ? | x |  |  |  |  |
| DVA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| ELVN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| ENS | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  | x |
| FIG | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| FLNG | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  | x |  |  |
| FSLY | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  |  |
| GENB | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| GLW | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| GNTX | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  |  |
| HIMS | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  | ? | x |  |  |  | x |
| HSIC | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| HTGC | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x | ? | x |  |  |  |  |
| IMAX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| IMVT | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| INOD | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  |  |  |  |
| IONS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  | x |  | x |
| IPGP | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| KNF | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| KSS | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  | x | x |  | ? |  |  |  |  |  |
| LEGN | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x | x |  | ? |  |  |  |  |  |
| LEU | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  | x |  |  |
| LIFE | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  |  |
| LINE | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| LQDA | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  | x |
| LYFT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| MATX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| MGA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| NEO | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| NOVT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| NRIX | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| NVCR | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| OKLO | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  | x |  | x |
| OMER | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| OSCR | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| OSIS | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  |  |
| PANW | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| PBI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| PCVX | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| PDD | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? |  |  |  |  | x |
| PGY | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  | x | x |  | ? |  |  |  |  |  |
| QXO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? |  |  |  |  | x |
| RARE | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| RELY | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| RH | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| RLAY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? |  |  |  |  |  |
| S | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| SA | 0 | 4 | yes |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? |  |  |  |  |  |
| SEDG | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| SGI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? |  |  |  |  | x |
| SLG | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| SPB | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| SRPT | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  |  |
| STRA | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  |  |
| SYM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| TTD | 0 | 4 | yes |  |  |  |  |  |  |  |  | x | x | x | x |  |  | ? |  |  |  |  | x |
| UFPT | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| UMH | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? |  |  |  |  |  |
| UPST | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  | x |  | x |
| URGN | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  | x |  |  |  | x |  |  |  | x |
| VKTX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  |  |  |  |  |  | x |
| VSAT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| WABC | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| WHR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| WSO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| WULF | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| YPF | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  |  |

### VOL (0)
_none_

CONFLICT (logged only, never a basket, DESIGN/110 §3): 95.

Ledger: emitted 168 (skipped 0), graded 503; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
