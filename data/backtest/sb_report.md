# S-B backtest report (generated)


## Inputs

- refreshed: {'index_vol_through': '2026-10-02', 'prices_through': '2026-10-02'}
- proxy: {'index_vol': ['1990-01-02', '2026-10-02'], 'sessions': ['2023-10-03', '2026-10-02'], 'n_sessions': 753}
- marked: {'panel': ['2026-03-13', '2026-10-02'], 'n_entry_sessions': 30}


## Gate ON share of entry sessions (proxy, by year)

| underlying | year | entry_sessions | gate_on | on_share |
|---|---|---|---|---|
| QQQ | 2023 | 9 | 1 | +11.11% |
| QQQ | 2024 | 52 | 26 | +50.00% |
| QQQ | 2025 | 52 | 15 | +28.85% |
| QQQ | 2026 | 37 | 16 | +43.24% |
| QQQ | all | 150 | 58 | +38.67% |
| SPY | 2023 | 9 | 1 | +11.11% |
| SPY | 2024 | 52 | 25 | +48.08% |
| SPY | 2025 | 52 | 16 | +30.77% |
| SPY | 2026 | 37 | 18 | +48.65% |
| SPY | all | 150 | 60 | +40.00% |


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
| SPY-PS | P3 | 27 | 27 | +5.16% | +5.71% | +96.30% | 10.48 | 0.0000 | 9.47 | 0.0000 | 3,953 | +5.53% | +2.57% | 18.10 | 2,844 |
| SPY-IC | P3 | 27 | 27 | +6.93% | +8.01% | +92.59% | 10.48 | 0.0000 | 9.21 | 0.0000 | 5,169 | +7.67% | +3.55% | 18.10 | 2,787 |
| QQQ-PS | P3 | 24 | 24 | +6.30% | +6.34% | +100.00% | 148.93 | 0.0000 | 187.35 | 0.0000 | 5,220 | +6.05% | +2.16% | 23.91 | 3,440 |
| QQQ-IC | P3 | 24 | 24 | +10.17% | +10.70% | +95.83% | 20.84 | 0.0000 | 19.69 | 0.0000 | 8,139 | +9.87% | +2.35% | 23.91 | 3,323 |
| SPY-PS | pooled | 60 | 60 | +4.14% | +5.62% | +95.00% | 3.75 | 0.0004 | 3.62 | 0.0006 | 6,774 | +5.48% | +2.97% | 17.23 | 2,482 |
| SPY-IC | pooled | 60 | 60 | +4.42% | +7.89% | +86.67% | 3.19 | 0.0023 | 3.18 | 0.0023 | 6,261 | +7.63% | +4.11% | 17.23 | 2,534 |
| QQQ-PS | pooled | 58 | 58 | +4.32% | +6.21% | +98.28% | 2.38 | 0.0205 | 2.35 | 0.0221 | 7,620 | +5.98% | +2.64% | 21.72 | 2,677 |
| QQQ-IC | pooled | 58 | 58 | +4.71% | +10.50% | +89.66% | 1.71 | 0.0923 | 1.82 | 0.0739 | 8,698 | +9.82% | +2.90% | 21.72 | 2,635 |


## BH(0.10) across the four sleeves (proxy, pooled, on the NW p)

| sleeve | n | mean_ror | nw_t | nw_p | bh_pass |
|---|---|---|---|---|---|
| SPY-PS | 60 | +4.14% | 3.75 | 0.0004 | yes |
| SPY-IC | 60 | +4.42% | 3.19 | 0.0023 | yes |
| QQQ-PS | 58 | +4.32% | 2.38 | 0.0205 | yes |
| QQQ-IC | 58 | +4.71% | 1.71 | 0.0923 | yes |


## Deflated Sharpe (6 trials) — proxy pooled

| sleeve | n | sr | sr_star | deflated_sr | dsr_prob | sr_star_null | deflated_sr_null | dsr_prob_null | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 60 | 0.4679 | 0.1330 | 0.3348 | 0.8284 | 0.1707 | 0.2971 | 0.7999 | -7.15 | 56.08 |
| SPY-IC | 60 | 0.4109 | 0.1330 | 0.2779 | 0.8603 | 0.1707 | 0.2402 | 0.8251 | -4.44 | 26.39 |
| QQQ-PS | 58 | 0.3090 | 0.1330 | 0.1760 | 0.7283 | 0.1707 | 0.1383 | 0.6835 | -7.61 | 60.91 |
| QQQ-IC | 58 | 0.2391 | 0.1330 | 0.1061 | 0.7070 | 0.1707 | 0.0684 | 0.6372 | -3.85 | 17.91 |


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
| SPY-PS | 27 | 1.82 | 23.25 | -21.43 | 0.0000 | 0.2654 | 1.56 | 0.9124 | -5.16 | 29.76 |
| SPY-IC | 27 | 1.77 | 23.25 | -21.48 | 0.0000 | 0.2654 | 1.51 | 0.9687 | -3.44 | 13.66 |
| QQQ-PS | 24 | 38.24 | 23.25 | 14.99 | 0.9978 | 0.2654 | 37.98 | 1.0000 | -0.4549 | 2.70 |
| QQQ-IC | 24 | 4.02 | 23.25 | -19.23 | 0.0000 | 0.2654 | 3.75 | 0.9469 | -4.85 | 26.69 |


