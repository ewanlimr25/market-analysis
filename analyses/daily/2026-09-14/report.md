# S-A daily — 2026-09-14 (off)

Preflight: WARN — prices.parquet ends 2026-09-04, BEFORE the 2026-09-14 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-09-04, BEFORE the 2026-09-14 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-09-04, BEFORE the 2026-09-14 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

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
Gate (2026-09-14, from 2026-09-11 closes): SPY ON (VIX 15.84, VIX3M 18.6, X 15.84 vs median 15.195) · QQQ OFF:G2 (VIX 15.84, VIX3M 18.6, X 21.02 vs median 21.61)

Next session (2026-09-15, from 2026-09-14 closes): SPY ON (VIX 17.1, VIX3M 19.28, X 17.1 vs median 15.205) · QQQ ON (VIX 17.1, VIX3M 19.28, X 22.05 vs median 21.61)

CBOE refresh: ok through 2026-09-14; index-vol through 2026-09-14

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
Universe: 2046 names.
Borrow snapshot: not recorded (pre-d1.5 document).
Bull counts: 0:962, 1:716, 2:283, 3:72, 4:13, 5:0, 6:0, 7:0, 8:0
Bear counts: 0:504, 1:690, 2:513, 3:258, 4:70, 5:10, 6:1, 7:0, 8:0

### LONG (47)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ADM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BG | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BP | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CDNA | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| CI | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CLH | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CMBT | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| CON | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| COP | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CRC | 3 | 0 | no |  | x |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| CTBI | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| DGX | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| E | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| GIB | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| GNW | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| GSL | 3 | 0 | yes | x | x |  |  |  | x |  |  |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HAE | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HBT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| HUM | 4 | 0 | no | x | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| IDT | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| ING | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| JOYY | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| LPG | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| MD | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| MPC | 3 | 0 | no | x | x |  |  |  |  |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| MTCH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MUFG | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| NMR | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| NVGS | 4 | 0 | no | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| NWSA | 4 | 0 | yes | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| PBRA | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| PPC | 3 | 0 | yes |  | x |  |  | x | x |  |  |  |  |  |  |  |  | ? |  |  |  |  |  |
| RDVT | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| SFL | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| SHEL | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| STNG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| STRF | 3 | 0 | no |  |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| TALO | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TBBB | 3 | 0 | no | x | x |  |  |  |  |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| TRV | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TTE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| UL | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| UNM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| VEON | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| VIST | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VZ | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WPP | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |

### SHORT (186)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  | x |
| ABVX | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x | x |  |  |  |  |  |  | x |
| AEE | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| AEO | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| AEP | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| AG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| AI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  |  |
| ALKS | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| AMAT | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| AOS | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  |  |
| ARCB | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  |  |
| ARES | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | x |  |  |  |  | x |
| ARWR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| AS | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| ASB | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| ASST | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  | x | x |
| BAM | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | x |  |  |  |  | x |
| BDC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| BEAM | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| BEN | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| BEPC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| BIPC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| BN | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  |  |  | x |
| BNL | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| BOOT | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  |  |
| BRKR | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| BRX | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| BTU | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| BX | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | x |  |  |  |  | x |
| CAMT | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| CAR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? | x |  |  |  |  |
| CBRS | 0 | 3 | no |  |  | ? |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| CBT | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  |  |
| CDE | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| CG | 0 | 4 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  |  |
| CHD | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| CHH | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| CIFR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| CLBK | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  | x |  |  |  |  |  |  |  |
| CLS | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |  |  | x |
| CLSK | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| CNM | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  | x |
| COHR | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| COHU | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| CORZ | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  |  |  |  |  |  | x |
| CPNG | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? | x |  |  |  | x |
| CRSP | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| CRWV | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| CVCO | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  | x |
| DAVE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| DKS | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  | x | x |  |  |  |  |  | x |  | x |
| DOC | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| DSL | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| EFC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  | x | x | ? | x |  |  |  |  |
| ENB | 0 | 5 | no |  |  |  |  |  |  |  |  |  | x | x |  |  | x | x | x |  |  |  | x |
| ESAB | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| EW | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| EWBC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| EXP | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  | x |
| EXR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| FRT | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| FSLR | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  |  | x |
| FTV | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| FUL | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| GD | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| GME | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x | x | x |  |  |  |  |  |  | x | x |
| GPI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| GWW | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| GXO | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? | x |  |  |  | x |
| HAPN | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  | x |  |  |  |  |  |  | x |
| HD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| HE | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  |  | x | x |  | x |  |  |
| HEI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| HGV | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| HYMC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| IFF | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| INCY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| INTC | 0 | 4 | yes |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| INVH | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| IONQ | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| IRT | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| ITRI | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | x | x |  |  |  |  |
| JBS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| KMB | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| KNF | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| LAD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| LAMR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  |  |
| LAZ | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  | x | x | ? |  |  |  |  | x |
| LCII | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x | x |  |  |  |  |
| LEU | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| LINE | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  |  |
| LUNR | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  |  |
| MAIN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | x |  |  |  |  |  |
| MC | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  |  |
| MDB | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| MDU | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| MHK | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| MRNA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| NAMS | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  | x |  |  |  |  |
| NBIS | 0 | 4 | yes |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  | x | x |
| NCLH | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  | x |  |  |  | x |
| NHI | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? | x |  |  |  |  |
| NN | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |  |  |  |  |
| NNN | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  |  |
| NTLA | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| NTST | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| NVO | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x | x | ? | x |  |  |  | x |
| NVS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x | x | ? |  |  |  |  | x |
| NVST | 0 | 4 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x | x | x |  |  |  |  |  |
| NWE | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | ? |  |  | x | x | ? | x |  |  |  |  |
| O | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| OBDC | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x |  |  |  |  | x |
| OGE | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| OMAB | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| ORCL | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| OSIS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| PBA | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| PDD | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| PECO | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  |  |
| PFSI | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  |  |
| PL | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |  |  |  | x |
| PLD | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| PLTR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| PNW | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| POOL | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  | x |
| POR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| POST | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| PRIM | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| PRMB | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| PRU | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| PSA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| QBTS | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  | x |
| RARE | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  | ? |  |  |  |  | x |
| RCUS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| RGTI | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| ROK | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  | x |
| SAM | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? |  |  |  |  |  |
| SFM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x | x |  |  | x |
| SIRI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  |  |
| SLS | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| SMCI | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| SNDK | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  | x | x |
| SOFI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| SPG | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| SR | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| SSD | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| STX | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  | x | x |
| SVM | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| TAP | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| TCOM | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? | x |  |  |  | x |
| TDG | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x | x |  |  |  | x |
| TER | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  | x | x |
| TFII | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| TFX | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| TJX | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  | x |
| TNL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| TROW | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| TRVI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  |  |
| TSLA | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| UMBF | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| UPS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| UPST | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  |  | x |
| USAR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| UUUU | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  | ? | x |  |  |  | x |
| VFC | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| VKTX | 0 | 5 | no |  |  |  |  |  |  | ? |  |  | x | x | x | x |  | ? | x |  |  |  |  |
| VMC | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  | x |
| VNT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| VSAT | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| VST | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| VSXY | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| VVV | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| WBI | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| WDC | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| WHD | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| WLDN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| WMS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| WOLF | 0 | 4 | yes |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  |  | x |
| WSC | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x |  |  |  |  |
| WULF | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| WY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| WYNN | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  | x |  |  |  | x |
| XENE | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  |  |
| XYZ | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  | x | x |
| ZTS | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| ZWS | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |

### VOL (1)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OVV | 2 | 0 | yes | x | x |  |  |  |  | ? |  |  |  |  |  |  |  | ? |  | x |  |  | x |

CONFLICT (logged only, never a basket, DESIGN/110 §3): 88.

Ledger: emitted 234 (skipped 0), graded 0; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
