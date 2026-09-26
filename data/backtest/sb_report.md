# S-B backtest report (generated)


## Inputs

- refreshed: {'index_vol_through': '2026-09-25', 'prices_through': '2026-09-25'}
- proxy: {'index_vol': ['1990-01-02', '2026-09-25'], 'sessions': ['2023-09-26', '2026-09-25'], 'n_sessions': 753}
- marked: {'panel': ['2026-03-13', '2026-09-25'], 'n_entry_sessions': 29}


## Gate ON share of entry sessions (proxy, by year)

| underlying | year | entry_sessions | gate_on | on_share |
|---|---|---|---|---|
| QQQ | 2023 | 10 | 2 | +20.00% |
| QQQ | 2024 | 52 | 26 | +50.00% |
| QQQ | 2025 | 52 | 15 | +28.85% |
| QQQ | 2026 | 36 | 15 | +41.67% |
| QQQ | all | 150 | 58 | +38.67% |
| SPY | 2023 | 10 | 2 | +20.00% |
| SPY | 2024 | 52 | 25 | +48.08% |
| SPY | 2025 | 52 | 16 | +30.77% |
| SPY | 2026 | 36 | 17 | +47.22% |
| SPY | all | 150 | 60 | +40.00% |


## Proxy: mean net return on risk per position; NW(lag 2) t and expiry-clustered t

| sleeve | window | n | expiries | mean_ror | median_ror | hit | nw_t | nw_p | cl_t | cl_p | net_usd_total | mean_credit_over_width | mean_cost_over_credit | mean_x | mean_risk_usd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | P1 | 20 | 20 | +2.17% | +5.47% | +95.00% | 0.7054 | 0.4891 | 0.6500 | 0.5235 | 1,200 | +5.40% | +3.64% | 15.62 | 2,000 |
| SPY-IC | P1 | 20 | 20 | -5.30% | +7.48% | +70.00% | -0.9741 | 0.3422 | -0.9112 | 0.3736 | -2,859 | +7.54% | +5.03% | 15.62 | 2,265 |
| QQQ-PS | P1 | 21 | 21 | +0.89% | +6.10% | +95.24% | 0.1894 | 0.8517 | 0.1767 | 0.8615 | 398.34 | +5.89% | +3.21% | 19.71 | 1,922 |
| QQQ-IC | P1 | 21 | 21 | -8.41% | +10.15% | +76.19% | -1.06 | 0.3013 | -1.05 | 0.3060 | -3,670 | +9.72% | +3.56% | 19.71 | 1,995 |
| SPY-PS | P2 | 14 | 14 | +5.14% | +5.68% | +92.86% | 10.81 | 0.0000 | 9.41 | 0.0000 | 1,739 | +5.52% | +2.80% | 18.13 | 2,436 |
| SPY-IC | P2 | 14 | 14 | +6.80% | +7.96% | +92.86% | 9.55 | 0.0000 | 8.25 | 0.0000 | 2,229 | +7.70% | +3.88% | 18.13 | 2,387 |
| QQQ-PS | P2 | 14 | 14 | +6.19% | +6.22% | +100.00% | 188.56 | 0.0000 | 139.83 | 0.0000 | 2,118 | +6.02% | +2.63% | 21.16 | 2,443 |
| QQQ-IC | P2 | 14 | 14 | +7.55% | +10.51% | +92.86% | 2.58 | 0.0227 | 2.48 | 0.0276 | 2,417 | +9.87% | +2.90% | 21.16 | 2,356 |
| SPY-PS | P3 | 26 | 26 | +5.14% | +5.73% | +96.15% | 10.08 | 0.0000 | 9.09 | 0.0000 | 3,801 | +5.53% | +2.57% | 18.19 | 2,848 |
| SPY-IC | P3 | 26 | 26 | +6.89% | +8.01% | +92.31% | 10.09 | 0.0000 | 8.82 | 0.0000 | 4,955 | +7.67% | +3.55% | 18.19 | 2,791 |
| QQQ-PS | P3 | 23 | 23 | +6.30% | +6.35% | +100.00% | 142.42 | 0.0000 | 179.41 | 0.0000 | 5,008 | +6.05% | +2.16% | 24.04 | 3,443 |
| QQQ-IC | P3 | 23 | 23 | +10.14% | +10.70% | +95.65% | 20.01 | 0.0000 | 18.83 | 0.0000 | 7,790 | +9.87% | +2.35% | 24.04 | 3,326 |
| SPY-PS | pooled | 60 | 60 | +4.15% | +5.64% | +95.00% | 3.75 | 0.0004 | 3.63 | 0.0006 | 6,740 | +5.49% | +2.98% | 17.32 | 2,469 |
| SPY-IC | pooled | 60 | 60 | +2.80% | +7.88% | +85.00% | 1.30 | 0.1986 | 1.34 | 0.1838 | 4,325 | +7.63% | +4.12% | 17.32 | 2,521 |
| QQQ-PS | pooled | 58 | 58 | +4.32% | +6.21% | +98.28% | 2.38 | 0.0205 | 2.35 | 0.0221 | 7,524 | +5.98% | +2.65% | 21.77 | 2,651 |
| QQQ-IC | pooled | 58 | 58 | +2.80% | +10.48% | +87.93% | 0.8090 | 0.4219 | 0.8862 | 0.3792 | 6,537 | +9.82% | +2.92% | 21.77 | 2,610 |


