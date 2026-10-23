# S-A daily — 2026-10-22 (S3)

Preflight: WARN — prices.parquet ends 2026-10-16, BEFORE the 2026-10-22 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-10-16, BEFORE the 2026-10-22 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-10-16, BEFORE the 2026-10-22 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (0)
_no event tonight clears the filters._

## Suppressed (112)
| ticker | variant | first_fail |
|---|---|---|
| ABCB | A1 | F4 |
| ABCB | A2 | F4 |
| ALV | A1 | F5 |
| ALV | A2 | F5 |
| AMTB | A1 | F3 |
| AMTB | A2 | F3 |
| APPF | A1 | F5 |
| APPF | A2 | F5 |
| ASB | A1 | F5 |
| ASB | A2 | F5 |
| AXP | A1 | F3 |
| AXP | A2 | F3 |
| BAH | A1 | F6 |
| BAH | A2 | F6 |
| BCPC | A1 | F4 |
| BCPC | A2 | F4 |
| BE | A1 | F3 |
| BE | A2 | F3 |
| BWMX | A1 | F3 |
| BWMX | A2 | F3 |
| BY | A1 | F3 |
| BY | A2 | F3 |
| BYD | A1 | F5 |
| BYD | A2 | F5 |
| COLB | A1 | F5 |
| COLB | A2 | F5 |
| CUBI | A1 | F4 |
| CUBI | A2 | F4 |
| DECK | A1 | F5 |
| DECK | A2 | F5 |
| E | A1 | F3 |
| E | A2 | F3 |
| EAF | A1 | F2 |
| EAF | A2 | F2 |
| EBC | A1 | F5 |
| EBC | A2 | F5 |
| ENVA | A1 | F5 |
| ENVA | A2 | F5 |
| FCNCA | A1 | F5 |
| FCNCA | A2 | F5 |
| FHB | A1 | F5 |
| FHB | A2 | F5 |
| FIBK | A1 | F4 |
| FIBK | A2 | F4 |
| FLG | A1 | F6 |
| FLG | A2 | F6 |
| FRBA | A1 | F3 |
| FRBA | A2 | F3 |
| FRST | A1 | F3 |
| FRST | A2 | F3 |
| GBCI | A1 | F4 |
| GBCI | A2 | F4 |
| GNTX | A1 | F5 |
| GNTX | A2 | F5 |
| GRC | A1 | F3 |
| GRC | A2 | F3 |
| HTH | A1 | F4 |
| HTH | A2 | F4 |
| INFY | A1 | F3 |
| INFY | A2 | F3 |
| JAKK | A1 | F3 |
| JAKK | A2 | F3 |
| KN | A1 | F4 |
| KN | A2 | F4 |
| KNSL | A1 | F5 |
| KNSL | A2 | F5 |
| KRC | A1 | F5 |
| KRC | A2 | F5 |
| MSBI | A1 | F3 |
| MSBI | A2 | F3 |
| MXL | A1 | F7 |
| MXL | A2 | F7 |
| MYFW | A1 | F3 |
| MYFW | A2 | F3 |
| NEM | A1 | F3 |
| NEM | A2 | F3 |
| OMC | A1 | F5 |
| OMC | A2 | F5 |
| PFBC | A1 | F3 |
| PFBC | A2 | F3 |
| PINE | A1 | F3 |
| PINE | A2 | F3 |
| RCI | A1 | F5 |
| RCI | A2 | F5 |
| REXR | A1 | F5 |
| REXR | A2 | F5 |
| RHI | A1 | F5 |
| RHI | A2 | F5 |
| RITM | A1 | F2 |
| RITM | A2 | F2 |
| RNG | A1 | F5 |
| RNG | A2 | F5 |
| SAM | A1 | F3 |
| SAM | A2 | F3 |
| SIGI | A1 | F4 |
| SIGI | A2 | F4 |
| SLB | A1 | F3 |
| SLB | A2 | F3 |
| SPFI | A1 | F3 |
| SPFI | A2 | F3 |
| SRCE | A1 | F4 |
| SRCE | A2 | F4 |
| SSNC | A1 | F5 |
| SSNC | A2 | F5 |
| UVE | A1 | F3 |
| UVE | A2 | F3 |
| VRSN | A1 | F5 |
| VRSN | A2 | F5 |
| WDC | A1 | F3 |
| WDC | A2 | F3 |
| WSFS | A1 | F4 |
| WSFS | A2 | F4 |

