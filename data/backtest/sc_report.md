# S-C backtest report (generated)


## Inputs

- entries: ['2026-03-13', '2026-03-20', '2026-03-27', '2026-05-01', '2026-05-08', '2026-05-15', '2026-05-22', '2026-05-29', '2026-06-05', '2026-06-12', '2026-06-18', '2026-06-26', '2026-07-02', '2026-07-10', '2026-07-17', '2026-07-24', '2026-07-31', '2026-08-07', '2026-08-14', '2026-08-21', '2026-08-28', '2026-09-04', '2026-09-11', '2026-09-18', '2026-09-25']
- n_weeks: 25
- prices_through: 2026-09-25
- sb_open: /Users/ewan/Development/market-analysis/data/backtest/sb_marked.parquet (27 positions)
- params: {'price_min': 10.0, 'mcap_min': 1000000000.0, 'mcap_max': 20000000000.0, 'adv_min': 50000000.0, 'iv30d_min': 0.3, 'iv30d_max': 0.8, 'dte_cal_min': 20, 'dte_cal_max': 40, 'target_dte_cal': 28, 'atm_band': 0.025, 'leg_size_min': 5, 'spread_max': 0.08, 'select_n': 10, 'c2_excluded_sectors': ['Technology'], 'wing_sigma': 2.0, 'stress_sigma': 3.0}


## Count trigger (read at 40 graded forward entry-weeks per pair)

| pair | forward_weeks | required | status | scale_required |
|---|---|---|---|---|
| C1-SS | 0 | 40 | NOT DUE | 80 |
| C1-IB | 0 | 40 | NOT DUE | 80 |
| C2-SS | 0 | 40 | NOT DUE | 80 |
| C2-IB | 0 | 40 | NOT DUE | 80 |


## Mean net return on risk, entry-week series; NW(lag 4) t

| pair | window | n | weeks | mean_ror | median_ror | hit | nw_t | nw_p | net_usd_total | mean_cost_ror |
|---|---|---|---|---|---|---|---|---|---|---|
| C1-SS | M | 68 | 16 | +6.22% | +4.60% | +68.75% | 1.76 | 0.0983 | 8,913 | +0.84% |
| C1-IB | M | 68 | 16 | +8.28% | +4.80% | +62.50% | 1.54 | 0.1438 | 6,274 | +2.08% |
| C2-SS | M | 64 | 15 | +6.70% | +5.36% | +73.33% | 2.36 | 0.0332 | 7,735 | +0.90% |
| C2-IB | M | 64 | 15 | +8.15% | +5.17% | +66.67% | 1.65 | 0.1213 | 4,792 | +2.11% |
| C1-SS | pooled | 68 | 16 | +6.22% | +4.60% | +68.75% | 1.76 | 0.0983 | 8,913 | +0.84% |
| C1-IB | pooled | 68 | 16 | +8.28% | +4.80% | +62.50% | 1.54 | 0.1438 | 6,274 | +2.08% |
| C2-SS | pooled | 64 | 15 | +6.70% | +5.36% | +73.33% | 2.36 | 0.0332 | 7,735 | +0.90% |
| C2-IB | pooled | 64 | 15 | +8.15% | +5.17% | +66.67% | 1.65 | 0.1213 | 4,792 | +2.11% |


## BH(0.10) across the four pairs (pooled; descriptive before the read)

| pair | weeks | mean_ror | nw_t | nw_p | bh_pass |
|---|---|---|---|---|---|
| C1-SS | 16 | +6.22% | 1.76 | 0.0983 | no |
| C1-IB | 16 | +8.28% | 1.54 | 0.1438 | no |
| C2-SS | 15 | +6.70% | 2.36 | 0.0332 | no |
| C2-IB | 15 | +8.15% | 1.65 | 0.1213 | no |


## Deflated Sharpe (6 trials, weekly series, pooled)

