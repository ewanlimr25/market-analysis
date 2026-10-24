# S-B backtest report (generated)


## Inputs

- refreshed: {'index_vol_through': '2026-10-23', 'prices_through': '2026-10-23'}
- proxy: {'index_vol': ['1990-01-02', '2026-10-23'], 'sessions': ['2023-10-24', '2026-10-23'], 'n_sessions': 753}
- marked: {'panel': ['2026-03-13', '2026-10-23'], 'n_entry_sessions': 33}


## Gate ON share of entry sessions (proxy, by year)

| underlying | year | entry_sessions | gate_on | on_share |
|---|---|---|---|---|
| QQQ | 2023 | 6 | 1 | +16.67% |
| QQQ | 2024 | 52 | 26 | +50.00% |
| QQQ | 2025 | 52 | 15 | +28.85% |
| QQQ | 2026 | 40 | 18 | +45.00% |
| QQQ | all | 150 | 60 | +40.00% |
| SPY | 2023 | 6 | 1 | +16.67% |
| SPY | 2024 | 52 | 25 | +48.08% |
| SPY | 2025 | 52 | 16 | +30.77% |
| SPY | 2026 | 40 | 20 | +50.00% |
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
| QQQ-PS | P3 | 26 | 26 | +5.58% | +6.32% | +96.15% | 7.89 | 0.0000 | 7.77 | 0.0000 | 4,993 | +6.04% | +2.16% | 23.69 | 3,447 |
| QQQ-IC | P3 | 26 | 26 | +9.46% | +10.65% | +92.31% | 11.43 | 0.0000 | 10.87 | 0.0000 | 8,192 | +9.86% | +2.35% | 23.69 | 3,328 |
| SPY-PS | pooled | 62 | 62 | +4.19% | +5.62% | +95.16% | 3.91 | 0.0002 | 3.79 | 0.0004 | 7,067 | +5.48% | +2.96% | 17.16 | 2,487 |
| SPY-IC | pooled | 62 | 62 | +4.53% | +7.89% | +87.10% | 3.36 | 0.0014 | 3.37 | 0.0013 | 6,668 | +7.63% | +4.09% | 17.16 | 2,535 |
| QQQ-PS | pooled | 60 | 60 | +4.07% | +6.20% | +96.67% | 2.30 | 0.0249 | 2.27 | 0.0270 | 7,392 | +5.98% | +2.62% | 21.69 | 2,705 |
| QQQ-IC | pooled | 60 | 60 | +4.59% | +10.50% | +88.33% | 1.72 | 0.0908 | 1.82 | 0.0731 | 8,751 | +9.82% | +2.88% | 21.69 | 2,660 |


## BH(0.10) across the four sleeves (proxy, pooled, on the NW p)

| sleeve | n | mean_ror | nw_t | nw_p | bh_pass |
|---|---|---|---|---|---|
| SPY-PS | 62 | +4.19% | 3.91 | 0.0002 | yes |
| SPY-IC | 62 | +4.53% | 3.36 | 0.0014 | yes |
| QQQ-PS | 60 | +4.07% | 2.30 | 0.0249 | yes |
| QQQ-IC | 60 | +4.59% | 1.72 | 0.0908 | yes |


## Deflated Sharpe (6 trials) — proxy pooled

