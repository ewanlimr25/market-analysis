# S-A daily — 2026-11-02 (S3)

Preflight: WARN — prices.parquet ends 2026-10-30, BEFORE the 2026-11-02 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-10-30, BEFORE the 2026-11-02 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-10-30, BEFORE the 2026-11-02 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (3)
| ticker | variant | structure | expiry | k | k_up | k_dn | credit_entry | credit_net_pct | risk_usd | contracts | entry_tier_max | cap_pass |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DT | A1 | SS | 2026-11-20T00:00:00.000 | 55.00 | — | — | 6.87 | +12.02% | 1,281.23 | 1 | 1 | yes |
| ON | A1 | SS | 2026-11-06T00:00:00.000 | 70.00 | — | — | 7.34 | +10.16% | 2,147.44 | 1 | 1 | no |
| FISV | A1 | SS | 2026-11-06T00:00:00.000 | 52.00 | — | — | 4.90 | +9.20% | 1,191.90 | 1 | 1 | yes |

## Suppressed (337)
| ticker | variant | first_fail |
|---|---|---|
| AAPL | A1 | F3 |
| AAPL | A2 | F3 |
| ADEA | A1 | F4 |
| ADEA | A2 | F4 |
| ADM | A1 | F5 |
| ADM | A2 | F5 |
| ADT | A1 | F2 |
| ADT | A2 | F2 |
| ADTN | A1 | F2 |
| ADTN | A2 | F2 |
| AEHR | A1 | F3 |
| AEHR | A2 | F3 |
| AEIS | A1 | F5 |
| AEIS | A2 | F5 |
| AESI | A1 | F2 |
| AESI | A2 | F2 |
| AHCO | A1 | F2 |
| AHCO | A2 | F2 |
| AHRT | A1 | F2 |
| AHRT | A2 | F2 |
| ALG | A1 | F3 |
| ALG | A2 | F3 |
| ALKS | A1 | F5 |
| ALKS | A2 | F5 |
| ALSN | A1 | F5 |
| ALSN | A2 | F5 |
| AME | A1 | F3 |
| AME | A2 | F3 |
| AMRX | A1 | F5 |
| AMRX | A2 | F5 |
| APO | A1 | F3 |
| APO | A2 | F3 |
| APTV | A1 | F5 |
| APTV | A2 | F5 |
| AROC | A1 | F4 |
| AROC | A2 | F4 |
| ARVN | A1 | F2 |
| ARVN | A2 | F2 |
| ASC | A1 | F3 |
| ASC | A2 | F3 |
| BALL | A1 | F5 |
| BALL | A2 | F5 |
| BCC | A1 | F4 |
| BCC | A2 | F4 |
| BETA | A1 | F4 |
| BETA | A2 | F4 |
| BLZE | A1 | F2 |
| BLZE | A2 | F2 |
| BMRN | A1 | F5 |
| BMRN | A2 | F5 |
| BNTX | A1 | F5 |
| BNTX | A2 | F5 |
| BR | A1 | F5 |
| BR | A2 | F5 |
| BRCC | A1 | F3 |
| BRCC | A2 | F3 |
| BVS | A1 | F3 |
| BVS | A2 | F3 |
| BWXT | A1 | F5 |
| BWXT | A2 | F5 |
| CALX | A1 | F4 |
| CALX | A2 | F4 |
| CBT | A1 | F4 |
| CBT | A2 | F4 |
| CC | A1 | F3 |
| CC | A2 | F3 |
| CE | A1 | F5 |
| CE | A2 | F5 |
| CLX | A1 | F6 |
| CLX | A2 | F6 |
| CMCO | A1 | F3 |
| CMCO | A2 | F3 |
| CNK | A1 | F5 |
| CNK | A2 | F5 |
| CRBG | A1 | F5 |
| CRBG | A2 | F5 |
| CRC | A1 | F4 |
| CRC | A2 | F4 |
| CRGY | A1 | F5 |
| CRGY | A2 | F5 |
| CSR | A1 | F3 |
| CSR | A2 | F3 |
| CSWC | A1 | F3 |
| CSWC | A2 | F3 |
| CVI | A1 | F4 |
| CVI | A2 | F4 |
| CWH | A1 | F2 |
| CWH | A2 | F2 |
| DD | A1 | F5 |
| DD | A2 | F5 |
| DHC | A1 | F2 |
| DHC | A2 | F2 |
| DOC | A1 | F5 |
| DOC | A2 | F5 |
| DOCN | A1 | F6 |
| DOCN | A2 | F6 |
| DT | A2 | A2_sector |
| DTIL | A1 | F2 |
| DTIL | A2 | F2 |
| EBS | A1 | F2 |
| EBS | A2 | F2 |
| ENLT | A1 | F4 |
| ENLT | A2 | F4 |
| EQH | A1 | F5 |
| EQH | A2 | F5 |
| ERO | A1 | F4 |
| ERO | A2 | F4 |
| ETN | A1 | F3 |
| ETN | A2 | F3 |
| EVER | A1 | F3 |
| EVER | A2 | F3 |
| EXPD | A1 | F5 |
| EXPD | A2 | F5 |
| FANG | A1 | F3 |
| FANG | A2 | F3 |
| FISV | A2 | A2_sector |
| FMS | A1 | F4 |
| FMS | A2 | F4 |
| FN | A1 | F7 |
| FN | A2 | F7 |
| FTS | A1 | F5 |
| FTS | A2 | F5 |
| FWRG | A1 | F3 |
| FWRG | A2 | F3 |
| GPK | A1 | F2 |
| GPK | A2 | F2 |
| HGTY | A1 | F3 |
| HGTY | A2 | F3 |
| HLF | A1 | F3 |
| HLF | A2 | F3 |
| HLIT | A1 | F3 |
| HLIT | A2 | F3 |
| HLMN | A1 | F2 |
| HLMN | A2 | F2 |
| HLNE | A1 | F5 |
| HLNE | A2 | F5 |
| HNGE | A1 | F6 |
| HNGE | A2 | F6 |
| HNI | A1 | F4 |
| HNI | A2 | F4 |
| HSIC | A1 | F5 |
| HSIC | A2 | F5 |
| HUN | A1 | F2 |
| HUN | A2 | F2 |
| IBTA | A1 | F3 |
| IBTA | A2 | F3 |
| ICHR | A1 | F3 |
| ICHR | A2 | F3 |
| IIPR | A1 | F3 |
| IIPR | A2 | F3 |
| INSP | A1 | F3 |
| INSP | A2 | F3 |
| IPGP | A1 | F4 |
| IPGP | A2 | F4 |
| IRT | A1 | F5 |
| IRT | A2 | F5 |
| IT | A1 | F5 |
| IT | A2 | F5 |
| JAZZ | A1 | F5 |
| JAZZ | A2 | F5 |
| JBTM | A1 | F5 |
| JBTM | A2 | F5 |
| KDP | A1 | F3 |
| KDP | A2 | F3 |
| KNF | A1 | F4 |
| KNF | A2 | F4 |
| LBTYA | A1 | F2 |
| LBTYA | A2 | F2 |
| LBTYK | A1 | F2 |
| LBTYK | A2 | F2 |
| LDOS | A1 | F5 |
| LDOS | A2 | F5 |
| LGIH | A1 | F3 |
| LGIH | A2 | F3 |
| LIFE | A1 | F3 |
| LIFE | A2 | F3 |
| LIND | A1 | F4 |
| LIND | A2 | F4 |
| LPX | A1 | F5 |
| LPX | A2 | F5 |
| LSCC | A1 | F6 |
| LSCC | A2 | F6 |
| MDGL | A1 | F5 |
| MDGL | A2 | F5 |
| MPC | A1 | F3 |
| MPC | A2 | F3 |
| MSA | A1 | F4 |
| MSA | A2 | F4 |
| MTCH | A1 | F6 |
| MTCH | A2 | F6 |
| MTUS | A1 | F3 |
| MTUS | A2 | F3 |
| MZTI | A1 | F4 |
| MZTI | A2 | F4 |
| NBIX | A1 | F5 |
| NBIX | A2 | F5 |
| NMFC | A1 | F2 |
| NMFC | A2 | F2 |
| NPO | A1 | F5 |
| NPO | A2 | F5 |
| NXRT | A1 | F3 |
| NXRT | A2 | F3 |
| O | A1 | F3 |
| O | A2 | F3 |
| OGS | A1 | F4 |
| OGS | A2 | F4 |
| ON | A2 | A2_sector |
| OTTR | A1 | F4 |
| OTTR | A2 | F4 |
| PAM | A1 | F4 |
| PAM | A2 | F4 |
| PAX | A1 | F2 |
| PAX | A2 | F2 |
| PAY | A1 | F4 |
| PAY | A2 | F4 |
| PFE | A1 | F3 |
| PFE | A2 | F3 |
| PHG | A1 | F4 |
| PHG | A2 | F4 |
| PJT | A1 | F5 |
| PJT | A2 | F5 |
| PLOW | A1 | F3 |
| PLOW | A2 | F3 |
| PLTR | A1 | F3 |
| PLTR | A2 | F3 |
| PNW | A1 | F5 |
| PNW | A2 | F5 |
| PPLI | A1 | F4 |
| PPLI | A2 | F4 |
| PS | A1 | F4 |
| PS | A2 | F4 |
| RACE | A1 | F3 |
| RACE | A2 | F3 |
| RHP | A1 | F5 |
| RHP | A2 | F5 |
| RIG | A1 | F2 |
| RIG | A2 | F2 |
| RNW | A1 | F2 |
| RNW | A2 | F2 |
| ROKU | A1 | F6 |
| ROKU | A2 | F6 |
| RRX | A1 | F5 |
| RRX | A2 | F5 |
| RVTY | A1 | F5 |
| RVTY | A2 | F5 |
| RYTM | A1 | F5 |
| RYTM | A2 | F5 |
| SBAC | A1 | F5 |
| SBAC | A2 | F5 |
| SBRA | A1 | F4 |
| SBRA | A2 | F4 |
| SHC | A1 | F4 |
| SHC | A2 | F4 |
| SHOP | A1 | F3 |
| SHOP | A2 | F3 |
| SIBN | A1 | F3 |
| SIBN | A2 | F3 |
| SOPH | A1 | F2 |
| SOPH | A2 | F2 |
| SRAD | A1 | F4 |
| SRAD | A2 | F4 |
| STVN | A1 | F4 |
| STVN | A2 | F4 |
| SUNC | A1 | F4 |
| SUNC | A2 | F4 |
| SYY | A1 | F5 |
| SYY | A2 | F5 |
| TAC | A1 | F4 |
| TAC | A2 | F4 |
| TBBB | A1 | F4 |
| TBBB | A2 | F4 |
| TCMD | A1 | F3 |
| TCMD | A2 | F3 |
| TEVA | A1 | F6 |
| TEVA | A2 | F6 |
| TLN | A1 | F5 |
| TLN | A2 | F5 |
| TNC | A1 | F3 |
| TNC | A2 | F3 |
| TRI | A1 | F3 |
| TRI | A2 | F3 |
| TTI | A1 | F2 |
| TTI | A2 | F2 |
| TVTX | A1 | F5 |
| TVTX | A2 | F5 |
| UDR | A1 | F5 |
| UDR | A2 | F5 |
| ULS | A1 | F5 |
| ULS | A2 | F5 |
| UMH | A1 | F3 |
| UMH | A2 | F3 |
| UPST | A1 | F7 |
| UPST | A2 | F7 |
| UPWK | A1 | F2 |
| UPWK | A2 | F2 |
| UTL | A1 | F3 |
| UTL | A2 | F3 |
| VAL | A1 | F5 |
| VAL | A2 | F5 |
| VITL | A1 | F2 |
| VITL | A2 | F2 |
| VNO | A1 | F4 |
| VNO | A2 | F4 |
| VNOM | A1 | F5 |
| VNOM | A2 | F5 |
| VOYA | A1 | F5 |
| VOYA | A2 | F5 |
| VOYG | A1 | F3 |
| VOYG | A2 | F3 |
| VRTX | A1 | F3 |
| VRTX | A2 | F3 |
| VSNT | A1 | F5 |
| VSNT | A2 | F5 |
| VTS | A1 | F3 |
| VTS | A2 | F3 |
| VVX | A1 | F4 |
| VVX | A2 | F4 |
| WAT | A1 | F5 |
| WAT | A2 | F5 |
| WAY | A1 | F5 |
| WAY | A2 | F5 |
| WMB | A1 | F3 |
| WMB | A2 | F3 |
| XHR | A1 | F3 |
| XHR | A2 | F3 |
| XIFR | A1 | F2 |
| XIFR | A2 | F2 |
| XMTR | A1 | F5 |
| XMTR | A2 | F5 |
| XPRO | A1 | F3 |
| XPRO | A2 | F3 |
| YUM | A1 | F5 |
| YUM | A2 | F5 |
| YUMC | A1 | F5 |
| YUMC | A2 | F5 |
| ZBRA | A1 | F5 |
| ZBRA | A2 | F5 |

