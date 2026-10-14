# S-A daily — 2026-10-13 (S3)

Preflight: WARN — prices.parquet ends 2026-10-09, BEFORE the 2026-10-13 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-10-09, BEFORE the 2026-10-13 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-10-09, BEFORE the 2026-10-13 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (0)
_no event tonight clears the filters._

## Suppressed (16)
| ticker | variant | first_fail |
|---|---|---|
| ASML | A1 | F3 |
| ASML | A2 | F3 |
| AZZ | A1 | F4 |
| AZZ | A2 | F4 |
| BAC | A1 | F3 |
| BAC | A2 | F3 |
| BLK | A1 | F3 |
| BLK | A2 | F3 |
| FAST | A1 | F3 |
| FAST | A2 | F3 |
| MS | A1 | F3 |
| MS | A2 | F3 |
| PGR | A1 | F3 |
| PGR | A2 | F3 |
| STT | A1 | F6 |
| STT | A2 | F6 |

## Exploration book tonight (6; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| AZZ | SS | 2026-10-16T00:00:00.000 | 135.00 | 10.21 | +6.94% | 2,560.10 | F4 |
| AZZ | IC | 2026-10-16T00:00:00.000 | 135.00 | 9.86 | +6.61% | 1,513.97 | F4 |
| FAST | SS | 2026-10-16T00:00:00.000 | 52.50 | 2.96 | +5.37% | 691.34 | F3 |
| FAST | IC | 2026-10-16T00:00:00.000 | 52.50 | 2.83 | +4.93% | 467.01 | F3 |
| STT | SS | 2026-10-16T00:00:00.000 | 175.00 | 7.82 | +4.17% | 2,292.44 | F6 |
| STT | IC | 2026-10-16T00:00:00.000 | 175.00 | 7.64 | +4.02% | 1,236.04 | F6 |

## Graded today (3)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| ACI | A1 | SS | exploration | +0.56% | 7.03 | 1 | no |
| DPZ | A1 | SS | exploration | +0.80% | 248.02 | 1 | no |
| DPZ | A1 | IC | exploration | +0.59% | 183.72 | 1 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 2 | 2 | +2.69% | 3.42 | 232.76 |
| sa-1.0 | champion | A1 | SS | 2 | 2 | +3.83% | 3.98 | 328.86 |
| sa-1.0 | champion | A2 | IC | 2 | 2 | +2.69% | 3.42 | 232.76 |
| sa-1.0 | champion | A2 | SS | 2 | 2 | +3.83% | 3.98 | 328.86 |
| sa-1.0 | exploration | A1 | IC | 7 | 6 | +0.40% | 0.52 | 97.01 |
| sa-1.0 | exploration | A1 | SS | 9 | 6 | +1.32% | 2.05 | 690.46 |

Ledger: emitted 0 (skipped 0), exploration 6 (skipped 0), graded 3; ledger open.

## S-B state
Gate (2026-10-13, from 2026-10-12 closes): SPY OFF:G2 (VIX 15.21, VIX3M 17.93, X 15.21 vs median 15.425) · QQQ OFF:G2 (VIX 15.21, VIX3M 17.93, X 20.84 vs median 21.22)

Next session (2026-10-14, from 2026-10-13 closes): SPY OFF:G2 (VIX 15.27, VIX3M 17.96, X 15.27 vs median 15.36) · QQQ OFF:G2 (VIX 15.27, VIX3M 17.96, X 21.14 vs median 21.174999999999997)

CBOE refresh: ok through 2026-10-13; index-vol through 2026-10-13

Entry day: no.

### S-B positions tonight (0)
_none_

