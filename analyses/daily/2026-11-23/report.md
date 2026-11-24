# S-A daily — 2026-11-23 (S3)

Preflight: WARN — prices.parquet ends 2026-11-20, BEFORE the 2026-11-23 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-11-20, BEFORE the 2026-11-23 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-11-20, BEFORE the 2026-11-23 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (2)
| ticker | variant | structure | expiry | k | k_up | k_dn | credit_entry | credit_net_pct | risk_usd | contracts | entry_tier_max | cap_pass |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BBY | A1 | SS | 2026-11-27T00:00:00.000 | 97.00 | — | — | 8.18 | +8.09% | 2,323.35 | 1 | 1 | yes |
| BBY | A2 | SS | 2026-11-27T00:00:00.000 | 97.00 | — | — | 8.18 | +8.09% | 2,323.35 | 1 | 1 | yes |

## Suppressed (54)
| ticker | variant | first_fail |
|---|---|---|
| A | A1 | F6 |
| A | A2 | F6 |
| ADI | A1 | F3 |
| ADI | A2 | F3 |
| AMTM | A1 | F4 |
| AMTM | A2 | F4 |
| ANF | A1 | F5 |
| ANF | A2 | F5 |
| BILI | A1 | F4 |
| BILI | A2 | F4 |
| BURL | A1 | F6 |
| BURL | A2 | F6 |
| CMBT | A1 | F4 |
| CMBT | A2 | F4 |
| CMP | A1 | F3 |
| CMP | A2 | F3 |
| DAC | A1 | F4 |
| DAC | A2 | F4 |
| DKS | A1 | F6 |
| DKS | A2 | F6 |
| DLTR | A1 | F6 |
| DLTR | A2 | F6 |
| DY | A1 | F5 |
| DY | A2 | F5 |
| EMBC | A1 | F2 |
| EMBC | A2 | F2 |
| HPE | A1 | F3 |
| HPE | A2 | F3 |
| ITRN | A1 | F3 |
| ITRN | A2 | F3 |
| J | A1 | F5 |
| J | A2 | F5 |
| KC | A1 | F2 |
| KC | A2 | F2 |
| KSS | A1 | F7 |
| KSS | A2 | F7 |
| MDT | A1 | F3 |
| MDT | A2 | F3 |
| MMED | A1 | F5 |
| MMED | A2 | F5 |
| PFLT | A1 | F2 |
| PFLT | A2 | F2 |
| SJM | A1 | F5 |
| SJM | A2 | F5 |
| SMTC | A1 | F6 |
| SMTC | A2 | F6 |
| SYM | A1 | F6 |
| SYM | A2 | F6 |
| TITN | A1 | F3 |
| TITN | A2 | F3 |
| VIPS | A1 | F4 |
| VIPS | A2 | F4 |
| ZM | A1 | F6 |
| ZM | A2 | F6 |

## Exploration book tonight (13; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| A | SS | 2026-12-18T00:00:00.000 | 175.00 | 15.11 | +8.16% | 2,606.62 | F6 |
| BBY | SS | 2026-11-27T00:00:00.000 | 97.00 | 8.18 | +8.09% | 2,323.35 | PASS |
| BILI | SS | 2026-12-18T00:00:00.000 | 11.00 | 1.48 | +12.52% | 236.78 | F4 |
| BURL | SS | 2026-11-27T00:00:00.000 | 235.00 | 24.07 | +9.50% | 6,138.15 | F6 |
| DKS | SS | 2026-11-27T00:00:00.000 | 133.00 | 15.44 | +10.25% | 3,381.73 | F6 |
| DLTR | SS | 2026-11-27T00:00:00.000 | 138.00 | 12.32 | +8.26% | 3,108.97 | F6 |
| HPE | SS | 2026-11-27T00:00:00.000 | 48.00 | 5.77 | +11.75% | 1,703.84 | F3 |
| KSS | SS | 2026-11-27T00:00:00.000 | 21.00 | 2.74 | +12.39% | 724.46 | F7 |
| SMTC | SS | 2026-11-27T00:00:00.000 | 104.00 | 12.58 | +10.91% | 4,893.74 | F6 |
| SMTC | IC | 2026-11-27T00:00:00.000 | 104.00 | 12.41 | +10.68% | 2,858.67 | F6 |
| SYM | SS | 2026-11-27T00:00:00.000 | 35.00 | 4.80 | +12.80% | 1,397.30 | F6 |
| ZM | SS | 2026-11-27T00:00:00.000 | 86.00 | 7.54 | +8.40% | 1,934.71 | F6 |
| ZM | IC | 2026-11-27T00:00:00.000 | 86.00 | 7.31 | +8.03% | 1,068.75 | F6 |

