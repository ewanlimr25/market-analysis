# S-A daily — 2026-10-30 (S3)

Preflight: WARN — prices.parquet ends 2026-10-23, BEFORE the 2026-10-30 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-10-23, BEFORE the 2026-10-30 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-10-23, BEFORE the 2026-10-30 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (0)
_no event tonight clears the filters._

## Suppressed (40)
| ticker | variant | first_fail |
|---|---|---|
| AKR | A1 | F4 |
| AKR | A2 | F4 |
| AXSM | A1 | F5 |
| AXSM | A2 | F5 |
| CHH | A1 | F5 |
| CHH | A2 | F5 |
| CHKP | A1 | F6 |
| CHKP | A2 | F6 |
| CIFR | A1 | F2 |
| CIFR | A2 | F2 |
| CNA | A1 | F4 |
| CNA | A2 | F4 |
| EL | A1 | F6 |
| EL | A2 | F6 |
| ETR | A1 | F3 |
| ETR | A2 | F3 |
| FOX | A1 | F4 |
| FOX | A2 | F4 |
| FOXA | A1 | F5 |
| FOXA | A2 | F5 |
| IDXX | A1 | F5 |
| IDXX | A2 | F5 |
| III | A1 | F2 |
| III | A2 | F2 |
| KRYS | A1 | F5 |
| KRYS | A2 | F5 |
| L | A1 | F5 |
| L | A2 | F5 |
| LTBR | A1 | F2 |
| LTBR | A2 | F2 |
| MAR | A1 | F3 |
| MAR | A2 | F3 |
| PEG | A1 | F5 |
| PEG | A2 | F5 |
| RYAAY | A1 | F5 |
| RYAAY | A2 | F5 |
| TEM | A1 | F6 |
| TEM | A2 | F6 |
| TSEM | A1 | F5 |
| TSEM | A2 | F5 |

## Exploration book tonight (4; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| CHKP | SS | 2026-11-20T00:00:00.000 | 150.00 | 17.91 | +11.00% | 2,998.44 | F6 |
| CHKP | IC | 2026-11-20T00:00:00.000 | 150.00 | 15.61 | +8.98% | 1,938.88 | F6 |
| EL | SS | 2026-11-06T00:00:00.000 | 109.00 | 11.29 | +8.77% | 2,448.05 | F6 |
| TEM | SS | 2026-11-06T00:00:00.000 | 72.00 | 9.24 | +12.10% | 2,798.06 | F6 |

## Graded today (18)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| RIVN | A1 | SS | champion | +3.10% | 71.07 | 1 | no |
| COIN | A1 | SS | champion | -2.91% | -468.07 | 1 | no |
| LYB | A1 | SS | champion | -0.73% | -47.72 | 1 | no |
| RIVN | A2 | SS | champion | +3.10% | 71.07 | 1 | no |
| LYB | A2 | SS | champion | -0.73% | -47.72 | 1 | no |
| AN | A1 | SS | exploration | -4.94% | -838.65 | 2 | no |
| AXTI | A1 | SS | exploration | +2.08% | 127.58 | 1 | no |
| COIN | A1 | SS | exploration | -2.91% | -468.07 | 1 | no |
| FSLR | A1 | SS | exploration | +1.83% | 324.71 | 1 | no |
| LYB | A1 | SS | exploration | -0.73% | -47.72 | 1 | no |
| MSTR | A1 | SS | exploration | -3.93% | -556.82 | 1 | no |
| NWL | A1 | SS | exploration | -8.45% | -43.23 | 1 | no |
| PINS | A1 | SS | exploration | +3.06% | 61.02 | 1 | no |
| RBLX | A1 | SS | exploration | -2.86% | -149.15 | 1 | no |
| RDDT | A1 | SS | exploration | -11.89% | -1,542.83 | 1 | no |
| RIVN | A1 | SS | exploration | +3.10% | 35.54 | 1 | no |
| VALE | A1 | SS | exploration | -0.40% | -4.44 | 1 | no |
| WY | A1 | SS | exploration | -1.60% | -31.56 | 1 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 6 | 4 | +0.80% | 0.99 | 268.43 |
| sa-1.0 | champion | A1 | SS | 21 | 10 | -0.15% | -0.26 | -1,097.49 |
| sa-1.0 | champion | A2 | IC | 6 | 4 | +0.80% | 0.99 | 268.43 |
| sa-1.0 | champion | A2 | SS | 20 | 10 | -0.01% | -0.01 | -629.42 |
| sa-1.0 | exploration | A1 | IC | 31 | 15 | -1.52% | -1.70 | -2,761.49 |
| sa-1.0 | exploration | A1 | SS | 144 | 18 | -0.94% | -3.03 | -10,469.70 |

