# S-A daily — 2026-11-11 (S3)

Preflight: WARN — prices.parquet ends 2026-11-06, BEFORE the 2026-11-11 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-11-06, BEFORE the 2026-11-11 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-11-06, BEFORE the 2026-11-11 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (0)
_no event tonight clears the filters._

## Suppressed (118)
| ticker | variant | first_fail |
|---|---|---|
| ABSI | A1 | F3 |
| ABSI | A2 | F3 |
| ACOG | A1 | F2 |
| ACOG | A2 | F2 |
| ADIG | A1 | F3 |
| ADIG | A2 | F3 |
| AGRO | A1 | F2 |
| AGRO | A2 | F2 |
| AIRO | A1 | F2 |
| AIRO | A2 | F2 |
| ALLT | A1 | F2 |
| ALLT | A2 | F2 |
| ARCO | A1 | F2 |
| ARCO | A2 | F2 |
| ARX | A1 | F4 |
| ARX | A2 | F4 |
| ASND | A1 | F5 |
| ASND | A2 | F5 |
| AVAH | A1 | F4 |
| AVAH | A2 | F4 |
| AVEX | A1 | F3 |
| AVEX | A2 | F3 |
| AZ | A1 | F2 |
| AZ | A2 | F2 |
| BN | A1 | F3 |
| BN | A2 | F3 |
| BRUN | A1 | F2 |
| BRUN | A2 | F2 |
| CAE | A1 | F4 |
| CAE | A2 | F4 |
| CDNL | A1 | F3 |
| CDNL | A2 | F3 |
| CEPU | A1 | F3 |
| CEPU | A2 | F3 |
| CLBT | A1 | F4 |
| CLBT | A2 | F4 |
| CMCL | A1 | F3 |
| CMCL | A2 | F3 |
| CRMD | A1 | F2 |
| CRMD | A2 | F2 |
| CTVA | A1 | F5 |
| CTVA | A2 | F5 |
| DGII | A1 | F4 |
| DGII | A2 | F4 |
| DPC | A1 | F5 |
| DPC | A2 | F5 |
| ECO | A1 | F6 |
| ECO | A2 | F6 |
| ENS | A1 | F5 |
| ENS | A2 | F5 |
| EPC | A1 | F3 |
| EPC | A2 | F3 |
| EROC | A1 | F2 |
| EROC | A2 | F2 |
| EYE | A1 | F3 |
| EYE | A2 | F3 |
| EZPW | A1 | F3 |
| EZPW | A2 | F3 |
| FIGR | A1 | F6 |
| FIGR | A2 | F6 |
| FNV | A1 | F6 |
| FNV | A2 | F6 |
| FPS | A1 | F6 |
| FPS | A2 | F6 |
| HBM | A1 | F6 |
| HBM | A2 | F6 |
| LGN | A1 | F5 |
| LGN | A2 | F5 |
| LUNR | A1 | F3 |
| LUNR | A2 | F3 |
| MBGL | A1 | F5 |
| MBGL | A2 | F5 |
| MDWD | A1 | F3 |
| MDWD | A2 | F3 |
| MOVE | A1 | F2 |
| MOVE | A2 | F2 |
| MWH | A1 | F4 |
| MWH | A2 | F4 |
| NBIS | A1 | F7 |
| NBIS | A2 | F7 |
| NEXN | A1 | F2 |
| NEXN | A2 | F2 |
| NIQ | A1 | F4 |
| NIQ | A2 | F4 |
| NTWK | A1 | F2 |
| NTWK | A2 | F2 |
| OCTV | A1 | F4 |
| OCTV | A2 | F4 |
| ONDS | A1 | F2 |
| ONDS | A2 | F2 |
| OPRX | A1 | F2 |
| OPRX | A2 | F2 |
| OR | A1 | F4 |
| OR | A2 | F4 |
| PSFE | A1 | F2 |
| PSFE | A2 | F2 |
| SPB | A1 | F4 |
| SPB | A2 | F4 |
| SSYS | A1 | F2 |
| SSYS | A2 | F2 |
| STDN | A1 | F3 |
| STDN | A2 | F3 |
| TK | A1 | F3 |
| TK | A2 | F3 |
| TNK | A1 | F4 |
| TNK | A2 | F4 |
| TTEK | A1 | F5 |
| TTEK | A2 | F5 |
| TWST | A1 | F6 |
| TWST | A2 | F6 |
| VYLR | A1 | F5 |
| VYLR | A2 | F5 |
| WWW | A1 | F3 |
| WWW | A2 | F3 |
| XE | A1 | F6 |
| XE | A2 | F6 |
| YETI | A1 | F6 |
| YETI | A2 | F6 |

