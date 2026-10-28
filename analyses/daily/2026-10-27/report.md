# S-A daily — 2026-10-27 (S3)

Preflight: WARN — prices.parquet ends 2026-10-23, BEFORE the 2026-10-27 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-10-23, BEFORE the 2026-10-27 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-10-23, BEFORE the 2026-10-27 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (8)
| ticker | variant | structure | expiry | k | k_up | k_dn | credit_entry | credit_net_pct | risk_usd | contracts | entry_tier_max | cap_pass |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CAKE | A1 | IC | 2026-11-20T00:00:00.000 | 110.00 | 130.00 | 85.00 | 11.16 | +9.72% | 1,384.19 | 1 | 1 | yes |
| EQT | A1 | IC | 2026-10-30T00:00:00.000 | 56.00 | 64.00 | 49.00 | 2.24 | +3.68% | 576.19 | 1 | 1 | no |
| CAKE | A1 | SS | 2026-11-20T00:00:00.000 | 110.00 | — | — | 12.55 | +11.13% | 2,158.84 | 1 | 1 | yes |
| EQT | A1 | SS | 2026-10-30T00:00:00.000 | 56.00 | — | — | 2.37 | +4.01% | 895.73 | 1 | 1 | yes |
| CAKE | A2 | IC | 2026-11-20T00:00:00.000 | 110.00 | 130.00 | 85.00 | 11.16 | +9.72% | 1,384.19 | 1 | 1 | yes |
| EQT | A2 | IC | 2026-10-30T00:00:00.000 | 56.00 | 64.00 | 49.00 | 2.24 | +3.68% | 576.19 | 1 | 1 | no |
| CAKE | A2 | SS | 2026-11-20T00:00:00.000 | 110.00 | — | — | 12.55 | +11.13% | 2,158.84 | 1 | 1 | yes |
| EQT | A2 | SS | 2026-10-30T00:00:00.000 | 56.00 | — | — | 2.37 | +4.01% | 895.73 | 1 | 1 | yes |