| sleeve | n | sr | sr_star | deflated_sr | dsr_prob | sr_star_null | deflated_sr_null | dsr_prob_null | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 62 | 0.4807 | 0.1485 | 0.3322 | 0.8239 | 0.1678 | 0.3129 | 0.8095 | -7.27 | 57.87 |
| SPY-IC | 62 | 0.4276 | 0.1485 | 0.2791 | 0.8583 | 0.1678 | 0.2598 | 0.8410 | -4.51 | 27.22 |
| QQQ-PS | 60 | 0.2927 | 0.1485 | 0.1442 | 0.7008 | 0.1678 | 0.1249 | 0.6759 | -7.42 | 59.28 |
| QQQ-IC | 60 | 0.2356 | 0.1485 | 0.0871 | 0.6762 | 0.1678 | 0.0677 | 0.6389 | -3.84 | 18.02 |


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
| SPY-PS | 29 | 1.90 | 0.3262 | 1.57 | 0.9091 | 0.2550 | 1.65 | 0.9186 | -5.35 | 31.73 |
| SPY-IC | 29 | 1.85 | 0.3262 | 1.53 | 0.9668 | 0.2550 | 1.60 | 0.9726 | -3.58 | 14.68 |
| QQQ-PS | 26 | 1.52 | 0.3262 | 1.20 | 0.8847 | 0.2550 | 1.27 | 0.8980 | -5.08 | 28.89 |
| QQQ-IC | 26 | 2.13 | 0.3262 | 1.81 | 0.9620 | 0.2550 | 1.88 | 0.9674 | -3.66 | 16.05 |


## PBO (CSCV over 16 entry blocks, proxy pooled)

- pbo: 0.5032634032634032
- mean_logit: 0.1783535669636181
- n_combinations: 12870
- n_configs: 4
- n_blocks: 16
- n_entries: 66


## Month rule (proxy; worst expiry-month vs median month, $ at frozen sizing)

| sleeve | n_months | median_month_usd | worst_month | worst_month_usd | worst_over_median | months_negative | month_rule_pass |
|---|---|---|---|---|---|---|---|
| SPY-PS | 28 | 245.68 | 2024-08 | -396.47 | 1.61 | 2 | yes |
| SPY-IC | 28 | 264.47 | 2024-08 | -1,537 | 5.81 | 4 | no |
| QQQ-PS | 28 | 271.59 | 2024-08 | -1,325 | 4.88 | 2 | no |
| QQQ-IC | 28 | 411.54 | 2024-01 | -1,574 | 3.82 | 4 | no |


## Tail report (proxy, pooled)

| sleeve | n | mean_ror | worst_ror | worst_entry | best_ror | mean_win_ror | worst_decile_share_of_loss | full_width_losses | mean_without_worst_1pct | mean_without_best_1pct | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 62 | +4.19% | -61.38% | 2024-07-12 | +6.12% | +5.63% | 1.00 | 0 | +5.26% | +4.16% | -7.27 | 54.87 |
| SPY-IC | 62 | +4.53% | -60.67% | 2024-07-12 | +8.42% | +7.72% | 0.9463 | 0 | +5.60% | +4.47% | -4.51 | 24.22 |
| QQQ-PS | 60 | +4.07% | -100.20% | 2024-07-12 | +6.60% | +6.15% | 1.00 | 1 | +5.84% | +4.03% | -7.42 | 56.28 |
| QQQ-IC | 60 | +4.59% | -95.11% | 2024-07-12 | +11.01% | +10.36% | 0.9939 | 0 | +6.28% | +4.48% | -3.84 | 15.02 |

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
| 2026-10-02 | 2026-10-23 | 21.20 | -12.36% | -442.05 |
| 2024-07-19 | 2024-08-09 | 21.51 | +3.83% | 89.96 |
| 2024-01-26 | 2024-02-16 | 17.03 | +5.66% | 90.87 |
| 2024-01-05 | 2024-01-26 | 17.13 | +5.67% | 85.64 |
| 2024-02-02 | 2024-02-23 | 17.22 | +5.80% | 93.02 |
| 2024-03-08 | 2024-03-28 | 19.04 | +5.83% | 104.43 |
| 2025-02-28 | 2025-03-21 | 22.66 | +5.85% | 153.54 |
| 2024-02-16 | 2024-03-08 | 18.60 | +5.86% | 104.89 |
| 2024-02-23 | 2024-03-15 | 17.70 | +5.88% | 99.73 |


## Gate modes and sensitivities (proxy, pooled; descriptive)

