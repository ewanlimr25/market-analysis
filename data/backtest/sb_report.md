# S-B backtest report (generated)


## Inputs

- refreshed: {'index_vol_through': '2026-10-30', 'prices_through': '2026-10-30'}
- proxy: {'index_vol': ['1990-01-02', '2026-10-30'], 'sessions': ['2023-10-31', '2026-10-30'], 'n_sessions': 753}
- marked: {'panel': ['2026-03-13', '2026-10-30'], 'n_entry_sessions': 34}


## Gate ON share of entry sessions (proxy, by year)

| underlying | year | entry_sessions | gate_on | on_share |
|---|---|---|---|---|
| QQQ | 2023 | 5 | 1 | +20.00% |
| QQQ | 2024 | 52 | 26 | +50.00% |
| QQQ | 2025 | 52 | 15 | +28.85% |
| QQQ | 2026 | 41 | 19 | +46.34% |
| QQQ | all | 150 | 61 | +40.67% |
| SPY | 2023 | 5 | 1 | +20.00% |
| SPY | 2024 | 52 | 25 | +48.08% |
| SPY | 2025 | 52 | 16 | +30.77% |
| SPY | 2026 | 41 | 20 | +48.78% |
| SPY | all | 150 | 62 | +41.33% |


## Proxy: mean net return on risk per position; NW(lag 2) t and expiry-clustered t

| sleeve | window | n | expiries | mean_ror | median_ror | hit | nw_t | nw_p | cl_t | cl_p | net_usd_total | mean_credit_over_width | mean_cost_over_credit | mean_x | mean_risk_usd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | P1 | 19 | 19 | +1.98% | +5.47% | +94.74% | 0.6124 | 0.5480 | 0.5611 | 0.5816 | 1,082 | +5.38% | +3.67% | 15.33 | 2,002 |
| SPY-IC | P1 | 19 | 19 | -0.90% | +7.49% | +73.68% | -0.2643 | 0.7945 | -0.2246 | 0.8248 | -1,137 | +7.53% | +5.06% | 15.33 | 2,282 |
| QQQ-PS | P1 | 20 | 20 | +0.63% | +6.06% | +95.00% | 0.1272 | 0.9001 | 0.1181 | 0.9072 | 281.38 | +5.89% | +3.21% | 19.47 | 1,924 |
| QQQ-IC | P1 | 20 | 20 | -3.81% | +10.16% | +80.00% | -0.5852 | 0.5653 | -0.5533 | 0.5865 | -1,858 | +9.72% | +3.56% | 19.47 | 2,004 |
| SPY-PS | P2 | 14 | 14 | +5.14% | +5.68% | +92.86% | 10.81 | 0.0000 | 9.41 | 0.0000 | 1,739 | +5.52% | +2.80% | 18.13 | 2,436 |
| SPY-IC | P2 | 14 | 14 | +6.80% | +7.96% | +92.86% | 9.55 | 0.0000 | 8.25 | 0.0000 | 2,229 | +7.70% | +3.88% | 18.13 | 2,387 |
| QQQ-PS | P2 | 14 | 14 | +6.19% | +6.22% | +100.00% | 188.56 | 0.0000 | 139.83 | 0.0000 | 2,118 | +6.02% | +2.63% | 21.16 | 2,443 |
| QQQ-IC | P2 | 14 | 14 | +7.55% | +10.51% | +92.86% | 2.58 | 0.0227 | 2.48 | 0.0276 | 2,417 | +9.87% | +2.90% | 21.16 | 2,356 |
| SPY-PS | P3 | 29 | 29 | +5.18% | +5.69% | +96.55% | 11.29 | 0.0000 | 10.23 | 0.0000 | 4,246 | +5.52% | +2.58% | 17.89 | 2,831 |
| SPY-IC | P3 | 29 | 29 | +6.99% | +8.00% | +93.10% | 11.27 | 0.0000 | 9.98 | 0.0000 | 5,576 | +7.66% | +3.56% | 17.89 | 2,773 |
| QQQ-PS | P3 | 27 | 27 | +3.10% | +6.31% | +92.59% | 1.06 | 0.2998 | 1.20 | 0.2401 | 2,855 | +6.03% | +2.16% | 23.57 | 3,448 |
| QQQ-IC | P3 | 27 | 27 | +6.89% | +10.61% | +88.89% | 2.27 | 0.0317 | 2.55 | 0.0168 | 6,199 | +9.86% | +2.35% | 23.57 | 3,328 |
| SPY-PS | pooled | 62 | 62 | +4.19% | +5.62% | +95.16% | 3.91 | 0.0002 | 3.79 | 0.0004 | 7,067 | +5.48% | +2.96% | 17.16 | 2,487 |
| SPY-IC | pooled | 62 | 62 | +4.53% | +7.89% | +87.10% | 3.36 | 0.0014 | 3.37 | 0.0013 | 6,668 | +7.63% | +4.09% | 17.16 | 2,535 |
| QQQ-PS | pooled | 61 | 61 | +3.00% | +6.19% | +95.08% | 1.41 | 0.1639 | 1.45 | 0.1521 | 5,255 | +5.98% | +2.61% | 21.67 | 2,718 |
| QQQ-IC | pooled | 61 | 61 | +3.53% | +10.48% | +86.89% | 1.23 | 0.2231 | 1.31 | 0.1939 | 6,758 | +9.82% | +2.87% | 21.67 | 2,671 |


