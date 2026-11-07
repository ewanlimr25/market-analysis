# S-A daily — 2026-11-05 (S3)

Preflight: WARN — prices.parquet ends 2026-10-30, BEFORE the 2026-11-05 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-10-30, BEFORE the 2026-11-05 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-10-30, BEFORE the 2026-11-05 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (4)
| ticker | variant | structure | expiry | k | k_up | k_dn | credit_entry | credit_net_pct | risk_usd | contracts | entry_tier_max | cap_pass |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DKNG | A1 | SS | 2026-11-13T00:00:00.000 | 24.00 | — | — | 2.65 | +10.89% | 645.00 | 1 | 1 | yes |
| VST | A1 | SS | 2026-11-13T00:00:00.000 | 115.00 | — | — | 10.88 | +9.28% | 2,801.39 | 1 | 1 | no |
| DKNG | A2 | SS | 2026-11-13T00:00:00.000 | 24.00 | — | — | 2.65 | +10.89% | 645.00 | 1 | 1 | yes |
| VST | A2 | SS | 2026-11-13T00:00:00.000 | 115.00 | — | — | 10.88 | +9.28% | 2,801.39 | 1 | 1 | no |

## Suppressed (402)
| ticker | variant | first_fail |
|---|---|---|
| AAOI | A1 | F5 |
| AAOI | A2 | F5 |
| ABNB | A1 | F3 |
| ABNB | A2 | F3 |
| ABX | A1 | F2 |
| ABX | A2 | F2 |
| AEE | A1 | F5 |
| AEE | A2 | F5 |
| AFRM | A1 | F5 |
| AFRM | A2 | F5 |
| AGM | A1 | F3 |
| AGM | A2 | F3 |
| AGO | A1 | F4 |
| AGO | A2 | F4 |
| AHR | A1 | F5 |
| AHR | A2 | F5 |
| AIP | A1 | F3 |
| AIP | A2 | F3 |
| AKAM | A1 | F5 |
| AKAM | A2 | F5 |
| ALRM | A1 | F4 |
| ALRM | A2 | F4 |
| AMN | A1 | F3 |
| AMN | A2 | F3 |
| AMR | A1 | F3 |
| AMR | A2 | F3 |
| ANIK | A1 | F3 |
| ANIK | A2 | F3 |
| AORT | A1 | F3 |
| AORT | A2 | F3 |
| AOSL | A1 | F3 |
| AOSL | A2 | F3 |
| APLE | A1 | F4 |
| APLE | A2 | F4 |
| ARCT | A1 | F2 |
| ARCT | A2 | F2 |
| ARLO | A1 | F3 |
| ARLO | A2 | F3 |
| ASTH | A1 | F4 |
| ASTH | A2 | F4 |
| ATEN | A1 | F3 |
| ATEN | A2 | F3 |
| ATMU | A1 | F4 |
| ATMU | A2 | F4 |
| AUGO | A1 | F5 |
| AUGO | A2 | F5 |
| AURA | A1 | F2 |
| AURA | A2 | F2 |
| AVPT | A1 | F5 |
| AVPT | A2 | F5 |
| AXON | A1 | F5 |
| AXON | A2 | F5 |
| BAM | A1 | F3 |
| BAM | A2 | F3 |
| BBDC | A1 | F2 |
| BBDC | A2 | F2 |
| BCIC | A1 | F2 |
| BCIC | A2 | F2 |
| BEN | A1 | F5 |
| BEN | A2 | F5 |
| BILL | A1 | F5 |
| BILL | A2 | F5 |
| BJRI | A1 | F3 |
| BJRI | A2 | F3 |
| BKD | A1 | F5 |
| BKD | A2 | F5 |
| BL | A1 | F3 |
| BL | A2 | F3 |
| BLMN | A1 | F3 |
| BLMN | A2 | F3 |
| CARG | A1 | F5 |
| CARG | A2 | F5 |
| CBL | A1 | F3 |
| CBL | A2 | F3 |
| CCSI | A1 | F3 |
| CCSI | A2 | F3 |
| CELC | A1 | F5 |
| CELC | A2 | F5 |
| CENX | A1 | F5 |
| CENX | A2 | F5 |
| CGBD | A1 | F3 |
| CGBD | A2 | F3 |
| CHTR | A1 | F5 |
| CHTR | A2 | F5 |
| CLMT | A1 | F6 |
| CLMT | A2 | F6 |
| COMP | A1 | F2 |
| COMP | A2 | F2 |
| CON | A1 | F5 |
| CON | A2 | F5 |
| CPK | A1 | F4 |
| CPK | A2 | F4 |
| CPT | A1 | F5 |
| CPT | A2 | F5 |
| CRSR | A1 | F3 |
| CRSR | A2 | F3 |
| CRVS | A1 | F2 |
| CRVS | A2 | F2 |
| CSTL | A1 | F3 |
| CSTL | A2 | F3 |
| CTRE | A1 | F5 |
| CTRE | A2 | F5 |
| CYRX | A1 | F3 |
| CYRX | A2 | F3 |
| DBX | A1 | F5 |
| DBX | A2 | F5 |
| DCBO | A1 | F3 |
| DCBO | A2 | F3 |
| DIOD | A1 | F4 |
| DIOD | A2 | F4 |
| DK | A1 | F6 |
| DK | A2 | F6 |
| DOCS | A1 | F6 |
| DOCS | A2 | F6 |
| DVN | A1 | F6 |
| DVN | A2 | F6 |
| ECHO | A1 | F5 |
| ECHO | A2 | F5 |
| ED | A1 | F5 |
| ED | A2 | F5 |
| EGAN | A1 | F2 |
| EGAN | A2 | F2 |
| EGY | A1 | F2 |
| EGY | A2 | F2 |
| ELAN | A1 | F5 |
| ELAN | A2 | F5 |
| EMA | A1 | F5 |
| EMA | A2 | F5 |
| ENB | A1 | F3 |
| ENB | A2 | F3 |
| EOG | A1 | F3 |
| EOG | A2 | F3 |
| ESNT | A1 | F5 |
| ESNT | A2 | F5 |
| EVC | A1 | F2 |
| EVC | A2 | F2 |
| EVCM | A1 | F2 |
| EVCM | A2 | F2 |
| FG | A1 | F4 |
| FG | A2 | F4 |
| FIGS | A1 | F5 |
| FIGS | A2 | F5 |
| FIVN | A1 | F5 |
| FIVN | A2 | F5 |
| FLGT | A1 | F3 |
| FLGT | A2 | F3 |
| FLR | A1 | F5 |
| FLR | A2 | F5 |
| FNF | A1 | F5 |
| FNF | A2 | F5 |
| FNKO | A1 | F2 |
| FNKO | A2 | F2 |
| FOXF | A1 | F3 |
| FOXF | A2 | F3 |
| FROG | A1 | F5 |
| FROG | A2 | F5 |
| G | A1 | F5 |
| G | A2 | F5 |
| GH | A1 | F7 |
| GH | A2 | F7 |
| GMED | A1 | F5 |
| GMED | A2 | F5 |
| GPRE | A1 | F3 |
| GPRE | A2 | F3 |
| GRDN | A1 | F3 |
| GRDN | A2 | F3 |
| GRND | A1 | F4 |
| GRND | A2 | F4 |
| GSBD | A1 | F2 |
| GSBD | A2 | F2 |
| GTE | A1 | F2 |
| GTE | A2 | F2 |
| HALO | A1 | F5 |
| HALO | A2 | F5 |
| HASI | A1 | F4 |
| HASI | A2 | F4 |
| HHH | A1 | F5 |
| HHH | A2 | F5 |
| HLIO | A1 | F3 |
| HLIO | A2 | F3 |
| HUM | A1 | F5 |
| HUM | A2 | F5 |
| HY | A1 | F3 |
| HY | A2 | F3 |
| IAG | A1 | F5 |
| IAG | A2 | F5 |
| IBEX | A1 | F3 |
| IBEX | A2 | F3 |
| ICFI | A1 | F3 |
| ICFI | A2 | F3 |
| ICUI | A1 | F4 |
| ICUI | A2 | F4 |
| INGN | A1 | F2 |
| INGN | A2 | F2 |
| INOD | A1 | F3 |
| INOD | A2 | F3 |
| INTT | A1 | F3 |
| INTT | A2 | F3 |
| IONQ | A1 | F7 |
| IONQ | A2 | F7 |
| IREN | A1 | F7 |
| IREN | A2 | F7 |
| IRTC | A1 | F5 |
| IRTC | A2 | F5 |
| JHX | A1 | F5 |
| JHX | A2 | F5 |
| JYNT | A1 | F2 |
| JYNT | A2 | F2 |
| KINS | A1 | F3 |
| KINS | A2 | F3 |
| KOP | A1 | F3 |
| KOP | A2 | F3 |
| KRMN | A1 | F5 |
| KRMN | A2 | F5 |
| KRO | A1 | F2 |
| KRO | A2 | F2 |
| KTOS | A1 | F5 |
| KTOS | A2 | F5 |
| KWY | A1 | F2 |
| KWY | A2 | F2 |
| KYIV | A1 | F4 |
| KYIV | A2 | F4 |
| LASR | A1 | F3 |
| LASR | A2 | F3 |
| LION | A1 | F4 |
| LION | A2 | F4 |
| LOCO | A1 | F3 |
| LOCO | A2 | F3 |
| LOMA | A1 | F2 |
| LOMA | A2 | F2 |
| LYFT | A1 | F5 |
| LYFT | A2 | F5 |
| LYV | A1 | F5 |
| LYV | A2 | F5 |
| MAIN | A1 | F4 |
| MAIN | A2 | F4 |
| MAT | A1 | F6 |
| MAT | A2 | F6 |
| MBC | A1 | F2 |
| MBC | A2 | F2 |
| MC | A1 | F5 |
| MC | A2 | F5 |
| MCHP | A1 | F5 |
| MCHP | A2 | F5 |
| MMI | A1 | F3 |
| MMI | A2 | F3 |
| MP | A1 | F5 |
| MP | A2 | F5 |
| MRNA | A1 | F3 |
| MRNA | A2 | F3 |
| MSDL | A1 | F3 |
| MSDL | A2 | F3 |
| MSGK | A1 | F5 |
| MSGK | A2 | F5 |
| MTD | A1 | F5 |
| MTD | A2 | F5 |
| NET | A1 | F3 |
| NET | A2 | F3 |
| NL | A1 | F2 |
| NL | A2 | F2 |
| NMIH | A1 | F4 |
| NMIH | A2 | F4 |
| NNI | A1 | F4 |
| NNI | A2 | F4 |
| NOG | A1 | F4 |
| NOG | A2 | F4 |
| NRDS | A1 | F3 |
| NRDS | A2 | F3 |
| OKLO | A1 | F6 |
| OKLO | A2 | F6 |
| OMDA | A1 | F3 |
| OMDA | A2 | F3 |
| OUT | A1 | F4 |
| OUT | A2 | F4 |
| PAGP | A1 | F5 |
| PAGP | A2 | F5 |
| PAR | A1 | F3 |
| PAR | A2 | F3 |
| PBA | A1 | F4 |
| PBA | A2 | F4 |
| PBYI | A1 | F2 |
| PBYI | A2 | F2 |
| PCTY | A1 | F5 |
| PCTY | A2 | F5 |
| PDFS | A1 | F3 |
| PDFS | A2 | F3 |
| PLSE | A1 | F4 |
| PLSE | A2 | F4 |
| PPL | A1 | F6 |
| PPL | A2 | F6 |
| PRAA | A1 | F3 |
| PRAA | A2 | F3 |
| PRDO | A1 | F3 |
| PRDO | A2 | F3 |
| PSIX | A1 | F3 |
| PSIX | A2 | F3 |
| PURR | A1 | F2 |
| PURR | A2 | F2 |
| QNT | A1 | F3 |
| QNT | A2 | F3 |
| RCEL | A1 | F3 |
| RCEL | A2 | F3 |
| REF | A1 | F3 |
| REF | A2 | F3 |
| REG | A1 | F5 |
| REG | A2 | F5 |
| RGA | A1 | F5 |
| RGA | A2 | F5 |
| RIGL | A1 | F3 |
| RIGL | A2 | F3 |
| RWAY | A1 | F2 |
| RWAY | A2 | F2 |
| SARO | A1 | F5 |
| SARO | A2 | F5 |
| SG | A1 | F3 |
| SG | A2 | F3 |
| SHO | A1 | F4 |
| SHO | A2 | F4 |
| SKWD | A1 | F4 |
| SKWD | A2 | F4 |
| SLVM | A1 | F3 |
| SLVM | A2 | F3 |
| SOLV | A1 | F5 |
| SOLV | A2 | F5 |
| SPG | A1 | F3 |
| SPG | A2 | F3 |
| SPNT | A1 | F4 |
| SPNT | A2 | F4 |
| SRPT | A1 | F3 |
| SRPT | A2 | F3 |
| STEP | A1 | F4 |
| STEP | A2 | F4 |
| STLN | A1 | F2 |
| STLN | A2 | F2 |
| STWD | A1 | F5 |
| STWD | A2 | F5 |
| SUZ | A1 | F2 |
| SUZ | A2 | F2 |
| SVM | A1 | F2 |
| SVM | A2 | F2 |
| SVV | A1 | F2 |
| SVV | A2 | F2 |
| TBCH | A1 | F3 |
| TBCH | A2 | F3 |
| TCX | A1 | F3 |
| TCX | A2 | F3 |
| TDC | A1 | F5 |
| TDC | A2 | F5 |
| TEAM | A1 | F5 |
| TEAM | A2 | F5 |
| TILE | A1 | F4 |
| TILE | A2 | F4 |
| TMDX | A1 | F5 |
| TMDX | A2 | F5 |
| TNDM | A1 | F3 |
| TNDM | A2 | F3 |
| TRUP | A1 | F3 |
| TRUP | A2 | F3 |
| TSSI | A1 | F2 |
| TSSI | A2 | F2 |
| TXG | A1 | F5 |
| TXG | A2 | F5 |
| TXRH | A1 | F5 |
| TXRH | A2 | F5 |
| UA | A1 | F2 |
| UA | A2 | F2 |
| UAA | A1 | F2 |
| UAA | A2 | F2 |
| UMAC | A1 | F3 |
| UMAC | A2 | F3 |
| UTZ | A1 | F3 |
| UTZ | A2 | F3 |
| VEON | A1 | F4 |
| VEON | A2 | F4 |
| VERA | A1 | F5 |
| VERA | A2 | F5 |
| VSAT | A1 | F6 |
| VSAT | A2 | F6 |
| VSTM | A1 | F2 |
| VSTM | A2 | F2 |
| WEST | A1 | F3 |
| WEST | A2 | F3 |
| WHG | A1 | F3 |
| WHG | A2 | F3 |
| WK | A1 | F6 |
| WK | A2 | F6 |
| WLDN | A1 | F3 |
| WLDN | A2 | F3 |
| WPM | A1 | F3 |
| WPM | A2 | F3 |
| WSC | A1 | F5 |
| WSC | A2 | F5 |
| WULF | A1 | F7 |
| WULF | A2 | F7 |
| WYNN | A1 | F5 |
| WYNN | A2 | F5 |
| XRAY | A1 | F4 |
| XRAY | A2 | F4 |
| YELP | A1 | F3 |
| YELP | A2 | F3 |
| ZD | A1 | F3 |
| ZD | A2 | F3 |

