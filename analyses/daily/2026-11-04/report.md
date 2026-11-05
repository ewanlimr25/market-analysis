# S-A daily — 2026-11-04 (S3)

Preflight: WARN — prices.parquet ends 2026-10-30, BEFORE the 2026-11-04 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-10-30, BEFORE the 2026-11-04 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-10-30, BEFORE the 2026-11-04 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (4)
| ticker | variant | structure | expiry | k | k_up | k_dn | credit_entry | credit_net_pct | risk_usd | contracts | entry_tier_max | cap_pass |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CHYM | A1 | IC | 2026-11-20T00:00:00.000 | 30.00 | 37.50 | 22.50 | 3.53 | +10.92% | 397.05 | 1 | 1 | yes |
| CHYM | A1 | SS | 2026-11-20T00:00:00.000 | 30.00 | — | — | 3.78 | +12.07% | 723.85 | 1 | 1 | yes |
| SHAK | A1 | SS | 2026-11-06T00:00:00.000 | 73.00 | — | — | 8.75 | +11.57% | 2,137.15 | 1 | 1 | yes |
| SHAK | A2 | SS | 2026-11-06T00:00:00.000 | 73.00 | — | — | 8.75 | +11.57% | 2,137.15 | 1 | 1 | yes |

## Suppressed (739)
| ticker | variant | first_fail |
|---|---|---|
| AAP | A1 | F6 |
| AAP | A2 | F6 |
| ABTC | A1 | F2 |
| ABTC | A2 | F2 |
| ACAD | A1 | F4 |
| ACAD | A2 | F4 |
| ACHC | A1 | F5 |
| ACHC | A2 | F5 |
| ACIW | A1 | F4 |
| ACIW | A2 | F4 |
| ACLS | A1 | F4 |
| ACLS | A2 | F4 |
| ACMR | A1 | F5 |
| ACMR | A2 | F5 |
| ACNT | A1 | F3 |
| ACNT | A2 | F3 |
| ACR | A1 | F3 |
| ACR | A2 | F3 |
| ACT | A1 | F4 |
| ACT | A2 | F4 |
| ADPT | A1 | F5 |
| ADPT | A2 | F5 |
| AEVA | A1 | F2 |
| AEVA | A2 | F2 |
| AFL | A1 | F3 |
| AFL | A2 | F3 |
| AG | A1 | F6 |
| AG | A2 | F6 |
| AGEN | A1 | F2 |
| AGEN | A2 | F2 |
| AGIO | A1 | F3 |
| AGIO | A2 | F3 |
| AGL | A1 | F3 |
| AGL | A2 | F3 |
| ALB | A1 | F6 |
| ALB | A2 | F6 |
| ALGT | A1 | F4 |
| ALGT | A2 | F4 |
| ALL | A1 | F3 |
| ALL | A2 | F3 |
| ALNT | A1 | F3 |
| ALNT | A2 | F3 |
| AMCR | A1 | F5 |
| AMCR | A2 | F5 |
| AMH | A1 | F5 |
| AMH | A2 | F5 |
| AMPL | A1 | F3 |
| AMPL | A2 | F3 |
| ANIP | A1 | F3 |
| ANIP | A2 | F3 |
| APA | A1 | F6 |
| APA | A2 | F6 |
| APD | A1 | F3 |
| APD | A2 | F3 |
| APP | A1 | F3 |
| APP | A2 | F3 |
| APPN | A1 | F5 |
| APPN | A2 | F5 |
| ARDT | A1 | F3 |
| ARDT | A2 | F3 |
| ARIS | A1 | F4 |
| ARIS | A2 | F4 |
| ARM | A1 | F3 |
| ARM | A2 | F3 |
| ARQT | A1 | F5 |
| ARQT | A2 | F5 |
| ARW | A1 | F5 |
| ARW | A2 | F5 |
| ASTE | A1 | F3 |
| ASTE | A2 | F3 |
| ATNI | A1 | F3 |
| ATNI | A2 | F3 |
| ATO | A1 | F5 |
| ATO | A2 | F5 |
| AU | A1 | F5 |
| AU | A2 | F5 |
| AWR | A1 | F4 |
| AWR | A2 | F4 |
| BBSI | A1 | F3 |
| BBSI | A2 | F3 |
| BBUC | A1 | F4 |
| BBUC | A2 | F4 |
| BCE | A1 | F5 |
| BCE | A2 | F5 |
| BDX | A1 | F3 |
| BDX | A2 | F3 |
| BGC | A1 | F4 |
| BGC | A2 | F4 |
| BIO | A1 | F5 |
| BIO | A2 | F5 |
| BKH | A1 | F5 |
| BKH | A2 | F5 |
| BKSY | A1 | F3 |
| BKSY | A2 | F3 |
| BKV | A1 | F4 |
| BKV | A2 | F4 |
| BLLN | A1 | F5 |
| BLLN | A2 | F5 |
| BOBS | A1 | F4 |
| BOBS | A2 | F4 |
| BROS | A1 | F6 |
| BROS | A2 | F6 |
| BSY | A1 | F5 |
| BSY | A2 | F5 |
| BTG | A1 | F2 |
| BTG | A2 | F2 |
| BYND | A1 | F2 |
| BYND | A2 | F2 |
| CAH | A1 | F3 |
| CAH | A2 | F3 |
| CAI | A1 | F5 |
| CAI | A2 | F5 |
| CARS | A1 | F3 |
| CARS | A2 | F3 |
| CAVA | A1 | F6 |
| CAVA | A2 | F6 |
| CCOI | A1 | F2 |
| CCOI | A2 | F2 |
| CDE | A1 | F6 |
| CDE | A2 | F6 |
| CDRE | A1 | F3 |
| CDRE | A2 | F3 |
| CERT | A1 | F3 |
| CERT | A2 | F3 |
| CF | A1 | F6 |
| CF | A2 | F6 |
| CG | A1 | F5 |
| CG | A2 | F5 |
| CGNX | A1 | F5 |
| CGNX | A2 | F5 |
| CHRD | A1 | F5 |
| CHRD | A2 | F5 |
| CHYM | A2 | A2_sector |
| CI | A1 | F3 |
| CI | A2 | F3 |
| CIM | A1 | F2 |
| CIM | A2 | F2 |
| CION | A1 | F2 |
| CION | A2 | F2 |
| CLDT | A1 | F3 |
| CLDT | A2 | F3 |
| CMI | A1 | F3 |
| CMI | A2 | F3 |
| CNQ | A1 | F3 |
| CNQ | A2 | F3 |
| CNR | A1 | F4 |
| CNR | A2 | F4 |
| CODI | A1 | F3 |
| CODI | A2 | F3 |
| COHR | A1 | F6 |
| COHR | A2 | F6 |
| COKE | A1 | F5 |
| COKE | A2 | F5 |
| COLD | A1 | F4 |
| COLD | A2 | F4 |
| COLL | A1 | F3 |
| COLL | A2 | F3 |
| COP | A1 | F3 |
| COP | A2 | F3 |
| CORZ | A1 | F7 |
| CORZ | A2 | F7 |
| CPAY | A1 | F5 |
| CPAY | A2 | F5 |
| CPS | A1 | F3 |
| CPS | A2 | F3 |
| CRK | A1 | F4 |
| CRK | A2 | F4 |
| CRUS | A1 | F5 |
| CRUS | A2 | F5 |
| CSV | A1 | F3 |
| CSV | A2 | F3 |
| CTKB | A1 | F2 |
| CTKB | A2 | F2 |
| CTRI | A1 | F4 |
| CTRI | A2 | F4 |
| CW | A1 | F5 |
| CW | A2 | F5 |
| CXT | A1 | F4 |
| CXT | A2 | F4 |
| CXW | A1 | F5 |
| CXW | A2 | F5 |
| CYTK | A1 | F5 |
| CYTK | A2 | F5 |
| DAVE | A1 | F5 |
| DAVE | A2 | F5 |
| DCO | A1 | F4 |
| DCO | A2 | F4 |
| DIBS | A1 | F2 |
| DIBS | A2 | F2 |
| DLX | A1 | F3 |
| DLX | A2 | F3 |
| DNOW | A1 | F4 |
| DNOW | A2 | F4 |
| DSGR | A1 | F3 |
| DSGR | A2 | F3 |
| DTE | A1 | F5 |
| DTE | A2 | F5 |
| DUK | A1 | F3 |
| DUK | A2 | F3 |
| ECPG | A1 | F4 |
| ECPG | A2 | F4 |
| ECVT | A1 | F2 |
| ECVT | A2 | F2 |
| EE | A1 | F3 |
| EE | A2 | F3 |
| EFC | A1 | F3 |
| EFC | A2 | F3 |
| ELF | A1 | F6 |
| ELF | A2 | F6 |
| ENOV | A1 | F3 |
| ENOV | A2 | F3 |
| EOLS | A1 | F2 |
| EOLS | A2 | F2 |
| EPAM | A1 | F5 |
| EPAM | A2 | F5 |
| ERII | A1 | F2 |
| ERII | A2 | F2 |
| ES | A1 | F5 |
| ES | A2 | F5 |
| EVRG | A1 | F5 |
| EVRG | A2 | F5 |
| EW | A1 | F3 |
| EW | A2 | F3 |
| EXPE | A1 | F6 |
| EXPE | A2 | F6 |
| FA | A1 | F4 |
| FA | A2 | F4 |
| FC | A1 | F3 |
| FC | A2 | F3 |
| FICO | A1 | F5 |
| FICO | A2 | F5 |
| FIG | A1 | F7 |
| FIG | A2 | F7 |
| FOUR | A1 | F7 |
| FOUR | A2 | F7 |
| FSK | A1 | F4 |
| FSK | A2 | F4 |
| FSLY | A1 | F6 |
| FSLY | A2 | F6 |
| FSM | A1 | F2 |
| FSM | A2 | F2 |
| FTDR | A1 | F5 |
| FTDR | A2 | F5 |
| FUN | A1 | F2 |
| FUN | A2 | F2 |
| FWONA | A1 | F4 |
| FWONA | A2 | F4 |
| FWONK | A1 | F5 |
| FWONK | A2 | F5 |
| GENI | A1 | F2 |
| GENI | A2 | F2 |
| GEO | A1 | F5 |
| GEO | A2 | F5 |
| GHM | A1 | F3 |
| GHM | A2 | F3 |
| GIL | A1 | F5 |
| GIL | A2 | F5 |
| GLIBK | A1 | F3 |
| GLIBK | A2 | F3 |
| GMAB | A1 | F5 |
| GMAB | A2 | F5 |
| GNE | A1 | F3 |
| GNE | A2 | F3 |
| GNK | A1 | F3 |
| GNK | A2 | F3 |
| GNL | A1 | F2 |
| GNL | A2 | F2 |
| GNW | A1 | F2 |
| GNW | A2 | F2 |
| GOLD | A1 | F3 |
| GOLD | A2 | F3 |
| GOOS | A1 | F2 |
| GOOS | A2 | F2 |
| GPGI | A1 | F4 |
| GPGI | A2 | F4 |
| GPN | A1 | F5 |
| GPN | A2 | F5 |
| GPOR | A1 | F5 |
| GPOR | A2 | F5 |
| GRAL | A1 | F5 |
| GRAL | A2 | F5 |
| HAE | A1 | F5 |
| HAE | A2 | F5 |
| HCC | A1 | F5 |
| HCC | A2 | F5 |
| HCI | A1 | F4 |
| HCI | A2 | F4 |
| HIMX | A1 | F3 |
| HIMX | A2 | F3 |
| HOS | A1 | F2 |
| HOS | A2 | F2 |
| HPP | A1 | F3 |
| HPP | A2 | F3 |
| HST | A1 | F5 |
| HST | A2 | F5 |
| HUBS | A1 | F5 |
| HUBS | A2 | F5 |
| IBP | A1 | F5 |
| IBP | A2 | F5 |
| IMAX | A1 | F4 |
| IMAX | A2 | F4 |
| INGR | A1 | F5 |
| INGR | A2 | F5 |
| INSW | A1 | F6 |
| INSW | A2 | F6 |
| IOND | A1 | F4 |
| IOND | A2 | F4 |
| IOVA | A1 | F2 |
| IOVA | A2 | F2 |
| IPAR | A1 | F4 |
| IPAR | A2 | F4 |
| IRM | A1 | F6 |
| IRM | A2 | F6 |
| ITT | A1 | F5 |
| ITT | A2 | F5 |
| JOBY | A1 | F2 |
| JOBY | A2 | F2 |
| KE | A1 | F3 |
| KE | A2 | F3 |
| KELYA | A1 | F3 |
| KELYA | A2 | F3 |
| KMB | A1 | F6 |
| KMB | A2 | F6 |
| KNTK | A1 | F5 |
| KNTK | A2 | F5 |
| KTB | A1 | F5 |
| KTB | A2 | F5 |
| KVYO | A1 | F5 |
| KVYO | A2 | F5 |
| LAMR | A1 | F5 |
| LAMR | A2 | F5 |
| LB | A1 | F3 |
| LB | A2 | F3 |
| LCII | A1 | F5 |
| LCII | A2 | F5 |
| LCUT | A1 | F2 |
| LCUT | A2 | F2 |
| LEGH | A1 | F3 |
| LEGH | A2 | F3 |
| LEU | A1 | F3 |
| LEU | A2 | F3 |
| LFST | A1 | F4 |
| LFST | A2 | F4 |
| LMAT | A1 | F4 |
| LMAT | A2 | F4 |
| LMND | A1 | F7 |
| LMND | A2 | F7 |
| LNC | A1 | F5 |
| LNC | A2 | F5 |
| LOAR | A1 | F5 |
| LOAR | A2 | F5 |
| LOPE | A1 | F4 |
| LOPE | A2 | F4 |
| LSPD | A1 | F3 |
| LSPD | A2 | F3 |
| LYTS | A1 | F3 |
| LYTS | A2 | F3 |
| LZ | A1 | F2 |
| LZ | A2 | F2 |
| MAC | A1 | F5 |
| MAC | A2 | F5 |
| MAIR | A1 | F4 |
| MAIR | A2 | F4 |
| MATV | A1 | F3 |
| MATV | A2 | F3 |
| MATX | A1 | F5 |
| MATX | A2 | F5 |
| MBUU | A1 | F3 |
| MBUU | A2 | F3 |
| MCK | A1 | F3 |
| MCK | A2 | F3 |
| MDA | A1 | F3 |
| MDA | A2 | F3 |
| MDU | A1 | F4 |
| MDU | A2 | F4 |
| MET | A1 | F3 |
| MET | A2 | F3 |
| MFC | A1 | F3 |
| MFC | A2 | F3 |
| MFIC | A1 | F3 |
| MFIC | A2 | F3 |
| MGNI | A1 | F4 |
| MGNI | A2 | F4 |
| MGY | A1 | F5 |
| MGY | A2 | F5 |
| MH | A1 | F4 |
| MH | A2 | F4 |
| MIDD | A1 | F5 |
| MIDD | A2 | F5 |
| MKSI | A1 | F5 |
| MKSI | A2 | F5 |
| MLYS | A1 | F3 |
| MLYS | A2 | F3 |
| MNTN | A1 | F3 |
| MNTN | A2 | F3 |
| MRVI | A1 | F2 |
| MRVI | A2 | F2 |
| MRX | A1 | F4 |
| MRX | A2 | F4 |
| MSI | A1 | F3 |
| MSI | A2 | F3 |
| MT | A1 | F5 |
| MT | A2 | F5 |
| MTG | A1 | F5 |
| MTG | A2 | F5 |
| MTRX | A1 | F2 |
| MTRX | A2 | F2 |
| MTSI | A1 | F5 |
| MTSI | A2 | F5 |
| MUR | A1 | F5 |
| MUR | A2 | F5 |
| MWA | A1 | F4 |
| MWA | A2 | F4 |
| MYGN | A1 | F2 |
| MYGN | A2 | F2 |
| NABL | A1 | F2 |
| NABL | A2 | F2 |
| NATR | A1 | F3 |
| NATR | A2 | F3 |
| NAVI | A1 | F2 |
| NAVI | A2 | F2 |
| NFG | A1 | F5 |
| NFG | A2 | F5 |
| NGVT | A1 | F4 |
| NGVT | A2 | F4 |
| NHP | A1 | F3 |
| NHP | A2 | F3 |
| NOA | A1 | F3 |
| NOA | A2 | F3 |
| NREF | A1 | F3 |
| NREF | A2 | F3 |
| NSIT | A1 | F5 |
| NSIT | A2 | F5 |
| NTCT | A1 | F4 |
| NTCT | A2 | F4 |
| NTGR | A1 | F3 |
| NTGR | A2 | F3 |
| NTR | A1 | F6 |
| NTR | A2 | F6 |
| NVMI | A1 | F5 |
| NVMI | A2 | F5 |
| NVRI | A1 | F3 |
| NVRI | A2 | F3 |
| NVST | A1 | F5 |
| NVST | A2 | F5 |
| NWE | A1 | F5 |
| NWE | A2 | F5 |
| NWN | A1 | F4 |
| NWN | A2 | F4 |
| NWS | A1 | F4 |
| NWS | A2 | F4 |
| NWSA | A1 | F5 |
| NWSA | A2 | F5 |
| NXST | A1 | F5 |
| NXST | A2 | F5 |
| OBDC | A1 | F4 |
| OBDC | A2 | F4 |
| OBE | A1 | F2 |
| OBE | A2 | F2 |
| OEC | A1 | F2 |
| OEC | A2 | F2 |
| OGC | A1 | F4 |
| OGC | A2 | F4 |
| ONC | A1 | F5 |
| ONC | A2 | F5 |
| ONIT | A1 | F3 |
| ONIT | A2 | F3 |
| ONT | A1 | F3 |
| ONT | A2 | F3 |
| ORA | A1 | F5 |
| ORA | A2 | F5 |
| OSCR | A1 | F6 |
| OSCR | A2 | F6 |
| OTEX | A1 | F4 |
| OTEX | A2 | F4 |
| PAAS | A1 | F5 |
| PAAS | A2 | F5 |
| PAYC | A1 | F5 |
| PAYC | A2 | F5 |
| PAYO | A1 | F2 |
| PAYO | A2 | F2 |
| PBH | A1 | F4 |
| PBH | A2 | F4 |
| PCRX | A1 | F3 |
| PCRX | A2 | F3 |
| PENN | A1 | F5 |
| PENN | A2 | F5 |
| PESI | A1 | F3 |
| PESI | A2 | F3 |
| PGEN | A1 | F2 |
| PGEN | A2 | F2 |
| PGNY | A1 | F4 |
| PGNY | A2 | F4 |
| PH | A1 | F3 |
| PH | A2 | F3 |
| PK | A1 | F5 |
| PK | A2 | F5 |
| PLMR | A1 | F4 |
| PLMR | A2 | F4 |
| PLNT | A1 | F5 |
| PLNT | A2 | F5 |
| POWI | A1 | F4 |
| POWI | A2 | F4 |
| PR | A1 | F5 |
| PR | A2 | F5 |
| PRCT | A1 | F3 |
| PRCT | A2 | F3 |
| PRI | A1 | F5 |
| PRI | A2 | F5 |
| PRKS | A1 | F3 |
| PRKS | A2 | F3 |
| PRM | A1 | F4 |
| PRM | A2 | F4 |
| PRMB | A1 | F5 |
| PRMB | A2 | F5 |
| PRSU | A1 | F3 |
| PRSU | A2 | F3 |
| PRVA | A1 | F4 |
| PRVA | A2 | F4 |
| PTC | A1 | F5 |
| PTC | A2 | F5 |
| PTLO | A1 | F2 |
| PTLO | A2 | F2 |
| PTON | A1 | F2 |
| PTON | A2 | F2 |
| PTRN | A1 | F4 |
| PTRN | A2 | F4 |
| PVLA | A1 | F4 |
| PVLA | A2 | F4 |
| PZZA | A1 | F3 |
| PZZA | A2 | F3 |
| QCOM | A1 | F3 |
| QCOM | A2 | F3 |
| QGEN | A1 | F6 |
| QGEN | A2 | F6 |
| QNST | A1 | F3 |
| QNST | A2 | F3 |
| RCUS | A1 | F4 |
| RCUS | A2 | F4 |
| RDN | A1 | F5 |
| RDN | A2 | F5 |
| RDVT | A1 | F3 |
| RDVT | A2 | F3 |
| REAX | A1 | F3 |
| REAX | A2 | F3 |
| RELY | A1 | F6 |
| RELY | A2 | F6 |
| REPX | A1 | F3 |
| REPX | A2 | F3 |
| RGLD | A1 | F5 |
| RGLD | A2 | F5 |
| RGR | A1 | F3 |
| RGR | A2 | F3 |
| RL | A1 | F5 |
| RL | A2 | F5 |
| RLAY | A1 | F4 |
| RLAY | A2 | F4 |
| RLJ | A1 | F3 |
| RLJ | A2 | F3 |
| ROCK | A1 | F3 |
| ROCK | A2 | F3 |
| ROK | A1 | F5 |
| ROK | A2 | F5 |
| ROOT | A1 | F3 |
| ROOT | A2 | F3 |
| RPD | A1 | F3 |
| RPD | A2 | F3 |
| RUN | A1 | F2 |
| RUN | A2 | F2 |
| RVMD | A1 | F5 |
| RVMD | A2 | F5 |
| RYN | A1 | F5 |
| RYN | A2 | F5 |
| SBGI | A1 | F3 |
| SBGI | A2 | F3 |
| SCSC | A1 | F3 |
| SCSC | A2 | F3 |
| SDGR | A1 | F3 |
| SDGR | A2 | F3 |
| SEG | A1 | F3 |
| SEG | A2 | F3 |
| SEI | A1 | F5 |
| SEI | A2 | F5 |
| SEZL | A1 | F5 |
| SEZL | A2 | F5 |
| SGHT | A1 | F2 |
| SGHT | A2 | F2 |
| SHOO | A1 | F5 |
| SHOO | A2 | F5 |
| SITM | A1 | F5 |
| SITM | A2 | F5 |
| SKT | A1 | F4 |
| SKT | A2 | F4 |
| SLF | A1 | F4 |
| SLF | A2 | F4 |
| SMA | A1 | F4 |
| SMA | A2 | F4 |
| SNAP | A1 | F2 |
| SNAP | A2 | F2 |
| SNDA | A1 | F3 |
| SNDA | A2 | F3 |
| SO | A1 | F3 |
| SO | A2 | F3 |
| SOBO | A1 | F4 |
| SOBO | A2 | F4 |
| SONY | A1 | F3 |
| SONY | A2 | F3 |
| SPHR | A1 | F5 |
| SPHR | A2 | F5 |
| SRE | A1 | F3 |
| SRE | A2 | F3 |
| SRI | A1 | F2 |
| SRI | A2 | F2 |
| STAA | A1 | F3 |
| STAA | A2 | F3 |
| STE | A1 | F5 |
| STE | A2 | F5 |
| STRA | A1 | F3 |
| STRA | A2 | F3 |
| SVC | A1 | F2 |
| SVC | A2 | F2 |
| TAP | A1 | F5 |
| TAP | A2 | F5 |
| TASK | A1 | F2 |
| TASK | A2 | F2 |
| TBI | A1 | F2 |
| TBI | A2 | F2 |
| TDAY | A1 | F2 |
| TDAY | A2 | F2 |
| TFX | A1 | F5 |
| TFX | A2 | F5 |
| TGB | A1 | F2 |
| TGB | A2 | F2 |
| TGLS | A1 | F3 |
| TGLS | A2 | F3 |
| TIC | A1 | F4 |
| TIC | A2 | F4 |
| TIGO | A1 | F5 |
| TIGO | A2 | F5 |
| TKNO | A1 | F2 |
| TKNO | A2 | F2 |
| TKO | A1 | F5 |
| TKO | A2 | F5 |
| TPC | A1 | F4 |
| TPC | A2 | F4 |
| TPL | A1 | F5 |
| TPL | A2 | F5 |
| TPR | A1 | F6 |
| TPR | A2 | F6 |
| TRGP | A1 | F3 |
| TRGP | A2 | F3 |
| TRIP | A1 | F3 |
| TRIP | A2 | F3 |
| TRLV | A1 | F3 |
| TRLV | A2 | F3 |
| TRP | A1 | F3 |
| TRP | A2 | F3 |
| TS | A1 | F5 |
| TS | A2 | F5 |
| TTAM | A1 | F4 |
| TTAM | A2 | F4 |
| U | A1 | F6 |
| U | A2 | F6 |
| UHAL | A1 | F3 |
| UHAL | A2 | F3 |
| UHALB | A1 | F3 |
| UHALB | A2 | F3 |
| USFD | A1 | F5 |
| USFD | A2 | F5 |
| USPH | A1 | F3 |
| USPH | A2 | F3 |
| UUUU | A1 | F2 |
| UUUU | A2 | F2 |
| VCEL | A1 | F4 |
| VCEL | A2 | F4 |
| VCTR | A1 | F5 |
| VCTR | A2 | F5 |
| VCYT | A1 | F5 |
| VCYT | A2 | F5 |
| VECO | A1 | F4 |
| VECO | A2 | F4 |
| VEL | A1 | F3 |
| VEL | A2 | F3 |
| VERX | A1 | F3 |
| VERX | A2 | F3 |
| VIAV | A1 | F5 |
| VIAV | A2 | F5 |
| VIR | A1 | F3 |
| VIR | A2 | F3 |
| VIRT | A1 | F5 |
| VIRT | A2 | F5 |
| VISN | A1 | F2 |
| VISN | A2 | F2 |
| VMD | A1 | F3 |
| VMD | A2 | F3 |
| VMRK | A1 | F5 |
| VMRK | A2 | F5 |
| VNT | A1 | F4 |
| VNT | A2 | F4 |
| VRSK | A1 | F5 |
| VRSK | A2 | F5 |
| VSEC | A1 | F5 |
| VSEC | A2 | F5 |
| VTRS | A1 | F6 |
| VTRS | A2 | F6 |
| VYX | A1 | F2 |
| VYX | A2 | F2 |
| WBI | A1 | F3 |
| WBI | A2 | F3 |
| WD | A1 | F3 |
| WD | A2 | F3 |
| WEN | A1 | F2 |
| WEN | A2 | F2 |
| WMS | A1 | F5 |
| WMS | A2 | F5 |
| WOLF | A1 | F3 |
| WOLF | A2 | F3 |
| WRBY | A1 | F5 |
| WRBY | A2 | F5 |
| WTS | A1 | F5 |
| WTS | A2 | F5 |
| WU | A1 | F2 |
| WU | A2 | F2 |
| WW | A1 | F3 |
| WW | A2 | F3 |
| XERS | A1 | F3 |
| XERS | A2 | F3 |
| XPER | A1 | F2 |
| XPER | A2 | F2 |
| XRN | A1 | F3 |
| XRN | A2 | F3 |
| Z | A1 | F5 |
| Z | A2 | F5 |
| ZG | A1 | F3 |
| ZG | A2 | F3 |
| ZLAB | A1 | F4 |
| ZLAB | A2 | F4 |
| ZTS | A1 | F6 |
| ZTS | A2 | F6 |