Ledger: emitted 0 (skipped 0), exploration 4 (skipped 0), graded 18; ledger open.

## S-B state
Gate (2026-10-30, from 2026-10-29 closes): SPY ON (VIX 17.2, VIX3M 19.37, X 17.2 vs median 16.57) · QQQ ON (VIX 17.2, VIX3M 19.37, X 25.18 vs median 22.795)

Next session (2026-11-02, from 2026-10-30 closes): SPY ON (VIX 19.42, VIX3M 20.78, X 19.42 vs median 16.775) · QQQ ON (VIX 19.42, VIX3M 20.78, X 28.5 vs median 23.335)

CBOE refresh: ok through 2026-10-30; index-vol through 2026-10-30

Entry day: yes.

### S-B positions tonight (4)
| underlying | structure | expiry | k_p1 | k_p2 | k_c1 | k_c2 | credit_entry | max_loss_usd | contracts | entry_tier_max |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY | PS | 2026-11-20 | 721.00 | 685.00 | — | — | 2.83 | 3,316.62 | 1 | 1 |
| SPY | IC | 2026-11-20 | 721.00 | 685.00 | 791.00 | 825.00 | 3.47 | 3,253.37 | 1 | 1 |
| QQQ | PS | 2026-11-20 | 645.00 | 595.00 | — | — | 3.74 | 4,625.69 | 1 | 1 |
| QQQ | IC | 2026-11-20 | 645.00 | 595.00 | 738.00 | 786.00 | 5.35 | 4,465.08 | 1 | 1 |

### S-B exploration book tonight (4; one contract per sleeve, gate ignored, gate verdict recorded)
| underlying | structure | expiry | k_p1 | k_p2 | k_c1 | k_c2 | credit_entry | max_loss_usd | gate_verdict |
|---|---|---|---|---|---|---|---|---|---|
| SPY | PS | 2026-11-20 | 721.00 | 685.00 | — | — | 2.83 | 3,316.62 | ON |
| SPY | IC | 2026-11-20 | 721.00 | 685.00 | 791.00 | 825.00 | 3.47 | 3,253.37 | ON |
| QQQ | PS | 2026-11-20 | 645.00 | 595.00 | — | — | 3.74 | 4,625.69 | ON |
| QQQ | IC | 2026-11-20 | 645.00 | 595.00 | 738.00 | 786.00 | 5.35 | 4,465.08 | ON |

### S-B graded at expiry today (4)
| underlying | structure | entry | expiry | settle_close | net_usd | ror | role |
|---|---|---|---|---|---|---|---|
| QQQ | PS | 2026-10-09 | 2026-10-30 | 691.11 | -2,085.92 | -56.50% | champion |
| SPY | PS | 2026-10-09 | 2026-10-30 | 756.10 | 120.10 | +4.49% | exploration |
| SPY | IC | 2026-10-09 | 2026-10-30 | 756.10 | 180.96 | +6.93% | exploration |
| QQQ | PS | 2026-10-09 | 2026-10-30 | 691.11 | -2,085.92 | -56.50% | exploration |

Open positions: QQQ-IC 3, QQQ-PS 3, SPY-IC 1, SPY-PS 3

### S-B forward ledger to date
| policy_id | role | sleeve | n | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|---|
| sb-1.0 | champion | QQQ-IC | 3 | +1.40% | 0.34 | 228.84 |
| sb-1.0 | champion | QQQ-PS | 4 | -15.42% | -1.22 | -2,226.57 |
| sb-1.0 | champion | SPY-IC | 2 | — | — | 372.65 |
| sb-1.0 | champion | SPY-PS | 3 | +5.06% | 34.39 | 400.25 |
| sb-1.0 | exploration | QQQ-IC | 3 | +1.40% | 0.34 | 228.84 |
| sb-1.0 | exploration | QQQ-PS | 5 | -10.96% | -0.92 | -2,014.38 |
| sb-1.0 | exploration | SPY-IC | 4 | +6.91% | 31.77 | 724.42 |
| sb-1.0 | exploration | SPY-PS | 5 | +4.98% | 25.88 | 644.67 |

