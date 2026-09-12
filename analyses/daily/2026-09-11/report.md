# S-A daily — 2026-09-11 (off)

Preflight: WARN — prices.parquet ends 2026-09-04, BEFORE the 2026-09-11 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-09-04, BEFORE the 2026-09-11 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-09-04, BEFORE the 2026-09-11 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (0)
_no event tonight clears the filters._

## Suppressed (0)
_none_

## Graded today (0)
_none due_

## Season to date (forward ledger)
_ledger empty_

Ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0; ledger CLOSED (before 2026-10-01; nothing written).

## S-B state
Gate (2026-09-11, from 2026-09-10 closes): SPY ON (VIX 17.84, VIX3M 19.73, X 17.84 vs median 15.16) · QQQ ON (VIX 17.84, VIX3M 19.73, X 23.33 vs median 21.465000000000003)

Next session (2026-09-14, from 2026-09-11 closes): SPY ON (VIX 15.84, VIX3M 18.6, X 15.84 vs median 15.195) · QQQ OFF:G2 (VIX 15.84, VIX3M 18.6, X 21.02 vs median 21.61)

CBOE refresh: ok through 2026-09-11; index-vol through 2026-09-11

Entry day: yes.

### S-B positions tonight (3)
| underlying | structure | expiry | k_p1 | k_p2 | k_c1 | k_c2 | credit_entry | max_loss_usd | contracts | entry_tier_max |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY | PS | 2026-10-02 | 735.00 | 705.00 | — | — | 1.60 | 2,840.27 | 1 | 1 |
| QQQ | PS | 2026-10-02 | 680.00 | 635.00 | — | — | 2.30 | 4,269.99 | 1 | 1 |
| QQQ | IC | 2026-10-02 | 680.00 | 635.00 | 750.00 | 795.00 | 3.32 | 4,168.49 | 1 | 1 |

### S-B skipped (1)
| underlying | structure | reason |
|---|---|---|
| SPY | IC | no_tier1_c2 |

### S-B exploration book tonight (3; one contract per sleeve, gate ignored, gate verdict recorded)
| underlying | structure | expiry | k_p1 | k_p2 | k_c1 | k_c2 | credit_entry | max_loss_usd | gate_verdict |
|---|---|---|---|---|---|---|---|---|---|
| SPY | PS | 2026-10-02 | 735.00 | 705.00 | — | — | 1.60 | 2,840.27 | ON |
| QQQ | PS | 2026-10-02 | 680.00 | 635.00 | — | — | 2.30 | 4,269.99 | ON |
| QQQ | IC | 2026-10-02 | 680.00 | 635.00 | 750.00 | 795.00 | 3.32 | 4,168.49 | ON |

### S-B graded at expiry today (0)
_none due_

Open positions: QQQ-IC 1, QQQ-PS 1, SPY-PS 1

### S-B forward ledger to date
_ledger empty_

S-B ledger: emitted 3 (skipped 0), exploration 3 (skipped 0), graded 0; ledger open.


## Watch basket (wb-1.0, exploration, paper only)
Universe: 2018 names.
Bull counts: 0:1042, 1:661, 2:246, 3:60, 4:9, 5:0, 6:0, 7:0, 8:0
Bear counts: 0:544, 1:686, 2:491, 3:215, 4:73, 5:8, 6:1, 7:0, 8:0

### LONG (42)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ADM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| APA | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| AR | 3 | 0 | no |  | x |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| ARW | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| BAC | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| BAND | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| BP | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| CHRD | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| CVX | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| DB | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DVN | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| EC | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| ECO | 3 | 0 | yes | x |  |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| EME | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| EOG | 3 | 0 | no | x | x |  |  |  | x |  |  |  | ? |  |  |  |  | ? |  |  |  |  | x |
| EXPD | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| GNW | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| HBT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| HIMX | 3 | 0 | yes |  |  |  | x | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HUM | 3 | 0 | no | x | x |  |  |  |  |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| ING | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| KEN | 3 | 0 | no |  | x | x | x |  |  | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| KT | 3 | 0 | no |  |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| LTC | 3 | 0 | no | x | x |  |  |  |  | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| MATX | 4 | 0 | no | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| MFG | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| MPC | 3 | 0 | no | x | x |  |  |  |  |  | x |  | ? |  |  |  |  |  |  |  |  | x | x |
| MTCH | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| NMR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| NVGS | 4 | 0 | no | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| QRVO | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| SSL | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| STNG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| STRF | 3 | 0 | no |  |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| STT | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| TTE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| UNM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| UVE | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| VLO | 3 | 0 | no | x | x |  |  |  |  |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| VOD | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| VOYA | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| VZ | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |

### SHORT (175)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AA | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | ? | x |  |  |  | x | x |  |  |  | x |
| AAOI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? | x | x |  |  | ? | x |  |  | x | x |
| ADC | 0 | 4 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x |  |  |  |  | x |
| AEE | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| AEO | 0 | 4 | no |  |  |  |  |  |  |  |  | x | ? | x | x |  |  | ? | x |  |  |  |  |
| AEVA | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | ? | x | x |  |  |  | x |  |  |  |  |
| AG | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | ? | x | x | x |  | ? | x |  |  |  | x |
| AI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  |  |
| ALC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | x |  |  |  |  |  |
| ALKS | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  |  |
| AOS | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  |  |
| ARES | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | x |  |  |  |  | x |
| ARWR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| ASST | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  |  |  |  |  | x |
| ATMU | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  | x | x |  |  |  |  |  |
| ATO | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | ? |  |  |  | x | ? | x |  |  |  | x |
| ATR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  | x | x | ? | x |  |  |  | x |
| AXP | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  | x |
| BALL | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | ? |  |  | x | x | ? | x |  |  |  | x |
| BAM | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | x |  |  |  |  |  |
| BEAM | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| BFB | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| BKE | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| BOOT | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  |  | x | x |  |  |  | x |
| BXP | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| CALM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CAR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| CBRL | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  |  |  |
| CBRS | 0 | 3 | no |  |  | ? |  |  |  | ? |  | x | ? |  | x |  |  | ? | x |  |  |  | x |
| CBT | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  |  |
| CCEP | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x | x | ? |  |  |  |  | x |
| CELH | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | ? | x | x |  |  | ? |  |  |  |  | x |
| CGON | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| CHD | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| CHH | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| CIFR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | ? | x | x |  |  | ? | x |  |  |  | x |
| CLF | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x | x | x |  |  |  |  |  |  |  | x |
| CLX | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | ? | x | x |  |  | ? |  |  |  |  | x |
| CNM | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  | x |
| CORZ | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  |  |  |  |  |  | x |
| CPNG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? | x |  |  |  | ? | x |  |  |  | x |
| CRSP | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| CRWV | 0 | 4 | yes |  |  |  |  |  |  | ? |  |  | ? | x | x | x |  | ? | x |  |  | x | x |
| CVNA | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? |  |  |  |  | x |
| DAVE | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| DCI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| DNLI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  |  |
| EFC | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | ? |  |  | x | x | ? | x |  |  |  |  |
| ELS | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? | x |  |  |  | x |
| ELVN | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| ENB | 0 | 4 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| EPRT | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? | x |  |  |  | x |
| EQPT | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| EWBC | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| EXP | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| FAF | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| FCX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | ? | x |  | x |  | ? | x |  |  |  | x |
| FIGR | 0 | 4 | yes |  |  |  |  |  |  | ? |  |  | ? | x | x | x |  | ? | x |  |  |  | x |
| FLG | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  | x | ? | x |  |  |  |  |
| FRVO | 0 | 4 | no |  |  | ? |  |  |  | ? |  | x | ? | x | x |  |  | ? | x |  | x |  | x |
| FSLR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | ? | x | x |  |  | ? | x |  |  |  | x |
| FTV | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| FULT | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| GXO | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | ? | x |  |  | x | ? | x |  |  |  | x |
| HASI | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | ? |  |  | x | x | x |  |  |  |  |  |
| HD | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | ? | x |  |  | x | ? | x |  |  |  | x |
| HE | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  |  | x | x |  | x |  |  |
| HEI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  |  |
| HGV | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| HHH | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| HYMC | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| IDA | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| IDXX | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  | x | x |  |  |  |  | x |
| INCY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| IONQ | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | ? | x | x |  |  | ? | x |  |  |  | x |
| ITRI | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | x | x |  |  |  |  |
| KBH | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| KD | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| KOD | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| KRC | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x | ? | x |  |  |  |  |
| LAD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| LAMR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| LAZ | 0 | 4 | yes |  |  |  |  |  |  | ? |  | x | x |  |  | x | x | ? |  |  |  |  |  |
| LEGN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| LEU | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| LINE | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  |  |
| LIVN | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? |  |  |  |  |  |
| LRN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| LUNR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? | x | x |  |  | ? | x |  |  |  | x |
| MAIN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | x |  |  |  |  |  |
| MAS | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  | x |
| MC | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  |  |
| MCD | 0 | 6 | no |  |  |  |  |  |  |  |  | x | ? | x | x |  | x | x | x |  |  |  | x |
| MHO | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| MLTX | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | ? |  |  | x |  |  | x |  |  |  |  |
| MMM | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? | x |  |  |  | x | x |  |  |  | x |
| MRNA | 0 | 5 | no |  |  |  |  |  |  | ? |  |  | x | x | x | x |  | ? | x |  |  | x | x |
| MSDL | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| NAMS | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  | x |  |  |  |  |
| NHI | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? | x |  |  |  |  |
| NKTR | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| NN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? | x | x |  |  |  | x |  |  |  |  |
| NVO | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | ? | x |  | x | x | ? | x |  |  |  | x |
| NVS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | ? | x |  | x | x | ? |  |  |  |  | x |
| NVTS | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? | x | x |  |  | ? | x |  |  | x |  |
| NXST | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | x |  |  |  |  |  |
| ORLY | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  | x |
| OSIS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| OUT | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| OWL | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | ? | x | x | x |  | ? | x |  |  |  | x |
| PATK | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  | x |
| PBA | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| PBI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| PDD | 0 | 4 | yes |  |  |  |  |  |  |  |  | x | x | x |  |  |  | ? | x |  |  |  | x |
| PECO | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | ? |  |  | x |  | x |  |  |  |  |
| PHM | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| PL | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |  |  |  | x |
| PLTR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | ? | x | x |  |  | ? | x |  |  | x | x |
| POOL | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| POR | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| PPG | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  | x |
| PRU | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| PSA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| QBTS | 0 | 4 | no |  |  |  |  |  |  |  |  | x | ? | x | x |  |  |  | x |  |  |  | x |
| RARE | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  | ? |  |  |  |  | x |
| RCUS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| RDDT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | ? | x | x |  |  | ? | x |  |  |  | x |
| RGTI | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | ? | x | x |  |  | ? | x |  |  |  | x |
| RJF | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| RKT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? | x |  |  |  | ? | x |  |  | x | x |
| SE | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | ? | x | x |  |  | x |  |  |  |  | x |
| SFM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| SHOP | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | ? | x |  | x |  | ? | x |  |  |  | x |
| SIGI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| SIRI | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? | x |  |  |  | x |
| SLS | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x | x | x |  | ? |  |  |  | x | x |
| SNA | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  |  |
| SNN | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  | x | x |  |  |  |  |  |
| SOFI | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | ? | x | x |  |  | ? | x |  |  |  | x |
| SPG | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| SSD | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| STNE | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | ? |  | x |  |  | ? | x |  |  |  |  |
| TAP | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| TCOM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  | x |
| TEM | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| TFX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| TJX | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? | x |  |  |  |  | x |  |  |  | x |
| TNL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| TRI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| TROW | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| TRVI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| TSLA | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? | x | x |  |  | ? | x |  |  | x | x |
| TTAN | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x | x |  | ? |  |  |  |  | x |
| TTD | 0 | 4 | no |  |  |  |  |  |  |  |  | x | ? | x | x |  |  | ? | x |  |  |  | x |
| TXT | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  | x |  |  |  | x |
| UMBF | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| UPS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| UPST | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | ? | x | x |  |  | ? | x |  |  |  | x |
| USAR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? | x | x |  |  | ? |  |  |  |  | x |
| UUUU | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  | ? | x |  |  |  | x |
| VKTX | 0 | 5 | no |  |  |  |  |  |  | ? |  |  | x | x | x | x |  | ? | x |  |  |  | x |
| VMC | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  | x |
| VNT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| VSXY | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| WCN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  | x | x | ? | x |  |  |  | x |
| WLDN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| WMS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  | x |  | x |  |  |  | x |
| WPC | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| WY | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  | x |
| WYNN | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  | x |  |  |  | x |
| XPO | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| XYZ | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | ? | x |  | x |  | ? | x |  |  |  | x |
| ZS | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | ? | x | x | x |  | ? | x |  |  |  | x |
| ZTS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  | x |
| ZWS | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  |  |

### VOL (1)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAL | 1 | 2 | no |  | x |  |  |  |  |  |  |  | ? |  | x |  |  |  | x | x |  |  | x |

CONFLICT (logged only, never a basket, DESIGN/110 §3): 70.

Ledger: emitted 218 (skipped 0), graded 0; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
