# S-A daily — 2026-11-03 (S3)

Preflight: WARN — prices.parquet ends 2026-10-30, BEFORE the 2026-11-03 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-10-30, BEFORE the 2026-11-03 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-10-30, BEFORE the 2026-11-03 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (10)
| ticker | variant | structure | expiry | k | k_up | k_dn | credit_entry | credit_net_pct | risk_usd | contracts | entry_tier_max | cap_pass |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PODD | A1 | IC | 2026-11-20T00:00:00.000 | 155.00 | 190.00 | 120.00 | 18.53 | +11.60% | 1,646.93 | 1 | 2 | no |
| SN | A1 | IC | 2026-11-20T00:00:00.000 | 210.00 | 260.00 | 160.00 | 22.72 | +10.21% | 2,728.16 | 1 | 2 | no |
| PODD | A1 | SS | 2026-11-20T00:00:00.000 | 155.00 | — | — | 19.91 | +12.59% | 3,591.95 | 1 | 1 | no |
| SWKS | A1 | SS | 2026-11-20T00:00:00.000 | 85.00 | — | — | 10.56 | +11.80% | 2,150.51 | 1 | 1 | yes |
| SN | A1 | SS | 2026-11-20T00:00:00.000 | 210.00 | — | — | 25.02 | +11.67% | 5,185.62 | 1 | 1 | no |
| XYZ | A1 | SS | 2026-11-06T00:00:00.000 | 76.00 | — | — | 6.94 | +8.92% | 1,832.42 | 1 | 1 | no |
| PODD | A2 | IC | 2026-11-20T00:00:00.000 | 155.00 | 190.00 | 120.00 | 18.53 | +11.60% | 1,646.93 | 1 | 2 | no |
| SN | A2 | IC | 2026-11-20T00:00:00.000 | 210.00 | 260.00 | 160.00 | 22.72 | +10.21% | 2,728.16 | 1 | 2 | no |
| PODD | A2 | SS | 2026-11-20T00:00:00.000 | 155.00 | — | — | 19.91 | +12.59% | 3,591.95 | 1 | 1 | no |
| SN | A2 | SS | 2026-11-20T00:00:00.000 | 210.00 | — | — | 25.02 | +11.67% | 5,185.62 | 1 | 1 | no |

