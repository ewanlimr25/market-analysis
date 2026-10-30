# S-A daily — 2026-10-29 (S3)

Preflight: WARN — prices.parquet ends 2026-10-23, BEFORE the 2026-10-29 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-10-23, BEFORE the 2026-10-29 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-10-23, BEFORE the 2026-10-29 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (9)
| ticker | variant | structure | expiry | k | k_up | k_dn | credit_entry | credit_net_pct | risk_usd | contracts | entry_tier_max | cap_pass |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RIVN | A1 | IC | 2026-11-06T00:00:00.000 | 11.50 | 14.50 | 8.00 | 1.30 | +10.82% | 439.45 | 2 | 1 | yes |
| LYB | A1 | IC | 2026-11-20T00:00:00.000 | 65.00 | 75.00 | 55.00 | 4.93 | +6.92% | 507.42 | 1 | 1 | yes |
| RIVN | A1 | SS | 2026-11-06T00:00:00.000 | 11.50 | — | — | 1.42 | +12.04% | 694.45 | 2 | 1 | yes |
| COIN | A1 | SS | 2026-11-06T00:00:00.000 | 160.00 | — | — | 16.44 | +9.99% | 4,715.03 | 1 | 1 | no |
| LYB | A1 | SS | 2026-11-20T00:00:00.000 | 65.00 | — | — | 5.60 | +8.13% | 1,007.86 | 1 | 1 | yes |
| RIVN | A2 | IC | 2026-11-06T00:00:00.000 | 11.50 | 14.50 | 8.00 | 1.30 | +10.82% | 439.45 | 2 | 1 | yes |
| LYB | A2 | IC | 2026-11-20T00:00:00.000 | 65.00 | 75.00 | 55.00 | 4.93 | +6.92% | 507.42 | 1 | 1 | yes |
| RIVN | A2 | SS | 2026-11-06T00:00:00.000 | 11.50 | — | — | 1.42 | +12.04% | 694.45 | 2 | 1 | yes |
| LYB | A2 | SS | 2026-11-20T00:00:00.000 | 65.00 | — | — | 5.60 | +8.13% | 1,007.86 | 1 | 1 | yes |

