# S-A daily — 2026-09-16 (off)

Preflight: WARN — prices.parquet ends 2026-09-04, BEFORE the 2026-09-16 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-09-04, BEFORE the 2026-09-16 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-09-04, BEFORE the 2026-09-16 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

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
Gate (2026-09-16, from 2026-09-15 closes): SPY ON (VIX 17.2, VIX3M 19.36, X 17.2 vs median 15.33) · QQQ ON (VIX 17.2, VIX3M 19.36, X 22.26 vs median 21.75)

Next session (2026-09-17, from 2026-09-16 closes): SPY ON (VIX 17.71, VIX3M 19.73, X 17.71 vs median 15.585) · QQQ ON (VIX 17.71, VIX3M 19.73, X 22.44 vs median 21.875)

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
Universe: 2031 names.
Borrow snapshot: not recorded (pre-d1.5 document).
Bull counts: 0:1066, 1:678, 2:238, 3:45, 4:4, 5:0, 6:0, 7:0, 8:0
Bear counts: 0:449, 1:674, 2:548, 3:263, 4:89, 5:8, 6:0, 7:0, 8:0

### LONG (19)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ADM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMN | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| ATRC | 3 | 0 | yes | x | x |  |  |  |  |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| CON | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| E | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| EQH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| FFIV | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| FTNT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ISRG | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| JOYY | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| LPG | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| LTC | 3 | 0 | no | x |  |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| NUE | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| NVGS | 4 | 0 | no | x | x |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| OFG | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| STNG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| TAK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| TK | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| WST | 4 | 0 | no | x |  |  | x |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |

### SHORT (224)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  | x |
| ABG | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| ABVX | 0 | 5 | no |  |  |  |  |  |  | ? |  |  | x | x | x | x |  | ? | x |  |  |  | x |
| ADC | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  |  | x |
| AEE | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| AEO | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| AG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| AGI | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| AGO | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | ? |  | x |  |  | x |  |  |  |  |  |
| AI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  |  |
| ALB | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| ALKS | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  | x |
| ALLY | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| AMBA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  |  |
| AMGN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| AMH | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| AMP | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| AN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| AOS | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? | x |  |  |  |  |
| APO | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  | x |  |  | x |  |  |  |  | x |
| ARR | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| AWI | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  |  |  |  | x | x |  |  |  |  |
| AXP | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| AXTA | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| AYI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  |  | x |  |  |  | x |
| BCO | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| BEPC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| BILI | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? | x |  |  |  |  |
| BIPC | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  |  |
| BN | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x |  |  |  |  | x |
| BNL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| BOOT | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| BROS | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  | x |
| BTU | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? | x |  |  |  |  |
| BXP | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| CAR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| CBRS | 0 | 3 | no |  |  | ? |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| CCI | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| CFG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| CG | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| CHD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| CHDN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| CLSK | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| CMC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| CMG | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| COIN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  | x | x |
| CPNG | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x |  |  |  | ? | x |  |  |  | x |
| CRCL | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| CTRE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| CUZ | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| CVNA | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x |  | x |  | ? |  |  |  |  | x |
| CXT | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| DAVE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| DKNG | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| DLB | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| DLTR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| DSL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| DTE | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| DUK | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| EBC | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| EFC | 0 | 4 | no |  |  |  |  |  |  |  |  |  | ? |  |  | x | x | x | x |  |  |  |  |
| EMN | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| ENPH | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  |  | x |
| EQPT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| ESS | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| EXP | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  | x |
| EXR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| F | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| FCN | 0 | 4 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x |  |  |  |  | x |
| FCPT | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| FE | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| FIGR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| FISV | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| FLG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| FOUR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| FRT | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| FSLR | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| FTV | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | x |  |  |  |  | x |
| FUL | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| FUN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| GD | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| GLNG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x | x |  |  | x |
| GLPI | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| GNTX | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| GWW | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| GXO | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? | x |  |  |  |  |
| HD | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x |  |  | x |  | x |  |  |  | x |
| HE | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  |  | x | x |  | x |  |  |
| HL | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| HSY | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  | x |
| HYMC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| IBM | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  | x |  | x |  | ? | x |  |  | x | x |
| IBN | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  |  |
| IDA | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| INBX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| INVH | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| IRON | 0 | 4 | yes |  |  |  |  |  |  |  |  |  | x |  | x | x | x | ? |  |  |  |  |  |
| IRTC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| ITRI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| JOE | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | ? |  | x | x |  | ? | x |  |  |  |  |
| KMB | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| KMI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| KNF | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| KOD | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  |  | x |  |  |  |  |
| KRC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| KSS | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? | x |  |  |  |  |
| KTOS | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| LCII | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| LEN | 0 | 4 | yes |  |  |  |  |  |  |  |  | x | x |  | x |  | x |  |  |  |  |  | x |
| LEU | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| LGND | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| LLYVK | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x |  |  | x | x |  |  |  |  |  |
| LMND | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  |  |
| LNT | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| LULU | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  | x |  |  | x |
| LUNR | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  |  |
| LYV | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| MAA | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  | x |  |  |  | x |
| MAT | 0 | 4 | yes |  |  |  |  |  |  |  |  | x | x |  | x |  | x | ? |  |  |  |  | x |
| MCD | 0 | 5 | no |  |  |  |  |  |  |  |  | x |  | x | x |  | x |  | x |  | x | x | x |
| MHO | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| MIAX | 0 | 4 | yes |  |  |  |  |  |  | ? |  | x | x |  |  | x |  | ? | x |  |  |  | x |
| MLTX | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  | x |  |  | x |  |  |  | x |
| MSCI | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| MTG | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| MU | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| NBIS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  | x | x |
| NHI | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? | x |  |  |  |  |
| NKE | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  | x |  | x |
| NLY | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  | x |
| NN | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |  |  |  |  |
| NTST | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| NVO | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| NVST | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x | x |  |  |  |  |  |
| NXST | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | x |  |  |  |  | x |
| NXT | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  | x |
| O | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? | x |  |  |  | x |
| OKE | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| ORCL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| ORLY | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  | x |
| OSIS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| PATK | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| PBA | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| PDD | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| PECO | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  |  |
| PFSI | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  | x |  | x |  | x |
| PHM | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| PIPR | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  |  |
| PL | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |  |  |  | x |
| PLD | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| PLTR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| PNW | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  |  |
| POOL | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| POR | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| PPG | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| PPL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| PRCT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| PRMB | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  |  |
| PSA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| PSMT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| RARE | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  | ? |  |  | x |  |  |
| RH | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  |  |  |  |  | x |
| RIVN | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  |  | x |
| RRC | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x | x |  | x |  | ? |  |  |  |  | x |
| RRR | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| RYTM | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x |  |  |  |  |  | x |
| SAM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? |  |  |  |  |  |
| SARO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| SBRA | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| SBUX | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  | x | ? | x |  |  |  | x |
| SFM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| SGHC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| SIRI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| SLS | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| SMG | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| SNDK | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  | x | x |
| SNEX | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| SNN | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x |  |  |  |  |  |
| SO | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  |  |  | x |
| SOFI | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| SPG | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| SPGI | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  |  | x |  | ? | x |  |  |  | x |
| STX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| SUI | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| SVM | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| SYY | 0 | 4 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| TAP | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| TFX | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| THO | 0 | 4 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x |  |  |  |  | x |
| TJX | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  | x |  | x |
| TROW | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| TRU | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| TSCO | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x |  |  |  |  | x |
| TSLA | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| TXT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x |  |  |  |  |  | x |
| UE | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | ? | ? |  |  | x | x | x |  |  |  |  |
| UFPI | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  |  |  |  |
| ULS | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| UMBF | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| UPST | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  |  | x |
| USAR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| USFD | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| UUUU | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  | ? | x |  |  |  | x |
| VFC | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  | x |  |  |  |  |
| VKTX | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  |  | x |
| VLY | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| VMC | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  | x |
| VSAT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| VSXY | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| VVV | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  | x |
| WAL | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| WDC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| WDFC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| WEC | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x | x |  |  |  | x |
| WHD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| WHR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  |  |  |  | x | x |
| WING | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| WLK | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  |  |
| WOLF | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  |  |  |
| WYNN | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  | x |  |  |  | x |
| XENE | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| XRAY | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| ZTO | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| ZWS | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  |  |

### VOL (2)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAL | 1 | 3 | no |  |  |  | x |  |  |  |  |  |  | x | x |  |  |  | x | x |  |  | x |
| ASST | 0 | 2 | yes |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x |  | x | x |

CONFLICT (logged only, never a basket, DESIGN/110 §3): 73.

Ledger: emitted 245 (skipped 0), graded 181; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
