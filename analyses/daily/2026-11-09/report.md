# S-A daily — 2026-11-09 (S3)

Preflight: WARN — prices.parquet ends 2026-11-06, BEFORE the 2026-11-09 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-11-06, BEFORE the 2026-11-09 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-11-06, BEFORE the 2026-11-09 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (4)
| ticker | variant | structure | expiry | k | k_up | k_dn | credit_entry | credit_net_pct | risk_usd | contracts | entry_tier_max | cap_pass |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ONON | A1 | IC | 2026-11-13T00:00:00.000 | 37.50 | 46.00 | 28.50 | 3.71 | +9.36% | 529.37 | 1 | 1 | yes |
| ONON | A1 | SS | 2026-11-13T00:00:00.000 | 37.50 | — | — | 3.84 | +9.97% | 947.78 | 1 | 1 | yes |
| ONON | A2 | IC | 2026-11-13T00:00:00.000 | 37.50 | 46.00 | 28.50 | 3.71 | +9.36% | 529.37 | 1 | 1 | yes |
| ONON | A2 | SS | 2026-11-13T00:00:00.000 | 37.50 | — | — | 3.84 | +9.97% | 947.78 | 1 | 1 | yes |

## Suppressed (198)
| ticker | variant | first_fail |
|---|---|---|
| AAON | A1 | F5 |
| AAON | A2 | F5 |
| ABCL | A1 | F4 |
| ABCL | A2 | F4 |
| ALH | A1 | F4 |
| ALH | A2 | F4 |
| ALTG | A1 | F2 |
| ALTG | A2 | F2 |
| AMBQ | A1 | F3 |
| AMBQ | A2 | F3 |
| AMCX | A1 | F2 |
| AMCX | A2 | F2 |
| AMRC | A1 | F3 |
| AMRC | A2 | F3 |
| AP | A1 | F2 |
| AP | A2 | F2 |
| APEI | A1 | F3 |
| APEI | A2 | F3 |
| APPS | A1 | F3 |
| APPS | A2 | F3 |
| ASTS | A1 | F7 |
| ASTS | A2 | F7 |
| ATAT | A1 | F4 |
| ATAT | A2 | F4 |
| AVNW | A1 | F3 |
| AVNW | A2 | F3 |
| BAP | A1 | F5 |
| BAP | A2 | F5 |
| BCSF | A1 | F3 |
| BCSF | A2 | F3 |
| BETR | A1 | F3 |
| BETR | A2 | F3 |
| BRSL | A1 | F3 |
| BRSL | A2 | F3 |
| BTDR | A1 | F2 |
| BTDR | A2 | F2 |
| BTGO | A1 | F2 |
| BTGO | A2 | F2 |
| BWAY | A1 | F3 |
| BWAY | A2 | F3 |
| CCAP | A1 | F2 |
| CCAP | A2 | F2 |
| CIB | A1 | F4 |
| CIB | A2 | F4 |
| CNNE | A1 | F3 |
| CNNE | A2 | F3 |
| CSQR | A1 | F4 |
| CSQR | A2 | F4 |
| CWCO | A1 | F3 |
| CWCO | A2 | F3 |
| CWEN | A1 | F4 |
| CWEN | A2 | F4 |
| CWST | A1 | F5 |
| CWST | A2 | F5 |
| DFTX | A1 | F5 |
| DFTX | A2 | F5 |
| DHT | A1 | F6 |
| DHT | A2 | F6 |
| DSP | A1 | F3 |
| DSP | A2 | F3 |
| EQPT | A1 | F5 |
| EQPT | A2 | F5 |
| EQX | A1 | F5 |
| EQX | A2 | F5 |
| ETD | A1 | F3 |
| ETD | A2 | F3 |
| ETOR | A1 | F3 |
| ETOR | A2 | F3 |
| EXK | A1 | F2 |
| EXK | A2 | F2 |
| FF | A1 | F2 |
| FF | A2 | F2 |
| FWRD | A1 | F3 |
| FWRD | A2 | F3 |
| GAIN | A1 | F3 |
| GAIN | A2 | F3 |
| GILT | A1 | F2 |
| GILT | A2 | F2 |
| GRPN | A1 | F3 |
| GRPN | A2 | F3 |
| GSHD | A1 | F3 |
| GSHD | A2 | F3 |
| HIMS | A1 | F7 |
| HIMS | A2 | F7 |
| HNRG | A1 | F3 |
| HNRG | A2 | F3 |
| HPK | A1 | F2 |
| HPK | A2 | F2 |
| HQ | A1 | F3 |
| HQ | A2 | F3 |
| HRB | A1 | F5 |
| HRB | A2 | F5 |
| HROW | A1 | F3 |
| HROW | A2 | F3 |
| HSAI | A1 | F3 |
| HSAI | A2 | F3 |
| INR | A1 | F3 |
| INR | A2 | F3 |
| JBS | A1 | F5 |
| JBS | A2 | F5 |
| KMPR | A1 | F3 |
| KMPR | A2 | F3 |
| LEGN | A1 | F5 |
| LEGN | A2 | F5 |
| LFVN | A1 | F2 |
| LFVN | A2 | F2 |
| LINE | A1 | F4 |
| LINE | A2 | F4 |
| LNSR | A1 | F2 |
| LNSR | A2 | F2 |
| LQDA | A1 | F5 |
| LQDA | A2 | F5 |
| LTRX | A1 | F2 |
| LTRX | A2 | F2 |
| MARA | A1 | F2 |
| MARA | A2 | F2 |
| MASS | A1 | F3 |
| MASS | A2 | F3 |
| MCFT | A1 | F3 |
| MCFT | A2 | F3 |
| NGS | A1 | F3 |
| NGS | A2 | F3 |
| NHI | A1 | F4 |
| NHI | A2 | F4 |
| NOVT | A1 | F5 |
| NOVT | A2 | F5 |
| NXE | A1 | F2 |
| NXE | A2 | F2 |
| ONTO | A1 | F5 |
| ONTO | A2 | F5 |
| OSG | A1 | F2 |
| OSG | A2 | F2 |
| OXY | A1 | F3 |
| OXY | A2 | F3 |
| PAYS | A1 | F3 |
| PAYS | A2 | F3 |
| PUBM | A1 | F3 |
| PUBM | A2 | F3 |
| QBTS | A1 | F7 |
| QBTS | A2 | F7 |
| QLYS | A1 | F6 |
| QLYS | A2 | F6 |
| QMCO | A1 | F3 |
| QMCO | A2 | F3 |
| QUBT | A1 | F2 |
| QUBT | A2 | F2 |
| REFI | A1 | F2 |
| REFI | A2 | F2 |
| RKLB | A1 | F7 |
| RKLB | A2 | F7 |
| SANM | A1 | F5 |
| SANM | A2 | F5 |
| SB | A1 | F2 |
| SB | A2 | F2 |
| SBH | A1 | F3 |
| SBH | A2 | F3 |
| SE | A1 | F6 |
| SE | A2 | F6 |
| SECZ | A1 | F2 |
| SECZ | A2 | F2 |
| SENS | A1 | F2 |
| SENS | A2 | F2 |
| SKYD | A1 | F2 |
| SKYD | A2 | F2 |
| SRRK | A1 | F5 |
| SRRK | A2 | F5 |
| TDG | A1 | F3 |
| TDG | A2 | F3 |
| TIMB | A1 | F4 |
| TIMB | A2 | F4 |
| TRVI | A1 | F4 |
| TRVI | A2 | F4 |
| TTD | A1 | F7 |
| TTD | A2 | F7 |
| TTWO | A1 | F6 |
| TTWO | A2 | F6 |
| USAR | A1 | F2 |
| USAR | A2 | F2 |
| VG | A1 | F6 |
| VG | A2 | F6 |
| VOD | A1 | F6 |
| VOD | A2 | F6 |
| WBTN | A1 | F2 |
| WBTN | A2 | F2 |
| WGS | A1 | F3 |
| WGS | A2 | F3 |
| WIX | A1 | F5 |
| WIX | A2 | F5 |
| WYFI | A1 | F2 |
| WYFI | A2 | F2 |
| XENE | A1 | F5 |
| XENE | A2 | F5 |
| XGN | A1 | F2 |
| XGN | A2 | F2 |
| ZETA | A1 | F6 |
| ZETA | A2 | F6 |
| ZYME | A1 | F4 |
| ZYME | A2 | F4 |

