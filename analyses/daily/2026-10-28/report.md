# S-A daily — 2026-10-28 (S3)

Preflight: WARN — prices.parquet ends 2026-10-23, BEFORE the 2026-10-28 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-10-23, BEFORE the 2026-10-28 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-10-23, BEFORE the 2026-10-28 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (10)
| ticker | variant | structure | expiry | k | k_up | k_dn | credit_entry | credit_net_pct | risk_usd | contracts | entry_tier_max | cap_pass |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F | A1 | IC | 2026-10-30T00:00:00.000 | 12.00 | 14.00 | 10.00 | 0.68 | +5.29% | 396.18 | 3 | 1 | yes |
| CROX | A1 | SS | 2026-11-20T00:00:00.000 | 120.00 | — | — | 15.89 | +12.93% | 2,856.81 | 1 | 1 | yes |
| CMG | A1 | SS | 2026-10-30T00:00:00.000 | 28.50 | — | — | 2.27 | +7.66% | 556.48 | 1 | 1 | no |
| TROW | A1 | SS | 2026-11-20T00:00:00.000 | 105.00 | — | — | 6.65 | +6.19% | 1,114.40 | 1 | 1 | no |
| F | A1 | SS | 2026-10-30T00:00:00.000 | 12.00 | — | — | 0.70 | +5.63% | 840.44 | 4 | 1 | no |
| F | A2 | IC | 2026-10-30T00:00:00.000 | 12.00 | 14.00 | 10.00 | 0.68 | +5.29% | 396.18 | 3 | 1 | yes |
| CROX | A2 | SS | 2026-11-20T00:00:00.000 | 120.00 | — | — | 15.89 | +12.93% | 2,856.81 | 1 | 1 | yes |
| CMG | A2 | SS | 2026-10-30T00:00:00.000 | 28.50 | — | — | 2.27 | +7.66% | 556.48 | 1 | 1 | no |
| TROW | A2 | SS | 2026-11-20T00:00:00.000 | 105.00 | — | — | 6.65 | +6.19% | 1,114.40 | 1 | 1 | no |
| F | A2 | SS | 2026-10-30T00:00:00.000 | 12.00 | — | — | 0.70 | +5.63% | 840.44 | 4 | 1 | no |

