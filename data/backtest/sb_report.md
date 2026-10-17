# S-B backtest report (generated)


## Inputs

- refreshed: {'index_vol_through': '2026-10-16', 'prices_through': '2026-10-16'}
- proxy: {'index_vol': ['1990-01-02', '2026-10-16'], 'sessions': ['2023-10-17', '2026-10-16'], 'n_sessions': 753}
- marked: {'panel': ['2026-03-13', '2026-10-16'], 'n_entry_sessions': 32}


## Gate ON share of entry sessions (proxy, by year)

| underlying | year | entry_sessions | gate_on | on_share |
|---|---|---|---|---|
| QQQ | 2023 | 7 | 1 | +14.29% |
| QQQ | 2024 | 52 | 26 | +50.00% |
| QQQ | 2025 | 52 | 15 | +28.85% |
| QQQ | 2026 | 39 | 17 | +43.59% |
| QQQ | all | 150 | 59 | +39.33% |
| SPY | 2023 | 7 | 1 | +14.29% |
| SPY | 2024 | 52 | 25 | +48.08% |
| SPY | 2025 | 52 | 16 | +30.77% |
| SPY | 2026 | 39 | 19 | +48.72% |
| SPY | all | 150 | 61 | +40.67% |


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
| SPY-PS | P3 | 28 | 28 | +5.18% | +5.70% | +96.43% | 10.89 | 0.0000 | 9.86 | 0.0000 | 4,102 | +5.53% | +2.57% | 17.98 | 2,837 |
| SPY-IC | P3 | 28 | 28 | +6.96% | +8.00% | +92.86% | 10.87 | 0.0000 | 9.60 | 0.0000 | 5,374 | +7.67% | +3.56% | 17.98 | 2,779 |
| QQQ-PS | P3 | 25 | 25 | +6.29% | +6.33% | +100.00% | 154.81 | 0.0000 | 192.02 | 0.0000 | 5,435 | +6.04% | +2.16% | 23.79 | 3,442 |
| QQQ-IC | P3 | 25 | 25 | +10.18% | +10.70% | +96.00% | 21.69 | 0.0000 | 20.55 | 0.0000 | 8,492 | +9.87% | +2.35% | 23.79 | 3,323 |
| SPY-PS | pooled | 61 | 61 | +4.17% | +5.63% | +95.08% | 3.83 | 0.0003 | 3.71 | 0.0005 | 6,923 | +5.48% | +2.97% | 17.19 | 2,485 |
| SPY-IC | pooled | 61 | 61 | +4.48% | +7.91% | +86.89% | 3.27 | 0.0018 | 3.28 | 0.0018 | 6,466 | +7.63% | +4.10% | 17.19 | 2,534 |
| QQQ-PS | pooled | 59 | 59 | +4.35% | +6.20% | +98.31% | 2.44 | 0.0177 | 2.41 | 0.0191 | 7,834 | +5.98% | +2.63% | 21.70 | 2,691 |
| QQQ-IC | pooled | 59 | 59 | +4.81% | +10.51% | +89.83% | 1.78 | 0.0811 | 1.89 | 0.0637 | 9,051 | +9.82% | +2.89% | 21.70 | 2,647 |


## BH(0.10) across the four sleeves (proxy, pooled, on the NW p)

| sleeve | n | mean_ror | nw_t | nw_p | bh_pass |
|---|---|---|---|---|---|
| SPY-PS | 61 | +4.17% | 3.83 | 0.0003 | yes |
| SPY-IC | 61 | +4.48% | 3.27 | 0.0018 | yes |
| QQQ-PS | 59 | +4.35% | 2.44 | 0.0177 | yes |
| QQQ-IC | 59 | +4.81% | 1.78 | 0.0811 | yes |


## Deflated Sharpe (6 trials) — proxy pooled

