# S-A daily — 2026-10-26 (S3)

Preflight: WARN — prices.parquet ends 2026-10-23, BEFORE the 2026-10-26 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-10-23, BEFORE the 2026-10-26 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-10-23, BEFORE the 2026-10-26 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (12)
| ticker | variant | structure | expiry | k | k_up | k_dn | credit_entry | credit_net_pct | risk_usd | contracts | entry_tier_max | cap_pass |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SOFI | A1 | IC | 2026-10-30T00:00:00.000 | 14.50 | 18.00 | 11.00 | 1.26 | +8.38% | 448.32 | 2 | 1 | yes |
| PYPL | A1 | IC | 2026-10-30T00:00:00.000 | 55.00 | 65.00 | 45.00 | 4.21 | +7.40% | 578.77 | 1 | 1 | yes |
| CNC | A1 | IC | 2026-10-30T00:00:00.000 | 68.00 | 81.00 | 55.00 | 5.00 | +6.91% | 800.20 | 1 | 1 | no |
| SOFI | A1 | SS | 2026-10-30T00:00:00.000 | 14.50 | — | — | 1.31 | +8.89% | 743.66 | 2 | 1 | yes |
| PYPL | A1 | SS | 2026-10-30T00:00:00.000 | 55.00 | — | — | 4.42 | +7.82% | 1,058.42 | 1 | 1 | yes |
| CNC | A1 | SS | 2026-10-30T00:00:00.000 | 68.00 | — | — | 5.18 | +7.29% | 1,500.71 | 1 | 1 | no |
| SOFI | A2 | IC | 2026-10-30T00:00:00.000 | 14.50 | 18.00 | 11.00 | 1.26 | +8.38% | 448.32 | 2 | 1 | yes |
| PYPL | A2 | IC | 2026-10-30T00:00:00.000 | 55.00 | 65.00 | 45.00 | 4.21 | +7.40% | 578.77 | 1 | 1 | yes |
| CNC | A2 | IC | 2026-10-30T00:00:00.000 | 68.00 | 81.00 | 55.00 | 5.00 | +6.91% | 800.20 | 1 | 1 | no |
| SOFI | A2 | SS | 2026-10-30T00:00:00.000 | 14.50 | — | — | 1.31 | +8.89% | 743.66 | 2 | 1 | yes |
| PYPL | A2 | SS | 2026-10-30T00:00:00.000 | 55.00 | — | — | 4.42 | +7.82% | 1,058.42 | 1 | 1 | yes |
| CNC | A2 | SS | 2026-10-30T00:00:00.000 | 68.00 | — | — | 5.18 | +7.29% | 1,500.71 | 1 | 1 | no |