## Suppressed (518)
| ticker | variant | first_fail |
|---|---|---|
| AAMI | A1 | F4 |
| AAMI | A2 | F4 |
| ADAM | A1 | F2 |
| ADAM | A2 | F2 |
| AEM | A1 | F3 |
| AEM | A2 | F3 |
| AGCO | A1 | F5 |
| AGCO | A2 | F5 |
| AGI | A1 | F6 |
| AGI | A2 | F6 |
| AIN | A1 | F3 |
| AIN | A2 | F3 |
| ALGM | A1 | F6 |
| ALGM | A2 | F6 |
| ALGN | A1 | F6 |
| ALGN | A2 | F6 |
| ALKT | A1 | F3 |
| ALKT | A2 | F3 |
| ALNY | A1 | F5 |
| ALNY | A2 | F5 |
| ALRS | A1 | F3 |
| ALRS | A2 | F3 |
| AM | A1 | F5 |
| AM | A2 | F5 |
| AMP | A1 | F5 |
| AMP | A2 | F5 |
| AMRZ | A1 | F6 |
| AMRZ | A2 | F6 |
| AMSF | A1 | F3 |
| AMSF | A2 | F3 |
| AOS | A1 | F5 |
| AOS | A2 | F5 |
| APG | A1 | F5 |
| APG | A2 | F5 |
| AR | A1 | F6 |
| AR | A2 | F6 |
| ARES | A1 | F6 |
| ARES | A2 | F6 |
| ARXS | A1 | F5 |
| ARXS | A2 | F5 |
| ASX | A1 | F3 |
| ASX | A2 | F3 |
| ATI | A1 | F5 |
| ATI | A2 | F5 |
| AUR | A1 | F2 |
| AUR | A2 | F2 |
| AVY | A1 | F5 |
| AVY | A2 | F5 |
| AWK | A1 | F5 |
| AWK | A2 | F5 |
| AXS | A1 | F5 |
| AXS | A2 | F5 |
| AXTA | A1 | F5 |
| AXTA | A2 | F5 |
| BAND | A1 | F3 |
| BAND | A2 | F3 |
| BAX | A1 | F6 |
| BAX | A2 | F6 |
| BBVA | A1 | F3 |
| BBVA | A2 | F3 |
| BC | A1 | F4 |
| BC | A2 | F4 |
| BCBP | A1 | F2 |
| BCBP | A2 | F2 |
| BDC | A1 | F4 |
| BDC | A2 | F4 |
| BELFB | A1 | F3 |
| BELFB | A2 | F3 |
| BFLY | A1 | F2 |
| BFLY | A2 | F2 |
| BG | A1 | F5 |
| BG | A2 | F5 |
| BHC | A1 | F2 |
| BHC | A2 | F2 |
| BHE | A1 | F4 |
| BHE | A2 | F4 |
| BLDR | A1 | F5 |
| BLDR | A2 | F5 |
| BMY | A1 | F3 |
| BMY | A2 | F3 |
| BNL | A1 | F4 |
| BNL | A2 | F4 |
| BOOT | A1 | F5 |
| BOOT | A2 | F5 |
| BUD | A1 | F3 |
| BUD | A2 | F3 |
| BWA | A1 | F5 |
| BWA | A2 | F5 |
| BXMT | A1 | F3 |
| BXMT | A2 | F3 |
| CARR | A1 | F6 |
| CARR | A2 | F6 |
| CAT | A1 | F3 |
| CAT | A2 | F3 |
| CBAN | A1 | F3 |
| CBAN | A2 | F3 |
| CCB | A1 | F3 |
| CCB | A2 | F3 |
| CCS | A1 | F3 |
| CCS | A2 | F3 |
| CFR | A1 | F5 |
| CFR | A2 | F5 |
| CHDN | A1 | F5 |
| CHDN | A2 | F5 |
| CLB | A1 | F3 |
| CLB | A2 | F3 |
| CLPT | A1 | F3 |
| CLPT | A2 | F3 |
| CMPR | A1 | F3 |
| CMPR | A2 | F3 |
| CNMD | A1 | F3 |
| CNMD | A2 | F3 |
| CNX | A1 | F5 |
| CNX | A2 | F5 |
| CNXN | A1 | F4 |
| CNXN | A2 | F4 |
| COHU | A1 | F5 |
| COHU | A2 | F5 |
| CP | A1 | F3 |
| CP | A2 | F3 |
| CRH | A1 | F3 |
| CRH | A2 | F3 |
| CSL | A1 | F5 |
| CSL | A2 | F5 |
| CSW | A1 | F4 |
| CSW | A2 | F4 |
| CTSH | A1 | F5 |
| CTSH | A2 | F5 |
| CVNA | A1 | F7 |
| CVNA | A2 | F7 |
| CWT | A1 | F4 |
| CWT | A2 | F4 |
| DAR | A1 | F5 |
| DAR | A2 | F5 |
| DFIN | A1 | F3 |
| DFIN | A2 | F3 |
| DGICA | A1 | F3 |
| DGICA | A2 | F3 |
| DHI | A1 | F6 |
| DHI | A2 | F6 |
| DRS | A1 | F4 |
| DRS | A2 | F4 |
| DTM | A1 | F5 |
| DTM | A2 | F5 |
| EBAY | A1 | F3 |
| EBAY | A2 | F3 |
| EFOR | A1 | F3 |
| EFOR | A2 | F3 |
| EFXT | A1 | F4 |
| EFXT | A2 | F4 |
| EG | A1 | F5 |
| EG | A2 | F5 |
| EGO | A1 | F5 |
| EGO | A2 | F5 |
| EHC | A1 | F5 |
| EHC | A2 | F5 |
| EIG | A1 | F3 |
| EIG | A2 | F3 |
| EME | A1 | F5 |
| EME | A2 | F5 |
| ENTG | A1 | F5 |
| ENTG | A2 | F5 |
| EPAC | A1 | F3 |
| EPAC | A2 | F3 |
| EPR | A1 | F4 |
| EPR | A2 | F4 |
| EQIX | A1 | F3 |
| EQIX | A2 | F3 |
| ESTA | A1 | F4 |
| ESTA | A2 | F4 |
| FBRT | A1 | F2 |
| FBRT | A2 | F2 |
| FCN | A1 | F5 |
| FCN | A2 | F5 |
| FCPT | A1 | F4 |
| FCPT | A2 | F4 |
| FLS | A1 | F5 |
| FLS | A2 | F5 |
| FOR | A1 | F3 |
| FOR | A2 | F3 |
| FORM | A1 | F5 |
| FORM | A2 | F5 |
| FPI | A1 | F3 |
| FPI | A2 | F3 |
| FSS | A1 | F5 |
| FSS | A2 | F5 |
| FTAI | A1 | F6 |
| FTAI | A2 | F6 |
| FTI | A1 | F5 |
| FTI | A2 | F5 |
| FTNT | A1 | F3 |
| FTNT | A2 | F3 |
| FTRE | A1 | F4 |
| FTRE | A2 | F4 |
| FVRR | A1 | F2 |
| FVRR | A2 | F2 |
| GATX | A1 | F4 |
| GATX | A2 | F4 |
| GBFH | A1 | F3 |
| GBFH | A2 | F3 |
| GEN | A1 | F5 |
| GEN | A2 | F5 |
| GFL | A1 | F6 |
| GFL | A2 | F6 |
| GKOS | A1 | F5 |
| GKOS | A2 | F5 |
| GOOG | A1 | F3 |
| GOOG | A2 | F3 |
| GOOGL | A1 | F3 |
| GOOGL | A2 | F3 |
| GRBK | A1 | F4 |
| GRBK | A2 | F4 |
| GTX | A1 | F5 |
| GTX | A2 | F5 |
| GVA | A1 | F5 |
| GVA | A2 | F5 |
| H | A1 | F5 |
| H | A2 | F5 |
| HAPN | A1 | F3 |
| HAPN | A2 | F3 |
| HDSN | A1 | F2 |
| HDSN | A2 | F2 |
| HGV | A1 | F4 |
| HGV | A2 | F4 |
| HII | A1 | F5 |
| HII | A2 | F5 |
| HIPO | A1 | F3 |
| HIPO | A2 | F3 |
| HLI | A1 | F5 |
| HLI | A2 | F5 |
| HLN | A1 | F5 |
| HLN | A2 | F5 |
| HOG | A1 | F5 |
| HOG | A2 | F5 |
| HONA | A1 | F3 |
| HONA | A2 | F3 |
| HRTG | A1 | F3 |
| HRTG | A2 | F3 |
| HSY | A1 | F6 |
| HSY | A2 | F6 |
| HWM | A1 | F3 |
| HWM | A2 | F3 |
| ICE | A1 | F3 |
| ICE | A2 | F3 |
| IDA | A1 | F5 |
| IDA | A2 | F5 |
| IDCC | A1 | F5 |
| IDCC | A2 | F5 |
| ILPT | A1 | F2 |
| ILPT | A2 | F2 |
| INCY | A1 | F6 |
| INCY | A2 | F6 |
| INDV | A1 | F5 |
| INDV | A2 | F5 |
| ING | A1 | F3 |
| ING | A2 | F3 |
| INSM | A1 | F6 |
| INSM | A2 | F6 |
| INVH | A1 | F5 |
| INVH | A2 | F5 |
| JBSS | A1 | F3 |
| JBSS | A2 | F3 |
| JOE | A1 | F4 |
| JOE | A2 | F4 |
| KBR | A1 | F5 |
| KBR | A2 | F5 |
| KGC | A1 | F6 |
| KGC | A2 | F6 |
| KIM | A1 | F5 |
| KIM | A2 | F5 |
| KLAC | A1 | F3 |
| KLAC | A2 | F3 |
| KREF | A1 | F2 |
| KREF | A2 | F2 |
| KYMR | A1 | F5 |
| KYMR | A2 | F5 |
| LAUR | A1 | F4 |
| LAUR | A2 | F4 |
| LGND | A1 | F5 |
| LGND | A2 | F5 |
| LHX | A1 | F6 |
| LHX | A2 | F6 |
| LIN | A1 | F3 |
| LIN | A2 | F3 |
| LKQ | A1 | F6 |
| LKQ | A2 | F6 |
| LLY | A1 | F3 |
| LLY | A2 | F3 |
| LNG | A1 | F3 |
| LNG | A2 | F3 |
| LTH | A1 | F5 |
| LTH | A2 | F5 |
| LXU | A1 | F3 |
| LXU | A2 | F3 |
| LYG | A1 | F2 |
| LYG | A2 | F2 |
| MA | A1 | F3 |
| MA | A2 | F3 |
| MAA | A1 | F5 |
| MAA | A2 | F5 |
| MAX | A1 | F3 |
| MAX | A2 | F3 |
| MBIN | A1 | F4 |
| MBIN | A2 | F4 |
| MBLY | A1 | F2 |
| MBLY | A2 | F2 |
| MCHB | A1 | F4 |
| MCHB | A2 | F4 |
| MCS | A1 | F3 |
| MCS | A2 | F3 |
| MD | A1 | F4 |
| MD | A2 | F4 |
| MGM | A1 | F6 |
| MGM | A2 | F6 |
| MGRC | A1 | F4 |
| MGRC | A2 | F4 |
| MKL | A1 | F5 |
| MKL | A2 | F5 |
| MNRO | A1 | F3 |
| MNRO | A2 | F3 |
| MO | A1 | F3 |
| MO | A2 | F3 |
| MORN | A1 | F5 |
| MORN | A2 | F5 |
| MRAM | A1 | F3 |
| MRAM | A2 | F3 |
| MRK | A1 | F3 |
| MRK | A2 | F3 |
| MSFT | A1 | F3 |
| MSFT | A2 | F3 |
| MTH | A1 | F5 |
| MTH | A2 | F5 |
| MUSA | A1 | F5 |
| MUSA | A2 | F5 |
| MYE | A1 | F3 |
| MYE | A2 | F3 |
| MYRG | A1 | F5 |
| MYRG | A2 | F5 |
| NCLH | A1 | F6 |
| NCLH | A2 | F6 |
| NEO | A1 | F4 |
| NEO | A2 | F4 |
| NEU | A1 | F5 |
| NEU | A2 | F5 |
| NEWT | A1 | F3 |
| NEWT | A2 | F3 |
| NEXT | A1 | F2 |
| NEXT | A2 | F2 |
| NMRK | A1 | F3 |
| NMRK | A2 | F3 |
| NOW | A1 | F3 |
| NOW | A2 | F3 |
| NSP | A1 | F3 |
| NSP | A2 | F3 |
| NVCR | A1 | F3 |
| NVCR | A2 | F3 |
| NWPX | A1 | F3 |
| NWPX | A2 | F3 |
| NXT | A1 | F5 |
| NXT | A2 | F5 |
| OBK | A1 | F3 |
| OBK | A2 | F3 |
| OLED | A1 | F5 |
| OLED | A2 | F5 |
| OMCL | A1 | F3 |
| OMCL | A2 | F3 |
| ORLY | A1 | F3 |
| ORLY | A2 | F3 |
| OSK | A1 | F5 |
| OSK | A2 | F5 |
| OWL | A1 | F2 |
| OWL | A2 | F2 |
| PATK | A1 | F4 |
| PATK | A2 | F4 |
| PBF | A1 | F5 |
| PBF | A2 | F5 |
| PBI | A1 | F4 |
| PBI | A2 | F4 |
| PFS | A1 | F4 |
| PFS | A2 | F4 |
| PGY | A1 | F3 |
| PGY | A2 | F3 |
| PHAT | A1 | F2 |
| PHAT | A2 | F2 |
| PHIN | A1 | F4 |
| PHIN | A2 | F4 |
| PI | A1 | F5 |
| PI | A2 | F5 |
| PLXS | A1 | F6 |
| PLXS | A2 | F6 |
| POR | A1 | F5 |
| POR | A2 | F5 |
| PPC | A1 | F4 |
| PPC | A2 | F4 |
| PRCH | A1 | F4 |
| PRCH | A2 | F4 |
| PRLB | A1 | F4 |
| PRLB | A2 | F4 |
| PTEN | A1 | F5 |
| PTEN | A2 | F5 |
| PWP | A1 | F3 |
| PWP | A2 | F3 |
| PWR | A1 | F3 |
| PWR | A2 | F3 |
| QSR | A1 | F5 |
| QSR | A2 | F5 |
| QTWO | A1 | F4 |
| QTWO | A2 | F4 |
| QUAD | A1 | F2 |
| QUAD | A2 | F2 |
| RES | A1 | F2 |
| RES | A2 | F2 |
| RJF | A1 | F5 |
| RJF | A2 | F5 |
| RM | A1 | F3 |
| RM | A2 | F3 |
| RSI | A1 | F3 |
| RSI | A2 | F3 |
| RYZ | A1 | F3 |
| RYZ | A2 | F3 |
| SAH | A1 | F3 |
| SAH | A2 | F3 |
| SAIA | A1 | F5 |
| SAIA | A2 | F5 |
| SBSI | A1 | F3 |
| SBSI | A2 | F3 |
| SCI | A1 | F5 |
| SCI | A2 | F5 |
| SFM | A1 | F5 |
| SFM | A2 | F5 |
| SHEL | A1 | F3 |
| SHEL | A2 | F3 |
| SIMO | A1 | F5 |
| SIMO | A2 | F5 |
| SIRI | A1 | F6 |
| SIRI | A2 | F6 |
| SLGN | A1 | F4 |
| SLGN | A2 | F4 |
| SPOK | A1 | F3 |
| SPOK | A2 | F3 |
| STGW | A1 | F2 |
| STGW | A2 | F2 |
| STM | A1 | F6 |
| STM | A2 | F6 |
| STRL | A1 | F5 |
| STRL | A2 | F5 |
| TAK | A1 | F3 |
| TAK | A2 | F3 |
| TAL | A1 | F4 |
| TAL | A2 | F4 |
| TDOC | A1 | F2 |
| TDOC | A2 | F2 |
| TECK | A1 | F5 |
| TECK | A2 | F5 |
| TENB | A1 | F5 |
| TENB | A2 | F5 |
| THC | A1 | F5 |
| THC | A2 | F5 |
| THG | A1 | F5 |
| THG | A2 | F5 |
| TMUS | A1 | F3 |
| TMUS | A2 | F3 |
| TNET | A1 | F4 |
| TNET | A2 | F4 |
| TPG | A1 | F5 |
| TPG | A2 | F5 |
| TRN | A1 | F4 |
| TRN | A2 | F4 |
| TRS | A1 | F3 |
| TRS | A2 | F3 |
| TSAT | A1 | F3 |
| TSAT | A2 | F3 |
| TT | A1 | F3 |
| TT | A2 | F3 |
| TTE | A1 | F3 |
| TTE | A2 | F3 |
| TW | A1 | F5 |
| TW | A2 | F5 |
| TWI | A1 | F2 |
| TWI | A2 | F2 |
| TXT | A1 | F5 |
| TXT | A2 | F5 |
| TYL | A1 | F5 |
| TYL | A2 | F5 |
| UFPI | A1 | F4 |
| UFPI | A2 | F4 |
| UPBD | A1 | F3 |
| UPBD | A2 | F3 |
| UVSP | A1 | F3 |
| UVSP | A2 | F3 |
| VICI | A1 | F5 |
| VICI | A2 | F5 |
| VIST | A1 | F5 |
| VIST | A2 | F5 |
| VMC | A1 | F5 |
| VMC | A2 | F5 |
| WCC | A1 | F5 |
| WCC | A2 | F5 |
| WEC | A1 | F5 |
| WEC | A2 | F5 |
| WEX | A1 | F5 |
| WEX | A2 | F5 |
| WFG | A1 | F4 |
| WFG | A2 | F4 |
| WHD | A1 | F4 |
| WHD | A2 | F4 |
| WNC | A1 | F3 |
| WNC | A2 | F3 |
| WST | A1 | F5 |
| WST | A2 | F5 |
| WTBA | A1 | F3 |
| WTBA | A2 | F3 |
| WTW | A1 | F5 |
| WTW | A2 | F5 |
| XEL | A1 | F5 |
| XEL | A2 | F5 |
| XPO | A1 | F5 |
| XPO | A2 | F5 |

