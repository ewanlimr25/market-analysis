# S-A daily — 2026-11-19 (S3)

Preflight: WARN — prices.parquet ends 2026-11-13, BEFORE the 2026-11-19 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-11-13, BEFORE the 2026-11-19 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-11-13, BEFORE the 2026-11-19 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (0)
_no event tonight clears the filters._

## Suppressed (30)
| ticker | variant | first_fail |
|---|---|---|
| BJ | A1 | F5 |
| BJ | A2 | F5 |
| BKE | A1 | F4 |
| BKE | A2 | F4 |
| BSP | A1 | F5 |
| BSP | A2 | F5 |
| ESE | A1 | F5 |
| ESE | A2 | F5 |
| ESTC | A1 | F7 |
| ESTC | A2 | F7 |
| FRO | A1 | F6 |
| FRO | A2 | F6 |
| GAP | A1 | F6 |
| GAP | A2 | F6 |
| GLOB | A1 | F3 |
| GLOB | A2 | F3 |
| GRRR | A1 | F2 |
| GRRR | A2 | F2 |
| INTU | A1 | F3 |
| INTU | A2 | F3 |
| KEYS | A1 | F5 |
| KEYS | A2 | F5 |
| MATW | A1 | F3 |
| MATW | A2 | F3 |
| NGVC | A1 | F3 |
| NGVC | A2 | F3 |
| POST | A1 | F6 |
| POST | A2 | F6 |
| ROST | A1 | F3 |
| ROST | A2 | F3 |

## Exploration book tonight (8; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| ESTC | SS | 2026-12-18T00:00:00.000 | 75.00 | 15.16 | +19.36% | 2,278.20 | F7 |
| ESTC | IC | 2026-12-18T00:00:00.000 | 75.00 | 12.80 | +15.68% | 1,219.88 | F7 |
| FRO | SS | 2026-12-18T00:00:00.000 | 45.00 | 6.79 | +13.64% | 879.88 | F6 |
| GAP | SS | 2026-11-27T00:00:00.000 | 19.00 | 2.37 | +11.85% | 479.38 | F6 |
| INTU | SS | 2026-11-27T00:00:00.000 | 310.00 | 30.03 | +9.00% | 7,416.15 | F3 |
| INTU | IC | 2026-11-27T00:00:00.000 | 310.00 | 28.52 | +8.29% | 4,147.87 | F3 |
| POST | SS | 2026-12-18T00:00:00.000 | 80.00 | 7.35 | +8.06% | 1,142.51 | F6 |
| ROST | SS | 2026-11-27T00:00:00.000 | 220.00 | 16.42 | +7.11% | 3,899.28 | F3 |

## Graded today (10)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| WSM | A1 | SS | champion | +0.25% | 65.24 | 1 | no |
| WSM | A2 | SS | champion | +0.25% | 65.24 | 1 | no |
| BBWI | A1 | SS | exploration | +3.97% | 74.09 | 1 | no |
| FUTU | A1 | SS | exploration | -1.59% | -131.87 | 1 | no |
| MMS | A1 | SS | exploration | -3.75% | -244.77 | 1 | no |
| P | A1 | SS | exploration | +1.03% | 104.18 | 1 | no |
| P | A1 | IC | exploration | +0.61% | 61.71 | 2 | no |
| SBLK | A1 | SS | exploration | -0.48% | -12.90 | 1 | no |
| UTI | A1 | SS | exploration | +3.28% | 72.44 | 1 | no |
| WSM | A1 | SS | exploration | +0.25% | 65.24 | 1 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 10 | 7 | +0.68% | 1.50 | 440.76 |
| sa-1.0 | champion | A1 | SS | 37 | 18 | -0.60% | -0.87 | -1,100.72 |
| sa-1.0 | champion | A2 | IC | 9 | 6 | +0.71% | 1.38 | 428.45 |
| sa-1.0 | champion | A2 | SS | 29 | 16 | -0.41% | -0.48 | -73.77 |
| sa-1.0 | exploration | A1 | IC | 63 | 26 | -1.05% | -1.72 | -9,328.26 |
| sa-1.0 | exploration | A1 | SS | 311 | 32 | -0.92% | -3.42 | -24,861.99 |

Ledger: emitted 0 (skipped 0), exploration 8 (skipped 0), graded 10; ledger open.

## S-B state
Gate (2026-11-19, from 2026-11-18 closes): SPY OFF:G1 (VIX 24.56, VIX3M 24.29, X 24.56 vs median 19.36) · QQQ OFF:G1 (VIX 24.56, VIX3M 24.29, X 33.12 vs median 28.560000000000002)

Next session (2026-11-20, from 2026-11-19 closes): SPY OFF:G1 (VIX 28.44, VIX3M 27.03, X 28.44 vs median 19.435000000000002) · QQQ OFF:G1 (VIX 28.44, VIX3M 27.03, X 36.48 vs median 28.645)