## Suppressed (164)
| ticker | variant | first_fail |
|---|---|---|
| ABG | A1 | F4 |
| ABG | A2 | F4 |
| AEYE | A1 | F2 |
| AEYE | A2 | F2 |
| AGYS | A1 | F4 |
| AGYS | A2 | F4 |
| AIT | A1 | F5 |
| AIT | A2 | F5 |
| AMKR | A1 | F7 |
| AMKR | A2 | F7 |
| AMT | A1 | F3 |
| AMT | A2 | F3 |
| ARCC | A1 | F5 |
| ARCC | A2 | F5 |
| ARE | A1 | F5 |
| ARE | A2 | F5 |
| AWI | A1 | F5 |
| AWI | A2 | F5 |
| BA | A1 | F3 |
| BA | A2 | F3 |
| BLX | A1 | F3 |
| BLX | A2 | F3 |
| BRO | A1 | F6 |
| BRO | A2 | F6 |
| BRX | A1 | F5 |
| BRX | A2 | F5 |
| CAC | A1 | F3 |
| CAC | A2 | F3 |
| CBC | A1 | F4 |
| CBC | A2 | F4 |
| CBU | A1 | F4 |
| CBU | A2 | F4 |
| CDNS | A1 | F3 |
| CDNS | A2 | F3 |
| CINF | A1 | F5 |
| CINF | A2 | F5 |
| CLS | A1 | F6 |
| CLS | A2 | F6 |
| CLW | A1 | F3 |
| CLW | A2 | F3 |
| CMS | A1 | F5 |
| CMS | A2 | F5 |
| CNP | A1 | F5 |
| CNP | A2 | F5 |
| CTOS | A1 | F2 |
| CTOS | A2 | F2 |
| CTS | A1 | F3 |
| CTS | A2 | F3 |
| CVLT | A1 | F5 |
| CVLT | A2 | F5 |
| DORM | A1 | F4 |
| DORM | A2 | F4 |
| DQ | A1 | F3 |
| DQ | A2 | F3 |
| ECL | A1 | F3 |
| ECL | A2 | F3 |
| EEFT | A1 | F4 |
| EEFT | A2 | F4 |
| FCX | A1 | F3 |
| FCX | A2 | F3 |
| FSBC | A1 | F3 |
| FSBC | A2 | F3 |
| GBX | A1 | F3 |
| GBX | A2 | F3 |
| GLW | A1 | F3 |
| GLW | A2 | F3 |
| GLXY | A1 | F7 |
| GLXY | A2 | F7 |
| HCA | A1 | F3 |
| HCA | A2 | F3 |
| HIG | A1 | F5 |
| HIG | A2 | F5 |
| HLT | A1 | F3 |
| HLT | A2 | F3 |
| HRI | A1 | F5 |
| HRI | A2 | F5 |
| HTO | A1 | F4 |
| HTO | A2 | F4 |
| HUBB | A1 | F5 |
| HUBB | A2 | F5 |
| HWKN | A1 | F4 |
| HWKN | A2 | F4 |
| IBCP | A1 | F3 |
| IBCP | A2 | F3 |
| INIO | A1 | F5 |
| INIO | A2 | F5 |
| IQV | A1 | F6 |
| IQV | A2 | F6 |
| ITRI | A1 | F5 |
| ITRI | A2 | F5 |
| ITW | A1 | F3 |
| ITW | A2 | F3 |
| IVZ | A1 | F6 |
| IVZ | A2 | F6 |
| JCI | A1 | F3 |
| JCI | A2 | F3 |
| KFRC | A1 | F3 |
| KFRC | A2 | F3 |
| KO | A1 | F3 |
| KO | A2 | F3 |
| KOF | A1 | F4 |
| KOF | A2 | F4 |
| LECO | A1 | F5 |
| LECO | A2 | F5 |
| MRP | A1 | F5 |
| MRP | A2 | F5 |
| NE | A1 | F5 |
| NE | A2 | F5 |
| NUE | A1 | F3 |
| NUE | A2 | F3 |
| NVS | A1 | F3 |
| NVS | A2 | F3 |
| NWBI | A1 | F4 |
| NWBI | A2 | F4 |
| PCAR | A1 | F3 |
| PCAR | A2 | F3 |
| PDM | A1 | F2 |
| PDM | A2 | F2 |
| PECO | A1 | F5 |
| PECO | A2 | F5 |
| PFG | A1 | F5 |
| PFG | A2 | F5 |
| PII | A1 | F4 |
| PII | A2 | F4 |
| PNR | A1 | F5 |
| PNR | A2 | F5 |
| PSA | A1 | F3 |
| PSA | A2 | F3 |
| PSMT | A1 | F4 |
| PSMT | A2 | F4 |
| RCL | A1 | F3 |
| RCL | A2 | F3 |
| RGEN | A1 | F5 |
| RGEN | A2 | F5 |
| RMBS | A1 | F6 |
| RMBS | A2 | F6 |
| SFD | A1 | F4 |
| SFD | A2 | F4 |
| SHW | A1 | F3 |
| SHW | A2 | F3 |
| SMPL | A1 | F3 |
| SMPL | A2 | F3 |
| SPGI | A1 | F3 |
| SPGI | A2 | F3 |
| SSD | A1 | F5 |
| SSD | A2 | F5 |
| SUI | A1 | F5 |
| SUI | A2 | F5 |
| SXC | A1 | F2 |
| SXC | A2 | F2 |
| TNL | A1 | F4 |
| TNL | A2 | F4 |
| TRU | A1 | F5 |
| TRU | A2 | F5 |
| UPS | A1 | F3 |
| UPS | A2 | F3 |
| VLRS | A1 | F2 |
| VLRS | A2 | F2 |
| WELL | A1 | F3 |
| WELL | A2 | F3 |
| WSO | A1 | F5 |
| WSO | A2 | F5 |
| XYL | A1 | F6 |
| XYL | A2 | F6 |