## Suppressed (314)
| ticker | variant | first_fail |
|---|---|---|
| AAT | A1 | F3 |
| AAT | A2 | F3 |
| ACGL | A1 | F5 |
| ACGL | A2 | F5 |
| ADP | A1 | F3 |
| ADP | A2 | F3 |
| AEP | A1 | F3 |
| AEP | A2 | F3 |
| AER | A1 | F5 |
| AER | A2 | F5 |
| AMRN | A1 | F3 |
| AMRN | A2 | F3 |
| AON | A1 | F3 |
| AON | A2 | F3 |
| APAM | A1 | F4 |
| APAM | A2 | F4 |
| APH | A1 | F3 |
| APH | A2 | F3 |
| AVTR | A1 | F5 |
| AVTR | A2 | F5 |
| AXGN | A1 | F5 |
| AXGN | A2 | F5 |
| BANC | A1 | F4 |
| BANC | A2 | F4 |
| BBNX | A1 | F3 |
| BBNX | A2 | F3 |
| BIIB | A1 | F6 |
| BIIB | A2 | F6 |
| BKR | A1 | F3 |
| BKR | A2 | F3 |
| BLCO | A1 | F4 |
| BLCO | A2 | F4 |
| BLKB | A1 | F4 |
| BLKB | A2 | F4 |
| BOOM | A1 | F2 |
| BOOM | A2 | F2 |
| BSX | A1 | F3 |
| BSX | A2 | F3 |
| BUSE | A1 | F4 |
| BUSE | A2 | F4 |
| BXP | A1 | F5 |
| BXP | A2 | F5 |
| CHE | A1 | F5 |
| CHE | A2 | F5 |
| CHEF | A1 | F5 |
| CHEF | A2 | F5 |
| CHRW | A1 | F5 |
| CHRW | A2 | F5 |
| CLH | A1 | F5 |
| CLH | A2 | F5 |
| CMRE | A1 | F3 |
| CMRE | A2 | F3 |
| CPF | A1 | F3 |
| CPF | A2 | F3 |
| CR | A1 | F5 |
| CR | A2 | F5 |
| CSGP | A1 | F5 |
| CSGP | A2 | F5 |
| CSTM | A1 | F4 |
| CSTM | A2 | F4 |
| CTO | A1 | F3 |
| CTO | A2 | F3 |
| CZR | A1 | F5 |
| CZR | A2 | F5 |
| DAN | A1 | F4 |
| DAN | A2 | F4 |
| DBD | A1 | F4 |
| DBD | A2 | F4 |
| DINO | A1 | F5 |
| DINO | A2 | F5 |
| DMC | A1 | F3 |
| DMC | A2 | F3 |
| EAT | A1 | F5 |
| EAT | A2 | F5 |
| EDU | A1 | F4 |
| EDU | A2 | F4 |
| ENPH | A1 | F7 |
| ENPH | A2 | F7 |
| ENSG | A1 | F5 |
| ENSG | A2 | F5 |
| ESS | A1 | F5 |
| ESS | A2 | F5 |
| ETSY | A1 | F6 |
| ETSY | A2 | F6 |
| EVR | A1 | F5 |
| EVR | A2 | F5 |
| EXE | A1 | F6 |
| EXE | A2 | F6 |
| EXLS | A1 | F5 |
| EXLS | A2 | F5 |
| EXR | A1 | F5 |
| EXR | A2 | F5 |
| EXTR | A1 | F4 |
| EXTR | A2 | F4 |
| FCF | A1 | F4 |
| FCF | A2 | F4 |
| FE | A1 | F6 |
| FE | A2 | F6 |
| FELE | A1 | F4 |
| FELE | A2 | F4 |
| FFBC | A1 | F4 |
| FFBC | A2 | F4 |
| FFIV | A1 | F5 |
| FFIV | A2 | F5 |
| FLEX | A1 | F7 |
| FLEX | A2 | F7 |
| FMX | A1 | F5 |
| FMX | A2 | F5 |
| FTV | A1 | F5 |
| FTV | A2 | F5 |
| GEHC | A1 | F6 |
| GEHC | A2 | F6 |
| GEV | A1 | F3 |
| GEV | A2 | F3 |
| GNRC | A1 | F6 |
| GNRC | A2 | F6 |
| GPI | A1 | F5 |
| GPI | A2 | F5 |
| GRMN | A1 | F3 |
| GRMN | A2 | F3 |
| GSK | A1 | F3 |
| GSK | A2 | F3 |
| HAFC | A1 | F3 |
| HAFC | A2 | F3 |
| HAYW | A1 | F4 |
| HAYW | A2 | F4 |
| HIW | A1 | F4 |
| HIW | A2 | F4 |
| HOOD | A1 | F3 |
| HOOD | A2 | F3 |
| HOPE | A1 | F3 |
| HOPE | A2 | F3 |
| ICLR | A1 | F5 |
| ICLR | A2 | F5 |
| IEX | A1 | F5 |
| IEX | A2 | F5 |
| INTA | A1 | F4 |
| INTA | A2 | F4 |
| IP | A1 | F6 |
| IP | A2 | F6 |
| IVT | A1 | F4 |
| IVT | A2 | F4 |
| JLL | A1 | F5 |
| JLL | A2 | F5 |
| JMKE | A1 | F5 |
| JMKE | A2 | F5 |
| JMSB | A1 | F3 |
| JMSB | A2 | F3 |
| KEX | A1 | F5 |
| KEX | A2 | F5 |
| KIDS | A1 | F3 |
| KIDS | A2 | F3 |
| LFUS | A1 | F5 |
| LFUS | A2 | F5 |
| LH | A1 | F5 |
| LH | A2 | F5 |
| LII | A1 | F5 |
| LII | A2 | F5 |
| LOGI | A1 | F5 |
| LOGI | A2 | F5 |
| LPLA | A1 | F5 |
| LPLA | A2 | F5 |
| LSTR | A1 | F5 |
| LSTR | A2 | F5 |
| LU | A1 | F2 |
| LU | A2 | F2 |
| MANH | A1 | F5 |
| MANH | A2 | F5 |
| MAS | A1 | F5 |
| MAS | A2 | F5 |
| MCRI | A1 | F4 |
| MCRI | A2 | F4 |
| MGPI | A1 | F3 |
| MGPI | A2 | F3 |
| MIR | A1 | F5 |
| MIR | A2 | F5 |
| MTLS | A1 | F2 |
| MTLS | A2 | F2 |
| NBHC | A1 | F3 |
| NBHC | A2 | F3 |
| NBR | A1 | F3 |
| NBR | A2 | F3 |
| NBTB | A1 | F4 |
| NBTB | A2 | F4 |
| NI | A1 | F5 |
| NI | A2 | F5 |
| NMR | A1 | F2 |
| NMR | A2 | F2 |
| NOV | A1 | F5 |
| NOV | A2 | F5 |
| NTB | A1 | F4 |
| NTB | A2 | F4 |
| NXPI | A1 | F3 |
| NXPI | A2 | F3 |
| OCFC | A1 | F3 |
| OCFC | A2 | F3 |
| ODFL | A1 | F5 |
| ODFL | A2 | F5 |
| OGE | A1 | F5 |
| OGE | A2 | F5 |
| OI | A1 | F2 |
| OI | A2 | F2 |
| OKE | A1 | F3 |
| OKE | A2 | F3 |
| OPFI | A1 | F2 |
| OPFI | A2 | F2 |
| ORN | A1 | F2 |
| ORN | A2 | F2 |
| OSS | A1 | F2 |
| OSS | A2 | F2 |
| OSW | A1 | F4 |
| OSW | A2 | F4 |
| OTIS | A1 | F6 |
| OTIS | A2 | F6 |
| OTLY | A1 | F3 |
| OTLY | A2 | F3 |
| PAG | A1 | F5 |
| PAG | A2 | F5 |
| PB | A1 | F5 |
| PB | A2 | F5 |
| PDS | A1 | F3 |
| PDS | A2 | F3 |
| PGC | A1 | F3 |
| PGC | A2 | F3 |
| PPG | A1 | F6 |
| PPG | A2 | F6 |
| PRG | A1 | F3 |
| PRG | A2 | F3 |
| PSN | A1 | F5 |
| PSN | A2 | F5 |
| PSX | A1 | F3 |
| PSX | A2 | F3 |
| PUMP | A1 | F2 |
| PUMP | A2 | F2 |
| RDWR | A1 | F3 |
| RDWR | A2 | F3 |
| REPL | A1 | F3 |
| REPL | A2 | F3 |
| RNR | A1 | F5 |
| RNR | A2 | F5 |
| RNST | A1 | F4 |
| RNST | A2 | F4 |
| ROG | A1 | F4 |
| ROG | A2 | F4 |
| RRC | A1 | F5 |
| RRC | A2 | F5 |
| RUSHA | A1 | F4 |
| RUSHA | A2 | F4 |
| SAN | A1 | F3 |
| SAN | A2 | F3 |
| SBCF | A1 | F4 |
| SBCF | A2 | F4 |
| SCL | A1 | F3 |
| SCL | A2 | F3 |
| SEVN | A1 | F2 |
| SEVN | A2 | F2 |
| SHEN | A1 | F3 |
| SHEN | A2 | F3 |
| SIFY | A1 | F3 |
| SIFY | A2 | F3 |
| SITE | A1 | F5 |
| SITE | A2 | F5 |
| SLDE | A1 | F4 |
| SLDE | A2 | F4 |
| ST | A1 | F5 |
| ST | A2 | F5 |
| STAG | A1 | F5 |
| STAG | A2 | F5 |
| STNG | A1 | F5 |
| STNG | A2 | F5 |
| STX | A1 | F3 |
| STX | A2 | F3 |
| SW | A1 | F5 |
| SW | A2 | F5 |
| TEL | A1 | F3 |
| TEL | A2 | F3 |
| TER | A1 | F3 |
| TER | A2 | F3 |
| TEX | A1 | F5 |
| TEX | A2 | F5 |
| TRMK | A1 | F4 |
| TRMK | A2 | F4 |
| UBS | A1 | F3 |
| UBS | A2 | F3 |
| UCTT | A1 | F5 |
| UCTT | A2 | F5 |
| UE | A1 | F4 |
| UE | A2 | F4 |
| UHS | A1 | F5 |
| UHS | A2 | F5 |
| ULCC | A1 | F2 |
| ULCC | A2 | F2 |
| UMBF | A1 | F5 |
| UMBF | A2 | F5 |
| UMC | A1 | F6 |
| UMC | A2 | F6 |
| V | A1 | F3 |
| V | A2 | F3 |
| VFC | A1 | F6 |
| VFC | A2 | F6 |
| VRT | A1 | F3 |
| VRT | A2 | F3 |
| VTR | A1 | F5 |
| VTR | A2 | F5 |
| WERN | A1 | F3 |
| WERN | A2 | F3 |
| WING | A1 | F5 |
| WING | A2 | F5 |
| WM | A1 | F3 |
| WM | A2 | F3 |
| WPC | A1 | F5 |
| WPC | A2 | F5 |
| ZWS | A1 | F4 |
| ZWS | A2 | F4 |