| sensitivity | sleeve | n | mean_ror | nw_t | cl_t | net_usd_total | mean_cost_over_credit |
|---|---|---|---|---|---|---|---|
| base | SPY-PS | 62 | +4.19% | 3.91 | 3.79 | 7,067 | +2.96% |
| base | SPY-IC | 62 | +4.53% | 3.36 | 3.37 | 6,668 | +4.09% |
| base | QQQ-PS | 60 | +4.07% | 2.30 | 2.27 | 7,392 | +2.62% |
| base | QQQ-IC | 60 | +4.59% | 1.72 | 1.82 | 8,751 | +2.88% |
| gate_off | SPY-PS | 150 | +3.23% | 2.93 | 3.26 | 13,327 | +3.01% |
| gate_off | SPY-IC | 150 | +3.02% | 2.20 | 2.53 | 9,972 | +4.16% |
| gate_off | QQQ-PS | 150 | +2.62% | 1.60 | 1.90 | 12,888 | +2.66% |
| gate_off | QQQ-IC | 150 | +0.59% | 0.2342 | 0.2962 | 2,241 | +2.93% |
| g1_only | SPY-PS | 139 | +3.74% | 4.08 | 4.70 | 13,695 | +3.08% |
| g1_only | SPY-IC | 139 | +4.09% | 3.65 | 4.23 | 13,619 | +4.25% |
| g1_only | QQQ-PS | 139 | +3.02% | 1.83 | 2.28 | 13,212 | +2.71% |
| g1_only | QQQ-IC | 139 | +2.10% | 0.8673 | 1.11 | 8,873 | +2.98% |
| g2_only | SPY-PS | 72 | +3.03% | 1.85 | 1.80 | 6,512 | +2.84% |
| g2_only | SPY-IC | 72 | +2.70% | 1.46 | 1.37 | 3,886 | +3.94% |
| g2_only | QQQ-PS | 70 | +3.02% | 1.52 | 1.47 | 6,881 | +2.54% |
| g2_only | QQQ-IC | 70 | +1.70% | 0.5731 | 0.5804 | 3,465 | +2.80% |
| costs_x2 | SPY-PS | 62 | +4.02% | 3.75 | 3.63 | 6,812 | +5.93% |
| costs_x2 | SPY-IC | 62 | +4.19% | 3.09 | 3.11 | 6,147 | +8.19% |
| costs_x2 | QQQ-PS | 60 | +3.90% | 2.21 | 2.17 | 7,138 | +5.24% |
| costs_x2 | QQQ-IC | 60 | +4.27% | 1.60 | 1.70 | 8,277 | +5.77% |
| wing_1.5 | SPY-PS | 62 | -0.52% | -0.3162 | -0.3055 | -586.09 | +19.37% |
| wing_1.5 | SPY-IC | 62 | -1.65% | -0.7308 | -0.7366 | -1,991 | +16.93% |
| wing_1.5 | QQQ-PS | 60 | +0.55% | 0.3045 | 0.3026 | 368.88 | +11.93% |
| wing_1.5 | QQQ-IC | 60 | +0.17% | 0.0474 | 0.0501 | -200.06 | +7.33% |


## Other structures on the proxy (descriptive; not sleeves, never a verdict input)

