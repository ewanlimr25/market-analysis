# S-B backtest report (generated)


## Inputs

- refreshed: {'index_vol_through': '2026-11-20', 'prices_through': '2026-11-20'}
- proxy: {'index_vol': ['1990-01-02', '2026-11-20'], 'sessions': ['2023-11-21', '2026-11-20'], 'n_sessions': 753}
- marked: {'panel': ['2026-03-13', '2026-11-20'], 'n_entry_sessions': 37}


## Gate ON share of entry sessions (proxy, by year)

| underlying | year | entry_sessions | gate_on | on_share |
|---|---|---|---|---|
| QQQ | 2023 | 2 | 1 | +50.00% |
| QQQ | 2024 | 52 | 26 | +50.00% |
| QQQ | 2025 | 52 | 15 | +28.85% |
| QQQ | 2026 | 44 | 22 | +50.00% |
| QQQ | all | 150 | 64 | +42.67% |
| SPY | 2023 | 2 | 1 | +50.00% |
| SPY | 2024 | 52 | 25 | +48.08% |
| SPY | 2025 | 52 | 16 | +30.77% |
| SPY | 2026 | 44 | 23 | +52.27% |
| SPY | all | 150 | 65 | +43.33% |


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
| SPY-PS | P3 | 32 | 32 | +2.38% | +5.70% | +93.75% | 0.8489 | 0.4025 | 0.8260 | 0.4151 | 1,739 | +5.54% | +2.54% | 18.05 | 2,886 |
| SPY-IC | P3 | 32 | 32 | +4.18% | +8.00% | +90.62% | 1.46 | 0.1554 | 1.41 | 0.1697 | 3,287 | +7.68% | +3.51% | 18.05 | 2,827 |
| QQQ-PS | P3 | 30 | 30 | +0.23% | +6.30% | +86.67% | 0.0587 | 0.9536 | 0.0658 | 0.9480 | -528.73 | +6.05% | +2.12% | 24.01 | 3,548 |
| QQQ-IC | P3 | 30 | 30 | +3.95% | +10.60% | +83.33% | 0.9974 | 0.3268 | 1.11 | 0.2782 | 3,348 | +9.88% | +2.31% | 24.01 | 3,421 |
| SPY-PS | pooled | 65 | 65 | +2.86% | +5.63% | +93.85% | 1.69 | 0.0965 | 1.64 | 0.1062 | 4,560 | +5.49% | +2.93% | 17.27 | 2,531 |
| SPY-IC | pooled | 65 | 65 | +3.26% | +7.91% | +86.15% | 1.76 | 0.0832 | 1.72 | 0.0904 | 4,380 | +7.64% | +4.04% | 17.27 | 2,573 |
| QQQ-PS | pooled | 64 | 64 | +1.66% | +6.19% | +92.19% | 0.6837 | 0.4967 | 0.7198 | 0.4743 | 1,871 | +5.99% | +2.57% | 21.97 | 2,799 |
| QQQ-IC | pooled | 64 | 64 | +2.31% | +10.48% | +84.38% | 0.7722 | 0.4429 | 0.8196 | 0.4155 | 3,907 | +9.83% | +2.83% | 21.97 | 2,745 |


## BH(0.10) across the four sleeves (proxy, pooled, on the NW p)

| sleeve | n | mean_ror | nw_t | nw_p | bh_pass |
|---|---|---|---|---|---|
| SPY-PS | 65 | +2.86% | 1.69 | 0.0965 | no |
| SPY-IC | 65 | +3.26% | 1.76 | 0.0832 | no |
| QQQ-PS | 64 | +1.66% | 0.6837 | 0.4967 | no |
| QQQ-IC | 64 | +2.31% | 0.7722 | 0.4429 | no |


## Deflated Sharpe (6 trials) — proxy pooled