### S-B graded at expiry today (0)
_none due_

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
Universe: 2009 names.
Borrow snapshot: 2026-10-13 (the session's own); fee known for 2003 names.
Bull counts: 0:841, 1:763, 2:286, 3:111, 4:8, 5:0, 6:0, 7:0, 8:0
Bear counts: 0:654, 1:716, 2:441, 3:160, 4:32, 5:6, 6:0, 7:0, 8:0

### LONG (70)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ABBV | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ABM | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| ACA | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| ADI | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| AES | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| AMG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMN | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| AMT | 3 | 0 | no |  | x |  |  | x | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| ARW | 3 | 0 | no | x | x |  |  |  | x |  |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| BPRE | 3 | 0 | no |  |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| CNXN | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| CON | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| DSGR | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DV | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| E | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| ECPG | 3 | 0 | no | x |  |  | x |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| EPC | 3 | 0 | yes | x |  |  | x |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| FFIV | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| FTNT | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| GCT | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| GGG | 3 | 0 | yes |  | x |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| GIB | 3 | 0 | no |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| HCA | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| HCI | 3 | 0 | yes |  | x |  | x |  | x | ? |  |  | ? |  |  |  |  |  |  |  |  |  | x |
| HGTY | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| HLF | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| HLI | 3 | 0 | no |  | x |  |  | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| HNGE | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| HXL | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |  |  |  |
| IR | 3 | 0 | yes |  | x |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| JCI | 3 | 0 | no | x | x |  |  |  | x |  |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| JOYY | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| KMPR | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| KNTK | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| LAUR | 4 | 0 | no | x | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| LXP | 3 | 0 | yes | x |  |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  |  |
| MCK | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| MQ | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| MSM | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| MTD | 3 | 0 | no | x |  |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| MUSA | 3 | 0 | yes |  | x |  | x |  |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| NWE | 3 | 0 | no | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PBH | 3 | 0 | no |  |  |  | x | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PD | 3 | 0 | no | x |  |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| PG | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PLUS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| PR | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| PRSU | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| REPX | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| RGA | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SCSC | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| SFL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| SGRY | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| SHEL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SNX | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SPNT | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| SSL | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| SU | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| TALO | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| TBBB | 3 | 0 | no | x | x |  |  |  |  |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| TEN | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TK | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TW | 4 | 0 | no |  | x | x |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| UFCS | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  | ? | ? |  |  |  |  |  |  |  |  |  |
| UTZ | 3 | 0 | yes | x |  |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  |  |
| UVE | 4 | 0 | no | x | x |  | x |  | x | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| VRSN | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| WS | 3 | 0 | yes |  |  |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| WST | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| ZBRA | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |

### SHORT (96)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| AG | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| AI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  |  |
| ALB | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  |  | x |  |  |  | x |
| ALG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| AMSC | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| APLD | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| ARCC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| ARLO | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  |  | x | x |  |  |  |  |
| ARM | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  | x | x |
| BA | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  |  | x |  |  | x | x |
| BLCO | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | ? |  |  | x | x | ? | x |  |  |  |  |
| BMNR | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| BMY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| CAR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  |  |  |  |  |  |  |
| CIEN | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| CLSK | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| CORZ | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  | ? |  |  |  |  | x |
| CPNG | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? | x |  |  |  | x |
| CRI | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x | x |  |  |  | ? | x |  |  |  |  |
| DPZ | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| ECHO | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| ENPH | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| ERAS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  | x |  |  |  |  |  |  | x |
| FIBK | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| FULT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| GLNG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| GLXY | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  | ? |  |  |  |  | x |
| GNTX | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x | x |  |  |  |  |
| GPCR | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  |  |  | x |  |  |
| GVA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| HSY | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x |  |  |  |  |  | x |
| HTO | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| HUBG | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | ? | x |  |  |  |  | x |  | x |  |  |
| HUT | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| HYMC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  |  | x |  |  |  |  |
| INCY | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| INFQ | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| INSM | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  | x |  |  |  | x |
| INTC | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| IP | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| IRTC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| ITRI | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| KHC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| KLAR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  |  |  |  |  |  |  |
| LCII | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| LEGN | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| LMND | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| LQDA | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  | x |  | x |
| LULU | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| MAIN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| MAT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| MP | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  |  |  |  |  | x |
| MU | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| MUX | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | ? |  | x |  |  | ? | x |  |  |  |  |
| NBIS | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| NEM | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  | x |
| NKTR | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  | x |  | x |
| OKLO | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| OPY | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | ? |  |  | x | x | ? | x |  |  |  |  |
| ORCL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| OSIS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| PATK | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  | x |
| PDD | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  |  |  |  |  | x | x |
| PFG | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| PFSI | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  |  |
| POWL | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| PPTA | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| PTGX | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| QBTS | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| QNT | 0 | 3 | yes |  |  | ? |  |  |  |  |  | x |  |  | x |  |  | ? | x |  |  |  |  |
| REPL | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| RH | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  |  |  |  |  | x |
| RIVN | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  | x |  |  | x | x |
| RKLB | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| RKT | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| SAN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| SARO | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| SFBS | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| SFM | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| SHAZ | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  |  |
| SNDK | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| SNDX | 0 | 4 | yes |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  |  |
| SNY | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| SOFI | 0 | 5 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | x | x |  |  | x | x |
| SOLV | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  |  |
| STDN | 0 | 3 | no |  |  | ? |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  | ? |  |  |
| SUPN | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| UPST | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  |  |  |  |  |  | x |
| USAR | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| VALE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| VERA | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| WDC | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| WLDN | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| WOLF | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| XE | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  |  |

### VOL (0)
_none_

CONFLICT (logged only, never a basket, DESIGN/110 §3): 78.

Ledger: emitted 166 (skipped 0), graded 604; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
