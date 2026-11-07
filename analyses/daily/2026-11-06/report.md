# S-A daily — 2026-11-06 (S3)

Preflight: WARN — prices.parquet ends 2026-10-30, BEFORE the 2026-11-06 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-10-30, BEFORE the 2026-11-06 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-10-30, BEFORE the 2026-11-06 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (0)
_no event tonight clears the filters._

## Suppressed (84)
| ticker | variant | first_fail |
|---|---|---|
| AMG | A1 | F5 |
| AMG | A2 | F5 |
| B | A1 | F3 |
| B | A2 | F3 |
| CECO | A1 | F5 |
| CECO | A2 | F5 |
| CEG | A1 | F3 |
| CEG | A2 | F3 |
| CEVA | A1 | F3 |
| CEVA | A2 | F3 |
| CNH | A1 | F5 |
| CNH | A2 | F5 |
| CTEV | A1 | F3 |
| CTEV | A2 | F3 |
| DCTH | A1 | F3 |
| DCTH | A2 | F3 |
| DOLE | A1 | F3 |
| DOLE | A2 | F3 |
| FERG | A1 | F5 |
| FERG | A2 | F5 |
| FRVO | A1 | F2 |
| FRVO | A2 | F2 |
| GCMG | A1 | F3 |
| GCMG | A2 | F3 |
| GSL | A1 | F3 |
| GSL | A2 | F3 |
| HE | A1 | F2 |
| HE | A2 | F2 |
| IMVT | A1 | F4 |
| IMVT | A2 | F4 |
| IONS | A1 | F6 |
| IONS | A2 | F6 |
| KGS | A1 | F5 |
| KGS | A2 | F5 |
| KKR | A1 | F3 |
| KKR | A2 | F3 |
| KSPI | A1 | F4 |
| KSPI | A2 | F4 |
| LINC | A1 | F3 |
| LINC | A2 | F3 |
| MNDY | A1 | F6 |
| MNDY | A2 | F6 |
| MUX | A1 | F3 |
| MUX | A2 | F3 |
| NESR | A1 | F5 |
| NESR | A2 | F5 |
| NRG | A1 | F5 |
| NRG | A2 | F5 |
| NRXS | A1 | F2 |
| NRXS | A2 | F2 |
| OCUL | A1 | F2 |
| OCUL | A2 | F2 |
| OFIX | A1 | F2 |
| OFIX | A2 | F2 |
| PRAX | A1 | F5 |
| PRAX | A2 | F5 |
| RBA | A1 | F5 |
| RBA | A2 | F5 |
| RDNT | A1 | F4 |
| RDNT | A2 | F4 |
| ROIV | A1 | F5 |
| ROIV | A2 | F5 |
| SBET | A1 | F2 |
| SBET | A2 | F2 |
| SGC | A1 | F3 |
| SGC | A2 | F3 |
| SGI | A1 | F5 |
| SGI | A2 | F5 |
| SOHU | A1 | F3 |
| SOHU | A2 | F3 |
| TGTX | A1 | F5 |
| TGTX | A2 | F5 |
| TH | A1 | F3 |
| TH | A2 | F3 |
| TPB | A1 | F3 |
| TPB | A2 | F3 |
| UNIT | A1 | F2 |
| UNIT | A2 | F2 |
| VIA | A1 | F4 |
| VIA | A2 | F4 |
| WHF | A1 | F2 |
| WHF | A2 | F2 |
| WTTR | A1 | F4 |
| WTTR | A2 | F4 |

## Exploration book tonight (8; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| B | SS | 2026-11-13T00:00:00.000 | 40.50 | 2.55 | +5.78% | 826.70 | F3 |
| CEG | SS | 2026-11-13T00:00:00.000 | 250.00 | 19.06 | +7.06% | 5,736.74 | F3 |
| CEG | IC | 2026-11-13T00:00:00.000 | 250.00 | 18.48 | +6.79% | 3,152.10 | F3 |
| FRVO | SS | 2026-11-20T00:00:00.000 | 9.00 | 1.75 | +16.50% | 411.36 | F2 |
| IONS | SS | 2026-11-20T00:00:00.000 | 40.00 | 5.63 | +13.27% | 1,139.32 | F6 |
| MNDY | SS | 2026-11-20T00:00:00.000 | 90.00 | 18.06 | +19.40% | 3,573.57 | F6 |
| MNDY | IC | 2026-11-20T00:00:00.000 | 90.00 | 16.83 | +17.60% | 2,317.20 | F6 |
| RDNT | SS | 2026-11-20T00:00:00.000 | 75.00 | 8.82 | +10.92% | 1,665.77 | F4 |