## Graded today (0)
_none due_

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 10 | 7 | +0.68% | 1.50 | 440.76 |
| sa-1.0 | champion | A1 | SS | 37 | 18 | -0.60% | -0.87 | -1,100.72 |
| sa-1.0 | champion | A2 | IC | 9 | 6 | +0.71% | 1.38 | 428.45 |
| sa-1.0 | champion | A2 | SS | 29 | 16 | -0.41% | -0.48 | -73.77 |
| sa-1.0 | exploration | A1 | IC | 65 | 27 | -1.00% | -1.69 | -9,174.86 |
| sa-1.0 | exploration | A1 | SS | 317 | 33 | -0.91% | -3.44 | -24,349.93 |

Ledger: emitted 2 (skipped 0), exploration 13 (skipped 0), graded 0; ledger open.

## S-B state
Gate (2026-11-23, from 2026-11-20 closes): SPY OFF:G1 (VIX 35.89, VIX3M 30.94, X 35.89 vs median 19.455) · QQQ OFF:G1 (VIX 35.89, VIX3M 30.94, X 45.25 vs median 28.77)

Next session (2026-11-24, from 2026-11-23 closes): SPY OFF:G1 (VIX 26.62, VIX3M 25.5, X 26.62 vs median 19.69) · QQQ OFF:G1 (VIX 26.62, VIX3M 25.5, X 36.31 vs median 29.174999999999997)

CBOE refresh: ok through 2026-11-23; index-vol through 2026-11-23

Entry day: no.

### S-B positions tonight (0)
_none_

### S-B graded at expiry today (0)
_none due_

Open positions: QQQ-IC 1, QQQ-PS 1

### S-B forward ledger to date
| policy_id | role | sleeve | n | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|---|
| sb-1.0 | champion | QQQ-IC | 6 | -10.73% | -1.11 | -2,892.74 |
| sb-1.0 | champion | QQQ-PS | 7 | -19.70% | -2.35 | -5,790.26 |
| sb-1.0 | champion | SPY-IC | 3 | -23.56% | -1.24 | -2,411.03 |
| sb-1.0 | champion | SPY-PS | 6 | -10.15% | -0.77 | -2,087.28 |
| sb-1.0 | exploration | QQQ-IC | 6 | -10.73% | -1.11 | -2,892.74 |
| sb-1.0 | exploration | QQQ-PS | 8 | -16.37% | -1.83 | -5,578.07 |
| sb-1.0 | exploration | SPY-IC | 5 | -11.58% | -0.75 | -2,059.26 |
| sb-1.0 | exploration | SPY-PS | 8 | -6.39% | -0.62 | -1,842.87 |

S-B ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0; ledger open.


## S-C state
Entry day: no; ledger open.

### S-C graded at expiry (0)
_none due_

### S-C open book (S-B open: yes; the 40% budget binds only then)
| pair | positions | open_risk_usd | budget_usd | max_sector_positions |
|---|---|---|---|---|
| C1-SS | 5 | 7,539.38 | 8,000.00 | 2 |
| C1-IB | 5 | 3,846.94 | 4,000.00 | 2 |
| C2-SS | 4 | 6,172.04 | 8,000.00 | 2 |
| C2-IB | 4 | 3,034.11 | 4,000.00 | 2 |

### S-C forward ledger to date (entry-week series)
| policy_id | role | pair | n | weeks | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|---|---|
| sc-1.0 | champion | C1-SS | 9 | 4 | -15.22% | -2.49 | -2,831.23 |
| sc-1.0 | champion | C1-IB | 9 | 4 | -29.08% | -2.64 | -3,081.53 |
| sc-1.0 | champion | C2-SS | 8 | 4 | -14.26% | -2.46 | -2,560.19 |
| sc-1.0 | champion | C2-IB | 8 | 4 | -27.55% | -2.62 | -2,798.52 |
| sc-1.0 | exploration | C1-SS | 500 | 5 | -20.16% | -15.31 | -653,580.75 |
| sc-1.0 | exploration | C1-IB | 496 | 5 | -30.88% | -23.29 | -533,174.58 |

