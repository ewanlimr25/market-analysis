# S-A daily — 2026-11-18 (S3)

Preflight: WARN — prices.parquet ends 2026-11-13, BEFORE the 2026-11-18 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-11-13, BEFORE the 2026-11-18 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-11-13, BEFORE the 2026-11-18 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (2)
| ticker | variant | structure | expiry | k | k_up | k_dn | credit_entry | credit_net_pct | risk_usd | contracts | entry_tier_max | cap_pass |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| WSM | A1 | SS | 2026-11-20T00:00:00.000 | 260.00 | — | — | 20.32 | +7.59% | 5,136.03 | 1 | 1 | no |
| WSM | A2 | SS | 2026-11-20T00:00:00.000 | 260.00 | — | — | 20.32 | +7.59% | 5,136.03 | 1 | 1 | no |

## Suppressed (60)
| ticker | variant | first_fail |
|---|---|---|
| BABA | A1 | F3 |
| BABA | A2 | F3 |
| BBWI | A1 | F6 |
| BBWI | A2 | F6 |
| CPA | A1 | F4 |
| CPA | A2 | F4 |
| DAO | A1 | F3 |
| DAO | A2 | F3 |
| FUTU | A1 | F6 |
| FUTU | A2 | F6 |
| HP | A1 | F4 |
| HP | A2 | F4 |
| JOYY | A1 | F4 |
| JOYY | A2 | F4 |
| KLIC | A1 | F4 |
| KLIC | A2 | F4 |
| LQDT | A1 | F3 |
| LQDT | A2 | F3 |
| MAGN | A1 | F3 |
| MAGN | A2 | F3 |
| MANU | A1 | F3 |
| MANU | A2 | F3 |
| MMS | A1 | F4 |
| MMS | A2 | F4 |
| NJR | A1 | F4 |
| NJR | A2 | F4 |
| NTES | A1 | F3 |
| NTES | A2 | F3 |
| P | A1 | F7 |
| P | A2 | F7 |
| PANW | A1 | F3 |
| PANW | A2 | F3 |
| PCYO | A1 | F3 |
| PCYO | A2 | F3 |
| PDD | A1 | F3 |
| PDD | A2 | F3 |
| ROAD | A1 | F5 |
| ROAD | A2 | F5 |
| RRGB | A1 | F2 |
| RRGB | A2 | F2 |
| SBLK | A1 | F4 |
| SBLK | A2 | F4 |
| SNEX | A1 | F5 |
| SNEX | A2 | F5 |
| TEN | A1 | F3 |
| TEN | A2 | F3 |
| UGI | A1 | F4 |
| UGI | A2 | F4 |
| UTI | A1 | F3 |
| UTI | A2 | F3 |
| VVV | A1 | F5 |
| VVV | A2 | F5 |
| WMG | A1 | F5 |
| WMG | A2 | F5 |
| WMT | A1 | F3 |
| WMT | A2 | F3 |
| WWD | A1 | F5 |
| WWD | A2 | F5 |
| YMM | A1 | F2 |
| YMM | A2 | F2 |

## Exploration book tonight (8; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| BBWI | SS | 2026-11-20T00:00:00.000 | 18.50 | 2.20 | +11.05% | 562.87 | F6 |
| FUTU | SS | 2026-11-20T00:00:00.000 | 82.45 | 5.53 | +6.30% | 2,540.90 | F6 |
| MMS | SS | 2026-11-20T00:00:00.000 | 65.00 | 5.25 | +4.35% | 1,178.81 | F4 |
| P | SS | 2026-11-20T00:00:00.000 | 100.00 | 14.16 | +13.54% | 3,996.20 | F7 |
| P | IC | 2026-11-20T00:00:00.000 | 100.00 | 13.78 | +13.06% | 2,122.22 | F7 |
| SBLK | SS | 2026-11-20T00:00:00.000 | 27.00 | 1.15 | +3.73% | 579.94 | F4 |
| UTI | SS | 2026-11-20T00:00:00.000 | 22.50 | 2.99 | +12.62% | 767.16 | F3 |
| WSM | SS | 2026-11-20T00:00:00.000 | 260.00 | 20.32 | +7.59% | 5,136.03 | PASS |

## Graded today (6)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| BLSH | A1 | SS | exploration | -1.61% | -31.02 | 1 | no |
| GLBE | A1 | SS | exploration | +1.67% | 66.32 | 1 | no |
| GLBE | A1 | IC | exploration | +0.93% | 36.89 | 1 | no |
| LZB | A1 | SS | exploration | +1.33% | 40.44 | 1 | no |
| TGT | A1 | SS | exploration | +2.90% | 462.20 | 1 | no |
| ZIM | A1 | SS | exploration | -1.86% | -55.31 | 1 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 10 | 7 | +0.68% | 1.50 | 440.76 |
| sa-1.0 | champion | A1 | SS | 36 | 17 | -0.62% | -0.88 | -1,165.96 |
| sa-1.0 | champion | A2 | IC | 9 | 6 | +0.71% | 1.38 | 428.45 |
| sa-1.0 | champion | A2 | SS | 28 | 15 | -0.43% | -0.49 | -139.01 |
| sa-1.0 | exploration | A1 | IC | 62 | 25 | -1.07% | -1.74 | -9,389.97 |
| sa-1.0 | exploration | A1 | SS | 304 | 31 | -0.95% | -3.50 | -24,788.39 |