## Exploration book tonight (31; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| ASTS | SS | 2026-11-13T00:00:00.000 | 37.00 | 5.56 | +14.86% | 1,894.32 | F7 |
| BTDR | SS | 2026-11-13T00:00:00.000 | 6.50 | 1.10 | +15.39% | 332.75 | F2 |
| CWEN | SS | 2026-11-20T00:00:00.000 | 35.00 | 2.32 | +6.19% | 527.95 | F4 |
| DHT | SS | 2026-11-20T00:00:00.000 | 21.00 | 2.18 | +8.02% | 485.80 | F6 |
| DHT | IC | 2026-11-20T00:00:00.000 | 21.00 | 1.98 | +6.80% | 301.79 | F6 |
| HIMS | SS | 2026-11-13T00:00:00.000 | 23.00 | 3.52 | +15.10% | 941.89 | F7 |
| HSAI | SS | 2026-11-20T00:00:00.000 | 14.00 | 2.05 | +13.86% | 472.91 | F3 |
| MARA | SS | 2026-11-13T00:00:00.000 | 6.50 | 0.83 | +12.18% | 336.85 | F2 |
| MARA | IC | 2026-11-13T00:00:00.000 | 6.50 | 0.81 | +11.62% | 218.89 | F2 |
| ONON | SS | 2026-11-13T00:00:00.000 | 37.50 | 3.84 | +9.97% | 947.78 | PASS |
| ONON | IC | 2026-11-13T00:00:00.000 | 37.50 | 3.71 | +9.36% | 529.37 | PASS |
| OXY | SS | 2026-11-13T00:00:00.000 | 56.00 | 2.50 | +4.33% | 988.74 | F3 |
| OXY | IC | 2026-11-13T00:00:00.000 | 56.00 | 2.46 | +4.23% | 553.98 | F3 |
| QBTS | SS | 2026-11-13T00:00:00.000 | 11.50 | 1.36 | +11.63% | 478.82 | F7 |
| QLYS | SS | 2026-11-20T00:00:00.000 | 200.00 | 27.32 | +12.60% | 6,216.08 | F6 |
| QUBT | SS | 2026-11-13T00:00:00.000 | 7.00 | 0.78 | +10.99% | 236.73 | F2 |
| QUBT | IC | 2026-11-13T00:00:00.000 | 7.00 | 0.74 | +10.02% | 125.94 | F2 |
| RKLB | SS | 2026-11-13T00:00:00.000 | 59.00 | 7.44 | +12.47% | 2,419.68 | F7 |
| RKLB | IC | 2026-11-13T00:00:00.000 | 59.00 | 7.25 | +12.08% | 1,374.81 | F7 |
| SE | SS | 2026-11-13T00:00:00.000 | 78.00 | 11.10 | +13.50% | 2,311.39 | F6 |
| SKYD | SS | 2026-11-13T00:00:00.000 | 8.50 | 0.73 | +6.98% | 247.65 | F2 |
| TTD | SS | 2026-11-13T00:00:00.000 | 15.00 | 2.78 | +18.13% | 492.91 | F7 |
| TTD | IC | 2026-11-13T00:00:00.000 | 15.00 | 2.55 | +16.40% | 244.59 | F7 |
| TTWO | SS | 2026-11-13T00:00:00.000 | 207.50 | 17.12 | +7.63% | 6,128.89 | F6 |
| TTWO | IC | 2026-11-13T00:00:00.000 | 207.50 | 16.73 | +7.38% | 3,576.85 | F6 |
| USAR | SS | 2026-11-13T00:00:00.000 | 9.00 | 1.17 | +12.63% | 435.13 | F2 |
| VG | SS | 2026-11-13T00:00:00.000 | 12.00 | 1.25 | +9.55% | 385.49 | F6 |
| VOD | SS | 2026-11-13T00:00:00.000 | 15.50 | 0.81 | +4.64% | 234.40 | F6 |
| WGS | SS | 2026-11-13T00:00:00.000 | 66.00 | 18.02 | +24.77% | 3,564.35 | F3 |
| ZETA | SS | 2026-11-13T00:00:00.000 | 32.50 | 4.76 | +13.99% | 1,009.08 | F6 |
| ZETA | IC | 2026-11-13T00:00:00.000 | 32.50 | 4.47 | +12.62% | 552.76 | F6 |