## Exploration book tonight (14; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| CLBT | SS | 2026-11-20T00:00:00.000 | 12.50 | 1.61 | +11.71% | 319.12 | F4 |
| ECO | SS | 2026-11-20T00:00:00.000 | 85.00 | 10.06 | +10.83% | 2,775.35 | F6 |
| ECO | IC | 2026-11-20T00:00:00.000 | 85.00 | 9.16 | +9.45% | 1,583.92 | F6 |
| FIGR | SS | 2026-11-13T00:00:00.000 | 24.00 | 3.09 | +11.47% | 981.87 | F6 |
| FNV | SS | 2026-11-20T00:00:00.000 | 250.00 | 14.08 | +5.07% | 4,633.72 | F6 |
| FNV | IC | 2026-11-20T00:00:00.000 | 250.00 | 13.72 | +4.84% | 2,628.12 | F6 |
| FPS | SS | 2026-11-13T00:00:00.000 | 24.50 | 3.40 | +12.91% | 1,177.23 | F6 |
| HBM | SS | 2026-11-20T00:00:00.000 | 22.50 | 2.21 | +9.25% | 615.35 | F6 |
| LUNR | SS | 2026-11-13T00:00:00.000 | 12.00 | 1.54 | +12.06% | 551.79 | F3 |
| NBIS | SS | 2026-11-13T00:00:00.000 | 155.00 | 20.46 | +13.09% | 7,031.93 | F7 |
| TWST | SS | 2026-11-20T00:00:00.000 | 125.00 | 24.32 | +18.34% | 5,404.60 | F6 |
| XE | SS | 2026-11-13T00:00:00.000 | 11.00 | 0.97 | +7.79% | 441.17 | F6 |
| YETI | SS | 2026-11-20T00:00:00.000 | 42.50 | 4.38 | +9.21% | 935.21 | F6 |
| YETI | IC | 2026-11-20T00:00:00.000 | 42.50 | 4.16 | +8.47% | 584.36 | F6 |

## Graded today (11)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| ALC | A1 | SS | exploration | +0.06% | 4.40 | 1 | no |
| ALC | A1 | IC | exploration | -0.91% | -67.66 | 2 | no |
| AMPX | A1 | SS | exploration | +2.33% | 21.30 | 1 | no |
| CRWV | A1 | SS | exploration | +0.41% | 19.87 | 1 | no |
| FLY | A1 | SS | exploration | +0.04% | 1.02 | 1 | no |
| GO | A1 | SS | exploration | -0.24% | -3.30 | 1 | no |
| MRCY | A1 | SS | exploration | -1.63% | -136.23 | 1 | no |
| NN | A1 | SS | exploration | -1.93% | -16.21 | 1 | no |
| PBR | A1 | SS | exploration | -1.04% | -18.96 | 1 | no |
| PBR | A1 | IC | exploration | -1.13% | -20.69 | 2 | no |
| RGTI | A1 | SS | exploration | +3.20% | 38.84 | 1 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 8 | 6 | +0.63% | 1.12 | 245.49 |
| sa-1.0 | champion | A1 | SS | 32 | 15 | -0.77% | -0.98 | -1,477.88 |
| sa-1.0 | champion | A2 | IC | 7 | 5 | +0.66% | 1.00 | 233.18 |
| sa-1.0 | champion | A2 | SS | 25 | 14 | -0.53% | -0.54 | -372.47 |
| sa-1.0 | exploration | A1 | IC | 58 | 23 | -1.11% | -1.67 | -9,252.44 |
| sa-1.0 | exploration | A1 | SS | 272 | 26 | -0.94% | -3.12 | -23,045.82 |

Ledger: emitted 0 (skipped 0), exploration 14 (skipped 0), graded 11; ledger open.

## S-B state
Gate (2026-11-11, from 2026-11-10 closes): SPY ON (VIX 19.46, VIX3M 20.64, X 19.46 vs median 18.415) · QQQ ON (VIX 19.46, VIX3M 20.64, X 28.57 vs median 25.979999999999997)

Next session (2026-11-12, from 2026-11-11 closes): SPY OFF:G2 (VIX 17.49, VIX3M 19.24, X 17.49 vs median 18.735) · QQQ OFF:G2 (VIX 17.49, VIX3M 19.24, X 26.74 vs median 26.765)