## BH(0.10) across the four sleeves (proxy, pooled, on the NW p)

| sleeve | n | mean_ror | nw_t | nw_p | bh_pass |
|---|---|---|---|---|---|
| SPY-PS | 62 | +4.19% | 3.91 | 0.0002 | yes |
| SPY-IC | 62 | +4.53% | 3.36 | 0.0014 | yes |
| QQQ-PS | 61 | +3.00% | 1.41 | 0.1639 | no |
| QQQ-IC | 61 | +3.53% | 1.23 | 0.2231 | no |


## Deflated Sharpe (6 trials) — proxy pooled

| sleeve | n | sr | sr_star | deflated_sr | dsr_prob | sr_star_null | deflated_sr_null | dsr_prob_null | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 62 | 0.4807 | 0.2102 | 0.2705 | 0.7756 | 0.1665 | 0.3143 | 0.8105 | -7.27 | 57.87 |
| SPY-IC | 62 | 0.4276 | 0.2102 | 0.2175 | 0.7984 | 0.1665 | 0.2612 | 0.8423 | -4.51 | 27.22 |
| QQQ-PS | 61 | 0.1857 | 0.2102 | -0.0245 | 0.4507 | 0.1665 | 0.0193 | 0.5389 | -5.61 | 35.38 |
| QQQ-IC | 61 | 0.1682 | 0.2102 | -0.0419 | 0.4003 | 0.1665 | 0.0018 | 0.5042 | -3.35 | 13.94 |


## Deflated Sharpe (6 trials) — proxy P1

| sleeve | n | sr | sr_star | deflated_sr | dsr_prob | sr_star_null | deflated_sr_null | dsr_prob_null | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 19 | 0.1287 | 0.1407 | -0.0120 | 0.4842 | 0.2983 | -0.1695 | 0.2876 | -4.36 | 21.99 |
| SPY-IC | 19 | -0.0515 | 0.1407 | -0.1922 | 0.1914 | 0.2983 | -0.3498 | 0.0561 | -2.58 | 10.34 |
| QQQ-PS | 20 | 0.0264 | 0.1407 | -0.1143 | 0.3191 | 0.2983 | -0.2719 | 0.1316 | -4.47 | 22.98 |
| QQQ-IC | 20 | -0.1237 | 0.1407 | -0.2644 | 0.0914 | 0.2983 | -0.4220 | 0.0168 | -2.21 | 6.87 |


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
| SPY-PS | 29 | 1.90 | 1.15 | 0.7546 | 0.7389 | 0.2502 | 1.65 | 0.9192 | -5.35 | 31.73 |
| SPY-IC | 29 | 1.85 | 1.15 | 0.7068 | 0.8023 | 0.2502 | 1.60 | 0.9730 | -3.58 | 14.68 |
| QQQ-PS | 27 | 0.2314 | 1.15 | -0.9146 | 0.0014 | 0.2502 | -0.0188 | 0.4754 | -4.70 | 25.87 |
| QQQ-IC | 27 | 0.4916 | 1.15 | -0.6544 | 0.0607 | 0.2502 | 0.2414 | 0.7161 | -4.52 | 24.52 |