## Graded today (8)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| B | A1 | SS | exploration | -1.39% | -56.24 | 1 | no |
| CEG | A1 | SS | exploration | +0.44% | 110.44 | 1 | no |
| CEG | A1 | IC | exploration | +0.21% | 52.29 | 1 | no |
| FRVO | A1 | SS | exploration | -0.12% | -1.11 | 1 | no |
| IONS | A1 | SS | exploration | -14.15% | -557.55 | 1 | no |
| MNDY | A1 | SS | exploration | +1.78% | 156.15 | 1 | no |
| MNDY | A1 | IC | exploration | +0.04% | 3.83 | 1 | no |
| RDNT | A1 | SS | exploration | -0.84% | -63.51 | 1 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 8 | 6 | +0.63% | 1.12 | 245.49 |
| sa-1.0 | champion | A1 | SS | 31 | 14 | -0.84% | -1.04 | -1,532.86 |
| sa-1.0 | champion | A2 | IC | 7 | 5 | +0.66% | 1.00 | 233.18 |
| sa-1.0 | champion | A2 | SS | 24 | 13 | -0.62% | -0.60 | -427.45 |
| sa-1.0 | exploration | A1 | IC | 51 | 21 | -1.45% | -2.23 | -9,584.33 |
| sa-1.0 | exploration | A1 | SS | 244 | 24 | -1.18% | -5.21 | -24,263.59 |