Ledger: emitted 2 (skipped 0), exploration 8 (skipped 0), graded 6; ledger open.

## S-B state
Gate (2026-11-18, from 2026-11-17 closes): SPY OFF:G1 (VIX 25.46, VIX3M 24.98, X 25.46 vs median 19.165) · QQQ OFF:G1 (VIX 25.46, VIX3M 24.98, X 34.44 vs median 28.525)

Next session (2026-11-19, from 2026-11-18 closes): SPY OFF:G1 (VIX 24.56, VIX3M 24.29, X 24.56 vs median 19.36) · QQQ OFF:G1 (VIX 24.56, VIX3M 24.29, X 33.12 vs median 28.560000000000002)

CBOE refresh: ok through 2026-11-18; index-vol through 2026-11-18

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

S-C ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 6.


## Watch basket (wb-1.0, exploration, paper only)
Universe: 1984 names.
Borrow snapshot: 2026-11-17 (fallback, 1 day old); fee known for 1977 names.
Bull counts: 0:756, 1:762, 2:349, 3:104, 4:13, 5:0, 6:0, 7:0, 8:0
Bear counts: 0:437, 1:763, 2:526, 3:191, 4:56, 5:11, 6:0, 7:0, 8:0

### LONG (38)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ADP | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AIZ | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMRX | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| ASND | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| BJ | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BWIN | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| COST | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| DEO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DIS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| EG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| ES | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EXC | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| GFF | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| GSAT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HG | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| HST | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HZO | 3 | 0 | no | x |  |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  |  |
| IBN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| IVZ | 3 | 0 | no |  | x |  | x | x |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| J | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LFUS | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LNTH | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| MDT | 3 | 0 | no |  | x |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| PG | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PWR | 3 | 0 | yes |  | x | x | x |  |  | ? |  |  |  |  |  |  |  | ? |  |  |  | x | x |
| R | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| REGN | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RLJ | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| SIGI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| STE | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| TAK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| VGNT | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| VRNS | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| WM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WRB | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WTRG | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| XHR | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  |  |

### SHORT (97)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ABNB | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| ADNT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| AMR | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  |  |
| ARES | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x |  | x |  | ? |  |  |  |  | x |
| ARWR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? | x |  | x |  | x |
| ASST | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  | x |
| AUPH | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| BC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| BEAM | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| BHF | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  | x |  |  |
| BIDU | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x | x |  |  | x |
| BLLN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| BTU | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  |  | x |  |  |  |  |
| BVN | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CAMT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| CBRS | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| CHRD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| CIGI | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CLMT | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  |  |
| CPNG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? |  |  |  |  | x |
| CYTK | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? | x |  |  |  | x |
| DNTH | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| DOCU | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| DOX | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? |  |  | x |  | x |
| DRTS | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| DVA | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  | x | ? | x |  |  |  | x |
| ENB | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| ENS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  |  |
| FDS | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| FIG | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| FLY | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? |  |  |  |  |  |
| FOR | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| FSLY | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| GENB | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| GFL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| GIL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  | x |
| GNTX | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  |  |
| HIMS | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  | ? | x |  |  |  | x |
| HTGC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| HUBS | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  |  |  | x |  | ? | x |  |  |  | x |
| IDYA | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| IMCR | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? | x |  |  |  |  |
| IMVT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| INOD | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  |  |
| IPGP | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| KEN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  |  |
| LEGN | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? |  |  |  |  |  |
| LGND | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| LIND | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| LQDA | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  | x |
| M | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| MAT | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  |  |  |
| MELI | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| MFC | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| MGA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| MQ | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| MSDL | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| NKE | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| NOG | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| NSP | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| NVCR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| NVDA | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  | x | x | x |
| NVO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| OKLO | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  | x |  | x |
| OLED | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| OXY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| PAGP | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  | x | ? |  |  |  |  |  |
| PATH | 0 | 4 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? | x |  |  |  | x |
| PCVX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| PFG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| PGY | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x | x |  | ? |  |  |  |  |  |
| PTCT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? |  |  |  |  |  |
| PTGX | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| RH | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| RLAY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| RRR | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| RTX | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  |  | x |
| SGHC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  |  |
| SKE | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? |  |  |  |  |  |
| SMMT | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x |  | x |  | ? |  |  |  |  | x |
| SPB | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| SRPT | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  |  |
| STLD | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| TAC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| TNGX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| TTAM | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| TTD | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  | ? |  |  |  |  | x |
| UPST | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  | x |  |  |
| VKTX | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  |  | x |
| VSAT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| WLY | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| WMS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| WRBY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| WSO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| XENE | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| XP | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  | x |  |  | x |
| ZM | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  |  | x |

### VOL (1)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| APA | 1 | 1 | yes |  |  |  |  |  |  | ? | x |  |  |  |  | x |  | ? |  | x |  |  | x |

CONFLICT (logged only, never a basket, DESIGN/110 §3): 125.

Ledger: emitted 136 (skipped 0), graded 549; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