## Exploration book tonight (25; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| AMKR | SS | 2026-10-30T00:00:00.000 | 37.00 | 5.02 | +13.08% | 1,241.49 | F7 |
| AMT | SS | 2026-11-20T00:00:00.000 | 190.00 | 13.19 | +6.74% | 2,470.91 | F3 |
| BRO | SS | 2026-11-20T00:00:00.000 | 70.00 | 5.53 | +7.26% | 965.84 | F6 |
| BRO | IC | 2026-11-20T00:00:00.000 | 70.00 | 4.85 | +6.05% | 514.70 | F6 |
| CDNS | SS | 2026-10-30T00:00:00.000 | 320.00 | 26.11 | +7.72% | 7,145.42 | F3 |
| CLS | SS | 2026-10-30T00:00:00.000 | 247.50 | 32.51 | +12.32% | 8,500.52 | F6 |
| CNC | SS | 2026-10-30T00:00:00.000 | 68.00 | 5.18 | +7.29% | 1,500.71 | PASS |
| CNC | IC | 2026-10-30T00:00:00.000 | 68.00 | 5.00 | +6.91% | 800.20 | PASS |
| FCX | SS | 2026-10-30T00:00:00.000 | 65.00 | 3.45 | +5.17% | 1,474.96 | F3 |
| GLXY | SS | 2026-10-30T00:00:00.000 | 15.50 | 2.07 | +12.77% | 716.53 | F7 |
| HLT | SS | 2026-10-30T00:00:00.000 | 352.50 | 15.14 | +3.94% | 4,824.42 | F3 |
| IQV | SS | 2026-11-20T00:00:00.000 | 270.00 | 28.94 | +9.94% | 4,912.91 | F6 |
| IQV | IC | 2026-11-20T00:00:00.000 | 270.00 | 26.65 | +8.96% | 3,335.25 | F6 |
| IVZ | SS | 2026-11-20T00:00:00.000 | 29.00 | 2.45 | +7.90% | 414.14 | F6 |
| NUE | SS | 2026-11-20T00:00:00.000 | 260.00 | 24.08 | +8.59% | 4,165.77 | F3 |
| PCAR | SS | 2026-11-20T00:00:00.000 | 105.00 | 8.37 | +6.61% | 1,104.06 | F3 |
| PYPL | SS | 2026-10-30T00:00:00.000 | 55.00 | 4.42 | +7.82% | 1,058.42 | PASS |
| PYPL | IC | 2026-10-30T00:00:00.000 | 55.00 | 4.21 | +7.40% | 578.77 | PASS |
| RCL | SS | 2026-10-30T00:00:00.000 | 280.00 | 20.30 | +6.63% | 5,974.94 | F3 |
| RMBS | SS | 2026-11-20T00:00:00.000 | 90.00 | 16.18 | +17.16% | 2,637.02 | F6 |
| SOFI | SS | 2026-10-30T00:00:00.000 | 14.50 | 1.31 | +8.89% | 371.83 | PASS |
| SOFI | IC | 2026-10-30T00:00:00.000 | 14.50 | 1.26 | +8.38% | 224.16 | PASS |
| UPS | SS | 2026-10-30T00:00:00.000 | 100.00 | 6.33 | +6.07% | 1,559.81 | F3 |
| UPS | IC | 2026-10-30T00:00:00.000 | 100.00 | 6.09 | +5.77% | 890.70 | F3 |
| XYL | SS | 2026-11-20T00:00:00.000 | 110.00 | 9.02 | +7.88% | 1,340.32 | F6 |

## Graded today (0)
_none due_

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 2 | 2 | +2.69% | 3.42 | 232.76 |
| sa-1.0 | champion | A1 | SS | 9 | 6 | +0.53% | 0.56 | 317.92 |
| sa-1.0 | champion | A2 | IC | 2 | 2 | +2.69% | 3.42 | 232.76 |
| sa-1.0 | champion | A2 | SS | 9 | 6 | +0.53% | 0.56 | 317.92 |
| sa-1.0 | exploration | A1 | IC | 15 | 12 | -0.89% | -1.46 | -1,769.09 |
| sa-1.0 | exploration | A1 | SS | 53 | 14 | -0.42% | -1.92 | -1,335.54 |

Ledger: emitted 12 (skipped 0), exploration 25 (skipped 0), graded 0; ledger open.

## S-B state
Gate (2026-10-26, from 2026-10-23 closes): SPY ON (VIX 19.45, VIX3M 20.48, X 19.45 vs median 16.055) · QQQ ON (VIX 19.45, VIX3M 20.48, X 28.3 vs median 22.1)

Next session (2026-10-27, from 2026-10-26 closes): SPY UNKNOWN:null input at 2026-10-26 · QQQ UNKNOWN:null input at 2026-10-26

CBOE refresh: ok through 2026-10-26; index-vol through 2026-10-26

Entry day: no.

### S-B positions tonight (0)
_none_

### S-B graded at expiry today (0)
_none due_

Open positions: QQQ-IC 2, QQQ-PS 3, SPY-PS 2