## PBO (CSCV over 16 entry blocks, proxy pooled)

- pbo: 0.6583527583527583
- mean_logit: -0.11987745954246806
- n_combinations: 12870
- n_configs: 4
- n_blocks: 16
- n_entries: 64


## Month rule (proxy; worst expiry-month vs median month, $ at frozen sizing)

| sleeve | n_months | median_month_usd | worst_month | worst_month_usd | worst_over_median | months_negative | month_rule_pass |
|---|---|---|---|---|---|---|---|
| SPY-PS | 28 | 241.49 | 2024-08 | -396.47 | 1.64 | 2 | yes |
| SPY-IC | 28 | 251.10 | 2024-08 | -1,537 | 6.12 | 4 | no |
| QQQ-PS | 28 | 271.59 | 2024-08 | -1,325 | 4.88 | 1 | no |
| QQQ-IC | 28 | 409.24 | 2024-01 | -1,574 | 3.85 | 4 | no |


## Tail report (proxy, pooled)

| sleeve | n | mean_ror | worst_ror | worst_entry | best_ror | mean_win_ror | worst_decile_share_of_loss | full_width_losses | mean_without_worst_1pct | mean_without_best_1pct | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 60 | +4.14% | -61.38% | 2024-07-12 | +6.12% | +5.63% | 1.00 | 0 | +5.26% | +4.11% | -7.15 | 53.08 |
| SPY-IC | 60 | +4.42% | -60.67% | 2024-07-12 | +8.42% | +7.72% | 0.9463 | 0 | +5.52% | +4.35% | -4.44 | 23.39 |
| QQQ-PS | 58 | +4.32% | -100.20% | 2024-07-12 | +6.60% | +6.15% | 1.00 | 1 | +6.15% | +4.28% | -7.61 | 57.91 |
| QQQ-IC | 58 | +4.71% | -95.11% | 2024-07-12 | +11.01% | +10.36% | 0.9937 | 0 | +6.47% | +4.60% | -3.85 | 14.91 |

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
| base | SPY-PS | 60 | +4.14% | 3.75 | 3.62 | 6,774 | +2.97% |
| base | SPY-IC | 60 | +4.42% | 3.19 | 3.18 | 6,261 | +4.11% |
| base | QQQ-PS | 58 | +4.32% | 2.38 | 2.35 | 7,620 | +2.64% |
| base | QQQ-IC | 58 | +4.71% | 1.71 | 1.82 | 8,698 | +2.90% |
| gate_off | SPY-PS | 150 | +3.23% | 2.92 | 3.25 | 13,358 | +3.04% |
| gate_off | SPY-IC | 150 | +2.63% | 1.88 | 2.16 | 8,333 | +4.20% |
| gate_off | QQQ-PS | 150 | +2.74% | 1.67 | 1.99 | 13,194 | +2.69% |
| gate_off | QQQ-IC | 150 | +0.48% | 0.1880 | 0.2370 | 2,074 | +2.96% |
| g1_only | SPY-PS | 139 | +3.74% | 4.08 | 4.70 | 13,727 | +3.11% |
| g1_only | SPY-IC | 139 | +3.66% | 3.15 | 3.66 | 11,980 | +4.30% |
| g1_only | QQQ-PS | 139 | +3.15% | 1.91 | 2.38 | 13,518 | +2.74% |
| g1_only | QQQ-IC | 139 | +1.98% | 0.8147 | 1.04 | 8,706 | +3.01% |
| g2_only | SPY-PS | 70 | +2.96% | 1.76 | 1.71 | 6,218 | +2.85% |
| g2_only | SPY-IC | 70 | +2.55% | 1.35 | 1.26 | 3,479 | +3.94% |
| g2_only | QQQ-PS | 68 | +3.20% | 1.57 | 1.52 | 7,108 | +2.55% |
| g2_only | QQQ-IC | 68 | +1.72% | 0.5653 | 0.5726 | 3,412 | +2.81% |
| costs_x2 | SPY-PS | 60 | +3.97% | 3.59 | 3.47 | 6,527 | +5.95% |
| costs_x2 | SPY-IC | 60 | +4.08% | 2.93 | 2.93 | 5,756 | +8.21% |
| costs_x2 | QQQ-PS | 58 | +4.15% | 2.29 | 2.26 | 7,375 | +5.27% |
| costs_x2 | QQQ-IC | 58 | +4.40% | 1.59 | 1.70 | 8,241 | +5.81% |
| wing_1.5 | SPY-PS | 60 | -0.60% | -0.3513 | -0.3390 | -683.64 | +19.46% |
| wing_1.5 | SPY-IC | 60 | -1.86% | -0.7993 | -0.8023 | -2,229 | +16.98% |
| wing_1.5 | QQQ-PS | 58 | +1.09% | 0.6119 | 0.6112 | 928.48 | +11.98% |
| wing_1.5 | QQQ-IC | 58 | +0.52% | 0.1415 | 0.1503 | 155.31 | +7.37% |