Ledger: emitted 4 (skipped 0), exploration 31 (skipped 0), graded 8; ledger open.

## S-B state
Gate (2026-11-09, from 2026-11-06 closes): SPY OFF:G1 (VIX 25.64, VIX3M 24.6, X 25.64 vs median 17.415) · QQQ OFF:G1 (VIX 25.64, VIX3M 24.6, X 34.02 vs median 25.2)

Next session (2026-11-10, from 2026-11-09 closes): SPY ON (VIX 19.92, VIX3M 20.85, X 19.92 vs median 17.955) · QQQ ON (VIX 19.92, VIX3M 20.85, X 28.97 vs median 25.39)

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
Universe: 2051 names.
Borrow snapshot: 2026-11-09 (the session's own); fee known for 2043 names.
Bull counts: 0:712, 1:744, 2:435, 3:143, 4:16, 5:1, 6:0, 7:0, 8:0
Bear counts: 0:808, 1:760, 2:339, 3:120, 4:21, 5:3, 6:0, 7:0, 8:0

### LONG (76)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ACEL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| ACM | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AER | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| AIZ | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMTB | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| ANRO | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| ATR | 3 | 0 | yes | x | x |  |  |  | x |  |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| AXTA | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| BANF | 3 | 0 | no |  |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| BATRK | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BIIB | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BKE | 3 | 0 | yes |  | x | x |  | x |  | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BLBD | 3 | 0 | no |  | x | x |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BLK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BRKB | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  | ? |  |  |  | x | x |
| BUD | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CDP | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  | ? |  |  |  |  | ? |  |  |  |  | x |
| COLM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| COST | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| CUBE | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| DEO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DLX | 3 | 0 | no |  |  | x |  | x | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DOLE | 3 | 0 | yes |  |  |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DPC | 3 | 0 | yes |  | x | ? |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| EBAY | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EGBN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| EHC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EW | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| EXLS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EXR | 4 | 0 | no | x | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| FAST | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| FLYW | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| FSV | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| GO | 4 | 0 | yes | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| GRBK | 3 | 0 | yes |  |  | x |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HG | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HLT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HON | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| IDT | 4 | 0 | no | x | x |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| IPAR | 4 | 0 | no | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| JOE | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| LH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LKFT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| LSCC | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MANU | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| MCBS | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| MICC | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| MMM | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| NATL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| NDAQ | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| NIQ | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| NVS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| NWE | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| PDM | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PFGC | 4 | 0 | no | x |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PPLI | 3 | 0 | yes |  |  |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| RDY | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| RPRX | 3 | 0 | no | x | x |  |  |  | x |  |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| RTO | 3 | 0 | yes |  | x |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| SAIC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| SBUX | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SGRY | 3 | 0 | no | x | x |  |  |  |  |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| SMA | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| SPNT | 4 | 0 | no | x | x |  |  |  | x | x |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TAC | 3 | 0 | no |  |  |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| TCOM | 3 | 0 | no |  | x |  | x |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| TDG | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TEVA | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| TRVI | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| TW | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VCTR | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VTRS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WAT | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| XHR | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| XYZ | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| ZLAB | 3 | 0 | yes | x | x |  | x |  |  | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |

### SHORT (69)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| AFRM | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| AKAM | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| ALAB | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| ALNY | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  | x |  | x |
| ANIP | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| ASST | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| ASTS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| AXON | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| AXTI | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| BA | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| BMNR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| CARR | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| CAT | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| CC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  |  |
| CFR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| CHTR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| CLMT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? | x | x |  |  | ? | x |  |  |  | x |
| COIN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  | x | x |
| CRCL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| CSGP | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| DASH | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? |  |  |  |  | x |
| DTM | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? |  |  |  |  | x |
| EC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| ENPH | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? |  |  |  |  | x |
| EQT | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  |  |  | x | x | ? |  |  |  |  | x |
| FIG | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| FSLY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| GNTX | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  | x |  | x |
| GOOGL | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  | x | x |
| GRAL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| HTGC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| IMAX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| IMO | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? |  |  |  |  | x |
| INGR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? |  |  |  |  | x |
| INOD | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  |  |
| INTC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| INVA | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| IONS | 0 | 4 | yes |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  | x | x | x |
| IRTC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  | x |  | ? |  |  |  |  | x |
| KBH | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| KHC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? |  |  |  |  | x |
| LITE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| LUNR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| MATX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| MGA | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| MGY | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| MNDY | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| MRVL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| MSTR | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| MTDR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| NFG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? |  |  |  |  | x |
| NRIX | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| NWS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  |  |
| ORCL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| OXY | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  | x | x | ? |  |  |  |  | x |
| PDD | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? |  |  |  |  | x |
| PENG | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| PTGX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| RHI | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| SHC | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| SM | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| SRPT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| STRA | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  | x |  |  | ? | x |  | x |  |  |
| SYF | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| W | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? |  |  |  |  | x |
| WHR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  |  |  |  |  |  |  |
| WIX | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? | x |  |  |  | x |
| ZD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |

### VOL (0)
_none_

CONFLICT (logged only, never a basket, DESIGN/110 §3): 80.

Ledger: emitted 145 (skipped 0), graded 588; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
