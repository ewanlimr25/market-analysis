# S-A daily — 2026-11-13 (S3)

Preflight: clear

## Tonight's candidates (2)
| ticker | variant | structure | expiry | k | k_up | k_dn | credit_entry | credit_net_pct | risk_usd | contracts | entry_tier_max | cap_pass |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BIDU | A1 | IC | 2026-11-20T00:00:00.000 | 78.00 | 93.00 | 63.00 | 5.42 | +6.59% | 957.85 | 1 | 3 | yes |
| BIDU | A1 | SS | 2026-11-20T00:00:00.000 | 78.00 | — | — | 5.48 | +6.74% | 1,655.32 | 1 | 1 | yes |

## Suppressed (19)
| ticker | variant | first_fail |
|---|---|---|
| ARMK | A1 | F5 |
| ARMK | A2 | F5 |
| BEKE | A1 | F5 |
| BEKE | A2 | F5 |
| BIDU | A2 | A2_sector |
| BXDC | A1 | F3 |
| BXDC | A2 | F3 |
| HTHT | A1 | F5 |
| HTHT | A2 | F5 |
| PERI | A1 | F3 |
| PERI | A2 | F3 |
| POET | A1 | F2 |
| POET | A2 | F2 |
| TSN | A1 | F6 |
| TSN | A2 | F6 |
| USDE | A1 | F2 |
| USDE | A2 | F2 |
| XPEV | A1 | F2 |
| XPEV | A2 | F2 |

## Exploration book tonight (6; one contract per structure for every priceable event, filters ignored, first failing filter recorded)
| ticker | structure | expiry | k | credit_entry | credit_net_pct | risk_usd | gate_verdict |
|---|---|---|---|---|---|---|---|
| BIDU | SS | 2026-11-20T00:00:00.000 | 78.00 | 5.48 | +6.74% | 1,655.32 | PASS |
| BIDU | IC | 2026-11-20T00:00:00.000 | 78.00 | 5.42 | +6.59% | 957.85 | PASS |
| TSN | SS | 2026-11-20T00:00:00.000 | 60.00 | 3.55 | +5.51% | 792.34 | F6 |
| TSN | IC | 2026-11-20T00:00:00.000 | 60.00 | 3.45 | +5.27% | 654.77 | F6 |
| XPEV | SS | 2026-11-20T00:00:00.000 | 9.50 | 0.79 | +7.97% | 241.09 | F2 |
| XPEV | IC | 2026-11-20T00:00:00.000 | 9.50 | 0.75 | +7.29% | 174.64 | F2 |

## Graded today (3)
| ticker | variant | structure | role | net_pct | net_usd | exit_tier_max | model_exit |
|---|---|---|---|---|---|---|---|
| ARWR | A1 | SS | exploration | -2.97% | -140.16 | 2 | no |
| CBRS | A1 | SS | exploration | -3.45% | -338.23 | 1 | no |
| DLO | A1 | SS | exploration | +2.78% | 38.08 | 1 | no |

## Season to date (forward ledger)
| policy_id | role | variant | structure | n | dates | mean_net_pct | t | net_usd_total |
|---|---|---|---|---|---|---|---|---|
| sa-1.0 | champion | A1 | IC | 8 | 6 | +0.63% | 1.12 | 245.49 |
| sa-1.0 | champion | A1 | SS | 32 | 15 | -0.77% | -0.98 | -1,477.88 |
| sa-1.0 | champion | A2 | IC | 7 | 5 | +0.66% | 1.00 | 233.18 |
| sa-1.0 | champion | A2 | SS | 25 | 14 | -0.53% | -0.54 | -372.47 |
| sa-1.0 | exploration | A1 | IC | 58 | 23 | -1.11% | -1.67 | -9,252.44 |
| sa-1.0 | exploration | A1 | SS | 286 | 28 | -0.97% | -3.41 | -25,430.76 |

Ledger: emitted 2 (skipped 0), exploration 6 (skipped 0), graded 3; ledger open.

## S-B state
Gate (2026-11-13, from 2026-11-12 closes): SPY OFF:G2 (VIX 18.7, VIX3M 20.06, X 18.7 vs median 18.735) · QQQ ON (VIX 18.7, VIX3M 20.06, X 28.55 vs median 26.935)

