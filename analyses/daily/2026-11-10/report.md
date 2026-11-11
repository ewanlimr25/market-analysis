# S-A daily — 2026-11-10 (S3)

Preflight: WARN — prices.parquet ends 2026-11-06, BEFORE the 2026-11-10 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-11-06, BEFORE the 2026-11-10 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-11-06, BEFORE the 2026-11-10 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (0)
_no event tonight clears the filters._

## Suppressed (82)
| ticker | variant | first_fail |
|---|---|---|
| AADX | A1 | F3 |
| AADX | A2 | F3 |
| ALC | A1 | F6 |
| ALC | A2 | F6 |
| AMPX | A1 | F2 |
| AMPX | A2 | F2 |
| ATEX | A1 | F3 |
| ATEX | A2 | F3 |
| ATRO | A1 | F4 |
| ATRO | A2 | F4 |
| AYA | A1 | F3 |
| AYA | A2 | F3 |
| AZTA | A1 | F3 |
| AZTA | A2 | F3 |
| BRCB | A1 | F3 |
| BRCB | A2 | F3 |
| BV | A1 | F3 |
| BV | A2 | F3 |
| CAPR | A1 | F2 |
| CAPR | A2 | F2 |
| CLFD | A1 | F3 |
| CLFD | A2 | F3 |
| CRWV | A1 | F7 |
| CRWV | A2 | F7 |
| EC | A1 | F4 |
| EC | A2 | F4 |
| ELMD | A1 | F3 |
| ELMD | A2 | F3 |
| FLNG | A1 | F3 |
| FLNG | A2 | F3 |
| FLY | A1 | F7 |
| FLY | A2 | F7 |
| FOSL | A1 | F2 |
| FOSL | A2 | F2 |
| GIB | A1 | F4 |
| GIB | A2 | F4 |
| GO | A1 | F3 |
| GO | A2 | F3 |
| INMD | A1 | F3 |
| INMD | A2 | F3 |
| KURA | A1 | F2 |
| KURA | A2 | F2 |
| LAND | A1 | F2 |
| LAND | A2 | F2 |
| MRCY | A1 | F6 |
| MRCY | A2 | F6 |
| NN | A1 | F2 |
| NN | A2 | F2 |
| ODD | A1 | F3 |
| ODD | A2 | F3 |
| PBR | A1 | F3 |
| PBR | A2 | F3 |
| PYPD | A1 | F2 |
| PYPD | A2 | F2 |
| QUIK | A1 | F2 |
| QUIK | A2 | F2 |
| RDCM | A1 | F3 |
| RDCM | A2 | F3 |
| RDNW | A1 | F2 |
| RDNW | A2 | F2 |
| REZI | A1 | F4 |
| REZI | A2 | F4 |
| RGTI | A1 | F7 |
| RGTI | A2 | F7 |
| RSKD | A1 | F2 |
| RSKD | A2 | F2 |
| RUM | A1 | F2 |
| RUM | A2 | F2 |
| SKYH | A1 | F3 |
| SKYH | A2 | F3 |
| SONO | A1 | F3 |
| SONO | A2 | F3 |
| SPIR | A1 | F2 |
| SPIR | A2 | F2 |
| STUB | A1 | F2 |
| STUB | A2 | F2 |
| SUNS | A1 | F2 |
| SUNS | A2 | F2 |
| VELO | A1 | F2 |
| VELO | A2 | F2 |
| VIV | A1 | F4 |
| VIV | A2 | F4 |