## Exploration book tonight (47; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| AAP | SS | 2026-11-06T00:00:00.000 | 51.00 | 6.45 | +10.98% | 1,428.68 | F6 |
| AG | SS | 2026-11-06T00:00:00.000 | 15.50 | 0.88 | +5.16% | 429.70 | F6 |
| ALB | SS | 2026-11-06T00:00:00.000 | 95.00 | 6.09 | +5.60% | 2,591.18 | F6 |
| APA | SS | 2026-11-06T00:00:00.000 | 44.50 | 2.36 | +4.48% | 1,057.66 | F6 |
| APP | SS | 2026-11-06T00:00:00.000 | 272.50 | 39.48 | +14.20% | 9,166.75 | F3 |
| APP | IC | 2026-11-06T00:00:00.000 | 272.50 | 37.86 | +13.54% | 4,964.18 | F3 |
| BROS | SS | 2026-11-06T00:00:00.000 | 44.00 | 5.41 | +11.18% | 1,205.77 | F6 |
| CAH | SS | 2026-11-06T00:00:00.000 | 260.00 | 14.45 | +4.87% | 3,815.51 | F3 |
| CAVA | SS | 2026-11-06T00:00:00.000 | 62.00 | 6.75 | +10.17% | 2,044.17 | F6 |
| CDE | SS | 2026-11-06T00:00:00.000 | 14.50 | 1.10 | +6.92% | 428.44 | F6 |
| CF | SS | 2026-11-06T00:00:00.000 | 110.00 | 6.26 | +5.07% | 2,317.24 | F6 |
| CHYM | SS | 2026-11-20T00:00:00.000 | 30.00 | 3.78 | +12.07% | 723.85 | PASS |
| CHYM | IC | 2026-11-20T00:00:00.000 | 30.00 | 3.53 | +10.92% | 397.05 | PASS |
| CI | SS | 2026-11-06T00:00:00.000 | 305.00 | 16.48 | +4.92% | 4,948.48 | F3 |
| COHR | SS | 2026-11-06T00:00:00.000 | 195.00 | 21.30 | +10.22% | 7,765.78 | F6 |
| CORZ | SS | 2026-11-06T00:00:00.000 | 12.50 | 1.42 | +10.79% | 550.14 | F7 |
| ELF | SS | 2026-11-06T00:00:00.000 | 114.00 | 12.94 | +10.15% | 3,001.49 | F6 |
| EW | SS | 2026-11-20T00:00:00.000 | 100.00 | 6.92 | +6.66% | 1,512.97 | F3 |
| EW | IC | 2026-11-20T00:00:00.000 | 100.00 | 6.32 | +5.59% | 867.84 | F3 |
| EXPE | SS | 2026-11-06T00:00:00.000 | 320.00 | 31.08 | +9.17% | 7,796.22 | F6 |
| FIG | SS | 2026-11-06T00:00:00.000 | 22.00 | 2.80 | +12.35% | 794.69 | F7 |
| FOUR | SS | 2026-11-20T00:00:00.000 | 45.00 | 7.26 | +15.71% | 1,381.97 | F7 |
| FOUR | IC | 2026-11-20T00:00:00.000 | 45.00 | 6.63 | +13.61% | 836.99 | F7 |
| FSLY | SS | 2026-11-06T00:00:00.000 | 21.00 | 3.84 | +17.08% | 993.00 | F6 |
| INSW | SS | 2026-11-20T00:00:00.000 | 100.00 | 12.09 | +11.36% | 2,636.77 | F6 |
| IRM | SS | 2026-11-06T00:00:00.000 | 119.00 | 5.85 | +4.53% | 2,015.83 | F6 |
| JOBY | SS | 2026-11-06T00:00:00.000 | 5.00 | 0.48 | +8.86% | 167.15 | F2 |
| KMB | SS | 2026-11-06T00:00:00.000 | 109.00 | 3.12 | +2.43% | 1,648.02 | F6 |
| LMND | SS | 2026-11-06T00:00:00.000 | 46.00 | 5.69 | +11.95% | 1,676.42 | F7 |
| MSI | SS | 2026-11-20T00:00:00.000 | 490.00 | 34.24 | +6.51% | 6,704.64 | F3 |
| MSI | IC | 2026-11-20T00:00:00.000 | 490.00 | 30.84 | +5.53% | 3,915.53 | F3 |
| NTR | SS | 2026-11-06T00:00:00.000 | 72.00 | 3.41 | +4.47% | 1,215.30 | F6 |
| OSCR | SS | 2026-11-06T00:00:00.000 | 35.00 | 3.65 | +9.54% | 1,185.95 | F6 |
| PTON | SS | 2026-11-06T00:00:00.000 | 5.50 | 0.70 | +11.29% | 155.11 | F2 |
| QGEN | SS | 2026-11-20T00:00:00.000 | 50.00 | 0.98 | +1.75% | 237.11 | F6 |
| RELY | SS | 2026-11-20T00:00:00.000 | 27.00 | 4.49 | +14.95% | 792.78 | F6 |
| SHAK | SS | 2026-11-06T00:00:00.000 | 73.00 | 8.75 | +11.57% | 2,137.15 | PASS |
| SNAP | SS | 2026-11-06T00:00:00.000 | 6.00 | 0.79 | +13.00% | 218.68 | F2 |
| SNAP | IC | 2026-11-06T00:00:00.000 | 6.00 | 0.75 | +12.01% | 124.78 | F2 |
| TPR | SS | 2026-11-06T00:00:00.000 | 126.00 | 12.25 | +8.98% | 2,795.34 | F6 |
| TRIP | SS | 2026-11-06T00:00:00.000 | 10.00 | 1.23 | +10.73% | 290.36 | F3 |
| U | SS | 2026-11-06T00:00:00.000 | 42.00 | 6.13 | +13.69% | 1,461.93 | F6 |
| VTRS | SS | 2026-11-20T00:00:00.000 | 19.00 | 1.62 | +6.75% | 270.80 | F6 |
| WEN | SS | 2026-11-06T00:00:00.000 | 7.50 | 0.48 | +3.83% | 128.26 | F2 |
| WOLF | SS | 2026-11-06T00:00:00.000 | 23.00 | 2.98 | +12.46% | 1,025.49 | F3 |
| ZTS | SS | 2026-11-20T00:00:00.000 | 90.00 | 8.80 | +9.25% | 1,678.84 | F6 |
| ZTS | IC | 2026-11-20T00:00:00.000 | 90.00 | 8.08 | +8.29% | 1,192.41 | F6 |