### S-B forward ledger to date
| policy_id | role | sleeve | n | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|---|
| sb-1.0 | champion | QQQ-IC | 3 | +1.40% | 0.34 | 228.84 |
| sb-1.0 | champion | QQQ-PS | 3 | -1.72% | -0.40 | -140.65 |
| sb-1.0 | champion | SPY-IC | 2 | — | — | 372.65 |
| sb-1.0 | champion | SPY-PS | 3 | +5.06% | 34.39 | 400.25 |
| sb-1.0 | exploration | QQQ-IC | 3 | +1.40% | 0.34 | 228.84 |
| sb-1.0 | exploration | QQQ-PS | 4 | +0.43% | 0.10 | 71.54 |
| sb-1.0 | exploration | SPY-IC | 3 | +6.91% | 23.93 | 543.46 |
| sb-1.0 | exploration | SPY-PS | 4 | +5.10% | 33.81 | 524.57 |

S-B ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0; ledger open.


## S-C state
Entry day: no; ledger open.

### S-C graded at expiry (0)
_none due_

### S-C open book (S-B open: yes; the 40% budget binds only then)
| pair | positions | open_risk_usd | budget_usd | max_sector_positions |
|---|---|---|---|---|
| C1-SS | 6 | 7,375.54 | 8,000.00 | 3 |
| C1-IB | 5 | 3,962.47 | 4,000.00 | 3 |
| C2-SS | 5 | 7,496.64 | 8,000.00 | 3 |
| C2-IB | 5 | 3,925.40 | 4,000.00 | 3 |

### S-C forward ledger to date (entry-week series)
_ledger empty_

Progress to the read: graded entry-weeks 0 of 40 (C1-SS), 0 of 40 (C1-IB), 0 of 40 (C2-SS), 0 of 40 (C2-IB)

S-C ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0.