| sleeve | n | sr | sr_star | deflated_sr | dsr_prob | sr_star_null | deflated_sr_null | dsr_prob_null | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 61 | 0.4745 | 0.1336 | 0.3409 | 0.8313 | 0.1693 | 0.3052 | 0.8049 | -7.21 | 56.98 |
| SPY-IC | 61 | 0.4194 | 0.1336 | 0.2858 | 0.8655 | 0.1693 | 0.2502 | 0.8333 | -4.48 | 26.80 |
| QQQ-PS | 59 | 0.3139 | 0.1336 | 0.1803 | 0.7322 | 0.1693 | 0.1446 | 0.6905 | -7.67 | 61.91 |
| QQQ-IC | 59 | 0.2461 | 0.1336 | 0.1124 | 0.7174 | 0.1693 | 0.0768 | 0.6528 | -3.89 | 18.22 |


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
| SPY-PS | 28 | 1.86 | 23.32 | -21.46 | 0.0000 | 0.2600 | 1.60 | 0.9157 | -5.26 | 30.76 |
| SPY-IC | 28 | 1.81 | 23.32 | -21.51 | 0.0000 | 0.2600 | 1.55 | 0.9708 | -3.51 | 14.17 |
| QQQ-PS | 25 | 38.40 | 23.32 | 15.08 | 0.9988 | 0.2600 | 38.14 | 1.0000 | -0.3569 | 2.58 |
| QQQ-IC | 25 | 4.11 | 23.32 | -19.21 | 0.0000 | 0.2600 | 3.85 | 0.9484 | -4.95 | 27.68 |


## PBO (CSCV over 16 entry blocks, proxy pooled)

- pbo: 0.6830613830613831
- mean_logit: -0.1941763124485397
- n_combinations: 12870
- n_configs: 4
- n_blocks: 16
- n_entries: 65


## Month rule (proxy; worst expiry-month vs median month, $ at frozen sizing)

| sleeve | n_months | median_month_usd | worst_month | worst_month_usd | worst_over_median | months_negative | month_rule_pass |
|---|---|---|---|---|---|---|---|
| SPY-PS | 28 | 245.68 | 2024-08 | -396.47 | 1.61 | 2 | yes |
| SPY-IC | 28 | 264.47 | 2024-08 | -1,537 | 5.81 | 4 | no |
| QQQ-PS | 28 | 286.14 | 2024-08 | -1,325 | 4.63 | 1 | no |
| QQQ-IC | 28 | 437.84 | 2024-01 | -1,574 | 3.59 | 4 | no |


## Tail report (proxy, pooled)

