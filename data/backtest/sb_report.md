# S-B backtest report (generated)


## Inputs

- refreshed: {'index_vol_through': '2026-11-13', 'prices_through': '2026-11-13'}
- proxy: {'index_vol': ['1990-01-02', '2026-11-13'], 'sessions': ['2023-11-14', '2026-11-13'], 'n_sessions': 753}
- marked: {'panel': ['2026-03-13', '2026-11-13'], 'n_entry_sessions': 36}


## Gate ON share of entry sessions (proxy, by year)

| underlying | year | entry_sessions | gate_on | on_share |
|---|---|---|---|---|
| QQQ | 2023 | 3 | 1 | +33.33% |
| QQQ | 2024 | 52 | 26 | +50.00% |
| QQQ | 2025 | 52 | 15 | +28.85% |
| QQQ | 2026 | 43 | 21 | +48.84% |
| QQQ | all | 150 | 63 | +42.00% |
| SPY | 2023 | 3 | 1 | +33.33% |
| SPY | 2024 | 52 | 25 | +48.08% |
| SPY | 2025 | 52 | 16 | +30.77% |
| SPY | 2026 | 43 | 22 | +51.16% |
| SPY | all | 150 | 64 | +42.67% |


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
| SPY-PS | P3 | 31 | 31 | +5.23% | +5.71% | +96.77% | 12.09 | 0.0000 | 11.03 | 0.0000 | 4,656 | +5.53% | +2.55% | 18.01 | 2,870 |
| SPY-IC | P3 | 31 | 31 | +7.08% | +8.01% | +93.55% | 12.04 | 0.0000 | 10.76 | 0.0000 | 6,133 | +7.67% | +3.53% | 18.01 | 2,811 |
| QQQ-PS | P3 | 29 | 29 | +2.71% | +6.31% | +89.66% | 0.9008 | 0.3754 | 1.11 | 0.2774 | 2,646 | +6.04% | +2.13% | 23.86 | 3,518 |
| QQQ-IC | P3 | 29 | 29 | +6.53% | +10.61% | +86.21% | 2.10 | 0.0448 | 2.55 | 0.0167 | 6,347 | +9.88% | +2.32% | 23.86 | 3,393 |
| SPY-PS | pooled | 64 | 64 | +4.24% | +5.64% | +95.31% | 4.08 | 0.0001 | 3.96 | 0.0002 | 7,477 | +5.48% | +2.94% | 17.24 | 2,517 |
| SPY-IC | pooled | 64 | 64 | +4.65% | +7.92% | +87.50% | 3.54 | 0.0008 | 3.56 | 0.0007 | 7,225 | +7.64% | +4.06% | 17.24 | 2,561 |
| QQQ-PS | pooled | 63 | 63 | +2.82% | +6.19% | +93.65% | 1.32 | 0.1921 | 1.40 | 0.1658 | 5,046 | +5.99% | +2.59% | 21.87 | 2,773 |
| QQQ-IC | pooled | 63 | 63 | +3.47% | +10.48% | +85.71% | 1.23 | 0.2219 | 1.33 | 0.1885 | 6,906 | +9.83% | +2.84% | 21.87 | 2,722 |


## BH(0.10) across the four sleeves (proxy, pooled, on the NW p)

| sleeve | n | mean_ror | nw_t | nw_p | bh_pass |
|---|---|---|---|---|---|
| SPY-PS | 64 | +4.24% | 4.08 | 0.0001 | yes |
| SPY-IC | 64 | +4.65% | 3.54 | 0.0008 | yes |
| QQQ-PS | 63 | +2.82% | 1.32 | 0.1921 | no |
| QQQ-IC | 63 | +3.47% | 1.23 | 0.2219 | no |


## Deflated Sharpe (6 trials) — proxy pooled

