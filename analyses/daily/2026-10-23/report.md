# S-A daily — 2026-10-23 (S3)

Preflight: WARN — prices.parquet ends 2026-10-16, BEFORE the 2026-10-23 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-10-16, BEFORE the 2026-10-23 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-10-16, BEFORE the 2026-10-23 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (0)
_no event tonight clears the filters._

## Suppressed (20)
| ticker | variant | first_fail |
|---|---|---|
| BFST | A1 | F3 |
| BFST | A2 | F3 |
| BMRC | A1 | F3 |
| BMRC | A2 | F3 |
| BOH | A1 | F4 |
| BOH | A2 | F4 |
| CX | A1 | F2 |
| CX | A2 | F2 |
| DEA | A1 | F3 |
| DEA | A2 | F3 |
| HBT | A1 | F3 |
| HBT | A2 | F3 |
| LKFN | A1 | F3 |
| LKFN | A2 | F3 |
| MED | A1 | F3 |
| MED | A2 | F3 |
| MMYT | A1 | F5 |
| MMYT | A2 | F5 |
| VZ | A1 | F3 |
| VZ | A2 | F3 |

## Exploration book tonight (0; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
_none priceable_

## Graded today (7)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| BAH | A1 | SS | exploration | -1.72% | -134.80 | 2 | no |
| BAH | A1 | IC | exploration | -2.60% | -203.51 | 2 | no |
| BE | A1 | SS | exploration | +0.78% | 169.08 | 1 | no |
| FLG | A1 | SS | exploration | -4.99% | -57.31 | 1 | no |
| INFY | A1 | SS | exploration | -2.10% | -27.76 | 1 | no |
| MXL | A1 | SS | exploration | +1.04% | 67.34 | 1 | no |
| SLB | A1 | SS | exploration | +0.38% | 19.08 | 1 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 2 | 2 | +2.69% | 3.42 | 232.76 |
| sa-1.0 | champion | A1 | SS | 9 | 6 | +0.53% | 0.56 | 317.92 |
| sa-1.0 | champion | A2 | IC | 2 | 2 | +2.69% | 3.42 | 232.76 |
| sa-1.0 | champion | A2 | SS | 9 | 6 | +0.53% | 0.56 | 317.92 |
| sa-1.0 | exploration | A1 | IC | 15 | 12 | -0.89% | -1.46 | -1,769.09 |
| sa-1.0 | exploration | A1 | SS | 53 | 14 | -0.42% | -1.92 | -1,335.54 |

Ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 7; ledger open.

## S-B state
Gate (2026-10-23, from 2026-10-22 closes): SPY ON (VIX 19.03, VIX3M 20.12, X 19.03 vs median 15.855) · QQQ ON (VIX 19.03, VIX3M 20.12, X 28.72 vs median 22.025)

Next session (2026-10-26, from 2026-10-23 closes): SPY ON (VIX 19.45, VIX3M 20.48, X 19.45 vs median 16.055) · QQQ ON (VIX 19.45, VIX3M 20.48, X 28.3 vs median 22.1)

CBOE refresh: ok through 2026-10-23; index-vol through 2026-10-23

Entry day: yes.

### S-B positions tonight (3)
| underlying | structure | expiry | k_p1 | k_p2 | k_c1 | k_c2 | credit_entry | max_loss_usd | contracts | entry_tier_max |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY | PS | 2026-11-13 | 725.00 | 685.00 | — | — | 2.02 | 3,798.04 | 1 | 1 |
| QQQ | PS | 2026-11-13 | 655.00 | 610.00 | — | — | 3.08 | 4,192.18 | 1 | 1 |
| QQQ | IC | 2026-11-13 | 655.00 | 610.00 | 752.00 | 795.00 | 4.79 | 4,020.96 | 1 | 1 |

### S-B skipped (1)
| underlying | structure | reason |
|---|---|---|
| SPY | IC | no_tier1_c2 |

