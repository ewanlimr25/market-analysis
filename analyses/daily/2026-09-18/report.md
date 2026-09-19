# S-A daily — 2026-09-18 (off)

Preflight: WARN — prices.parquet ends 2026-09-04, BEFORE the 2026-09-18 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-09-04, BEFORE the 2026-09-18 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-09-04, BEFORE the 2026-09-18 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

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
Gate (2026-09-18, from 2026-09-17 closes): SPY OFF:G2 (VIX 15.44, VIX3M 18.55, X 15.44 vs median 15.585) · QQQ OFF:G2 (VIX 15.44, VIX3M 18.55, X 19.96 vs median 21.875)

Next session (2026-09-21, from 2026-09-18 closes): SPY OFF:G2 (VIX 14.81, VIX3M 18.24, X 14.81 vs median 15.585) · QQQ OFF:G2 (VIX 14.81, VIX3M 18.24, X 19.29 vs median 21.75)

CBOE refresh: ok through 2026-09-18; index-vol through 2026-09-18

Entry day: yes.

### S-B positions tonight (0)
_none_

### S-B skipped (4)
| underlying | structure | reason |
|---|---|---|
| SPY | PS | OFF:G2 |
| SPY | IC | OFF:G2 |
| QQQ | PS | OFF:G2 |
| QQQ | IC | OFF:G2 |

### S-B exploration book tonight (3; one contract per sleeve, gate ignored, gate verdict recorded)
| underlying | structure | expiry | k_p1 | k_p2 | k_c1 | k_c2 | credit_entry | max_loss_usd | gate_verdict |
|---|---|---|---|---|---|---|---|---|---|
| SPY | PS | 2026-10-09 | 735.00 | 710.00 | — | — | 1.28 | 2,372.08 | OFF:G2 |
| SPY | IC | 2026-10-09 | 735.00 | 710.00 | 789.00 | 820.00 | 1.79 | 2,921.08 | OFF:G2 |
| QQQ | PS | 2026-10-09 | 688.00 | 655.00 | — | — | 2.19 | 3,081.16 | OFF:G2 |

### S-B graded at expiry today (0)
_none due_

Open positions: QQQ-IC 1, QQQ-PS 1, SPY-PS 1

### S-B forward ledger to date
_ledger empty_

S-B ledger: emitted 0 (skipped 0), exploration 3 (skipped 0), graded 0; ledger open.


## Watch basket (wb-1.0, exploration, paper only)
Universe: 2080 names.
Borrow snapshot: not recorded (pre-d1.5 document).
Bull counts: 0:1120, 1:673, 2:241, 3:46, 4:0, 5:0, 6:0, 7:0, 8:0
Bear counts: 0:458, 1:687, 2:580, 3:262, 4:79, 5:13, 6:0, 7:1, 8:0

### LONG (21)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| BLFS | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| CHT | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| EQH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| FFIV | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| GNK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| ISRG | 3 | 0 | no |  | x |  |  | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| JOYY | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| LAZR | 3 | 0 | no | x |  | ? |  | x | ? | ? | x |  | ? |  |  |  | ? | ? |  |  | ? |  |  |
| LPG | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| NVGS | 3 | 0 | no | x |  |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| PBLS | 3 | 0 | yes | x | x | ? |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  | ? |  | x |
| PRLB | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| TAK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TK | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| UNM | 3 | 0 | no | x |  |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| VEON | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| VRSN | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WFG | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| WST | 3 | 0 | no | x |  |  | x |  |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| ZIM | 3 | 0 | yes | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |

### SHORT (224)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  | x | x |
| ABVX | 0 | 5 | no |  |  |  |  |  |  | ? |  |  | x | x | x | x |  | ? | x |  |  |  | x |
| ADC | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  |  | x |
| AEE | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  | x |
| AI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| ALB | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| ALC | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x |  |  |  |  | x |
| AMGN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| AMH | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| AMP | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| AMR | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| AN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| AOS | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? | x |  |  |  | x |
| ARCB | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| ARR | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x | x |  | x |  | x |
| ASND | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? |  |  |  |  | x |
| ASTH | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | ? |  | x |  |  | x | x |  |  |  |  |
| ATO | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x | x |  |  |  | x |
| AXP | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  | x | x |
| AYI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  |  | x |  |  |  | x |
| BA | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  | x | ? | x |  |  | x | x |
| BALL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? |  |  |  |  | x |
| BIPC | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  |  |
| BIRK | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  |  | x |  |  | x | x |
| BKH | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| BLDR | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  |  | x |  |  |  | x |
| BNL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| BRO | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| BROS | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  | x |
| BRSL | 0 | 4 | yes |  |  |  |  |  |  |  |  | x | ? |  |  |  | x | x | x |  |  |  |  |
| BTU | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? | x |  |  |  | x |
| CAR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| CAVA | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  |  |  |  |  | x |
| CBRS | 0 | 3 | no |  |  | ? |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| CBT | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| CFG | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| CG | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  | x |  |  |  | x |
| CHD | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| CMS | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  |  |  | x |  | x |  |  |  | x |
| COST | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  |  | x | ? | x |  |  | x | x |
| CPB | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  |  |  | x |
| CPNG | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x |  |  |  | ? | x |  |  |  | x |
| CPT | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  | x |  |  |  | x |
| CTRE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| CUZ | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| CVNA | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| CXT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| DAVE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? |  |  |  |  | x |
| DIS | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| DKNG | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| DLTR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| DRI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| DSL | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| DTE | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x | x |  |  |  | x |
| DVA | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| DX | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x |  | x |  |  |  | x |
| EBC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| EFC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| ENB | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| EQPT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| ERAS | 0 | 4 | yes |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? | x |  |  |  | x |
| ESAB | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| ESS | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| ETSY | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  | x |  | x | ? | x |  |  |  | x |
| EXC | 0 | 5 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x | x |  |  |  | x |
| EXP | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| FA | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| FCPT | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  | x | ? | x |  |  |  | x |
| FISV | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  | x |
| FLG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| FNB | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x | ? |  |  | x | ? | x |  |  |  | x |
| FRT | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| FSK | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| FSLR | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  | x | x |
| FSV | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  | x |
| FTV | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| FUL | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| FULT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| FUN | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  |  |
| GGAL | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| GIL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| GLPI | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| GNTX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| GPGI | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| GS | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  |  | x | ? | x |  |  | x | x |
| GWW | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| HAS | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| HBAN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| HD | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x |  |  | x |  | x |  |  | x | x |
| HGV | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| HSY | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  | x |
| HUBS | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| HYMC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  |  | x |  |  |  | x |
| IBN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| INBX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| INFY | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| INVH | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| IRT | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  | x |  |  |  | x |
| IRTC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| ITRI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| IVT | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| JBS | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  | x |
| JBTM | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| KIM | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| KMB | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| KNF | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| KOD | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  |  | x |  |  |  |  |
| KRC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| KSS | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? | x |  |  |  | x |
| LAMR | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| LCII | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| LINE | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| LMND | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| LNT | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| LRN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| LULU | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  | x |  |  | x |
| LUNR | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  | x |
| LVS | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  | x |  | x |
| LYV | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| MAC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  | x |
| MAT | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x |  |  | x | ? |  |  |  |  | x |
| MCD | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x |  |  | x |  | x |  | x | x | x |
| MDLN | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| MGEE | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | ? |  |  |  | x |  | x |  |  |  |  |
| MKC | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  |  |  | x |
| MLTX | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  | x |  |  | x |  |  |  |  |
| MP | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| MRSH | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| MTB | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| MTG | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| MTZ | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  |  | x |  |  |  | x |
| NCLH | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  | x |  |  |  | x |
| NHI | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  | x |  |  |  | x |
| NKE | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  | x | x | x |
| NLY | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  |  | x | x |  |  |  |  | x |
| NRG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| NTRS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| NTST | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| NVO | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| O | 0 | 7 | no |  |  |  |  |  |  |  |  | x | x | x | x |  | x | x | x |  |  |  | x |
| OKE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| ORI | 0 | 4 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| OSIS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| OTIS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| PATK | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| PBH | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  | x | ? | x |  |  |  | x |
| PBI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| PDD | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| PFSI | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  | x |
| PHM | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| PL | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  | x |  |  |  | x |
| PLTR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| POOL | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| POR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  | x |
| PPG | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| PPL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| PRCT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| PSA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| PSMT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| QSR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| QXO | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  | x |  |  |  | x |
| RBLX | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| RCL | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  | x |
| RDN | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| RIVN | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  |  | x |
| RJF | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| RKT | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? | x |  |  |  | x |
| RYTM | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x | x |  |  |  |  |  | x |
| SAM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x |  |  |  |  |  | x |
| SBUX | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x |  |  | x | ? | x |  |  |  | x |
| SF | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  | x |  | ? | x |  |  |  | x |
| SGHC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| SMG | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| SNEX | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| SOFI | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| SPGI | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  | x |  | ? | x |  |  |  | x |
| SRPT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| STEP | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| STWD | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  | x |  | x |
| STZ | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| SUI | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| SYY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| TAP | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| TFC | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| TFX | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| THO | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x |  | x |  | x | x |  |  |  |  | x |
| TRI | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| TROW | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| TRU | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| TSLA | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| TTAN | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? |  | x |  |  | x |
| TTD | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? |  |  |  |  | x |
| TXT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x |  |  |  |  |  | x |
| U | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| UDR | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| UFPI | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  |  |  | x |
| ULS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| UMBF | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| UNP | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| UPS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| UPST | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  | ? | x |  |  |  | x |
| USAR | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| USFD | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| UUUU | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  | ? | x |  |  |  | x |
| VFC | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  | x |  |  |  | x |
| VICI | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x |  |  | x | ? | x |  |  |  | x |
| VKTX | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  |  |  |
| VLY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| VMC | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  | x |
| VVV | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  | x |
| WAL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| WDFC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| WEC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| WHD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| WHR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  |  | x |  |  | x |
| WM | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| WMG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| WMS | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| WOLF | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? | x |  |  |  | x |
| WPC | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| WY | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x | x |  |  |  | x |
| WYNN | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  | x |  |  |  | x |
| XENE | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x | x | x |  | x |
| XYZ | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  |  | x | ? | x |  |  |  | x |

### VOL (7)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| APA | 2 | 1 | yes | x |  |  |  |  |  | ? | x |  |  |  |  | x |  |  |  | x |  |  | x |
| ASST | 0 | 2 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x |  | x | x |
| CLSK | 1 | 2 | yes |  |  |  |  | x |  | ? |  |  |  | x | x |  |  | ? |  | x |  |  | x |
| EQX | 0 | 0 | yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ? |  | x |  |  | x |
| EXK | 1 | 0 | no |  |  |  |  | x |  | ? |  |  |  |  |  |  |  | ? |  | x |  |  | x |
| HIMS | 0 | 2 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x |  |  | x |
| IONQ | 0 | 2 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? |  | x |  |  | x |

CONFLICT (logged only, never a basket, DESIGN/110 §3): 80.

Ledger: emitted 252 (skipped 0), graded 218; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