| sleeve | n | sr | sr_star | deflated_sr | dsr_prob | sr_star_null | deflated_sr_null | dsr_prob_null | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 64 | 0.4946 | 0.2251 | 0.2696 | 0.7720 | 0.1638 | 0.3308 | 0.8198 | -7.39 | 59.64 |
| SPY-IC | 64 | 0.4450 | 0.2251 | 0.2199 | 0.7979 | 0.1638 | 0.2812 | 0.8569 | -4.59 | 28.03 |
| QQQ-PS | 63 | 0.1767 | 0.2251 | -0.0484 | 0.3998 | 0.1638 | 0.0129 | 0.5270 | -5.56 | 35.20 |
| QQQ-IC | 63 | 0.1675 | 0.2251 | -0.0575 | 0.3624 | 0.1638 | 0.0037 | 0.5091 | -3.36 | 14.13 |


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
| SPY-PS | 31 | 1.98 | 1.22 | 0.7580 | 0.7343 | 0.2414 | 1.74 | 0.9246 | -5.52 | 33.67 |
| SPY-IC | 31 | 1.93 | 1.22 | 0.7103 | 0.7971 | 0.2414 | 1.69 | 0.9762 | -3.71 | 15.68 |
| QQQ-PS | 29 | 0.2057 | 1.22 | -1.02 | 0.0001 | 0.2414 | -0.0357 | 0.4490 | -4.49 | 24.48 |
| QQQ-IC | 29 | 0.4729 | 1.22 | -0.7499 | 0.0278 | 0.2414 | 0.2314 | 0.7227 | -4.33 | 23.34 |


## PBO (CSCV over 16 entry blocks, proxy pooled)

- pbo: 0.3502719502719503
- mean_logit: 0.2800130693213883
- n_combinations: 12870
- n_configs: 4
- n_blocks: 16
- n_entries: 69


## Month rule (proxy; worst expiry-month vs median month, $ at frozen sizing)

| sleeve | n_months | median_month_usd | worst_month | worst_month_usd | worst_over_median | months_negative | month_rule_pass |
|---|---|---|---|---|---|---|---|
| SPY-PS | 29 | 249.60 | 2024-08 | -396.47 | 1.59 | 2 | yes |
| SPY-IC | 29 | 266.06 | 2024-08 | -1,537 | 5.78 | 4 | no |
| QQQ-PS | 29 | 258.31 | 2026-10 | -2,153 | 8.33 | 3 | no |
| QQQ-IC | 29 | 397.25 | 2026-10 | -1,592 | 4.01 | 5 | no |


## Tail report (proxy, pooled)