## Exploration book tonight (8; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| BAH | SS | 2026-11-20T00:00:00.000 | 80.00 | 9.06 | +10.74% | 1,305.33 | F6 |
| BAH | IC | 2026-11-20T00:00:00.000 | 80.00 | 8.11 | +9.41% | 689.31 | F6 |
| BE | SS | 2026-10-30T00:00:00.000 | 215.00 | 29.52 | +13.36% | 8,297.78 | F3 |
| FLG | SS | 2026-10-30T00:00:00.000 | 11.50 | 0.80 | +5.06% | 219.76 | F6 |
| INFY | SS | 2026-11-20T00:00:00.000 | 13.00 | 1.44 | +9.57% | 189.17 | F3 |
| INFY | IC | 2026-11-20T00:00:00.000 | 13.00 | 1.15 | +6.74% | 84.78 | F3 |
| MXL | SS | 2026-11-20T00:00:00.000 | 65.00 | 17.83 | +26.84% | 2,968.02 | F7 |
| SLB | SS | 2026-10-30T00:00:00.000 | 50.00 | 2.85 | +5.33% | 815.83 | F3 |

## Graded today (17)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| LUV | A1 | SS | champion | +1.65% | 65.76 | 1 | no |
| LUV | A2 | SS | champion | +1.65% | 65.76 | 1 | no |
| AAL | A1 | SS | exploration | +0.49% | 5.96 | 1 | no |
| BX | A1 | SS | exploration | -0.73% | -79.67 | 1 | no |
| CCI | A1 | SS | exploration | -1.50% | -117.95 | 1 | no |
| CMCSA | A1 | SS | exploration | +0.91% | 20.17 | 1 | no |
| CMCSA | A1 | IC | exploration | +1.35% | 29.68 | 2 | no |
| CSX | A1 | SS | exploration | -2.37% | -114.32 | 1 | no |
| DOW | A1 | SS | exploration | +0.50% | 15.14 | 1 | no |
| HON | A1 | SS | exploration | +1.02% | 219.19 | 1 | no |
| KMI | A1 | SS | exploration | +0.75% | 25.48 | 1 | no |
| LUV | A1 | SS | exploration | +1.65% | 65.76 | 1 | no |
| LVS | A1 | SS | exploration | -0.18% | -6.87 | 1 | no |
| NDAQ | A1 | SS | exploration | -3.28% | -315.46 | 2 | no |
| PCG | A1 | SS | exploration | -0.50% | -6.62 | 1 | no |
| TSCO | A1 | SS | exploration | -1.68% | -54.90 | 1 | no |
| WCN | A1 | SS | exploration | -1.94% | -327.55 | 1 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 2 | 2 | +2.69% | 3.42 | 232.76 |
| sa-1.0 | champion | A1 | SS | 9 | 6 | +0.53% | 0.56 | 317.92 |
| sa-1.0 | champion | A2 | IC | 2 | 2 | +2.69% | 3.42 | 232.76 |
| sa-1.0 | champion | A2 | SS | 9 | 6 | +0.53% | 0.56 | 317.92 |
| sa-1.0 | exploration | A1 | IC | 14 | 11 | -0.77% | -1.18 | -1,565.58 |
| sa-1.0 | exploration | A1 | SS | 47 | 13 | -0.33% | -1.37 | -1,371.17 |

Ledger: emitted 0 (skipped 0), exploration 8 (skipped 0), graded 17; ledger open.

## S-B state
Gate (2026-10-22, from 2026-10-21 closes): SPY ON (VIX 16.68, VIX3M 18.72, X 16.68 vs median 15.594999999999999) · QQQ ON (VIX 16.68, VIX3M 18.72, X 24.42 vs median 21.84)

Next session (2026-10-23, from 2026-10-22 closes): SPY UNKNOWN:null input at 2026-10-22 · QQQ UNKNOWN:null input at 2026-10-22