S-B ledger: emitted 4 (skipped 0), exploration 4 (skipped 0), graded 4; ledger open.


## S-C state
Entry day: yes; ledger open.

Stopped at: F1 2259 · F2 1117 · F3 1004 · F4 806 · F7 63 · F5 406 · F6 91 · F8 225 · F9 6; C1:selected 3 · C2:selected 3

### S-C positions tonight (12; paper, before the read)
| variant | rank | ticker | sector | structure | close | iv30d | expiry | dte_cal | k | k_up | k_dn | credit_entry | max_loss_usd | stress_loss_usd | entry_cost_usd | contracts | sigma_hold | cap_pass | cap_reason |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 | 1 | DINO | Energy | IB | 115.09 | 0.56 | 2026-11-20 | 21 | 115.00 | 145.00 | 85.00 | 11.97 | 1,802.94 | — | 41.93 | 1 | 15.43 | yes | — |
| C1 | 2 | WHR | Consumer Cyclical | IB | 29.95 | 0.65 | 2026-11-20 | 21 | 30.00 | 40.00 | 20.00 | 3.68 | 631.71 | — | 11.03 | 1 | 4.68 | yes | — |
| C1 | 3 | RDDT | Communication Services | IB | 91.65 | 0.66 | 2026-11-27 | 28 | 90.00 | 125.00 | 58.00 | 12.88 | 2,211.63 | — | 44.46 | 1 | 16.86 | no | cap_budget |
| C1 | 1 | DINO | Energy | SS | 115.09 | 0.56 | 2026-11-20 | 21 | 115.00 | — | — | 12.42 | — | 3,396.83 | 25.21 | 1 | 15.43 | yes | — |
| C1 | 2 | WHR | Consumer Cyclical | SS | 29.95 | 0.65 | 2026-11-20 | 21 | 30.00 | — | — | 3.80 | — | 1,028.24 | 9.21 | 1 | 4.68 | yes | — |
| C1 | 3 | RDDT | Communication Services | SS | 91.65 | 0.66 | 2026-11-27 | 28 | 90.00 | — | — | 13.24 | — | 3,897.22 | 41.56 | 1 | 16.86 | no | cap_budget |
| C2 | 1 | DINO | Energy | IB | 115.09 | 0.56 | 2026-11-20 | 21 | 115.00 | 145.00 | 85.00 | 11.97 | 1,802.94 | — | 41.93 | 1 | 15.43 | yes | — |
| C2 | 2 | WHR | Consumer Cyclical | IB | 29.95 | 0.65 | 2026-11-20 | 21 | 30.00 | 40.00 | 20.00 | 3.68 | 631.71 | — | 11.03 | 1 | 4.68 | yes | — |
| C2 | 3 | RDDT | Communication Services | IB | 91.65 | 0.66 | 2026-11-27 | 28 | 90.00 | 125.00 | 58.00 | 12.88 | 2,211.63 | — | 44.46 | 1 | 16.86 | no | cap_budget |
| C2 | 1 | DINO | Energy | SS | 115.09 | 0.56 | 2026-11-20 | 21 | 115.00 | — | — | 12.42 | — | 3,396.83 | 25.21 | 1 | 15.43 | yes | — |
| C2 | 2 | WHR | Consumer Cyclical | SS | 29.95 | 0.65 | 2026-11-20 | 21 | 30.00 | — | — | 3.80 | — | 1,028.24 | 9.21 | 1 | 4.68 | yes | — |
| C2 | 3 | RDDT | Communication Services | SS | 91.65 | 0.66 | 2026-11-27 | 28 | 90.00 | — | — | 13.24 | — | 3,897.22 | 41.56 | 1 | 16.86 | no | cap_budget |

Exploration book: 109 priceable names at one contract each, by first failing filter: F1 32, F2 3, F3 48, F4 4, F5 13, F9 6, PASS 3