| sleeve | n | mean_ror | worst_ror | worst_entry | best_ror | mean_win_ror | worst_decile_share_of_loss | full_width_losses | mean_without_worst_1pct | mean_without_best_1pct | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 64 | +4.24% | -61.38% | 2024-07-12 | +6.12% | +5.64% | 1.00 | 0 | +5.29% | +4.22% | -7.39 | 56.64 |
| SPY-IC | 64 | +4.65% | -60.67% | 2024-07-12 | +8.42% | +7.74% | 0.9463 | 0 | +5.68% | +4.59% | -4.59 | 25.03 |
| QQQ-PS | 63 | +2.82% | -100.20% | 2024-07-12 | +6.60% | +6.16% | 1.00 | 1 | +4.49% | +2.76% | -5.56 | 32.20 |
| QQQ-IC | 63 | +3.47% | -95.11% | 2024-07-12 | +11.07% | +10.38% | 0.9467 | 0 | +5.06% | +3.35% | -3.36 | 11.13 |

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
| base | SPY-PS | 64 | +4.24% | 4.08 | 3.96 | 7,477 | +2.94% |
| base | SPY-IC | 64 | +4.65% | 3.54 | 3.56 | 7,225 | +4.06% |
| base | QQQ-PS | 63 | +2.82% | 1.32 | 1.40 | 5,046 | +2.59% |
| base | QQQ-IC | 63 | +3.47% | 1.23 | 1.33 | 6,906 | +2.84% |
| gate_off | SPY-PS | 150 | +3.24% | 2.93 | 3.26 | 13,450 | +2.97% |
| gate_off | SPY-IC | 150 | +3.15% | 2.28 | 2.63 | 10,595 | +4.10% |
| gate_off | QQQ-PS | 150 | +2.06% | 1.20 | 1.43 | 10,047 | +2.62% |
| gate_off | QQQ-IC | 150 | +0.32% | 0.1242 | 0.1564 | 811.08 | +2.88% |
| g1_only | SPY-PS | 139 | +3.75% | 4.09 | 4.71 | 13,818 | +3.04% |
| g1_only | SPY-IC | 139 | +4.23% | 3.76 | 4.38 | 14,242 | +4.19% |
| g1_only | QQQ-PS | 139 | +2.42% | 1.38 | 1.72 | 10,371 | +2.66% |
| g1_only | QQQ-IC | 139 | +1.81% | 0.7304 | 0.9278 | 7,443 | +2.92% |
| g2_only | SPY-PS | 74 | +3.11% | 1.95 | 1.90 | 6,922 | +2.83% |
| g2_only | SPY-IC | 74 | +2.85% | 1.57 | 1.48 | 4,443 | +3.91% |
| g2_only | QQQ-PS | 73 | +1.99% | 0.9040 | 0.9184 | 4,534 | +2.52% |
| g2_only | QQQ-IC | 73 | +0.85% | 0.2854 | 0.2909 | 1,620 | +2.77% |
| costs_x2 | SPY-PS | 64 | +4.08% | 3.91 | 3.80 | 7,212 | +5.88% |
| costs_x2 | SPY-IC | 64 | +4.31% | 3.27 | 3.30 | 6,687 | +8.12% |
| costs_x2 | QQQ-PS | 63 | +2.66% | 1.24 | 1.32 | 4,776 | +5.17% |
| costs_x2 | QQQ-IC | 63 | +3.16% | 1.12 | 1.21 | 6,405 | +5.69% |
| wing_1.5 | SPY-PS | 64 | -0.43% | -0.2674 | -0.2588 | -496.77 | +19.11% |
| wing_1.5 | SPY-IC | 64 | -1.44% | -0.6535 | -0.6615 | -1,812 | +16.79% |
| wing_1.5 | QQQ-PS | 63 | -1.52% | -0.5422 | -0.6326 | -2,015 | +11.78% |
| wing_1.5 | QQQ-IC | 63 | -1.63% | -0.4125 | -0.4535 | -2,215 | +7.24% |


## Other structures on the proxy (descriptive; not sleeves, never a verdict input)

