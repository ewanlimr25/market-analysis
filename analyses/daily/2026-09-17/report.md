# S-A daily — 2026-09-17 (off)

Preflight: WARN — prices.parquet ends 2026-09-04, BEFORE the 2026-09-17 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-09-04, BEFORE the 2026-09-17 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-09-04, BEFORE the 2026-09-17 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

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
Gate (2026-09-17, from 2026-09-16 closes): SPY ON (VIX 17.71, VIX3M 19.73, X 17.71 vs median 15.585) · QQQ ON (VIX 17.71, VIX3M 19.73, X 22.44 vs median 21.875)

Next session (2026-09-18, from 2026-09-17 closes): SPY OFF:G2 (VIX 15.44, VIX3M 18.55, X 15.44 vs median 15.585) · QQQ OFF:G2 (VIX 15.44, VIX3M 18.55, X 19.96 vs median 21.875)

CBOE refresh: ok through 2026-09-18; index-vol through 2026-09-18

Entry day: no.

### S-B positions tonight (0)
_none_

### S-B graded at expiry today (0)
_none due_

Open positions: QQQ-IC 1, QQQ-PS 1, SPY-PS 1

### S-B forward ledger to date
_ledger empty_

S-B ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0; ledger open.


## Watch basket (wb-1.0, exploration, paper only)
Universe: 2045 names.
Borrow snapshot: not recorded (pre-d1.5 document).
Bull counts: 0:1066, 1:689, 2:237, 3:47, 4:6, 5:0, 6:0, 7:0, 8:0
Bear counts: 0:497, 1:657, 2:532, 3:259, 4:92, 5:7, 6:1, 7:0, 8:0

### LONG (22)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ADM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| CVBF | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| E | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| ECO | 3 | 0 | no | x | x |  |  |  |  |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| EQH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| FFIV | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| FTNT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| GNK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HRTG | 3 | 0 | no | x | x |  |  |  |  |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| ISRG | 3 | 0 | no |  | x |  |  | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| JOYY | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| LKFT | 3 | 0 | yes |  | x | x |  | x |  | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| LPG | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| LTC | 4 | 0 | no | x | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| NVGS | 3 | 0 | no | x |  |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| PNTG | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| SFL | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TAK | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| TH | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TK | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| UNM | 3 | 0 | no | x |  |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| WST | 4 | 0 | no | x |  |  | x |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |

### SHORT (228)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AA | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  | x |  |  | x | x |  |  |  |  |
| AAOI | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  | x |
| ABG | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| ABVX | 0 | 5 | no |  |  |  |  |  |  | ? |  |  | x | x | x | x |  | ? | x |  |  |  | x |
| ADC | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  |  | x |
| AEE | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| AEO | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  |  |  |
| ALC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x |  |  |  |  | x |
| ALKS | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  |  |
| AMBA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| AMGN | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  |  | x |
| AMH | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| AMP | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| AN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| AOS | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? | x |  |  |  | x |
| ARCB | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| ARR | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| AXP | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| AXTA | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| AYI | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | x | x |  |  |  | x |
| BA | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  | x | ? | x |  |  | x | x |
| BCO | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| BILI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| BIPC | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  |  |
| BKH | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| BLDR | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  |  | x |  |  |  | x |
| BN | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x |  |  |  |  | x |
| BRO | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| BROS | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  | x |
| BTU | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| BXP | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| CAR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? | x |  |  |  |  |
| CAVA | 0 | 4 | yes |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  |  |  |  |  | x |
| CBRS | 0 | 4 | no |  |  | ? |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| CBT | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  |  |
| CCI | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| CFG | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| CG | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  | x |  |  |  | x |
| CHDN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| CLX | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| COO | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  |  |  |  |  | x |
| CPNG | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x |  |  |  | ? | x |  |  |  | x |
| CPT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  | x |
| CRCL | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  | x |  | x | x |
| CSX | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| CTRE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| CURB | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| CUZ | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| CWST | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| CXT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| D | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| DAL | 0 | 4 | yes |  |  |  |  |  |  |  |  |  | x | x |  |  | x |  | x |  |  |  | x |
| DAVE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| DKNG | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x | x |  |  | x |
| DX | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x | x |  |  |  | x |
| EFC | 0 | 4 | no |  |  |  |  |  |  |  |  |  | ? |  |  | x | x | x | x |  |  |  |  |
| EMN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| ENB | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| ENPH | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  |  | x |
| EPRT | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  | x |
| EQPT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| EQT | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  | x |  | x | ? |  |  |  |  | x |
| ESAB | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| EXP | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| F | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| FCN | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x |  |  |  |  | x |
| FCPT | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| FE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| FER | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  |  |  |  | x | x |  | x |  |  |
| FIGR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| FISV | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  | x |
| FLG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| FOUR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| FRT | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| FSLR | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  | x | x |
| FTV | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | x |  |  |  |  | x |
| FULT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| GLNG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| GLPI | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| GNTX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| GPGI | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| GS | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  | x |  |  | x | ? | x |  |  | x | x |
| GWW | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| HAYW | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| HBAN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| HD | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x |  |  | x |  | x |  |  |  | x |
| HE | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  |  | x | x |  | x |  |  |
| HGV | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| HSY | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  | x |
| HYMC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  |  | x |  |  |  | x |
| IBM | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| IBN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| IDA | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| IDXX | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  |  | x |
| INBX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| INVH | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| IRTC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| ITRI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  |  |
| JBS | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  |  |
| JBTM | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| KIM | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| KMB | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| KNF | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| KOD | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  |  | x |  |  |  |  |
| KRMN | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  |  |  |  |  | x |
| KSS | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? | x |  |  |  |  |
| LAMR | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  |  |
| LMND | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| LNT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| LULU | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  | x |  | x | x |
| LVS | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| LYV | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| MAA | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x | x |  |  |  | x |
| MAC | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| MAS | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| MCD | 0 | 5 | no |  |  |  |  |  |  |  |  | x |  | x | x |  | x |  | x |  | x | x | x |
| MHO | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| MLTX | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  | x |  |  | x |  |  |  | x |
| MMM | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  | x |
| MTB | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| MTZ | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  | x |  |  |  | x | x |  |  | x |
| NCLH | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  | x |  |  |  | x |
| NFLX | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| NHI | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  | x |  |  |  |  |
| NKE | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  | x | x | x |
| NN | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |  |  |  |  |
| NTRS | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| NVO | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| NVST | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  |  |
| NXST | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | x |  |  |  |  |  |
| O | 0 | 6 | no |  |  |  |  |  |  |  |  | x | x | x |  |  | x | x | x |  |  |  | x |
| OCFC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | ? |  |  | x | x | ? | x |  |  |  |  |
| OKE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| OSIS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| OTIS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| OUT | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  |  |
| PATK | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| PBH | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| PCAR | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| PDD | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| PHM | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| PINS | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  | x |
| PIPR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? | x |  |  |  | x |
| PL | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |  |  |  | x |
| PLTR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| POOL | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| POR | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| PPG | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| PPL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| PRCT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| PRMB | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| PSA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| PSMT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| QSR | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| RBLX | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| RCI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| RCL | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  |  |  |  |  | x |
| RDN | 0 | 4 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  |  |
| RH | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  |  |  |  |  | x |
| RIVN | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  | x | x |
| RJF | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| RKT | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? | x |  |  |  | x |
| ROL | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  |  | x | x |  | x |  | x |
| RRC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x |  | x |  | ? |  |  |  |  | x |
| RRR | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| SAM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x |  |  |  |  |  |  |
| SARO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| SBRA | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| SBUX | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x |  |  | x | ? | x |  |  |  | x |
| SF | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  | x |  | ? | x |  |  |  |  |
| SFM | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| SGHC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| SIRI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| SLS | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x | x |  | ? |  |  |  |  |  |
| SMG | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| SNN | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x |  |  |  |  |  |
| SOFI | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| SPG | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| SPGI | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  | x |  | ? | x |  |  |  | x |
| SRAD | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| STEP | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| STWD | 0 | 4 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  | x |
| STZ | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| SUI | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| SWX | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x | ? |  |  | x |  | x |  |  |  |  |
| SYY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| TAP | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? | x |  |  |  | x |
| TFX | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| THO | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x |  |  |  |  | x |
| TROW | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| TRU | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| TSCO | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x |  |  |  |  | x |
| TSLA | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| TTAN | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| TXT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x |  |  |  |  |  | x |
| UDR | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| UE | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| UFPI | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  |  |  |  |
| ULS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| UMBF | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| UNP | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| UPS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| UPST | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  | ? | x |  |  |  | x |
| USAR | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| USFD | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| UUUU | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  | ? | x |  |  |  | x |
| VICI | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| VKTX | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  |  |  |
| VLY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| VMC | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  | x |
| VMRK | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | ? |  |  |  | x | ? | x |  |  |  | x |
| VSAT | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  |  | x |
| VSXY | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| VVV | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  | x |
| WDC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| WHD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| WHR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  |  |  |  |  | x |
| WING | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| WLK | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  |  |
| WMG | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| WMS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| WOLF | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  |  |  |
| WY | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  | x |  |  |  | x |
| WYNN | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  | x |  |  |  | x |
| XEL | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| XENE | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| XYZ | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| ZWS | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  |  |

### VOL (6)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CRCL | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  | x |  | x | x |
| EXK | 1 | 2 | yes |  |  |  |  | x |  | ? |  |  |  |  | x | x |  | ? |  | x |  |  | x |
| HIMS | 0 | 2 | yes |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? |  | x |  |  | x |
| IONQ | 0 | 2 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? |  | x |  |  | x |
| PGY | 0 | 1 | yes |  |  |  |  |  |  | ? |  |  |  |  | x |  |  | ? |  | x |  |  | x |
| TBBB | 2 | 1 | yes | x |  |  |  |  |  |  | x |  | ? |  |  | x |  |  |  | x |  |  |  |

CONFLICT (logged only, never a basket, DESIGN/110 §3): 75.

Ledger: emitted 256 (skipped 0), graded 232; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