| pair | n | sr | sr_star | deflated_sr | dsr_prob | sr_star_null | deflated_sr_null | dsr_prob_null | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|
| C1-SS | 16 | 0.5269 | 0.1109 | 0.4160 | 0.9500 | 0.3357 | 0.1912 | 0.7751 | 0.2747 | 2.51 |
| C1-IB | 16 | 0.4508 | 0.1109 | 0.3399 | 0.9301 | 0.3357 | 0.1151 | 0.6915 | 0.6005 | 2.29 |
| C2-SS | 15 | 0.6361 | 0.1109 | 0.5252 | 0.9853 | 0.3357 | 0.3004 | 0.8936 | 0.5715 | 2.76 |
| C2-IB | 15 | 0.4607 | 0.1109 | 0.3498 | 0.9270 | 0.3357 | 0.1250 | 0.6983 | 0.6021 | 2.65 |


## PBO (CSCV over entry-week blocks; descriptive)

- pbo: 0.6571428571428571
- mean_logit: -0.08539635170492044
- n_combinations: 70
- n_configs: 4
- n_blocks: 8
- n_weeks: 16


## Month rule (net $ by expiry month at the frozen sizing, pooled)

| pair | n_months | median_month_usd | worst_month | worst_month_usd | worst_over_median | months_negative | month_rule_pass |
|---|---|---|---|---|---|---|---|
| C1-SS | 6 | 1,540 | 2026-08 | -499.67 | 0.3245 | 1 | yes |
| C1-IB | 6 | 1,138 | 2026-08 | -521.42 | 0.4583 | 2 | yes |
| C2-SS | 6 | 1,144 | 2026-09 | -2,976 | 2.60 | 1 | yes |
| C2-IB | 6 | 906.69 | 2026-09 | -3,629 | 4.00 | 2 | no |


## Tail (pooled)

| pair | n | mean_ror | worst_ror | best_ror | worst_decile_share_of_loss | realized_stress | mean_without_worst_1pct | skew |
|---|---|---|---|---|---|---|---|---|
| C1-SS | 68 | +3.64% | -81.91% | +35.76% | +58.64% | 0 | +4.91% | -1.10 |
| C1-IB | 68 | +3.45% | -102.63% | +60.59% | +49.39% | 0 | +5.03% | -0.6604 |
| C2-SS | 64 | +3.73% | -51.61% | +33.01% | +53.45% | 0 | +4.61% | -0.6958 |
| C2-IB | 64 | +2.78% | -102.04% | +55.49% | +47.00% | 0 | +4.44% | -0.5728 |

Worst 10 positions, C1-SS:

| ticker | entry | expiry | ror | net_usd |
|---|---|---|---|---|
| PATH | 2026-07-24 | 2026-08-21 | -81.91% | -766.11 |
| U | 2026-03-20 | 2026-04-17 | -52.04% | -488.31 |
| FOXA | 2026-06-26 | 2026-07-17 | -51.61% | -434.26 |
| ARWR | 2026-08-28 | 2026-09-18 | -50.88% | -1,073 |
| GIS | 2026-07-31 | 2026-08-21 | -39.98% | -274.06 |
| FLR | 2026-05-15 | 2026-06-18 | -26.79% | -373.69 |
| IREN | 2026-08-28 | 2026-09-25 | -19.09% | -329.80 |
| CORZ | 2026-03-20 | 2026-04-17 | -15.92% | -121.06 |
| RIVN | 2026-05-22 | 2026-06-18 | -15.33% | -81.06 |
| CELH | 2026-03-20 | 2026-04-17 | -15.26% | -224.21 |

Worst 10 positions, C1-IB:

| ticker | entry | expiry | ror | net_usd |
|---|---|---|---|---|
| PATH | 2026-07-24 | 2026-08-21 | -102.63% | -509.05 |
| U | 2026-03-20 | 2026-04-17 | -100.15% | -514.88 |
| ARWR | 2026-08-28 | 2026-09-18 | -90.21% | -1,100 |
| FOXA | 2026-06-26 | 2026-07-17 | -66.44% | -447.50 |
| GIS | 2026-07-31 | 2026-08-21 | -54.48% | -291.92 |
| FLR | 2026-05-15 | 2026-06-18 | -52.21% | -400.60 |
| IREN | 2026-08-28 | 2026-09-25 | -36.46% | -377.32 |
| CELH | 2026-03-20 | 2026-04-17 | -32.97% | -249.81 |
| CORZ | 2026-03-20 | 2026-04-17 | -32.69% | -146.05 |
| CRCL | 2026-06-18 | 2026-07-17 | -31.26% | -686.39 |

Worst 10 positions, C2-SS:

| ticker | entry | expiry | ror | net_usd |
|---|---|---|---|---|
| FOXA | 2026-06-26 | 2026-07-17 | -51.61% | -434.26 |
| ARWR | 2026-08-28 | 2026-09-18 | -50.88% | -1,073 |
| BROS | 2026-08-21 | 2026-09-18 | -50.52% | -584.48 |
| GIS | 2026-07-31 | 2026-08-21 | -39.98% | -274.06 |
| ALB | 2026-08-21 | 2026-09-18 | -30.94% | -1,409 |
| FLR | 2026-05-15 | 2026-06-18 | -26.79% | -373.69 |
| MP | 2026-06-18 | 2026-07-17 | -21.34% | -573.21 |
| IREN | 2026-08-28 | 2026-09-25 | -19.09% | -329.80 |
| RIVN | 2026-05-22 | 2026-06-18 | -15.33% | -81.06 |
| CELH | 2026-03-20 | 2026-04-17 | -15.26% | -224.21 |

Worst 10 positions, C2-IB:

| ticker | entry | expiry | ror | net_usd |
|---|---|---|---|---|
| BROS | 2026-08-21 | 2026-09-18 | -102.04% | -614.23 |
| ARWR | 2026-08-28 | 2026-09-18 | -90.21% | -1,100 |
| FOXA | 2026-06-26 | 2026-07-17 | -66.44% | -447.50 |
| ALB | 2026-08-21 | 2026-09-18 | -59.76% | -1,544 |
| GIS | 2026-07-31 | 2026-08-21 | -54.48% | -291.92 |
| FLR | 2026-05-15 | 2026-06-18 | -52.21% | -400.60 |
| MP | 2026-06-18 | 2026-07-17 | -38.47% | -622.17 |
| IREN | 2026-08-28 | 2026-09-25 | -36.46% | -377.32 |
| CELH | 2026-03-20 | 2026-04-17 | -32.97% | -249.81 |
| CRCL | 2026-06-18 | 2026-07-17 | -31.26% | -686.39 |


## Stratum: cap_tercile (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | T1 | 22 | 12 | +2.11% |
| C1-SS | T2 | 23 | 13 | +4.21% |
| C1-SS | T3 | 23 | 10 | +4.52% |
| C1-IB | T1 | 22 | 12 | +1.01% |
| C1-IB | T2 | 23 | 13 | +4.53% |
| C1-IB | T3 | 23 | 10 | +4.71% |
| C2-SS | T1 | 22 | 12 | +5.83% |
| C2-SS | T2 | 21 | 10 | +4.61% |
| C2-SS | T3 | 21 | 9 | +0.67% |
| C2-IB | T1 | 22 | 12 | +5.29% |
| C2-IB | T2 | 21 | 10 | +5.32% |
| C2-IB | T3 | 21 | 9 | -2.39% |


## Stratum: iv_tercile (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | T1 | 22 | 9 | +2.69% |
| C1-SS | T2 | 20 | 12 | +6.41% |
| C1-SS | T3 | 26 | 8 | +2.31% |
| C1-IB | T1 | 22 | 9 | +2.61% |
| C1-IB | T2 | 20 | 12 | +6.79% |
| C1-IB | T3 | 26 | 8 | +1.60% |
| C2-SS | T1 | 22 | 10 | +5.83% |
| C2-SS | T2 | 24 | 13 | +1.72% |
| C2-SS | T3 | 18 | 7 | +3.86% |
| C2-IB | T1 | 22 | 10 | +7.33% |
| C2-IB | T2 | 24 | 13 | -1.41% |
| C2-IB | T3 | 18 | 7 | +2.81% |