## Suppressed (289)
| ticker | variant | first_fail |
|---|---|---|
| ABBV | A1 | F3 |
| ABBV | A2 | F3 |
| ACIC | A1 | F3 |
| ACIC | A2 | F3 |
| AJG | A1 | F3 |
| AJG | A2 | F3 |
| ALHC | A1 | F2 |
| ALHC | A2 | F2 |
| AMZN | A1 | F3 |
| AMZN | A2 | F3 |
| AN | A1 | F6 |
| AN | A2 | F6 |
| ASUR | A1 | F2 |
| ASUR | A2 | F2 |
| ATEC | A1 | F3 |
| ATEC | A2 | F3 |
| ATR | A1 | F5 |
| ATR | A2 | F5 |
| AX | A1 | F4 |
| AX | A2 | F4 |
| AXTI | A1 | F7 |
| AXTI | A2 | F7 |
| AZN | A1 | F3 |
| AZN | A2 | F3 |
| BBIO | A1 | F5 |
| BBIO | A2 | F5 |
| BCH | A1 | F4 |
| BCH | A2 | F4 |
| BFAM | A1 | F4 |
| BFAM | A2 | F4 |
| BP | A1 | F3 |
| BP | A2 | F3 |
| BSAC | A1 | F4 |
| BSAC | A2 | F4 |
| BTSG | A1 | F5 |
| BTSG | A2 | F5 |
| BVN | A1 | F4 |
| BVN | A2 | F4 |
| CBOE | A1 | F5 |
| CBOE | A2 | F5 |
| CCEC | A1 | F3 |
| CCEC | A2 | F3 |
| CCJ | A1 | F5 |
| CCJ | A2 | F5 |
| CDNA | A1 | F5 |
| CDNA | A2 | F5 |
| CDP | A1 | F4 |
| CDP | A2 | F4 |
| CGAU | A1 | F4 |
| CGAU | A2 | F4 |
| CHD | A1 | F5 |
| CHD | A2 | F5 |
| CL | A1 | F3 |
| CL | A2 | F3 |
| CNI | A1 | F3 |
| CNI | A2 | F3 |
| CNO | A1 | F5 |
| CNO | A2 | F5 |
| COIN | A2 | A2_sector |
| COLM | A1 | F4 |
| COLM | A2 | F4 |
| CPRI | A1 | F3 |
| CPRI | A2 | F3 |
| CRI | A1 | F3 |
| CRI | A2 | F3 |
| CUBE | A1 | F5 |
| CUBE | A2 | F5 |
| CUZ | A1 | F4 |
| CUZ | A2 | F4 |
| CVEO | A1 | F3 |
| CVEO | A2 | F3 |
| CVLG | A1 | F3 |
| CVLG | A2 | F3 |
| CVSA | A1 | F4 |
| CVSA | A2 | F4 |
| CVX | A1 | F3 |
| CVX | A2 | F3 |
| D | A1 | F3 |
| D | A2 | F3 |
| DLR | A1 | F3 |
| DLR | A2 | F3 |
| DVA | A1 | F5 |
| DVA | A2 | F5 |
| DXC | A1 | F5 |
| DXC | A2 | F5 |
| DXCM | A1 | F5 |
| DXCM | A2 | F5 |
| EIX | A1 | F5 |
| EIX | A2 | F5 |
| EMN | A1 | F5 |
| EMN | A2 | F5 |
| ERIE | A1 | F4 |
| ERIE | A2 | F4 |
| EXC | A1 | F5 |
| EXC | A2 | F5 |
| EXEL | A1 | F5 |
| EXEL | A2 | F5 |
| EXPO | A1 | F4 |
| EXPO | A2 | F4 |
| FBIZ | A1 | F3 |
| FBIZ | A2 | F3 |
| FDXF | A1 | F5 |
| FDXF | A2 | F5 |
| FET | A1 | F3 |
| FET | A2 | F3 |
| FHI | A1 | F4 |
| FHI | A2 | F4 |
| FISI | A1 | F3 |
| FISI | A2 | F3 |
| FND | A1 | F5 |
| FND | A2 | F5 |
| FORR | A1 | F3 |
| FORR | A2 | F3 |
| FRT | A1 | F5 |
| FRT | A2 | F5 |
| FSLR | A1 | F6 |
| FSLR | A2 | F6 |
| GD | A1 | F3 |
| GD | A2 | F3 |
| GDDY | A1 | F5 |
| GDDY | A2 | F5 |
| GDYN | A1 | F2 |
| GDYN | A2 | F2 |
| GILD | A1 | F3 |
| GILD | A2 | F3 |
| GLPI | A1 | F5 |
| GLPI | A2 | F5 |
| GTES | A1 | F4 |
| GTES | A2 | F4 |
| HG | A1 | F4 |
| HG | A2 | F4 |
| HR | A1 | F5 |
| HR | A2 | F5 |
| HTGC | A1 | F4 |
| HTGC | A2 | F4 |
| ILMN | A1 | F5 |
| ILMN | A2 | F5 |
| IMO | A1 | F3 |
| IMO | A2 | F3 |
| INBK | A1 | F3 |
| INBK | A2 | F3 |
| INGM | A1 | F4 |
| INGM | A2 | F4 |
| INTC | A1 | F3 |
| INTC | A2 | F3 |
| INVX | A1 | F4 |
| INVX | A2 | F4 |
| IR | A1 | F6 |
| IR | A2 | F6 |
| IRMD | A1 | F3 |
| IRMD | A2 | F3 |
| IVR | A1 | F2 |
| IVR | A2 | F2 |
| JKS | A1 | F2 |
| JKS | A2 | F2 |
| KRG | A1 | F5 |
| KRG | A2 | F5 |
| KVUE | A1 | F5 |
| KVUE | A2 | F5 |
| KWR | A1 | F4 |
| KWR | A2 | F4 |
| LEA | A1 | F5 |
| LEA | A2 | F5 |
| LNT | A1 | F5 |
| LNT | A2 | F5 |
| MDLZ | A1 | F3 |
| MDLZ | A2 | F3 |
| MEOH | A1 | F4 |
| MEOH | A2 | F4 |
| MFIN | A1 | F3 |
| MFIN | A2 | F3 |
| MGA | A1 | F5 |
| MGA | A2 | F5 |
| MHK | A1 | F5 |
| MHK | A2 | F5 |
| MIAX | A1 | F5 |
| MIAX | A2 | F5 |
| MMSI | A1 | F5 |
| MMSI | A2 | F5 |
| MPWR | A1 | F3 |
| MPWR | A2 | F3 |
| MSEX | A1 | F3 |
| MSEX | A2 | F3 |
| MSTR | A1 | F3 |
| MSTR | A2 | F3 |
| MTX | A1 | F3 |
| MTX | A2 | F3 |
| MTZ | A1 | F5 |
| MTZ | A2 | F5 |
| MVBF | A1 | F3 |
| MVBF | A2 | F3 |
| NEXA | A1 | F3 |
| NEXA | A2 | F3 |
| NPKI | A1 | F3 |
| NPKI | A2 | F3 |
| NVT | A1 | F5 |
| NVT | A2 | F5 |
| NWG | A1 | F3 |
| NWG | A2 | F3 |
| NWL | A1 | F2 |
| NWL | A2 | F2 |
| OABI | A1 | F2 |
| OABI | A2 | F2 |
| OIS | A1 | F2 |
| OIS | A2 | F2 |
| OLN | A1 | F3 |
| OLN | A2 | F3 |
| OMF | A1 | F5 |
| OMF | A2 | F5 |
| OSIS | A1 | F4 |
| OSIS | A2 | F4 |
| OSPN | A1 | F3 |
| OSPN | A2 | F3 |
| PEB | A1 | F5 |
| PEB | A2 | F5 |
| PFSI | A1 | F4 |
| PFSI | A2 | F4 |
| PINS | A1 | F6 |
| PINS | A2 | F6 |
| PIPR | A1 | F5 |
| PIPR | A2 | F5 |
| PMT | A1 | F2 |
| PMT | A2 | F2 |
| PRTS | A1 | F2 |
| PRTS | A2 | F2 |
| PTCT | A1 | F5 |
| PTCT | A2 | F5 |
| RBC | A1 | F5 |
| RBC | A2 | F5 |
| RBLX | A1 | F6 |
| RBLX | A2 | F6 |
| RDDT | A1 | F7 |
| RDDT | A2 | F7 |
| REAL | A1 | F3 |
| REAL | A2 | F3 |
| REGN | A1 | F3 |
| REGN | A2 | F3 |
| RMD | A1 | F5 |
| RMD | A2 | F5 |
| RSG | A1 | F3 |
| RSG | A2 | F3 |
| RYAN | A1 | F5 |
| RYAN | A2 | F5 |
| SAMG | A1 | F3 |
| SAMG | A2 | F3 |
| SBUX | A1 | F3 |
| SBUX | A2 | F3 |
| SKYW | A1 | F4 |
| SKYW | A2 | F4 |
| SMP | A1 | F3 |
| SMP | A2 | F3 |
| SNDK | A1 | F3 |
| SNDK | A2 | F3 |
| SNDR | A1 | F4 |
| SNDR | A2 | F4 |
| SNY | A1 | F3 |
| SNY | A2 | F3 |
| SPSC | A1 | F4 |
| SPSC | A2 | F4 |
| SPXC | A1 | F5 |
| SPXC | A2 | F5 |
| STOK | A1 | F3 |
| STOK | A2 | F3 |
| STRZ | A1 | F3 |
| STRZ | A2 | F3 |
| SUPN | A1 | F4 |
| SUPN | A2 | F4 |
| SXT | A1 | F4 |
| SXT | A2 | F4 |
| SYK | A1 | F3 |
| SYK | A2 | F3 |
| TBBK | A1 | F4 |
| TBBK | A2 | F4 |
| TFII | A1 | F4 |
| TFII | A2 | F4 |
| TWLO | A1 | F5 |
| TWLO | A2 | F5 |
| VALE | A1 | F6 |
| VALE | A2 | F6 |
| VLTO | A1 | F5 |
| VLTO | A2 | F5 |
| WKC | A1 | F3 |
| WKC | A2 | F3 |
| WT | A1 | F4 |
| WT | A2 | F4 |
| WY | A1 | F6 |
| WY | A2 | F6 |
| XOM | A1 | F3 |
| XOM | A2 | F3 |