## Suppressed (416)
| ticker | variant | first_fail |
|---|---|---|
| ACEL | A1 | F3 |
| ACEL | A2 | F3 |
| ADNT | A1 | F3 |
| ADNT | A2 | F3 |
| ADUS | A1 | F4 |
| ADUS | A2 | F4 |
| AFG | A1 | F5 |
| AFG | A2 | F5 |
| AIG | A1 | F6 |
| AIG | A2 | F6 |
| AIZ | A1 | F5 |
| AIZ | A2 | F5 |
| ALAB | A1 | F7 |
| ALAB | A2 | F7 |
| ALIT | A1 | F3 |
| ALIT | A2 | F3 |
| AMD | A1 | F3 |
| AMD | A2 | F3 |
| AMGN | A1 | F3 |
| AMGN | A2 | F3 |
| AMWL | A1 | F3 |
| AMWL | A2 | F3 |
| ANDE | A1 | F4 |
| ANDE | A2 | F4 |
| ANET | A1 | F3 |
| ANET | A2 | F3 |
| ANGI | A1 | F2 |
| ANGI | A2 | F2 |
| ARCB | A1 | F4 |
| ARCB | A2 | F4 |
| ASH | A1 | F4 |
| ASH | A2 | F4 |
| ASIX | A1 | F3 |
| ASIX | A2 | F3 |
| ATHM | A1 | F4 |
| ATHM | A2 | F4 |
| ATRC | A1 | F4 |
| ATRC | A2 | F4 |
| ATS | A1 | F3 |
| ATS | A2 | F3 |
| AUDC | A1 | F3 |
| AUDC | A2 | F3 |
| AVA | A1 | F4 |
| AVA | A2 | F4 |
| AVNT | A1 | F4 |
| AVNT | A2 | F4 |
| AVT | A1 | F5 |
| AVT | A2 | F5 |
| BATRA | A1 | F3 |
| BATRA | A2 | F3 |
| BATRK | A1 | F4 |
| BATRK | A2 | F4 |
| BCO | A1 | F5 |
| BCO | A2 | F5 |
| BCRX | A1 | F2 |
| BCRX | A2 | F2 |
| BEPC | A1 | F5 |
| BEPC | A2 | F5 |
| BKNG | A1 | F3 |
| BKNG | A2 | F3 |
| BRKR | A1 | F5 |
| BRKR | A2 | F5 |
| BTU | A1 | F4 |
| BTU | A2 | F4 |
| BXC | A1 | F3 |
| BXC | A2 | F3 |
| BXSL | A1 | F4 |
| BXSL | A2 | F4 |
| CAMT | A1 | F5 |
| CAMT | A2 | F5 |
| CAR | A1 | F4 |
| CAR | A2 | F4 |
| CBLL | A1 | F3 |
| CBLL | A2 | F3 |
| CDW | A1 | F5 |
| CDW | A2 | F5 |
| CHCT | A1 | F3 |
| CHCT | A2 | F3 |
| CHT | A1 | F4 |
| CHT | A2 | F4 |
| CIGI | A1 | F4 |
| CIGI | A2 | F4 |
| COR | A1 | F3 |
| COR | A2 | F3 |
| CPNG | A1 | F6 |
| CPNG | A2 | F6 |
| CRCL | A1 | F7 |
| CRCL | A2 | F7 |
| CRCT | A1 | F2 |
| CRCT | A2 | F2 |
| CRL | A1 | F5 |
| CRL | A2 | F5 |
| CRTO | A1 | F3 |
| CRTO | A2 | F3 |
| CVE | A1 | F3 |
| CVE | A2 | F3 |
| CVS | A1 | F3 |
| CVS | A2 | F3 |
| CWK | A1 | F4 |
| CWK | A2 | F4 |
| CXDO | A1 | F2 |
| CXDO | A2 | F2 |
| DDOG | A1 | F3 |
| DDOG | A2 | F3 |
| DEI | A1 | F2 |
| DEI | A2 | F2 |
| DIN | A1 | F3 |
| DIN | A2 | F3 |
| DNLI | A1 | F4 |
| DNLI | A2 | F4 |
| DRH | A1 | F4 |
| DRH | A2 | F4 |
| DUOL | A1 | F6 |
| DUOL | A2 | F6 |
| ECG | A1 | F5 |
| ECG | A2 | F5 |
| EMR | A1 | F3 |
| EMR | A2 | F3 |
| ESAB | A1 | F5 |
| ESAB | A2 | F5 |
| EVTC | A1 | F3 |
| EVTC | A2 | F3 |
| EXP | A1 | F5 |
| EXP | A2 | F5 |
| FBIN | A1 | F5 |
| FBIN | A2 | F5 |
| FIS | A1 | F6 |
| FIS | A2 | F6 |
| FLOC | A1 | F3 |
| FLOC | A2 | F3 |
| FLUT | A1 | F5 |
| FLUT | A2 | F5 |
| FLYW | A1 | F4 |
| FLYW | A2 | F4 |
| FOA | A1 | F3 |
| FOA | A2 | F3 |
| FRPT | A1 | F5 |
| FRPT | A2 | F5 |
| FRSH | A1 | F5 |
| FRSH | A2 | F5 |
| FSTR | A1 | F3 |
| FSTR | A2 | F3 |
| FTK | A1 | F3 |
| FTK | A2 | F3 |
| GEF | A1 | F4 |
| GEF | A2 | F4 |
| GFS | A1 | F5 |
| GFS | A2 | F5 |
| GIC | A1 | F3 |
| GIC | A2 | F3 |
| GOLF | A1 | F4 |
| GOLF | A2 | F4 |
| GOOD | A1 | F3 |
| GOOD | A2 | F3 |
| GWW | A1 | F3 |
| GWW | A2 | F3 |
| GXO | A1 | F5 |
| GXO | A2 | F5 |
| HCKT | A1 | F3 |
| HCKT | A2 | F3 |
| HL | A1 | F6 |
| HL | A2 | F6 |
| HMN | A1 | F3 |
| HMN | A2 | F3 |
| HRMY | A1 | F4 |
| HRMY | A2 | F4 |
| HURN | A1 | F5 |
| HURN | A2 | F5 |
| HUT | A1 | F7 |
| HUT | A2 | F7 |
| HZO | A1 | F3 |
| HZO | A2 | F3 |
| IFF | A1 | F5 |
| IFF | A2 | F5 |
| IGIC | A1 | F3 |
| IGIC | A2 | F3 |
| INN | A1 | F2 |
| INN | A2 | F2 |
| INNV | A1 | F2 |
| INNV | A2 | F2 |
| IOSP | A1 | F4 |
| IOSP | A2 | F4 |
| IPI | A1 | F3 |
| IPI | A2 | F3 |
| ITUB | A1 | F2 |
| ITUB | A2 | F2 |
| JKHY | A1 | F5 |
| JKHY | A2 | F5 |
| JXN | A1 | F5 |
| JXN | A2 | F5 |
| KAI | A1 | F4 |
| KAI | A2 | F4 |
| KD | A1 | F4 |
| KD | A2 | F4 |
| KHC | A1 | F6 |
| KHC | A2 | F6 |
| KMT | A1 | F4 |
| KMT | A2 | F4 |
| KODK | A1 | F2 |
| KODK | A2 | F2 |
| LAW | A1 | F2 |
| LAW | A2 | F2 |
| LIVN | A1 | F4 |
| LIVN | A2 | F4 |
| LMB | A1 | F3 |
| LMB | A2 | F3 |
| LTC | A1 | F4 |
| LTC | A2 | F4 |
| MCD | A1 | F3 |
| MCD | A2 | F3 |
| MCY | A1 | F4 |
| MCY | A2 | F4 |
| MDLN | A1 | F5 |
| MDLN | A2 | F5 |
| METC | A1 | F2 |
| METC | A2 | F2 |
| MFA | A1 | F2 |
| MFA | A2 | F2 |
| MITT | A1 | F2 |
| MITT | A2 | F2 |
| MLM | A1 | F5 |
| MLM | A2 | F5 |
| MOD | A1 | F5 |
| MOD | A2 | F5 |
| MOS | A1 | F6 |
| MOS | A2 | F6 |
| MQ | A1 | F3 |
| MQ | A2 | F3 |
| MSGE | A1 | F4 |
| MSGE | A2 | F4 |
| MTDR | A1 | F5 |
| MTDR | A2 | F5 |
| MTRN | A1 | F5 |
| MTRN | A2 | F5 |
| MTW | A1 | F3 |
| MTW | A2 | F3 |
| NATL | A1 | F4 |
| NATL | A2 | F4 |
| NICE | A1 | F5 |
| NICE | A2 | F5 |
| NNN | A1 | F5 |
| NNN | A2 | F5 |
| NOMD | A1 | F3 |
| NOMD | A2 | F3 |
| NVCT | A1 | F3 |
| NVCT | A2 | F3 |
| NVGS | A1 | F3 |
| NVGS | A2 | F3 |
| NVO | A1 | F3 |
| NVO | A2 | F3 |
| NVTS | A1 | F2 |
| NVTS | A2 | F2 |
| NYT | A1 | F5 |
| NYT | A2 | F5 |
| OC | A1 | F5 |
| OC | A2 | F5 |
| OHI | A1 | F5 |
| OHI | A2 | F5 |
| OPCH | A1 | F5 |
| OPCH | A2 | F5 |
| OPLN | A1 | F4 |
| OPLN | A2 | F4 |
| OPRT | A1 | F3 |
| OPRT | A2 | F3 |
| OUST | A1 | F6 |
| OUST | A2 | F6 |
| OVV | A1 | F6 |
| OVV | A2 | F6 |
| PACS | A1 | F4 |
| PACS | A2 | F4 |
| PARR | A1 | F5 |
| PARR | A2 | F5 |
| PAYP | A1 | F4 |
| PAYP | A2 | F4 |
| PCOR | A1 | F5 |
| PCOR | A2 | F5 |
| PFGC | A1 | F5 |
| PFGC | A2 | F5 |
| PRGO | A1 | F4 |
| PRGO | A2 | F4 |
| PRIM | A1 | F5 |
| PRIM | A2 | F5 |
| PRU | A1 | F5 |
| PRU | A2 | F5 |
| PSTL | A1 | F3 |
| PSTL | A2 | F3 |
| Q | A1 | F5 |
| Q | A2 | F5 |
| QDEL | A1 | F3 |
| QDEL | A2 | F3 |
| QURE | A1 | F3 |
| QURE | A2 | F3 |
| RAL | A1 | F5 |
| RAL | A2 | F5 |
| REYN | A1 | F4 |
| REYN | A2 | F4 |
| RIOT | A1 | F7 |
| RIOT | A2 | F7 |
| RPC | A1 | F2 |
| RPC | A2 | F2 |
| RPRX | A1 | F5 |
| RPRX | A2 | F5 |
| RRR | A1 | F4 |
| RRR | A2 | F4 |
| RSVR | A1 | F2 |
| RSVR | A2 | F2 |
| RVLV | A1 | F3 |
| RVLV | A2 | F3 |
| RYAM | A1 | F2 |
| RYAM | A2 | F2 |
| SAFE | A1 | F3 |
| SAFE | A2 | F3 |
| SDRL | A1 | F4 |
| SDRL | A2 | F4 |
| SEDG | A1 | F6 |
| SEDG | A2 | F6 |
| SFL | A1 | F3 |
| SFL | A2 | F3 |
| SGHC | A1 | F4 |
| SGHC | A2 | F4 |
| SHLS | A1 | F2 |
| SHLS | A2 | F2 |
| SKY | A1 | F5 |
| SKY | A2 | F5 |
| SLRC | A1 | F3 |
| SLRC | A2 | F3 |
| SM | A1 | F5 |
| SM | A2 | F5 |
| SMCI | A1 | F7 |
| SMCI | A2 | F7 |
| SMG | A1 | F5 |
| SMG | A2 | F5 |
| SOLS | A1 | F5 |
| SOLS | A2 | F5 |
| SPT | A1 | F3 |
| SPT | A2 | F3 |
| SSRM | A1 | F5 |
| SSRM | A2 | F5 |
| SU | A1 | F3 |
| SU | A2 | F3 |
| SWIM | A1 | F2 |
| SWIM | A2 | F2 |
| SWK | A1 | F5 |
| SWK | A2 | F5 |
| SWKS | A2 | A2_sector |
| SWX | A1 | F5 |
| SWX | A2 | F5 |
| TALO | A1 | F5 |
| TALO | A2 | F5 |
| TFPM | A1 | F4 |
| TFPM | A2 | F4 |
| TKR | A1 | F5 |
| TKR | A2 | F5 |
| TOST | A1 | F6 |
| TOST | A2 | F6 |
| TREE | A1 | F3 |
| TREE | A2 | F3 |
| TREX | A1 | F5 |
| TREX | A2 | F5 |
| TRIN | A1 | F3 |
| TRIN | A2 | F3 |
| TRMB | A1 | F5 |
| TRMB | A2 | F5 |
| TRMD | A1 | F5 |
| TRMD | A2 | F5 |
| TRNS | A1 | F3 |
| TRNS | A2 | F3 |
| TSLX | A1 | F3 |
| TSLX | A2 | F3 |
| TWIN | A1 | F3 |
| TWIN | A2 | F3 |
| TX | A1 | F4 |
| TX | A2 | F4 |
| UBER | A1 | F3 |
| UBER | A2 | F3 |
| UFCS | A1 | F3 |
| UFCS | A2 | F3 |
| UFPT | A1 | F4 |
| UFPT | A2 | F4 |
| UNM | A1 | F6 |
| UNM | A2 | F6 |
| URGN | A1 | F3 |
| URGN | A2 | F3 |
| USNA | A1 | F3 |
| USNA | A2 | F3 |
| UTHR | A1 | F5 |
| UTHR | A2 | F5 |
| VAC | A1 | F4 |
| VAC | A2 | F4 |
| VET | A1 | F3 |
| VET | A2 | F3 |
| VGNT | A1 | F4 |
| VGNT | A2 | F4 |
| VPG | A1 | F3 |
| VPG | A2 | F3 |
| VRDN | A1 | F5 |
| VRDN | A2 | F5 |
| VRNS | A1 | F5 |
| VRNS | A2 | F5 |
| VSH | A1 | F5 |
| VSH | A2 | F5 |
| W | A1 | F6 |
| W | A2 | F6 |
| WLK | A1 | F5 |
| WLK | A2 | F5 |
| WTRG | A1 | F5 |
| WTRG | A2 | F5 |
| XPEL | A1 | F3 |
| XPEL | A2 | F3 |
| XYZ | A2 | A2_sector |
| YOU | A1 | F5 |
| YOU | A2 | F5 |
| ZBH | A1 | F5 |
| ZBH | A2 | F5 |
| ZVRA | A1 | F3 |
| ZVRA | A2 | F3 |