| sleeve | n | sr | sr_star | deflated_sr | dsr_prob | sr_star_null | deflated_sr_null | dsr_prob_null | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 65 | 0.2032 | 0.0845 | 0.1187 | 0.7265 | 0.1625 | 0.0407 | 0.5818 | -5.60 | 34.67 |
| SPY-IC | 65 | 0.2133 | 0.0845 | 0.1287 | 0.7545 | 0.1625 | 0.0507 | 0.6069 | -4.51 | 25.21 |
| QQQ-PS | 64 | 0.0900 | 0.0845 | 0.0055 | 0.5144 | 0.1625 | -0.0725 | 0.3162 | -4.48 | 23.12 |
| QQQ-IC | 64 | 0.1025 | 0.0845 | 0.0179 | 0.5491 | 0.1625 | -0.0601 | 0.3398 | -2.99 | 11.23 |


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
| SPY-PS | 32 | 0.1460 | 0.1331 | 0.0129 | 0.5205 | 0.2374 | -0.0914 | 0.3584 | -5.45 | 33.24 |
| SPY-IC | 32 | 0.2485 | 0.1331 | 0.1155 | 0.6498 | 0.2374 | 0.0112 | 0.5148 | -5.28 | 31.85 |
| QQQ-PS | 30 | 0.0120 | 0.1331 | -0.1211 | 0.2614 | 0.2374 | -0.2254 | 0.1171 | -3.37 | 13.77 |
| QQQ-IC | 30 | 0.2018 | 0.1331 | 0.0687 | 0.6088 | 0.2374 | -0.0356 | 0.4431 | -3.31 | 13.47 |


## PBO (CSCV over 16 entry blocks, proxy pooled)

- pbo: 0.3884226884226884
- mean_logit: 0.13155887784459738
- n_combinations: 12870
- n_configs: 4
- n_blocks: 16
- n_entries: 70


## Month rule (proxy; worst expiry-month vs median month, $ at frozen sizing)

| sleeve | n_months | median_month_usd | worst_month | worst_month_usd | worst_over_median | months_negative | month_rule_pass |
|---|---|---|---|---|---|---|---|
| SPY-PS | 29 | 241.76 | 2026-11 | -2,507 | 10.37 | 3 | no |
| SPY-IC | 29 | 262.88 | 2026-11 | -2,289 | 8.71 | 5 | no |
| QQQ-PS | 29 | 258.31 | 2026-11 | -3,384 | 13.10 | 3 | no |
| QQQ-IC | 29 | 397.25 | 2026-11 | -2,851 | 7.18 | 6 | no |


## Tail report (proxy, pooled)

| sleeve | n | mean_ror | worst_ror | worst_entry | best_ror | mean_win_ror | worst_decile_share_of_loss | full_width_losses | mean_without_worst_1pct | mean_without_best_1pct | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 65 | +2.86% | -85.96% | 2026-10-30 | +6.12% | +5.64% | 1.00 | 0 | +4.24% | +2.81% | -5.60 | 31.67 |
| SPY-IC | 65 | +3.26% | -85.76% | 2026-10-30 | +8.42% | +7.74% | 0.9354 | 0 | +4.65% | +3.18% | -4.51 | 22.21 |
| QQQ-PS | 64 | +1.66% | -100.20% | 2024-07-12 | +6.60% | +6.16% | 1.00 | 1 | +3.27% | +1.58% | -4.48 | 20.12 |
| QQQ-IC | 64 | +2.31% | -95.11% | 2024-07-12 | +11.07% | +10.38% | 0.9231 | 0 | +3.86% | +2.17% | -2.99 | 8.23 |

Worst 10 positions, SPY-PS (pooled):

| entry | expiry | x | ror | net_usd |
|---|---|---|---|---|
| 2026-10-30 | 2026-11-20 | 19.42 | -85.96% | -2,917 |
| 2024-07-12 | 2024-08-02 | 12.46 | -61.38% | -932.00 |
| 2026-02-27 | 2026-03-20 | 19.86 | -8.97% | -271.21 |
| 2025-02-28 | 2025-03-21 | 19.63 | -1.94% | -51.25 |
| 2024-02-16 | 2024-03-08 | 14.24 | +5.19% | 83.63 |
| 2024-06-21 | 2024-07-12 | 13.20 | +5.23% | 84.26 |
| 2024-04-05 | 2024-04-26 | 16.03 | +5.27% | 94.91 |
| 2024-03-15 | 2024-04-05 | 14.41 | +5.32% | 85.71 |
| 2024-01-19 | 2024-02-09 | 13.30 | +5.34% | 151.77 |
| 2024-05-31 | 2024-06-21 | 12.92 | +5.34% | 80.95 |

Worst 10 positions, QQQ-PS (pooled):

