# S-A daily — 2026-10-06 (S3)

Preflight: WARN — prices.parquet ends 2026-10-02, BEFORE the 2026-10-06 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-10-02, BEFORE the 2026-10-06 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-10-02, BEFORE the 2026-10-06 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (0)
_no event tonight clears the filters._

## Suppressed (10)
| ticker | variant | first_fail |
|---|---|---|
| NEOG | A1 | F5 |
| NEOG | A2 | F5 |
| PENG | A1 | F7 |
| PENG | A2 | F7 |
| SAR | A1 | F3 |
| SAR | A2 | F3 |
| STZ | A1 | F6 |
| STZ | A2 | F6 |
| WS | A1 | F3 |
| WS | A2 | F3 |

## Exploration book tonight (3; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| PENG | SS | 2026-10-16T00:00:00.000 | 65.00 | 12.23 | +18.29% | 1,983.77 | F7 |
| STZ | SS | 2026-10-09T00:00:00.000 | 116.00 | 5.68 | +4.64% | 869.53 | F6 |
| STZ | IC | 2026-10-09T00:00:00.000 | 116.00 | 5.14 | +4.08% | 485.73 | F6 |

## Graded today (4)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| LW | A1 | SS | exploration | -0.52% | -23.39 | 1 | no |
| LW | A1 | IC | exploration | -1.23% | -54.90 | 1 | no |
| RPM | A1 | SS | exploration | -0.25% | -24.18 | 2 | no |
| RPM | A1 | IC | exploration | -1.31% | -124.76 | 2 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 1 | 1 | +1.91% | — | 66.98 |
| sa-1.0 | champion | A1 | SS | 1 | 1 | +2.87% | — | 100.79 |
| sa-1.0 | champion | A2 | IC | 1 | 1 | +1.91% | — | 66.98 |
| sa-1.0 | champion | A2 | SS | 1 | 1 | +2.87% | — | 100.79 |
| sa-1.0 | exploration | A1 | IC | 3 | 2 | -0.21% | -0.15 | -112.68 |
| sa-1.0 | exploration | A1 | SS | 3 | 2 | +0.70% | 0.48 | 53.21 |

Ledger: emitted 0 (skipped 0), exploration 3 (skipped 0), graded 4; ledger open.

## S-B state
Gate (2026-10-06, from 2026-10-05 closes): SPY OFF:G2 (VIX 15.52, VIX3M 18.0, X 15.52 vs median 15.780000000000001) · QQQ ON (VIX 15.52, VIX3M 18.0, X 21.7 vs median 21.475)

Next session (2026-10-07, from 2026-10-06 closes): SPY OFF:G2 (VIX 15.01, VIX3M 17.64, X 15.01 vs median 15.780000000000001) · QQQ OFF:G2 (VIX 15.01, VIX3M 17.64, X 21.15 vs median 21.705)

CBOE refresh: ok through 2026-10-09; index-vol through 2026-10-09

Entry day: no.

### S-B positions tonight (0)
_none_

### S-B graded at expiry today (0)
_none due_

Open positions: QQQ-IC 2, QQQ-PS 2, SPY-IC 2, SPY-PS 2

### S-B forward ledger to date
| policy_id | role | sleeve | n | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|---|
| sb-1.0 | champion | QQQ-IC | 1 | — | — | 321.63 |
| sb-1.0 | champion | QQQ-PS | 1 | — | — | 224.53 |
| sb-1.0 | champion | SPY-PS | 1 | — | — | 155.40 |
| sb-1.0 | exploration | QQQ-IC | 1 | — | — | 321.63 |
| sb-1.0 | exploration | QQQ-PS | 1 | — | — | 224.53 |
| sb-1.0 | exploration | SPY-PS | 1 | — | — | 155.40 |

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
| C2-SS | 4 | 6,032.94 | 8,000.00 | 3 |
| C2-IB | 4 | 3,571.32 | 4,000.00 | 3 |

### S-C forward ledger to date (entry-week series)
_ledger empty_

Progress to the read: graded entry-weeks 0 of 40 (C1-SS), 0 of 40 (C1-IB), 0 of 40 (C2-SS), 0 of 40 (C2-IB)

S-C ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0.