## Exploration book tonight (24; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| AEHR | SS | 2026-11-06T00:00:00.000 | 51.00 | 8.99 | +16.45% | 2,787.43 | F3 |
| APO | SS | 2026-11-06T00:00:00.000 | 119.00 | 6.68 | +5.05% | 2,449.74 | F3 |
| CLX | SS | 2026-11-20T00:00:00.000 | 90.00 | 7.36 | +7.74% | 1,478.25 | F6 |
| CLX | IC | 2026-11-20T00:00:00.000 | 90.00 | 6.84 | +7.07% | 816.24 | F6 |
| DOCN | SS | 2026-11-06T00:00:00.000 | 90.00 | 14.14 | +14.75% | 4,466.21 | F6 |
| DT | SS | 2026-11-20T00:00:00.000 | 55.00 | 6.87 | +12.02% | 1,281.23 | PASS |
| FANG | SS | 2026-11-20T00:00:00.000 | 200.00 | 14.20 | +6.88% | 3,002.30 | F3 |
| FANG | IC | 2026-11-20T00:00:00.000 | 200.00 | 13.06 | +6.17% | 1,694.10 | F3 |
| FISV | SS | 2026-11-06T00:00:00.000 | 52.00 | 4.90 | +9.20% | 1,191.90 | PASS |
| FN | SS | 2026-11-20T00:00:00.000 | 320.00 | 59.40 | +18.20% | 11,149.50 | F7 |
| FN | IC | 2026-11-20T00:00:00.000 | 320.00 | 54.59 | +16.44% | 6,541.13 | F7 |
| HLF | SS | 2026-11-06T00:00:00.000 | 13.00 | 1.79 | +12.37% | 375.32 | F3 |
| HNGE | SS | 2026-11-20T00:00:00.000 | 115.00 | 17.18 | +13.36% | 3,310.92 | F6 |
| LSCC | SS | 2026-11-20T00:00:00.000 | 95.00 | 15.96 | +15.18% | 3,070.95 | F6 |
| LSCC | IC | 2026-11-20T00:00:00.000 | 95.00 | 14.45 | +13.19% | 1,554.51 | F6 |
| MTCH | SS | 2026-11-20T00:00:00.000 | 42.50 | 4.60 | +10.31% | 701.36 | F6 |
| MTCH | IC | 2026-11-20T00:00:00.000 | 42.50 | 3.99 | +8.66% | 351.15 | F6 |
| O | SS | 2026-11-20T00:00:00.000 | 57.50 | 2.27 | +3.76% | 1.00 | F3 |
| ON | SS | 2026-11-06T00:00:00.000 | 70.00 | 7.34 | +10.16% | 2,147.44 | PASS |
| ROKU | SS | 2026-11-06T00:00:00.000 | 155.00 | 6.67 | +4.04% | 1,525.14 | F6 |
| ROKU | IC | 2026-11-06T00:00:00.000 | 155.00 | 5.91 | +3.38% | 908.50 | F6 |
| TEVA | SS | 2026-11-06T00:00:00.000 | 41.00 | 2.88 | +6.59% | 725.65 | F6 |
| UPST | SS | 2026-11-06T00:00:00.000 | 21.50 | 2.86 | +13.03% | 718.09 | F7 |
| WMB | SS | 2026-11-06T00:00:00.000 | 72.00 | 3.63 | +4.88% | 1,110.96 | F3 |