## Exploration book tonight (21; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| ABNB | SS | 2026-11-13T00:00:00.000 | 170.00 | 15.03 | +8.38% | 3,182.04 | F3 |
| CLMT | SS | 2026-11-20T00:00:00.000 | 43.00 | 6.89 | +14.94% | 1,284.76 | F6 |
| COMP | SS | 2026-11-20T00:00:00.000 | 9.00 | 1.70 | +17.28% | 274.12 | F2 |
| DK | SS | 2026-11-20T00:00:00.000 | 62.50 | 8.00 | +11.42% | 1,773.42 | F6 |
| DKNG | SS | 2026-11-13T00:00:00.000 | 24.00 | 2.65 | +10.89% | 645.00 | PASS |
| DOCS | SS | 2026-11-20T00:00:00.000 | 32.50 | 6.80 | +19.31% | 1,078.55 | F6 |
| DOCS | IC | 2026-11-20T00:00:00.000 | 32.50 | 6.02 | +16.55% | 648.31 | F6 |
| DVN | SS | 2026-11-13T00:00:00.000 | 43.00 | 2.79 | +6.02% | 774.86 | F6 |
| GH | SS | 2026-11-20T00:00:00.000 | 150.00 | 31.68 | +19.98% | 5,415.49 | F7 |
| INOD | SS | 2026-11-13T00:00:00.000 | 38.00 | 7.75 | +18.21% | 1,806.89 | F3 |
| IONQ | SS | 2026-11-13T00:00:00.000 | 26.50 | 4.17 | +15.23% | 980.86 | F7 |
| IREN | SS | 2026-11-13T00:00:00.000 | 18.00 | 4.55 | +24.62% | 1,084.77 | F7 |
| MAT | SS | 2026-11-20T00:00:00.000 | 15.00 | 1.91 | +11.74% | 388.37 | F6 |
| MRNA | SS | 2026-11-13T00:00:00.000 | 242.50 | 33.90 | +13.63% | 9,569.09 | F3 |
| MRNA | IC | 2026-11-13T00:00:00.000 | 242.50 | 31.48 | +12.16% | 5,601.70 | F3 |
| OKLO | SS | 2026-11-13T00:00:00.000 | 19.50 | 3.05 | +14.73% | 827.35 | F6 |
| PPL | SS | 2026-11-20T00:00:00.000 | 36.00 | 1.56 | +3.70% | 308.52 | F6 |
| VSAT | SS | 2026-11-20T00:00:00.000 | 60.00 | 12.38 | +19.43% | 2,421.16 | F6 |
| VST | SS | 2026-11-13T00:00:00.000 | 115.00 | 10.88 | +9.28% | 2,801.39 | PASS |
| WK | SS | 2026-11-20T00:00:00.000 | 85.00 | 11.85 | +12.87% | 2,347.79 | F6 |
| WULF | SS | 2026-11-13T00:00:00.000 | 10.00 | 2.03 | +19.80% | 531.11 | F7 |