## Exploration book tonight (13; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| ALC | SS | 2026-11-20T00:00:00.000 | 75.00 | 6.03 | +7.32% | 1,175.94 | F6 |
| ALC | IC | 2026-11-20T00:00:00.000 | 75.00 | 5.28 | +6.21% | 722.05 | F6 |
| AMPX | SS | 2026-11-13T00:00:00.000 | 9.00 | 1.37 | +13.64% | 395.72 | F2 |
| ATEX | SS | 2026-11-20T00:00:00.000 | 75.00 | 9.65 | +11.14% | 2,609.85 | F3 |
| AZTA | SS | 2026-11-20T00:00:00.000 | 40.00 | 5.58 | +9.47% | 1,193.47 | F3 |
| CRWV | SS | 2026-11-13T00:00:00.000 | 49.00 | 8.81 | +17.86% | 2,546.98 | F7 |
| FLY | SS | 2026-11-13T00:00:00.000 | 23.50 | 3.60 | +14.51% | 1,089.74 | F7 |
| GO | SS | 2026-11-20T00:00:00.000 | 14.00 | 1.84 | +11.78% | 392.98 | F3 |
| MRCY | SS | 2026-11-20T00:00:00.000 | 85.00 | 11.73 | +10.85% | 2,591.11 | F6 |
| NN | SS | 2026-11-13T00:00:00.000 | 8.50 | 1.15 | +11.67% | 619.52 | F2 |
| PBR | SS | 2026-11-13T00:00:00.000 | 18.50 | 0.90 | +4.62% | 348.25 | F3 |
| PBR | IC | 2026-11-13T00:00:00.000 | 18.50 | 0.85 | +4.28% | 214.58 | F3 |
| RGTI | SS | 2026-11-13T00:00:00.000 | 12.00 | 1.37 | +10.98% | 496.21 | F7 |

## Graded today (26)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| ONON | A1 | SS | champion | +1.47% | 54.98 | 1 | no |
| ONON | A2 | SS | champion | +1.47% | 54.98 | 1 | no |
| ASTS | A1 | SS | exploration | +3.59% | 132.24 | 1 | no |
| BTDR | A1 | SS | exploration | +2.21% | 14.65 | 1 | no |
| DHT | A1 | SS | exploration | -3.96% | -81.50 | 1 | no |
| HIMS | A1 | SS | exploration | +1.92% | 44.08 | 1 | no |
| MARA | A1 | SS | exploration | -1.61% | -10.68 | 1 | no |
| MARA | A1 | IC | exploration | -2.04% | -13.54 | 2 | no |
| ONON | A1 | SS | exploration | +1.47% | 54.98 | 1 | no |
| OXY | A1 | SS | exploration | +0.65% | 36.01 | 1 | no |
| OXY | A1 | IC | exploration | +0.54% | 29.85 | 1 | no |
| QBTS | A1 | SS | exploration | +0.17% | 1.94 | 1 | no |
| QLYS | A1 | SS | exploration | +0.23% | 46.67 | 2 | no |
| QUBT | A1 | SS | exploration | +0.85% | 5.81 | 1 | no |
| RKLB | A1 | SS | exploration | +3.92% | 230.99 | 1 | no |
| RKLB | A1 | IC | exploration | +3.56% | 209.51 | 1 | no |
| SE | A1 | SS | exploration | +6.61% | 516.36 | 1 | no |
| SKYD | A1 | SS | exploration | -1.95% | -16.95 | 1 | no |
| TTD | A1 | SS | exploration | +9.30% | 139.04 | 1 | no |
| TTD | A1 | IC | exploration | +7.58% | 113.33 | 1 | no |
| TTWO | A1 | SS | exploration | -1.60% | -332.42 | 1 | no |
| USAR | A1 | SS | exploration | -1.09% | -9.59 | 1 | no |
| VG | A1 | SS | exploration | +1.43% | 16.95 | 1 | no |
| WGS | A1 | SS | exploration | +6.03% | 396.22 | 1 | no |
| ZETA | A1 | SS | exploration | +3.78% | 122.25 | 1 | no |
| ZETA | A1 | IC | exploration | +2.51% | 81.09 | 2 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 8 | 6 | +0.63% | 1.12 | 245.49 |
| sa-1.0 | champion | A1 | SS | 32 | 15 | -0.77% | -0.98 | -1,477.88 |
| sa-1.0 | champion | A2 | IC | 7 | 5 | +0.66% | 1.00 | 233.18 |
| sa-1.0 | champion | A2 | SS | 25 | 14 | -0.53% | -0.54 | -372.47 |
| sa-1.0 | exploration | A1 | IC | 56 | 22 | -1.11% | -1.62 | -9,164.09 |
| sa-1.0 | exploration | A1 | SS | 263 | 25 | -0.98% | -3.19 | -22,956.55 |

Ledger: emitted 0 (skipped 0), exploration 13 (skipped 0), graded 26; ledger open.