## Exploration book tonight (49; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| AEM | SS | 2026-10-30T00:00:00.000 | 182.50 | 7.10 | +3.61% | 4,016.64 | F3 |
| AGI | SS | 2026-11-20T00:00:00.000 | 31.00 | 3.01 | +7.89% | 526.63 | F6 |
| ALGM | SS | 2026-11-20T00:00:00.000 | 35.00 | 6.41 | +16.63% | 1,025.50 | F6 |
| ALGN | SS | 2026-10-30T00:00:00.000 | 152.50 | 15.45 | +9.03% | 3,425.63 | F6 |
| AMRZ | SS | 2026-11-20T00:00:00.000 | 40.00 | 3.32 | +7.72% | 558.66 | F6 |
| AMRZ | IC | 2026-11-20T00:00:00.000 | 40.00 | 2.75 | +5.96% | 224.79 | F6 |
| AR | SS | 2026-10-30T00:00:00.000 | 42.00 | 1.88 | +3.93% | 833.81 | F6 |
| ARES | SS | 2026-10-30T00:00:00.000 | 124.00 | 6.80 | +4.73% | 2,566.66 | F6 |
| AUR | SS | 2026-10-30T00:00:00.000 | 5.00 | 0.51 | +7.91% | 170.14 | F2 |
| BAX | SS | 2026-10-30T00:00:00.000 | 25.50 | 2.16 | +6.84% | 569.52 | F6 |
| BC | SS | 2026-11-20T00:00:00.000 | 70.00 | 6.80 | +7.29% | 1,099.68 | F4 |
| CARR | SS | 2026-10-30T00:00:00.000 | 57.00 | 3.26 | +5.23% | 1,021.12 | F6 |
| CMG | SS | 2026-10-30T00:00:00.000 | 28.50 | 2.27 | +7.66% | 556.48 | PASS |
| CROX | SS | 2026-11-20T00:00:00.000 | 120.00 | 15.89 | +12.93% | 2,856.81 | PASS |
| CVNA | SS | 2026-10-30T00:00:00.000 | 59.00 | 7.72 | +12.62% | 1,936.92 | F7 |
| DHI | SS | 2026-10-30T00:00:00.000 | 142.00 | 8.32 | +4.60% | 2,513.49 | F6 |
| EBAY | SS | 2026-10-30T00:00:00.000 | 118.00 | 8.66 | +6.89% | 2,070.49 | F3 |
| EBAY | IC | 2026-10-30T00:00:00.000 | 118.00 | 8.36 | +6.44% | 1,163.79 | F3 |
| F | SS | 2026-10-30T00:00:00.000 | 12.00 | 0.70 | +5.63% | 210.11 | PASS |
| F | IC | 2026-10-30T00:00:00.000 | 12.00 | 0.68 | +5.29% | 132.06 | PASS |
| FTAI | SS | 2026-10-30T00:00:00.000 | 165.00 | 15.94 | +8.54% | 5,434.17 | F6 |
| GFL | SS | 2026-10-30T00:00:00.000 | 43.50 | 3.95 | +4.76% | 1,341.25 | F6 |
| HONA | SS | 2026-11-20T00:00:00.000 | 175.00 | 18.21 | +9.17% | 3,434.06 | F3 |
| HONA | IC | 2026-11-20T00:00:00.000 | 175.00 | 16.85 | +8.18% | 1,814.67 | F3 |
| HSY | SS | 2026-10-30T00:00:00.000 | 162.50 | 6.58 | +3.04% | 2,196.25 | F6 |
| HWM | SS | 2026-10-30T00:00:00.000 | 195.00 | 12.43 | +5.66% | 3,909.85 | F3 |
| ICE | SS | 2026-10-30T00:00:00.000 | 155.00 | 5.45 | +2.94% | 1,839.95 | F3 |
| INCY | SS | 2026-11-20T00:00:00.000 | 115.00 | 9.93 | +7.59% | 1,916.49 | F6 |
| INSM | SS | 2026-11-20T00:00:00.000 | 97.50 | 15.47 | +13.46% | 2,796.83 | F6 |
| KGC | SS | 2026-10-30T00:00:00.000 | 22.50 | 1.05 | +3.67% | 494.15 | F6 |
| LHX | SS | 2026-10-30T00:00:00.000 | 260.00 | 11.94 | +3.96% | 3,646.08 | F6 |
| LKQ | SS | 2026-11-20T00:00:00.000 | 17.50 | 1.70 | +8.75% | 263.58 | F6 |
| LKQ | IC | 2026-11-20T00:00:00.000 | 17.50 | 1.26 | +4.99% | 123.78 | F6 |
| MBLY | SS | 2026-10-30T00:00:00.000 | 7.00 | 0.80 | +9.89% | 247.55 | F2 |
| MGM | SS | 2026-11-20T00:00:00.000 | 27.00 | 2.44 | +8.16% | 508.23 | F6 |
| MGM | IC | 2026-11-20T00:00:00.000 | 27.00 | 2.14 | +6.71% | 286.21 | F6 |
| NCLH | SS | 2026-10-30T00:00:00.000 | 16.00 | 1.25 | +7.36% | 392.47 | F6 |
| NCLH | IC | 2026-10-30T00:00:00.000 | 16.00 | 1.20 | +6.96% | 229.79 | F6 |
| OWL | SS | 2026-10-30T00:00:00.000 | 9.50 | 0.55 | +4.88% | 240.13 | F2 |
| PGY | SS | 2026-11-20T00:00:00.000 | 20.00 | 3.94 | +18.09% | 596.73 | F3 |
| PLXS | SS | 2026-11-20T00:00:00.000 | 240.00 | 26.00 | +9.44% | 4,425.99 | F6 |
| PWR | SS | 2026-11-20T00:00:00.000 | 600.00 | 70.05 | +10.85% | 12,670.83 | F3 |
| PWR | IC | 2026-11-20T00:00:00.000 | 600.00 | 63.41 | +9.48% | 7,658.96 | F3 |
| RSI | SS | 2026-11-20T00:00:00.000 | 15.00 | 2.23 | +14.04% | 337.36 | F3 |
| SIRI | SS | 2026-10-30T00:00:00.000 | 27.50 | 1.58 | +4.75% | 431.60 | F6 |
| STM | SS | 2026-10-30T00:00:00.000 | 48.50 | 4.36 | +8.10% | 1,384.85 | F6 |
| TDOC | SS | 2026-10-30T00:00:00.000 | 7.00 | 0.76 | +8.61% | 221.29 | F2 |
| TDOC | IC | 2026-10-30T00:00:00.000 | 7.00 | 0.70 | +7.32% | 130.23 | F2 |
| TROW | SS | 2026-11-20T00:00:00.000 | 105.00 | 6.65 | +6.19% | 1,114.40 | PASS |

