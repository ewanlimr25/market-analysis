# S-A daily — 2026-10-09 (S3)

Preflight: WARN — prices.parquet ends 2026-10-02, BEFORE the 2026-10-09 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-10-02, BEFORE the 2026-10-09 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-10-02, BEFORE the 2026-10-09 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (0)
_no event tonight clears the filters._

## Suppressed (0)
_none_

## Graded today (2)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| DAL | A1 | SS | exploration | +1.04% | 85.83 | 1 | no |
| DAL | A1 | IC | exploration | -0.50% | -41.26 | 1 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 2 | 2 | +2.69% | 3.42 | 232.76 |
| sa-1.0 | champion | A1 | SS | 2 | 2 | +3.83% | 3.98 | 328.86 |
| sa-1.0 | champion | A2 | IC | 2 | 2 | +2.69% | 3.42 | 232.76 |
| sa-1.0 | champion | A2 | SS | 2 | 2 | +3.83% | 3.98 | 328.86 |
| sa-1.0 | exploration | A1 | IC | 6 | 5 | +0.37% | 0.40 | -86.72 |
| sa-1.0 | exploration | A1 | SS | 7 | 5 | +1.50% | 1.80 | 435.41 |

Ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 2; ledger open.

## S-B state
Gate (2026-10-09, from 2026-10-08 closes): SPY OFF:G2 (VIX 15.41, VIX3M 18.08, X 15.41 vs median 15.594999999999999) · QQQ ON (VIX 15.41, VIX3M 18.08, X 21.98 vs median 21.22)

Next session (2026-10-12, from 2026-10-09 closes): SPY OFF:G2 (VIX 14.84, VIX3M 17.77, X 14.84 vs median 15.48) · QQQ OFF:G2 (VIX 14.84, VIX3M 17.77, X 20.55 vs median 21.22)

CBOE refresh: ok through 2026-10-09; index-vol through 2026-10-09

Entry day: yes.

### S-B positions tonight (1)
| underlying | structure | expiry | k_p1 | k_p2 | k_c1 | k_c2 | credit_entry | max_loss_usd | contracts | entry_tier_max |
|---|---|---|---|---|---|---|---|---|---|---|
| QQQ | PS | 2026-10-30 | 714.00 | 675.00 | — | — | 2.08 | 3,691.86 | 1 | 1 |

### S-B skipped (3)
| underlying | structure | reason |
|---|---|---|
| SPY | PS | OFF:G2 |
| SPY | IC | OFF:G2 |
| QQQ | IC | no_tier1_c2 |

### S-B exploration book tonight (3; one contract per sleeve, gate ignored, gate verdict recorded)
| underlying | structure | expiry | k_p1 | k_p2 | k_c1 | k_c2 | credit_entry | max_loss_usd | gate_verdict |
|---|---|---|---|---|---|---|---|---|---|
| SPY | PS | 2026-10-30 | 751.00 | 723.00 | — | — | 1.24 | 2,676.25 | OFF:G2 |
| SPY | IC | 2026-10-30 | 751.00 | 723.00 | 806.00 | 832.00 | 1.88 | 2,611.82 | OFF:G2 |
| QQQ | PS | 2026-10-30 | 714.00 | 675.00 | — | — | 2.08 | 3,691.86 | ON |

### S-B graded at expiry today (3)
| underlying | structure | entry | expiry | settle_close | net_usd | ror | role |
|---|---|---|---|---|---|---|---|
| SPY | PS | 2026-09-18 | 2026-10-09 | 778.56 | 124.32 | +5.24% | exploration |
| SPY | IC | 2026-09-18 | 2026-10-09 | 778.56 | 170.81 | +5.85% | exploration |
| QQQ | PS | 2026-09-18 | 2026-10-09 | 751.18 | 212.19 | +6.89% | exploration |

Open positions: QQQ-IC 2, QQQ-PS 3, SPY-IC 2, SPY-PS 2