## Exploration book tonight (36; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| AIG | SS | 2026-11-06T00:00:00.000 | 81.00 | 3.04 | +3.33% | 1,074.54 | F6 |
| ALAB | SS | 2026-11-06T00:00:00.000 | 235.00 | 30.76 | +12.74% | 10,600.18 | F7 |
| BTU | SS | 2026-11-06T00:00:00.000 | 21.00 | 1.87 | +8.26% | 552.07 | F4 |
| CAR | SS | 2026-11-06T00:00:00.000 | 109.00 | 10.93 | +9.20% | 3,761.49 | F4 |
| CPNG | SS | 2026-11-06T00:00:00.000 | 15.50 | 1.48 | +9.12% | 397.24 | F6 |
| CRCL | SS | 2026-11-06T00:00:00.000 | 75.00 | 8.27 | +10.77% | 2,814.41 | F7 |
| CVE | SS | 2026-11-20T00:00:00.000 | 31.00 | 2.55 | +8.04% | 546.21 | F3 |
| DDOG | SS | 2026-11-06T00:00:00.000 | 220.00 | 32.17 | +14.27% | 8,010.66 | F3 |
| DDOG | IC | 2026-11-06T00:00:00.000 | 220.00 | 31.24 | +13.78% | 4,375.89 | F3 |
| DUOL | SS | 2026-11-06T00:00:00.000 | 127.00 | 19.03 | +13.62% | 4,022.68 | F6 |
| EMR | SS | 2026-11-06T00:00:00.000 | 165.00 | 9.30 | +4.79% | 2,466.98 | F3 |
| FIS | SS | 2026-11-06T00:00:00.000 | 39.00 | 3.04 | +7.31% | 795.13 | F6 |
| HL | SS | 2026-11-06T00:00:00.000 | 13.00 | 1.01 | +6.78% | 374.81 | F6 |
| HL | IC | 2026-11-06T00:00:00.000 | 13.00 | 0.98 | +6.45% | 252.43 | F6 |
| HUT | SS | 2026-11-06T00:00:00.000 | 63.00 | 9.58 | +14.55% | 3,444.89 | F7 |
| KHC | SS | 2026-11-06T00:00:00.000 | 24.50 | 1.04 | +3.96% | 410.61 | F6 |
| MOS | SS | 2026-11-06T00:00:00.000 | 18.50 | 1.35 | +6.86% | 469.28 | F6 |
| MOS | IC | 2026-11-06T00:00:00.000 | 18.50 | 1.27 | +6.22% | 272.91 | F6 |
| OUST | SS | 2026-11-06T00:00:00.000 | 29.00 | 4.76 | +15.42% | 1,291.83 | F6 |
| OVV | SS | 2026-11-20T00:00:00.000 | 65.00 | 5.73 | +7.98% | 1,179.78 | F6 |
| PODD | SS | 2026-11-20T00:00:00.000 | 155.00 | 19.91 | +12.59% | 3,591.95 | PASS |
| PODD | IC | 2026-11-20T00:00:00.000 | 155.00 | 18.53 | +11.60% | 1,646.93 | PASS |
| RIOT | SS | 2026-11-06T00:00:00.000 | 14.00 | 2.42 | +16.86% | 770.23 | F7 |
| SEDG | SS | 2026-11-06T00:00:00.000 | 33.00 | 4.43 | +12.50% | 1,372.04 | F6 |
| SGHC | SS | 2026-11-20T00:00:00.000 | 11.00 | 1.53 | +12.39% | 290.14 | F4 |
| SMCI | SS | 2026-11-06T00:00:00.000 | 31.50 | 4.53 | +14.19% | 1,221.75 | F7 |
| SN | SS | 2026-11-20T00:00:00.000 | 210.00 | 25.02 | +11.67% | 5,185.62 | PASS |
| SN | IC | 2026-11-20T00:00:00.000 | 210.00 | 22.72 | +10.21% | 2,728.16 | PASS |
| SU | SS | 2026-11-06T00:00:00.000 | 75.00 | 3.12 | +3.94% | 1,201.87 | F3 |
| SWKS | SS | 2026-11-20T00:00:00.000 | 85.00 | 10.56 | +11.80% | 2,150.51 | PASS |
| TOST | SS | 2026-11-06T00:00:00.000 | 33.50 | 3.52 | +10.04% | 865.51 | F6 |
| TOST | IC | 2026-11-06T00:00:00.000 | 33.50 | 3.33 | +9.30% | 466.97 | F6 |
| UNM | SS | 2026-11-20T00:00:00.000 | 92.50 | 8.40 | +8.89% | 1,481.14 | F6 |
| W | SS | 2026-11-06T00:00:00.000 | 112.00 | 13.57 | +11.62% | 3,634.22 | F6 |
| W | IC | 2026-11-06T00:00:00.000 | 112.00 | 13.12 | +11.14% | 2,087.80 | F6 |
| XYZ | SS | 2026-11-06T00:00:00.000 | 76.00 | 6.94 | +8.92% | 1,832.42 | PASS |