## Graded today (36)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| CAKE | A1 | IC | champion | -0.07% | -7.75 | 1 | no |
| CAKE | A1 | SS | champion | +1.09% | 118.04 | 1 | no |
| EQT | A1 | SS | champion | -0.01% | -0.38 | 1 | no |
| CAKE | A2 | IC | champion | -0.07% | -7.75 | 1 | no |
| CAKE | A2 | SS | champion | +1.09% | 118.04 | 1 | no |
| EQT | A2 | SS | champion | -0.01% | -0.38 | 1 | no |
| AON | A1 | SS | exploration | +0.54% | 164.42 | 2 | no |
| BIIB | A1 | SS | exploration | +0.06% | 15.90 | 1 | no |
| BSX | A1 | SS | exploration | -2.57% | -115.78 | 1 | no |
| BSX | A1 | IC | exploration | -2.99% | -134.60 | 1 | no |
| CAKE | A1 | SS | exploration | +1.09% | 118.04 | 1 | no |
| CAKE | A1 | IC | exploration | -0.07% | -7.75 | 1 | no |
| ENPH | A1 | SS | exploration | -4.25% | -126.38 | 1 | no |
| EQT | A1 | SS | exploration | -0.01% | -0.38 | 1 | no |
| ETSY | A1 | SS | exploration | -0.18% | -15.75 | 1 | no |
| ETSY | A1 | IC | exploration | -0.70% | -61.56 | 2 | no |
| EXE | A1 | SS | exploration | -0.31% | -28.95 | 1 | no |
| FLEX | A1 | SS | exploration | -1.11% | -92.54 | 1 | no |
| FLEX | A1 | IC | exploration | -2.01% | -168.13 | 2 | no |
| GEHC | A1 | SS | exploration | -2.67% | -189.33 | 1 | no |
| GNRC | A1 | SS | exploration | +0.12% | 23.91 | 1 | no |
| GRMN | A1 | SS | exploration | +2.32% | 671.16 | 1 | no |
| HOOD | A1 | SS | exploration | +2.26% | 214.21 | 1 | no |
| HOOD | A1 | IC | exploration | +2.03% | 192.37 | 1 | no |
| IP | A1 | SS | exploration | -0.30% | -10.09 | 2 | no |
| NXPI | A1 | SS | exploration | +3.72% | 943.18 | 1 | no |
| NXPI | A1 | IC | exploration | +2.63% | 668.59 | 1 | no |
| OKE | A1 | SS | exploration | -0.47% | -45.43 | 1 | no |
| OTIS | A1 | SS | exploration | -0.75% | -55.42 | 1 | no |
| PPG | A1 | SS | exploration | -0.50% | -57.13 | 2 | no |
| REPL | A1 | SS | exploration | -0.71% | -9.25 | 1 | no |
| TER | A1 | SS | exploration | +1.55% | 504.14 | 1 | no |
| UMC | A1 | SS | exploration | -0.09% | -1.67 | 1 | no |
| VFC | A1 | SS | exploration | +2.03% | 34.47 | 1 | no |
| VRT | A1 | SS | exploration | -2.68% | -560.10 | 1 | no |
| VRT | A1 | IC | exploration | -2.64% | -551.88 | 1 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 6 | 4 | +0.80% | 0.99 | 268.43 |
| sa-1.0 | champion | A1 | SS | 14 | 8 | +0.47% | 0.78 | 536.34 |
| sa-1.0 | champion | A2 | IC | 6 | 4 | +0.80% | 0.99 | 268.43 |
| sa-1.0 | champion | A2 | SS | 14 | 8 | +0.47% | 0.78 | 536.34 |
| sa-1.0 | exploration | A1 | IC | 27 | 14 | -0.65% | -1.79 | -1,700.12 |
| sa-1.0 | exploration | A1 | SS | 94 | 16 | -0.42% | -2.59 | -2,381.03 |

