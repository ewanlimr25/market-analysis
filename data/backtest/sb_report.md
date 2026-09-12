# S-B backtest report (generated)


## Inputs

- refreshed: {'index_vol_through': '2026-09-11', 'prices_through': '2026-09-11'}
- proxy: {'index_vol': ['1990-01-02', '2026-09-11'], 'sessions': ['2023-09-12', '2026-09-11'], 'n_sessions': 753}
- marked: {'panel': ['2026-03-13', '2026-09-11'], 'n_entry_sessions': 27}


## Gate ON share of entry sessions (proxy, by year)

| underlying | year | entry_sessions | gate_on | on_share |
|---|---|---|---|---|
| QQQ | 2023 | 12 | 3 | +25.00% |
| QQQ | 2024 | 52 | 26 | +50.00% |
| QQQ | 2025 | 52 | 15 | +28.85% |
| QQQ | 2026 | 34 | 15 | +44.12% |
| QQQ | all | 150 | 59 | +39.33% |
| SPY | 2023 | 12 | 3 | +25.00% |
| SPY | 2024 | 52 | 25 | +48.08% |
| SPY | 2025 | 52 | 16 | +30.77% |
| SPY | 2026 | 34 | 17 | +50.00% |
| SPY | all | 150 | 61 | +40.67% |


## Proxy: mean net return on risk per position; NW(lag 2) t and expiry-clustered t

| sleeve | window | n | expiries | mean_ror | median_ror | hit | nw_t | nw_p | cl_t | cl_p | net_usd_total | mean_credit_over_width | mean_cost_over_credit | mean_x | mean_risk_usd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | P1 | 21 | 21 | +2.34% | +5.48% | +95.24% | 0.7935 | 0.4368 | 0.7349 | 0.4709 | 1,319 | +5.41% | +3.62% | 15.91 | 2,004 |
| SPY-IC | P1 | 21 | 21 | -4.67% | +7.49% | +71.43% | -0.9517 | 0.3526 | -0.8382 | 0.4118 | -2,697 | +7.55% | +4.99% | 15.91 | 2,254 |
| QQQ-PS | P1 | 22 | 22 | +1.14% | +6.10% | +95.45% | 0.2514 | 0.8040 | 0.2355 | 0.8161 | 521.68 | +5.90% | +3.20% | 19.96 | 1,924 |
| QQQ-IC | P1 | 22 | 22 | -8.11% | +10.12% | +72.73% | -1.09 | 0.2902 | -1.06 | 0.3007 | -3,704 | +9.72% | +3.55% | 19.96 | 1,994 |
| SPY-PS | P2 | 14 | 14 | +5.14% | +5.68% | +92.86% | 10.81 | 0.0000 | 9.41 | 0.0000 | 1,739 | +5.52% | +2.80% | 18.13 | 2,436 |
| SPY-IC | P2 | 14 | 14 | +6.80% | +7.96% | +92.86% | 9.55 | 0.0000 | 8.25 | 0.0000 | 2,229 | +7.70% | +3.88% | 18.13 | 2,387 |
| QQQ-PS | P2 | 14 | 14 | +6.19% | +6.22% | +100.00% | 188.56 | 0.0000 | 139.83 | 0.0000 | 2,118 | +6.02% | +2.63% | 21.16 | 2,443 |
| QQQ-IC | P2 | 14 | 14 | +7.55% | +10.51% | +92.86% | 2.58 | 0.0227 | 2.48 | 0.0276 | 2,417 | +9.87% | +2.90% | 21.16 | 2,356 |
| SPY-PS | P3 | 26 | 26 | +5.14% | +5.73% | +96.15% | 10.08 | 0.0000 | 9.09 | 0.0000 | 3,801 | +5.53% | +2.57% | 18.19 | 2,848 |
| SPY-IC | P3 | 26 | 26 | +6.89% | +8.01% | +92.31% | 10.09 | 0.0000 | 8.82 | 0.0000 | 4,955 | +7.67% | +3.55% | 18.19 | 2,791 |
| QQQ-PS | P3 | 23 | 23 | +6.30% | +6.35% | +100.00% | 142.42 | 0.0000 | 179.41 | 0.0000 | 5,008 | +6.05% | +2.16% | 24.04 | 3,443 |
| QQQ-IC | P3 | 23 | 23 | +10.14% | +10.70% | +95.65% | 20.01 | 0.0000 | 18.83 | 0.0000 | 7,790 | +9.87% | +2.35% | 24.04 | 3,326 |
| SPY-PS | pooled | 61 | 61 | +4.18% | +5.65% | +95.08% | 3.84 | 0.0003 | 3.71 | 0.0005 | 6,858 | +5.49% | +2.98% | 17.39 | 2,463 |
| SPY-IC | pooled | 61 | 61 | +2.89% | +7.88% | +85.25% | 1.39 | 0.1706 | 1.41 | 0.1644 | 4,487 | +7.63% | +4.12% | 17.39 | 2,513 |
| QQQ-PS | pooled | 59 | 59 | +4.35% | +6.22% | +98.31% | 2.44 | 0.0177 | 2.41 | 0.0191 | 7,648 | +5.99% | +2.66% | 21.83 | 2,639 |
| QQQ-IC | pooled | 59 | 59 | +2.72% | +10.48% | +86.44% | 0.7944 | 0.4302 | 0.8768 | 0.3842 | 6,503 | +9.81% | +2.93% | 21.83 | 2,599 |