Next session (2026-11-16, from 2026-11-13 closes): SPY ON (VIX 19.3, VIX3M 20.62, X 19.3 vs median 18.865000000000002) · QQQ ON (VIX 19.3, VIX3M 20.62, X 29.38 vs median 27.715)

CBOE refresh: ok through 2026-11-13; index-vol through 2026-11-13

Entry day: yes.

### S-B positions tonight (2)
| underlying | structure | expiry | k_p1 | k_p2 | k_c1 | k_c2 | credit_entry | max_loss_usd | contracts | entry_tier_max |
|---|---|---|---|---|---|---|---|---|---|---|
| QQQ | PS | 2026-12-04 | 630.00 | 575.00 | — | — | 2.97 | 5,203.45 | 1 | 1 |
| QQQ | IC | 2026-12-04 | 630.00 | 575.00 | 728.00 | 770.00 | 4.34 | 5,066.36 | 1 | 1 |

### S-B skipped (2)
| underlying | structure | reason |
|---|---|---|
| SPY | PS | OFF:G2 |
| SPY | IC | OFF:G2 |

### S-B exploration book tonight (4; one contract per sleeve, gate ignored, gate verdict recorded)
| underlying | structure | expiry | k_p1 | k_p2 | k_c1 | k_c2 | credit_entry | max_loss_usd | gate_verdict |
|---|---|---|---|---|---|---|---|---|---|
| SPY | PS | 2026-12-04 | 720.00 | 685.00 | — | — | 1.71 | 3,328.71 | OFF:G2 |
| SPY | IC | 2026-12-04 | 720.00 | 685.00 | 790.00 | 830.00 | 2.04 | 3,795.83 | OFF:G2 |
| QQQ | PS | 2026-12-04 | 630.00 | 575.00 | — | — | 2.97 | 5,203.45 | ON |
| QQQ | IC | 2026-12-04 | 630.00 | 575.00 | 728.00 | 770.00 | 4.34 | 5,066.36 | ON |

### S-B graded at expiry today (6)
| underlying | structure | entry | expiry | settle_close | net_usd | ror | role |
|---|---|---|---|---|---|---|---|
| SPY | PS | 2026-10-23 | 2026-11-13 | 754.37 | 196.74 | +5.18% | champion |
| QQQ | PS | 2026-10-23 | 2026-11-13 | 679.89 | 303.42 | +7.24% | champion |
| QQQ | IC | 2026-10-23 | 2026-11-13 | 679.89 | 469.34 | +11.67% | champion |
| SPY | PS | 2026-10-23 | 2026-11-13 | 754.37 | 196.74 | +5.18% | exploration |
| QQQ | PS | 2026-10-23 | 2026-11-13 | 679.89 | 303.42 | +7.24% | exploration |
| QQQ | IC | 2026-10-23 | 2026-11-13 | 679.89 | 469.34 | +11.67% | exploration |

Open positions: QQQ-IC 2, QQQ-PS 2, SPY-IC 1, SPY-PS 1

### S-B forward ledger to date
| policy_id | role | sleeve | n | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|---|
| sb-1.0 | champion | QQQ-IC | 5 | +1.18% | 0.35 | 243.94 |
| sb-1.0 | champion | QQQ-PS | 6 | -11.12% | -1.35 | -2,499.87 |
| sb-1.0 | champion | SPY-IC | 2 | — | — | 372.65 |
| sb-1.0 | champion | SPY-PS | 5 | +4.97% | 34.99 | 755.37 |
| sb-1.0 | exploration | QQQ-IC | 5 | +1.18% | 0.35 | 243.94 |
| sb-1.0 | exploration | QQQ-PS | 7 | -8.55% | -1.02 | -2,287.68 |
| sb-1.0 | exploration | SPY-IC | 4 | +6.91% | 31.77 | 724.42 |
| sb-1.0 | exploration | SPY-PS | 7 | +4.94% | 29.94 | 999.78 |

S-B ledger: emitted 2 (skipped 0), exploration 4 (skipped 0), graded 6; ledger open.


## S-C state
Entry day: yes; ledger open.