Progress to the read: graded entry-weeks 4 of 40 (C1-SS), 4 of 40 (C1-IB), 4 of 40 (C2-SS), 4 of 40 (C2-IB)

S-C ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0.


## Watch basket (wb-1.0, exploration, paper only)
Universe: 2007 names.
Borrow snapshot: 2026-11-23 (the session's own); fee known for 2001 names.
Bull counts: 0:819, 1:761, 2:336, 3:78, 4:13, 5:0, 6:0, 7:0, 8:0
Bear counts: 0:430, 1:748, 2:534, 3:229, 4:56, 5:10, 6:0, 7:0, 8:0

### LONG (29)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AFG | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| AMRX | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| CON | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| COST | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| CRI | 3 | 0 | yes |  | x |  |  | x | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| DGX | 3 | 0 | no | x | x |  |  |  | x |  |  |  |  |  |  |  |  |  |  |  |  |  | x |
| DIS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| EG | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| EPRT | 4 | 0 | no |  | x |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| ES | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| GFF | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| GILD | 3 | 0 | no | x | x |  |  |  | x |  |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| GSAT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HG | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| HZO | 4 | 0 | no | x | x |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| IR | 3 | 0 | no |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LNTH | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| NATL | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| NTSK | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| R | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| RPRX | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SHO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  | ? |  |  |  | ? |  |  |  |  |  |
| TAK | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TGT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VLTO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VRNS | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| WDFC | 3 | 0 | no |  | x |  |  | x | x |  |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| WRB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |

### SHORT (88)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| ACAD | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| ADBE | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| AMZN | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  | x | x |
| ARWR | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| ARXS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| AUPH | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| AVGO | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  | x | x |
| AVLN | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| AX | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| BC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| BE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| BMNR | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  | x | x |
| BPRE | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  |  |
| BRKR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| BXSL | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CAAP | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  |  |
| CACI | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| CARG | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  | x | x |  | ? |  |  |  |  |  |
| CC | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  |  |  |
| CELH | 0 | 5 | yes |  |  |  |  |  |  | ? |  | x | x | x |  | x |  | ? | x |  |  |  | x |
| CFR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| CLF | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| CNP | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| COP | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| CRM | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  | x | x |
| DKNG | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| DLB | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x | ? |  |  |  |  |  |
| DOLE | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  |  |  | x | x | ? |  |  |  |  |  |
| DTM | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  |  |
| DUOL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| EXE | 0 | 5 | yes |  |  |  |  |  |  |  |  | x |  |  | x |  | x | x | x |  |  |  | x |
| FLUT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  | x |
| FLY | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| FRSH | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  |  |
| FRVO | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  | x |  |  |
| GLNG | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x |  |  |  | ? | x |  | x |  |  |
| GS | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| HOMB | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x | x | ? |  |  |  |  |  |
| HOPE | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  |  |
| HUT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| HYMC | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? | x |  |  |  |  |
| IIPR | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? |  |  |  |  |  |
| IMCR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| IMO | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  |  |
| INGR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? |  |  |  |  | x |
| INSP | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| IP | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? |  |  |  |  | x |
| KSS | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x | x |  | ? |  |  |  |  |  |
| LYFT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| M | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? | x |  |  |  | x |
| META | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| MFC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| MNST | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| MOD | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| MP | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  |  | x |
| MRK | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| MTDR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  |  |
| NOG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| NOVT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| NOW | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  | x | x |
| NSP | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| NVCR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| NYT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? |  |  |  |  | x |
| OFG | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| OXY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| PBI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  |  |
| PCOR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| PFG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| PRU | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| ROAD | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| SBUX | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  | x | x |
| SEZL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| SG | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  |  |  |
| SMCI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| SPCX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| STAA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| STWD | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  | x |  | x |
| TAC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| TRGP | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| TTE | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  |  |
| U | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| UGI | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  |  |
| WAL | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? |  |  |  |  |  |
| WOLF | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? |  |  |  |  | x |
| WSM | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| WSO | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| ZM | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |

### VOL (1)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAL | 0 | 2 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? |  | x |  |  | x |

CONFLICT (logged only, never a basket, DESIGN/110 §3): 173.

Ledger: emitted 118 (skipped 0), graded 495; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
