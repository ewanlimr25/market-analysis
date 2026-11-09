# S-B backtest report (generated)


## Inputs

- refreshed: {'index_vol_through': '2026-11-06', 'prices_through': '2026-11-06'}
- proxy: {'index_vol': ['1990-01-02', '2026-11-06'], 'sessions': ['2023-11-07', '2026-11-06'], 'n_sessions': 753}
- marked: {'panel': ['2026-03-13', '2026-11-06'], 'n_entry_sessions': 35}


## Gate ON share of entry sessions (proxy, by year)

| underlying | year | entry_sessions | gate_on | on_share |
|---|---|---|---|---|
| QQQ | 2023 | 4 | 1 | +25.00% |
| QQQ | 2024 | 52 | 26 | +50.00% |
| QQQ | 2025 | 52 | 15 | +28.85% |
| QQQ | 2026 | 42 | 20 | +47.62% |
| QQQ | all | 150 | 62 | +41.33% |
| SPY | 2023 | 4 | 1 | +25.00% |
| SPY | 2024 | 52 | 25 | +48.08% |
| SPY | 2025 | 52 | 16 | +30.77% |
| SPY | 2026 | 42 | 21 | +50.00% |
| SPY | all | 150 | 63 | +42.00% |


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
| SPY-PS | P3 | 30 | 30 | +5.21% | +5.70% | +96.67% | 11.70 | 0.0000 | 10.63 | 0.0000 | 4,453 | +5.52% | +2.56% | 17.96 | 2,853 |
| SPY-IC | P3 | 30 | 30 | +7.03% | +8.00% | +93.33% | 11.66 | 0.0000 | 10.37 | 0.0000 | 5,856 | +7.67% | +3.54% | 17.96 | 2,794 |
| QQQ-PS | P3 | 28 | 28 | +2.58% | +6.30% | +89.29% | 0.8139 | 0.4228 | 1.02 | 0.3183 | 2,352 | +6.04% | +2.15% | 23.70 | 3,483 |
| QQQ-IC | P3 | 28 | 28 | +6.37% | +10.60% | +85.71% | 1.95 | 0.0622 | 2.40 | 0.0235 | 5,870 | +9.87% | +2.33% | 23.70 | 3,360 |
| SPY-PS | pooled | 63 | 63 | +4.22% | +5.63% | +95.24% | 4.00 | 0.0002 | 3.87 | 0.0003 | 7,274 | +5.48% | +2.95% | 17.20 | 2,503 |
| SPY-IC | pooled | 63 | 63 | +4.59% | +7.91% | +87.30% | 3.45 | 0.0010 | 3.46 | 0.0010 | 6,948 | +7.63% | +4.08% | 17.20 | 2,549 |
| QQQ-PS | pooled | 62 | 62 | +2.76% | +6.19% | +93.55% | 1.26 | 0.2115 | 1.35 | 0.1816 | 4,752 | +5.98% | +2.60% | 21.76 | 2,745 |
| QQQ-IC | pooled | 62 | 62 | +3.35% | +10.48% | +85.48% | 1.16 | 0.2489 | 1.26 | 0.2112 | 6,429 | +9.82% | +2.86% | 21.76 | 2,696 |


## BH(0.10) across the four sleeves (proxy, pooled, on the NW p)

| sleeve | n | mean_ror | nw_t | nw_p | bh_pass |
|---|---|---|---|---|---|
| SPY-PS | 63 | +4.22% | 4.00 | 0.0002 | yes |
| SPY-IC | 63 | +4.59% | 3.45 | 0.0010 | yes |
| QQQ-PS | 62 | +2.76% | 1.26 | 0.2115 | no |
| QQQ-IC | 62 | +3.35% | 1.16 | 0.2489 | no |


## Deflated Sharpe (6 trials) — proxy pooled