## Exploration book tonight (18; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| AN | SS | 2026-11-20T00:00:00.000 | 170.00 | 17.44 | +9.82% | 3,094.99 | F6 |
| AXTI | SS | 2026-11-06T00:00:00.000 | 60.00 | 10.51 | +16.49% | 2,859.64 | F7 |
| COIN | SS | 2026-11-06T00:00:00.000 | 160.00 | 16.44 | +9.99% | 4,715.03 | PASS |
| FSLR | SS | 2026-11-06T00:00:00.000 | 177.50 | 19.56 | +9.82% | 4,470.07 | F6 |
| IR | SS | 2026-11-20T00:00:00.000 | 80.00 | 6.35 | +7.33% | 1,141.26 | F6 |
| IR | IC | 2026-11-20T00:00:00.000 | 80.00 | 4.95 | +5.12% | 504.53 | F6 |
| LYB | SS | 2026-11-20T00:00:00.000 | 65.00 | 5.60 | +8.13% | 1,007.86 | PASS |
| LYB | IC | 2026-11-20T00:00:00.000 | 65.00 | 4.93 | +6.92% | 507.42 | PASS |
| MSTR | SS | 2026-11-06T00:00:00.000 | 142.00 | 13.19 | +9.12% | 4,374.68 | F3 |
| NWL | SS | 2026-11-20T00:00:00.000 | 5.00 | 0.85 | +14.00% | 160.19 | F2 |
| PINS | SS | 2026-11-06T00:00:00.000 | 20.00 | 2.92 | +13.43% | 551.00 | F6 |
| RBLX | SS | 2026-11-06T00:00:00.000 | 52.00 | 8.77 | +15.97% | 1,689.64 | F6 |
| RDDT | SS | 2026-11-06T00:00:00.000 | 130.00 | 19.72 | +14.57% | 4,216.73 | F7 |
| RIVN | SS | 2026-11-06T00:00:00.000 | 11.50 | 1.42 | +12.04% | 347.22 | PASS |
| RIVN | IC | 2026-11-06T00:00:00.000 | 11.50 | 1.30 | +10.82% | 219.72 | PASS |
| VALE | SS | 2026-11-06T00:00:00.000 | 11.00 | 0.62 | +5.10% | 192.95 | F6 |
| VALE | IC | 2026-11-06T00:00:00.000 | 11.00 | 0.59 | +4.71% | 141.39 | F6 |
| WY | SS | 2026-11-20T00:00:00.000 | 20.00 | 1.38 | +6.04% | 247.93 | F6 |