## S-B state
Gate (2026-11-10, from 2026-11-09 closes): SPY ON (VIX 19.92, VIX3M 20.85, X 19.92 vs median 17.955) · QQQ ON (VIX 19.92, VIX3M 20.85, X 28.97 vs median 25.39)

Next session (2026-11-11, from 2026-11-10 closes): SPY UNKNOWN:null input at 2026-11-10 · QQQ UNKNOWN:null input at 2026-11-10

CBOE refresh: ok through 2026-11-10; index-vol through 2026-11-10

Entry day: no.

### S-B positions tonight (0)
_none_

### S-B graded at expiry today (0)
_none due_

Open positions: QQQ-IC 2, QQQ-PS 2, SPY-IC 1, SPY-PS 2

### S-B forward ledger to date
| policy_id | role | sleeve | n | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|---|
| sb-1.0 | champion | QQQ-IC | 4 | -1.45% | -0.31 | -225.41 |
| sb-1.0 | champion | QQQ-PS | 5 | -14.80% | -1.51 | -2,803.29 |
| sb-1.0 | champion | SPY-IC | 2 | — | — | 372.65 |
| sb-1.0 | champion | SPY-PS | 4 | +4.91% | 25.45 | 558.63 |
| sb-1.0 | exploration | QQQ-IC | 4 | -1.45% | -0.31 | -225.41 |
| sb-1.0 | exploration | QQQ-PS | 6 | -11.18% | -1.12 | -2,591.10 |
| sb-1.0 | exploration | SPY-IC | 4 | +6.91% | 31.77 | 724.42 |
| sb-1.0 | exploration | SPY-PS | 6 | +4.90% | 24.34 | 803.04 |

S-B ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0; ledger open.


## S-C state
Entry day: no; ledger open.

### S-C graded at expiry (0)
_none due_

### S-C open book (S-B open: yes; the 40% budget binds only then)
| pair | positions | open_risk_usd | budget_usd | max_sector_positions |
|---|---|---|---|---|
| C1-SS | 4 | 5,657.44 | 8,000.00 | 2 |
| C1-IB | 3 | 2,756.16 | 4,000.00 | 2 |
| C2-SS | 3 | 4,970.59 | 8,000.00 | 2 |
| C2-IB | 4 | 3,110.24 | 4,000.00 | 2 |

### S-C forward ledger to date (entry-week series)
| policy_id | role | pair | n | weeks | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|---|---|
| sc-1.0 | champion | C1-SS | 6 | 2 | — | — | -1,362.15 |
| sc-1.0 | champion | C1-IB | 6 | 2 | — | — | -1,519.19 |
| sc-1.0 | champion | C2-SS | 5 | 2 | — | — | -1,091.11 |
| sc-1.0 | champion | C2-IB | 5 | 2 | — | — | -1,236.18 |
| sc-1.0 | exploration | C1-SS | 142 | 2 | — | — | -218,951.20 |
| sc-1.0 | exploration | C1-IB | 142 | 2 | — | — | -188,897.18 |

Progress to the read: graded entry-weeks 2 of 40 (C1-SS), 2 of 40 (C1-IB), 2 of 40 (C2-SS), 2 of 40 (C2-IB)

S-C ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0.