## Graded today (4)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| CHKP | A1 | SS | exploration | +1.98% | 300.51 | 1 | no |
| CHKP | A1 | IC | exploration | +0.50% | 76.57 | 2 | no |
| EL | A1 | SS | exploration | -0.06% | -6.06 | 1 | no |
| TEM | A1 | SS | exploration | +0.50% | 36.07 | 1 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 6 | 4 | +0.80% | 0.99 | 268.43 |
| sa-1.0 | champion | A1 | SS | 21 | 10 | -0.15% | -0.26 | -1,097.49 |
| sa-1.0 | champion | A2 | IC | 6 | 4 | +0.80% | 0.99 | 268.43 |
| sa-1.0 | champion | A2 | SS | 20 | 10 | -0.01% | -0.01 | -629.42 |
| sa-1.0 | exploration | A1 | IC | 32 | 16 | -1.46% | -1.68 | -2,684.92 |
| sa-1.0 | exploration | A1 | SS | 147 | 19 | -0.91% | -2.91 | -10,139.18 |

Ledger: emitted 3 (skipped 0), exploration 24 (skipped 0), graded 4; ledger open.

## S-B state
Gate (2026-11-02, from 2026-10-30 closes): SPY ON (VIX 19.42, VIX3M 20.78, X 19.42 vs median 16.775) · QQQ ON (VIX 19.42, VIX3M 20.78, X 28.5 vs median 23.335)