## BH(0.10) across the four sleeves (proxy, pooled, on the NW p)

| sleeve | n | mean_ror | nw_t | nw_p | bh_pass |
|---|---|---|---|---|---|
| SPY-PS | 60 | +4.15% | 3.75 | 0.0004 | yes |
| SPY-IC | 60 | +2.80% | 1.30 | 0.1986 | no |
| QQQ-PS | 58 | +4.32% | 2.38 | 0.0205 | yes |
| QQQ-IC | 58 | +2.80% | 0.8090 | 0.4219 | no |


## Deflated Sharpe (6 trials) — proxy pooled

| sleeve | n | sr | sr_star | deflated_sr | dsr_prob | sr_star_null | deflated_sr_null | dsr_prob_null | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 60 | 0.4686 | 0.2039 | 0.2647 | 0.7730 | 0.1707 | 0.2979 | 0.8003 | -7.15 | 56.08 |
| SPY-IC | 60 | 0.1736 | 0.2039 | -0.0303 | 0.4336 | 0.1707 | 0.0029 | 0.5064 | -4.39 | 24.14 |
| QQQ-PS | 58 | 0.3089 | 0.2039 | 0.1050 | 0.6415 | 0.1707 | 0.1382 | 0.6834 | -7.61 | 60.91 |
| QQQ-IC | 58 | 0.1164 | 0.2039 | -0.0876 | 0.2907 | 0.1707 | -0.0543 | 0.3661 | -3.39 | 13.92 |


## Deflated Sharpe (6 trials) — proxy P1

| sleeve | n | sr | sr_star | deflated_sr | dsr_prob | sr_star_null | deflated_sr_null | dsr_prob_null | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 20 | 0.1453 | 0.2387 | -0.0934 | 0.3797 | 0.2907 | -0.1454 | 0.3167 | -4.47 | 22.99 |
| SPY-IC | 20 | -0.2038 | 0.2387 | -0.4425 | 0.0058 | 0.2907 | -0.4945 | 0.0024 | -2.43 | 8.72 |
| QQQ-PS | 21 | 0.0386 | 0.2387 | -0.2002 | 0.2054 | 0.2907 | -0.2522 | 0.1501 | -4.58 | 23.97 |
| QQQ-IC | 21 | -0.2292 | 0.2387 | -0.4680 | 0.0042 | 0.2907 | -0.5200 | 0.0017 | -1.83 | 4.93 |


## Deflated Sharpe (6 trials) — proxy P2

| sleeve | n | sr | sr_star | deflated_sr | dsr_prob | sr_star_null | deflated_sr_null | dsr_prob_null | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 14 | 2.52 | 23.15 | -20.64 | 0.0000 | 0.3475 | 2.17 | 0.9058 | -3.71 | 16.80 |
| SPY-IC | 14 | 2.20 | 23.15 | -20.95 | 0.0000 | 0.3475 | 1.86 | 0.9662 | -2.32 | 7.03 |
| QQQ-PS | 14 | 37.37 | 23.15 | 14.22 | 0.9737 | 0.3475 | 37.02 | 1.0000 | -0.8537 | 2.91 |
| QQQ-IC | 14 | 0.6626 | 23.15 | -22.49 | 0.0000 | 0.3475 | 0.3151 | 0.6903 | -3.74 | 16.98 |


## Deflated Sharpe (6 trials) — proxy P3

| sleeve | n | sr | sr_star | deflated_sr | dsr_prob | sr_star_null | deflated_sr_null | dsr_prob_null | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 26 | 1.78 | 22.75 | -20.96 | 0.0000 | 0.2711 | 1.51 | 0.9089 | -5.07 | 28.78 |
| SPY-IC | 26 | 1.73 | 22.75 | -21.02 | 0.0000 | 0.2711 | 1.46 | 0.9663 | -3.36 | 13.14 |
| QQQ-PS | 23 | 37.41 | 22.75 | 14.66 | 0.9980 | 0.2711 | 37.14 | 1.0000 | -0.4577 | 2.58 |
| QQQ-IC | 23 | 3.93 | 22.75 | -18.82 | 0.0000 | 0.2711 | 3.66 | 0.9452 | -4.75 | 25.70 |


## PBO (CSCV over 16 entry blocks, proxy pooled)

- pbo: 0.5073038073038073
- mean_logit: -0.13913884806440033
- n_combinations: 12870
- n_configs: 4
- n_blocks: 16
- n_entries: 64


## Month rule (proxy; worst expiry-month vs median month, $ at frozen sizing)