Stopped at: F1 2253 · F2 1144 · F3 986 · F4 721 · F7 111 · F5 90 · F6 178 · F8 485 · F9 1; C1:selected 2 · C2:selected 2

### S-C positions tonight (8; paper, before the read)
| variant | rank | ticker | sector | structure | close | iv30d | expiry | dte_cal | k | k_up | k_dn | credit_entry | max_loss_usd | stress_loss_usd | entry_cost_usd | contracts | sigma_hold | cap_pass | cap_reason |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 | 1 | RIVN | Consumer Cyclical | IB | 12.20 | 0.60 | 2026-12-11 | 28 | 12.00 | 16.50 | 8.00 | 1.55 | 295.48 | — | 8.32 | 1 | 2.04 | yes | — |
| C1 | 2 | PBF | Energy | IB | 71.28 | 0.63 | 2026-12-18 | 35 | 70.00 | 100.00 | 42.50 | 10.66 | 1,934.05 | — | 30.01 | 1 | 13.86 | no | cap_budget |
| C1 | 1 | RIVN | Consumer Cyclical | SS | 12.20 | 0.60 | 2026-12-11 | 28 | 12.00 | — | — | 1.64 | — | 467.72 | 10.01 | 2 | 2.04 | yes | — |
| C1 | 2 | PBF | Energy | SS | 71.28 | 0.63 | 2026-12-18 | 35 | 70.00 | — | — | 11.02 | — | 3,184.35 | 26.73 | 1 | 13.86 | no | cap_budget |
| C2 | 1 | RIVN | Consumer Cyclical | IB | 12.20 | 0.60 | 2026-12-11 | 28 | 12.00 | 16.50 | 8.00 | 1.55 | 295.48 | — | 8.32 | 1 | 2.04 | yes | — |
| C2 | 2 | PBF | Energy | IB | 71.28 | 0.63 | 2026-12-18 | 35 | 70.00 | 100.00 | 42.50 | 10.66 | 1,934.05 | — | 30.01 | 1 | 13.86 | no | cap_budget |
| C2 | 1 | RIVN | Consumer Cyclical | SS | 12.20 | 0.60 | 2026-12-11 | 28 | 12.00 | — | — | 1.64 | — | 467.72 | 10.01 | 2 | 2.04 | yes | — |
| C2 | 2 | PBF | Energy | SS | 71.28 | 0.63 | 2026-12-18 | 35 | 70.00 | — | — | 11.02 | — | 3,184.35 | 26.73 | 1 | 13.86 | no | cap_budget |

Exploration book: 43 priceable names at one contract each, by first failing filter: F1 10, F2 3, F3 21, F4 1, F5 3, F6 2, F9 1, PASS 2

### S-C graded at expiry (0)
_none due_

### S-C open book (S-B open: yes; the 40% budget binds only then)
| pair | positions | open_risk_usd | budget_usd | max_sector_positions |
|---|---|---|---|---|
| C1-SS | 5 | 6,592.89 | 8,000.00 | 3 |
| C1-IB | 4 | 3,051.64 | 4,000.00 | 3 |
| C2-SS | 4 | 5,906.04 | 8,000.00 | 3 |
| C2-IB | 5 | 3,405.73 | 4,000.00 | 3 |

### S-C forward ledger to date (entry-week series)
| policy_id | role | pair | n | weeks | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|---|---|
| sc-1.0 | champion | C1-SS | 6 | 2 | — | — | -1,362.15 |
| sc-1.0 | champion | C1-IB | 6 | 2 | — | — | -1,519.19 |
| sc-1.0 | champion | C2-SS | 5 | 2 | — | — | -1,091.11 |
| sc-1.0 | champion | C2-IB | 5 | 2 | — | — | -1,236.18 |
| sc-1.0 | exploration | C1-SS | 197 | 3 | -12.29% | -3.69 | -237,221.66 |
| sc-1.0 | exploration | C1-IB | 197 | 3 | -21.29% | -3.98 | -211,937.98 |

Progress to the read: graded entry-weeks 2 of 40 (C1-SS), 2 of 40 (C1-IB), 2 of 40 (C2-SS), 2 of 40 (C2-IB)