Next session (2026-11-03, from 2026-11-02 closes): SPY ON (VIX 21.15, VIX3M 21.6, X 21.15 vs median 16.89) · QQQ ON (VIX 21.15, VIX3M 21.6, X 30.89 vs median 24.1)

CBOE refresh: ok through 2026-11-02; index-vol through 2026-11-02

Entry day: no.

### S-B positions tonight (0)
_none_

### S-B graded at expiry today (0)
_none due_

Open positions: QQQ-IC 3, QQQ-PS 3, SPY-IC 1, SPY-PS 3

### S-B forward ledger to date
| policy_id | role | sleeve | n | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|---|
| sb-1.0 | champion | QQQ-IC | 3 | +1.40% | 0.34 | 228.84 |
| sb-1.0 | champion | QQQ-PS | 4 | -15.42% | -1.22 | -2,226.57 |
| sb-1.0 | champion | SPY-IC | 2 | — | — | 372.65 |
| sb-1.0 | champion | SPY-PS | 3 | +5.06% | 34.39 | 400.25 |
| sb-1.0 | exploration | QQQ-IC | 3 | +1.40% | 0.34 | 228.84 |
| sb-1.0 | exploration | QQQ-PS | 5 | -10.96% | -0.92 | -2,014.38 |
| sb-1.0 | exploration | SPY-IC | 4 | +6.91% | 31.77 | 724.42 |
| sb-1.0 | exploration | SPY-PS | 5 | +4.98% | 25.88 | 644.67 |