| entry | expiry | x | ror | net_usd |
|---|---|---|---|---|
| 2024-07-12 | 2024-08-02 | 17.26 | -100.20% | -1,890 |
| 2026-10-30 | 2026-11-20 | 28.50 | -71.91% | -3,175 |
| 2026-10-09 | 2026-10-30 | 20.55 | -61.39% | -2,137 |
| 2026-10-02 | 2026-10-23 | 21.20 | -12.36% | -442.05 |
| 2026-10-16 | 2026-11-06 | 27.13 | -11.42% | -503.48 |
| 2024-07-19 | 2024-08-09 | 21.51 | +3.83% | 89.96 |
| 2024-01-26 | 2024-02-16 | 17.03 | +5.66% | 90.87 |
| 2024-01-05 | 2024-01-26 | 17.13 | +5.67% | 85.64 |
| 2024-02-02 | 2024-02-23 | 17.22 | +5.80% | 93.02 |
| 2024-03-08 | 2024-03-28 | 19.04 | +5.83% | 104.43 |


## Gate modes and sensitivities (proxy, pooled; descriptive)

| sensitivity | sleeve | n | mean_ror | nw_t | cl_t | net_usd_total | mean_cost_over_credit |
|---|---|---|---|---|---|---|---|
| base | SPY-PS | 65 | +2.86% | 1.69 | 1.64 | 4,560 | +2.93% |
| base | SPY-IC | 65 | +3.26% | 1.76 | 1.72 | 4,380 | +4.04% |
| base | QQQ-PS | 64 | +1.66% | 0.6837 | 0.7198 | 1,871 | +2.57% |
| base | QQQ-IC | 64 | +2.31% | 0.7722 | 0.8196 | 3,907 | +2.83% |
| gate_off | SPY-PS | 150 | +2.63% | 2.11 | 2.27 | 10,382 | +2.96% |
| gate_off | SPY-IC | 150 | +2.52% | 1.70 | 1.89 | 7,539 | +4.08% |
| gate_off | QQQ-PS | 150 | +1.55% | 0.8617 | 1.01 | 6,711 | +2.60% |
| gate_off | QQQ-IC | 150 | -0.22% | -0.0854 | -0.1062 | -2,471 | +2.86% |
| g1_only | SPY-PS | 139 | +3.09% | 2.78 | 3.01 | 10,750 | +3.02% |
| g1_only | SPY-IC | 139 | +3.55% | 2.78 | 3.05 | 11,186 | +4.17% |
| g1_only | QQQ-PS | 139 | +1.86% | 1.01 | 1.24 | 7,035 | +2.65% |
| g1_only | QQQ-IC | 139 | +1.22% | 0.4847 | 0.6062 | 4,161 | +2.91% |
| g2_only | SPY-PS | 75 | +1.93% | 0.9908 | 0.9597 | 4,005 | +2.82% |
| g2_only | SPY-IC | 75 | +1.67% | 0.7965 | 0.7477 | 1,597 | +3.90% |
| g2_only | QQQ-PS | 74 | +0.99% | 0.4136 | 0.4198 | 1,359 | +2.51% |
| g2_only | QQQ-IC | 74 | -0.12% | -0.0374 | -0.0378 | -1,379 | +2.76% |
| costs_x2 | SPY-PS | 65 | +2.69% | 1.59 | 1.54 | 4,291 | +5.85% |
| costs_x2 | SPY-IC | 65 | +2.92% | 1.58 | 1.54 | 3,833 | +8.09% |
| costs_x2 | QQQ-PS | 64 | +1.49% | 0.6165 | 0.6490 | 1,596 | +5.15% |
| costs_x2 | QQQ-IC | 64 | +2.00% | 0.6689 | 0.7103 | 3,397 | +5.66% |
| wing_1.5 | SPY-PS | 65 | -1.97% | -0.9074 | -0.8758 | -2,254 | +19.00% |
| wing_1.5 | SPY-IC | 65 | -2.97% | -1.15 | -1.13 | -3,525 | +16.72% |
| wing_1.5 | QQQ-PS | 64 | -3.07% | -0.9548 | -1.08 | -4,244 | +11.73% |
| wing_1.5 | QQQ-IC | 64 | -3.18% | -0.7580 | -0.8224 | -4,319 | +7.21% |


## Other structures on the proxy (descriptive; not sleeves, never a verdict input)