| sleeve | n_months | median_month_usd | worst_month | worst_month_usd | worst_over_median | months_negative | month_rule_pass |
|---|---|---|---|---|---|---|---|
| SPY-PS | 28 | 241.49 | 2024-08 | -396.47 | 1.64 | 2 | yes |
| SPY-IC | 28 | 251.10 | 2023-11 | -1,722 | 6.86 | 5 | no |
| QQQ-PS | 28 | 271.59 | 2024-08 | -1,325 | 4.88 | 1 | no |
| QQQ-IC | 28 | 409.24 | 2023-11 | -1,812 | 4.43 | 5 | no |


## Tail report (proxy, pooled)

| sleeve | n | mean_ror | worst_ror | worst_entry | best_ror | mean_win_ror | worst_decile_share_of_loss | full_width_losses | mean_without_worst_1pct | mean_without_best_1pct | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 60 | +4.15% | -61.38% | 2024-07-12 | +6.12% | +5.64% | 1.00 | 0 | +5.26% | +4.12% | -7.15 | 53.08 |
| SPY-IC | 60 | +2.80% | -88.96% | 2023-10-27 | +8.42% | +7.71% | 0.9363 | 0 | +4.36% | +2.71% | -4.39 | 21.14 |
| QQQ-PS | 58 | +4.32% | -100.20% | 2024-07-12 | +6.60% | +6.15% | 1.00 | 1 | +6.15% | +4.28% | -7.61 | 57.91 |
| QQQ-IC | 58 | +2.80% | -100.38% | 2023-10-27 | +11.01% | +10.35% | 0.9585 | 1 | +4.61% | +2.65% | -3.39 | 10.92 |

Worst 10 positions, SPY-PS (pooled):

| entry | expiry | x | ror | net_usd |
|---|---|---|---|---|
| 2024-07-12 | 2024-08-02 | 12.46 | -61.38% | -932.00 |
| 2026-02-27 | 2026-03-20 | 19.86 | -8.97% | -271.21 |
| 2025-02-28 | 2025-03-21 | 19.63 | -1.94% | -51.25 |
| 2024-02-16 | 2024-03-08 | 14.24 | +5.19% | 83.63 |
| 2024-06-21 | 2024-07-12 | 13.20 | +5.23% | 84.26 |
| 2024-04-05 | 2024-04-26 | 16.03 | +5.27% | 94.91 |
| 2024-03-15 | 2024-04-05 | 14.41 | +5.32% | 85.71 |
| 2024-01-19 | 2024-02-09 | 13.30 | +5.34% | 151.77 |
| 2024-05-31 | 2024-06-21 | 12.92 | +5.34% | 80.95 |
| 2025-08-22 | 2025-09-12 | 14.22 | +5.36% | 111.71 |

Worst 10 positions, QQQ-PS (pooled):

| entry | expiry | x | ror | net_usd |
|---|---|---|---|---|
| 2024-07-12 | 2024-08-02 | 17.26 | -100.20% | -1,890 |
| 2024-07-19 | 2024-08-09 | 21.51 | +3.83% | 89.96 |
| 2024-01-26 | 2024-02-16 | 17.03 | +5.66% | 90.87 |
| 2024-01-05 | 2024-01-26 | 17.13 | +5.67% | 85.64 |
| 2024-02-02 | 2024-02-23 | 17.22 | +5.80% | 93.02 |
| 2024-03-08 | 2024-03-28 | 19.04 | +5.83% | 104.43 |
| 2025-02-28 | 2025-03-21 | 22.66 | +5.85% | 153.54 |
| 2024-02-16 | 2024-03-08 | 18.60 | +5.86% | 104.89 |
| 2024-02-23 | 2024-03-15 | 17.70 | +5.88% | 99.73 |
| 2023-12-22 | 2024-01-12 | 16.62 | +5.89% | 88.84 |


## Gate modes and sensitivities (proxy, pooled; descriptive)