## BH(0.10) across the four sleeves (proxy, pooled, on the NW p)

| sleeve | n | mean_ror | nw_t | nw_p | bh_pass |
|---|---|---|---|---|---|
| SPY-PS | 61 | +4.18% | 3.84 | 0.0003 | yes |
| SPY-IC | 61 | +2.89% | 1.39 | 0.1706 | no |
| QQQ-PS | 59 | +4.35% | 2.44 | 0.0177 | yes |
| QQQ-IC | 59 | +2.72% | 0.7944 | 0.4302 | no |


## Deflated Sharpe (6 trials) — proxy pooled

| sleeve | n | sr | sr_star | deflated_sr | dsr_prob | sr_star_null | deflated_sr_null | dsr_prob_null | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 61 | 0.4753 | 0.2075 | 0.2678 | 0.7743 | 0.1693 | 0.3060 | 0.8053 | -7.21 | 56.97 |
| SPY-IC | 61 | 0.1802 | 0.2075 | -0.0273 | 0.4405 | 0.1693 | 0.0110 | 0.5240 | -4.43 | 24.53 |
| QQQ-PS | 59 | 0.3139 | 0.2075 | 0.1064 | 0.6427 | 0.1693 | 0.1447 | 0.6905 | -7.67 | 61.91 |
| QQQ-IC | 59 | 0.1141 | 0.2075 | -0.0934 | 0.2762 | 0.1693 | -0.0551 | 0.3629 | -3.41 | 14.08 |


## Deflated Sharpe (6 trials) — proxy P1

| sleeve | n | sr | sr_star | deflated_sr | dsr_prob | sr_star_null | deflated_sr_null | dsr_prob_null | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 21 | 0.1604 | 0.2409 | -0.0805 | 0.3964 | 0.2837 | -0.1233 | 0.3438 | -4.58 | 23.99 |
| SPY-IC | 21 | -0.1829 | 0.2409 | -0.4238 | 0.0076 | 0.2837 | -0.4666 | 0.0038 | -2.51 | 9.14 |
| QQQ-PS | 22 | 0.0502 | 0.2409 | -0.1907 | 0.2173 | 0.2837 | -0.2335 | 0.1693 | -4.69 | 24.97 |
| QQQ-IC | 22 | -0.2262 | 0.2409 | -0.4671 | 0.0034 | 0.2837 | -0.5099 | 0.0016 | -1.89 | 5.21 |


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

- pbo: 0.5072261072261073
- mean_logit: -0.1155267913902092
- n_combinations: 12870
- n_configs: 4
- n_blocks: 16
- n_entries: 65


## Month rule (proxy; worst expiry-month vs median month, $ at frozen sizing)

