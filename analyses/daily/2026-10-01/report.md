# S-A daily — 2026-10-01 (S3)

Preflight: WARN — prices.parquet ends 2026-09-25, BEFORE the 2026-10-01 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_prices.py; returns.parquet ends 2026-09-25, BEFORE the 2026-10-01 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_returns.py; features.parquet ends 2026-09-25, BEFORE the 2026-10-01 trade date -- any lane reading it gets a stale regime/factor read. Rebuild: python3 scripts/truthset/build_features.py

## Tonight's candidates (0)
_no event tonight clears the filters._

## Suppressed (0)
_none_

## Graded today (0)
_none due_

## Season to date (forward ledger)
_ledger empty_

Ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0; ledger open.

## S-B state
Gate (2026-10-01, from 2026-09-30 closes): SPY ON (VIX 16.34, VIX3M 18.37, X 16.34 vs median 15.695) · QQQ ON (VIX 16.34, VIX3M 18.37, X 22.46 vs median 21.155)

Next session (2026-10-02, from 2026-10-01 closes): SPY ON (VIX 16.39, VIX3M 18.58, X 16.39 vs median 15.695) · QQQ ON (VIX 16.39, VIX3M 18.58, X 22.51 vs median 21.155)

CBOE refresh: ok through 2026-10-02; index-vol through 2026-10-02

Entry day: no.

### S-B positions tonight (0)
_none_

### S-B graded at expiry today (0)
_none due_

Open positions: QQQ-IC 2, QQQ-PS 2, SPY-IC 1, SPY-PS 2

### S-B forward ledger to date
_ledger empty_

S-B ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0; ledger open.


## S-C state
Entry day: no; ledger CLOSED (opens 2026-10-02; nothing written).

### S-C graded at expiry (0)
_none due_

### S-C open book (S-B open: yes; the 40% budget binds only then)
| pair | positions | open_risk_usd | budget_usd | max_sector_positions |
|---|---|---|---|---|
| C1-SS | 0 | 0.00 | 8,000.00 | 0 |
| C1-IB | 0 | 0.00 | 4,000.00 | 0 |
| C2-SS | 0 | 0.00 | 8,000.00 | 0 |
| C2-IB | 0 | 0.00 | 4,000.00 | 0 |

### S-C forward ledger to date (entry-week series)
_ledger empty_

Progress to the read: graded entry-weeks 0 of 40 (C1-SS), 0 of 40 (C1-IB), 0 of 40 (C2-SS), 0 of 40 (C2-IB)

S-C ledger: emitted 0 (skipped 0), exploration 0 (skipped 0), graded 0.