CBOE refresh: ok through 2026-10-22; index-vol through 2026-10-22

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
Universe: 2018 names.
Borrow snapshot: 2026-10-22 (the session's own); fee known for 2012 names.
Bull counts: 0:700, 1:742, 2:412, 3:137, 4:26, 5:1, 6:0, 7:0, 8:0
Bear counts: 0:817, 1:730, 2:324, 3:116, 4:28, 5:3, 6:0, 7:0, 8:0

### LONG (100)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ABM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| ACA | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| ALRM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| AMG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| AMGN | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMN | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| ASB | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AVPT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| AWI | 3 | 0 | no |  | x |  | x |  |  | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| BBY | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| BFA | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BIIB | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BOBS | 3 | 0 | no |  | x |  | x | x |  | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BP | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| BRKB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  | x | x |
| BTI | 3 | 0 | yes |  | x |  |  | x | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| BUSE | 3 | 0 | yes | x | x |  | x |  |  | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BVS | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BY | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| CAH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CBLL | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| CFG | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CHT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| CNK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| COKE | 3 | 0 | yes | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| CON | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| COP | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  | x | x |
| CPA | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| CSL | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CUBI | 3 | 0 | no |  |  |  | x | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DV | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| E | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| EBAY | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| EPRT | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EQNR | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| EWBC | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| FCPT | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| FIZZ | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| GABC | 3 | 0 | yes | x | x |  | x |  |  | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| GIC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HCA | 3 | 0 | no |  | x |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| HCSG | 3 | 0 | no | x |  |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HLI | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| HMC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| HRTG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HST | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| HSTM | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| IOSP | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| JOE | 3 | 0 | no |  |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| KOF | 3 | 0 | no | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| LION | 4 | 0 | yes |  | x | x |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| LQDT | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| LSPD | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| LXP | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  |
| MAR | 4 | 0 | no | x | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| MD | 4 | 0 | no | x | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| MQ | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  |
| MTD | 3 | 0 | no | x | x |  |  |  |  |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| NSSC | 4 | 0 | no |  | x |  | x | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| NVCR | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| NWE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| NXPI | 4 | 0 | no |  | x | x |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| OCTV | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| PFS | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PNFP | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PNTG | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PPG | 3 | 0 | yes |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| PRSU | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PRVA | 3 | 0 | yes |  | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| QLYS | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| REYN | 3 | 0 | no |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| RGA | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RSG | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| SBCF | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| SFBS | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  | ? | ? |  |  |  | ? |  |  |  |  |  |
| SHEL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SN | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| SSD | 3 | 0 | no |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| SSL | 3 | 0 | no | x |  |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| SSNC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| STAG | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| SU | 4 | 0 | no | x | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  | x | x |
| TAK | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| TALO | 3 | 0 | no | x | x |  |  |  |  |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| TOWN | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TRMK | 3 | 0 | yes |  | x |  | x |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TTC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TW | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| UCB | 3 | 0 | no | x |  |  | x |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| UTHR | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VIV | 4 | 0 | no |  | x |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| VLTO | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VRSN | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| WLY | 3 | 0 | yes | x | x |  |  |  |  | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| WMK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| WOR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| WSM | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| ZION | 3 | 0 | no |  | x |  | x |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |

### SHORT (62)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| AG | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  | x |
| ALB | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  | x |
| ALG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| ALK | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  |  | x |  |  | x | x |
| AMSC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| ARM | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| ASTS | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  | x | x |
| AVAV | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| BDC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CDE | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  | x |
| COIN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  | x | x |
| CORZ | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  |  |  |  |  |  | x |
| CPNG | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? | x |  |  |  | x |
| CRS | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  | x |  |  |  | x |  | x |  | x |
| CVNA | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| DELL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| DRS | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  |  | x | x |  |  |  |  |
| DUOL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| DXCM | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| ECHO | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| ELAN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| FIGR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| FLNG | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| FN | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| FSK | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| GGG | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  |  | x |  | ? | x |  |  |  | x |
| GME | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  | x |  |  | x |
| GOOG | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  | x | x |
| GPGI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| HIMS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| HL | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  | x |
| HOOD | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  |  | x | x |
| INSM | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| IONQ | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| JBS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| KTOS | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| LUNR | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  |  |
| MAIN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| META | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| MMED | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  | x |
| PL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| POWL | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| QBTS | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  | x |
| QURE | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  |  |
| RGTI | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| RIVN | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  | x |  |  |  | x |
| RKLB | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| SHAK | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  | x | x |  | ? | x |  |  |  |  |
| SIRI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| SKHY | 0 | 4 | no |  |  | ? |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  | x | x |
| SPCX | 0 | 3 | no |  |  | ? |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  | x | x |
| STRD | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  | x |  | x | x |  |  |  |  |
| T | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| TGTX | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| TTMI | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| VKTX | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| VSAT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| WLDN | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| WOLF | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| XE | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  | x |  |  |

### VOL (4)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CAG | 1 | 0 | yes |  |  |  |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |  |  | x |
| DOCU | 2 | 0 | yes | x |  |  |  |  |  | ? | x |  |  |  |  |  |  |  |  | x |  |  | x |
| GIS | 0 | 0 | yes |  |  |  |  |  |  | ? |  |  |  |  |  |  |  |  |  | x |  |  | x |
| GME | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  | x |  |  | x |

CONFLICT (logged only, never a basket, DESIGN/110 §3): 76.

Ledger: emitted 166 (skipped 0), graded 546; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