## Watch basket (wb-1.0, exploration, paper only)
Universe: 1986 names.
Borrow snapshot: 2026-10-06 (the session's own); fee known for 1981 names.
Bull counts: 0:926, 1:717, 2:289, 3:47, 4:7, 5:0, 6:0, 7:0, 8:0
Bear counts: 0:508, 1:741, 2:502, 3:179, 4:50, 5:5, 6:1, 7:0, 8:0

### LONG (30)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAT | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| ABBV | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ACA | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| ADI | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| AME | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMG | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMN | 4 | 0 | no | x | x |  |  |  | x | x |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BCPC | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| BRZE | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| CLBT | 3 | 0 | no |  |  | x |  | x |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| CNXN | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| CON | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| EFOR | 3 | 0 | no | x | x |  |  |  |  | x |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| FFIV | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HNGE | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| JOYY | 4 | 0 | no | x | x |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| KEYS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LIN | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MSM | 4 | 0 | no | x | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| MTD | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| NHC | 3 | 0 | no | x |  |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| NTES | 3 | 0 | no |  | x |  | x |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PAGS | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| PD | 3 | 0 | yes | x |  |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| PLUS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| RAL | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| RGA | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SNX | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TOST | 3 | 0 | no |  | x |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| TW | 4 | 0 | no |  |  | x |  | x | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |

### SHORT (121)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ABCB | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| ABVX | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |  |  |  | x |
| AG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| AMT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | x |  |  |  |  | x |
| APLD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| ARCC | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| ASTS | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  | x | x |
| ATO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x |  |  |  |  |  | x |
| AYI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| BA | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  | x | x |
| BCE | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x |  |  |  |  |  |
| BCH | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | ? |  |  | x | x | ? | x |  |  |  |  |
| BMO | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| BMY | 0 | 4 | yes |  |  |  |  |  |  | ? |  |  | x | x |  |  | x | ? | x |  |  |  | x |
| BXSL | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? |  |  |  |  | x |
| CAG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| CALM | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  | x |
| CAR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  |  |  |  |  |  | x |
| CARG | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| CCJ | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| CFR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| CLBK | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CLSK | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| CM | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| CRCL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| CRSP | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| CTRE | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  |  |
| CWT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  | x |
| CXW | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? |  |  |  |  | x |
| DAVE | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? | x |  |  |  | x |
| DX | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  |  | x | x |  | x |  | x |
| ENB | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x |  | x |  |  |  | x |
| ENPH | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  |  |  |  |  |  | x |
| ERIE | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| FBP | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | ? |  |  | x | ? | x |  |  |  | x |
| FLY | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| GFL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| GLPI | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x | x |  | x |  | x |
| GLXY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| GNTX | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  | x |  |  |  |  |
| GSK | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| HDB | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| HESM | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| HIMS | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  |  | x |
| HR | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  |  |  |  | x | x |  |  |  | x |
| HROW | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? | x |  |  |  |  | x |  |  |  |  |
| HSY | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? |  |  |  |  | x |
| HUT | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| IMO | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| INCY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| IOVA | 0 | 4 | yes |  |  |  |  |  |  | ? |  |  | x | x | x | x |  | ? |  |  |  |  | x |
| IRTC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| ITRI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| JAZZ | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| JBTM | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| JPM | 0 | 4 | no |  |  |  |  |  |  |  |  |  |  | x |  |  | x | x | x |  |  |  | x |
| KBH | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| KBR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| KD | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| KHC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| KLAC | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  | x |  | x |  | ? |  |  |  |  | x |
| KNSL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | x |  |  |  |  |  |
| LEGN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| LOGI | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| LUNR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| MAA | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x |  | x |  |  |  | x |
| MAIN | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  |  |
| MARA | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| MDGL | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x | x |  |  |  |  | x |
| META | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| MGM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  | x |
| MSDL | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  |  |
| NEM | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  | x |
| NHI | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  |  |
| NKE | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  |  |  |  | x | x | x |
| NKTR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  |  |  | x |  | x |
| NN | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  |  |  |
| OBDC | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  | x |
| OCFC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| OGS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x |  |  |  |  |  | x |
| OLED | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| OLN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| ORI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? |  |  |  |  |  |
| PAG | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  |  |
| PEP | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  | x |  |  |  | x |  | x |
| PLD | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| PNC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| PRCT | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| PRMB | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x |  |  |  |  |
| PRU | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | x |  |  |  |  | x |
| PSA | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  | x |
| QBTS | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| QSR | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x |  |  | x |  | x |  |  |  | x |
| QURE | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  |  | x |
| RCI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| RKLB | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| SBRA | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  |  |
| SBUX | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  | x |
| SF | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x |  | x |  |  |  | x |
| SNEX | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| SNY | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| SOFI | 0 | 6 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  | x | x |  |  | x | x |
| STAG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| SW | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| TKO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? |  |  |  |  | x |
| TRVI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  |  | x |  |  |  | x |
| UEC | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  |  | x |
| USAR | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| UUUU | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  | x |  |  |  | x |
| VLY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| VMC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| VRTX | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| VSAT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| VSEC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| WAL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| WELL | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  | x | x |
| WLDN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| WPC | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  | x |  |  |  | x |
| WSO | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| XENE | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  | x |
| ZBH | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |

### VOL (0)
_none_

CONFLICT (logged only, never a basket, DESIGN/110 §3): 78.

Ledger: emitted 151 (skipped 0), graded 438; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