## Watch basket (wb-1.0, exploration, paper only)
Universe: 2005 names.
Borrow snapshot: 2026-10-01 (the session's own); fee known for 1999 names.
Bull counts: 0:983, 1:720, 2:257, 3:40, 4:5, 5:0, 6:0, 7:0, 8:0
Bear counts: 0:471, 1:632, 2:562, 3:249, 4:74, 5:15, 6:2, 7:0, 8:0

### LONG (26)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ACA | 4 | 0 | no | x |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| AES | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| AME | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMN | 4 | 0 | no | x |  |  |  |  | x | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| AMRX | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| APH | 3 | 0 | yes | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| ARW | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AVPT | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| BRZE | 3 | 0 | no |  |  |  | x | x |  | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| DSGR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| EFOR | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| FTNT | 4 | 0 | no | x | x |  |  |  | x |  | x |  |  |  |  |  |  |  |  |  |  |  | x |
| HHH | 3 | 0 | no |  | x |  | x |  | x | ? |  |  | ? |  |  |  |  | ? |  |  |  |  | x |
| HNGE | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| JOYY | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| KEYS | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LAZR | 3 | 0 | no | x |  | ? |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  | ? |  |  |
| MTD | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| NVGS | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| OMDA | 3 | 0 | no |  | x |  | x |  |  | ? | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| OPY | 3 | 0 | no | x |  |  | x |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PRLB | 3 | 0 | no | x |  |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| SCSC | 4 | 0 | yes | x | x |  |  |  |  | x | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| TK | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| TWLO | 3 | 0 | no | x | x |  |  |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VEON | 3 | 0 | no | x | x |  |  |  |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |

### SHORT (182)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAL | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| ABVX | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| ACAD | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? | x |  |  |  |  | x |  |  |  |  |
| AEE | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x | x |  |  |  | x |
| AEM | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  | x |  | x |  |  |  |  | x |
| AFG | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| AHR | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| AIZ | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  |
| AKAM | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| AMT | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  |  | x |
| APLD | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| ATO | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x | x |  | x |  | x |
| AVA | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | x |  |  | x |  |  |
| AXP | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x |  | x |  |  |  | x |
| AYI | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| AZO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| BABA | 0 | 5 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  | x | ? | x |  |  | x | x |
| BAC | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  |  | x | ? | x |  |  | x | x |
| BCE | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x |  |  |  |  | x |
| BDX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| BEPC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  | x |  |  |
| BHF | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  | x |
| BIDU | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| BILI | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? | x |  |  |  |  |
| BILL | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| BIRK | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  |  |  |  |  |  | x |
| BMO | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| BMRN | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| CACC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | ? |  |  |  | x | x |  |  |  | x |
| CALM | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  | x |
| CAR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  | x |  |  |  |  |
| CB | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| CBRS | 0 | 4 | no |  |  | ? |  |  |  | ? |  | x |  | x | x |  |  | ? | x | x |  | x | x |
| CC | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  |  |
| CELH | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| CFR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| CINF | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| CLSK | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| CM | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| CMPS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| CNA | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| CNX | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  |  |  |  |
| COF | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  | x |  |  | x |  | x |  |  |  | x |
| CP | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| CPT | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x |  | x |  |  |  | x |
| CRCL | 0 | 4 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? | x |  |  |  | x |
| CTAS | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| CWT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? |  |  |  | x | x | x |  |  |  |  |
| DG | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  | x |
| DKNG | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  | x |  |  |  | x |
| DOC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| DOLE | 0 | 4 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  | x | x | x |  |  |  |  |
| DOW | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  |  | x | x |  |  |  |  | x |
| DPZ | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  | x |  |  |  | x |
| DTM | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  | x |
| DUK | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | x | x |  |  |  | x |
| ED | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| EIX | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| ENB | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x | x |  |  |  | x |
| EPRT | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  | x |
| ERIE | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| ESTA | 0 | 4 | yes |  |  |  |  |  |  |  |  |  | x |  | x |  |  | x | x |  |  |  |  |
| FCNCA | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| FE | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? | x |  |  |  | x |
| FIGR | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| FLY | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| FOUR | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  | x |  |  |  | x |
| FOXA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  | x | x |
| FSK | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  |  | x |  |  |  |  |
| FSLR | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  | ? | x |  |  | x | x |
| FTI | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| FWONK | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  | x |
| GIL | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| GLPI | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x | x |  | x |  | x |
| GLXY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| GPN | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  |  |  |  | x |
| HD | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  |  | x |  |  |  | x |
| HRL | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  |  | x | x |  |  |  | x |
| HROW | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  | x |  |  |  | x |  |  |  |  |
| HUM | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| HUT | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  | x | x |  | ? | x |  |  |  | x |
| IBN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| IFF | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| INSM | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| IRTC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| JAZZ | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| JPM | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  |  | x | ? | x |  |  |  | x |
| KLAR | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  |  |  |  |  |  |
| KMX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| KRYS | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | x |  |  |  |  |  |
| KYMR | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| LI | 0 | 3 | yes |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| LNC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| LNTH | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| LUNR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  | x |
| MAA | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x |  | x |  |  |  | x |
| MARA | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| MCO | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  | x |
| MDGL | 0 | 4 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x | x | x |  |  |  |  | x |
| MELI | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  | x |
| MET | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| META | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| MGM | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  | x |  | x |
| MKL | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  |  | x | x |  |  |  | x |
| MMS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? |  |  |  |  | x |
| MP | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  |  |  |  |  |  | x |
| MSDL | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  |  |
| NE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| NFLX | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| NHI | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x | x |  |  |  |  |
| NN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  |  |
| NOC | 0 | 3 | yes |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  |  |  |  | x |
| NXST | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| O | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  | x |  | x |  | x |
| OGS | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? | x |  |  |  | x |
| OKE | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| OKLO | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| ORCL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  | x | x |
| ORI | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  |  |
| PBA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | x |  |  |  |  | x |
| PCG | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  | x |  | x |
| PEP | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  | x |  |  |  | x |  | x |
| PFSI | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  | x |  | x |
| PGY | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| PIPR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  |  |  | x | ? | x |  |  |  | x |
| PL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| PLD | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x | x |  |  |  | x |
| PLNT | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  | x |  | x |
| PNC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| POST | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| PRI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  |  |
| PRU | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| PURR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| QCOM | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| QSR | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  | x |
| QURE | 0 | 5 | no |  |  |  |  |  |  | ? |  |  | x | x | x | x |  | ? | x |  |  |  | x |
| RCI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| RCUS | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  |  | ? | x |  |  |  |  |
| RDN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | x |  |  |  |  | x |
| RGTI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| RIOT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| RJF | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  | x |  |  |  | x |
| ROST | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| RRC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| RRR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| RY | 0 | 3 | yes |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  | x |
| SAIC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| SAM | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  |  |
| SAN | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  | x |
| SEDG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| SF | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x |  | x |  |  |  | x |
| SKT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | x |  |  |  |  |  |
| SLGN | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| SLS | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  | x |
| SMG | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  |  |
| SNEX | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| SUI | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  | x |  |  |  | x |
| SUPN | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| SW | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| SYF | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| TEM | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| THO | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? | x |  |  |  | x |
| TKO | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x | ? | x |  |  |  | x |
| TSCO | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | x |  |  |  |  | x |
| TTE | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  |  |  | x | x | ? | x |  |  |  | x |
| UMAC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| UPST | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  | x |  |  |  | x |
| USAR | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| UUUU | 0 | 5 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  | x |  |  |  | x |
| UVV | 0 | 3 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  |  | x | x |  | x |  | x |
| VICI | 0 | 5 | no |  |  |  |  |  |  |  |  | x |  | x |  |  | x | x | x |  | x |  | x |
| VKTX | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x | x | x | x |  | ? |  |  |  |  | x |
| VMC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  |  | x |  |  |  | x |
| VMRK | 0 | 4 | no |  |  |  |  |  |  |  |  | x | ? |  |  |  | x | x | x |  |  |  | x |
| VSEC | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| WCN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  |  |  | x |  | x |  |  |  | x |
| WD | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | ? |  | x |  |  | ? | x |  | x |  |  |
| WDAY | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x |  |  |  | x |
| WMT | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x |  |  |  | ? | x |  |  |  | x |
| WPC | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  |  |  | x |  | x |  |  |  | x |
| WULF | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| YELP | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | ? | x | x |  |  |  |  |  | x |  |  |

### VOL (0)
_none_

CONFLICT (logged only, never a basket, DESIGN/110 §3): 63.

Ledger: emitted 208 (skipped 0), graded 484; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