| sleeve | n_months | median_month_usd | worst_month | worst_month_usd | worst_over_median | months_negative | month_rule_pass |
|---|---|---|---|---|---|---|---|
| SPY-PS | 28 | 241.49 | 2024-08 | -396.47 | 1.64 | 2 | yes |
| SPY-IC | 28 | 251.10 | 2023-11 | -1,560 | 6.21 | 5 | no |
| QQQ-PS | 28 | 271.59 | 2024-08 | -1,325 | 4.88 | 1 | no |
| QQQ-IC | 28 | 409.24 | 2023-11 | -1,846 | 4.51 | 5 | no |


## Tail report (proxy, pooled)

| sleeve | n | mean_ror | worst_ror | worst_entry | best_ror | mean_win_ror | worst_decile_share_of_loss | full_width_losses | mean_without_worst_1pct | mean_without_best_1pct | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 61 | +4.18% | -61.38% | 2024-07-12 | +6.12% | +5.64% | 1.00 | 0 | +5.27% | +4.14% | -7.21 | 53.97 |
| SPY-IC | 61 | +2.89% | -88.96% | 2023-10-27 | +8.42% | +7.72% | 0.9363 | 0 | +4.42% | +2.80% | -4.43 | 21.53 |
| QQQ-PS | 59 | +4.35% | -100.20% | 2024-07-12 | +6.60% | +6.15% | 1.00 | 1 | +6.15% | +4.31% | -7.67 | 58.91 |
| QQQ-IC | 59 | +2.72% | -100.38% | 2023-10-27 | +11.01% | +10.35% | 0.9540 | 1 | +4.50% | +2.58% | -3.41 | 11.08 |

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
| base | SPY-PS | 61 | +4.18% | 3.84 | 3.71 | 6,858 | +2.98% |
| base | SPY-IC | 61 | +2.89% | 1.39 | 1.41 | 4,487 | +4.12% |
| base | QQQ-PS | 59 | +4.35% | 2.44 | 2.41 | 7,648 | +2.66% |
| base | QQQ-IC | 59 | +2.72% | 0.7944 | 0.8768 | 6,503 | +2.93% |
| gate_off | SPY-PS | 150 | +3.24% | 2.93 | 3.26 | 13,279 | +3.05% |
| gate_off | SPY-IC | 150 | +1.99% | 1.26 | 1.46 | 6,326 | +4.21% |
| gate_off | QQQ-PS | 150 | +2.74% | 1.67 | 1.99 | 12,945 | +2.71% |
| gate_off | QQQ-IC | 150 | -0.35% | -0.1312 | -0.1632 | -574.01 | +2.98% |
| g1_only | SPY-PS | 139 | +3.75% | 4.09 | 4.71 | 13,647 | +3.12% |
| g1_only | SPY-IC | 139 | +2.97% | 2.11 | 2.47 | 9,973 | +4.31% |
| g1_only | QQQ-PS | 139 | +3.15% | 1.91 | 2.38 | 13,269 | +2.76% |
| g1_only | QQQ-IC | 139 | +1.09% | 0.4257 | 0.5330 | 6,058 | +3.04% |
| g2_only | SPY-PS | 71 | +3.01% | 1.81 | 1.76 | 6,303 | +2.86% |
| g2_only | SPY-IC | 71 | +1.26% | 0.5576 | 0.5319 | 1,704 | +3.96% |
| g2_only | QQQ-PS | 69 | +3.24% | 1.62 | 1.57 | 7,136 | +2.57% |
| g2_only | QQQ-IC | 69 | +0.06% | 0.0173 | 0.0180 | 1,217 | +2.84% |
| costs_x2 | SPY-PS | 61 | +4.00% | 3.67 | 3.56 | 6,608 | +5.96% |
| costs_x2 | SPY-IC | 61 | +2.55% | 1.22 | 1.24 | 3,975 | +8.24% |
| costs_x2 | QQQ-PS | 59 | +4.18% | 2.34 | 2.32 | 7,400 | +5.32% |
| costs_x2 | QQQ-IC | 59 | +2.40% | 0.7001 | 0.7736 | 6,040 | +5.86% |
| wing_1.5 | SPY-PS | 61 | -0.54% | -0.3175 | -0.3068 | -618.90 | +19.27% |
| wing_1.5 | SPY-IC | 61 | -3.31% | -1.20 | -1.22 | -4,148 | +16.97% |
| wing_1.5 | QQQ-PS | 59 | +1.13% | 0.6431 | 0.6425 | 1,032 | +12.02% |
| wing_1.5 | QQQ-IC | 59 | -1.60% | -0.3756 | -0.4183 | -3,188 | +7.42% |