| sensitivity | sleeve | n | mean_ror | nw_t | cl_t | net_usd_total | mean_cost_over_credit |
|---|---|---|---|---|---|---|---|
| base | SPY-PS | 60 | +4.15% | 3.75 | 3.63 | 6,740 | +2.98% |
| base | SPY-IC | 60 | +2.80% | 1.30 | 1.34 | 4,325 | +4.12% |
| base | QQQ-PS | 58 | +4.32% | 2.38 | 2.35 | 7,524 | +2.65% |
| base | QQQ-IC | 58 | +2.80% | 0.8090 | 0.8862 | 6,537 | +2.92% |
| gate_off | SPY-PS | 150 | +3.23% | 2.93 | 3.26 | 13,325 | +3.04% |
| gate_off | SPY-IC | 150 | +1.98% | 1.24 | 1.46 | 6,397 | +4.21% |
| gate_off | QQQ-PS | 150 | +2.74% | 1.67 | 1.99 | 13,098 | +2.70% |
| gate_off | QQQ-IC | 150 | -0.26% | -0.1002 | -0.1249 | -86.82 | +2.97% |
| g1_only | SPY-PS | 139 | +3.74% | 4.08 | 4.70 | 13,693 | +3.12% |
| g1_only | SPY-IC | 139 | +2.97% | 2.07 | 2.47 | 10,044 | +4.30% |
| g1_only | QQQ-PS | 139 | +3.15% | 1.91 | 2.38 | 13,422 | +2.75% |
| g1_only | QQQ-IC | 139 | +1.18% | 0.4586 | 0.5755 | 6,545 | +3.02% |
| g2_only | SPY-PS | 70 | +2.97% | 1.77 | 1.71 | 6,185 | +2.85% |
| g2_only | SPY-IC | 70 | +1.17% | 0.5008 | 0.4849 | 1,542 | +3.95% |
| g2_only | QQQ-PS | 68 | +3.20% | 1.57 | 1.52 | 7,013 | +2.57% |
| g2_only | QQQ-IC | 68 | +0.09% | 0.0245 | 0.0255 | 1,251 | +2.83% |
| costs_x2 | SPY-PS | 60 | +3.98% | 3.59 | 3.48 | 6,493 | +5.96% |
| costs_x2 | SPY-IC | 60 | +2.46% | 1.14 | 1.18 | 3,820 | +8.24% |
| costs_x2 | QQQ-PS | 58 | +4.15% | 2.29 | 2.26 | 7,280 | +5.31% |
| costs_x2 | QQQ-IC | 58 | +2.48% | 0.7158 | 0.7850 | 6,081 | +5.85% |
| wing_1.5 | SPY-PS | 60 | -0.58% | -0.3378 | -0.3261 | -663.01 | +19.32% |
| wing_1.5 | SPY-IC | 60 | -3.45% | -1.21 | -1.25 | -4,245 | +16.98% |
| wing_1.5 | QQQ-PS | 58 | +1.09% | 0.6109 | 0.6101 | 960.95 | +12.04% |
| wing_1.5 | QQQ-IC | 58 | -1.38% | -0.3230 | -0.3550 | -2,758 | +7.42% |


## Other structures on the proxy (descriptive; not sleeves, never a verdict input)