## Graded today (49)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| CROX | A1 | SS | champion | -10.36% | -1,237.81 | 1 | no |
| CMG | A1 | SS | champion | -0.48% | -13.80 | 1 | no |
| TROW | A1 | SS | champion | -0.41% | -43.09 | 2 | no |
| F | A1 | SS | champion | +2.20% | 105.59 | 1 | no |
| CROX | A2 | SS | champion | -10.36% | -1,237.81 | 1 | no |
| CMG | A2 | SS | champion | -0.48% | -13.80 | 1 | no |
| TROW | A2 | SS | champion | -0.41% | -43.09 | 2 | no |
| F | A2 | SS | champion | +2.20% | 105.59 | 1 | no |
| AEM | A1 | SS | exploration | -1.00% | -183.26 | 1 | no |
| AGI | A1 | SS | exploration | -3.75% | -118.80 | 1 | no |
| ALGM | A1 | SS | exploration | -0.32% | -11.40 | 2 | no |
| ALGN | A1 | SS | exploration | +2.04% | 312.33 | 1 | no |
| AR | A1 | SS | exploration | -0.26% | -10.79 | 1 | no |
| ARES | A1 | SS | exploration | -1.15% | -142.94 | 1 | no |
| AUR | A1 | SS | exploration | -1.62% | -8.22 | 1 | no |
| BAX | A1 | SS | exploration | -0.77% | -19.53 | 1 | no |
| BC | A1 | SS | exploration | -4.10% | -282.88 | 2 | no |
| CARR | A1 | SS | exploration | -1.22% | -68.66 | 2 | no |
| CMG | A1 | SS | exploration | -0.48% | -13.80 | 1 | no |
| CROX | A1 | SS | exploration | -10.36% | -1,237.81 | 1 | no |
| CVNA | A1 | SS | exploration | -2.66% | -157.01 | 1 | no |
| DHI | A1 | SS | exploration | +0.54% | 77.25 | 1 | no |
| EBAY | A1 | SS | exploration | +2.62% | 309.25 | 1 | no |
| F | A1 | SS | exploration | +2.20% | 26.40 | 1 | no |
| FTAI | A1 | SS | exploration | -5.40% | -904.03 | 2 | no |
| GFL | A1 | SS | exploration | -0.04% | -1.83 | 1 | no |
| HONA | A1 | SS | exploration | -4.03% | -713.69 | 2 | no |
| HONA | A1 | IC | exploration | -4.43% | -783.09 | 2 | no |
| HSY | A1 | SS | exploration | -0.69% | -113.80 | 1 | no |
| HWM | A1 | SS | exploration | +0.79% | 155.11 | 1 | no |
| ICE | A1 | SS | exploration | -3.93% | -612.42 | 1 | no |
| INSM | A1 | SS | exploration | -3.96% | -385.30 | 1 | no |
| KGC | A1 | SS | exploration | -1.19% | -27.39 | 1 | no |
| LHX | A1 | SS | exploration | -1.42% | -370.38 | 1 | no |
| LKQ | A1 | SS | exploration | -1.44% | -24.81 | 1 | no |
| LKQ | A1 | IC | exploration | -4.75% | -81.62 | 2 | no |
| MBLY | A1 | SS | exploration | +1.08% | 7.62 | 1 | no |
| MGM | A1 | SS | exploration | -1.56% | -42.59 | 1 | no |
| MGM | A1 | IC | exploration | -2.76% | -75.30 | 2 | no |
| NCLH | A1 | SS | exploration | -4.97% | -80.01 | 1 | no |
| OWL | A1 | SS | exploration | -1.80% | -17.56 | 1 | no |
| PGY | A1 | SS | exploration | +3.92% | 80.40 | 1 | no |
| PWR | A1 | SS | exploration | -0.40% | -243.99 | 1 | no |
| RSI | A1 | SS | exploration | -8.22% | -123.66 | 1 | no |
| SIRI | A1 | SS | exploration | -0.02% | -0.56 | 1 | no |
| STM | A1 | SS | exploration | +3.34% | 162.20 | 1 | no |
| TDOC | A1 | SS | exploration | -18.23% | -125.40 | 1 | no |
| TDOC | A1 | IC | exploration | -17.64% | -121.36 | 1 | no |
| TROW | A1 | SS | exploration | -0.41% | -43.09 | 2 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 6 | 4 | +0.80% | 0.99 | 268.43 |
| sa-1.0 | champion | A1 | SS | 18 | 9 | -0.14% | -0.21 | -652.77 |
| sa-1.0 | champion | A2 | IC | 6 | 4 | +0.80% | 0.99 | 268.43 |
| sa-1.0 | champion | A2 | SS | 18 | 9 | -0.14% | -0.21 | -652.77 |
| sa-1.0 | exploration | A1 | IC | 31 | 15 | -1.52% | -1.70 | -2,761.49 |
| sa-1.0 | exploration | A1 | SS | 131 | 17 | -0.83% | -2.44 | -7,336.09 |