## Watch basket (wb-1.0, exploration, paper only)
Universe: 1998 names.
Borrow snapshot: 2026-11-10 (the session's own); fee known for 1992 names.
Bull counts: 0:711, 1:660, 2:440, 3:170, 4:17, 5:0, 6:0, 7:0, 8:0
Bear counts: 0:775, 1:752, 2:321, 3:121, 4:25, 5:4, 6:0, 7:0, 8:0

### LONG (93)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ABM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| AER | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| AIZ | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ALGN | 3 | 0 | yes |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| ALH | 3 | 0 | yes |  |  |  |  | x | x | x |  |  | ? |  |  |  |  |  |  |  |  |  | x |
| AMTB | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| ATR | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| AXTA | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BANF | 3 | 0 | no |  |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| BEN | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BFA | 3 | 0 | no | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BLK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BRKB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  | x | x |
| BUD | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BV | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BWIN | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| CL | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| CNK | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CNO | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| COLM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| COST | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| CRBG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CRUS | 3 | 0 | yes |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| CTRE | 3 | 0 | no |  |  |  | x | x | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| CUBE | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| DEO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| DHR | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| DLX | 3 | 0 | no |  |  | x |  | x | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DRH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| EBAY | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EHC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EMR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EPC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| EW | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| EXLS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EXR | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| FAST | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| FTS | 3 | 0 | no |  | x |  |  |  | x | x |  |  | ? |  |  |  |  | ? |  |  |  |  | x |
| GFF | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| GWW | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| HBT | 3 | 0 | no | x | x |  |  |  | x |  |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HII | 3 | 0 | yes |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HLT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HMN | 4 | 0 | no | x |  |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| JJSF | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| JNJ | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| KO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| KOF | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| LH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LLY | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| LNTH | 3 | 0 | yes |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| LSCC | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MANU | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| MCBS | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| MDT | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| MET | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MMM | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| MSCI | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| NATL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| NDAQ | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| NWE | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| OBDC | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| OMAB | 3 | 0 | yes |  | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  | x |
| PFGC | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PPC | 3 | 0 | no |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| PPLI | 3 | 0 | no |  |  |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| RLJ | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| RPRX | 3 | 0 | no | x | x |  |  |  | x |  |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| RYAAY | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| SAIC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| SBUX | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SEIC | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| SGRY | 3 | 0 | no | x | x |  |  |  |  |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| SIGI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| SJM | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| SPNT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| STN | 3 | 0 | no |  | x |  |  |  | x | x |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TAC | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TNC | 3 | 0 | yes |  |  |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TW | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| USPH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| UTI | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| VCTR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VLTO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VOYA | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| VTRS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WAB | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WAT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WMK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| XHR | 4 | 0 | no | x | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| XNCR | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |

### SHORT (87)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| ACI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| ALAB | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| ALNY | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? | x |  | x |  | x |
| ASST | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| ASTS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| AXON | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| AXTI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| BA | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| BABA | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  | x | x |
| BFH | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? |  |  |  |  |  |
| BMNR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| CAT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  | x | x | x |
| CBRL | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? |  |  |  |  |  |
| CFR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| CHKP | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| CIGI | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CLMT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? | x | x |  |  |  | x |  |  |  | x |
| COIN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| CORT | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| CRCL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| CRSP | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| CRWD | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| CSGP | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| CVNA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  | x | x |
| DASH | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? |  |  |  |  | x |
| DBX | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| DVA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| EC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| ENPH | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? |  |  |  |  | x |
| FIG | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| FLG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  | x |
| FRO | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| FSLR | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  | x | x |
| FSLY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  |  |
| GFL | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  |  | x |
| GOOGL | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  | x | x |
| GRAL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| HIMS | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  | x | x |
| HPQ | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| HTGC | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  |  |
| HYMC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| IMAX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| IMO | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? |  |  |  |  | x |
| INGR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? |  |  |  |  |  |
| INOD | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  |  |
| INTC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| INVA | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| IONS | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? | x |  | x |  | x |
| IRTC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  | x |  | ? |  |  |  |  | x |
| KBH | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  | x | x |  | ? | x |  |  |  |  |
| KHC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? |  |  |  |  | x |
| KLAR | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? | x |  |  |  |  |
| LEGN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| LINE | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| LUNR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| LYFT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| MATX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| MELI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| MGA | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| MRVL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| MSTR | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| NE | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? |  |  |  |  |  |
| NFG | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? |  |  |  |  |  |
| NFLX | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  | x | x |
| NRIX | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  | x | x |  | ? | x |  |  |  | x |
| NSC | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| NWS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| NWSA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| ONON | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| ORCL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| OXY | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  | x | x | ? |  |  |  |  | x |
| PBI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| PINS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| PS | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| PTGX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| RHI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| SEDG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  |  |
| SFM | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  | x |  | x |
| SOFI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| TPL | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| TREX | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| VCYT | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  | x |  | ? |  |  |  |  | x |
| VMI | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  |
| W | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| WIX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| YPF | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x |  |  |  |  |

### VOL (0)
_none_

CONFLICT (logged only, never a basket, DESIGN/110 §3): 82.

Ledger: emitted 180 (skipped 0), graded 518; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