Single legs, naked shorts and the call spread re-priced on the same entry rows with the frozen smile and costs. Risk: debit = premium; credit spread = width - credit; naked = the 2-sigma stress loss (the matching spread's max loss), Reg-T proxy margin beside. `PS` here is the champion recomputed as a check. Drafts: `ledger/challengers/drafts/sb-c-callspread.json`, `sb-c-nakedput-margin.json`.

| set | structure | underlying | n | mean_ror | nw_t | hit | mean_pnl_usd | worst_ror | mean_premium_usd | mean_margin_usd | total_pnl_usd |
|---|---|---|---|---|---|---|---|---|---|---|---|
| gate ON | long_c1 | QQQ | 58 | +27.23% | 0.4303 | +10.34% | -9.43 | -102.60% | 117.32 | — | -546.98 |
| gate ON | long_p1 | QQQ | 58 | -75.67% | -3.10 | +1.72% | -207.83 | -101.38% | 250.28 | — | -12,054 |
| gate ON | long_c2 | QQQ | 58 | -119.47% | -75.94 | +0.00% | -8.87 | -134.00% | 7.52 | — | -514.27 |
| gate ON | long_p2 | QQQ | 58 | -87.79% | -6.18 | +1.72% | -73.34 | -103.38% | 80.56 | — | -4,254 |
| gate ON | short_p1_naked | QQQ | 58 | +6.98% | 3.07 | +98.28% | 203.07 | -124.66% | -250.28 | 7,588 | 11,778 |
| gate ON | short_c1_naked | QQQ | 58 | -1.28% | -0.4756 | +89.66% | 5.41 | -100.03% | -117.32 | 7,719 | 313.85 |
| gate ON | CS | QQQ | 58 | -1.61% | -0.5980 | +87.93% | -3.46 | -100.16% | -109.80 | — | -200.42 |
| gate ON | PS | QQQ | 58 | +4.32% | 2.38 | +98.28% | 129.73 | -100.20% | -169.72 | — | 7,524 |
| gate ON | long_c1 | SPY | 60 | +44.77% | 0.5478 | +13.33% | 9.56 | -104.68% | 58.88 | — | 573.51 |
| gate ON | long_p1 | SPY | 60 | -84.67% | -7.01 | +3.33% | -192.23 | -101.40% | 217.69 | — | -11,534 |
| gate ON | long_c2 | SPY | 60 | -148.29% | -69.44 | +0.00% | -5.48 | -173.85% | 3.77 | — | -329.09 |
| gate ON | long_p2 | SPY | 60 | -102.43% | -1,097 | +0.00% | -79.50 | -103.47% | 77.69 | — | -4,770 |
| gate ON | short_p1_naked | SPY | 60 | +7.49% | 6.82 | +96.67% | 187.98 | -57.60% | -217.69 | 9,407 | 11,279 |
| gate ON | short_c1_naked | SPY | 60 | -1.10% | -0.5970 | +86.67% | -13.48 | -89.21% | -58.88 | 9,569 | -809.00 |
| gate ON | CS | SPY | 60 | -1.32% | -0.7194 | +86.67% | -18.97 | -89.43% | -55.11 | — | -1,138 |
| gate ON | PS | SPY | 60 | +4.15% | 3.75 | +95.00% | 108.48 | -61.38% | -140.00 | — | 6,509 |
| every Friday | long_c1 | QQQ | 150 | +57.49% | 1.16 | +16.67% | 69.27 | -102.61% | 115.94 | — | 10,390 |
| every Friday | long_p1 | QQQ | 150 | -62.63% | -3.35 | +5.33% | -167.37 | -101.46% | 246.17 | — | -25,105 |
| every Friday | long_c2 | QQQ | 150 | -120.83% | -125.98 | +0.00% | -8.79 | -139.37% | 7.40 | — | -1,318 |
| every Friday | long_p2 | QQQ | 150 | -96.58% | -17.30 | +0.67% | -77.51 | -103.68% | 79.33 | — | -11,627 |
| every Friday | short_p1_naked | QQQ | 150 | +5.69% | 3.24 | +94.67% | 162.65 | -124.66% | -246.17 | 7,689 | 24,397 |
| every Friday | short_c1_naked | QQQ | 150 | -2.62% | -1.23 | +83.33% | -73.27 | -100.03% | -115.94 | 7,821 | -10,991 |
| every Friday | CS | QQQ | 150 | -2.95% | -1.38 | +82.00% | -82.06 | -100.16% | -108.54 | — | -12,309 |
| every Friday | PS | QQQ | 150 | +2.74% | 1.67 | +94.67% | 85.14 | -100.20% | -166.84 | — | 12,771 |
| every Friday | long_c1 | SPY | 150 | +37.65% | 0.7237 | +13.33% | 24.29 | -105.35% | 58.20 | — | 3,644 |
| every Friday | long_p1 | SPY | 150 | -74.52% | -6.09 | +4.67% | -163.94 | -101.52% | 214.94 | — | -24,591 |
| every Friday | long_c2 | SPY | 150 | -149.99% | -87.15 | +0.00% | -5.45 | -188.16% | 3.73 | — | -817.09 |
| every Friday | long_p2 | SPY | 150 | -102.48% | -1,493 | +0.00% | -78.31 | -103.74% | 76.50 | — | -11,746 |
| every Friday | short_p1_naked | SPY | 150 | +6.58% | 5.95 | +95.33% | 159.71 | -92.22% | -214.94 | 9,367 | 23,956 |
| every Friday | short_c1_naked | SPY | 150 | -1.00% | -0.8337 | +86.00% | -28.20 | -89.21% | -58.20 | 9,522 | -4,230 |
| every Friday | CS | SPY | 150 | -1.23% | -1.02 | +86.00% | -33.65 | -89.43% | -54.47 | — | -5,047 |
| every Friday | PS | SPY | 150 | +3.23% | 2.93 | +94.67% | 81.40 | -95.48% | -138.43 | — | 12,210 |


## Marked (panel): sleeve table

| sleeve | window | n | expiries | mean_ror | median_ror | hit | nw_t | nw_p | cl_t | cl_p | net_usd_total | mean_credit_over_width | mean_cost_over_credit | mean_x | mean_risk_usd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | P3 | 8 | 8 | +5.88% | +5.98% | +100.00% | 23.89 | 0.0000 | 20.93 | 0.0000 | 1,471 | +5.67% | +2.41% | 18.47 | 3,099 |
| SPY-IC | P3 | 6 | 6 | +7.69% | +7.80% | +100.00% | 18.61 | 0.0000 | 20.91 | 0.0000 | 1,463 | +7.37% | +3.44% | 18.79 | 3,148 |
| QQQ-PS | P3 | 7 | 7 | +7.27% | +6.97% | +100.00% | 52.34 | 0.0000 | 28.96 | 0.0000 | 2,111 | +6.94% | +2.63% | 27.30 | 4,147 |
| QQQ-IC | P3 | 3 | 3 | +10.21% | +10.38% | +100.00% | 42.67 | 0.0005 | 18.41 | 0.0029 | 1,360 | +9.52% | +2.98% | 28.45 | 4,433 |
| SPY-PS | pooled | 8 | 8 | +5.88% | +5.98% | +100.00% | 23.89 | 0.0000 | 20.93 | 0.0000 | 1,471 | +5.67% | +2.41% | 18.47 | 3,099 |
| SPY-IC | pooled | 6 | 6 | +7.69% | +7.80% | +100.00% | 18.61 | 0.0000 | 20.91 | 0.0000 | 1,463 | +7.37% | +3.44% | 18.79 | 3,148 |
| QQQ-PS | pooled | 7 | 7 | +7.27% | +6.97% | +100.00% | 52.34 | 0.0000 | 28.96 | 0.0000 | 2,111 | +6.94% | +2.63% | 27.30 | 4,147 |
| QQQ-IC | pooled | 3 | 3 | +10.21% | +10.38% | +100.00% | 42.67 | 0.0005 | 18.41 | 0.0029 | 1,360 | +9.52% | +2.98% | 28.45 | 4,433 |


## Marked vs proxy on the same positions (§6.7 criterion 2)

| sleeve | n_marked | n_overlap | marked_mean_ror | proxy_mean_ror | gap_ror | marked_cost_ror | overlap_pass |
|---|---|---|---|---|---|---|---|
| SPY-PS | 8 | 8 | +5.88% | +5.72% | -0.16% | +0.14% | yes |
| SPY-IC | 6 | 6 | +7.69% | +8.07% | +0.38% | +0.27% | no |
| QQQ-PS | 7 | 7 | +7.27% | +6.40% | -0.87% | +0.20% | yes |
| QQQ-IC | 3 | 3 | +10.21% | +10.77% | +0.56% | +0.32% | no |


## Marked: tiers, credit, width, cost

| underlying | structure | n | graded | entry_tier_max | mean_credit | mean_width | mean_cost_over_credit |
|---|---|---|---|---|---|---|---|
| QQQ | IC | 5 | 3 | 1 | 4.21 | 47.40 | +2.98% |
| QQQ | PS | 9 | 7 | 1 | 2.88 | 43.78 | +2.63% |
| SPY | IC | 7 | 6 | 1 | 2.46 | 33.00 | +3.44% |
| SPY | PS | 10 | 8 | 1 | 1.80 | 32.00 | +2.41% |


## Marked: skipped entries by reason

| underlying | structure | reason | n |
|---|---|---|---|
| QQQ | IC | OFF:G1 | 1 |
| QQQ | IC | OFF:G2 | 18 |
| QQQ | IC | no_tier1_c2 | 4 |
| QQQ | PS | OFF:G1 | 1 |
| QQQ | PS | OFF:G2 | 18 |
| SPY | IC | OFF:G1 | 1 |
| SPY | IC | OFF:G2 | 17 |
| SPY | IC | no_tier1_c2 | 3 |
| SPY | PS | OFF:G1 | 1 |
| SPY | PS | OFF:G2 | 17 |


## Marked sensitivities (descriptive)

| sensitivity | sleeve | n | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|
| base | SPY-PS | 8 | +5.88% | 23.89 | 1,471 |
| base | SPY-IC | 6 | +7.69% | 18.61 | 1,463 |
| base | QQQ-PS | 7 | +7.27% | 52.34 | 2,111 |
| base | QQQ-IC | 3 | +10.21% | 42.67 | 1,360 |
| gate_off | SPY-PS | 21 | +5.67% | 30.89 | 3,566 |
| gate_off | SPY-IC | 18 | +3.92% | 1.16 | 1,255 |
| gate_off | QQQ-PS | 21 | +6.65% | 31.83 | 5,532 |
| gate_off | QQQ-IC | 16 | +2.14% | 0.3169 | 1,461 |
| band_0.15 | SPY-PS | 8 | +5.88% | 23.89 | 1,471 |
| band_0.15 | SPY-IC | 6 | +7.69% | 18.61 | 1,463 |
| band_0.15 | QQQ-PS | 6 | +7.39% | 46.63 | 1,896 |
| band_0.15 | QQQ-IC | 2 | — | — | 940.20 |
| wing_1.5 | SPY-PS | 8 | +7.89% | 27.11 | 1,515 |
| wing_1.5 | SPY-IC | 8 | +6.23% | 1.57 | 1,202 |
| wing_1.5 | QQQ-PS | 7 | +9.96% | 32.15 | 1,436 |
| wing_1.5 | QQQ-IC | 7 | +16.89% | 47.48 | 2,310 |


## Go / no-go (DESIGN/80 §6.7; t >= 2.0; read 2026-12-01)

| sleeve | n_proxy | mean_proxy | nw_t_proxy | bh_pass | mean_p1 | mean_p2 | mean_p3 | n_marked | mean_marked | gap_ror | worst_over_median | deflated_sr | deflated_sr_null | forward_n | c1_proxy | c2_marked | c3_month | c4_dsr | c4_dsr_null | c5_scale | verdict | note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 60 | +4.15% | 3.75 | yes | +2.17% | +5.14% | +5.14% | 8 | +5.88% | -0.16% | 1.64 | 0.2647 | 0.2979 | 0 | yes | yes | yes | yes | yes | no | GO-MIN | clears 1-4; one contract until the forward ledger holds >= 40 graded positions (now 0) |
| SPY-IC | 60 | +2.80% | 1.30 | no | -5.30% | +6.80% | +6.89% | 6 | +7.69% | +0.38% | 6.86 | -0.0303 | 0.0029 | 0 | no | no | no | no | yes | no | NO-GO | fails c1_proxy, c2_marked, c3_month, c4_dsr |
| QQQ-PS | 58 | +4.32% | 2.38 | yes | +0.89% | +6.19% | +6.30% | 7 | +7.27% | -0.87% | 4.88 | 0.1050 | 0.1382 | 0 | yes | yes | no | yes | yes | no | NO-GO | fails c3_month |
| QQQ-IC | 58 | +2.80% | 0.8090 | no | -8.41% | +7.55% | +10.14% | 3 | +10.21% | +0.56% | 4.43 | -0.0876 | -0.0543 | 0 | no | no | no | no | no | no | NO-GO | fails c1_proxy, c2_marked, c3_month, c4_dsr |


## Appendix: columns and symbols

Layers, gate and position columns (DESIGN/80 §2 to §5):

| term | meaning |
|---|---|
| `sleeve` | one (underlying, structure): `SPY-PS`, `SPY-IC`, `QQQ-PS`, `QQQ-IC`. Never pooled across sleeves. |
| `PS / IC` | put spread (short `p1`, long `p2`) / iron condor (the put spread plus short `c1`, long `c2`). §3.5 |
| `p1, p2, c1, c2` | the four legs; targets `S(1-m)`, `S(1-2m)`, `S(1+m)`, `S(1+2m)` with wings at 2σ. §3.4 |
| `proxy` | layer 1: three years of positions priced from CBOE closes with a fixed smile and spread (§5.1). Every leg is tier 3. |
| `marked` | layer 2: positions priced from the panel's late prints (§5.2), each leg a tier-1 print. Pooled = the `P3` window only. |
| `forward` | layer 3: `ledger/sb/`, the paper positions the nightly emits from 2026-09-11. §5.3 |
| `window` | a proxy sub-period (`P1` 2023-09-08 to 2024-08-30; `P2` 2024-09-06 to 2025-08-29; `P3` 2025-09-05 to 2026-11-06); `pooled` = all three. |
| `gate, ON / OFF:G1 / OFF:G2 / UNKNOWN` | G1 = `VIX3M > VIX` (contango); G2 = `X > median(X, prior 20 sessions)`. ON needs both; `OFF:G1` failed G1 first, `OFF:G2` failed G2; UNKNOWN = an input missing, fail closed. Read on the prior session's closes. §2 |
| `X, x, mean_x` | the vol index for the underlying: VIX for SPY, VXN for QQQ. `x` on a row is the entry session's close; `mean_x` its average over the rows. §3.3 |
| `m` | the σ unit `X/100 × sqrt(DTE_cal/365)`; strikes sit at 1m and 2m from spot. §3.3 |
| `tier` | mark quality of a leg: 1 = late print with size ≥ 5 (marked entries); 3 = proxy model price; 4 = intrinsic at expiry (every exit). `entry_tier_max` is the worst leg on the row. |
| `credit` | net premium received per share at entry; `width` the distance `p1 − p2` (or the wider wing for an IC). |
| `max_loss_usd / risk_usd / contracts` | max loss per contract `(width − credit) × 100`; `contracts` is the largest count with max loss ≤ 3% of $100,000; `risk_usd` = max loss × contracts. §4 |
| `net_usd, net_usd_total` | P&L of the position at the frozen sizing after costs (half-spread per leg touch plus $0.65 a contract), and its sum over the cell. §3.8 |
| `ror, mean_ror, median_ror` | return on risk = `net_usd / risk_usd`; the primary unit. A full-width loss is −100%. |
| `hit` | share of positions with `ror > 0`. |
| `mean_risk_usd` | average `risk_usd` over the rows of the cell. |
| `credit_over_width, mean_credit_over_width` | credit as a share of width: how much of the max loss is collected up front. |
| `cost_over_credit, mean_cost_over_credit` | round-trip cost as a share of the credit collected. |

Statistics (§6.1 to §6.5):

| term | meaning |
|---|---|
| `n / expiries` | positions in the cell / distinct expiry sessions (the clusters). |
| `nw_t, nw_p` | Newey-West (Bartlett, lag 2) t of the mean `ror` on the entry-ordered series, and its p (Student t, n − 1 df). The primary t: weekly entries overlap three-deep. §6.1 |
| `cl_t, cl_p` | the same mean with the SE clustered by expiry session; the companion t, G − 1 df. |
| `bh_pass` | Benjamini-Hochberg at FDR 0.1 across the four sleeves on `nw_p`: true if the sleeve is rejected (its p survives the multiplicity charge). §6.3 |
| `sr` | per-position Sharpe, `mean(ror) / sd(ror)`, not annualised. |
| `sr_star` | the expected best Sharpe among 6 null trials (4 sleeves + 2 alternates), charging the observed cross-sleeve variance of the Sharpe. §6.3 |
| `deflated_sr` | `sr − sr_star`; > 0 is criterion 4. The pre-registered estimator. |
| `dsr_prob` | probabilistic Sharpe: P(true SR > `sr_star`) given the sample's skew and kurtosis. |
| `sr_star_null, deflated_sr_null, dsr_prob_null` | the same three charging the null sampling variance `1 / min(n)` instead of the observed cross-sleeve variance (D16). Reported beside the pre-registered version; when the two disagree the read records both and the null benchmark governs. |
| `skew, kurt` | sample skew and non-excess kurtosis of `ror` (a normal has kurt 3). Hold-to-expiry spreads are bimodal, so these are large. |
| `pbo` | probability of backtest overfitting (CSCV over 16 entry blocks): the share of in-sample / out-of-sample splits in which the best sleeve in-sample ranks below the median out-of-sample. 0.5 is coin-flip; the four sleeves are the configurations. |
| `mean_logit, n_combinations` | mean logit of the out-of-sample rank across splits (negative = worse than median); number of splits (half of the blocks in-sample). |
| `n_months, median_month_usd, worst_month, worst_month_usd` | net $ per expiry month at the frozen sizing; the median month, and the worst month and its $. |
| `worst_over_median` | `−worst_month_usd / median_month_usd`; the month rule needs a positive median and this ratio ≤ 3. §6.7(3) |
| `months_negative / month_rule_pass` | count of losing months / the rule's verdict. |
| `worst_ror, worst_entry, best_ror, mean_win_ror` | the single worst and best positions (and the worst one's entry date); mean `ror` over winning positions. |
| `worst_decile_share_of_loss` | share of all losses (in `ror`) sitting in the worst tenth of positions: tail concentration. |
| `full_width_losses` | positions that lost at least 98% of risk (the spread finished fully in the money). |
| `mean_without_worst_1pct / mean_without_best_1pct` | mean `ror` with the worst / best 1% of positions removed: how much of the mean is one tail. |

Sensitivities and skip reasons (§6.6; descriptive, cannot promote a configuration):

| term | meaning |
|---|---|
| `base` | the frozen rule: gate ON, frozen costs, wings at 2σ, strike band ±0.25σ. |
| `gate_off` | a position every entry Friday regardless of the gate (the gate's marginal value is base vs this). |
| `g1_only / g2_only` | gate = contango only / level-above-median only. |
| `costs_x2` | every cost doubled (proxy only). |
| `wing_1.5` | wings at 1.5σ instead of 2σ. |
| `band_0.15` | marked only: nearest tier-1 strike within ±0.15σ instead of ±0.25σ. |
| `skipped reason `OFF:G1`, `OFF:G2`` | no entry because the gate was off (which condition failed first). |
| `skipped reason `no_tier1_<leg>`` | no strike with a tier-1 print inside the band for that leg (marked layer only). |
| `skipped reason `degenerate_strikes`` | the order `p2 < p1 < S < c1 < c2` did not hold. |

Other structures on the proxy (descriptive; never a verdict input):

| term | meaning |
|---|---|
| `long_c1, long_p1, long_c2, long_p2` | one long leg at the 1σ or 2σ strike; risk = the premium paid, so −100% is the premium gone. |
| `short_p1_naked, short_c1_naked` | one short leg at 1σ with no wing; risk = the 2σ stress loss (the matching spread's max loss at the same strikes); `mean_margin_usd` is the Reg-T proxy margin per contract, reported for buying power only. |
| `CS` | call credit spread, short `c1` long `c2`; risk = width − credit. Not a sleeve; a challenger draft. |
| `PS (in this table)` | the champion put spread recomputed by the same code, as a check against the sleeve table. |
| `set` | `gate ON` = the champion's entry nights; `every Friday` = every entry session, gate ignored. |
| `mean_pnl_usd / total_pnl_usd / mean_premium_usd` | per one contract: mean and total net $, and the mean premium (positive = paid, negative = received). |

Go / no-go columns (§6.7; read 2026-12-01):

| term | meaning |
|---|---|
| `n_proxy, mean_proxy, nw_t_proxy` | pooled proxy count, mean `ror` and NW t. |
| `mean_p1, mean_p2, mean_p3` | mean `ror` in each proxy window; criterion 1 needs all three > 0. |
| `n_marked, mean_marked` | marked positions and their mean `ror` (the `P3` panel window). |
| `gap_ror` | on the (entry, sleeve) pairs both layers hold, `proxy mean − marked mean`; criterion 2 allows a gap up to the marked round-trip cost. |
| `forward_n` | graded positions in `ledger/sb/`; criterion 5 needs ≥ 40 with a positive mean. |
| `c1_proxy` | mean > 0, `nw_t ≥ 2`, `bh_pass`, and a positive mean in every window. |
| `c2_marked` | marked mean > 0 and the overlap check passes. |
| `c3_month` | the month rule (`worst_over_median`). |
| `c4_dsr` | `deflated_sr > 0`, the pre-registered estimator. |
| `c4_dsr_null` | `deflated_sr_null > 0`, the D16 companion; reported, does not enter the verdict. |
| `c5_scale` | the forward count trigger for sizing above one contract. |
| `verdict` | `GO-MIN`: clears 1 to 4, one contract at the read. `GO-SCALE`: also 5. `NO-GO`: fails one of 1 to 4 (the note names which). `NOT YET`: the proxy holds no positions for the sleeve. |

Percentages are `ror` unless the column says `usd`. Every threshold above is read from `engine/config.py`; none moves before the read.