S-B ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0; ledger open.


## S-C state
Entry day: no; ledger open.

### S-C graded at expiry (0)
_none due_

### S-C open book (S-B open: yes; the 40% budget binds only then)
| pair | positions | open_risk_usd | budget_usd | max_sector_positions |
|---|---|---|---|---|
| C1-SS | 3 | 5,111.92 | 8,000.00 | 1 |
| C1-IB | 2 | 2,434.65 | 4,000.00 | 1 |
| C2-SS | 3 | 5,888.76 | 8,000.00 | 1 |
| C2-IB | 3 | 2,788.73 | 4,000.00 | 1 |

### S-C forward ledger to date (entry-week series)
| policy_id | role | pair | n | weeks | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|---|---|
| sc-1.0 | champion | C1-SS | 5 | 1 | — | — | -802.36 |
| sc-1.0 | champion | C1-IB | 5 | 1 | — | — | -929.16 |
| sc-1.0 | champion | C2-SS | 4 | 1 | — | — | -531.32 |
| sc-1.0 | champion | C2-IB | 4 | 1 | — | — | -646.15 |
| sc-1.0 | exploration | C1-SS | 81 | 1 | — | — | -70,974.83 |
| sc-1.0 | exploration | C1-IB | 81 | 1 | — | — | -75,280.86 |