Single legs, naked shorts and the call spread re-priced on the same entry rows with the frozen smile and costs. Risk: debit = premium; credit spread = width - credit; naked = the 2-sigma stress loss (the matching spread's max loss), Reg-T proxy margin beside. `PS` here is the champion recomputed as a check. Drafts: `ledger/challengers/drafts/sb-c-callspread.json`, `sb-c-nakedput-margin.json`.

| set | structure | underlying | n | mean_ror | nw_t | hit | mean_pnl_usd | worst_ror | mean_premium_usd | mean_margin_usd | total_pnl_usd |
|---|---|---|---|---|---|---|---|---|---|---|---|
| gate ON | long_c1 | QQQ | 63 | -23.09% | -0.6128 | +7.94% | -55.40 | -102.60% | 122.72 | — | -3,490 |
| gate ON | long_p1 | QQQ | 63 | -59.99% | -2.26 | +6.35% | -162.55 | -101.38% | 261.73 | — | -10,241 |
| gate ON | long_c2 | QQQ | 63 | -120.04% | -98.23 | +0.00% | -9.29 | -134.00% | 7.87 | — | -585.32 |
| gate ON | long_p2 | QQQ | 63 | -88.88% | -6.79 | +1.59% | -77.61 | -103.38% | 84.09 | — | -4,889 |
| gate ON | short_p1_naked | QQQ | 63 | +5.52% | 2.23 | +93.65% | 157.70 | -124.66% | -261.73 | 7,881 | 9,935 |
| gate ON | short_c1_naked | QQQ | 63 | +0.81% | 0.4916 | +92.06% | 51.31 | -66.02% | -122.72 | 8,019 | 3,233 |
| gate ON | CS | QQQ | 63 | +0.48% | 0.2912 | +90.48% | 42.02 | -66.40% | -114.85 | — | 2,647 |
| gate ON | PS | QQQ | 63 | +2.82% | 1.32 | +93.65% | 80.09 | -100.20% | -177.64 | — | 5,046 |
| gate ON | long_c1 | SPY | 64 | -29.57% | -0.8477 | +10.94% | -25.56 | -104.68% | 60.23 | — | -1,636 |
| gate ON | long_p1 | SPY | 64 | -85.68% | -7.54 | +3.12% | -198.64 | -101.40% | 222.35 | — | -12,713 |
| gate ON | long_c2 | SPY | 64 | -147.47% | -72.36 | +0.00% | -5.58 | -173.85% | 3.85 | — | -357.08 |
| gate ON | long_p2 | SPY | 64 | -102.40% | -1,145 | +0.00% | -81.14 | -103.47% | 79.31 | — | -5,193 |
| gate ON | short_p1_naked | SPY | 64 | +7.58% | 7.34 | +96.88% | 194.35 | -57.60% | -222.35 | 9,657 | 12,438 |
| gate ON | short_c1_naked | SPY | 64 | +0.55% | 0.6574 | +89.06% | 21.61 | -27.78% | -60.23 | 9,823 | 1,383 |
| gate ON | CS | SPY | 64 | +0.33% | 0.3883 | +89.06% | 16.03 | -28.03% | -56.37 | — | 1,026 |
| gate ON | PS | SPY | 64 | +4.24% | 4.08 | +95.31% | 113.21 | -61.38% | -143.04 | — | 7,246 |
| every Friday | long_c1 | QQQ | 150 | +29.04% | 0.6295 | +14.00% | 43.58 | -102.60% | 120.40 | — | 6,537 |
| every Friday | long_p1 | QQQ | 150 | -55.18% | -2.82 | +7.33% | -151.72 | -101.45% | 255.82 | — | -22,758 |
| every Friday | long_c2 | QQQ | 150 | -120.43% | -147.61 | +0.00% | -9.12 | -134.00% | 7.70 | — | -1,368 |
| every Friday | long_p2 | QQQ | 150 | -96.51% | -17.29 | +0.67% | -80.48 | -103.62% | 82.27 | — | -12,072 |
| every Friday | short_p1_naked | QQQ | 150 | +5.01% | 2.73 | +92.67% | 146.92 | -124.66% | -255.82 | 7,898 | 22,038 |
| every Friday | short_c1_naked | QQQ | 150 | -1.41% | -0.7062 | +86.00% | -47.64 | -90.15% | -120.40 | 8,036 | -7,146 |
| every Friday | CS | QQQ | 150 | -1.74% | -0.8716 | +84.67% | -56.75 | -90.50% | -112.71 | — | -8,513 |
| every Friday | PS | QQQ | 150 | +2.06% | 1.20 | +92.67% | 66.44 | -100.20% | -173.55 | — | 9,966 |
| every Friday | long_c1 | SPY | 150 | -10.30% | -0.2730 | +10.00% | 2.96 | -105.35% | 59.86 | — | 444.08 |
| every Friday | long_p1 | SPY | 150 | -74.50% | -6.09 | +4.67% | -169.94 | -101.48% | 220.91 | — | -25,491 |
| every Friday | long_c2 | SPY | 150 | -148.41% | -97.07 | +0.00% | -5.57 | -180.85% | 3.84 | — | -835.35 |
| every Friday | long_p2 | SPY | 150 | -102.42% | -1,645 | +0.00% | -80.41 | -103.54% | 78.59 | — | -12,061 |
| every Friday | short_p1_naked | SPY | 150 | +6.58% | 5.95 | +95.33% | 165.66 | -92.22% | -220.91 | 9,592 | 24,849 |
| every Friday | short_c1_naked | SPY | 150 | +0.09% | 0.1049 | +90.00% | -6.91 | -59.74% | -59.86 | 9,753 | -1,036 |
| every Friday | CS | SPY | 150 | -0.13% | -0.1459 | +90.00% | -12.48 | -59.95% | -56.02 | — | -1,871 |
| every Friday | PS | SPY | 150 | +3.24% | 2.93 | +94.67% | 85.25 | -95.48% | -142.33 | — | 12,788 |


## Marked (panel): sleeve table

| sleeve | window | n | expiries | mean_ror | median_ror | hit | nw_t | nw_p | cl_t | cl_p | net_usd_total | mean_credit_over_width | mean_cost_over_credit | mean_x | mean_risk_usd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | P3 | 13 | 13 | +5.53% | +5.47% | +100.00% | 21.13 | 0.0000 | 25.10 | 0.0000 | 2,227 | +5.38% | +2.89% | 17.94 | 3,078 |
| SPY-IC | P3 | 8 | 8 | +7.63% | +7.77% | +100.00% | 23.96 | 0.0000 | 26.27 | 0.0000 | 1,836 | +7.33% | +3.61% | 17.87 | 2,987 |
| QQQ-PS | P3 | 13 | 13 | -1.39% | +6.75% | +76.92% | -0.2250 | 0.8258 | -0.2664 | 0.7945 | -471.76 | +6.36% | +2.44% | 25.40 | 4,068 |
| QQQ-IC | P3 | 8 | 8 | +4.50% | +8.97% | +75.00% | 1.27 | 0.2451 | 1.28 | 0.2406 | 1,582 | +8.90% | +2.87% | 25.48 | 4,234 |
| SPY-PS | pooled | 13 | 13 | +5.53% | +5.47% | +100.00% | 21.13 | 0.0000 | 25.10 | 0.0000 | 2,227 | +5.38% | +2.89% | 17.94 | 3,078 |
| SPY-IC | pooled | 8 | 8 | +7.63% | +7.77% | +100.00% | 23.96 | 0.0000 | 26.27 | 0.0000 | 1,836 | +7.33% | +3.61% | 17.87 | 2,987 |
| QQQ-PS | pooled | 13 | 13 | -1.39% | +6.75% | +76.92% | -0.2250 | 0.8258 | -0.2664 | 0.7945 | -471.76 | +6.36% | +2.44% | 25.40 | 4,068 |
| QQQ-IC | pooled | 8 | 8 | +4.50% | +8.97% | +75.00% | 1.27 | 0.2451 | 1.28 | 0.2406 | 1,582 | +8.90% | +2.87% | 25.48 | 4,234 |


## Marked vs proxy on the same positions (§6.7 criterion 2)

| sleeve | n_marked | n_overlap | marked_mean_ror | proxy_mean_ror | gap_ror | marked_cost_ror | overlap_pass |
|---|---|---|---|---|---|---|---|
| SPY-PS | 13 | 13 | +5.53% | +5.71% | +0.19% | +0.16% | no |
| SPY-IC | 8 | 8 | +7.63% | +8.02% | +0.39% | +0.28% | no |
| QQQ-PS | 13 | 13 | -1.39% | -1.64% | -0.25% | +0.17% | no |
| QQQ-IC | 8 | 8 | +4.50% | +6.02% | +1.52% | +0.28% | no |


## Marked: tiers, credit, width, cost

| underlying | structure | n | graded | entry_tier_max | mean_credit | mean_width | mean_cost_over_credit |
|---|---|---|---|---|---|---|---|
| QQQ | IC | 10 | 8 | 1 | 4.30 | 47.70 | +2.87% |
| QQQ | PS | 15 | 13 | 1 | 2.86 | 44.67 | +2.44% |
| SPY | IC | 9 | 8 | 1 | 2.50 | 32.67 | +3.61% |
| SPY | PS | 14 | 13 | 1 | 1.84 | 32.79 | +2.89% |


## Marked: skipped entries by reason

| underlying | structure | reason | n |
|---|---|---|---|
| QQQ | IC | OFF:G1 | 2 |
| QQQ | IC | OFF:G2 | 18 |
| QQQ | IC | no_tier1_c2 | 5 |
| QQQ | PS | OFF:G1 | 2 |
| QQQ | PS | OFF:G2 | 18 |
| SPY | IC | OFF:G1 | 2 |
| SPY | IC | OFF:G2 | 19 |
| SPY | IC | no_tier1_c2 | 5 |
| SPY | PS | OFF:G1 | 2 |
| SPY | PS | OFF:G2 | 19 |


## Marked sensitivities (descriptive)

| sensitivity | sleeve | n | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|
| base | SPY-PS | 13 | +5.53% | 21.13 | 2,227 |
| base | SPY-IC | 8 | +7.63% | 23.96 | 1,836 |
| base | QQQ-PS | 13 | -1.39% | -0.2250 | -471.76 |
| base | QQQ-IC | 8 | +4.50% | 1.27 | 1,582 |
| gate_off | SPY-PS | 28 | +5.49% | 31.10 | 4,565 |
| gate_off | SPY-IC | 22 | +4.46% | 1.59 | 1,980 |
| gate_off | QQQ-PS | 28 | +2.77% | 0.8777 | 3,161 |
| gate_off | QQQ-IC | 21 | +1.89% | 0.3599 | 1,683 |
| band_0.15 | SPY-PS | 13 | +5.53% | 21.13 | 2,227 |
| band_0.15 | SPY-IC | 8 | +7.63% | 23.96 | 1,836 |
| band_0.15 | QQQ-PS | 11 | -2.72% | -0.3862 | -911.48 |
| band_0.15 | QQQ-IC | 5 | +2.06% | 0.5394 | 478.76 |
| wing_1.5 | SPY-PS | 13 | +7.33% | 18.31 | 2,245 |
| wing_1.5 | SPY-IC | 13 | +7.29% | 2.83 | 2,183 |
| wing_1.5 | QQQ-PS | 13 | -5.09% | -0.4723 | -1,203 |
| wing_1.5 | QQQ-IC | 13 | +0.35% | 0.0297 | 302.39 |


## Go / no-go (DESIGN/80 §6.7; t >= 2.0; read 2026-12-01)

| sleeve | n_proxy | mean_proxy | nw_t_proxy | bh_pass | mean_p1 | mean_p2 | mean_p3 | n_marked | mean_marked | gap_ror | worst_over_median | deflated_sr | deflated_sr_null | forward_n | c1_proxy | c2_marked | c3_month | c4_dsr | c4_dsr_null | c5_scale | verdict | note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 64 | +4.24% | 4.08 | yes | +1.98% | +5.14% | +5.23% | 13 | +5.53% | +0.19% | 1.59 | 0.2696 | 0.3308 | 5 | yes | no | yes | yes | yes | no | NO-GO | fails c2_marked |
| SPY-IC | 64 | +4.65% | 3.54 | yes | -0.90% | +6.80% | +7.08% | 8 | +7.63% | +0.39% | 5.78 | 0.2199 | 0.2812 | 2 | no | no | no | yes | yes | no | NO-GO | fails c1_proxy, c2_marked, c3_month |
| QQQ-PS | 63 | +2.82% | 1.32 | no | +0.63% | +6.19% | +2.71% | 13 | -1.39% | -0.25% | 8.33 | -0.0484 | 0.0129 | 6 | no | no | no | no | yes | no | NO-GO | fails c1_proxy, c2_marked, c3_month, c4_dsr |
| QQQ-IC | 63 | +3.47% | 1.23 | no | -3.81% | +7.55% | +6.53% | 8 | +4.50% | +1.52% | 4.01 | -0.0575 | 0.0037 | 5 | no | no | no | no | yes | no | NO-GO | fails c1_proxy, c2_marked, c3_month, c4_dsr |


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