| sleeve | n | mean_ror | worst_ror | worst_entry | best_ror | mean_win_ror | worst_decile_share_of_loss | full_width_losses | mean_without_worst_1pct | mean_without_best_1pct | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 61 | +4.17% | -61.38% | 2024-07-12 | +6.12% | +5.63% | 1.00 | 0 | +5.26% | +4.14% | -7.21 | 53.98 |
| SPY-IC | 61 | +4.48% | -60.67% | 2024-07-12 | +8.42% | +7.72% | 0.9463 | 0 | +5.56% | +4.41% | -4.48 | 23.80 |
| QQQ-PS | 59 | +4.35% | -100.20% | 2024-07-12 | +6.60% | +6.15% | 1.00 | 1 | +6.15% | +4.31% | -7.67 | 58.91 |
| QQQ-IC | 59 | +4.81% | -95.11% | 2024-07-12 | +11.01% | +10.36% | 0.9937 | 0 | +6.54% | +4.71% | -3.89 | 15.22 |

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
| base | SPY-PS | 61 | +4.17% | 3.83 | 3.71 | 6,923 | +2.97% |
| base | SPY-IC | 61 | +4.48% | 3.27 | 3.28 | 6,466 | +4.10% |
| base | QQQ-PS | 59 | +4.35% | 2.44 | 2.41 | 7,834 | +2.63% |
| base | QQQ-IC | 59 | +4.81% | 1.78 | 1.89 | 9,051 | +2.89% |
| gate_off | SPY-PS | 150 | +3.23% | 2.93 | 3.26 | 13,340 | +3.02% |
| gate_off | SPY-IC | 150 | +3.02% | 2.20 | 2.53 | 9,983 | +4.17% |
| gate_off | QQQ-PS | 150 | +2.75% | 1.67 | 1.99 | 13,421 | +2.67% |
| gate_off | QQQ-IC | 150 | +0.72% | 0.2850 | 0.3607 | 2,848 | +2.94% |
| g1_only | SPY-PS | 139 | +3.74% | 4.08 | 4.70 | 13,708 | +3.09% |
| g1_only | SPY-IC | 139 | +4.09% | 3.65 | 4.23 | 13,630 | +4.27% |
| g1_only | QQQ-PS | 139 | +3.15% | 1.91 | 2.39 | 13,745 | +2.72% |
| g1_only | QQQ-IC | 139 | +2.24% | 0.9245 | 1.18 | 9,480 | +2.99% |
| g2_only | SPY-PS | 71 | +3.00% | 1.81 | 1.76 | 6,368 | +2.84% |
| g2_only | SPY-IC | 71 | +2.63% | 1.40 | 1.32 | 3,684 | +3.94% |
| g2_only | QQQ-PS | 69 | +3.24% | 1.62 | 1.57 | 7,323 | +2.55% |
| g2_only | QQQ-IC | 69 | +1.85% | 0.6148 | 0.6239 | 3,765 | +2.81% |
| costs_x2 | SPY-PS | 61 | +4.00% | 3.67 | 3.55 | 6,672 | +5.94% |
| costs_x2 | SPY-IC | 61 | +4.14% | 3.01 | 3.02 | 5,953 | +8.20% |
| costs_x2 | QQQ-PS | 59 | +4.18% | 2.35 | 2.32 | 7,585 | +5.26% |
| costs_x2 | QQQ-IC | 59 | +4.50% | 1.66 | 1.76 | 8,586 | +5.79% |
| wing_1.5 | SPY-PS | 61 | -0.56% | -0.3318 | -0.3203 | -629.43 | +19.39% |
| wing_1.5 | SPY-IC | 61 | -1.75% | -0.7633 | -0.7678 | -2,105 | +16.94% |
| wing_1.5 | QQQ-PS | 59 | +1.12% | 0.6372 | 0.6368 | 974.81 | +11.97% |
| wing_1.5 | QQQ-IC | 59 | +0.66% | 0.1828 | 0.1944 | 301.77 | +7.35% |


## Other structures on the proxy (descriptive; not sleeves, never a verdict input)