## Other structures on the proxy (descriptive; not sleeves, never a verdict input)

Single legs, naked shorts and the call spread re-priced on the same entry rows with the frozen smile and costs. Risk: debit = premium; credit spread = width - credit; naked = the 2-sigma stress loss (the matching spread's max loss), Reg-T proxy margin beside. `PS` here is the champion recomputed as a check. Drafts: `ledger/challengers/drafts/sb-c-callspread.json`, `sb-c-nakedput-margin.json`.

| set | structure | underlying | n | mean_ror | nw_t | hit | mean_pnl_usd | worst_ror | mean_premium_usd | mean_margin_usd | total_pnl_usd |
|---|---|---|---|---|---|---|---|---|---|---|---|
| gate ON | long_c1 | QQQ | 58 | -16.34% | -0.4027 | +8.62% | -45.19 | -102.60% | 118.52 | — | -2,621 |
| gate ON | long_p1 | QQQ | 58 | -75.66% | -3.10 | +1.72% | -210.33 | -101.38% | 252.77 | — | -12,199 |
| gate ON | long_c2 | QQQ | 58 | -120.60% | -96.28 | +0.00% | -9.01 | -134.00% | 7.59 | — | -522.37 |
| gate ON | long_p2 | QQQ | 58 | -87.77% | -6.18 | +1.72% | -74.17 | -103.38% | 81.38 | — | -4,302 |
| gate ON | short_p1_naked | QQQ | 58 | +6.98% | 3.07 | +98.28% | 205.55 | -124.66% | -252.77 | 7,686 | 11,922 |
| gate ON | short_c1_naked | QQQ | 58 | +0.51% | 0.2892 | +91.38% | 41.16 | -66.02% | -118.52 | 7,819 | 2,387 |
| gate ON | CS | QQQ | 58 | +0.18% | 0.1025 | +89.66% | 32.15 | -66.40% | -110.93 | — | 1,865 |
| gate ON | PS | QQQ | 58 | +4.32% | 2.38 | +98.28% | 131.38 | -100.20% | -171.38 | — | 7,620 |
| gate ON | long_c1 | SPY | 60 | -24.68% | -0.6678 | +11.67% | -22.19 | -104.68% | 59.30 | — | -1,331 |
| gate ON | long_p1 | SPY | 60 | -84.67% | -7.01 | +3.33% | -193.22 | -101.40% | 218.68 | — | -11,593 |
| gate ON | long_c2 | SPY | 60 | -148.04% | -69.89 | +0.00% | -5.51 | -173.85% | 3.79 | — | -330.71 |
| gate ON | long_p2 | SPY | 60 | -102.42% | -1,103 | +0.00% | -79.92 | -103.47% | 78.11 | — | -4,795 |
| gate ON | short_p1_naked | SPY | 60 | +7.49% | 6.82 | +96.67% | 188.96 | -57.60% | -218.68 | 9,509 | 11,338 |
| gate ON | short_c1_naked | SPY | 60 | +0.43% | 0.4874 | +88.33% | 18.25 | -27.78% | -59.30 | 9,674 | 1,095 |
| gate ON | CS | SPY | 60 | +0.21% | 0.2328 | +88.33% | 12.74 | -28.03% | -55.51 | — | 764.34 |
| gate ON | PS | SPY | 60 | +4.14% | 3.75 | +95.00% | 109.04 | -61.38% | -140.57 | — | 6,542 |
| every Friday | long_c1 | QQQ | 150 | +40.65% | 0.8797 | +16.00% | 55.44 | -102.61% | 116.40 | — | 8,316 |
| every Friday | long_p1 | QQQ | 150 | -62.63% | -3.35 | +5.33% | -168.33 | -101.46% | 247.13 | — | -25,250 |
| every Friday | long_c2 | QQQ | 150 | -121.27% | -136.66 | +0.00% | -8.84 | -139.37% | 7.42 | — | -1,326 |
| every Friday | long_p2 | QQQ | 150 | -96.58% | -17.30 | +0.67% | -77.83 | -103.68% | 79.65 | — | -11,675 |
| every Friday | short_p1_naked | QQQ | 150 | +5.69% | 3.24 | +94.67% | 163.61 | -124.66% | -247.13 | 7,727 | 24,541 |
| every Friday | short_c1_naked | QQQ | 150 | -1.92% | -0.9622 | +84.00% | -59.45 | -90.15% | -116.40 | 7,860 | -8,917 |
| every Friday | CS | QQQ | 150 | -2.26% | -1.13 | +82.67% | -68.29 | -90.50% | -108.98 | — | -10,244 |
| every Friday | PS | QQQ | 150 | +2.74% | 1.67 | +94.67% | 85.78 | -100.20% | -167.48 | — | 12,866 |
| every Friday | long_c1 | SPY | 150 | +9.87% | 0.2485 | +12.67% | 11.59 | -105.35% | 58.37 | — | 1,739 |
| every Friday | long_p1 | SPY | 150 | -74.52% | -6.09 | +4.67% | -164.34 | -101.52% | 215.33 | — | -24,650 |
| every Friday | long_c2 | SPY | 150 | -149.89% | -87.22 | +0.00% | -5.46 | -188.16% | 3.74 | — | -818.71 |
| every Friday | long_p2 | SPY | 150 | -102.48% | -1,493 | +0.00% | -78.48 | -103.74% | 76.67 | — | -11,771 |
| every Friday | short_p1_naked | SPY | 150 | +6.57% | 5.95 | +95.33% | 160.10 | -92.22% | -215.33 | 9,408 | 24,015 |
| every Friday | short_c1_naked | SPY | 150 | -0.39% | -0.4163 | +86.67% | -15.51 | -59.74% | -58.37 | 9,565 | -2,326 |
| every Friday | CS | SPY | 150 | -0.62% | -0.6558 | +86.67% | -20.97 | -59.95% | -54.63 | — | -3,145 |
| every Friday | PS | SPY | 150 | +3.23% | 2.92 | +94.67% | 81.62 | -95.48% | -138.66 | — | 12,243 |


## Marked (panel): sleeve table

| sleeve | window | n | expiries | mean_ror | median_ror | hit | nw_t | nw_p | cl_t | cl_p | net_usd_total | mean_credit_over_width | mean_cost_over_credit | mean_x | mean_risk_usd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | P3 | 9 | 9 | +5.83% | +5.96% | +100.00% | 24.57 | 0.0000 | 23.17 | 0.0000 | 1,627 | +5.63% | +2.44% | 18.18 | 3,070 |
| SPY-IC | P3 | 6 | 6 | +7.69% | +7.80% | +100.00% | 18.61 | 0.0000 | 20.91 | 0.0000 | 1,463 | +7.37% | +3.44% | 18.79 | 3,148 |
| QQQ-PS | P3 | 8 | 8 | +7.02% | +6.86% | +100.00% | 34.01 | 0.0000 | 21.12 | 0.0000 | 2,336 | +6.72% | +2.60% | 26.51 | 4,163 |
| QQQ-IC | P3 | 4 | 4 | +9.59% | +9.78% | +100.00% | 22.69 | 0.0002 | 13.01 | 0.0010 | 1,681 | +8.98% | +2.98% | 26.59 | 4,367 |
| SPY-PS | pooled | 9 | 9 | +5.83% | +5.96% | +100.00% | 24.57 | 0.0000 | 23.17 | 0.0000 | 1,627 | +5.63% | +2.44% | 18.18 | 3,070 |
| SPY-IC | pooled | 6 | 6 | +7.69% | +7.80% | +100.00% | 18.61 | 0.0000 | 20.91 | 0.0000 | 1,463 | +7.37% | +3.44% | 18.79 | 3,148 |
| QQQ-PS | pooled | 8 | 8 | +7.02% | +6.86% | +100.00% | 34.01 | 0.0000 | 21.12 | 0.0000 | 2,336 | +6.72% | +2.60% | 26.51 | 4,163 |
| QQQ-IC | pooled | 4 | 4 | +9.59% | +9.78% | +100.00% | 22.69 | 0.0002 | 13.01 | 0.0010 | 1,681 | +8.98% | +2.98% | 26.59 | 4,367 |


## Marked vs proxy on the same positions (§6.7 criterion 2)

| sleeve | n_marked | n_overlap | marked_mean_ror | proxy_mean_ror | gap_ror | marked_cost_ror | overlap_pass |
|---|---|---|---|---|---|---|---|
| SPY-PS | 9 | 9 | +5.83% | +5.70% | -0.13% | +0.14% | yes |
| SPY-IC | 6 | 6 | +7.69% | +8.07% | +0.38% | +0.27% | no |
| QQQ-PS | 8 | 8 | +7.02% | +6.39% | -0.63% | +0.19% | yes |
| QQQ-IC | 4 | 4 | +9.59% | +10.76% | +1.18% | +0.30% | no |


## Marked: tiers, credit, width, cost

| underlying | structure | n | graded | entry_tier_max | mean_credit | mean_width | mean_cost_over_credit |
|---|---|---|---|---|---|---|---|
| QQQ | IC | 6 | 4 | 1 | 4.01 | 46.17 | +2.98% |
| QQQ | PS | 10 | 8 | 1 | 2.79 | 43.10 | +2.60% |
| SPY | IC | 8 | 6 | 1 | 2.38 | 32.25 | +3.44% |
| SPY | PS | 11 | 9 | 1 | 1.75 | 31.45 | +2.44% |


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
| base | SPY-PS | 9 | +5.83% | 24.57 | 1,627 |
| base | SPY-IC | 6 | +7.69% | 18.61 | 1,463 |
| base | QQQ-PS | 8 | +7.02% | 34.01 | 2,336 |
| base | QQQ-IC | 4 | +9.59% | 22.69 | 1,681 |
| gate_off | SPY-PS | 22 | +5.66% | 32.05 | 3,721 |
| gate_off | SPY-IC | 18 | +3.92% | 1.16 | 1,255 |
| gate_off | QQQ-PS | 22 | +6.59% | 29.80 | 5,756 |
| gate_off | QQQ-IC | 17 | +2.47% | 0.3870 | 1,782 |
| band_0.15 | SPY-PS | 9 | +5.83% | 24.57 | 1,627 |
| band_0.15 | SPY-IC | 6 | +7.69% | 18.61 | 1,463 |
| band_0.15 | QQQ-PS | 6 | +7.39% | 46.63 | 1,896 |
| band_0.15 | QQQ-IC | 2 | — | — | 940.20 |
| wing_1.5 | SPY-PS | 9 | +7.81% | 26.07 | 1,715 |
| wing_1.5 | SPY-IC | 9 | +6.61% | 1.83 | 1,464 |
| wing_1.5 | QQQ-PS | 8 | +9.68% | 36.39 | 1,579 |
| wing_1.5 | QQQ-IC | 8 | +16.37% | 35.22 | 2,535 |


## Go / no-go (DESIGN/80 §6.7; t >= 2.0; read 2026-12-01)

| sleeve | n_proxy | mean_proxy | nw_t_proxy | bh_pass | mean_p1 | mean_p2 | mean_p3 | n_marked | mean_marked | gap_ror | worst_over_median | deflated_sr | deflated_sr_null | forward_n | c1_proxy | c2_marked | c3_month | c4_dsr | c4_dsr_null | c5_scale | verdict | note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 60 | +4.14% | 3.75 | yes | +1.98% | +5.14% | +5.16% | 9 | +5.83% | -0.13% | 1.64 | 0.3348 | 0.2971 | 0 | yes | yes | yes | yes | yes | no | GO-MIN | clears 1-4; one contract until the forward ledger holds >= 40 graded positions (now 0) |
| SPY-IC | 60 | +4.42% | 3.19 | yes | -0.90% | +6.80% | +6.93% | 6 | +7.69% | +0.38% | 6.12 | 0.2779 | 0.2402 | 0 | no | no | no | yes | yes | no | NO-GO | fails c1_proxy, c2_marked, c3_month |
| QQQ-PS | 58 | +4.32% | 2.38 | yes | +0.63% | +6.19% | +6.30% | 8 | +7.02% | -0.63% | 4.88 | 0.1760 | 0.1383 | 0 | yes | yes | no | yes | yes | no | NO-GO | fails c3_month |
| QQQ-IC | 58 | +4.71% | 1.71 | yes | -3.81% | +7.55% | +10.17% | 4 | +9.59% | +1.18% | 3.85 | 0.1061 | 0.0684 | 0 | no | no | no | yes | yes | no | NO-GO | fails c1_proxy, c2_marked, c3_month |


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