CBOE refresh: ok through 2026-11-12; index-vol through 2026-11-12

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
Universe: 2020 names.
Borrow snapshot: 2026-11-11 (the session's own); fee known for 2012 names.
Bull counts: 0:697, 1:701, 2:432, 3:168, 4:22, 5:0, 6:0, 7:0, 8:0
Bear counts: 0:812, 1:771, 2:308, 3:113, 4:14, 5:2, 6:0, 7:0, 8:0

### LONG (108)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ABM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| ACEL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| AER | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| AIZ | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ALGN | 3 | 0 | no |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| ALH | 3 | 0 | no |  |  |  |  | x | x | x |  |  | ? |  |  |  |  |  |  |  |  |  | x |
| ALSN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| AMTB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| ANRO | 4 | 0 | no |  | x |  | x | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| AWI | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| AXGN | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AXTA | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| BANF | 3 | 0 | no |  |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| BEN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BIIB | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BKE | 3 | 0 | no |  | x | x |  | x |  | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BLK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BRKB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  | x | x |
| BUD | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CAC | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| CAE | 3 | 0 | no |  | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| CE | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| CL | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| CME | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| CNK | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| CNO | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| COLM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| COMP | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CON | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| COST | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| CRBG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CRUS | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CUBE | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| DEO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DHR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DLX | 3 | 0 | no |  |  | x |  | x | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DRH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| EHC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| EMR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EPC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| EQH | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| EW | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| EXLS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| EXR | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| FAST | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| FERG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| GD | 3 | 0 | yes |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| GFF | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| GWW | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| HAWK | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| HG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HII | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HLT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HSAI | 4 | 0 | yes |  |  | x | x | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HZO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| ICE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| IDT | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| KO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| KOF | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| LH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LKFT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| LLY | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| LNTH | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| LQDT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| MANU | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| MCBS | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| MET | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MGEE | 3 | 0 | yes |  | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| MICC | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| MMM | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| MRSH | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| MSCI | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| MSI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| NDAQ | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| NWE | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| NXPI | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PACS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PDM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PLUS | 3 | 0 | no | x |  |  |  | x | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PPLI | 3 | 0 | no |  |  |  | x |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| R | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RLJ | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| RPRX | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RTO | 3 | 0 | no |  | x |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| SAIC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SBUX | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SEIC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| SGRY | 3 | 0 | no | x | x |  |  |  |  |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| SIGI | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| SJM | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| SMA | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| STN | 3 | 0 | no |  | x |  |  |  | x | x |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| STT | 3 | 0 | yes |  |  | x | x |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SUNB | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TAC | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| TAK | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| TEL | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TNC | 3 | 0 | no |  |  |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TW | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| UTHR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VCTR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VLTO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VRNS | 3 | 0 | yes | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| VZ | 3 | 0 | yes | x |  |  |  | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| WAB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WAT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WMK | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |

### SHORT (74)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| ACI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| AFRM | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| AI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  |  |
| AMKR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| ASST | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| ASTS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| AXON | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  | x | x |
| AXTI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| BABA | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  | x | x |
| BFH | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? |  |  |  |  |  |
| BILI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  |  |  |  |  |  |  |
| BMA | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | ? |  |  |  |  | x | x |  |  |  |  |
| BMNR | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| BXP | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| CAT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  | x | x |
| CBRL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? |  |  |  |  |  |
| CFR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| CHKP | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| CIGI | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CLMT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? | x | x |  |  |  | x |  |  |  |  |
| CRCL | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| CRSP | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| CSGP | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| DASH | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? |  |  |  |  | x |
| DBX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| DVA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| FICO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| FIG | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| FIVN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? |  |  |  |  |  |
| FLG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  |  |
| FSLR | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  |  | x |
| FSLY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| GRAL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| HIMS | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  | ? | x |  |  | x | x |
| IMAX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| INGR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? |  |  |  |  | x |
| INOD | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  |  |  |
| INVA | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| IONS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  | x |  | x |
| IRTC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  | x |  | ? |  |  |  |  | x |
| KBH | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| KHC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? |  |  |  |  | x |
| LINE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| LUNR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| LYFT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  |  |
| MATX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| MELI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  | x | x |
| MGA | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| MMSI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| MOS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| MSTR | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| NEO | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| NFG | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? |  |  |  |  |  |
| NSC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| ONON | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| ORCL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| PBI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| PPL | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? |  |  |  |  | x |
| PS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| PTGX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| RGTI | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| RHI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| SEDG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  |  |
| SLG | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| SRPT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| ST | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| SYF | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| TDS | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| TREX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| UPST | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  |  | x |
| WHR | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| WIX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| YPF | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x |  |  |  |  |

### VOL (0)
_none_

CONFLICT (logged only, never a basket, DESIGN/110 §3): 81.

Ledger: emitted 182 (skipped 0), graded 560; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