CBOE refresh: ok through 2026-11-19; index-vol through 2026-11-19

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
| sc-1.0 | exploration | C1-SS | 200 | 4 | -9.72% | -2.49 | -237,853.02 |
| sc-1.0 | exploration | C1-IB | 200 | 4 | -19.19% | -3.82 | -212,479.36 |

Progress to the read: graded entry-weeks 2 of 40 (C1-SS), 2 of 40 (C1-IB), 2 of 40 (C2-SS), 2 of 40 (C2-IB)

S-C ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0.


## Watch basket (wb-1.0, exploration, paper only)
Universe: 1994 names.
Borrow snapshot: 2026-11-19 (the session's own); fee known for 1988 names.
Bull counts: 0:827, 1:800, 2:294, 3:66, 4:7, 5:0, 6:0, 7:0, 8:0
Bear counts: 0:379, 1:723, 2:590, 3:230, 4:66, 5:6, 6:0, 7:0, 8:0

### LONG (20)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BCS | 3 | 0 | yes |  | x | x | x |  |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| BJ | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BLCO | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| COST | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  | x | x |
| EG | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| GSAT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| HMN | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| HZO | 3 | 0 | no | x |  |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  |  |
| IBN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| KO | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| KOF | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| LNTH | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| ONC | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| R | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| SIGI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| SONY | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TAK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TGT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VRNS | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| WRB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |

### SHORT (109)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ABVX | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| ACAD | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| ACI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| ACIW | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| ADNT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| AEP | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| AFRM | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| AMPL | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? |  |  |  |  | x |
| AMSC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| ARWR | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  | x |  | x |
| AUPH | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| BABA | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| BC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| BDC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| BIDU | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  | x |  | x |
| BLLN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| BRKR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| BTU | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  |  | x |  |  |  |  |
| BWXT | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  | x |  | x |
| CAAP | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CAMT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| CNP | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? | x |  |  |  | x |
| COGT | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  |  |
| COIN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  | x | x |
| CPNG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? |  |  |  |  | x |
| CRSP | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| CVX | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| DBD | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| DE | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x | x | ? |  |  |  |  | x |
| DLB | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x | x | ? |  |  |  |  | x |
| DNTH | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| ENS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  | x |  | x |
| FDS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| FHB | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? |  |  |  |  | x |
| FIBK | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| FLNG | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? | x |  | x |  |  |
| FNV | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x | x | ? |  |  |  |  | x |
| FOR | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  | x |  |  |
| FOUR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| FPS | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| GAP | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| GDS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  | x |
| GFL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| GIL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  |  |
| GLNG | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  | ? | x |  |  |  | x |
| GLPI | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| GNTX | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  |  |
| GSL | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  | x | x | x | ? |  |  |  |  |  |
| HASI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| IDYA | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| IMO | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| IMVT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| INCY | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| INGR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? |  |  |  |  |  |
| INOD | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  |  |
| IONS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  | x |  | x |
| IPGP | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| IRMD | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| KLAR | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? |  |  |  |  | x |
| KNF | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| KSS | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x | x | x |  | ? |  |  |  |  |  |
| L | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| LGND | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| LIND | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| LQDA | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  | x |
| LQDT | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| M | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| MAT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  |  |  |
| MDGL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| MDU | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| MQ | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| MSDL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| NFG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  |  |
| NU | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| NVDA | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  | x | x | x |
| OLED | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| OXY | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x | x | ? | x |  |  |  | x |
| PAGP | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  | x | ? |  |  |  |  | x |
| PATH | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| PBI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  |  |
| PCOR | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| PFG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| PGY | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x | x |  | ? |  |  |  |  |  |
| PTGX | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| REG | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| REPL | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x | x |  | ? |  |  |  |  |  |
| ROAD | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| RRR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| STAA | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| STNG | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  | x |  | x | ? | x |  |  |  |  |
| STWD | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  | x |  |  |
| SYM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| TBBK | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| TNGX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| TPG | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| TTD | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  | ? |  |  |  |  | x |
| UGI | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| VKTX | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  |  | x |
| WABC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| WAL | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? |  |  |  |  |  |
| WIX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| WK | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| WMS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| WOLF | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  |  |
| WSM | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| WSO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| XENE | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| ZM | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| ZTO | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  |  |

### VOL (2)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAL | 1 | 1 | no |  | x |  |  |  |  |  |  |  |  | x |  |  |  | ? |  | x |  |  | x |
| PINS | 0 | 2 | yes |  |  |  |  |  |  | ? |  |  |  |  | x |  |  | ? | x | x |  |  | x |

CONFLICT (logged only, never a basket, DESIGN/110 §3): 147.

Ledger: emitted 131 (skipped 0), graded 530; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