### S-C graded at expiry (18)
| ticker | variant | structure | E | expiry | settle_close | settle_source | corporate_action | net_usd | ror |
|---|---|---|---|---|---|---|---|---|---|
| WULF | C1 | IB | 2026-10-02 | 2026-10-30 | 11.73 | daily_contract | — | -135.29 | -33.51% |
| MARA | C1 | IB | 2026-10-02 | 2026-10-30 | 6.76 | daily_contract | — | -295.57 | -93.14% |
| QBTS | C1 | IB | 2026-10-02 | 2026-10-30 | 10.64 | daily_contract | — | -283.01 | -72.35% |
| CRCL | C1 | IB | 2026-10-02 | 2026-10-30 | 72.53 | daily_contract | — | 296.24 | +15.33% |
| OKLO | C1 | IB | 2026-10-02 | 2026-10-30 | 25.25 | daily_contract | — | -511.52 | -55.76% |
| WULF | C1 | SS | 2026-10-02 | 2026-10-30 | 11.73 | daily_contract | — | -115.59 | -16.43% |
| MARA | C1 | SS | 2026-10-02 | 2026-10-30 | 6.76 | daily_contract | — | -282.66 | -50.61% |
| QBTS | C1 | SS | 2026-10-02 | 2026-10-30 | 10.64 | daily_contract | — | -271.04 | -41.33% |
| CRCL | C1 | SS | 2026-10-02 | 2026-10-30 | 72.53 | daily_contract | — | 352.05 | +10.74% |
| OKLO | C1 | SS | 2026-10-02 | 2026-10-30 | 25.25 | daily_contract | — | -485.12 | -32.46% |
| WULF | C2 | IB | 2026-10-02 | 2026-10-30 | 11.73 | daily_contract | — | -135.29 | -33.51% |
| MARA | C2 | IB | 2026-10-02 | 2026-10-30 | 6.76 | daily_contract | — | -295.57 | -93.14% |
| CRCL | C2 | IB | 2026-10-02 | 2026-10-30 | 72.53 | daily_contract | — | 296.24 | +15.33% |
| OKLO | C2 | IB | 2026-10-02 | 2026-10-30 | 25.25 | daily_contract | — | -511.52 | -55.76% |
| WULF | C2 | SS | 2026-10-02 | 2026-10-30 | 11.73 | daily_contract | — | -115.59 | -16.43% |
| MARA | C2 | SS | 2026-10-02 | 2026-10-30 | 6.76 | daily_contract | — | -282.66 | -50.61% |
| CRCL | C2 | SS | 2026-10-02 | 2026-10-30 | 72.53 | daily_contract | — | 352.05 | +10.74% |
| OKLO | C2 | SS | 2026-10-02 | 2026-10-30 | 25.25 | daily_contract | — | -485.12 | -32.46% |

### S-C open book (S-B open: yes; the 40% budget binds only then)
| pair | positions | open_risk_usd | budget_usd | max_sector_positions |
|---|---|---|---|---|
| C1-SS | 3 | 5,111.92 | 8,000.00 | 1 |
| C1-IB | 2 | 2,434.65 | 4,000.00 | 1 |
| C2-SS | 3 | 5,888.76 | 8,000.00 | 1 |
| C2-IB | 3 | 2,788.73 | 4,000.00 | 1 |

### S-C forward ledger to date (entry-week series)
| policy_id | role | pair | n | weeks | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|---|---|
| sc-1.0 | champion | C1-SS | 5 | 1 | — | — | -802.36 |
| sc-1.0 | champion | C1-IB | 5 | 1 | — | — | -929.16 |
| sc-1.0 | champion | C2-SS | 4 | 1 | — | — | -531.32 |
| sc-1.0 | champion | C2-IB | 4 | 1 | — | — | -646.15 |
| sc-1.0 | exploration | C1-SS | 81 | 1 | — | — | -70,974.83 |
| sc-1.0 | exploration | C1-IB | 81 | 1 | — | — | -75,280.86 |

Progress to the read: graded entry-weeks 1 of 40 (C1-SS), 1 of 40 (C1-IB), 1 of 40 (C2-SS), 1 of 40 (C2-IB)

S-C ledger: emitted 12 (skipped 0), exploration 217 (skipped 0), graded 180.