## Graded today (27)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| DT | A1 | SS | champion | -3.52% | -193.97 | 1 | no |
| ON | A1 | SS | champion | +2.09% | 146.71 | 1 | no |
| FISV | A1 | SS | champion | -0.23% | -11.98 | 1 | no |
| AEHR | A1 | SS | exploration | -8.13% | -418.19 | 2 | no |
| APO | A1 | SS | exploration | -1.70% | -203.28 | 1 | no |
| CLX | A1 | SS | exploration | -0.62% | -56.05 | 1 | no |
| CLX | A1 | IC | exploration | -1.05% | -94.42 | 1 | no |
| DOCN | A1 | SS | exploration | +3.06% | 274.70 | 1 | no |
| DT | A1 | SS | exploration | -3.52% | -193.97 | 1 | no |
| FANG | A1 | SS | exploration | -0.97% | -192.57 | 2 | no |
| FANG | A1 | IC | exploration | -1.37% | -273.62 | 2 | no |
| FISV | A1 | SS | exploration | -0.23% | -11.98 | 1 | no |
| FN | A1 | SS | exploration | -1.80% | -566.23 | 1 | no |
| FN | A1 | IC | exploration | -2.10% | -661.82 | 1 | no |
| HLF | A1 | SS | exploration | -2.77% | -36.79 | 1 | no |
| HNGE | A1 | SS | exploration | +0.57% | 66.29 | 1 | no |
| LSCC | A1 | SS | exploration | -4.51% | -430.18 | 1 | no |
| LSCC | A1 | IC | exploration | -5.30% | -505.74 | 1 | no |
| MTCH | A1 | SS | exploration | -0.50% | -21.16 | 1 | no |
| MTCH | A1 | IC | exploration | -1.97% | -82.92 | 1 | no |
| O | A1 | SS | exploration | -0.15% | -8.68 | 1 | no |
| ON | A1 | SS | exploration | +2.09% | 146.71 | 1 | no |
| ROKU | A1 | SS | exploration | +0.54% | 83.34 | 1 | no |
| ROKU | A1 | IC | exploration | -0.03% | -4.66 | 2 | no |
| TEVA | A1 | SS | exploration | +0.02% | 0.83 | 1 | no |
| UPST | A1 | SS | exploration | +3.37% | 71.94 | 1 | no |
| WMB | A1 | SS | exploration | -0.07% | -4.72 | 1 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 6 | 4 | +0.80% | 0.99 | 268.43 |
| sa-1.0 | champion | A1 | SS | 24 | 11 | -0.20% | -0.40 | -1,156.73 |
| sa-1.0 | champion | A2 | IC | 6 | 4 | +0.80% | 0.99 | 268.43 |
| sa-1.0 | champion | A2 | SS | 20 | 10 | -0.01% | -0.01 | -629.42 |
| sa-1.0 | exploration | A1 | IC | 38 | 17 | -1.54% | -2.10 | -4,308.10 |
| sa-1.0 | exploration | A1 | SS | 165 | 20 | -0.90% | -3.24 | -11,639.13 |