## PBO (CSCV over 16 entry blocks, proxy pooled)

- pbo: 0.3240870240870241
- mean_logit: 0.35825267803294036
- n_combinations: 12870
- n_configs: 4
- n_blocks: 16
- n_entries: 67


## Month rule (proxy; worst expiry-month vs median month, $ at frozen sizing)

| sleeve | n_months | median_month_usd | worst_month | worst_month_usd | worst_over_median | months_negative | month_rule_pass |
|---|---|---|---|---|---|---|---|
| SPY-PS | 28 | 245.68 | 2024-08 | -396.47 | 1.61 | 2 | yes |
| SPY-IC | 28 | 264.47 | 2024-08 | -1,537 | 5.81 | 4 | no |
| QQQ-PS | 28 | 271.59 | 2026-10 | -2,153 | 7.93 | 2 | no |
| QQQ-IC | 28 | 409.24 | 2026-10 | -1,592 | 3.89 | 5 | no |


## Tail report (proxy, pooled)

| sleeve | n | mean_ror | worst_ror | worst_entry | best_ror | mean_win_ror | worst_decile_share_of_loss | full_width_losses | mean_without_worst_1pct | mean_without_best_1pct | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 62 | +4.19% | -61.38% | 2024-07-12 | +6.12% | +5.63% | 1.00 | 0 | +5.26% | +4.16% | -7.27 | 54.87 |
| SPY-IC | 62 | +4.53% | -60.67% | 2024-07-12 | +8.42% | +7.72% | 0.9463 | 0 | +5.60% | +4.47% | -4.51 | 24.22 |
| QQQ-PS | 61 | +3.00% | -100.20% | 2024-07-12 | +6.60% | +6.15% | 1.00 | 1 | +4.72% | +2.94% | -5.61 | 32.38 |
| QQQ-IC | 61 | +3.53% | -95.11% | 2024-07-12 | +11.01% | +10.36% | 0.9688 | 0 | +5.18% | +3.41% | -3.35 | 10.94 |

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
| 2026-10-09 | 2026-10-30 | 20.55 | -61.39% | -2,137 |
| 2026-10-02 | 2026-10-23 | 21.20 | -12.36% | -442.05 |
| 2024-07-19 | 2024-08-09 | 21.51 | +3.83% | 89.96 |
| 2024-01-26 | 2024-02-16 | 17.03 | +5.66% | 90.87 |
| 2024-01-05 | 2024-01-26 | 17.13 | +5.67% | 85.64 |
| 2024-02-02 | 2024-02-23 | 17.22 | +5.80% | 93.02 |
| 2024-03-08 | 2024-03-28 | 19.04 | +5.83% | 104.43 |
| 2025-02-28 | 2025-03-21 | 22.66 | +5.85% | 153.54 |
| 2024-02-16 | 2024-03-08 | 18.60 | +5.86% | 104.89 |


## Gate modes and sensitivities (proxy, pooled; descriptive)