## Graded today (21)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| DKNG | A1 | SS | champion | -22.16% | -521.07 | 1 | no |
| VST | A1 | SS | champion | +1.18% | 133.27 | 1 | no |
| DKNG | A2 | SS | champion | -22.16% | -521.07 | 1 | no |
| VST | A2 | SS | champion | +1.18% | 133.27 | 1 | no |
| ABNB | A1 | SS | exploration | -3.97% | -673.64 | 1 | no |
| CLMT | A1 | SS | exploration | -0.38% | -16.65 | 1 | no |
| DKNG | A1 | SS | exploration | -22.16% | -521.07 | 1 | no |
| DOCS | A1 | SS | exploration | +6.57% | 218.86 | 1 | no |
| DOCS | A1 | IC | exploration | +4.09% | 136.20 | 1 | no |
| DVN | A1 | SS | exploration | -3.06% | -130.90 | 1 | no |
| INOD | A1 | SS | exploration | -1.40% | -54.13 | 2 | no |
| IONQ | A1 | SS | exploration | +1.00% | 26.38 | 1 | no |
| IREN | A1 | SS | exploration | -0.77% | -14.06 | 1 | no |
| MAT | A1 | SS | exploration | +3.31% | 49.59 | 2 | no |
| MRNA | A1 | SS | exploration | +0.20% | 48.48 | 1 | no |
| MRNA | A1 | IC | exploration | -1.14% | -274.03 | 1 | no |
| OKLO | A1 | SS | exploration | -4.15% | -80.38 | 1 | no |
| VSAT | A1 | SS | exploration | -0.44% | -26.31 | 2 | no |
| VST | A1 | SS | exploration | +1.18% | 133.27 | 1 | no |
| WK | A1 | SS | exploration | -6.39% | -545.22 | 1 | no |
| WULF | A1 | SS | exploration | +2.68% | 26.86 | 1 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 8 | 6 | +0.63% | 1.12 | 245.49 |
| sa-1.0 | champion | A1 | SS | 31 | 14 | -0.84% | -1.04 | -1,532.86 |
| sa-1.0 | champion | A2 | IC | 7 | 5 | +0.66% | 1.00 | 233.18 |
| sa-1.0 | champion | A2 | SS | 24 | 13 | -0.62% | -0.60 | -427.45 |
| sa-1.0 | exploration | A1 | IC | 49 | 20 | -1.52% | -2.25 | -9,640.45 |
| sa-1.0 | exploration | A1 | SS | 238 | 23 | -1.15% | -4.93 | -23,851.78 |

Ledger: emitted 0 (skipped 0), exploration 8 (skipped 0), graded 21; ledger open.

## S-B state
Gate (2026-11-06, from 2026-11-05 closes): SPY OFF:G1 (VIX 28.18, VIX3M 25.55, X 28.18 vs median 17.255) · QQQ OFF:G1 (VIX 28.18, VIX3M 25.55, X 38.26 vs median 25.13)

Next session (2026-11-09, from 2026-11-06 closes): SPY OFF:G1 (VIX 25.64, VIX3M 24.6, X 25.64 vs median 17.415) · QQQ OFF:G1 (VIX 25.64, VIX3M 24.6, X 34.02 vs median 25.2)

CBOE refresh: ok through 2026-11-06; index-vol through 2026-11-06

Entry day: yes.

### S-B positions tonight (0)
_none_

### S-B skipped (4)
| underlying | structure | reason |
|---|---|---|
| SPY | PS | OFF:G1 |
| SPY | IC | OFF:G1 |
| QQQ | PS | OFF:G1 |
| QQQ | IC | OFF:G1 |

### S-B exploration book tonight (3; one contract per sleeve, gate ignored, gate verdict recorded)
| underlying | structure | expiry | k_p1 | k_p2 | k_c1 | k_c2 | credit_entry | max_loss_usd | gate_verdict |
|---|---|---|---|---|---|---|---|---|---|
| SPY | PS | 2026-11-27 | 690.00 | 655.00 | — | — | 1.86 | 3,313.51 | OFF:G1 |
| QQQ | PS | 2026-11-27 | 600.00 | 550.00 | — | — | 3.68 | 4,632.27 | OFF:G1 |
| QQQ | IC | 2026-11-27 | 600.00 | 550.00 | 710.00 | 754.00 | 5.09 | 4,490.97 | OFF:G1 |