## Stratum: sector (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | Basic Materials | 10 | 9 | +4.19% |
| C1-SS | Communication Services | 3 | 3 | -12.50% |
| C1-SS | Consumer Cyclical | 14 | 10 | +7.83% |
| C1-SS | Consumer Defensive | 5 | 5 | +1.08% |
| C1-SS | Energy | 3 | 3 | +1.96% |
| C1-SS | Financial Services | 5 | 3 | +4.07% |
| C1-SS | Healthcare | 2 | 2 | -12.95% |
| C1-SS | Industrials | 9 | 6 | +9.59% |
| C1-SS | Real Estate | 1 | 1 | +17.43% |
| C1-SS | Technology | 15 | 8 | -0.04% |
| C1-SS | Utilities | 1 | 1 | +24.41% |
| C1-IB | Basic Materials | 10 | 9 | +3.00% |
| C1-IB | Communication Services | 3 | 3 | -18.48% |
| C1-IB | Consumer Cyclical | 14 | 10 | +8.59% |
| C1-IB | Consumer Defensive | 5 | 5 | +3.53% |
| C1-IB | Energy | 3 | 3 | -1.40% |
| C1-IB | Financial Services | 5 | 3 | +3.93% |
| C1-IB | Healthcare | 2 | 2 | -26.34% |
| C1-IB | Industrials | 9 | 6 | +12.20% |
| C1-IB | Real Estate | 1 | 1 | +19.86% |
| C1-IB | Technology | 15 | 8 | -0.69% |
| C1-IB | Utilities | 1 | 1 | +40.15% |
| C2-SS | Basic Materials | 15 | 10 | +3.03% |
| C2-SS | Communication Services | 3 | 3 | -12.50% |
| C2-SS | Consumer Cyclical | 16 | 10 | +5.18% |
| C2-SS | Consumer Defensive | 5 | 5 | +1.08% |
| C2-SS | Energy | 4 | 3 | +4.97% |
| C2-SS | Financial Services | 6 | 4 | +1.89% |
| C2-SS | Healthcare | 3 | 3 | -0.54% |
| C2-SS | Industrials | 10 | 6 | +7.12% |
| C2-SS | Real Estate | 1 | 1 | +17.43% |
| C2-SS | Utilities | 1 | 1 | +24.41% |
| C2-IB | Basic Materials | 15 | 10 | +1.23% |
| C2-IB | Communication Services | 3 | 3 | -18.48% |
| C2-IB | Consumer Cyclical | 16 | 10 | +3.46% |
| C2-IB | Consumer Defensive | 5 | 5 | +3.53% |
| C2-IB | Energy | 4 | 3 | +4.18% |
| C2-IB | Financial Services | 6 | 4 | -0.25% |
| C2-IB | Healthcare | 3 | 3 | -4.81% |
| C2-IB | Industrials | 10 | 6 | +8.11% |
| C2-IB | Real Estate | 1 | 1 | +19.86% |
| C2-IB | Utilities | 1 | 1 | +40.15% |


## Stratum: regime (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | CHOP | 43 | 8 | +5.51% |
| C1-SS | PULLBACK | 19 | 5 | -1.30% |
| C1-SS | UPTREND | 6 | 3 | +5.83% |
| C1-IB | CHOP | 43 | 8 | +6.63% |
| C1-IB | PULLBACK | 19 | 5 | -4.50% |
| C1-IB | UPTREND | 6 | 3 | +5.80% |
| C2-SS | CHOP | 42 | 7 | +1.50% |
| C2-SS | PULLBACK | 17 | 5 | +9.63% |
| C2-SS | UPTREND | 5 | 3 | +2.45% |
| C2-IB | CHOP | 42 | 7 | -0.70% |
| C2-IB | PULLBACK | 17 | 5 | +12.35% |
| C2-IB | UPTREND | 5 | 3 | -0.50% |