## Watch basket (wb-1.0, exploration, paper only)
Universe: 2006 names.
Borrow snapshot: 2026-10-30 (the session's own); fee known for 1999 names.
Bull counts: 0:690, 1:719, 2:406, 3:164, 4:26, 5:1, 6:0, 7:0, 8:0
Bear counts: 0:752, 1:767, 2:313, 3:138, 4:31, 5:5, 6:0, 7:0, 8:0

### LONG (109)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ABBV | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| ABM | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| ADC | 3 | 0 | no |  | x |  | x | x |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| ADI | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ADP | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ADUS | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| AFG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ALRM | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| AMRX | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| APG | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AXS | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BFST | 3 | 0 | yes | x |  |  |  |  | x | x |  |  | ? | ? |  |  |  |  |  |  |  |  |  |
| BIIB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| BLK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BOOT | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BRKB | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| CAH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CB | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CBZ | 3 | 0 | no | x |  |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| CCK | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CHT | 4 | 0 | no | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| CNH | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| CNM | 3 | 0 | yes |  |  | x |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| CNO | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| COLM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| CON | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| COST | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| CSL | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| CUBE | 3 | 0 | no | x | x |  |  |  |  | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| DCOM | 3 | 0 | no | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DHR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DLTR | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DNOW | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| DOW | 3 | 0 | no |  | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| E | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| ECL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EHC | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EPC | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| EPRT | 3 | 0 | no |  | x |  | x |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| FLYW | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| FTS | 4 | 0 | no | x | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  | x |
| GMAB | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| GWW | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| HASI | 3 | 0 | no |  | x |  |  | x |  | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| HLT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ICE | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| J | 3 | 0 | yes | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| KNTK | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| LFST | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| LH | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| LNG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LTH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| MA | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| MAR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MAS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MCBS | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| MCK | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MD | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| MORN | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| MRSH | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MSCI | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| NDAQ | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| NGG | 3 | 0 | yes |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  |  |
| NUE | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| NWE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| NXPI | 4 | 0 | no |  |  | x |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ONC | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| OPLN | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  |
| PKG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PNTG | 3 | 0 | no | x | x |  |  |  | x |  |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| PPG | 4 | 0 | no |  |  | x |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PRGS | 3 | 0 | yes | x |  |  |  |  | x | x |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| R | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RLJ | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| RPRX | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| RS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| RSG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SBH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| SDRL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| SIGI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| SJM | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SMA | 4 | 0 | no | x | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| SNPS | 3 | 0 | no |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SO | 3 | 0 | yes |  | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| SPNT | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| STGW | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| SUNB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TAK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| TFX | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| THG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TILE | 3 | 0 | no |  | x |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| TOL | 3 | 0 | yes |  | x |  |  | x | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| TRGP | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TTC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TTE | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| TW | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| URI | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| UVE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| V | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| VLTO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VRSN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VRTX | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| VTRS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| WCN | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WDFC | 3 | 0 | yes |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| WPP | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| WSM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WTRG | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |

### SHORT (72)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| AI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  |  |
| ALAB | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| ALG | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  | x |  | x |  |  |  |  |
| ALNY | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? | x |  | x |  | x |
| ASTS | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? |  |  |  | x | x |
| BCE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| BMNR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| BMO | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| BNL | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  |  |
| BRKR | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| CAR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  |  |
| CAT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  | x | x | x |
| CDE | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  | x |
| CLH | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  | x |
| CLS | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| COIN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  | x | x |
| CRCL | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| CRWV | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| DBD | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| DCI | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  |  | x | x |  |  |  | x |
| DMC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| DUOL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| ENPH | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  |  | x |
| FIG | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| FLY | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  |  |
| FNV | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| FSLY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| GOOG | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  | x | x |
| GOOGL | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| GPC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| HUBB | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| INTC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| KTB | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| LEU | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  | x |  |  |
| LI | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? | x |  |  |  |  |
| LITE | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  | x | x |
| MDLN | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? |  |  |  |  | x |
| MELI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| META | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| MKC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| MP | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  |  |  |  |  |  | x |
| MRVL | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| MSTR | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| NBIS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| NFLX | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  | x | x |
| NOW | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| NU | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  | x |  | ? |  |  |  |  | x |
| NVAX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  |  |
| OKLO | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  | x |  | x |
| ORCL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| PBI | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x | ? | x |  |  |  |  |
| PFSI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| PINS | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| QCOM | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| QNT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| RDDT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| RSI | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  | x |  |  |  | x |  | x |  | x |
| SE | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| SEDG | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  |  |  |  |
| SMCI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| SOLV | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| SPCX | 0 | 4 | no |  |  | ? |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| STRA | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  | x | x | ? | x |  |  |  |  |
| STRL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| TFII | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  | x |
| TMDX | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  |  |
| TWST | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| UPST | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? |  |  |  |  | x |
| VALE | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  | x |  | x |
| WIX | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| XP | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? |  |  |  |  | x |

### VOL (1)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GME | 0 | 2 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? |  | x |  | x | x |

CONFLICT (logged only, never a basket, DESIGN/110 §3): 74.

Ledger: emitted 182 (skipped 0), graded 542; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