## Exploration book tonight (35; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| AON | SS | 2026-11-20T00:00:00.000 | 310.00 | 22.87 | +7.25% | 3,343.36 | F3 |
| BIIB | SS | 2026-10-30T00:00:00.000 | 252.50 | 14.87 | +5.21% | 4,955.76 | F6 |
| BIIB | IC | 2026-10-30T00:00:00.000 | 252.50 | 14.47 | +4.96% | 2,803.44 | F6 |
| BSX | SS | 2026-10-30T00:00:00.000 | 45.00 | 3.74 | +7.98% | 948.43 | F3 |
| BSX | IC | 2026-10-30T00:00:00.000 | 45.00 | 3.60 | +7.47% | 540.35 | F3 |
| CAKE | SS | 2026-11-20T00:00:00.000 | 110.00 | 12.55 | +11.13% | 2,158.84 | PASS |
| CAKE | IC | 2026-11-20T00:00:00.000 | 110.00 | 11.16 | +9.72% | 1,384.19 | PASS |
| ENPH | SS | 2026-10-30T00:00:00.000 | 29.50 | 3.52 | +11.43% | 1,012.09 | F7 |
| EQT | SS | 2026-10-30T00:00:00.000 | 56.00 | 2.37 | +4.01% | 895.73 | PASS |
| EQT | IC | 2026-10-30T00:00:00.000 | 56.00 | 2.24 | +3.68% | 576.19 | PASS |
| ETSY | SS | 2026-10-30T00:00:00.000 | 87.00 | 8.15 | +8.72% | 2,154.05 | F6 |
| ETSY | IC | 2026-10-30T00:00:00.000 | 87.00 | 7.86 | +8.18% | 1,213.93 | F6 |
| EXE | SS | 2026-10-30T00:00:00.000 | 94.00 | 3.96 | +3.90% | 1,620.21 | F6 |
| FE | SS | 2026-11-20T00:00:00.000 | 46.00 | 1.89 | +3.54% | 325.13 | F6 |
| FE | IC | 2026-11-20T00:00:00.000 | 46.00 | 1.55 | +2.65% | 245.46 | F6 |
| FLEX | SS | 2026-11-20T00:00:00.000 | 85.00 | 14.92 | +17.18% | 2,474.80 | F7 |
| FLEX | IC | 2026-11-20T00:00:00.000 | 85.00 | 13.57 | +15.20% | 1,643.31 | F7 |
| GEHC | SS | 2026-10-30T00:00:00.000 | 71.00 | 4.52 | +5.95% | 1,273.91 | F6 |
| GNRC | SS | 2026-10-30T00:00:00.000 | 195.00 | 16.50 | +8.12% | 5,157.52 | F6 |
| GRMN | SS | 2026-11-20T00:00:00.000 | 290.00 | 28.85 | +9.53% | 4,929.09 | F3 |
| HOOD | SS | 2026-10-30T00:00:00.000 | 95.00 | 8.61 | +9.01% | 2,771.29 | F3 |
| HOOD | IC | 2026-10-30T00:00:00.000 | 95.00 | 8.40 | +8.77% | 1,659.81 | F3 |
| IP | SS | 2026-10-30T00:00:00.000 | 33.00 | 2.10 | +5.48% | 591.03 | F6 |
| NXPI | SS | 2026-11-20T00:00:00.000 | 250.00 | 31.48 | +12.06% | 5,534.74 | F3 |
| NXPI | IC | 2026-11-20T00:00:00.000 | 250.00 | 28.77 | +10.86% | 3,122.70 | F3 |
| OKE | SS | 2026-11-20T00:00:00.000 | 95.00 | 6.15 | +6.15% | 1,082.54 | F3 |
| OTIS | SS | 2026-11-20T00:00:00.000 | 75.00 | 4.74 | +5.93% | 595.28 | F6 |
| PPG | SS | 2026-10-30T00:00:00.000 | 113.00 | 4.37 | +3.47% | 1,469.37 | F6 |
| REPL | SS | 2026-10-30T00:00:00.000 | 13.00 | 1.45 | +10.08% | 673.21 | F3 |
| TEL | SS | 2026-11-20T00:00:00.000 | 230.00 | 21.49 | +9.31% | 3,601.20 | F3 |
| TER | SS | 2026-10-30T00:00:00.000 | 325.00 | 34.09 | +9.81% | 10,333.91 | F3 |
| UMC | SS | 2026-11-20T00:00:00.000 | 19.00 | 2.41 | +11.58% | 388.52 | F6 |
| VFC | SS | 2026-10-30T00:00:00.000 | 17.00 | 1.71 | +9.48% | 359.26 | F6 |
| VRT | SS | 2026-10-30T00:00:00.000 | 210.00 | 21.55 | +10.16% | 5,737.49 | F3 |
| VRT | IC | 2026-10-30T00:00:00.000 | 210.00 | 21.13 | +9.92% | 3,386.77 | F3 |