Single legs, naked shorts and the call spread re-priced on the same entry rows with the frozen smile and costs. Risk: debit = premium; credit spread = width - credit; naked = the 2-sigma stress loss (the matching spread's max loss), Reg-T proxy margin beside. `PS` here is the champion recomputed as a check. Drafts: `ledger/challengers/drafts/sb-c-callspread.json`, `sb-c-nakedput-margin.json`.

| set | structure | underlying | n | mean_ror | nw_t | hit | mean_pnl_usd | worst_ror | mean_premium_usd | mean_margin_usd | total_pnl_usd |
|---|---|---|---|---|---|---|---|---|---|---|---|
| gate ON | long_c1 | QQQ | 59 | -17.79% | -0.4450 | +8.47% | -47.05 | -102.60% | 119.10 | — | -2,776 |
| gate ON | long_p1 | QQQ | 59 | -76.09% | -3.17 | +1.69% | -212.35 | -101.38% | 254.03 | — | -12,529 |
| gate ON | long_c2 | QQQ | 59 | -120.51% | -96.96 | +0.00% | -9.04 | -134.00% | 7.62 | — | -533.47 |
| gate ON | long_p2 | QQQ | 59 | -88.01% | -6.30 | +1.69% | -74.78 | -103.38% | 81.84 | — | -4,412 |
| gate ON | short_p1_naked | QQQ | 59 | +7.02% | 3.14 | +98.31% | 207.57 | -124.66% | -254.03 | 7,739 | 12,247 |
| gate ON | short_c1_naked | QQQ | 59 | +0.58% | 0.3295 | +91.53% | 43.01 | -66.02% | -119.10 | 7,873 | 2,537 |
| gate ON | CS | QQQ | 59 | +0.25% | 0.1401 | +89.83% | 33.97 | -66.40% | -111.47 | — | 2,004 |
| gate ON | PS | QQQ | 59 | +4.35% | 2.44 | +98.31% | 132.79 | -100.20% | -172.19 | — | 7,834 |
| gate ON | long_c1 | SPY | 61 | -25.96% | -0.7131 | +11.48% | -22.90 | -104.68% | 59.38 | — | -1,397 |
| gate ON | long_p1 | SPY | 61 | -84.93% | -7.14 | +3.28% | -193.99 | -101.40% | 218.99 | — | -11,833 |
| gate ON | long_c2 | SPY | 61 | -147.95% | -70.80 | +0.00% | -5.52 | -173.85% | 3.80 | — | -336.61 |
| gate ON | long_p2 | SPY | 61 | -102.42% | -1,118 | +0.00% | -80.02 | -103.47% | 78.21 | — | -4,881 |
| gate ON | short_p1_naked | SPY | 61 | +7.51% | 6.95 | +96.72% | 189.72 | -57.60% | -218.99 | 9,558 | 11,573 |
| gate ON | short_c1_naked | SPY | 61 | +0.46% | 0.5305 | +88.52% | 18.96 | -27.78% | -59.38 | 9,722 | 1,157 |
| gate ON | CS | SPY | 61 | +0.24% | 0.2721 | +88.52% | 13.45 | -28.03% | -55.58 | — | 820.22 |
| gate ON | PS | SPY | 61 | +4.17% | 3.83 | +95.08% | 109.70 | -61.38% | -140.78 | — | 6,692 |
| every Friday | long_c1 | QQQ | 150 | +35.42% | 0.7680 | +15.33% | 50.73 | -102.60% | 117.43 | — | 7,609 |
| every Friday | long_p1 | QQQ | 150 | -62.62% | -3.35 | +5.33% | -170.60 | -101.46% | 249.39 | — | -25,590 |
| every Friday | long_c2 | QQQ | 150 | -121.02% | -139.91 | +0.00% | -8.91 | -139.37% | 7.49 | — | -1,337 |
| every Friday | long_p2 | QQQ | 150 | -96.56% | -17.29 | +0.67% | -78.57 | -103.68% | 80.38 | — | -11,785 |
| every Friday | short_p1_naked | QQQ | 150 | +5.70% | 3.24 | +94.67% | 165.86 | -124.66% | -249.39 | 7,795 | 24,878 |
| every Friday | short_c1_naked | QQQ | 150 | -1.70% | -0.8506 | +84.67% | -54.75 | -90.15% | -117.43 | 7,929 | -8,212 |
| every Friday | CS | QQQ | 150 | -2.03% | -1.02 | +83.33% | -63.66 | -90.50% | -109.94 | — | -9,549 |
| every Friday | PS | QQQ | 150 | +2.75% | 1.67 | +94.67% | 87.29 | -100.20% | -169.01 | — | 13,094 |
| every Friday | long_c1 | SPY | 150 | -5.65% | -0.1499 | +11.33% | 5.62 | -105.35% | 58.73 | — | 843.74 |
| every Friday | long_p1 | SPY | 150 | -74.51% | -6.09 | +4.67% | -165.75 | -101.52% | 216.74 | — | -24,862 |
| every Friday | long_c2 | SPY | 150 | -149.46% | -90.11 | +0.00% | -5.49 | -188.16% | 3.77 | — | -823.03 |
| every Friday | long_p2 | SPY | 150 | -102.46% | -1,519 | +0.00% | -78.96 | -103.74% | 77.15 | — | -11,843 |
| every Friday | short_p1_naked | SPY | 150 | +6.57% | 5.94 | +95.33% | 161.50 | -92.22% | -216.74 | 9,478 | 24,225 |
| every Friday | short_c1_naked | SPY | 150 | -0.02% | -0.0270 | +88.00% | -9.55 | -59.74% | -58.73 | 9,636 | -1,432 |
| every Friday | CS | SPY | 150 | -0.25% | -0.2792 | +88.00% | -15.03 | -59.95% | -54.97 | — | -2,255 |
| every Friday | PS | SPY | 150 | +3.23% | 2.93 | +94.67% | 82.54 | -95.48% | -139.59 | — | 12,382 |


## Marked (panel): sleeve table

| sleeve | window | n | expiries | mean_ror | median_ror | hit | nw_t | nw_p | cl_t | cl_p | net_usd_total | mean_credit_over_width | mean_cost_over_credit | mean_x | mean_risk_usd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | P3 | 10 | 10 | +5.75% | +5.74% | +100.00% | 23.66 | 0.0000 | 23.91 | 0.0000 | 1,755 | +5.56% | +2.54% | 17.85 | 3,020 |
| SPY-IC | P3 | 7 | 7 | +7.73% | +7.97% | +100.00% | 22.80 | 0.0000 | 24.67 | 0.0000 | 1,662 | +7.41% | +3.52% | 18.23 | 3,054 |
| QQQ-PS | P3 | 9 | 9 | +6.84% | +6.76% | +100.00% | 22.27 | 0.0000 | 19.85 | 0.0000 | 2,525 | +6.55% | +2.55% | 25.89 | 4,090 |
| QQQ-IC | P3 | 5 | 5 | +9.42% | +9.17% | +100.00% | 22.15 | 0.0000 | 15.88 | 0.0001 | 2,043 | +8.83% | +2.85% | 25.45 | 4,319 |
| SPY-PS | pooled | 10 | 10 | +5.75% | +5.74% | +100.00% | 23.66 | 0.0000 | 23.91 | 0.0000 | 1,755 | +5.56% | +2.54% | 17.85 | 3,020 |
| SPY-IC | pooled | 7 | 7 | +7.73% | +7.97% | +100.00% | 22.80 | 0.0000 | 24.67 | 0.0000 | 1,662 | +7.41% | +3.52% | 18.23 | 3,054 |
| QQQ-PS | pooled | 9 | 9 | +6.84% | +6.76% | +100.00% | 22.27 | 0.0000 | 19.85 | 0.0000 | 2,525 | +6.55% | +2.55% | 25.89 | 4,090 |
| QQQ-IC | pooled | 5 | 5 | +9.42% | +9.17% | +100.00% | 22.15 | 0.0000 | 15.88 | 0.0001 | 2,043 | +8.83% | +2.85% | 25.45 | 4,319 |


## Marked vs proxy on the same positions (§6.7 criterion 2)

| sleeve | n_marked | n_overlap | marked_mean_ror | proxy_mean_ror | gap_ror | marked_cost_ror | overlap_pass |
|---|---|---|---|---|---|---|---|
| SPY-PS | 10 | 10 | +5.75% | +5.69% | -0.05% | +0.15% | yes |
| SPY-IC | 7 | 7 | +7.73% | +8.05% | +0.32% | +0.28% | no |
| QQQ-PS | 9 | 9 | +6.84% | +6.36% | -0.47% | +0.18% | yes |
| QQQ-IC | 5 | 5 | +9.42% | +10.73% | +1.30% | +0.28% | no |


## Marked: tiers, credit, width, cost

| underlying | structure | n | graded | entry_tier_max | mean_credit | mean_width | mean_cost_over_credit |
|---|---|---|---|---|---|---|---|
| QQQ | IC | 7 | 5 | 1 | 4.07 | 46.71 | +2.85% |
| QQQ | PS | 12 | 9 | 1 | 2.76 | 43.33 | +2.55% |
| SPY | IC | 8 | 7 | 1 | 2.38 | 32.25 | +3.52% |
| SPY | PS | 12 | 10 | 1 | 1.74 | 31.92 | +2.54% |


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
| SPY | IC | no_tier1_c2 | 4 |
| SPY | PS | OFF:G1 | 1 |
| SPY | PS | OFF:G2 | 18 |


## Marked sensitivities (descriptive)

| sensitivity | sleeve | n | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|
| base | SPY-PS | 10 | +5.75% | 23.66 | 1,755 |
| base | SPY-IC | 7 | +7.73% | 22.80 | 1,662 |
| base | QQQ-PS | 9 | +6.84% | 22.27 | 2,525 |
| base | QQQ-IC | 5 | +9.42% | 22.15 | 2,043 |
| gate_off | SPY-PS | 24 | +5.62% | 33.40 | 3,973 |
| gate_off | SPY-IC | 20 | +4.22% | 1.38 | 1,625 |
| gate_off | QQQ-PS | 24 | +6.55% | 31.48 | 6,158 |
| gate_off | QQQ-IC | 18 | +2.82% | 0.4661 | 2,144 |
| band_0.15 | SPY-PS | 10 | +5.75% | 23.66 | 1,755 |
| band_0.15 | SPY-IC | 7 | +7.73% | 22.80 | 1,662 |
| band_0.15 | QQQ-PS | 7 | +7.10% | 28.50 | 2,085 |
| band_0.15 | QQQ-IC | 2 | — | — | 940.20 |
| wing_1.5 | SPY-PS | 10 | +7.72% | 25.30 | 1,895 |
| wing_1.5 | SPY-IC | 10 | +7.02% | 2.11 | 1,771 |
| wing_1.5 | QQQ-PS | 9 | +9.43% | 24.79 | 1,704 |
| wing_1.5 | QQQ-IC | 9 | +16.26% | 33.65 | 2,801 |


## Go / no-go (DESIGN/80 §6.7; t >= 2.0; read 2026-12-01)

| sleeve | n_proxy | mean_proxy | nw_t_proxy | bh_pass | mean_p1 | mean_p2 | mean_p3 | n_marked | mean_marked | gap_ror | worst_over_median | deflated_sr | deflated_sr_null | forward_n | c1_proxy | c2_marked | c3_month | c4_dsr | c4_dsr_null | c5_scale | verdict | note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 61 | +4.17% | 3.83 | yes | +1.98% | +5.14% | +5.18% | 10 | +5.75% | -0.05% | 1.61 | 0.3409 | 0.3052 | 2 | yes | yes | yes | yes | yes | no | GO-MIN | clears 1-4; one contract until the forward ledger holds >= 40 graded positions (now 2) |
| SPY-IC | 61 | +4.48% | 3.27 | yes | -0.90% | +6.80% | +6.96% | 7 | +7.73% | +0.32% | 5.81 | 0.2858 | 0.2502 | 1 | no | no | no | yes | yes | no | NO-GO | fails c1_proxy, c2_marked, c3_month |
| QQQ-PS | 59 | +4.35% | 2.44 | yes | +0.63% | +6.19% | +6.29% | 9 | +6.84% | -0.47% | 4.63 | 0.1803 | 0.1446 | 2 | yes | yes | no | yes | yes | no | NO-GO | fails c3_month |
| QQQ-IC | 59 | +4.81% | 1.78 | yes | -3.81% | +7.55% | +10.18% | 5 | +9.42% | +1.30% | 3.59 | 0.1124 | 0.0768 | 2 | no | no | no | yes | yes | no | NO-GO | fails c1_proxy, c2_marked, c3_month |


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
