# S-A daily — 2026-09-09 (off)

Preflight: WARN — prices.parquet ends 2026-09-04, BEFORE the 2026-09-09 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-09-04, BEFORE the 2026-09-09 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-09-04, BEFORE the 2026-09-09 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

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
Gate (2026-09-09, from 2026-09-08 closes): SPY ON (VIX 15.72, VIX3M 18.39, X 15.72 vs median 15.16) · QQQ ON (VIX 15.72, VIX3M 18.39, X 21.71 vs median 21.465000000000003)

Next session (2026-09-10, from 2026-09-09 closes): SPY UNKNOWN:null input at 2026-09-09 · QQQ UNKNOWN:null input at 2026-09-09

CBOE refresh: ok through 2026-09-09; index-vol through 2026-09-09

Entry day: no.

### S-B positions tonight (0)
_none_

### S-B graded at expiry today (0)
_none due_

Open positions: none

### S-B forward ledger to date
_ledger empty_

S-B ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0; ledger CLOSED (before 2026-09-11; nothing written).


## Watch basket (wb-1.0, exploration, paper only)
Universe: 2035 names.
Bull counts: 0:984, 1:725, 2:255, 3:63, 4:6, 5:2, 6:0, 7:0, 8:0
Bear counts: 0:574, 1:725, 2:493, 3:188, 4:50, 5:5, 6:0, 7:0, 8:0

### LONG (38)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ACT | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| ADM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BLCO | 3 | 0 | yes |  | x |  |  |  | x | x |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| CMBT | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| CMC | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| COP | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CVX | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DB | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  |
| DMC | 5 | 0 | no | x | x |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| EC | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| FLEX | 3 | 0 | no |  | x |  | x |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| GNK | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| GNW | 3 | 0 | yes | x | x |  |  |  | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HAL | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HSAI | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HSBC | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| HUM | 3 | 0 | no | x | x |  |  |  |  |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| ING | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| LAZR | 3 | 0 | no | x |  | ? |  | x | ? | ? | x |  | ? |  |  |  | ? | ? |  |  | ? |  |  |
| LTC | 4 | 0 | yes | x | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  |  |
| NMR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| NTR | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| OPY | 4 | 0 | yes | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| PAYP | 3 | 0 | no |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| QRVO | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| SFL | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| SKHY | 3 | 0 | no | x | x | ? |  |  | ? | ? | x |  |  |  |  |  | ? | ? |  |  | ? | x | x |
| STNG | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| STRF | 4 | 0 | no |  | x |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| TDS | 3 | 0 | no |  |  |  |  | x | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| TEN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| UHS | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| UNM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| VLO | 3 | 0 | yes | x | x |  |  |  |  |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| VZ | 3 | 0 | no | x | x |  |  |  | x |  |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| WOR | 3 | 0 | no |  | x |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| WPM | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WTRG | 5 | 0 | no | x | x |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |

### SHORT (143)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| ABVX | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x | x | x |  |  |  |  |  |  |  | x |
| ACGL | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| ACI | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| AEO | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| AI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  |  |
| ALC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | x |  |  |  |  | x |
| ALKT | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| ANIP | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| AOS | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| APLE | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| ASH | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| ASST | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  |  |  |  |  | x |
| AXP | 0 | 4 | no |  |  |  |  |  |  |  |  |  |  | x |  |  | x | x | x |  |  |  | x |
| BBUC | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | ? |  |  |  |  | x | x |  |  |  |  |
| BCO | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | x | x |  |  |  |  |
| BEAM | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| BFB | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| BIDU | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? | x |  |  |  | x |
| BJ | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| BLDR | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  |  | x |  |  |  | x |
| BN | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  |  | x |
| BNT | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | ? |  |  |  | x | x |  |  |  |  |  |
| BRO | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| BRZE | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| BXP | 0 | 4 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| BYD | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x |  |  |  |  |  |
| CALM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| CBRL | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x | x | x |  |  | ? |  |  |  |  |  |
| CBT | 0 | 4 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  |  |
| CHD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| CHTR | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| CINF | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| CL | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| CNM | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| COIN | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  |  | x |
| CPNG | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| CPT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  | x |
| CRSP | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| DKNG | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| EPRT | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| ESAB | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| EXP | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| EXR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| FAF | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| FICO | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| FIG | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x | x |  | ? |  |  |  |  | x |
| FLG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  | x |  |  |  |  |  | x |
| FNF | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  |  |  | x |
| FSLR | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  | x | x |  |  |  |  |  |  |  | x |
| FTV | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| GIL | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| GXO | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| HAYW | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  |  |  |  | x | x |  |  |  |  |
| HD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| HEI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| IDA | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  |  |
| IDXX | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  |  | x |
| IFF | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| INOD | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  |  |
| IONQ | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| IRMD | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| IRT | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| ITRI | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  |  | x |  |  |  | x |
| ITW | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | x | x |  |  |  | x |
| JBS | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x |  | x |  | ? | x |  |  |  |  |
| KD | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| KHC | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? |  |  |  |  | x |
| KMB | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| KMI | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? | x |  |  |  | x |
| KSPI | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| KSS | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| LAD | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| LINE | 0 | 4 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  |  |
| LOAR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| LRN | 0 | 4 | yes |  |  |  |  |  |  |  |  |  | x |  | x | x |  | ? | x |  |  |  | x |
| LULU | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| LUNR | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| LUV | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x |  |  |  | x |
| LVS | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  | x | ? | x |  |  |  | x |
| LYV | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| MCD | 0 | 4 | yes |  |  |  |  |  |  |  |  | x |  | x |  |  | x | ? | x |  |  |  | x |
| MCY | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | ? |  | x |  | x | ? | x |  |  |  |  |
| MFC | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| MLM | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  |  |  |  | x | x |  |  |  | x |
| MO | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| MSCI | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |
| MTH | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| NAMS | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  | x |  |  |  |  |
| NCLH | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  | x |  |  |  | x |
| NN | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  |  |
| NTCT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| NTLA | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| NVS | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x |  | x | x | ? |  |  |  |  | x |
| NVTS | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  |  |
| ONON | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  | x |
| OPCH | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| OSIS | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| OTEX | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| OTIS | 0 | 5 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x | x |  |  |  | x |
| OUST | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  |  |
| OWL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| PATK | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  |  |
| PECO | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x | ? |  |  | x | ? | x |  |  |  |  |
| PHM | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| PL | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  | ? | x |  |  |  | x |
| PLTR | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| PRU | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| PURR | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| QBTS | 0 | 4 | yes |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| QURE | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| RARE | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x | x |  | ? |  |  |  |  |  |
| RCUS | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| SBUX | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| SFM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| SIGI | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| SIRI | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x |  | x |  | ? | x |  |  |  | x |
| SRPT | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| SSD | 0 | 4 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  |  |
| SUI | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| TCOM | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| TDG | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x | x |  |  |  | x |
| TNL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| TROW | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| TRVI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  |  |
| TTAN | 0 | 4 | yes |  |  |  |  |  |  |  |  | x | x |  | x | x |  | ? |  |  |  |  | x |
| TTD | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| TTWO | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  | x | x |  |  | x |  |  |  |  | x |
| TXT | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  | x |  |  |  | x |
| UPS | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  | x | ? | x |  |  |  | x |
| UPST | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| UUUU | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  | ? | x |  |  |  | x |
| VICI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| VSXY | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| WCN | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| WLDN | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| WMS | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| WSBC | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| WYNN | 0 | 4 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  | x |  |  |  | x |
| XE | 0 | 3 | yes |  |  | ? |  |  |  |  |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| XYL | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  | x |  |  |  | x |
| ZS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| ZTS | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |

### VOL (0)
_none_

CONFLICT (logged only, never a basket, DESIGN/110 §3): 72.

Ledger: emitted 181 (skipped 0), graded 0; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