## Watch basket (wb-1.0, exploration, paper only)
Universe: 1998 names.
Borrow snapshot: 2026-10-26 (the session's own); fee known for 1990 names.
Bull counts: 0:666, 1:698, 2:412, 3:179, 4:38, 5:5, 6:0, 7:0, 8:0
Bear counts: 0:757, 1:708, 2:361, 3:129, 4:38, 5:5, 6:0, 7:0, 8:0

### LONG (123)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| ABBV | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| ABM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| AES | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| ALRM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| AMG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| AMGN | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMRX | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| APPN | 3 | 0 | no | x | x |  |  |  |  |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| AXS | 3 | 0 | yes |  | x |  |  | x | x | ? |  |  |  |  |  |  |  |  |  |  |  |  |  |
| AZN | 3 | 0 | yes |  | x |  | x |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| BBT | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  | ? |  |  |  |  |  |  |  |  |  | x |
| BFA | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BIIB | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| BNT | 3 | 0 | yes |  | x | x | x |  |  | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BRKB | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| BVS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| BY | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| CAH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CATY | 4 | 0 | yes | x | x |  | x |  | x | ? |  |  | ? | ? |  |  |  | ? |  |  |  |  |  |
| CFG | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CNK | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| CNOB | 4 | 0 | yes | x | x |  | x |  | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| COKE | 3 | 0 | no | x | x |  |  |  | x |  |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| COP | 3 | 0 | no | x | x |  |  |  |  | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| CUBI | 5 | 0 | no | x |  |  | x | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DBX | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| DCOM | 3 | 0 | yes | x |  |  | x |  | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DFIN | 3 | 0 | yes | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| DHR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DRH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DV | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| EGBN | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| EOG | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| EPC | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| EPRT | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| EQH | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EXPO | 3 | 0 | yes | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  | x |
| FANG | 4 | 0 | yes | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| FIZZ | 3 | 0 | no |  |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| FLYW | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| FMS | 3 | 0 | no |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| FSBC | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| GIC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| GPOR | 3 | 0 | no |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| HAFN | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HBT | 3 | 0 | no | x | x |  | x |  |  | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HCA | 3 | 0 | no |  | x |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| HCSG | 4 | 0 | no | x |  |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HLI | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| HMC | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| HONA | 3 | 0 | no |  | x | ? |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  | x |  | x |
| HST | 5 | 0 | no | x | x |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| JOE | 3 | 0 | no |  |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| KFRC | 4 | 0 | yes | x |  |  | x |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| KVUE | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| LIN | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LION | 3 | 0 | no |  |  | x |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| LNG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LQDT | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| LSPD | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| LTH | 3 | 0 | yes | x |  |  | x |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MAR | 4 | 0 | no | x | x |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| MBWM | 3 | 0 | yes | x |  |  | x |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| MCB | 3 | 0 | yes | x |  |  |  | x | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| MCBS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? | ? |  |  |  | ? |  |  |  |  |  |
| MH | 3 | 0 | yes |  | x |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| MQ | 3 | 0 | no |  | x |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| MRSH | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| MSCI | 3 | 0 | yes |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| NFG | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| NWE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| NWN | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| NWSA | 4 | 0 | no | x | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| ORLY | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| OVV | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| PANW | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| PLMR | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| PLUS | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PNFP | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| PRSU | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| QLYS | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| R | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RDWR | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| REAL | 3 | 0 | no |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| RLJ | 4 | 0 | no | x | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| RNR | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| ROP | 3 | 0 | yes |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| RS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RSG | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| SBAC | 3 | 0 | no |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SBH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| SDRL | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| SHO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? | ? |  |  |  | ? |  |  |  |  |  |
| SMA | 3 | 0 | yes |  | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| SN | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| SNPS | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SNY | 3 | 0 | no |  | x |  | x | x |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| SPNT | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| SU | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  | x | x |
| TAK | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  |  |
| TALO | 3 | 0 | no | x |  |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| TCBK | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TK | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TMP | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TRGP | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TRMD | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| TS | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| TTC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| TTE | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| TW | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| TYL | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| URI | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| UTHR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VCEL | 3 | 0 | yes |  | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| VET | 3 | 0 | yes | x | x |  |  |  |  | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| VLTO | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VSTS | 3 | 0 | no |  |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| WLY | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| WMT | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| WOR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| WTRG | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |

### SHORT (91)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AA | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x | x |  |  | x |
| AAOI | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| ABVX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  |  |
| AG | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  | x |
| ALB | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  | x |
| ALG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| AMKR | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| AMSC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| ASTS | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  | x | x |
| AXSM | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  | x |  |  |  | x |  | x |  | x |
| BHF | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  | x |  |  |
| BIDU | 0 | 5 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | x | x |  |  |  | x |
| BILI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  |  |
| BMNR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x | ? |  | x | x |
| BROS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| CAR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| CBRS | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  | x | x | x |
| CC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CDE | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  | x |
| CHEF | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| CLMT | 0 | 4 | no |  |  |  |  |  |  |  |  |  | ? | x | x | x |  | ? | x |  |  |  | x |
| CLS | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| COIN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  | x | x |
| CORZ | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  |  |  |  |  |  | x |
| CRCL | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  |  | x |
| CSWC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| CVNA | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  |  | x |
| DVA | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| ECHO | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  | x | x |
| ELAN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| ENPH | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| F | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| FICO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| FIGR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| FN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| FSK | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| GGG | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  | x |  | ? | x |  |  |  | x |
| GLW | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| GLXY | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  |  |  |  |  | x |
| GOOG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  | x | x |
| GOOGL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  | x | x |
| GPGI | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| HIMS | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x | x |  | ? |  |  |  |  | x |
| HL | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  | x |
| HOOD | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  |  | x | x |
| HSY | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| HUT | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  | x |
| HYMC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  |  | x |  |  |  |  |
| INFY | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  | x |  | ? |  |  |  |  | x |
| IREN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  | x | x |
| KLAR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? | x |  |  |  |  |
| KNX | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| KT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  |  |
| KTOS | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| LEU | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  | x | x | x |
| LUNR | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  |  |
| META | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| MGA | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| MP | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  |  |  |  |  | x |
| MSGS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? |  |  |  |  | x |
| MWH | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| NAMS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| NU | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| OKLO | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  | x |
| ORCL | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| PINS | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| PPTA | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| PSIX | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  |  |
| QBTS | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  | x |
| RCUS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| RIOT | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| RIVN | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  | x |  |  |  | x |
| RKLB | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| SCCO | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| SGI | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| SKHY | 0 | 3 | no |  |  | ? |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  | x | x |
| SLM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| SLS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  |  |
| SMCI | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  |  | x |
| SNDX | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| SOFI | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| SPCX | 0 | 4 | no |  |  | ? |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| SRPT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| STRL | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| VALE | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| VC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  |  |
| VKTX | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| VSEC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| WOLF | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? |  |  |  |  |  |
| XP | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  | x | x |  | ? |  |  |  |  | x |
| XYZ | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  |  | x |

### VOL (3)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAL | 0 | 0 | no |  |  |  |  |  |  | ? |  |  |  |  |  |  |  |  |  | x |  |  | x |
| CLF | 0 | 2 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? |  | x |  |  | x |
| GME | 0 | 2 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? |  | x |  |  | x |

CONFLICT (logged only, never a basket, DESIGN/110 §3): 96.

Ledger: emitted 217 (skipped 0), graded 519; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