### S-B exploration book tonight (3; one contract per sleeve, gate ignored, gate verdict recorded)
| underlying | structure | expiry | k_p1 | k_p2 | k_c1 | k_c2 | credit_entry | max_loss_usd | gate_verdict |
|---|---|---|---|---|---|---|---|---|---|
| SPY | PS | 2026-11-13 | 725.00 | 685.00 | — | — | 2.02 | 3,798.04 | ON |
| QQQ | PS | 2026-11-13 | 655.00 | 610.00 | — | — | 3.08 | 4,192.18 | ON |
| QQQ | IC | 2026-11-13 | 655.00 | 610.00 | 752.00 | 795.00 | 4.79 | 4,020.96 | ON |

### S-B graded at expiry today (8)
| underlying | structure | entry | expiry | settle_close | net_usd | ror | role |
|---|---|---|---|---|---|---|---|
| SPY | PS | 2026-10-02 | 2026-10-23 | 759.99 | 116.78 | +4.71% | champion |
| SPY | IC | 2026-10-02 | 2026-10-23 | 759.99 | 173.92 | +6.91% | champion |
| QQQ | PS | 2026-10-02 | 2026-10-23 | 704.54 | -554.13 | -15.82% | champion |
| QQQ | IC | 2026-10-02 | 2026-10-23 | 704.54 | -455.03 | -12.30% | champion |
| SPY | PS | 2026-10-02 | 2026-10-23 | 759.99 | 116.78 | +4.71% | exploration |
| SPY | IC | 2026-10-02 | 2026-10-23 | 759.99 | 173.92 | +6.91% | exploration |
| QQQ | PS | 2026-10-02 | 2026-10-23 | 704.54 | -554.13 | -15.82% | exploration |
| QQQ | IC | 2026-10-02 | 2026-10-23 | 704.54 | -455.03 | -12.30% | exploration |

Open positions: QQQ-IC 2, QQQ-PS 3, SPY-PS 2

### S-B forward ledger to date
| policy_id | role | sleeve | n | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|---|
| sb-1.0 | champion | QQQ-IC | 3 | +1.40% | 0.34 | 228.84 |
| sb-1.0 | champion | QQQ-PS | 3 | -1.72% | -0.40 | -140.65 |
| sb-1.0 | champion | SPY-IC | 2 | — | — | 372.65 |
| sb-1.0 | champion | SPY-PS | 3 | +5.06% | 34.39 | 400.25 |
| sb-1.0 | exploration | QQQ-IC | 3 | +1.40% | 0.34 | 228.84 |
| sb-1.0 | exploration | QQQ-PS | 4 | +0.43% | 0.10 | 71.54 |
| sb-1.0 | exploration | SPY-IC | 3 | +6.91% | 23.93 | 543.46 |
| sb-1.0 | exploration | SPY-PS | 4 | +5.10% | 33.81 | 524.57 |

S-B ledger: emitted 3 (skipped 0), exploration 3 (skipped 0), graded 8; ledger open.


## S-C state
Entry day: yes; ledger open.

Stopped at: F1 2259 · F2 1141 · F3 998 · F4 787 · F7 61 · F5 585 · F6 42 · F8 106 · F9 3; C1:selected 1 · C2:selected 1

### S-C positions tonight (4; paper, before the read)
| variant | rank | ticker | sector | structure | close | iv30d | expiry | dte_cal | k | k_up | k_dn | credit_entry | max_loss_usd | stress_loss_usd | entry_cost_usd | contracts | sigma_hold | cap_pass | cap_reason |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 | 1 | AAL | Industrials | IB | 11.94 | 0.47 | 2026-11-20 | 28 | 12.00 | 15.00 | 9.00 | 1.23 | 177.04 | — | 12.65 | 2 | 1.55 | no | cap_budget |
| C1 | 1 | AAL | Industrials | SS | 11.94 | 0.47 | 2026-11-20 | 28 | 12.00 | — | — | 1.29 | — | 343.43 | 6.22 | 2 | 1.55 | yes | — |
| C2 | 1 | AAL | Industrials | IB | 11.94 | 0.47 | 2026-11-20 | 28 | 12.00 | 15.00 | 9.00 | 1.23 | 177.04 | — | 12.65 | 2 | 1.55 | yes | — |
| C2 | 1 | AAL | Industrials | SS | 11.94 | 0.47 | 2026-11-20 | 28 | 12.00 | — | — | 1.29 | — | 343.43 | 6.22 | 2 | 1.55 | no | cap_budget |