### S-B graded at expiry today (6)
| underlying | structure | entry | expiry | settle_close | net_usd | ror | role |
|---|---|---|---|---|---|---|---|
| SPY | PS | 2026-10-16 | 2026-11-06 | 735.24 | 158.37 | +4.48% | champion |
| QQQ | PS | 2026-10-16 | 2026-11-06 | 656.17 | -576.72 | -12.31% | champion |
| QQQ | IC | 2026-10-16 | 2026-11-06 | 656.17 | -454.25 | -9.97% | champion |
| SPY | PS | 2026-10-16 | 2026-11-06 | 735.24 | 158.37 | +4.48% | exploration |
| QQQ | PS | 2026-10-16 | 2026-11-06 | 656.17 | -576.72 | -12.31% | exploration |
| QQQ | IC | 2026-10-16 | 2026-11-06 | 656.17 | -454.25 | -9.97% | exploration |

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

S-B ledger: emitted 0 (skipped 0), exploration 3 (skipped 0), graded 6; ledger open.


## S-C state
Entry day: yes; ledger open.

Stopped at: F1 2252 · F2 1137 · F3 986 · F4 773 · F7 672 · F5 50 · F6 23 · F8 75 · F9 3; C1:selected 1 · C2:selected 1

### S-C positions tonight (4; paper, before the read)
| variant | rank | ticker | sector | structure | close | iv30d | expiry | dte_cal | k | k_up | k_dn | credit_entry | max_loss_usd | stress_loss_usd | entry_cost_usd | contracts | sigma_hold | cap_pass | cap_reason |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 | 1 | NCLH | Consumer Cyclical | IB | 17.93 | 0.49 | 2026-12-04 | 28 | 18.00 | 23.00 | 13.00 | 1.78 | 321.51 | — | 6.22 | 1 | 2.43 | yes | — |
| C1 | 1 | NCLH | Consumer Cyclical | SS | 17.93 | 0.49 | 2026-12-04 | 28 | 18.00 | — | — | 1.90 | — | 545.52 | 4.35 | 1 | 2.43 | yes | — |
| C2 | 1 | NCLH | Consumer Cyclical | IB | 17.93 | 0.49 | 2026-12-04 | 28 | 18.00 | 23.00 | 13.00 | 1.78 | 321.51 | — | 6.22 | 1 | 2.43 | yes | — |
| C2 | 1 | NCLH | Consumer Cyclical | SS | 17.93 | 0.49 | 2026-12-04 | 28 | 18.00 | — | — | 1.90 | — | 545.52 | 4.35 | 1 | 2.43 | yes | — |

Exploration book: 31 priceable names at one contract each, by first failing filter: F1 6, F2 1, F3 16, F5 2, F6 2, F9 3, PASS 1

### S-C graded at expiry (4)
| ticker | variant | structure | E | expiry | settle_close | settle_source | corporate_action | net_usd | ror |
|---|---|---|---|---|---|---|---|---|---|
| OKLO | C1 | IB | 2026-10-09 | 2026-11-06 | 23.55 | daily_contract | — | -590.04 | -70.69% |
| OKLO | C1 | SS | 2026-10-09 | 2026-11-06 | 23.55 | daily_contract | — | -559.79 | -38.24% |
| OKLO | C2 | IB | 2026-10-09 | 2026-11-06 | 23.55 | daily_contract | — | -590.04 | -70.69% |
| OKLO | C2 | SS | 2026-10-09 | 2026-11-06 | 23.55 | daily_contract | — | -559.79 | -38.24% |

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

S-C ledger: emitted 4 (skipped 0), exploration 62 (skipped 0), graded 126.