## Graded today (35)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| SOFI | A1 | IC | champion | -3.04% | -87.76 | 1 | no |
| PYPL | A1 | IC | champion | +3.07% | 168.45 | 1 | no |
| CNC | A1 | IC | champion | -0.55% | -37.27 | 1 | no |
| SOFI | A1 | SS | champion | -2.63% | -75.81 | 1 | no |
| PYPL | A1 | SS | champion | +3.48% | 191.36 | 1 | no |
| CNC | A1 | SS | champion | -0.22% | -14.79 | 1 | no |
| SOFI | A2 | IC | champion | -3.04% | -87.76 | 1 | no |
| PYPL | A2 | IC | champion | +3.07% | 168.45 | 1 | no |
| CNC | A2 | IC | champion | -0.55% | -37.27 | 1 | no |
| SOFI | A2 | SS | champion | -2.63% | -75.81 | 1 | no |
| PYPL | A2 | SS | champion | +3.48% | 191.36 | 1 | no |
| CNC | A2 | SS | champion | -0.22% | -14.79 | 1 | no |
| AMKR | A1 | SS | exploration | +3.74% | 137.55 | 1 | no |
| AMT | A1 | SS | exploration | -0.91% | -170.77 | 2 | no |
| BRO | A1 | SS | exploration | -0.83% | -59.22 | 1 | no |
| BRO | A1 | IC | exploration | -1.60% | -114.01 | 1 | no |
| CDNS | A1 | SS | exploration | +0.99% | 318.49 | 1 | no |
| CLS | A1 | SS | exploration | -4.04% | -995.22 | 1 | no |
| CNC | A1 | SS | exploration | -0.22% | -14.79 | 1 | no |
| CNC | A1 | IC | exploration | -0.55% | -37.27 | 1 | no |
| FCX | A1 | SS | exploration | -0.03% | -1.88 | 1 | no |
| GLXY | A1 | SS | exploration | +0.62% | 9.72 | 1 | no |
| HLT | A1 | SS | exploration | -0.39% | -137.30 | 1 | no |
| IVZ | A1 | SS | exploration | -6.33% | -180.43 | 1 | no |
| NUE | A1 | SS | exploration | -1.08% | -278.69 | 1 | no |
| PCAR | A1 | SS | exploration | -1.74% | -181.54 | 2 | no |
| PYPL | A1 | SS | exploration | +3.48% | 191.36 | 1 | no |
| PYPL | A1 | IC | exploration | +3.07% | 168.45 | 1 | no |
| RCL | A1 | SS | exploration | -2.48% | -696.20 | 1 | no |
| RMBS | A1 | SS | exploration | +0.94% | 84.98 | 1 | no |
| SOFI | A1 | SS | exploration | -2.63% | -37.91 | 1 | no |
| SOFI | A1 | IC | exploration | -3.04% | -43.88 | 1 | no |
| UPS | A1 | SS | exploration | +1.88% | 187.73 | 1 | no |
| UPS | A1 | IC | exploration | +1.58% | 158.66 | 1 | no |
| XYL | A1 | SS | exploration | -5.56% | -602.63 | 2 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 5 | 3 | +0.97% | 0.91 | 276.18 |
| sa-1.0 | champion | A1 | SS | 12 | 7 | +0.45% | 0.65 | 418.67 |
| sa-1.0 | champion | A2 | IC | 5 | 3 | +0.97% | 0.91 | 276.18 |
| sa-1.0 | champion | A2 | SS | 12 | 7 | +0.45% | 0.65 | 418.67 |
| sa-1.0 | exploration | A1 | IC | 20 | 13 | -0.70% | -1.41 | -1,637.15 |
| sa-1.0 | exploration | A1 | SS | 71 | 15 | -0.52% | -2.98 | -3,762.28 |