| sleeve | n | sr | sr_star | deflated_sr | dsr_prob | sr_star_null | deflated_sr_null | dsr_prob_null | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 63 | 0.4877 | 0.2239 | 0.2638 | 0.7685 | 0.1651 | 0.3226 | 0.8153 | -7.33 | 58.75 |
| SPY-IC | 63 | 0.4362 | 0.2239 | 0.2124 | 0.7913 | 0.1651 | 0.2711 | 0.8497 | -4.55 | 27.63 |
| QQQ-PS | 62 | 0.1716 | 0.2239 | -0.0523 | 0.3914 | 0.1651 | 0.0065 | 0.5137 | -5.51 | 34.65 |
| QQQ-IC | 62 | 0.1605 | 0.2239 | -0.0634 | 0.3485 | 0.1651 | -0.0046 | 0.4886 | -3.33 | 13.90 |


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
| SPY-PS | 30 | 1.94 | 1.20 | 0.7361 | 0.7310 | 0.2457 | 1.70 | 0.9220 | -5.44 | 32.70 |
| SPY-IC | 30 | 1.89 | 1.20 | 0.6882 | 0.7928 | 0.2457 | 1.65 | 0.9746 | -3.65 | 15.18 |
| QQQ-PS | 28 | 0.1921 | 1.20 | -1.01 | 0.0001 | 0.2457 | -0.0536 | 0.4231 | -4.41 | 23.71 |
| QQQ-IC | 28 | 0.4537 | 1.20 | -0.7512 | 0.0261 | 0.2457 | 0.2080 | 0.7046 | -4.25 | 22.62 |


## PBO (CSCV over 16 entry blocks, proxy pooled)

- pbo: 0.3111111111111111
- mean_logit: 0.3812737614519031
- n_combinations: 12870
- n_configs: 4
- n_blocks: 16
- n_entries: 68


## Month rule (proxy; worst expiry-month vs median month, $ at frozen sizing)

| sleeve | n_months | median_month_usd | worst_month | worst_month_usd | worst_over_median | months_negative | month_rule_pass |
|---|---|---|---|---|---|---|---|
| SPY-PS | 29 | 241.76 | 2024-08 | -396.47 | 1.64 | 2 | yes |
| SPY-IC | 29 | 266.06 | 2024-08 | -1,537 | 5.78 | 4 | no |
| QQQ-PS | 29 | 258.31 | 2026-10 | -2,153 | 8.33 | 3 | no |
| QQQ-IC | 29 | 397.25 | 2026-10 | -1,592 | 4.01 | 6 | no |


## Tail report (proxy, pooled)

| sleeve | n | mean_ror | worst_ror | worst_entry | best_ror | mean_win_ror | worst_decile_share_of_loss | full_width_losses | mean_without_worst_1pct | mean_without_best_1pct | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 63 | +4.22% | -61.38% | 2024-07-12 | +6.12% | +5.63% | 1.00 | 0 | +5.28% | +4.19% | -7.33 | 55.75 |
| SPY-IC | 63 | +4.59% | -60.67% | 2024-07-12 | +8.42% | +7.73% | 0.9463 | 0 | +5.64% | +4.53% | -4.55 | 24.63 |
| QQQ-PS | 62 | +2.76% | -100.20% | 2024-07-12 | +6.60% | +6.15% | 1.00 | 1 | +4.45% | +2.70% | -5.51 | 31.65 |
| QQQ-IC | 62 | +3.35% | -95.11% | 2024-07-12 | +11.01% | +10.36% | 0.9467 | 0 | +4.96% | +3.22% | -3.33 | 10.90 |

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
| 2026-10-16 | 2026-11-06 | 27.13 | -11.42% | -503.48 |
| 2024-07-19 | 2024-08-09 | 21.51 | +3.83% | 89.96 |
| 2024-01-26 | 2024-02-16 | 17.03 | +5.66% | 90.87 |
| 2024-01-05 | 2024-01-26 | 17.13 | +5.67% | 85.64 |
| 2024-02-02 | 2024-02-23 | 17.22 | +5.80% | 93.02 |
| 2024-03-08 | 2024-03-28 | 19.04 | +5.83% | 104.43 |
| 2025-02-28 | 2025-03-21 | 22.66 | +5.85% | 153.54 |


## Gate modes and sensitivities (proxy, pooled; descriptive)