| sensitivity | sleeve | n | mean_ror | nw_t | cl_t | net_usd_total | mean_cost_over_credit |
|---|---|---|---|---|---|---|---|
| base | SPY-PS | 62 | +4.19% | 3.91 | 3.79 | 7,067 | +2.96% |
| base | SPY-IC | 62 | +4.53% | 3.36 | 3.37 | 6,668 | +4.09% |
| base | QQQ-PS | 61 | +3.00% | 1.41 | 1.45 | 5,255 | +2.61% |
| base | QQQ-IC | 61 | +3.53% | 1.23 | 1.31 | 6,758 | +2.87% |
| gate_off | SPY-PS | 150 | +3.23% | 2.93 | 3.26 | 13,328 | +3.00% |
| gate_off | SPY-IC | 150 | +3.04% | 2.21 | 2.54 | 10,044 | +4.14% |
| gate_off | QQQ-PS | 150 | +2.18% | 1.27 | 1.51 | 10,592 | +2.65% |
| gate_off | QQQ-IC | 150 | +0.15% | 0.0571 | 0.0718 | 51.87 | +2.91% |
| g1_only | SPY-PS | 139 | +3.74% | 4.08 | 4.70 | 13,697 | +3.07% |
| g1_only | SPY-IC | 139 | +4.11% | 3.67 | 4.25 | 13,691 | +4.24% |
| g1_only | QQQ-PS | 139 | +2.54% | 1.46 | 1.81 | 10,916 | +2.69% |
| g1_only | QQQ-IC | 139 | +1.62% | 0.6556 | 0.8310 | 6,683 | +2.96% |
| g2_only | SPY-PS | 72 | +3.03% | 1.85 | 1.80 | 6,512 | +2.84% |
| g2_only | SPY-IC | 72 | +2.70% | 1.46 | 1.37 | 3,886 | +3.94% |
| g2_only | QQQ-PS | 71 | +2.11% | 0.9571 | 0.9530 | 4,743 | +2.54% |
| g2_only | QQQ-IC | 71 | +0.83% | 0.2715 | 0.2761 | 1,471 | +2.79% |
| costs_x2 | SPY-PS | 62 | +4.02% | 3.75 | 3.63 | 6,812 | +5.93% |
| costs_x2 | SPY-IC | 62 | +4.19% | 3.09 | 3.11 | 6,147 | +8.19% |
| costs_x2 | QQQ-PS | 61 | +2.83% | 1.33 | 1.37 | 4,996 | +5.22% |
| costs_x2 | QQQ-IC | 61 | +3.22% | 1.12 | 1.20 | 6,275 | +5.75% |
| wing_1.5 | SPY-PS | 62 | -0.52% | -0.3162 | -0.3055 | -586.09 | +19.37% |
| wing_1.5 | SPY-IC | 62 | -1.65% | -0.7308 | -0.7366 | -1,991 | +16.93% |
| wing_1.5 | QQQ-PS | 61 | -1.10% | -0.4170 | -0.4539 | -1,384 | +11.91% |
| wing_1.5 | QQQ-IC | 61 | -1.39% | -0.3499 | -0.3765 | -1,846 | +7.31% |


## Other structures on the proxy (descriptive; not sleeves, never a verdict input)