## Graded today (35)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| SN | A1 | IC | champion | -0.17% | -35.25 | 2 | no |
| SWKS | A1 | SS | champion | -2.15% | -183.87 | 1 | no |
| SN | A1 | SS | champion | +0.93% | 195.18 | 1 | no |
| XYZ | A1 | SS | champion | -5.64% | -428.18 | 1 | no |
| SN | A2 | IC | champion | -0.17% | -35.25 | 2 | no |
| SN | A2 | SS | champion | +0.93% | 195.18 | 1 | no |
| AIG | A1 | SS | exploration | +0.08% | 6.16 | 1 | no |
| ALAB | A1 | SS | exploration | +3.29% | 768.90 | 1 | no |
| BTU | A1 | SS | exploration | -14.22% | -294.56 | 2 | no |
| CAR | A1 | SS | exploration | -1.85% | -201.76 | 2 | no |
| CPNG | A1 | SS | exploration | -1.70% | -26.03 | 1 | no |
| CRCL | A1 | SS | exploration | +3.51% | 264.35 | 1 | no |
| DDOG | A1 | SS | exploration | +2.18% | 479.31 | 1 | no |
| DDOG | A1 | IC | exploration | +1.70% | 373.44 | 1 | no |
| EMR | A1 | SS | exploration | +0.00% | 0.83 | 1 | no |
| HL | A1 | SS | exploration | -6.17% | -81.43 | 1 | no |
| HUT | A1 | SS | exploration | -4.24% | -269.63 | 1 | no |
| KHC | A1 | SS | exploration | -1.29% | -31.58 | 1 | no |
| MOS | A1 | SS | exploration | -0.26% | -4.74 | 1 | no |
| MOS | A1 | IC | exploration | -0.86% | -15.83 | 2 | no |
| OUST | A1 | SS | exploration | +1.63% | 47.19 | 1 | no |
| RIOT | A1 | SS | exploration | +1.44% | 20.26 | 1 | no |
| SEDG | A1 | SS | exploration | +3.56% | 116.92 | 1 | no |
| SGHC | A1 | SS | exploration | -0.96% | -10.79 | 2 | no |
| SMCI | A1 | SS | exploration | +6.80% | 214.55 | 1 | no |
| SN | A1 | SS | exploration | +0.93% | 195.18 | 1 | no |
| SN | A1 | IC | exploration | -0.17% | -35.25 | 2 | no |
| SU | A1 | SS | exploration | -0.50% | -37.75 | 1 | no |
| SWKS | A1 | SS | exploration | -2.15% | -183.87 | 1 | no |
| TOST | A1 | SS | exploration | +3.01% | 100.83 | 1 | no |
| TOST | A1 | IC | exploration | +2.37% | 79.59 | 2 | no |
| UNM | A1 | SS | exploration | -11.01% | -1,002.03 | 2 | no |
| W | A1 | SS | exploration | -1.51% | -168.64 | 1 | no |
| W | A1 | IC | exploration | -1.95% | -217.34 | 2 | no |
| XYZ | A1 | SS | exploration | -5.64% | -428.18 | 1 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 7 | 5 | +0.66% | 1.00 | 233.18 |
| sa-1.0 | champion | A1 | SS | 27 | 12 | -0.43% | -0.90 | -1,573.61 |
| sa-1.0 | champion | A2 | IC | 7 | 5 | +0.66% | 1.00 | 233.18 |
| sa-1.0 | champion | A2 | SS | 21 | 11 | +0.04% | 0.06 | -434.24 |
| sa-1.0 | exploration | A1 | IC | 43 | 18 | -1.34% | -1.97 | -4,123.48 |
| sa-1.0 | exploration | A1 | SS | 189 | 21 | -0.92% | -3.81 | -12,165.64 |