Ledger: emitted 10 (skipped 0), exploration 36 (skipped 0), graded 27; ledger open.

## S-B state
Gate (2026-11-03, from 2026-11-02 closes): SPY ON (VIX 21.15, VIX3M 21.6, X 21.15 vs median 16.89) · QQQ ON (VIX 21.15, VIX3M 21.6, X 30.89 vs median 24.1)

Next session (2026-11-04, from 2026-11-03 closes): SPY UNKNOWN:null input at 2026-11-03 · QQQ UNKNOWN:null input at 2026-11-03

CBOE refresh: ok through 2026-11-03; index-vol through 2026-11-03

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
Universe: 2030 names.
Borrow snapshot: 2026-11-03 (the session's own); fee known for 1933 names.
Bull counts: 0:620, 1:736, 2:439, 3:191, 4:42, 5:2, 6:0, 7:0, 8:0
Bear counts: 0:666, 1:821, 2:342, 3:155, 4:41, 5:5, 6:0, 7:0, 8:0

### LONG (106)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ADI | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| ADUS | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  | x |
| AIN | 3 | 0 | yes | x | x |  |  |  |  | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| ALSN | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMX | 4 | 0 | no |  | x |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| APG | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| ASB | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| AXS | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BANF | 3 | 0 | yes |  | x |  |  | x |  |  | x |  | ? | ? |  |  |  |  |  |  |  |  |  |
| BCPC | 3 | 0 | no |  |  |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BJ | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| BLK | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BOOT | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BY | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| CACI | 3 | 0 | yes | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| CBC | 4 | 0 | no | x | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  | x |
| CCK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CME | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| COLM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| CON | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| COR | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| COST | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CPK | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| CSL | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| CUBE | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| DG | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DGX | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| DOW | 3 | 0 | no |  | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| DUK | 3 | 0 | yes |  | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| EG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EHC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ENR | 3 | 0 | no | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| EPAC | 3 | 0 | no | x |  |  |  | x | x | ? |  |  | ? |  |  |  |  |  |  |  |  |  | x |
| EPRT | 3 | 0 | no |  | x |  | x |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EXLS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EXPD | 3 | 0 | yes | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| FELE | 3 | 0 | yes |  |  | x |  | x | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| FIZZ | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| FNF | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| FTS | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  | x |
| FUL | 4 | 0 | no |  | x |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| GIC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| GM | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| GWW | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| HASI | 3 | 0 | no |  | x |  |  | x |  | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| HCI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HCSG | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HEIA | 4 | 0 | yes |  | x |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| HG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HHH | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| HZO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| ICE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| IR | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LFST | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| MCBS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| MCK | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| MCO | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MD | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| MDLZ | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MIDD | 4 | 0 | yes |  | x |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  |  |
| MSCI | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| NATL | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| NBTB | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| NUE | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| OPLN | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  |
| PB | 3 | 0 | yes |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| PG | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| PLMR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| POR | 4 | 0 | no |  | x | x |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| R | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| RAL | 3 | 0 | no | x | x |  | x |  |  | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| REYN | 4 | 0 | no |  |  |  |  | x | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| RLJ | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| RNR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ROK | 3 | 0 | yes |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RPM | 3 | 0 | yes |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| SAIC | 4 | 0 | no | x | x |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| SBH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| SFNC | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| SHW | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SIGI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| SONY | 3 | 0 | no |  | x |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| STBA | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? | ? |  |  |  | ? |  |  |  |  |  |
| SUNB | 5 | 0 | no | x | x |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| TAK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| TDS | 3 | 0 | no |  |  |  | x | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TDY | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| THG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TILE | 3 | 0 | no |  |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| TMO | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TOL | 3 | 0 | no |  | x |  |  | x | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| TW | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TXN | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| URI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| UTHR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| UVE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| VLTO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VSTS | 3 | 0 | no |  | x |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| VTRS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| WCN | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WMT | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| WOR | 3 | 0 | no |  | x |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| WPP | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| WTRG | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| XHR | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| ZTS | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |

### SHORT (81)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAMI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| ABCL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| AMH | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| BAND | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| BBAR | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | ? |  |  |  |  | x | x |  |  |  |  |
| BILI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| BMNR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| BTU | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  | x |  |  |  |  |
| CAT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  | x |  | x |
| CC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  |  |  |  |  |  |  |
| CCJ | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| CECO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  |  |
| CLMT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? | x | x |  |  | ? | x |  |  |  |  |
| CLS | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| CSCO | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| DUOL | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? | x |  |  |  | x |
| EC | 0 | 4 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  |  |
| ENPH | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? |  |  |  |  | x |
| EQX | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| FIG | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| FLUT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? |  |  |  |  | x |
| FOXA | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| FSLR | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? |  |  |  |  | x |
| GOOG | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  | x | x |
| GOOGL | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  | x | x |
| GPC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| GTES | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| IDCC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? |  |  |  |  |  |
| IMAX | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| INOD | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  |  |
| INTC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| KD | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| KGC | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| KMX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| KRMN | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  | x |  |  |  |  |  |  |  | x |
| LI | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? | x |  |  |  |  |
| LITE | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| LMND | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  |  |
| LOGI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? |  |  |  |  |  |
| LQDA | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |
| LRN | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| LYFT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| MDGL | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| META | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| MGA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| MGY | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| MLYS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  |  |  | x |  |  |
| MSTR | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| MTDR | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| NEO | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| NOW | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| OKE | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| ORCL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| OSIS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| PAM | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | ? |  |  |  |  | x | x |  |  |  |  |
| PBI | 0 | 5 | no |  |  |  |  |  |  |  |  |  | x |  | x | x | x | ? | x |  |  |  |  |
| PLTR | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  | x | x |
| RARE | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| RH | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? | x |  |  |  | x |
| RVMD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| SCCO | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| SEZL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| SHC | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  |  |
| SKYW | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| SLM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  |  |
| SPCX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | ? |  | x | x |  | ? | x |  |  | x | x |
| STRL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| STVN | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | ? |  |  | x |  | ? | x |  |  |  | x |
| TMDX | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| UBER | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| VALE | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  | x |  | x |
| VKTX | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  |  |  |  |  |  | x |
| VOYG | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| WEX | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| WIX | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| WLDN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| WOLF | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  | x |  |  | ? | x |  |  |  | x |
| XP | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| ZD | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x | ? | x |  |  |  |  |
| ZETA | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  |  |  |
| ZWS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  | x | x | ? |  |  |  |  | x |

### VOL (0)
_none_

CONFLICT (logged only, never a basket, DESIGN/110 §3): 116.

Ledger: emitted 187 (skipped 0), graded 491; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