Ledger: emitted 10 (skipped 0), exploration 49 (skipped 0), graded 36; ledger open.

## S-B state
Gate (2026-10-28, from 2026-10-27 closes): SPY ON (VIX 17.52, VIX3M 19.57, X 17.52 vs median 16.365000000000002) · QQQ ON (VIX 17.52, VIX3M 19.57, X 24.91 vs median 22.485)

Next session (2026-10-29, from 2026-10-28 closes): SPY ON (VIX 16.91, VIX3M 19.22, X 16.91 vs median 16.425) · QQQ ON (VIX 16.91, VIX3M 19.22, X 23.78 vs median 22.605)

CBOE refresh: ok through 2026-10-28; index-vol through 2026-10-28

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
Universe: 1999 names.
Borrow snapshot: 2026-10-28 (the session's own); fee known for 1990 names.
Bull counts: 0:767, 1:670, 2:392, 3:141, 4:29, 5:0, 6:0, 7:0, 8:0
Bear counts: 0:722, 1:778, 2:333, 3:134, 4:29, 5:3, 6:0, 7:0, 8:0

### LONG (90)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ABBV | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| ABM | 4 | 0 | no | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| ADI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ALGM | 3 | 0 | yes |  | x |  | x |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ALKT | 3 | 0 | no |  |  | x | x |  |  | x |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALRM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| AMG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| AMGN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  | x | x |
| AMRX | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| APG | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ARQT | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| AZZ | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| BY | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| CBC | 4 | 0 | no | x | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| CNK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| COLM | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| CRBG | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CSX | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CUBE | 3 | 0 | yes |  | x |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| CUBI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DDOG | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DHR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DNOW | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| DOV | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DOW | 3 | 0 | yes |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| DRH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DV | 4 | 0 | no | x | x |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| EGBN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| EPRT | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EQH | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| FET | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| FTS | 3 | 0 | yes |  | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| GENB | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  | ? |  |  |  |  |  |  |  |  |  | x |
| GILD | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HAL | 3 | 0 | no |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| HASI | 3 | 0 | no |  | x |  | x |  |  | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| HBNC | 4 | 0 | yes | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HHH | 3 | 0 | no |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| HLI | 3 | 0 | no |  | x |  |  | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| HST | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| INGM | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| IRM | 3 | 0 | no |  | x |  | x | x |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| JCI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| JOE | 3 | 0 | no |  |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| KMPR | 3 | 0 | no |  | x |  |  |  | x | x |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| LIN | 4 | 0 | no |  | x |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| LKFT | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| LNG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LQDT | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| MAR | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| MCBS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| MD | 4 | 0 | no | x | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| MHK | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| MMS | 3 | 0 | no |  | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  |  |
| NTAP | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| NTNX | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| NUE | 3 | 0 | yes | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| NWE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| NXPI | 3 | 0 | no |  |  | x |  | x | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| OSW | 3 | 0 | yes | x | x |  |  |  |  | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| PLUS | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PPG | 4 | 0 | no |  |  | x |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| R | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RDVT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| RLJ | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| ROP | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| RS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RYZ | 3 | 0 | yes |  | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| SBH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| SDRL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| SN | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| SNPS | 3 | 0 | no |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SSD | 4 | 0 | no |  |  | x |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  |  |
| SUNB | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TALO | 4 | 0 | no | x | x |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| TDY | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TEL | 3 | 0 | yes |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TEN | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TFX | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| THG | 3 | 0 | yes | x | x |  |  |  | x |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| TRGP | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TTC | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| UCB | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| UNFI | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| URI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| UTHR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| VLTO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VNOM | 3 | 0 | yes |  | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  |  |
| VSTS | 4 | 0 | no | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| WOR | 3 | 0 | no |  | x |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |

### SHORT (76)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AA | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| AAOI | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| ABVX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  |  |
| AI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  |  |
| ALG | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| AWI | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  |  | x |  | ? | x |  |  |  | x |
| BA | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  | x | x | x |
| BDC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| BHF | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  |  |
| BNL | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  |  |
| CAR | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CBRS | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  | x | x |
| CDE | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  | x |
| CLMT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? | x | x |  |  | ? | x |  |  |  |  |
| COIN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  | x | x |
| CRCL | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  |  | x |
| CRWV | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| DAR | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  | x |  |  | x | x |  |  |  | x |
| DASH | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| DLO | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? |  |  |  |  |  |
| DUOL | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? | x |  |  |  | x |
| EEFT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| ENPH | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| F | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| FFIV | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| FOUR | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| GLXY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  |  |  |  |  |  | x |
| HGV | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| HL | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  | x |
| HOOD | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  |  | x | x |
| HSY | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| HUBB | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| HUT | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  | x |
| INFY | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  | x |  | ? |  |  |  |  | x |
| IREN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  | x | x |
| KHC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? |  |  |  |  | x |
| KTB | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| LII | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| LNN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| LPLA | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  |  | x |  | ? | x |  |  |  | x |
| LPX | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| LYV | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| MDLN | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? |  |  |  |  | x |
| META | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| MKC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| MRK | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x | x | ? |  |  |  |  | x |
| MTZ | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  | x |  | x |
| NFLX | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| NHI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| NTES | 0 | 4 | yes |  |  |  |  |  |  | ? |  | x | x |  |  | x | x | ? |  |  |  |  |  |
| NU | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  | x |  | ? |  |  |  |  | x |
| NVAX | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  |  |  |
| OMC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| PDD | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| PINS | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| PSMT | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| RCUS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| RDDT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| SEDG | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| SGI | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| SHAZ | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  |  | x |  |  |  |  |
| SLM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  | x |
| SOLV | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| SPCX | 0 | 4 | no |  |  | ? |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| STEP | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| STRL | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| TMDX | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| TSLX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| UBER | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| VALE | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| VC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  | x |
| VSEC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| VST | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| WELL | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| XP | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| XYZ | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  | x |  | ? | x |  |  |  | x |

### VOL (1)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TTMI | 0 | 2 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? |  | x |  |  | x |

CONFLICT (logged only, never a basket, DESIGN/110 §3): 89.

Ledger: emitted 167 (skipped 0), graded 511; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