Progress to the read: graded entry-weeks 1 of 40 (C1-SS), 1 of 40 (C1-IB), 1 of 40 (C2-SS), 1 of 40 (C2-IB)

S-C ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0.


## Watch basket (wb-1.0, exploration, paper only)
Universe: 2066 names.
Borrow snapshot: 2026-11-02 (the session's own); fee known for 2059 names.
Bull counts: 0:617, 1:763, 2:444, 3:197, 4:45, 5:0, 6:0, 7:0, 8:0
Bear counts: 0:751, 1:775, 2:351, 3:147, 4:38, 5:4, 6:0, 7:0, 8:0

### LONG (131)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ABM | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| ADC | 3 | 0 | no |  | x |  | x | x |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| ADI | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| ADUS | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  | x |
| ALRM | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| ALSN | 3 | 0 | yes |  | x |  | x |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMTB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| AMX | 3 | 0 | no |  | x |  |  | x | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| ANAB | 3 | 0 | yes |  | x |  | x |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| APG | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| AXS | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AZO | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BALL | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BFST | 4 | 0 | no | x | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| BJ | 4 | 0 | yes | x | x |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| BOOT | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BRKB | 4 | 0 | no | x | x |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  | x | x |
| CAH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CCK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CHT | 4 | 0 | no | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| CL | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CNO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| COLM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| CON | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| COST | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| CPK | 3 | 0 | yes | x |  |  |  |  | x | x |  |  | ? | ? |  |  |  |  |  |  |  |  |  |
| CSL | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| CSX | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CUBE | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| DCOM | 3 | 0 | no | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DG | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DGX | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| DRH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| ECL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EGBN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| EHC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ENR | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| EPAC | 3 | 0 | yes | x |  |  |  | x | x | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| EPRT | 3 | 0 | no |  | x |  | x |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EXLS | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| FIZZ | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| FLYW | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| FMBH | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| FTS | 4 | 0 | no | x | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  | x |
| FUL | 4 | 0 | no |  | x |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| FWONA | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  | ? | ? |  |  |  |  |  |  |  |  |  |
| FWONK | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| GIB | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| GM | 3 | 0 | yes | x | x |  |  | x |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| GWW | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| HBNC | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| HCSG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HD | 3 | 0 | yes |  | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x | x |
| HLT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HMC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| HZO | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? | ? |  |  |  |  |  |  |  |  |  |
| ICE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| IOSP | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| LFST | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| LIN | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| LIND | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| MA | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| MAS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MCBS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| MCK | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MD | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| MDLZ | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MGRC | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| MORN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| MRSH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MSCI | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| MSI | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| NDAQ | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| NGG | 4 | 0 | no |  | x |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| NUE | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| NWE | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| OPLN | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  |
| PAY | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| PBLS | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PGNY | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| PGR | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PLMR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| POR | 3 | 0 | yes |  |  | x |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PPG | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PRGS | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PRSU | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PUK | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PWP | 3 | 0 | yes |  | x | x | x |  |  | ? |  |  | ? |  |  |  |  | ? |  |  |  |  | x |
| R | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| REYN | 4 | 0 | no |  |  |  |  | x | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| RGA | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RLJ | 4 | 0 | no | x | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| RS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| RSG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SAIC | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| SBH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| SBSI | 4 | 0 | yes | x | x |  |  | x | x | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| SJM | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SMA | 4 | 0 | no | x | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| SO | 3 | 0 | no |  | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| SONY | 3 | 0 | yes |  | x |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| SPNT | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| SUNB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| TAK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| TDS | 4 | 0 | yes |  | x |  | x | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TGT | 3 | 0 | yes | x | x |  | x |  |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| THG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TILE | 4 | 0 | no | x | x |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| TOL | 3 | 0 | no |  | x |  |  | x | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| TRMB | 3 | 0 | yes |  | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| TW | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TXN | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| ULS | 3 | 0 | yes |  | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  |  |
| URI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| UTHR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| UTL | 3 | 0 | yes | x |  |  |  |  | x | x |  |  | ? | ? |  |  |  |  |  |  |  |  |  |
| UVE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| V | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| VLTO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VRTX | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VTRS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| WABC | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| WCN | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WDFC | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| WLK | 3 | 0 | yes |  | x |  | x |  |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| WMT | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| WOR | 4 | 0 | no | x | x |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| WTRG | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| XHR | 3 | 0 | yes | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |

### SHORT (80)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAMI | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| ABCL | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| ALNY | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  | ? | x |  | x |  | x |
| AVAV | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| AXSM | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  |  | x |  | x |  | x |
| BAND | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| BMNR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| BRKR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| BTU | 0 | 4 | yes |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  | x |  |  |  |  |
| CAMT | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  |  |  |  |  |  |
| CAT | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  | x | x | x |
| CC | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  |  |  |  |  |  | x |
| CDE | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  | x |
| CLMT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? | x | x |  |  | ? | x |  |  |  |  |
| CLS | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| COIN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  | x | x |
| CRCL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| CSCO | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| DUOL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| ENPH | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? |  |  |  |  | x |
| FIG | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| FLUT | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| FNV | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| FSLY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| GOOG | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  | x | x |
| GOOGL | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  | x | x |
| GPC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| GRAL | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| HIMS | 0 | 5 | no |  |  |  |  |  |  | ? |  |  | x | x | x | x |  | ? | x |  |  |  | x |
| IDCC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? |  |  |  |  |  |
| INOD | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| INTC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| KTOS | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| LEU | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  | x |  |  |
| LI | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? | x |  |  |  |  |
| LITE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  | x | x |
| LMND | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| LOGI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? |  |  |  |  | x |
| LQDA | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  |  |  | x |
| META | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| MGY | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| MLYS | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  |  |  | x |  |  |
| MMSI | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? |  |  |  |  | x |
| MP | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  |  |  |  |  |  | x |
| MSTR | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| MTZ | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  |  |  |  |  |  | x |
| MYE | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | ? |  |  | x | x | ? | x |  |  |  |  |
| NEO | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| NOW | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| OKE | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| ON | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| ORCL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| PBI | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x | ? | x |  |  |  |  |
| PTCT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| RARE | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| RDDT | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? |  |  |  | x | x |
| RSI | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  | x |  | x |
| RVMD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| SEDG | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  | x | x |  |  |  | x |
| SIMO | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| SKYW | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| SLM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  |  |
| SNDX | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| SNN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| SPCX | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| STRA | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| STRL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| TMDX | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| TPL | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| VALE | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  | x |  | x |
| VMI | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  |
| WEX | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| WIX | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| WLDN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| WOLF | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  |  |
| WRBY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| WSC | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x | x | x |  |  |  |  |  |  |  | x |
| XP | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| ZD | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| ZWS | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  |  |  | x | x | ? |  |  |  |  | x |

### VOL (0)
_none_

CONFLICT (logged only, never a basket, DESIGN/110 §3): 99.

Ledger: emitted 211 (skipped 0), graded 562; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