| sensitivity | sleeve | n | mean_ror | nw_t | cl_t | net_usd_total | mean_cost_over_credit |
|---|---|---|---|---|---|---|---|
| base | SPY-PS | 63 | +4.22% | 4.00 | 3.87 | 7,274 | +2.95% |
| base | SPY-IC | 63 | +4.59% | 3.45 | 3.46 | 6,948 | +4.08% |
| base | QQQ-PS | 62 | +2.76% | 1.26 | 1.35 | 4,752 | +2.60% |
| base | QQQ-IC | 62 | +3.35% | 1.16 | 1.26 | 6,429 | +2.86% |
| gate_off | SPY-PS | 150 | +3.24% | 2.93 | 3.26 | 13,398 | +2.98% |
| gate_off | SPY-IC | 150 | +3.08% | 2.23 | 2.57 | 10,259 | +4.12% |
| gate_off | QQQ-PS | 150 | +2.06% | 1.19 | 1.42 | 9,916 | +2.64% |
| gate_off | QQQ-IC | 150 | +0.19% | 0.0740 | 0.0933 | 110.29 | +2.89% |
| g1_only | SPY-PS | 139 | +3.75% | 4.09 | 4.70 | 13,766 | +3.05% |
| g1_only | SPY-IC | 139 | +4.15% | 3.70 | 4.29 | 13,906 | +4.21% |
| g1_only | QQQ-PS | 139 | +2.41% | 1.37 | 1.71 | 10,240 | +2.68% |
| g1_only | QQQ-IC | 139 | +1.67% | 0.6732 | 0.8563 | 6,742 | +2.94% |
| g2_only | SPY-PS | 73 | +3.07% | 1.90 | 1.85 | 6,719 | +2.83% |
| g2_only | SPY-IC | 73 | +2.78% | 1.52 | 1.43 | 4,166 | +3.92% |
| g2_only | QQQ-PS | 72 | +1.93% | 0.8591 | 0.8773 | 4,240 | +2.53% |
| g2_only | QQQ-IC | 72 | +0.71% | 0.2337 | 0.2395 | 1,142 | +2.78% |
| costs_x2 | SPY-PS | 63 | +4.05% | 3.83 | 3.71 | 7,015 | +5.90% |
| costs_x2 | SPY-IC | 63 | +4.25% | 3.18 | 3.20 | 6,418 | +8.15% |
| costs_x2 | QQQ-PS | 62 | +2.60% | 1.19 | 1.27 | 4,487 | +5.20% |
| costs_x2 | QQQ-IC | 62 | +3.04% | 1.05 | 1.15 | 5,937 | +5.72% |
| wing_1.5 | SPY-PS | 63 | -0.48% | -0.2906 | -0.2810 | -538.16 | +19.23% |
| wing_1.5 | SPY-IC | 63 | -1.55% | -0.6924 | -0.6993 | -1,900 | +16.86% |
| wing_1.5 | QQQ-PS | 62 | -1.61% | -0.5578 | -0.6566 | -2,098 | +11.85% |
| wing_1.5 | QQQ-IC | 62 | -1.82% | -0.4489 | -0.4981 | -2,432 | +7.28% |


## Other structures on the proxy (descriptive; not sleeves, never a verdict input)