Single legs, naked shorts and the call spread re-priced on the same entry rows with the frozen smile and costs. Risk: debit = premium; credit spread = width - credit; naked = the 2-sigma stress loss (the matching spread's max loss), Reg-T proxy margin beside. `PS` here is the champion recomputed as a check. Drafts: `ledger/challengers/drafts/sb-c-callspread.json`, `sb-c-nakedput-margin.json`.

| set | structure | underlying | n | mean_ror | nw_t | hit | mean_pnl_usd | worst_ror | mean_premium_usd | mean_margin_usd | total_pnl_usd |
|---|---|---|---|---|---|---|---|---|---|---|---|
| gate ON | long_c1 | QQQ | 61 | -20.53% | -0.5292 | +8.20% | -50.70 | -102.60% | 120.31 | — | -3,093 |
| gate ON | long_p1 | QQQ | 61 | -61.77% | -2.32 | +4.92% | -166.87 | -101.38% | 256.45 | — | -10,179 |
| gate ON | long_c2 | QQQ | 61 | -120.32% | -98.50 | +0.00% | -9.11 | -134.00% | 7.69 | — | -555.89 |
| gate ON | long_p2 | QQQ | 61 | -88.46% | -6.54 | +1.64% | -75.92 | -103.38% | 82.68 | — | -4,631 |
| gate ON | short_p1_naked | QQQ | 61 | +5.68% | 2.29 | +95.08% | 162.07 | -124.66% | -256.45 | 7,842 | 9,886 |
| gate ON | short_c1_naked | QQQ | 61 | +0.70% | 0.4107 | +91.80% | 46.65 | -66.02% | -120.31 | 7,978 | 2,846 |
| gate ON | CS | QQQ | 61 | +0.37% | 0.2159 | +90.16% | 37.53 | -66.40% | -112.62 | — | 2,290 |
| gate ON | PS | QQQ | 61 | +3.00% | 1.41 | +95.08% | 86.15 | -100.20% | -173.77 | — | 5,255 |
| gate ON | long_c1 | SPY | 62 | -27.21% | -0.7582 | +11.29% | -23.62 | -104.68% | 59.48 | — | -1,465 |
| gate ON | long_p1 | SPY | 62 | -85.19% | -7.27 | +3.23% | -194.70 | -101.40% | 219.26 | — | -12,072 |
| gate ON | long_c2 | SPY | 62 | -147.86% | -71.72 | +0.00% | -5.52 | -173.85% | 3.80 | — | -342.49 |
| gate ON | long_p2 | SPY | 62 | -102.42% | -1,133 | +0.00% | -80.17 | -103.47% | 78.36 | — | -4,971 |
| gate ON | short_p1_naked | SPY | 62 | +7.53% | 7.08 | +96.77% | 190.44 | -57.60% | -219.26 | 9,602 | 11,807 |
| gate ON | short_c1_naked | SPY | 62 | +0.49% | 0.5731 | +88.71% | 19.68 | -27.78% | -59.48 | 9,767 | 1,220 |
| gate ON | CS | SPY | 62 | +0.27% | 0.3110 | +88.71% | 14.16 | -28.03% | -55.67 | — | 877.92 |
| gate ON | PS | SPY | 62 | +4.19% | 3.91 | +95.16% | 110.26 | -61.38% | -140.90 | — | 6,836 |
| every Friday | long_c1 | QQQ | 150 | +35.06% | 0.7587 | +15.33% | 49.27 | -102.60% | 118.66 | — | 7,390 |
| every Friday | long_p1 | QQQ | 150 | -56.46% | -2.91 | +6.67% | -153.11 | -101.45% | 251.96 | — | -22,967 |
| every Friday | long_c2 | QQQ | 150 | -120.74% | -144.52 | +0.00% | -8.99 | -135.19% | 7.57 | — | -1,349 |
| every Friday | long_p2 | QQQ | 150 | -96.54% | -17.29 | +0.67% | -79.39 | -103.62% | 81.19 | — | -11,908 |
| every Friday | short_p1_naked | QQQ | 150 | +5.12% | 2.81 | +93.33% | 148.35 | -124.66% | -251.96 | 7,860 | 22,252 |
| every Friday | short_c1_naked | QQQ | 150 | -1.68% | -0.8408 | +84.67% | -53.30 | -90.15% | -118.66 | 7,996 | -7,996 |
| every Friday | CS | QQQ | 150 | -2.01% | -1.01 | +83.33% | -62.30 | -90.50% | -111.09 | — | -9,344 |
| every Friday | PS | QQQ | 150 | +2.18% | 1.27 | +93.33% | 68.96 | -100.20% | -170.77 | — | 10,344 |
| every Friday | long_c1 | SPY | 150 | -6.31% | -0.1671 | +11.33% | 4.95 | -105.35% | 59.18 | — | 742.53 |
| every Friday | long_p1 | SPY | 150 | -74.51% | -6.09 | +4.67% | -167.26 | -101.52% | 218.25 | — | -25,089 |
| every Friday | long_c2 | SPY | 150 | -148.93% | -94.76 | +0.00% | -5.52 | -180.85% | 3.80 | — | -827.99 |
| every Friday | long_p2 | SPY | 150 | -102.45% | -1,580 | +0.00% | -79.52 | -103.74% | 77.71 | — | -11,928 |
| every Friday | short_p1_naked | SPY | 150 | +6.57% | 5.94 | +95.33% | 163.00 | -92.22% | -218.25 | 9,543 | 24,451 |
| every Friday | short_c1_naked | SPY | 150 | -0.01% | -0.0066 | +88.67% | -8.88 | -59.74% | -59.18 | 9,703 | -1,332 |
| every Friday | CS | SPY | 150 | -0.23% | -0.2583 | +88.67% | -14.40 | -59.95% | -55.39 | — | -2,160 |
| every Friday | PS | SPY | 150 | +3.23% | 2.93 | +94.67% | 83.49 | -95.48% | -140.54 | — | 12,523 |


## Marked (panel): sleeve table

| sleeve | window | n | expiries | mean_ror | median_ror | hit | nw_t | nw_p | cl_t | cl_p | net_usd_total | mean_credit_over_width | mean_cost_over_credit | mean_x | mean_risk_usd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | P3 | 11 | 11 | +5.65% | +5.51% | +100.00% | 22.21 | 0.0000 | 23.85 | 0.0000 | 1,872 | +5.48% | +2.61% | 17.61 | 2,971 |
| SPY-IC | P3 | 8 | 8 | +7.63% | +7.77% | +100.00% | 23.96 | 0.0000 | 26.27 | 0.0000 | 1,836 | +7.33% | +3.61% | 17.87 | 2,987 |
| QQQ-PS | P3 | 11 | 11 | -1.17% | +6.75% | +81.82% | -0.1696 | 0.8687 | -0.1924 | 0.8512 | -190.96 | +6.33% | +2.53% | 24.97 | 4,000 |
| QQQ-IC | P3 | 6 | 6 | +5.74% | +8.97% | +83.33% | 1.69 | 0.1517 | 1.54 | 0.1830 | 1,574 | +8.61% | +2.91% | 24.74 | 4,216 |
| SPY-PS | pooled | 11 | 11 | +5.65% | +5.51% | +100.00% | 22.21 | 0.0000 | 23.85 | 0.0000 | 1,872 | +5.48% | +2.61% | 17.61 | 2,971 |
| SPY-IC | pooled | 8 | 8 | +7.63% | +7.77% | +100.00% | 23.96 | 0.0000 | 26.27 | 0.0000 | 1,836 | +7.33% | +3.61% | 17.87 | 2,987 |
| QQQ-PS | pooled | 11 | 11 | -1.17% | +6.75% | +81.82% | -0.1696 | 0.8687 | -0.1924 | 0.8512 | -190.96 | +6.33% | +2.53% | 24.97 | 4,000 |
| QQQ-IC | pooled | 6 | 6 | +5.74% | +8.97% | +83.33% | 1.69 | 0.1517 | 1.54 | 0.1830 | 1,574 | +8.61% | +2.91% | 24.74 | 4,216 |


## Marked vs proxy on the same positions (§6.7 criterion 2)

| sleeve | n_marked | n_overlap | marked_mean_ror | proxy_mean_ror | gap_ror | marked_cost_ror | overlap_pass |
|---|---|---|---|---|---|---|---|
| SPY-PS | 11 | 11 | +5.65% | +5.67% | +0.02% | +0.15% | yes |
| SPY-IC | 8 | 8 | +7.63% | +8.02% | +0.39% | +0.28% | no |
| QQQ-PS | 11 | 11 | -1.17% | -1.50% | -0.33% | +0.17% | no |
| QQQ-IC | 6 | 6 | +5.74% | +7.48% | +1.74% | +0.28% | no |


## Marked: tiers, credit, width, cost

| underlying | structure | n | graded | entry_tier_max | mean_credit | mean_width | mean_cost_over_credit |
|---|---|---|---|---|---|---|---|
| QQQ | IC | 9 | 6 | 1 | 4.29 | 46.89 | +2.91% |
| QQQ | PS | 14 | 11 | 1 | 2.85 | 43.93 | +2.53% |
| SPY | IC | 9 | 8 | 1 | 2.50 | 32.67 | +3.61% |
| SPY | PS | 14 | 11 | 1 | 1.84 | 32.79 | +2.61% |


## Marked: skipped entries by reason

| underlying | structure | reason | n |
|---|---|---|---|
| QQQ | IC | OFF:G1 | 1 |
| QQQ | IC | OFF:G2 | 18 |
| QQQ | IC | no_tier1_c2 | 5 |
| QQQ | PS | OFF:G1 | 1 |
| QQQ | PS | OFF:G2 | 18 |
| SPY | IC | OFF:G1 | 1 |
| SPY | IC | OFF:G2 | 18 |
| SPY | IC | no_tier1_c2 | 5 |
| SPY | PS | OFF:G1 | 1 |
| SPY | PS | OFF:G2 | 18 |


## Marked sensitivities (descriptive)

| sensitivity | sleeve | n | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|
| base | SPY-PS | 11 | +5.65% | 22.21 | 1,872 |
| base | SPY-IC | 8 | +7.63% | 23.96 | 1,836 |
| base | QQQ-PS | 11 | -1.17% | -0.1696 | -190.96 |
| base | QQQ-IC | 6 | +5.74% | 1.69 | 1,574 |
| gate_off | SPY-PS | 26 | +5.54% | 31.66 | 4,210 |
| gate_off | SPY-IC | 22 | +4.46% | 1.59 | 1,980 |
| gate_off | QQQ-PS | 26 | +3.19% | 1.04 | 3,442 |
| gate_off | QQQ-IC | 19 | +2.00% | 0.3484 | 1,675 |
| band_0.15 | SPY-PS | 11 | +5.65% | 22.21 | 1,872 |
| band_0.15 | SPY-IC | 8 | +7.63% | 23.96 | 1,836 |
| band_0.15 | QQQ-PS | 9 | -2.74% | -0.3330 | -630.68 |
| band_0.15 | QQQ-IC | 3 | +2.93% | 0.6216 | 471.17 |
| wing_1.5 | SPY-PS | 11 | +7.60% | 23.62 | 2,039 |
| wing_1.5 | SPY-IC | 11 | +7.09% | 2.34 | 1,893 |
| wing_1.5 | QQQ-PS | 11 | -4.12% | -0.3542 | -673.40 |
| wing_1.5 | QQQ-IC | 11 | +1.70% | 0.1366 | 579.11 |


## Go / no-go (DESIGN/80 §6.7; t >= 2.0; read 2026-12-01)

| sleeve | n_proxy | mean_proxy | nw_t_proxy | bh_pass | mean_p1 | mean_p2 | mean_p3 | n_marked | mean_marked | gap_ror | worst_over_median | deflated_sr | deflated_sr_null | forward_n | c1_proxy | c2_marked | c3_month | c4_dsr | c4_dsr_null | c5_scale | verdict | note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 62 | +4.19% | 3.91 | yes | +1.98% | +5.14% | +5.18% | 11 | +5.65% | +0.02% | 1.61 | 0.2705 | 0.3143 | 3 | yes | yes | yes | yes | yes | no | GO-MIN | clears 1-4; one contract until the forward ledger holds >= 40 graded positions (now 3) |
| SPY-IC | 62 | +4.53% | 3.36 | yes | -0.90% | +6.80% | +6.99% | 8 | +7.63% | +0.39% | 5.81 | 0.2175 | 0.2612 | 2 | no | no | no | yes | yes | no | NO-GO | fails c1_proxy, c2_marked, c3_month |
| QQQ-PS | 61 | +3.00% | 1.41 | no | +0.63% | +6.19% | +3.10% | 11 | -1.17% | -0.33% | 7.93 | -0.0245 | 0.0193 | 4 | no | no | no | no | yes | no | NO-GO | fails c1_proxy, c2_marked, c3_month, c4_dsr |
| QQQ-IC | 61 | +3.53% | 1.23 | no | -3.81% | +7.55% | +6.89% | 6 | +5.74% | +1.74% | 3.89 | -0.0419 | 0.0018 | 3 | no | no | no | no | yes | no | NO-GO | fails c1_proxy, c2_marked, c3_month, c4_dsr |


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
| `forward_n` | graded champion positions in `ledger/sb/`; criterion 5 needs ≥ 40 with a positive mean. |
| `c1_proxy` | mean > 0, `nw_t ≥ 2`, `bh_pass`, and a positive mean in every window. |
| `c2_marked` | marked mean > 0 and the overlap check passes. |
| `c3_month` | the month rule (`worst_over_median`). |
| `c4_dsr` | `deflated_sr > 0`, the pre-registered estimator. |
| `c4_dsr_null` | `deflated_sr_null > 0`, the D16 companion; reported, does not enter the verdict. |
| `c5_scale` | the forward count trigger for sizing above one contract. |
| `verdict` | `GO-MIN`: clears 1 to 4, one contract at the read. `GO-SCALE`: also 5. `NO-GO`: fails one of 1 to 4 (the note names which). `NOT YET`: the proxy holds no positions for the sleeve. |

Percentages are `ror` unless the column says `usd`. Every threshold above is read from `engine/config.py`; none moves before the read.