Single legs, naked shorts and the call spread re-priced on the same entry rows with the frozen smile and costs. Risk: debit = premium; credit spread = width - credit; naked = the 2-sigma stress loss (the matching spread's max loss), Reg-T proxy margin beside. `PS` here is the champion recomputed as a check. Drafts: `ledger/challengers/drafts/sb-c-callspread.json`, `sb-c-nakedput-margin.json`.

| set | structure | underlying | n | mean_ror | nw_t | hit | mean_pnl_usd | worst_ror | mean_premium_usd | mean_margin_usd | total_pnl_usd |
|---|---|---|---|---|---|---|---|---|---|---|---|
| gate ON | long_c1 | QQQ | 60 | -19.18% | -0.4872 | +8.33% | -48.89 | -102.60% | 119.70 | — | -2,933 |
| gate ON | long_p1 | QQQ | 60 | -73.18% | -3.09 | +3.33% | -203.38 | -101.38% | 255.31 | — | -12,203 |
| gate ON | long_c2 | QQQ | 60 | -120.42% | -97.75 | +0.00% | -9.08 | -134.00% | 7.66 | — | -544.62 |
| gate ON | long_p2 | QQQ | 60 | -88.24% | -6.42 | +1.67% | -75.38 | -103.38% | 82.28 | — | -4,523 |
| gate ON | short_p1_naked | QQQ | 60 | +6.75% | 3.05 | +96.67% | 198.58 | -124.66% | -255.31 | 7,790 | 11,915 |
| gate ON | short_c1_naked | QQQ | 60 | +0.64% | 0.3693 | +91.67% | 44.84 | -66.02% | -119.70 | 7,925 | 2,690 |
| gate ON | CS | QQQ | 60 | +0.31% | 0.1773 | +90.00% | 35.76 | -66.40% | -112.04 | — | 2,146 |
| gate ON | PS | QQQ | 60 | +4.07% | 2.30 | +96.67% | 123.21 | -100.20% | -173.03 | — | 7,392 |
| gate ON | long_c1 | SPY | 62 | -27.21% | -0.7582 | +11.29% | -23.62 | -104.68% | 59.48 | — | -1,465 |
| gate ON | long_p1 | SPY | 62 | -85.19% | -7.27 | +3.23% | -194.70 | -101.40% | 219.26 | — | -12,072 |
| gate ON | long_c2 | SPY | 62 | -147.86% | -71.72 | +0.00% | -5.52 | -173.85% | 3.80 | — | -342.49 |
| gate ON | long_p2 | SPY | 62 | -102.42% | -1,133 | +0.00% | -80.17 | -103.47% | 78.36 | — | -4,971 |
| gate ON | short_p1_naked | SPY | 62 | +7.53% | 7.08 | +96.77% | 190.44 | -57.60% | -219.26 | 9,602 | 11,807 |
| gate ON | short_c1_naked | SPY | 62 | +0.49% | 0.5731 | +88.71% | 19.68 | -27.78% | -59.48 | 9,767 | 1,220 |
| gate ON | CS | SPY | 62 | +0.27% | 0.3110 | +88.71% | 14.16 | -28.03% | -55.67 | — | 877.92 |
| gate ON | PS | SPY | 62 | +4.19% | 3.91 | +95.16% | 110.26 | -61.38% | -140.90 | — | 6,836 |
| every Friday | long_c1 | QQQ | 150 | +35.43% | 0.7676 | +15.33% | 50.15 | -102.60% | 118.01 | — | 7,523 |
| every Friday | long_p1 | QQQ | 150 | -61.29% | -3.28 | +6.00% | -167.45 | -101.46% | 250.64 | — | -25,118 |
| every Friday | long_c2 | QQQ | 150 | -120.91% | -141.40 | +0.00% | -8.95 | -139.37% | 7.53 | — | -1,342 |
| every Friday | long_p2 | QQQ | 150 | -96.55% | -17.29 | +0.67% | -78.96 | -103.68% | 80.77 | — | -11,844 |
| every Friday | short_p1_naked | QQQ | 150 | +5.57% | 3.17 | +94.00% | 162.70 | -124.66% | -250.64 | 7,827 | 24,405 |
| every Friday | short_c1_naked | QQQ | 150 | -1.70% | -0.8509 | +84.67% | -54.18 | -90.15% | -118.01 | 7,962 | -8,127 |
| every Friday | CS | QQQ | 150 | -2.03% | -1.02 | +83.33% | -63.13 | -90.50% | -110.48 | — | -9,469 |
| every Friday | PS | QQQ | 150 | +2.62% | 1.60 | +94.00% | 83.73 | -100.20% | -169.87 | — | 12,560 |
| every Friday | long_c1 | SPY | 150 | -5.64% | -0.1495 | +11.33% | 5.41 | -105.35% | 58.95 | — | 811.16 |
| every Friday | long_p1 | SPY | 150 | -74.51% | -6.09 | +4.67% | -166.46 | -101.52% | 217.45 | — | -24,969 |
| every Friday | long_c2 | SPY | 150 | -149.22% | -92.09 | +0.00% | -5.50 | -188.16% | 3.78 | — | -825.47 |
| every Friday | long_p2 | SPY | 150 | -102.46% | -1,543 | +0.00% | -79.23 | -103.74% | 77.42 | — | -11,884 |
| every Friday | short_p1_naked | SPY | 150 | +6.57% | 5.94 | +95.33% | 162.21 | -92.22% | -217.45 | 9,511 | 24,331 |
| every Friday | short_c1_naked | SPY | 150 | -0.02% | -0.0258 | +88.00% | -9.33 | -59.74% | -58.95 | 9,669 | -1,400 |
| every Friday | CS | SPY | 150 | -0.25% | -0.2778 | +88.00% | -14.84 | -59.95% | -55.17 | — | -2,226 |
| every Friday | PS | SPY | 150 | +3.23% | 2.93 | +94.67% | 82.98 | -95.48% | -140.03 | — | 12,448 |


## Marked (panel): sleeve table

| sleeve | window | n | expiries | mean_ror | median_ror | hit | nw_t | nw_p | cl_t | cl_p | net_usd_total | mean_credit_over_width | mean_cost_over_credit | mean_x | mean_risk_usd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | P3 | 11 | 11 | +5.65% | +5.51% | +100.00% | 22.21 | 0.0000 | 23.85 | 0.0000 | 1,872 | +5.48% | +2.61% | 17.61 | 2,971 |
| SPY-IC | P3 | 8 | 8 | +7.63% | +7.77% | +100.00% | 23.96 | 0.0000 | 26.27 | 0.0000 | 1,836 | +7.33% | +3.61% | 17.87 | 2,987 |
| QQQ-PS | P3 | 10 | 10 | +4.53% | +6.75% | +90.00% | 1.96 | 0.0822 | 1.95 | 0.0832 | 1,957 | +6.43% | +2.56% | 25.42 | 4,031 |
| QQQ-IC | P3 | 6 | 6 | +5.74% | +8.97% | +83.33% | 1.69 | 0.1517 | 1.54 | 0.1830 | 1,574 | +8.61% | +2.91% | 24.74 | 4,216 |
| SPY-PS | pooled | 11 | 11 | +5.65% | +5.51% | +100.00% | 22.21 | 0.0000 | 23.85 | 0.0000 | 1,872 | +5.48% | +2.61% | 17.61 | 2,971 |
| SPY-IC | pooled | 8 | 8 | +7.63% | +7.77% | +100.00% | 23.96 | 0.0000 | 26.27 | 0.0000 | 1,836 | +7.33% | +3.61% | 17.87 | 2,987 |
| QQQ-PS | pooled | 10 | 10 | +4.53% | +6.75% | +90.00% | 1.96 | 0.0822 | 1.95 | 0.0832 | 1,957 | +6.43% | +2.56% | 25.42 | 4,031 |
| QQQ-IC | pooled | 6 | 6 | +5.74% | +8.97% | +83.33% | 1.69 | 0.1517 | 1.54 | 0.1830 | 1,574 | +8.61% | +2.91% | 24.74 | 4,216 |


## Marked vs proxy on the same positions (§6.7 criterion 2)

| sleeve | n_marked | n_overlap | marked_mean_ror | proxy_mean_ror | gap_ror | marked_cost_ror | overlap_pass |
|---|---|---|---|---|---|---|---|
| SPY-PS | 11 | 11 | +5.65% | +5.67% | +0.02% | +0.15% | yes |
| SPY-IC | 8 | 8 | +7.63% | +8.02% | +0.39% | +0.28% | no |
| QQQ-PS | 10 | 10 | +4.53% | +4.49% | -0.04% | +0.18% | yes |
| QQQ-IC | 6 | 6 | +5.74% | +7.48% | +1.74% | +0.28% | no |


## Marked: tiers, credit, width, cost

| underlying | structure | n | graded | entry_tier_max | mean_credit | mean_width | mean_cost_over_credit |
|---|---|---|---|---|---|---|---|
| QQQ | IC | 8 | 6 | 1 | 4.16 | 46.50 | +2.91% |
| QQQ | PS | 13 | 10 | 1 | 2.78 | 43.46 | +2.56% |
| SPY | IC | 8 | 8 | 1 | 2.38 | 32.25 | +3.61% |
| SPY | PS | 13 | 11 | 1 | 1.76 | 32.54 | +2.61% |


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
| base | QQQ-PS | 10 | +4.53% | 1.96 | 1,957 |
| base | QQQ-IC | 6 | +5.74% | 1.69 | 1,574 |
| gate_off | SPY-PS | 25 | +5.58% | 32.92 | 4,090 |
| gate_off | SPY-IC | 21 | +4.35% | 1.48 | 1,799 |
| gate_off | QQQ-PS | 25 | +5.64% | 6.02 | 5,589 |
| gate_off | QQQ-IC | 19 | +2.00% | 0.3484 | 1,675 |
| band_0.15 | SPY-PS | 11 | +5.65% | 22.21 | 1,872 |
| band_0.15 | SPY-IC | 8 | +7.63% | 23.96 | 1,836 |
| band_0.15 | QQQ-PS | 8 | +4.19% | 1.51 | 1,517 |
| band_0.15 | QQQ-IC | 3 | +2.93% | 0.6216 | 471.17 |
| wing_1.5 | SPY-PS | 11 | +7.60% | 23.62 | 2,039 |
| wing_1.5 | SPY-IC | 11 | +7.09% | 2.34 | 1,893 |
| wing_1.5 | QQQ-PS | 10 | +5.49% | 1.41 | 1,089 |
| wing_1.5 | QQQ-IC | 10 | +11.92% | 2.79 | 2,268 |


## Go / no-go (DESIGN/80 §6.7; t >= 2.0; read 2026-12-01)

| sleeve | n_proxy | mean_proxy | nw_t_proxy | bh_pass | mean_p1 | mean_p2 | mean_p3 | n_marked | mean_marked | gap_ror | worst_over_median | deflated_sr | deflated_sr_null | forward_n | c1_proxy | c2_marked | c3_month | c4_dsr | c4_dsr_null | c5_scale | verdict | note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 62 | +4.19% | 3.91 | yes | +1.98% | +5.14% | +5.18% | 11 | +5.65% | +0.02% | 1.61 | 0.3322 | 0.3129 | 3 | yes | yes | yes | yes | yes | no | GO-MIN | clears 1-4; one contract until the forward ledger holds >= 40 graded positions (now 3) |
| SPY-IC | 62 | +4.53% | 3.36 | yes | -0.90% | +6.80% | +6.99% | 8 | +7.63% | +0.39% | 5.81 | 0.2791 | 0.2598 | 2 | no | no | no | yes | yes | no | NO-GO | fails c1_proxy, c2_marked, c3_month |
| QQQ-PS | 60 | +4.07% | 2.30 | yes | +0.63% | +6.19% | +5.58% | 10 | +4.53% | -0.04% | 4.88 | 0.1442 | 0.1249 | 3 | yes | yes | no | yes | yes | no | NO-GO | fails c3_month |
| QQQ-IC | 60 | +4.59% | 1.72 | yes | -3.81% | +7.55% | +9.46% | 6 | +5.74% | +1.74% | 3.82 | 0.0871 | 0.0677 | 3 | no | no | no | yes | yes | no | NO-GO | fails c1_proxy, c2_marked, c3_month |


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