Single legs, naked shorts and the call spread re-priced on the same entry rows with the frozen smile and costs. Risk: debit = premium; credit spread = width - credit; naked = the 2-sigma stress loss (the matching spread's max loss), Reg-T proxy margin beside. `PS` here is the champion recomputed as a check. Drafts: `ledger/challengers/drafts/sb-c-callspread.json`, `sb-c-nakedput-margin.json`.

| set | structure | underlying | n | mean_ror | nw_t | hit | mean_pnl_usd | worst_ror | mean_premium_usd | mean_margin_usd | total_pnl_usd |
|---|---|---|---|---|---|---|---|---|---|---|---|
| gate ON | long_c1 | QQQ | 62 | -21.83% | -0.5711 | +8.06% | -53.01 | -102.60% | 121.46 | — | -3,287 |
| gate ON | long_p1 | QQQ | 62 | -59.33% | -2.19 | +6.45% | -158.19 | -101.38% | 259.02 | — | -9,808 |
| gate ON | long_c2 | QQQ | 62 | -120.18% | -98.54 | +0.00% | -9.20 | -134.00% | 7.78 | — | -570.35 |
| gate ON | long_p2 | QQQ | 62 | -88.68% | -6.67 | +1.61% | -76.73 | -103.38% | 83.34 | — | -4,757 |
| gate ON | short_p1_naked | QQQ | 62 | +5.46% | 2.16 | +93.55% | 153.36 | -124.66% | -259.02 | 7,864 | 9,509 |
| gate ON | short_c1_naked | QQQ | 62 | +0.76% | 0.4511 | +91.94% | 48.94 | -66.02% | -121.46 | 8,001 | 3,034 |
| gate ON | CS | QQQ | 62 | +0.43% | 0.2535 | +90.32% | 39.74 | -66.40% | -113.68 | — | 2,464 |
| gate ON | PS | QQQ | 62 | +2.76% | 1.26 | +93.55% | 76.64 | -100.20% | -175.68 | — | 4,752 |
| gate ON | long_c1 | SPY | 63 | -28.41% | -0.8030 | +11.11% | -24.59 | -104.68% | 59.84 | — | -1,549 |
| gate ON | long_p1 | SPY | 63 | -85.44% | -7.41 | +3.17% | -196.76 | -101.40% | 220.89 | — | -12,396 |
| gate ON | long_c2 | SPY | 63 | -147.64% | -72.07 | +0.00% | -5.56 | -173.85% | 3.83 | — | -350.08 |
| gate ON | long_p2 | SPY | 63 | -102.41% | -1,140 | +0.00% | -80.69 | -103.47% | 78.87 | — | -5,083 |
| gate ON | short_p1_naked | SPY | 63 | +7.56% | 7.21 | +96.83% | 192.48 | -57.60% | -220.89 | 9,629 | 12,127 |
| gate ON | short_c1_naked | SPY | 63 | +0.52% | 0.6148 | +88.89% | 20.65 | -27.78% | -59.84 | 9,795 | 1,301 |
| gate ON | CS | SPY | 63 | +0.30% | 0.3491 | +88.89% | 15.09 | -28.03% | -56.01 | — | 950.64 |
| gate ON | PS | SPY | 63 | +4.22% | 4.00 | +95.24% | 111.80 | -61.38% | -142.03 | — | 7,043 |
| every Friday | long_c1 | QQQ | 150 | +31.61% | 0.6854 | +14.67% | 46.17 | -102.60% | 119.50 | — | 6,925 |
| every Friday | long_p1 | QQQ | 150 | -55.19% | -2.82 | +7.33% | -149.71 | -101.45% | 253.82 | — | -22,456 |
| every Friday | long_c2 | QQQ | 150 | -120.59% | -146.04 | +0.00% | -9.05 | -135.19% | 7.63 | — | -1,358 |
| every Friday | long_p2 | QQQ | 150 | -96.53% | -17.29 | +0.67% | -79.90 | -103.62% | 81.70 | — | -11,985 |
| every Friday | short_p1_naked | QQQ | 150 | +5.00% | 2.72 | +92.67% | 144.93 | -124.66% | -253.82 | 7,880 | 21,739 |
| every Friday | short_c1_naked | QQQ | 150 | -1.53% | -0.7647 | +85.33% | -50.21 | -90.15% | -119.50 | 8,017 | -7,532 |
| every Friday | CS | QQQ | 150 | -1.86% | -0.9303 | +84.00% | -59.27 | -90.50% | -111.87 | — | -8,890 |
| every Friday | PS | QQQ | 150 | +2.06% | 1.19 | +92.67% | 65.03 | -100.20% | -172.12 | — | 9,754 |
| every Friday | long_c1 | SPY | 150 | -7.58% | -0.2007 | +10.67% | 4.19 | -105.35% | 59.51 | — | 628.22 |
| every Friday | long_p1 | SPY | 150 | -74.50% | -6.09 | +4.67% | -168.65 | -101.48% | 219.63 | — | -25,298 |
| every Friday | long_c2 | SPY | 150 | -148.63% | -96.21 | +0.00% | -5.55 | -180.85% | 3.82 | — | -832.11 |
| every Friday | long_p2 | SPY | 150 | -102.43% | -1,615 | +0.00% | -79.98 | -103.66% | 78.16 | — | -11,997 |
| every Friday | short_p1_naked | SPY | 150 | +6.57% | 5.95 | +95.33% | 164.38 | -92.22% | -219.63 | 9,568 | 24,657 |
| every Friday | short_c1_naked | SPY | 150 | +0.03% | 0.0283 | +89.33% | -8.13 | -59.74% | -59.51 | 9,728 | -1,219 |
| every Friday | CS | SPY | 150 | -0.20% | -0.2232 | +89.33% | -13.67 | -59.95% | -55.69 | — | -2,051 |
| every Friday | PS | SPY | 150 | +3.24% | 2.93 | +94.67% | 84.41 | -95.48% | -141.47 | — | 12,661 |


## Marked (panel): sleeve table

| sleeve | window | n | expiries | mean_ror | median_ror | hit | nw_t | nw_p | cl_t | cl_p | net_usd_total | mean_credit_over_width | mean_cost_over_credit | mean_x | mean_risk_usd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | P3 | 12 | 12 | +5.56% | +5.49% | +100.00% | 20.31 | 0.0000 | 23.42 | 0.0000 | 2,030 | +5.40% | +2.91% | 17.81 | 3,018 |
| SPY-IC | P3 | 8 | 8 | +7.63% | +7.77% | +100.00% | 23.96 | 0.0000 | 26.27 | 0.0000 | 1,836 | +7.33% | +3.61% | 17.87 | 2,987 |
| QQQ-PS | P3 | 12 | 12 | -2.11% | +6.66% | +75.00% | -0.3060 | 0.7653 | -0.3752 | 0.7147 | -775.18 | +6.32% | +2.53% | 25.15 | 4,057 |
| QQQ-IC | P3 | 7 | 7 | +3.47% | +8.77% | +71.43% | 0.7778 | 0.4662 | 0.8965 | 0.4045 | 1,113 | +8.65% | +2.99% | 25.08 | 4,265 |
| SPY-PS | pooled | 12 | 12 | +5.56% | +5.49% | +100.00% | 20.31 | 0.0000 | 23.42 | 0.0000 | 2,030 | +5.40% | +2.91% | 17.81 | 3,018 |
| SPY-IC | pooled | 8 | 8 | +7.63% | +7.77% | +100.00% | 23.96 | 0.0000 | 26.27 | 0.0000 | 1,836 | +7.33% | +3.61% | 17.87 | 2,987 |
| QQQ-PS | pooled | 12 | 12 | -2.11% | +6.66% | +75.00% | -0.3060 | 0.7653 | -0.3752 | 0.7147 | -775.18 | +6.32% | +2.53% | 25.15 | 4,057 |
| QQQ-IC | pooled | 7 | 7 | +3.47% | +8.77% | +71.43% | 0.7778 | 0.4662 | 0.8965 | 0.4045 | 1,113 | +8.65% | +2.99% | 25.08 | 4,265 |


## Marked vs proxy on the same positions (§6.7 criterion 2)

| sleeve | n_marked | n_overlap | marked_mean_ror | proxy_mean_ror | gap_ror | marked_cost_ror | overlap_pass |
|---|---|---|---|---|---|---|---|
| SPY-PS | 12 | 12 | +5.56% | +5.69% | +0.14% | +0.16% | yes |
| SPY-IC | 8 | 8 | +7.63% | +8.02% | +0.39% | +0.28% | no |
| QQQ-PS | 12 | 12 | -2.11% | -2.33% | -0.21% | +0.17% | no |
| QQQ-IC | 7 | 7 | +3.47% | +5.30% | +1.83% | +0.29% | no |


## Marked: tiers, credit, width, cost

| underlying | structure | n | graded | entry_tier_max | mean_credit | mean_width | mean_cost_over_credit |
|---|---|---|---|---|---|---|---|
| QQQ | IC | 9 | 7 | 1 | 4.29 | 46.89 | +2.99% |
| QQQ | PS | 14 | 12 | 1 | 2.85 | 43.93 | +2.53% |
| SPY | IC | 9 | 8 | 1 | 2.50 | 32.67 | +3.61% |
| SPY | PS | 14 | 12 | 1 | 1.84 | 32.79 | +2.91% |


## Marked: skipped entries by reason

| underlying | structure | reason | n |
|---|---|---|---|
| QQQ | IC | OFF:G1 | 2 |
| QQQ | IC | OFF:G2 | 18 |
| QQQ | IC | no_tier1_c2 | 5 |
| QQQ | PS | OFF:G1 | 2 |
| QQQ | PS | OFF:G2 | 18 |
| SPY | IC | OFF:G1 | 2 |
| SPY | IC | OFF:G2 | 18 |
| SPY | IC | no_tier1_c2 | 5 |
| SPY | PS | OFF:G1 | 2 |
| SPY | PS | OFF:G2 | 18 |


## Marked sensitivities (descriptive)

| sensitivity | sleeve | n | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|
| base | SPY-PS | 12 | +5.56% | 20.31 | 2,030 |
| base | SPY-IC | 8 | +7.63% | 23.96 | 1,836 |
| base | QQQ-PS | 12 | -2.11% | -0.3060 | -775.18 |
| base | QQQ-IC | 7 | +3.47% | 0.7778 | 1,113 |
| gate_off | SPY-PS | 27 | +5.50% | 30.50 | 4,369 |
| gate_off | SPY-IC | 22 | +4.46% | 1.59 | 1,980 |
| gate_off | QQQ-PS | 27 | +2.61% | 0.7829 | 2,858 |
| gate_off | QQQ-IC | 20 | +1.40% | 0.2520 | 1,214 |
| band_0.15 | SPY-PS | 12 | +5.56% | 20.31 | 2,030 |
| band_0.15 | SPY-IC | 8 | +7.63% | 23.96 | 1,836 |
| band_0.15 | QQQ-PS | 10 | -3.71% | -0.4647 | -1,215 |
| band_0.15 | QQQ-IC | 4 | -0.34% | -0.0628 | 9.42 |
| wing_1.5 | SPY-PS | 12 | +7.35% | 17.49 | 2,114 |
| wing_1.5 | SPY-IC | 12 | +7.05% | 2.54 | 1,998 |
| wing_1.5 | QQQ-PS | 12 | -6.33% | -0.5251 | -1,380 |
| wing_1.5 | QQQ-IC | 12 | -0.72% | -0.0556 | -21.58 |


## Go / no-go (DESIGN/80 §6.7; t >= 2.0; read 2026-12-01)

| sleeve | n_proxy | mean_proxy | nw_t_proxy | bh_pass | mean_p1 | mean_p2 | mean_p3 | n_marked | mean_marked | gap_ror | worst_over_median | deflated_sr | deflated_sr_null | forward_n | c1_proxy | c2_marked | c3_month | c4_dsr | c4_dsr_null | c5_scale | verdict | note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 63 | +4.22% | 4.00 | yes | +1.98% | +5.14% | +5.21% | 12 | +5.56% | +0.14% | 1.64 | 0.2638 | 0.3226 | 4 | yes | yes | yes | yes | yes | no | GO-MIN | clears 1-4; one contract until the forward ledger holds >= 40 graded positions (now 4) |
| SPY-IC | 63 | +4.59% | 3.45 | yes | -0.90% | +6.80% | +7.03% | 8 | +7.63% | +0.39% | 5.78 | 0.2124 | 0.2711 | 2 | no | no | no | yes | yes | no | NO-GO | fails c1_proxy, c2_marked, c3_month |
| QQQ-PS | 62 | +2.76% | 1.26 | no | +0.63% | +6.19% | +2.58% | 12 | -2.11% | -0.21% | 8.33 | -0.0523 | 0.0065 | 5 | no | no | no | no | yes | no | NO-GO | fails c1_proxy, c2_marked, c3_month, c4_dsr |
| QQQ-IC | 62 | +3.35% | 1.16 | no | -3.81% | +7.55% | +6.37% | 7 | +3.47% | +1.83% | 4.01 | -0.0634 | -0.0046 | 4 | no | no | no | no | no | no | NO-GO | fails c1_proxy, c2_marked, c3_month, c4_dsr |


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