Single legs, naked shorts and the call spread re-priced on the same entry rows with the frozen smile and costs. Risk: debit = premium; credit spread = width - credit; naked = the 2-sigma stress loss (the matching spread's max loss), Reg-T proxy margin beside. `PS` here is the champion recomputed as a check. Drafts: `ledger/challengers/drafts/sb-c-callspread.json`, `sb-c-nakedput-margin.json`.

| set | structure | underlying | n | mean_ror | nw_t | hit | mean_pnl_usd | worst_ror | mean_premium_usd | mean_margin_usd | total_pnl_usd |
|---|---|---|---|---|---|---|---|---|---|---|---|
| gate ON | long_c1 | QQQ | 64 | -24.31% | -0.6545 | +7.81% | -57.58 | -102.60% | 123.81 | — | -3,685 |
| gate ON | long_p1 | QQQ | 64 | -47.53% | -1.64 | +7.81% | -112.51 | -101.38% | 264.08 | — | -7,201 |
| gate ON | long_c2 | QQQ | 64 | -119.91% | -97.89 | +0.00% | -9.38 | -134.00% | 7.95 | — | -600.03 |
| gate ON | long_p2 | QQQ | 64 | -89.08% | -6.91 | +1.56% | -78.41 | -103.38% | 84.75 | — | -5,018 |
| gate ON | short_p1_naked | QQQ | 64 | +4.35% | 1.61 | +92.19% | 107.64 | -124.66% | -264.08 | 7,893 | 6,889 |
| gate ON | short_c1_naked | QQQ | 64 | +0.87% | 0.5312 | +92.19% | 53.48 | -66.02% | -123.81 | 8,032 | 3,423 |
| gate ON | CS | QQQ | 64 | +0.53% | 0.3279 | +90.62% | 44.11 | -66.40% | -115.86 | — | 2,823 |
| gate ON | PS | QQQ | 64 | +1.66% | 0.6837 | +92.19% | 29.24 | -100.20% | -179.33 | — | 1,871 |
| gate ON | long_c1 | SPY | 65 | -30.69% | -0.8924 | +10.77% | -26.43 | -104.68% | 60.53 | — | -1,718 |
| gate ON | long_p1 | SPY | 65 | -70.54% | -3.81 | +4.62% | -152.44 | -101.40% | 223.74 | — | -9,909 |
| gate ON | long_c2 | SPY | 65 | -147.29% | -72.56 | +0.00% | -5.60 | -173.85% | 3.87 | — | -364.20 |
| gate ON | long_p2 | SPY | 65 | -102.39% | -1,149 | +0.00% | -81.54 | -103.47% | 79.71 | — | -5,300 |
| gate ON | short_p1_naked | SPY | 65 | +6.19% | 3.66 | +95.38% | 148.14 | -82.80% | -223.74 | 9,682 | 9,629 |
| gate ON | short_c1_naked | SPY | 65 | +0.58% | 0.6989 | +89.23% | 22.47 | -27.78% | -60.53 | 9,849 | 1,461 |
| gate ON | CS | SPY | 65 | +0.35% | 0.4262 | +89.23% | 16.87 | -28.03% | -56.66 | — | 1,097 |
| gate ON | PS | SPY | 65 | +2.86% | 1.69 | +93.85% | 66.60 | -85.96% | -144.02 | — | 4,329 |
| every Friday | long_c1 | QQQ | 150 | +29.05% | 0.6296 | +14.00% | 42.74 | -102.60% | 121.23 | — | 6,412 |
| every Friday | long_p1 | QQQ | 150 | -49.59% | -2.45 | +8.00% | -130.59 | -101.38% | 257.72 | — | -19,589 |
| every Friday | long_c2 | QQQ | 150 | -120.29% | -148.71 | +0.00% | -9.18 | -134.00% | 7.76 | — | -1,377 |
| every Friday | long_p2 | QQQ | 150 | -96.50% | -17.29 | +0.67% | -81.03 | -103.38% | 82.83 | — | -12,155 |
| every Friday | short_p1_naked | QQQ | 150 | +4.49% | 2.36 | +92.00% | 125.77 | -124.66% | -257.72 | 7,913 | 18,866 |
| every Friday | short_c1_naked | QQQ | 150 | -1.41% | -0.7076 | +86.00% | -46.81 | -90.15% | -121.23 | 8,051 | -7,022 |
| every Friday | CS | QQQ | 150 | -1.74% | -0.8728 | +84.67% | -55.99 | -90.50% | -113.48 | — | -8,399 |
| every Friday | PS | QQQ | 150 | +1.55% | 0.8617 | +92.00% | 44.74 | -100.20% | -174.89 | — | 6,711 |
| every Friday | long_c1 | SPY | 150 | -10.29% | -0.2726 | +10.00% | 2.66 | -105.35% | 60.16 | — | 398.45 |
| every Friday | long_p1 | SPY | 150 | -67.83% | -4.93 | +5.33% | -150.40 | -101.48% | 222.17 | — | -22,561 |
| every Friday | long_c2 | SPY | 150 | -148.14% | -98.59 | +0.00% | -5.59 | -180.85% | 3.86 | — | -838.98 |
| every Friday | long_p2 | SPY | 150 | -102.41% | -1,672 | +0.00% | -80.81 | -103.54% | 78.99 | — | -12,121 |
| every Friday | short_p1_naked | SPY | 150 | +5.96% | 4.78 | +94.67% | 146.12 | -92.22% | -222.17 | 9,615 | 21,917 |
| every Friday | short_c1_naked | SPY | 150 | +0.09% | 0.1037 | +90.00% | -6.61 | -59.74% | -60.16 | 9,777 | -991.49 |
| every Friday | CS | SPY | 150 | -0.13% | -0.1468 | +90.00% | -12.20 | -59.95% | -56.30 | — | -1,830 |
| every Friday | PS | SPY | 150 | +2.63% | 2.11 | +94.00% | 65.31 | -95.48% | -143.18 | — | 9,796 |


## Marked (panel): sleeve table

| sleeve | window | n | expiries | mean_ror | median_ror | hit | nw_t | nw_p | cl_t | cl_p | net_usd_total | mean_credit_over_width | mean_cost_over_credit | mean_x | mean_risk_usd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | P3 | 14 | 14 | -0.99% | +5.33% | +92.86% | -0.1578 | 0.8770 | -0.1518 | 0.8817 | -615.82 | +5.55% | +2.86% | 18.04 | 3,095 |
| SPY-IC | P3 | 9 | 9 | -2.73% | +7.57% | +88.89% | -0.2837 | 0.7839 | -0.2633 | 0.7990 | -947.71 | +7.58% | +3.57% | 18.04 | 3,017 |
| QQQ-PS | P3 | 14 | 14 | -6.37% | +6.66% | +71.43% | -0.8717 | 0.3992 | -0.9178 | 0.3754 | -3,762 | +6.44% | +2.46% | 25.62 | 4,108 |
| QQQ-IC | P3 | 9 | 9 | -3.81% | +8.77% | +66.67% | -0.4648 | 0.6545 | -0.4297 | 0.6788 | -1,555 | +9.10% | +2.89% | 25.82 | 4,260 |
| SPY-PS | pooled | 14 | 14 | -0.99% | +5.33% | +92.86% | -0.1578 | 0.8770 | -0.1518 | 0.8817 | -615.82 | +5.55% | +2.86% | 18.04 | 3,095 |
| SPY-IC | pooled | 9 | 9 | -2.73% | +7.57% | +88.89% | -0.2837 | 0.7839 | -0.2633 | 0.7990 | -947.71 | +7.58% | +3.57% | 18.04 | 3,017 |
| QQQ-PS | pooled | 14 | 14 | -6.37% | +6.66% | +71.43% | -0.8717 | 0.3992 | -0.9178 | 0.3754 | -3,762 | +6.44% | +2.46% | 25.62 | 4,108 |
| QQQ-IC | pooled | 9 | 9 | -3.81% | +8.77% | +66.67% | -0.4648 | 0.6545 | -0.4297 | 0.6788 | -1,555 | +9.10% | +2.89% | 25.82 | 4,260 |


## Marked vs proxy on the same positions (§6.7 criterion 2)

| sleeve | n_marked | n_overlap | marked_mean_ror | proxy_mean_ror | gap_ror | marked_cost_ror | overlap_pass |
|---|---|---|---|---|---|---|---|
| SPY-PS | 14 | 14 | -0.99% | -0.83% | +0.16% | +0.16% | no |
| SPY-IC | 9 | 9 | -2.73% | -2.40% | +0.32% | +0.29% | no |
| QQQ-PS | 14 | 14 | -6.37% | -6.66% | -0.29% | +0.17% | no |
| QQQ-IC | 9 | 9 | -3.81% | -2.52% | +1.29% | +0.29% | no |


## Marked: tiers, credit, width, cost

| underlying | structure | n | graded | entry_tier_max | mean_credit | mean_width | mean_cost_over_credit |
|---|---|---|---|---|---|---|---|
| QQQ | IC | 10 | 9 | 1 | 4.30 | 47.70 | +2.89% |
| QQQ | PS | 15 | 14 | 1 | 2.86 | 44.67 | +2.46% |
| SPY | IC | 9 | 9 | 1 | 2.50 | 32.67 | +3.57% |
| SPY | PS | 14 | 14 | 1 | 1.84 | 32.79 | +2.86% |


## Marked: skipped entries by reason

| underlying | structure | reason | n |
|---|---|---|---|
| QQQ | IC | OFF:G1 | 3 |
| QQQ | IC | OFF:G2 | 18 |
| QQQ | IC | no_tier1_c2 | 5 |
| QQQ | PS | OFF:G1 | 3 |
| QQQ | PS | OFF:G2 | 18 |
| SPY | IC | OFF:G1 | 3 |
| SPY | IC | OFF:G2 | 19 |
| SPY | IC | no_tier1_c2 | 5 |
| SPY | PS | OFF:G1 | 3 |
| SPY | PS | OFF:G2 | 19 |


## Marked sensitivities (descriptive)

| sensitivity | sleeve | n | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|
| base | SPY-PS | 14 | -0.99% | -0.1578 | -615.82 |
| base | SPY-IC | 9 | -2.73% | -0.2837 | -947.71 |
| base | QQQ-PS | 14 | -6.37% | -0.8717 | -3,762 |
| base | QQQ-IC | 9 | -3.81% | -0.4648 | -1,555 |
| gate_off | SPY-PS | 29 | +2.34% | 0.7543 | 1,723 |
| gate_off | SPY-IC | 23 | +0.55% | 0.1194 | -804.11 |
| gate_off | QQQ-PS | 29 | +0.22% | 0.0559 | -129.26 |
| gate_off | QQQ-IC | 22 | -1.39% | -0.2361 | -1,454 |
| band_0.15 | SPY-PS | 14 | -0.99% | -0.1578 | -615.82 |
| band_0.15 | SPY-IC | 9 | -2.73% | -0.2837 | -947.71 |
| band_0.15 | QQQ-PS | 12 | -8.42% | -1.03 | -4,202 |
| band_0.15 | QQQ-IC | 6 | -9.99% | -0.9924 | -2,658 |
| wing_1.5 | SPY-PS | 14 | -0.37% | -0.0501 | 627.50 |
| wing_1.5 | SPY-IC | 14 | -0.42% | -0.0559 | 615.82 |
| wing_1.5 | QQQ-PS | 14 | -11.90% | -1.01 | -3,504 |
| wing_1.5 | QQQ-IC | 14 | -6.88% | -0.5376 | -1,873 |


## Go / no-go (DESIGN/80 §6.7; t >= 2.0; read 2026-12-01)

| sleeve | n_proxy | mean_proxy | nw_t_proxy | bh_pass | mean_p1 | mean_p2 | mean_p3 | n_marked | mean_marked | gap_ror | worst_over_median | deflated_sr | deflated_sr_null | forward_n | c1_proxy | c2_marked | c3_month | c4_dsr | c4_dsr_null | c5_scale | verdict | note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 65 | +2.86% | 1.69 | no | +1.98% | +5.14% | +2.38% | 14 | -0.99% | +0.16% | 10.37 | 0.1187 | 0.0407 | 6 | no | no | no | yes | yes | no | NO-GO | fails c1_proxy, c2_marked, c3_month |
| SPY-IC | 65 | +3.26% | 1.76 | no | -0.90% | +6.80% | +4.18% | 9 | -2.73% | +0.32% | 8.71 | 0.1287 | 0.0507 | 3 | no | no | no | yes | yes | no | NO-GO | fails c1_proxy, c2_marked, c3_month |
| QQQ-PS | 64 | +1.66% | 0.6837 | no | +0.63% | +6.19% | +0.23% | 14 | -6.37% | -0.29% | 13.10 | 0.0055 | -0.0725 | 7 | no | no | no | yes | no | no | NO-GO | fails c1_proxy, c2_marked, c3_month |
| QQQ-IC | 64 | +2.31% | 0.7722 | no | -3.81% | +7.55% | +3.95% | 9 | -3.81% | +1.29% | 7.18 | 0.0179 | -0.0601 | 6 | no | no | no | yes | no | no | NO-GO | fails c1_proxy, c2_marked, c3_month |


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