Exploration book: 153 priceable names at one contract each, by first failing filter: F1 36, F2 9, F3 86, F4 1, F5 16, F6 1, F9 3, PASS 1

### S-C graded at expiry (0)
_none due_

### S-C open book (S-B open: yes; the 40% budget binds only then)
| pair | positions | open_risk_usd | budget_usd | max_sector_positions |
|---|---|---|---|---|
| C1-SS | 6 | 7,375.54 | 8,000.00 | 3 |
| C1-IB | 5 | 3,962.47 | 4,000.00 | 3 |
| C2-SS | 5 | 7,496.64 | 8,000.00 | 3 |
| C2-IB | 5 | 3,925.40 | 4,000.00 | 3 |

### S-C forward ledger to date (entry-week series)
_ledger empty_

Progress to the read: graded entry-weeks 0 of 40 (C1-SS), 0 of 40 (C1-IB), 0 of 40 (C2-SS), 0 of 40 (C2-IB)

S-C ledger: emitted 4 (skipped 0), exploration 304 (skipped 0), graded 0.


## Watch basket (wb-1.0, exploration, paper only)
Universe: 1971 names.
Borrow snapshot: 2026-10-23 (the session's own); fee known for 1966 names.
Bull counts: 0:651, 1:741, 2:400, 3:142, 4:33, 5:4, 6:0, 7:0, 8:0
Bear counts: 0:718, 1:723, 2:360, 3:132, 4:33, 5:5, 6:0, 7:0, 8:0

### LONG (98)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  | x | x |
| ABM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| ADUS | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| AFG | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALKT | 3 | 0 | no |  | x | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALRM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| AMG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMRX | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| AMT | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| AMTB | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| AMX | 3 | 0 | yes |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| APPN | 3 | 0 | no | x | x |  |  |  |  |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| ASB | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ASND | 3 | 0 | no |  | x | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| AVPT | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BBY | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| BIIB | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| BLLN | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| BP | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| BVS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BY | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| CAH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CFG | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CLBT | 3 | 0 | no |  |  |  | x | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| CNK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| CNR | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| COKE | 3 | 0 | no | x | x |  |  |  | x |  |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| CUBI | 4 | 0 | no | x |  |  | x | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| DBX | 3 | 0 | yes | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  |  |
| DT | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DV | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| E | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| EBAY | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| EPRT | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| FAST | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| FIZZ | 3 | 0 | no |  |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| FLYW | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| FMS | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| FTRE | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| GIB | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| GPOR | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| GWW | 4 | 0 | yes | x | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| HAFN | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HALO | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HCSG | 4 | 0 | no | x |  |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HST | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| IOSP | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| JOE | 3 | 0 | no |  |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| KVUE | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| LFST | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| LH | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| LIN | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LION | 3 | 0 | no |  |  | x |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| LNG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LQDT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| LSPD | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| MAR | 4 | 0 | no | x | x |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| MD | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| MMS | 3 | 0 | yes |  | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  |  |
| MQ | 4 | 0 | no |  | x |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  |
| NSSC | 4 | 0 | no |  | x |  | x | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| NWE | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| NWSA | 4 | 0 | no | x | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| OCFC | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| OVV | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| PLMR | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  |  |
| PNFP | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PRSU | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PRVA | 3 | 0 | no |  | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| PSO | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? | ? |  |  |  |  |  |  |  |  |  |
| RDVT | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| REAL | 3 | 0 | no |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| RNR | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| RPRX | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| RS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| RSG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| SBAC | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SBH | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| SHEL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| SJM | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| SPNT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| SSL | 3 | 0 | no | x | x |  |  |  |  |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| STE | 3 | 0 | yes |  | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| SU | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  | x | x |
| TEN | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TENB | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TRMD | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TTC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| TW | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| TYL | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| UCB | 5 | 0 | no | x | x |  | x |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| VLTO | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| VSTS | 4 | 0 | yes |  | x |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| W | 3 | 0 | yes | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| WMT | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| WOR | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| XPRO | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |

### SHORT (86)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AA | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| AAOI | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| AG | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  | x |
| ALB | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  | x |
| ALG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| AMSC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| APLD | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  |  |  |  |  |  | x |
| ASTS | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  | x | x |
| BA | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| BDC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| BKV | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | ? |  | x |  |  | ? | x |  |  |  | x |
| BNL | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  | x |  |  |
| CBRS | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| CC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CDE | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  | x |
| CHEF | 0 | 4 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  |  |
| CLMT | 0 | 4 | yes |  |  |  |  |  |  | ? |  |  | ? | x | x | x |  | ? | x |  |  |  |  |
| CLS | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| CMG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| COIN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  | x | x |
| CORZ | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  |  |  |  |  |  | x |
| CPNG | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? | x |  |  |  | x |
| CRCL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |  |  | x |
| CRWV | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| CSWC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| DAR | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  |  | x |  |  | x | x |  |  |  |  |
| ECHO | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| ELAN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| FIGR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| FSK | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| GDS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| GE | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| GGG | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  | x |  | ? | x |  |  |  | x |
| GLXY | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  |  |  |  |  | x |
| GOOG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  | x | x |
| GOOGL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  | x | x |
| HIMS | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x | x |  | ? |  |  |  |  | x |
| HL | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  | x |
| HOOD | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  |  | x | x |
| HYMC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  |  | x |  |  |  |  |
| IAG | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| INFY | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  | x |  | ? |  |  |  |  | x |
| INSM | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  | x |  |  |  | x |
| IONQ | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| IREN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  | x | x |
| JMKE | 0 | 3 | yes |  |  | ? |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  | ? |  |  |
| KOD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  |  |  |
| KT | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| KTOS | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| LUNR | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  |  |
| META | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| MGA | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| MP | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  |  |  |  |  | x |
| MSGS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? |  |  |  |  | x |
| MWH | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| NCLH | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| OKLO | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  | x |
| PCG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| PKX | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| PL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| PPTA | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  |  |  |
| QBTS | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  | x |
| RCUS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| REPL | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x |  |  |  | ? | x |  |  |  |  |
| RIOT | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| RIVN | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  | x |  |  |  | x |
| RKLB | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| SCCO | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| SKHY | 0 | 3 | no |  |  | ? |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  | x | x |
| SLM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| SLS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  |  |
| SMCI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| SOFI | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| SPCX | 0 | 4 | no |  |  | ? |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| STEP | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| TMDX | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  | x |  |  |  |  |  |  |  |  |
| TNGX | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| TTMI | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| VALE | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| VC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  | x |
| VKTX | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| WLDN | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| WOLF | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  | ? |  |  |  |  |  |
| WULF | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  |  |  |  |  |  | x |
| XE | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  | x |  | x |
| XYZ | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  |  | x |

### VOL (2)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAL | 0 | 1 | yes |  |  |  |  |  |  | ? |  |  |  |  | x |  |  |  |  | x |  |  | x |
| GME | 0 | 2 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? |  | x |  |  | x |

CONFLICT (logged only, never a basket, DESIGN/110 §3): 83.

Ledger: emitted 186 (skipped 0), graded 539; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