### S-B forward ledger to date
| policy_id | role | sleeve | n | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|---|
| sb-1.0 | champion | QQQ-IC | 1 | — | — | 321.63 |
| sb-1.0 | champion | QQQ-PS | 1 | — | — | 224.53 |
| sb-1.0 | champion | SPY-PS | 1 | — | — | 155.40 |
| sb-1.0 | exploration | QQQ-IC | 1 | — | — | 321.63 |
| sb-1.0 | exploration | QQQ-PS | 2 | — | — | 436.72 |
| sb-1.0 | exploration | SPY-IC | 1 | — | — | 170.81 |
| sb-1.0 | exploration | SPY-PS | 2 | — | — | 279.72 |

S-B ledger: emitted 1 (skipped 0), exploration 3 (skipped 0), graded 3; ledger open.


## S-C state
Entry day: yes; ledger open.

Stopped at: F1 2647 · F2 1069 · F3 996 · F4 747 · F7 687 · F5 99 · F6 6 · F8 49 · F9 3; C1:selected 1 · C2:selected 1

### S-C positions tonight (4; paper, before the read)
| variant | rank | ticker | sector | structure | close | iv30d | expiry | dte_cal | k | k_up | k_dn | credit_entry | max_loss_usd | stress_loss_usd | entry_cost_usd | contracts | sigma_hold | cap_pass | cap_reason |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 | 1 | OKLO | Utilities | IB | 34.70 | 0.65 | 2026-11-06 | 28 | 34.00 | 47.00 | 22.00 | 4.65 | 834.71 | — | 10.33 | 1 | 6.29 | no | cap_budget |
| C1 | 1 | OKLO | Utilities | SS | 34.70 | 0.65 | 2026-11-06 | 28 | 34.00 | — | — | 4.93 | — | 1,463.69 | 8.02 | 1 | 6.29 | no | cap_budget |
| C2 | 1 | OKLO | Utilities | IB | 34.70 | 0.65 | 2026-11-06 | 28 | 34.00 | 47.00 | 22.00 | 4.65 | 834.71 | — | 10.33 | 1 | 6.29 | no | cap_budget |
| C2 | 1 | OKLO | Utilities | SS | 34.70 | 0.65 | 2026-11-06 | 28 | 34.00 | — | — | 4.93 | — | 1,463.69 | 8.02 | 1 | 6.29 | yes | — |

Exploration book: 62 priceable names at one contract each, by first failing filter: F1 12, F2 4, F3 36, F5 6, F9 3, PASS 1

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

S-C ledger: emitted 4 (skipped 0), exploration 124 (skipped 0), graded 0.