S-C ledger: emitted 8 (skipped 0), exploration 86 (skipped 0), graded 110.


## Watch basket (wb-1.0, exploration, paper only)
Universe: 1981 names.
Borrow snapshot: 2026-11-13 (the session's own); fee known for 1976 names.
Bull counts: 0:841, 1:673, 2:313, 3:144, 4:10, 5:0, 6:0, 7:0, 8:0
Bear counts: 0:744, 1:755, 2:343, 3:106, 4:29, 5:4, 6:0, 7:0, 8:0

### LONG (85)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ABM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| AIZ | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMGN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| AMTB | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| ASND | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| BIIB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BLK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| BRKB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  | x | x |
| BUD | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| BY | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| CAH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CE | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| CHT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| CL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CME | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| CNA | 3 | 0 | yes |  | x |  |  | x |  | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| COR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| COST | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| CRBG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| DEO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| DOLE | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| DRH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| ECL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| EGBN | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| EHC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  |  |
| EW | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| FAST | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| FLYW | 3 | 0 | no | x | x |  |  |  |  |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| GWW | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HDB | 3 | 0 | yes |  | x | x |  |  | x | ? |  |  |  |  |  |  |  |  |  |  |  |  | x |
| HG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| HII | 3 | 0 | no |  |  |  |  | x | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| HUM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| HZO | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| IBN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| ICE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| IDT | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  |  |
| JNJ | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| KO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LIN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| LLY | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  | x | x |
| LNTH | 3 | 0 | no |  |  |  |  |  | x | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| MA | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MDLZ | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MDT | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| MEOH | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MET | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| MRSH | 3 | 0 | no | x | x |  |  |  | x | ? |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| MSCI | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  | ? |  |  |  |  | x |
| MSI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| NATL | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| NJR | 3 | 0 | yes |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| NWE | 3 | 0 | no | x |  |  |  |  | x |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| NWN | 3 | 0 | no |  | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| PG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| PGR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| R | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RDY | 3 | 0 | no |  | x |  |  |  | x | x |  |  | ? |  |  |  |  |  |  |  |  |  | x |
| RLJ | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| RPRX | 4 | 0 | no | x | x |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| RSG | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SAIC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| SEIC | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| SGRY | 3 | 0 | no | x | x |  |  |  |  |  | x |  | ? |  |  |  |  |  |  |  |  |  | x |
| SHO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| SIGI | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| SMA | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| SPNT | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| STE | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| STT | 3 | 0 | no |  |  | x | x |  |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| TAK | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| TEVA | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  |  |  |  |  |  | x |
| TRMK | 4 | 0 | no | x | x |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  | x |
| UVE | 3 | 0 | no | x |  |  |  |  | x | ? | x |  | ? |  |  |  |  | ? |  |  |  |  |  |
| VCTR | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  |  |
| VLTO | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| VRNS | 3 | 0 | no | x |  |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  | x |
| WAB | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WCN | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WM | 3 | 0 | no | x |  |  |  |  | x | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |
| WTRG | 3 | 0 | no | x |  |  |  |  | x | x |  |  |  |  |  |  |  |  |  |  |  |  | x |
| ZWS | 4 | 0 | no |  | x |  | x | x |  | ? | x |  |  |  |  |  |  | ? |  |  |  |  | x |

### SHORT (83)
| ticker | bull | bear | episode | C-HIGH | C-IVUP | C-DIV | C-DIV-D | C-AVWAP | C-POC | C-POC-A | C-SWING | C-LOW | C-SHORT | C-OIBUILD | C-CROWD | C-AVWAP-LOSS | C-POC-LOSS | C-POC-A-LOSS | C-SWING-LOSS | C-VOL | C-RSI | C-LEAP | C-DP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| AI | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  | ? |  |  |  |  |  |
| APLD | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| ASTS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| AXON | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| AXTI | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  |  | x |
| BA | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| BC | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| BHVN | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| BIDU | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| BILI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| BMNR | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| BRKR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| BX | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| BXMT | 0 | 3 | yes |  |  |  |  |  |  |  |  | x | ? |  | x |  |  | ? | x |  | x |  |  |
| BXP | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| CBRS | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  |  |  |  |  | x | x |
| CELC | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| CGON | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| CLMT | 0 | 3 | no |  |  |  |  |  |  |  |  |  | ? | x | x |  |  |  | x |  |  |  |  |
| CRCL | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| CRSP | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  | x |
| CVLT | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| DLO | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| DOX | 0 | 3 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? |  |  |  |  |  |
| DRTS | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| DVA | 0 | 4 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x | x | ? | x |  |  |  | x |
| EC | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| ELVN | 0 | 3 | yes |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| ENPH | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? |  |  |  |  | x |
| FICO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| FIG | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| FLG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  | x |  |  |
| HIMS | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x | x | x |  |  | ? | x |  |  |  | x |
| HYMC | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  |  |
| IMAX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| INOD | 0 | 4 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  | ? | x |  |  |  |  |
| INVA | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | ? |  |  |  | x | ? | x |  |  |  |  |
| IONQ | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  |  | x |
| IONS | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x |  | x |  |  | ? | x |  | x |  | x |
| IREN | 0 | 3 | no |  |  |  |  |  |  |  |  | x |  | x | x |  |  |  |  |  |  | x | x |
| LINE | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| LKQ | 0 | 4 | yes |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? | x |  |  |  |  |
| LUNR | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  |  | x |
| LYFT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| MATX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| MGA | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| MLYS | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  |  |  | x |  |  |
| MP | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x | x |  |  | ? |  |  |  |  | x |
| MSTR | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| NEO | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| NFLX | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  |  | x | x |
| NKE | 0 | 3 | no |  |  |  |  |  |  |  |  |  |  | x | x |  |  | ? | x |  |  | x | x |
| NOVT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| NRIX | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  | x |  |  | ? | x |  |  |  |  |
| OKLO | 0 | 4 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? | x |  | x |  | x |
| ONON | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  |  | x |
| ORCL | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| PAGP | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x | x |  |  | x | ? |  |  |  |  |  |
| PBI | 0 | 4 | no |  |  |  |  |  |  |  |  |  | x |  | x |  | x | ? | x |  |  |  |  |
| PDD | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? |  |  |  |  | x |
| PTGX | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| QXO | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x | x |  |  |  | ? |  |  |  |  | x |
| RDDT | 0 | 4 | no |  |  |  |  |  |  |  |  | x | x | x | x |  |  |  |  |  |  |  | x |
| RIVN | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x | x |  |  | x |
| RLAY | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  | x | x |  | ? |  |  |  |  |  |
| S | 0 | 3 | no |  |  |  |  |  |  | ? |  |  |  | x |  | x |  | ? | x |  |  |  | x |
| SEDG | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  |  | x |  |  | ? | x |  |  |  | x |
| SGI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  | x | ? |  |  |  |  | x |
| SHC | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  |  | x | ? | x |  |  |  | x |
| SLG | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| SOFI | 0 | 3 | no |  |  |  |  |  |  | ? |  | x |  | x | x |  |  | ? |  |  |  | x | x |
| SRPT | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| SYF | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  | x |
| SYM | 0 | 3 | no |  |  |  |  |  |  | ? |  | x | x |  |  |  |  | ? | x |  |  |  |  |
| TECK | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  | x |  |  |  | x | ? | x |  |  |  |  |
| TEM | 0 | 3 | yes |  |  |  |  |  |  | ? |  |  |  | x | x | x |  | ? |  |  |  | x | x |
| TREX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| UPST | 0 | 5 | no |  |  |  |  |  |  | ? |  | x | x | x | x |  |  | ? | x |  |  |  |  |
| VSAT | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| WHR | 0 | 4 | no |  |  |  |  |  |  | ? |  | x | x |  | x |  |  | ? | x |  |  |  | x |
| WIX | 0 | 3 | no |  |  |  |  |  |  | ? |  |  | x |  |  | x |  | ? | x |  |  |  |  |
| YPF | 0 | 3 | no |  |  |  |  |  |  |  |  |  | x | x |  |  |  |  | x |  |  |  | x |

### VOL (0)
_none_

CONFLICT (logged only, never a basket, DESIGN/110 §3): 62.

Ledger: emitted 168 (skipped 0), graded 468; ledger open.

Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 §6); nothing here is a trade.