## Marked (panel): sleeve table

| sleeve | window | n | expiries | mean_ror | median_ror | hit | nw_t | nw_p | cl_t | cl_p | net_usd_total | mean_credit_over_width | mean_cost_over_credit | mean_x | mean_risk_usd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | P3 | 7 | 7 | +6.02% | +5.99% | +100.00% | 28.20 | 0.0000 | 21.72 | 0.0000 | 1,342 | +5.80% | +2.32% | 18.94 | 3,161 |
| SPY-IC | P3 | 5 | 5 | +7.98% | +8.04% | +100.00% | 28.76 | 0.0000 | 28.37 | 0.0000 | 1,275 | +7.62% | +3.34% | 19.53 | 3,176 |
| QQQ-PS | P3 | 7 | 7 | +7.27% | +6.97% | +100.00% | 52.34 | 0.0000 | 28.96 | 0.0000 | 2,111 | +6.94% | +2.63% | 27.30 | 4,147 |
| QQQ-IC | P3 | 3 | 3 | +10.21% | +10.38% | +100.00% | 42.67 | 0.0005 | 18.41 | 0.0029 | 1,360 | +9.52% | +2.98% | 28.45 | 4,433 |
| SPY-PS | pooled | 7 | 7 | +6.02% | +5.99% | +100.00% | 28.20 | 0.0000 | 21.72 | 0.0000 | 1,342 | +5.80% | +2.32% | 18.94 | 3,161 |
| SPY-IC | pooled | 5 | 5 | +7.98% | +8.04% | +100.00% | 28.76 | 0.0000 | 28.37 | 0.0000 | 1,275 | +7.62% | +3.34% | 19.53 | 3,176 |
| QQQ-PS | pooled | 7 | 7 | +7.27% | +6.97% | +100.00% | 52.34 | 0.0000 | 28.96 | 0.0000 | 2,111 | +6.94% | +2.63% | 27.30 | 4,147 |
| QQQ-IC | pooled | 3 | 3 | +10.21% | +10.38% | +100.00% | 42.67 | 0.0005 | 18.41 | 0.0029 | 1,360 | +9.52% | +2.98% | 28.45 | 4,433 |


## Marked vs proxy on the same positions (§6.7 criterion 2)

| sleeve | n_marked | n_overlap | marked_mean_ror | proxy_mean_ror | gap_ror | marked_cost_ror | overlap_pass |
|---|---|---|---|---|---|---|---|
| SPY-PS | 7 | 7 | +6.02% | +5.73% | -0.29% | +0.14% | yes |
| SPY-IC | 5 | 5 | +7.98% | +8.12% | +0.14% | +0.27% | yes |
| QQQ-PS | 7 | 7 | +7.27% | +6.40% | -0.87% | +0.20% | yes |
| QQQ-IC | 3 | 3 | +10.21% | +10.77% | +0.56% | +0.32% | no |


## Marked: tiers, credit, width, cost

| underlying | structure | n | graded | entry_tier_max | mean_credit | mean_width | mean_cost_over_credit |
|---|---|---|---|---|---|---|---|
| QQQ | IC | 4 | 3 | 1 | 4.33 | 48.00 | +2.98% |
| QQQ | PS | 8 | 7 | 1 | 3.00 | 44.62 | +2.63% |
| SPY | IC | 6 | 5 | 1 | 2.52 | 34.00 | +3.34% |
| SPY | PS | 9 | 7 | 1 | 1.85 | 32.56 | +2.32% |