Ledger: emitted 4 (skipped 0), exploration 47 (skipped 0), graded 35; ledger open.

## S-B state
Gate (2026-11-04, from 2026-11-03 closes): SPY ON (VIX 20.83, VIX3M 21.27, X 20.83 vs median 17.055) · QQQ ON (VIX 20.83, VIX3M 21.27, X 30.53 vs median 24.665)

Next session (2026-11-05, from 2026-11-04 closes): SPY UNKNOWN:null input at 2026-11-04 · QQQ UNKNOWN:null input at 2026-11-04

CBOE refresh: ok through 2026-11-04; index-vol through 2026-11-04

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
Universe: 2095 names.
Borrow snapshot: 2026-11-04 (the session's own); fee known for 2088 names.
Bull counts: 0:532, 1:749, 2:502, 3:258, 4:49, 5:5, 6:0, 7:0, 8:0
Bear counts: 0:850, 1:791, 2:297, 3:121, 4:32, 5:4, 6:0, 7:0, 8:0

### LONG (170)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3 | 0 | no | x | x |  |  |  | x |  |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| ABM | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| ACEL | 5 | 0 | yes | x | x |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| AER | 4 | 0 | yes | x | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| ALRM | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| ALSN | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMAL | 3 | 0 | no | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| AMX | 4 | 0 | no |  | x |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| APOG | 3 | 0 | yes | x |  |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| ASB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| ATMU | 3 | 0 | no |  | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  |  |
| AVAH | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| AVY | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AWR | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BCPC | 4 | 0 | no | x |  |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| BFA | 3 | 0 | no | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BFST | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| BIIB | 4 | 0 | no | x | x |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| BJ | 5 | 0 | no | x | x |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| BLBD | 3 | 0 | yes |  | x | x |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BLK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BOOT | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BY | 3 | 0 | no | x | x |  |  |  |  |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| CAH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CCK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CCNE | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? | ? |  |  |  | ? |  |  |  |  |  |
| CHE | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| CHT | 5 | 0 | no | x | x |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| CL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CNC | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| COLM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| COST | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| CPB | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CPK | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| CRBG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CSL | 4 | 0 | no |  |  |  |  | x | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| CUBE | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| CUBI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DCOM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DLR | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DRH | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| ECL | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EFC | 3 | 0 | yes |  | x | x | x |  |  | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| EG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EHC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EPC | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| EQH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ESNT | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| EXLS | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EXR | 3 | 0 | yes | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| FAST | 3 | 0 | no | x | x |  |  |  |  |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| FIVE | 4 | 0 | yes | x | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| FIZZ | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| FMBH | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| FMS | 3 | 0 | no |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| FMX | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| FTS | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  | x |
| FUL | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| GBX | 3 | 0 | yes |  | x | x | x |  |  | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| GFF | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  |  |  |  |  |  | x |
| GIC | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| GLBE | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| GLPI | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| GM | 3 | 0 | no | x |  |  | x |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| GWW | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| HCI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HCSG | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HEIA | 3 | 0 | no |  |  |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HG | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HGTY | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HLT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HMC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| HMN | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  | ? | ? |  |  |  | ? |  |  |  |  |  |
| HON | 4 | 0 | yes |  |  |  |  | x | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| HZO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| ICE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ICFI | 3 | 0 | yes | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| IDT | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| INTA | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| IR | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| IVZ | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| JEF | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| JXN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| KO | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| KYIV | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| LFST | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| LH | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| LIN | 3 | 0 | no | x |  |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| LKFT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? | ? |  |  |  |  |  |  |  |  |  |
| LTC | 3 | 0 | no | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  | x |
| LUV | 3 | 0 | no |  | x |  |  | x | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| MA | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| MAS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MBWM | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| MCBS | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| MCK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MCO | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MDLZ | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MET | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MGRC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| MIDD | 3 | 0 | no |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| MRSH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MSCI | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| MT | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| NATL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| NBTB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| NDAQ | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| NGG | 3 | 0 | no |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| NIQ | 3 | 0 | yes | x | x |  |  |  | x |  |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| NVS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| NWE | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| NXPI | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| PG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PGR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PLMR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| POR | 4 | 0 | no |  | x | x |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PRSU | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PWP | 3 | 0 | no |  | x | x | x |  |  | ? |  |  | ? |  |  |  |  | ? |  |  |  |  | x |
| R | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RDY | 3 | 0 | yes |  | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| RELX | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| REYN | 4 | 0 | no |  |  |  |  | x | x | x | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| RL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RLJ | 4 | 0 | no | x | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| RNR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ROK | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| RPM | 3 | 0 | no |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| RPRX | 3 | 0 | no | x | x |  |  |  | x |  |  |  |  |  |  |  |  |  |  |  |  |  | x |
| RSG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SAIC | 4 | 0 | no | x | x |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| SBH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| SBUX | 3 | 0 | yes | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| SFBS | 3 | 0 | no |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| SHO | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? | ? |  |  |  | ? |  |  |  |  |  |
| SHW | 3 | 0 | no |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SIGI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| SJM | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SKWD | 4 | 0 | yes | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| SMA | 4 | 0 | no | x | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| SONY | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| STBA | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TAK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| TCBK | 3 | 0 | no |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TDG | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TDS | 3 | 0 | no |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TILE | 4 | 0 | no | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| TOL | 3 | 0 | no |  | x |  |  | x | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| TRMK | 3 | 0 | no |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TW | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TXN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| UE | 3 | 0 | yes |  |  | x | x | x |  | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| UHALB | 3 | 0 | yes |  | x |  | x | x |  | ? |  |  | ? | ? |  |  |  | ? |  |  |  |  |  |
| UTHR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| UVE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| V | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| VLTO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VRSN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VSTS | 3 | 0 | no |  | x |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| VTRS | 4 | 0 | no | x | x |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| WCN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WDFC | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| WM | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WMT | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| WOR | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| WPP | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| WTRG | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| XHR | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| XNCR | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| YELP | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |

### SHORT (59)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ABCL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| ALAB | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| AMD | 0 | 4 | yes |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| ARM | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| ASST | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| BAND | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| BBAR | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  |  | x | x |  |  |  |  |
| BE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| BTU | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  | x |  |  |  | x |
| BXDC | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | ? |  | x |  |  | ? | x |  |  |  |  |
| CAMT | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  |  |  |  |  |  |
| CAR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  |  |  |  |  |  | x |
| CAT | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  | x | x | x |
| CLMT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? | x | x |  |  | ? | x |  |  |  | x |
| CRCL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| CSCO | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| CVE | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| DDOG | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  | x | x |
| DOX | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? |  |  | x |  | x |
| EC | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  |  |
| FIG | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| FLUT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? |  |  |  |  | x |
| FSLR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  | x | x |
| FSLY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| GOOGL | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  | x | x |
| GXO | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  | x |
| IDCC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? |  |  |  |  | x |
| INOD | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  |  |
| INTC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| KLAC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| KMX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| LITE | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| LMND | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? |  |  |  |  | x |
| MDGL | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| MGY | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| MTDR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| NRG | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  |  | x |  |  |  | x |
| NRIX | 0 | 4 | yes |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? | x |  |  |  | x |
| ORCL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| PBI | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x | ? | x |  |  |  |  |
| PLTR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| SCCO | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| SEDG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  |  |  |  |  |  | x |
| SEI | 0 | 4 | yes |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? | x |  |  |  | x |
| SHC | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| SM | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| STRL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  | x | x | x |
| TDW | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| TLN | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| TMDX | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| UNM | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| VG | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| VIST | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| VSAT | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x | x |  | ? |  |  |  |  | x |
| WDS | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | ? |  |  | x | x | ? | x |  |  |  |  |
| WEX | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| WLDN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| WOLF | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  | x |  |
| ZBRA | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |

### VOL (0)
_none_

CONFLICT (logged only, never a basket, DESIGN/110 §3): 86.

Ledger: emitted 229 (skipped 0), graded 467; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