## Watch basket (wb-1.0, exploration, paper only)
Universe: 1977 names.
Borrow snapshot: 2026-10-09 (the session's own); fee known for 1969 names.
Bull counts: 0:878, 1:730, 2:285, 3:76, 4:7, 5:1, 6:0, 7:0, 8:0
Bear counts: 0:552, 1:711, 2:485, 3:180, 4:43, 5:5, 6:1, 7:0, 8:0

### LONG (44)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ACA | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  |
| AMG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ANET | 3 | 0 | no | x | x |  |  |  |  | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| BP | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BPRE | 3 | 0 | no |  |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| CEG | 3 | 0 | no |  | x |  | x | x |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| CHT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| CLBT | 3 | 0 | no |  |  | x |  | x |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| CON | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| DSGR | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| E | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| EBAY | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| ECPG | 3 | 0 | no | x |  |  | x |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| ESTC | 3 | 0 | yes | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| FFIV | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| FTNT | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| GCT | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HCA | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| HGTY | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HLI | 3 | 0 | yes |  |  | x |  | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| HMC | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| HNGE | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| JCI | 3 | 0 | yes | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| JOYY | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| KFY | 3 | 0 | yes |  | x |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| LAUR | 3 | 0 | yes | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  |  |
| MCK | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| MSM | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| MTD | 4 | 0 | no | x | x |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| NVGS | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PAGS | 3 | 0 | no |  |  |  |  | x | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| PD | 3 | 0 | no | x |  |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| PG | 3 | 0 | yes |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PRSU | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| RGA | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SFL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| SHAK | 3 | 0 | no |  | x |  |  | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| SHEL | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SHOP | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TAK | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| TAL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| TW | 3 | 0 | no |  |  | x |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| UVE | 3 | 0 | no | x |  |  | x |  | x | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| ZBRA | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |

### SHORT (119)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AA | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  | x |
| AG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| ALB | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  |  | x |  |  |  | x |
| AOS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| APLD | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| ARCC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| ARM | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  | x | x |
| ATEX | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| BA | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  | x | x |
| BAC | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  |  | x |  | x |  |  |  | x |
| BLDR | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  |  | x |  |  |  | x |
| BMNR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| BMO | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| BMY | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  | x | ? | x |  |  |  | x |
| CALM | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  |  |
| CAR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  |  |  |  |  |  |  |
| CG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CIFR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| CLBK | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CM | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| CORZ | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? |  |  |  |  | x |
| CTVA | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  | x |  | ? |  |  |  |  | x |
| DHI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| ENPH | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  |  |  |  |  |  | x |
| EPR | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  |  |
| EPRT | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  |  |
| FCN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| FIBK | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| FIG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  |  |  |  |  |  | x |
| FIGR | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  | x |
| FLY | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  |  |
| FRT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  |  |
| FULT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| GBDC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| GLNG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| GLXY | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? |  |  |  |  | x |
| GRBK | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| GSK | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| GVA | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| HAPN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| HDB | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| HSY | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x |  |  |  |  |  | x |
| HTGC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  |  |
| HTO | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| HUT | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| HYMC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  |  | x |  |  |  |  |
| INCY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| INFY | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  | x | ? |  |  |  |  | x |
| INGR | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  |  |
| INSM | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  | x |  |  |  | x |
| IP | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| IREN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| IRTC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| ITRI | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| JAZZ | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| JPM | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  |  | x |  | x |  |  | x | x |
| KD | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| KLAR | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  |  |  |  |  |  | x |
| KMX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| LEGN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| LOGI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| LQDA | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  | x |  | x |
| LULU | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| MAIN | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  |  |
| MAT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| MESO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| META | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| MGM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  | x |
| MP | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  |  |  |  |  | x |
| MTH | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| NEM | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  | x |
| NHI | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| NKE | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  |  |  |  | x | x | x |
| NKTR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  |  |  |  |  |  |
| NVTS | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| OBDC | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  |  |
| OLN | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  |  |
| ORCL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| OZK | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| PATK | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  |  |
| PEP | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  | x |  |  |  |  | x | x |
| PFG | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| PFSI | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  | x |  | x |  | x |
| PHM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| PK | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| PLD | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  | x |
| PNC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  | x |
| PUK | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  |  | x | x |  |  |  |  |
| QBTS | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| QURE | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  |  | x |
| RGTI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| RH | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  |  |  |  |  | x |
| RIVN | 0 | 5 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  | x | x |  |  |  | x |
| RKLB | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| ROK | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  | x | x |
| RVMD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| SAN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| SARO | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| SBRA | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  |  |
| SLF | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| SNDK | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| SNEX | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| SOFI | 0 | 6 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  | x | x |  |  | x | x |
| SRPT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  |  | x |  |  |  |  |
| TRVI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x |  |  |  | x |
| UBSI | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| UFPT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| USAR | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| VFC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  | x |
| VMC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| WDC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| WELL | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| WHR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  |  |  | x | x |  |
| WLK | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| WPC | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  | x |  |  |  |  |
| WSO | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| WT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| WULF | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| ZBH | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  | x | x | ? | x |  |  |  | x |

### VOL (0)
_none_

CONFLICT (logged only, never a basket, DESIGN/110 §3): 72.

Ledger: emitted 163 (skipped 0), graded 680; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