## Stratum: sb_gate (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | OFF:G1 | 5 | 2 | +6.19% |
| C1-SS | OFF:G2 | 22 | 7 | +7.36% |
| C1-SS | ON | 41 | 7 | +1.33% |
| C1-IB | OFF:G1 | 5 | 2 | +7.59% |
| C1-IB | OFF:G2 | 22 | 7 | +9.05% |
| C1-IB | ON | 41 | 7 | -0.06% |
| C2-SS | OFF:G1 | 4 | 2 | +10.69% |
| C2-SS | OFF:G2 | 20 | 6 | +5.41% |
| C2-SS | ON | 40 | 7 | +2.20% |
| C2-IB | OFF:G1 | 4 | 2 | +14.50% |
| C2-IB | OFF:G2 | 20 | 6 | +5.69% |
| C2-IB | ON | 40 | 7 | +0.16% |


## Stratum: month (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | 2026-03 | 15 | 3 | -0.64% |
| C1-SS | 2026-05 | 16 | 4 | +9.43% |
| C1-SS | 2026-06 | 16 | 4 | +5.66% |
| C1-SS | 2026-07 | 6 | 2 | -11.72% |
| C1-SS | 2026-08 | 15 | 3 | +5.72% |
| C1-IB | 2026-03 | 15 | 3 | -5.67% |
| C1-IB | 2026-05 | 16 | 4 | +12.80% |
| C1-IB | 2026-06 | 16 | 4 | +7.26% |
| C1-IB | 2026-07 | 6 | 2 | -13.64% |
| C1-IB | 2026-08 | 15 | 3 | +5.37% |
| C2-SS | 2026-03 | 14 | 3 | +6.92% |
| C2-SS | 2026-05 | 15 | 4 | +8.06% |
| C2-SS | 2026-06 | 15 | 3 | +5.26% |
| C2-SS | 2026-07 | 5 | 2 | +2.32% |
| C2-SS | 2026-08 | 15 | 3 | -4.62% |
| C2-IB | 2026-03 | 14 | 3 | +7.70% |
| C2-IB | 2026-05 | 15 | 4 | +10.44% |
| C2-IB | 2026-06 | 15 | 3 | +6.80% |
| C2-IB | 2026-07 | 5 | 2 | +4.16% |
| C2-IB | 2026-08 | 15 | 3 | -13.95% |


## Funnel: suppressed names by first failing filter (all weeks)

| variant | reason | n |
|---|---|---|
| C1 | F10 | 42 |
| C2 | C2_sector | 31 |
| C2 | F10 | 17 |
| all | F1 | 63899 |
| all | F2 | 26252 |
| all | F3 | 25640 |
| all | F4 | 19071 |
| all | F5 | 2987 |
| all | F6 | 3245 |
| all | F7 | 5878 |
| all | F8 | 8658 |
| all | F9 | 259 |


## Go / no-go (DESIGN/90 §6; forward t >= 2.0; criterion 4 on the null benchmark)

| pair | variant | structure | forward_weeks | required | status | scale_required | verdict | note |
|---|---|---|---|---|---|---|---|---|
| C1-SS | C1 | SS | 0 | 40 | NOT DUE | 80 | NOT DUE | 0 of 40 graded forward entry-weeks |
| C1-IB | C1 | IB | 0 | 40 | NOT DUE | 80 | NOT DUE | 0 of 40 graded forward entry-weeks |
| C2-SS | C2 | SS | 0 | 40 | NOT DUE | 80 | NOT DUE | 0 of 40 graded forward entry-weeks |
| C2-IB | C2 | IB | 0 | 40 | NOT DUE | 80 | NOT DUE | 0 of 40 graded forward entry-weeks |
