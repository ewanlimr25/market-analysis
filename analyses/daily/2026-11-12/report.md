# S-A daily — 2026-11-12 (S3)

Preflight: WARN — prices.parquet ends 2026-11-06, BEFORE the 2026-11-12 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-11-06, BEFORE the 2026-11-12 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-11-06, BEFORE the 2026-11-12 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (0)
_no event tonight clears the filters._

## Suppressed (50)
| ticker | variant | first_fail |
|---|---|---|
| ALMU | A1 | F2 |
| ALMU | A2 | F2 |
| AMAT | A1 | F3 |
| AMAT | A2 | F3 |
| ARWR | A1 | F6 |
| ARWR | A2 | F6 |
| BLTE | A1 | F4 |
| BLTE | A2 | F4 |
| CBRS | A1 | F7 |
| CBRS | A2 | F7 |
| CSCO | A1 | F3 |
| CSCO | A2 | F3 |
| DLO | A1 | F4 |
| DLO | A2 | F4 |
| DMAC | A1 | F2 |
| DMAC | A2 | F2 |
| DMRC | A1 | F2 |
| DMRC | A2 | F2 |
| FLO | A1 | F2 |
| FLO | A2 | F2 |
| FTW | A1 | F3 |
| FTW | A2 | F3 |
| HAWK | A1 | F3 |
| HAWK | A2 | F3 |
| HTFL | A1 | F5 |
| HTFL | A2 | F5 |
| JCAP | A1 | F3 |
| JCAP | A2 | F3 |
| LFTO | A1 | F4 |
| LFTO | A2 | F4 |
| LWAY | A1 | F3 |
| LWAY | A2 | F3 |
| NKTR | A1 | F3 |
| NKTR | A2 | F3 |
| NPCE | A1 | F3 |
| NPCE | A2 | F3 |
| OFRM | A1 | F3 |
| OFRM | A2 | F3 |
| RMR | A1 | F3 |
| RMR | A2 | F3 |
| SBC | A1 | F2 |
| SBC | A2 | F2 |
| STN | A1 | F4 |
| STN | A2 | F4 |
| STNE | A1 | F2 |
| STNE | A2 | F2 |
| WYY | A1 | F2 |
| WYY | A2 | F2 |
| YSS | A1 | F2 |
| YSS | A2 | F2 |

## Exploration book tonight (3; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| ARWR | SS | 2026-11-20T00:00:00.000 | 47.50 | 4.40 | +8.44% | 1,157.83 | F6 |
| CBRS | SS | 2026-11-20T00:00:00.000 | 98.00 | 17.75 | +17.31% | 4,369.77 | F7 |
| DLO | SS | 2026-11-20T00:00:00.000 | 14.00 | 1.63 | +11.15% | 342.55 | F4 |

## Graded today (11)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| CLBT | A1 | SS | exploration | +2.35% | 29.89 | 1 | no |
| ECO | A1 | SS | exploration | +0.77% | 66.32 | 1 | no |
| FIGR | A1 | SS | exploration | +0.25% | 6.15 | 1 | no |
| FNV | A1 | SS | exploration | -1.25% | -310.46 | 1 | no |
| FPS | A1 | SS | exploration | -2.17% | -53.38 | 1 | no |
| HBM | A1 | SS | exploration | -3.75% | -82.42 | 1 | no |
| LUNR | A1 | SS | exploration | -6.46% | -78.70 | 1 | no |
| NBIS | A1 | SS | exploration | -7.68% | -1,191.47 | 1 | no |
| TWST | A1 | SS | exploration | -3.18% | -389.91 | 2 | no |
| XE | A1 | SS | exploration | +1.02% | 11.19 | 1 | no |
| YETI | A1 | SS | exploration | +1.13% | 48.15 | 1 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 8 | 6 | +0.63% | 1.12 | 245.49 |
| sa-1.0 | champion | A1 | SS | 32 | 15 | -0.77% | -0.98 | -1,477.88 |
| sa-1.0 | champion | A2 | IC | 7 | 5 | +0.66% | 1.00 | 233.18 |
| sa-1.0 | champion | A2 | SS | 25 | 14 | -0.53% | -0.54 | -372.47 |
| sa-1.0 | exploration | A1 | IC | 58 | 23 | -1.11% | -1.67 | -9,252.44 |
| sa-1.0 | exploration | A1 | SS | 283 | 27 | -0.97% | -3.36 | -24,990.45 |

Ledger: emitted 0 (skipped 0), exploration 3 (skipped 0), graded 11; ledger open.

## S-B state
Gate (2026-11-12, from 2026-11-11 closes): SPY OFF:G2 (VIX 17.49, VIX3M 19.24, X 17.49 vs median 18.735) · QQQ OFF:G2 (VIX 17.49, VIX3M 19.24, X 26.74 vs median 26.765)