## Marked: skipped entries by reason

| underlying | structure | reason | n |
|---|---|---|---|
| QQQ | IC | OFF:G1 | 1 |
| QQQ | IC | OFF:G2 | 17 |
| QQQ | IC | no_tier1_c2 | 4 |
| QQQ | PS | OFF:G1 | 1 |
| QQQ | PS | OFF:G2 | 17 |
| SPY | IC | OFF:G1 | 1 |
| SPY | IC | OFF:G2 | 16 |
| SPY | IC | no_tier1_c2 | 3 |
| SPY | PS | OFF:G1 | 1 |
| SPY | PS | OFF:G2 | 16 |


## Marked sensitivities (descriptive)

| sensitivity | sleeve | n | mean_ror | nw_t | net_usd_total |
|---|---|---|---|---|---|
| base | SPY-PS | 7 | +6.02% | 28.20 | 1,342 |
| base | SPY-IC | 5 | +7.98% | 28.76 | 1,275 |
| base | QQQ-PS | 7 | +7.27% | 52.34 | 2,111 |
| base | QQQ-IC | 3 | +10.21% | 42.67 | 1,360 |
| gate_off | SPY-PS | 18 | +5.77% | 31.80 | 3,170 |
| gate_off | SPY-IC | 15 | +3.37% | 0.8365 | 710.33 |
| gate_off | QQQ-PS | 18 | +6.83% | 40.44 | 4,991 |
| gate_off | QQQ-IC | 13 | +0.84% | 0.1028 | 594.81 |
| band_0.15 | SPY-PS | 7 | +6.02% | 28.20 | 1,342 |
| band_0.15 | SPY-IC | 5 | +7.98% | 28.76 | 1,275 |
| band_0.15 | QQQ-PS | 6 | +7.39% | 46.63 | 1,896 |
| band_0.15 | QQQ-IC | 2 | — | — | 940.20 |
| wing_1.5 | SPY-PS | 7 | +8.09% | 34.17 | 1,333 |
| wing_1.5 | SPY-IC | 7 | +5.69% | 1.23 | 912.59 |
| wing_1.5 | QQQ-PS | 7 | +9.96% | 32.15 | 1,436 |
| wing_1.5 | QQQ-IC | 7 | +16.89% | 47.48 | 2,310 |


## Go / no-go (DESIGN/80 §6.7; t >= 2.0; read 2026-12-01)

| sleeve | n_proxy | mean_proxy | nw_t_proxy | bh_pass | mean_p1 | mean_p2 | mean_p3 | n_marked | mean_marked | gap_ror | worst_over_median | deflated_sr | deflated_sr_null | forward_n | c1_proxy | c2_marked | c3_month | c4_dsr | c4_dsr_null | c5_scale | verdict | note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY-PS | 61 | +4.18% | 3.84 | yes | +2.34% | +5.14% | +5.14% | 7 | +6.02% | -0.29% | 1.64 | 0.2678 | 0.3060 | 0 | yes | yes | yes | yes | yes | no | GO-MIN | clears 1-4; one contract until the forward ledger holds >= 40 graded positions (now 0) |
| SPY-IC | 61 | +2.89% | 1.39 | no | -4.67% | +6.80% | +6.89% | 5 | +7.98% | +0.14% | 6.21 | -0.0273 | 0.0110 | 0 | no | yes | no | no | yes | no | NO-GO | fails c1_proxy, c3_month, c4_dsr |
| QQQ-PS | 59 | +4.35% | 2.44 | yes | +1.14% | +6.19% | +6.30% | 7 | +7.27% | -0.87% | 4.88 | 0.1064 | 0.1447 | 0 | yes | yes | no | yes | yes | no | NO-GO | fails c3_month |
| QQQ-IC | 59 | +2.72% | 0.7944 | no | -8.11% | +7.55% | +10.14% | 3 | +10.21% | +0.56% | 4.51 | -0.0934 | -0.0551 | 0 | no | no | no | no | no | no | NO-GO | fails c1_proxy, c2_marked, c3_month, c4_dsr |


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