Ledger: emitted 9 (skipped 0), exploration 18 (skipped 0), graded 49; ledger open.

## S-B state
Gate (2026-10-29, from 2026-10-28 closes): SPY ON (VIX 16.91, VIX3M 19.22, X 16.91 vs median 16.425) · QQQ ON (VIX 16.91, VIX3M 19.22, X 23.78 vs median 22.605)

Next session (2026-10-30, from 2026-10-29 closes): SPY UNKNOWN:null input at 2026-10-29 · QQQ UNKNOWN:null input at 2026-10-29

CBOE refresh: ok through 2026-10-29; index-vol through 2026-10-29

Entry day: no.

### S-B positions tonight (0)
_none_

### S-B graded at expiry today (0)
_none due_

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

S-B ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0; ledger open.


## S-C state
Entry day: no; ledger open.

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

S-C ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0.


## Watch basket (wb-1.0, exploration, paper only)
Universe: 2022 names.
Borrow snapshot: 2026-10-29 (the session's own); fee known for 2015 names.
Bull counts: 0:772, 1:688, 2:393, 3:141, 4:26, 5:2, 6:0, 7:0, 8:0
Bear counts: 0:855, 1:745, 2:276, 3:115, 4:29, 5:2, 6:0, 7:0, 8:0

### LONG (103)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ABBV | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| ABM | 4 | 0 | no | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| ADC | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| ADI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ADUS | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  | x |
| AFG | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| ALRM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| AMAL | 3 | 0 | no | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| AMG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMGN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| AMRX | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| ARLO | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| ARQT | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| BBY | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| BIIB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| BLK | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BOOT | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CBC | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| CBZ | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  |
| CHT | 4 | 0 | no | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| CNK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| CRBG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CSX | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CTS | 3 | 0 | yes |  | x |  |  | x | x | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| CUBI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| DHR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DOV | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DRH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| DV | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| EBAY | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ECL | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EGBN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| EQH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EXPO | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  | x |
| FTS | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  | x |
| GCT | 3 | 0 | no | x |  |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| GENB | 3 | 0 | no |  | x |  | x | x |  | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| HAL | 3 | 0 | no |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| HASI | 3 | 0 | no |  | x |  |  | x |  | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| HBNC | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| HGTY | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HLT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HRI | 3 | 0 | no | x |  |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HST | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| IOSP | 5 | 0 | no | x | x |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| JCI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| JOE | 4 | 0 | no | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| KNTK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| KVUE | 4 | 0 | no | x | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| KYN | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| LFST | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| LH | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| LION | 3 | 0 | no |  |  | x |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LNG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LUV | 3 | 0 | yes |  |  |  | x | x | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| MA | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| MAR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MAS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MCBS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| MD | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| MRSH | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| NDAQ | 4 | 0 | yes | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| NUE | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| NXPI | 4 | 0 | no |  |  | x |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| OPLN | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| OUT | 3 | 0 | yes | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  |  |
| PKG | 3 | 0 | yes | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| PLUS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PPG | 4 | 0 | no |  |  | x |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| R | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| RBRK | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| REYN | 3 | 0 | no |  |  |  |  | x |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| RLJ | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| ROP | 3 | 0 | no | x |  |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| SBH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| SDRL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| SIBN | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| SIGI | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| SSD | 4 | 0 | no |  |  | x |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  |  |
| SUNB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| TDY | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TEL | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TILE | 3 | 0 | no |  | x |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| TMO | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TRAX | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TRGP | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TTAM | 3 | 0 | yes |  | x | x |  | x |  | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| TTC | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TTE | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  |  |
| UCB | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| URI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| UTHR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| V | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VLTO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VOR | 3 | 0 | yes |  | x |  | x |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| VRSN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VSTS | 4 | 0 | no | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| W | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| WPP | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| WSM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WTRG | 4 | 0 | no | x | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |

### SHORT (66)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AA | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| ABVX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| ALG | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| ALNY | 0 | 4 | yes |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  | x | x |
| ASST | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| BNL | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  | x |
| CAR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| CAT | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| CC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? |  |  |  |  |  |
| CDE | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  | x |
| CLMT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? | x | x |  |  | ? | x |  |  |  | x |
| COIN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  | x | x |
| CRCL | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  |  | x |
| CRWV | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| DAVE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| DLO | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? |  |  |  |  |  |
| DMC | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| DUOL | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? | x |  |  |  |  |
| ENPH | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  |  | x |
| FFIV | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| FNV | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| FOUR | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| FTNT | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  | x | x |
| GLXY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  |  |  |  |  |  | x |
| GOOG | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| GOOGL | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| GPC | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| HGV | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| HL | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  | x |
| HSY | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| HUBB | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| HUT | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  | x |
| INFY | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  | x |  | ? |  |  |  |  | x |
| IREN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  | x | x |
| KHC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? |  |  |  |  | x |
| LPLA | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  | x |  | ? | x |  |  |  | x |
| LPX | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| LULU | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  |  |  |  |  |  | x |
| MDLN | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? |  |  |  |  | x |
| META | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| MGNI | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  |
| MKC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| MRVL | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| NFLX | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| NTES | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? |  |  |  |  | x |
| NU | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  | x |  | ? |  |  |  |  | x |
| NVAX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  |  |
| NVO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| PBI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| PDD | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| PINS | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| RDDT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| RIOT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  |  |  |  |  |  | x |
| SE | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| SEDG | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  |  |  |  |
| SFM | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? | x |  | x |  | x |
| SOLV | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| SPCX | 0 | 3 | no |  |  | ? |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  | x | x |
| STRA | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | ? |  |  | x | x | ? | x |  |  |  |  |
| TMDX | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  |  |
| UBER | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  | x | x |
| VALE | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  | x |  | x |
| VC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  | x |
| VZ | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| XP | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| XYZ | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  | x |  | ? | x |  |  |  | x |

### VOL (0)
_none_

CONFLICT (logged only, never a basket, DESIGN/110 §3): 74.

Ledger: emitted 169 (skipped 0), graded 529; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