Next session (2026-11-13, from 2026-11-12 closes): SPY UNKNOWN:null input at 2026-11-12 · QQQ UNKNOWN:null input at 2026-11-12

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
Universe: 1987 names.
Borrow snapshot: 2026-11-12 (the session's own); fee known for 1980 names.
Bull counts: 0:819, 1:655, 2:356, 3:147, 4:10, 5:0, 6:0, 7:0, 8:0
Bear counts: 0:749, 1:753, 2:350, 3:104, 4:29, 5:2, 6:0, 7:0, 8:0

### LONG (87)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AER | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| AIZ | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMGN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMTB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| ANRO | 4 | 0 | no |  | x |  | x | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| AXSM | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BANF | 3 | 0 | no |  |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| BATRK | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BLBD | 3 | 0 | no |  | x | x | x |  |  | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BLK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BRKB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  | x | x |
| BUD | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CE | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| CHE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| CHT | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| CME | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CNK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| CNO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| COLM | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| COMP | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| COST | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| CRBG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| CRUS | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| CTRI | 3 | 0 | yes |  | x |  |  | x | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| DCOM | 3 | 0 | no | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DEO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| DOW | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DRVN | 3 | 0 | yes |  |  | x | x |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| EE | 3 | 0 | yes |  |  | x |  | x | x | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| EG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EGBN | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? | ? |  |  |  |  |  |  |  |  |  |
| EHC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| EMR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EQIX | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EW | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| FAST | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| GFF | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| GWW | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HAYW | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HII | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HUM | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| HZO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| ICE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| KO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LKFT | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| LLY | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| MANU | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| MEOH | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MET | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MSI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| NATL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| NDAQ | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| NWE | 4 | 0 | no | x | x |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| NXPI | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PGR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PLUS | 3 | 0 | no | x |  |  |  | x | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PPLI | 3 | 0 | no |  |  |  | x |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| RLJ | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| RNR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| RPRX | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RSG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SAIC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| SEIC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| SGRY | 3 | 0 | no | x | x |  |  |  |  |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| SIGI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| SMA | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| SPNT | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| STT | 3 | 0 | no |  |  | x | x |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TAK | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| TEL | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TNC | 3 | 0 | no |  |  |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| UTHR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VCTR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VIV | 3 | 0 | no |  | x | x |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| VLTO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VRNS | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| VTOL | 3 | 0 | yes |  | x | x | x |  |  | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| VZ | 3 | 0 | no | x |  |  |  | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| WAB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WAT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WCN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |

### SHORT (80)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| ALNY | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? | x |  | x |  | x |
| ASST | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| ASTS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| AXON | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  | x | x |
| AXTI | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| BA | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| BHVN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| BILI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| BMNR | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| BRKR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| BX | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| BXP | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| CAKE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| CAT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| CELC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| CIGI | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CLMT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? | x | x |  |  |  | x |  |  |  |  |
| COIN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  | x | x |
| CRCL | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| CSGP | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  |  |
| CVNA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| DRTS | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| DVA | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? | x |  |  |  | x |
| ENPH | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| FIG | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| FLG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  | x |
| FSLR | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  | x | x |
| GFL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| GMAB | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| GRAL | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| HIMS | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  | ? | x |  |  |  | x |
| HYMC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| IMAX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| INGR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? |  |  |  |  |  |
| INOD | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  |  |  |
| IONQ | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| IONS | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? | x |  | x |  | x |
| IRTC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  | x |  | ? |  |  |  |  | x |
| KHC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? |  |  |  |  | x |
| KLAR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? |  |  |  |  | x |
| LEGN | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x | x |  | ? |  |  |  |  | x |
| LINE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| LUNR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| MATX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| MELI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| MGA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| MLYS | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  |  |  | x |  | x |
| MMSI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| MSTR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| NEO | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| NFLX | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| NOVT | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| NVDA | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  | x | x |
| ONON | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| ORCL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| PAGP | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x | x |  |  | x | ? |  |  |  |  | x |
| PBI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| PDD | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| PPL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? |  |  |  |  | x |
| PTGX | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| RGTI | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| RIVN | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? | x |  |  |  | x |
| S | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| SEDG | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  |  |
| SLG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| SOFI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| SRPT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| ST | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| SYF | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| SYM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| TREX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| UAL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| UPST | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  |  | x |
| VCYT | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? |  |  |  |  |  |
| WHR | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| WIX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| XP | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| YPF | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x |  |  |  | x |

### VOL (0)
_none_

CONFLICT (logged only, never a basket, DESIGN/110 §3): 70.

Ledger: emitted 167 (skipped 0), graded 524; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