## Graded today (42)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| CHYM | A1 | IC | champion | +0.41% | 12.31 | 2 | no |
| CHYM | A1 | SS | champion | +1.14% | 33.95 | 1 | no |
| SHAK | A1 | SS | champion | +5.42% | 394.61 | 1 | no |
| SHAK | A2 | SS | champion | +5.42% | 394.61 | 1 | no |
| AG | A1 | SS | exploration | -4.24% | -65.28 | 2 | no |
| ALB | A1 | SS | exploration | -2.21% | -210.33 | 1 | no |
| APA | A1 | SS | exploration | -0.61% | -27.32 | 1 | no |
| APP | A1 | SS | exploration | -15.69% | -4,259.22 | 1 | no |
| APP | A1 | IC | exploration | -12.89% | -3,498.93 | 1 | no |
| BROS | A1 | SS | exploration | -6.24% | -273.39 | 1 | no |
| CAH | A1 | SS | exploration | -3.65% | -956.51 | 2 | no |
| CAVA | A1 | SS | exploration | -2.03% | -125.14 | 1 | no |
| CDE | A1 | SS | exploration | -0.56% | -8.21 | 1 | no |
| CF | A1 | SS | exploration | -1.19% | -132.81 | 1 | no |
| CHYM | A1 | SS | exploration | +1.14% | 33.95 | 1 | no |
| CHYM | A1 | IC | exploration | +0.41% | 12.31 | 2 | no |
| CI | A1 | SS | exploration | +0.13% | 41.21 | 2 | no |
| COHR | A1 | SS | exploration | -2.15% | -419.40 | 1 | no |
| CORZ | A1 | SS | exploration | -0.26% | -3.35 | 1 | no |
| ELF | A1 | SS | exploration | +2.53% | 287.61 | 1 | no |
| EW | A1 | SS | exploration | -0.49% | -48.82 | 1 | no |
| EXPE | A1 | SS | exploration | -3.48% | -1,100.09 | 1 | no |
| FIG | A1 | SS | exploration | -1.38% | -30.53 | 1 | no |
| FOUR | A1 | SS | exploration | -2.41% | -107.67 | 1 | no |
| FOUR | A1 | IC | exploration | -4.00% | -178.97 | 2 | no |
| FSLY | A1 | SS | exploration | -6.82% | -143.47 | 1 | no |
| INSW | A1 | SS | exploration | +0.17% | 17.29 | 2 | no |
| IRM | A1 | SS | exploration | -6.22% | -738.99 | 1 | no |
| JOBY | A1 | SS | exploration | -4.23% | -21.34 | 1 | no |
| KMB | A1 | SS | exploration | -1.50% | -163.65 | 2 | no |
| LMND | A1 | SS | exploration | +0.60% | 27.41 | 1 | no |
| MSI | A1 | SS | exploration | -3.38% | -1,679.70 | 1 | no |
| MSI | A1 | IC | exploration | -3.45% | -1,713.55 | 2 | no |
| NTR | A1 | SS | exploration | +0.19% | 13.68 | 1 | no |
| OSCR | A1 | SS | exploration | -3.90% | -137.18 | 1 | no |
| PTON | A1 | SS | exploration | +0.88% | 4.80 | 1 | no |
| SHAK | A1 | SS | exploration | +5.42% | 394.61 | 1 | no |
| SNAP | A1 | SS | exploration | -0.59% | -3.49 | 1 | no |
| U | A1 | SS | exploration | -4.08% | -173.20 | 1 | no |
| VTRS | A1 | SS | exploration | -3.49% | -67.23 | 1 | no |
| WEN | A1 | SS | exploration | -0.69% | -5.23 | 1 | no |
| WOLF | A1 | SS | exploration | -2.02% | -46.20 | 1 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 8 | 6 | +0.63% | 1.12 | 245.49 |
| sa-1.0 | champion | A1 | SS | 29 | 13 | -0.17% | -0.33 | -1,145.05 |
| sa-1.0 | champion | A2 | IC | 7 | 5 | +0.66% | 1.00 | 233.18 |
| sa-1.0 | champion | A2 | SS | 22 | 12 | +0.28% | 0.43 | -39.64 |
| sa-1.0 | exploration | A1 | IC | 47 | 19 | -1.65% | -2.39 | -9,502.62 |
| sa-1.0 | exploration | A1 | SS | 223 | 22 | -1.11% | -4.41 | -22,292.86 |