## Watch basket (wb-1.0, exploration, paper only)
Universe: 2027 names.
Borrow snapshot: 2026-11-06 (the session's own); fee known for 2019 names.
Bull counts: 0:741, 1:759, 2:384, 3:121, 4:21, 5:1, 6:0, 7:0, 8:0
Bear counts: 0:619, 1:784, 2:403, 3:181, 4:36, 5:4, 6:0, 7:0, 8:0

### LONG (61)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AER | 4 | 0 | no | x | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| AMAL | 3 | 0 | no | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| ASND | 3 | 0 | no |  |  | x |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| ATHM | 4 | 0 | yes |  | x |  | x | x | x | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| BJ | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| BLBD | 3 | 0 | no |  | x | x |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BRKB | 4 | 0 | no | x | x |  |  |  | x | x |  |  | ? |  |  |  |  | ? |  |  |  | x | x |
| BUD | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CAE | 3 | 0 | no |  | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| CCK | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| CHT | 4 | 0 | no | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| CNMD | 3 | 0 | no | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| COST | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| CUBE | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| DEO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DLX | 3 | 0 | no |  |  | x |  | x | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| EBAY | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EHC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EW | 3 | 0 | yes | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| EXC | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EXR | 4 | 0 | no | x | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| FAST | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| FMS | 4 | 0 | no |  | x |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| FTS | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  | ? |  |  |  |  | x |
| FWONA | 3 | 0 | no | x |  |  |  | x | x | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| FWONK | 3 | 0 | no | x |  |  |  | x | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| GIB | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| GIII | 3 | 0 | no |  | x |  |  | x | x |  |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HLT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HR | 3 | 0 | no |  | x |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| HTO | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HZO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| INSM | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| IPAR | 4 | 0 | no | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| KO | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| LH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MA | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| MCBS | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| MDT | 3 | 0 | yes | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| MMM | 3 | 0 | no |  | x |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| MSCI | 3 | 0 | no |  | x |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| MSEX | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| NDAQ | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| NWE | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| NXT | 3 | 0 | yes |  | x | x |  | x |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| PFGC | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PGNY | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| POR | 4 | 0 | no |  | x | x |  | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| RSG | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| SBSI | 3 | 0 | no |  | x |  |  |  | x | x |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| SMA | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| SPNT | 4 | 0 | no | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| TRAX | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| TW | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| USPH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| V | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| VIPS | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| VLTO | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| VMC | 3 | 0 | no |  | x |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| WFG | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |

### SHORT (92)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| ACI | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| AKAM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| ALAB | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| ALNY | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  | x |  | x |
| AMR | 0 | 4 | yes |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  |  |
| ANIP | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| ARM | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| ASST | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| AXON | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| AXSM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  | x |  | x |
| BA | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| BBIO | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| BDC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| BTU | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  | x |  | x |  |  |
| BX | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| CAKE | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| CAR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| CC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? |  |  |  |  | x |
| CFR | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| CHRD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? |  |  |  |  | x |
| CLMT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? | x | x |  |  | ? | x |  |  |  | x |
| CNQ | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x | x |  | x |  | ? |  |  |  |  | x |
| COHR | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| COIN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  | x | x |
| CRCL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| CVE | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| CYTK | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| DASH | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? |  |  |  |  | x |
| ECHO | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| ENPH | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? |  |  |  |  | x |
| FICO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| FIG | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| FIVN | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| FLG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  | x |
| FLUT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? |  |  |  |  | x |
| FSLY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| GH | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| GIL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  |  |
| GL | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| GNTX | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  |  |
| GRAL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| GTES | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| HIMS | 0 | 5 | no |  |  |  |  |  |  | ? |  |  | x | x | x | x |  | ? | x |  |  |  | x |
| HONA | 0 | 3 | yes |  |  | ? |  |  |  | ? |  | x |  |  | x |  | x | ? |  |  | x |  | x |
| HTGC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| IEX | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| IMAX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| IMO | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? |  |  |  |  | x |
| INOD | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| INVA | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| IRTC | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x | x |  | ? |  |  |  |  | x |
| KBH | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| LITE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| LUNR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| LYFT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| MATX | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| MELI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| META | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| MGY | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| MNDY | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| MSGE | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | ? |  |  | x | x | ? | x |  |  |  |  |
| MSTR | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| MTDR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| NFG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? |  |  |  |  | x |
| NFLX | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  | x | x |
| NRIX | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  | x | x |  | ? | x |  |  |  |  |
| NWS | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  |  |
| NWSA | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| OKE | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| OXY | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  | x |  | x | x | ? |  |  |  |  | x |
| PBI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| PTGX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| REG | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| RH | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| RIVN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| SGHC | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x | x | x |  |  |  |  |  |  |  |  |
| SGI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| SHC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| SHOO | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  |  |
| SLF | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x | ? |  |  |  |  |  |
| SPCX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| SRPT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| ST | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| TDW | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| TEN | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | ? |  | x | x |  | ? | x |  |  |  |  |
| TPL | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| TSEM | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| VCYT | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x | x |  | ? |  |  |  |  | x |
| WGS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| WSO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| ZD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |

### VOL (0)
_none_

CONFLICT (logged only, never a basket, DESIGN/110 §3): 116.

Ledger: emitted 153 (skipped 0), graded 534; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