Ledger: emitted 8 (skipped 0), exploration 35 (skipped 0), graded 35; ledger open.

## S-B state
Gate (2026-10-27, from 2026-10-26 closes): SPY ON (VIX 18.39, VIX3M 19.94, X 18.39 vs median 16.205) · QQQ ON (VIX 18.39, VIX3M 19.94, X 26.4 vs median 22.295)

Next session (2026-10-28, from 2026-10-27 closes): SPY UNKNOWN:null input at 2026-10-27 · QQQ UNKNOWN:null input at 2026-10-27

CBOE refresh: ok through 2026-10-27; index-vol through 2026-10-27

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
Universe: 1989 names.
Borrow snapshot: 2026-10-27 (the session's own); fee known for 1981 names.
Bull counts: 0:731, 1:722, 2:382, 3:129, 4:21, 5:4, 6:0, 7:0, 8:0
Bear counts: 0:721, 1:745, 2:360, 3:126, 4:34, 5:3, 6:0, 7:0, 8:0

### LONG (86)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ABM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| ADI | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| AES | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| ALRM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| AM | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| AMG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| AMN | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| AMRX | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| AN | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| ANF | 3 | 0 | yes | x | x |  |  |  |  | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| BIIB | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| BY | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| CAE | 3 | 0 | yes |  | x |  |  | x | x | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| CEG | 3 | 0 | no |  | x | x | x |  |  | ? |  |  |  |  |  |  |  | ? |  |  |  | x | x |
| CHT | 4 | 0 | no | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| CNK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| CNOB | 3 | 0 | no | x |  |  | x |  | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| COKE | 3 | 0 | no | x | x |  |  |  | x |  |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| CSX | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CTRE | 3 | 0 | yes |  | x |  | x |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CUBI | 4 | 0 | no | x |  |  | x |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DCOM | 3 | 0 | no | x |  |  | x |  | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DHR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DNOW | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| DOV | 3 | 0 | yes |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DRH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| DV | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| EGBN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| EPRT | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EQH | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| FET | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| GILD | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HAFN | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HAL | 3 | 0 | yes |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| HASI | 3 | 0 | yes |  | x |  | x | x |  |  |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| HLI | 4 | 0 | no |  | x |  | x | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| HONA | 3 | 0 | no |  | x | ? |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  | x |  | x |
| HRI | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HST | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| INGM | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| JOE | 3 | 0 | no |  |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| JXN | 3 | 0 | yes | x |  |  | x |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| KFRC | 3 | 0 | no | x |  |  | x |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| LECO | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LION | 3 | 0 | no |  |  | x |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| LKFT | 4 | 0 | yes | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| LNG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LTH | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MAR | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| MCBS | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| NSSC | 3 | 0 | no |  | x |  | x |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| NTAP | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| NTNX | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| NWE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| NXPI | 4 | 0 | no |  |  | x |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PDS | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PLUS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PNFP | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PSN | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| PSO | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? | ? |  |  |  | ? |  |  |  |  |  |
| R | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RLJ | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| ROP | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| RS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SBH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| SHO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? | ? |  |  |  | ? |  |  |  |  |  |
| SN | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| SPNT | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| TALO | 3 | 0 | no | x |  |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| TEN | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| TFX | 3 | 0 | yes | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| TILE | 3 | 0 | no |  | x |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| TRGP | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TRMD | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| TRMK | 3 | 0 | no |  | x |  | x |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TTC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| TW | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| TXN | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| UNFI | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| URI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| UTHR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VLTO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VSTS | 5 | 0 | no | x | x |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| VTRS | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| W | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| ZWS | 3 | 0 | yes |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |

### SHORT (83)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AA | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| AAOI | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| ABVX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| AG | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  | x |
| AHR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| ASTS | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  | x | x |
| BA | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  | x | x | x |
| BHF | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  | x |  |  |
| BILI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  |  |
| CAR | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| CDE | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  | x |
| CECO | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  |  |  |  |
| CLMT | 0 | 4 | no |  |  |  |  |  |  |  |  |  | ? | x | x | x |  | ? | x |  |  |  | x |
| CLS | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| CMG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| COIN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  | x | x |
| CRCL | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  |  | x |
| CRWV | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| CSWC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| CVNA | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  |  | x |
| DKNG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  |  |  |  |  |  | x |
| ECHO | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| EEFT | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| ENPH | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| F | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| FICO | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| FN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| FOUR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| FSK | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x |  |  |  |  |  |  |
| GGG | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  | x |  | ? | x |  |  |  | x |
| GLW | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| GLXY | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  |  |  |  | x | x |
| GOOG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  | x | x |
| GOOGL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  | x | x |
| GPGI | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| HIMS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| HL | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  | x |
| HOOD | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  |  | x | x |
| HSY | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| HUT | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  | x |
| HYMC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  |  | x |  |  |  |  |
| INFY | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  | x |  | ? |  |  |  |  | x |
| IREN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  | x | x |
| ITT | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| KLAR | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| LMND | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  |  |
| LNN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| LUNR | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  | x |
| META | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| MGA | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| MRK | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x | x | ? |  |  |  |  | x |
| MTZ | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  | x |  | x |
| MUFG | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  |  |
| MWH | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| NVAX | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  |  |  |
| OMC | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| ORCL | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| ORI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| PINS | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| POWL | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  | ? | x |  |  | x | x |
| PPTA | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  |  |
| RCUS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| RDDT | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| RGEN | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| RIOT | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| SE | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| SEZL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| SFM | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| SKHY | 0 | 3 | no |  |  | ? |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  | x | x |
| SLM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  |  |
| SNN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| TMDX | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  |  |  |  |  |  | x |
| TSLX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| UNM | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| VALE | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| VC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  | x |
| VKTX | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| VSEC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| WELL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| WLDN | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| XP | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x | x |  | ? |  |  |  |  | x |
| XYZ | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  |  | x |

### VOL (0)
_none_

CONFLICT (logged only, never a basket, DESIGN/110 §3): 102.

Ledger: emitted 169 (skipped 0), graded 515; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