Ledger: emitted 4 (skipped 0), exploration 21 (skipped 0), graded 42; ledger open.

## S-B state
Gate (2026-11-05, from 2026-11-04 closes): SPY OFF:G2 (VIX 16.61, VIX3M 18.8, X 16.61 vs median 17.255) · QQQ ON (VIX 16.61, VIX3M 18.8, X 25.08 vs median 25.045)

Next session (2026-11-06, from 2026-11-05 closes): SPY UNKNOWN:null input at 2026-11-05 · QQQ UNKNOWN:null input at 2026-11-05

CBOE refresh: ok through 2026-11-05; index-vol through 2026-11-05

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
Universe: 2056 names.
Borrow snapshot: 2026-11-05 (the session's own); fee known for 2048 names.
Bull counts: 0:454, 1:810, 2:501, 3:220, 4:68, 5:3, 6:0, 7:0, 8:0
Bear counts: 0:676, 1:784, 2:384, 3:168, 4:40, 5:3, 6:1, 7:0, 8:0

### LONG (159)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ABBV | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| ABM | 4 | 0 | no | x | x |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| ACEL | 4 | 0 | no | x |  |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| ACGL | 3 | 0 | yes | x | x |  |  |  | x |  |  |  |  |  |  |  |  |  |  |  |  |  | x |
| AER | 4 | 0 | no | x | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| AMAL | 3 | 0 | no | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| AMGN | 3 | 0 | no | x |  |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| AMX | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ANF | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ASND | 4 | 0 | no |  | x | x |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| ASR | 3 | 0 | yes |  | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| AVY | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AWR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| AXS | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AXTA | 3 | 0 | yes |  | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  |  |
| AYI | 3 | 0 | yes |  | x |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| BALL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BFA | 3 | 0 | no | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BJ | 5 | 0 | no | x | x |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| BLBD | 3 | 0 | no |  | x | x |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BLK | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BNT | 3 | 0 | no |  | x | x |  |  | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BOOT | 3 | 0 | no |  | x |  | x |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BRKB | 5 | 0 | no | x | x |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  | x | x |
| BUD | 4 | 0 | yes | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CAG | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CBC | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| CCK | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CERT | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| CHT | 4 | 0 | no | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| CHWY | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CNK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CNMD | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| CNO | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| COST | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| CPB | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CPK | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| CUBE | 4 | 0 | no | x | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| DCOM | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DECK | 3 | 0 | yes |  | x |  |  | x | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| DEO | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DFIN | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DG | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DGX | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| DLX | 3 | 0 | yes |  | x | x |  | x |  | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DRH | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| ECL | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EHC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ELV | 4 | 0 | yes | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EPRT | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| ESLT | 3 | 0 | yes |  | x | x | x |  |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| ESNT | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EXLS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| EXR | 4 | 0 | no | x | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| FAST | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| FIVE | 3 | 0 | no |  | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| FIZZ | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| FMS | 3 | 0 | no |  |  |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| FTS | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  | x |
| FUL | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| FWONA | 4 | 0 | no | x |  |  | x | x | x | ? |  |  | ? |  |  |  |  |  |  |  |  |  | x |
| GABC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| GBX | 3 | 0 | no |  | x | x | x |  |  | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| GFF | 3 | 0 | no | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| GIB | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| GIII | 4 | 0 | yes |  | x |  |  | x | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| GLBE | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| HBT | 3 | 0 | no | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| HCA | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HD | 3 | 0 | no |  | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x | x |
| HG | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HLT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HMC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| HMN | 4 | 0 | no |  | x |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HR | 3 | 0 | yes |  | x |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| IBN | 4 | 0 | yes | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ICE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| INTA | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| IPAR | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| IVZ | 3 | 0 | no |  | x |  | x |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| JCAP | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  | ? | ? |  |  |  | ? |  |  |  |  |  |
| KO | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LEVI | 3 | 0 | yes |  | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  |  |
| LH | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LKFT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| LLY | 3 | 0 | yes | x | x |  |  |  | x |  |  |  |  |  |  |  |  |  |  |  |  | x | x |
| LUV | 3 | 0 | no |  | x |  |  | x | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| LVS | 3 | 0 | yes |  | x | x | x |  |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| MA | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| MAA | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MANU | 3 | 0 | yes |  |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| MCBS | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| MCO | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MDLZ | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MIDD | 3 | 0 | no |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| MMM | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| MRSH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MSCI | 4 | 0 | no | x | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| MSEX | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| MSI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MTG | 3 | 0 | yes |  | x |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| NBTB | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| NDAQ | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| NGG | 3 | 0 | no |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| NVS | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| NWE | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| NWN | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| OBK | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| ONC | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| PACS | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| PFGC | 3 | 0 | yes |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PGR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| POR | 4 | 0 | no |  | x | x |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PPC | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| PPG | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PRG | 3 | 0 | yes |  | x | x | x |  |  | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| RELX | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| REYN | 3 | 0 | no |  | x |  |  |  | x | x |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| RNR | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RPM | 3 | 0 | no |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| RPRX | 3 | 0 | no | x | x |  |  |  | x |  |  |  |  |  |  |  |  |  |  |  |  |  | x |
| RSG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SBH | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| SBUX | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| SHW | 4 | 0 | no |  | x |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SIGI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SJM | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SKWD | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| SMA | 4 | 0 | no | x | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| SPGI | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SPNT | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| STN | 3 | 0 | yes |  | x |  |  |  | x | x |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TAK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TCOM | 4 | 0 | yes |  | x |  | x | x | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| TDG | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| THC | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| THG | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TMP | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TMUS | 3 | 0 | yes |  |  | x | x | x |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| TW | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| UTL | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| V | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| VIPS | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| VLTO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VMC | 3 | 0 | yes |  | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| VRSN | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VTR | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| VTRS | 3 | 0 | no | x |  |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| WCN | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WDFC | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| WM | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WMT | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| WPP | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| WTRG | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| WWW | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| YUM | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |

### SHORT (57)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ALNY | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? | x |  | x |  | x |
| BDC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| BTU | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  | x |  | x |  | x |
| CAR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| CC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? |  |  |  |  | x |
| CELC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| CHRD | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? |  |  |  |  | x |
| CLMT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? | x | x |  |  | ? | x |  |  |  |  |
| CRCL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| CVE | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| CVSA | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| CYTK | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| EC | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  |  |
| FICO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| FIG | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| FLR | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| FLUT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  |  |  |  |  |  | x |
| FSLR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  | x | x |
| FSLY | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  |  | x |
| GEO | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| GIL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  | x |
| GNK | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | ? |  |  | x | x | ? | x |  |  |  |  |
| GRAL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| GTES | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| ICHR | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  |  |
| IDCC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? |  |  |  |  |  |
| INOD | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| IPGP | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| LMND | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? |  |  |  |  | x |
| MELI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  | x | x |
| MGY | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| MTDR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| NRIX | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| NVMI | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| OTTR | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | ? |  |  | x | x | ? |  |  |  |  |  |
| PLTR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| RDDT | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? |  |  |  |  | x |
| RSI | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  | x |  | x |
| SEDG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| SHC | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| SHOO | 0 | 4 | yes |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  |  | x |
| SKYW | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| SM | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| SRPT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| STRA | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  | x |  |  | ? | x |  | x |  |  |
| SYM | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| TKR | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| TPL | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| VCYT | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  | x |  | ? |  |  |  |  | x |
| VG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| VOYG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| VSAT | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x | x |  | ? |  |  |  |  | x |
| W | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| WDS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | ? |  |  | x | x | ? | x |  |  |  |  |
| WOLF | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  | x |  |  | ? | x |  |  | x | x |
| XP | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| ZD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |

### VOL (0)
_none_

CONFLICT (logged only, never a basket, DESIGN/110 §3): 121.

Ledger: emitted 216 (skipped 0), graded 498; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
