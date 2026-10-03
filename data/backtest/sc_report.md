# S-C backtest report (generated)


## Inputs

- entries: ['2026-03-13', '2026-03-20', '2026-03-27', '2026-05-01', '2026-05-08', '2026-05-15', '2026-05-22', '2026-05-29', '2026-06-05', '2026-06-12', '2026-06-18', '2026-06-26', '2026-07-02', '2026-07-10', '2026-07-17', '2026-07-24', '2026-07-31', '2026-08-07', '2026-08-14', '2026-08-21', '2026-08-28', '2026-09-04', '2026-09-11', '2026-09-18', '2026-09-25', '2026-10-02']
- n_weeks: 26
- prices_through: 2026-10-02
- sb_open: /Users/ewan/Development/market-analysis/data/backtest/sb_marked.parquet (35 positions)
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
| C1-SS | M | 70 | 17 | +7.23% | +5.06% | +70.59% | 2.22 | 0.0410 | 9,437 | +0.85% |
| C1-IB | M | 70 | 17 | +9.90% | +5.88% | +64.71% | 2.05 | 0.0573 | 6,739 | +2.09% |
| C2-SS | M | 65 | 16 | +7.12% | +5.39% | +75.00% | 2.88 | 0.0115 | 8,070 | +0.90% |
| C2-IB | M | 65 | 16 | +8.92% | +5.59% | +68.75% | 2.09 | 0.0539 | 5,082 | +2.12% |
| C1-SS | pooled | 70 | 17 | +7.23% | +5.06% | +70.59% | 2.22 | 0.0410 | 9,437 | +0.85% |
| C1-IB | pooled | 70 | 17 | +9.90% | +5.88% | +64.71% | 2.05 | 0.0573 | 6,739 | +2.09% |
| C2-SS | pooled | 65 | 16 | +7.12% | +5.39% | +75.00% | 2.88 | 0.0115 | 8,070 | +0.90% |
| C2-IB | pooled | 65 | 16 | +8.92% | +5.59% | +68.75% | 2.09 | 0.0539 | 5,082 | +2.12% |


## BH(0.10) across the four pairs (pooled; descriptive before the read)

| pair | weeks | mean_ror | nw_t | nw_p | bh_pass |
|---|---|---|---|---|---|
| C1-SS | 17 | +7.23% | 2.22 | 0.0410 | yes |
| C1-IB | 17 | +9.90% | 2.05 | 0.0573 | yes |
| C2-SS | 16 | +7.12% | 2.88 | 0.0115 | yes |
| C2-IB | 16 | +8.92% | 2.09 | 0.0539 | yes |


## Deflated Sharpe (6 trials, weekly series, pooled)

| pair | n | sr | sr_star | deflated_sr | dsr_prob | sr_star_null | deflated_sr_null | dsr_prob_null | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|
| C1-SS | 17 | 0.5942 | 0.1068 | 0.4875 | 0.9734 | 0.3250 | 0.2692 | 0.8572 | 0.1481 | 2.19 |
| C1-IB | 17 | 0.5211 | 0.1068 | 0.4144 | 0.9650 | 0.3250 | 0.1961 | 0.8045 | 0.4297 | 1.89 |
| C2-SS | 16 | 0.6902 | 0.1068 | 0.5834 | 0.9916 | 0.3250 | 0.3652 | 0.9328 | 0.4449 | 2.68 |
| C2-IB | 16 | 0.5135 | 0.1068 | 0.4067 | 0.9551 | 0.3250 | 0.1885 | 0.7841 | 0.4640 | 2.53 |


## PBO (CSCV over entry-week blocks; descriptive)

- pbo: 0.6142857142857143
- mean_logit: -0.03663035310976745
- n_combinations: 70
- n_configs: 4
- n_blocks: 8
- n_weeks: 17


## Month rule (net $ by expiry month at the frozen sizing, pooled)

| pair | n_months | median_month_usd | worst_month | worst_month_usd | worst_over_median | months_negative | month_rule_pass |
|---|---|---|---|---|---|---|---|
| C1-SS | 7 | 861.02 | 2026-08 | -499.67 | 0.5803 | 1 | yes |
| C1-IB | 7 | 743.03 | 2026-08 | -521.42 | 0.7018 | 2 | yes |
| C2-SS | 7 | 861.02 | 2026-09 | -2,976 | 3.46 | 1 | no |
| C2-IB | 7 | 743.03 | 2026-09 | -3,629 | 4.88 | 2 | no |


## Tail (pooled)

| pair | n | mean_ror | worst_ror | best_ror | worst_decile_share_of_loss | realized_stress | mean_without_worst_1pct | skew |
|---|---|---|---|---|---|---|---|---|
| C1-SS | 70 | +4.20% | -81.91% | +35.76% | +62.34% | 0 | +5.44% | -1.12 |
| C1-IB | 70 | +4.38% | -102.63% | +60.59% | +53.25% | 0 | +5.93% | -0.6895 |
| C2-SS | 65 | +3.88% | -51.61% | +33.01% | +53.45% | 0 | +4.75% | -0.7174 |
| C2-IB | 65 | +3.05% | -102.04% | +55.49% | +47.00% | 0 | +4.69% | -0.5950 |

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
| C1-SS | T1 | 23 | 13 | +3.46% |
| C1-SS | T2 | 23 | 13 | +4.21% |
| C1-SS | T3 | 24 | 11 | +4.89% |
| C1-IB | T1 | 23 | 13 | +3.19% |
| C1-IB | T2 | 23 | 13 | +4.53% |
| C1-IB | T3 | 24 | 11 | +5.36% |
| C2-SS | T1 | 22 | 12 | +5.83% |
| C2-SS | T2 | 22 | 11 | +2.08% |
| C2-SS | T3 | 21 | 10 | +3.73% |
| C2-IB | T1 | 22 | 12 | +5.29% |
| C2-IB | T2 | 22 | 11 | +0.98% |
| C2-IB | T3 | 21 | 10 | +2.88% |


## Stratum: iv_tercile (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | T1 | 22 | 10 | +5.61% |
| C1-SS | T2 | 21 | 13 | +3.68% |
| C1-SS | T3 | 27 | 9 | +3.45% |
| C1-IB | T1 | 22 | 10 | +7.64% |
| C1-IB | T2 | 21 | 13 | +2.17% |
| C1-IB | T3 | 27 | 9 | +3.44% |
| C2-SS | T1 | 23 | 11 | +6.16% |
| C2-SS | T2 | 24 | 13 | +1.72% |
| C2-SS | T3 | 18 | 7 | +3.86% |
| C2-IB | T1 | 23 | 11 | +7.90% |
| C2-IB | T2 | 24 | 13 | -1.41% |
| C2-IB | T3 | 18 | 7 | +2.81% |


## Stratum: sector (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | Basic Materials | 10 | 9 | +4.19% |
| C1-SS | Communication Services | 3 | 3 | -12.50% |
| C1-SS | Consumer Cyclical | 15 | 11 | +8.20% |
| C1-SS | Consumer Defensive | 5 | 5 | +1.08% |
| C1-SS | Energy | 3 | 3 | +1.96% |
| C1-SS | Financial Services | 5 | 3 | +4.07% |
| C1-SS | Healthcare | 2 | 2 | -12.95% |
| C1-SS | Industrials | 9 | 6 | +9.59% |
| C1-SS | Real Estate | 1 | 1 | +17.43% |
| C1-SS | Technology | 16 | 9 | +2.03% |
| C1-SS | Utilities | 1 | 1 | +24.41% |
| C1-IB | Basic Materials | 10 | 9 | +3.00% |
| C1-IB | Communication Services | 3 | 3 | -18.48% |
| C1-IB | Consumer Cyclical | 15 | 11 | +9.38% |
| C1-IB | Consumer Defensive | 5 | 5 | +3.53% |
| C1-IB | Energy | 3 | 3 | -1.40% |
| C1-IB | Financial Services | 5 | 3 | +3.93% |
| C1-IB | Healthcare | 2 | 2 | -26.34% |
| C1-IB | Industrials | 9 | 6 | +12.20% |
| C1-IB | Real Estate | 1 | 1 | +19.86% |
| C1-IB | Technology | 16 | 9 | +2.55% |
| C1-IB | Utilities | 1 | 1 | +40.15% |
| C2-SS | Basic Materials | 15 | 10 | +3.03% |
| C2-SS | Communication Services | 3 | 3 | -12.50% |
| C2-SS | Consumer Cyclical | 17 | 11 | +5.67% |
| C2-SS | Consumer Defensive | 5 | 5 | +1.08% |
| C2-SS | Energy | 4 | 3 | +4.97% |
| C2-SS | Financial Services | 6 | 4 | +1.89% |
| C2-SS | Healthcare | 3 | 3 | -0.54% |
| C2-SS | Industrials | 10 | 6 | +7.12% |
| C2-SS | Real Estate | 1 | 1 | +17.43% |
| C2-SS | Utilities | 1 | 1 | +24.41% |
| C2-IB | Basic Materials | 15 | 10 | +1.23% |
| C2-IB | Communication Services | 3 | 3 | -18.48% |
| C2-IB | Consumer Cyclical | 17 | 11 | +4.46% |
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
| C1-SS | CHOP | 45 | 9 | +6.30% |
| C1-SS | PULLBACK | 19 | 5 | -1.30% |
| C1-SS | UPTREND | 6 | 3 | +5.83% |
| C1-IB | CHOP | 45 | 9 | +7.93% |
| C1-IB | PULLBACK | 19 | 5 | -4.50% |
| C1-IB | UPTREND | 6 | 3 | +5.80% |
| C2-SS | CHOP | 43 | 8 | +1.78% |
| C2-SS | PULLBACK | 17 | 5 | +9.63% |
| C2-SS | UPTREND | 5 | 3 | +2.45% |
| C2-IB | CHOP | 43 | 8 | -0.21% |
| C2-IB | PULLBACK | 17 | 5 | +12.35% |
| C2-IB | UPTREND | 5 | 3 | -0.50% |


## Stratum: sb_gate (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | OFF:G1 | 5 | 2 | +6.19% |
| C1-SS | OFF:G2 | 24 | 8 | +8.69% |
| C1-SS | ON | 41 | 7 | +1.33% |
| C1-IB | OFF:G1 | 5 | 2 | +7.59% |
| C1-IB | OFF:G2 | 24 | 8 | +11.28% |
| C1-IB | ON | 41 | 7 | -0.06% |
| C2-SS | OFF:G1 | 4 | 2 | +10.69% |
| C2-SS | OFF:G2 | 21 | 7 | +5.79% |
| C2-SS | ON | 40 | 7 | +2.20% |
| C2-IB | OFF:G1 | 4 | 2 | +14.50% |
| C2-IB | OFF:G2 | 21 | 7 | +6.39% |
| C2-IB | ON | 40 | 7 | +0.16% |


## Stratum: month (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | 2026-03 | 15 | 3 | -0.64% |
| C1-SS | 2026-05 | 16 | 4 | +9.43% |
| C1-SS | 2026-06 | 16 | 4 | +5.66% |
| C1-SS | 2026-07 | 6 | 2 | -11.72% |
| C1-SS | 2026-08 | 15 | 3 | +5.72% |
| C1-SS | 2026-09 | 2 | 1 | +23.27% |
| C1-IB | 2026-03 | 15 | 3 | -5.67% |
| C1-IB | 2026-05 | 16 | 4 | +12.80% |
| C1-IB | 2026-06 | 16 | 4 | +7.26% |
| C1-IB | 2026-07 | 6 | 2 | -13.64% |
| C1-IB | 2026-08 | 15 | 3 | +5.37% |
| C1-IB | 2026-09 | 2 | 1 | +35.83% |
| C2-SS | 2026-03 | 14 | 3 | +6.92% |
| C2-SS | 2026-05 | 15 | 4 | +8.06% |
| C2-SS | 2026-06 | 15 | 3 | +5.26% |
| C2-SS | 2026-07 | 5 | 2 | +2.32% |
| C2-SS | 2026-08 | 15 | 3 | -4.62% |
| C2-SS | 2026-09 | 1 | 1 | +13.39% |
| C2-IB | 2026-03 | 14 | 3 | +7.70% |
| C2-IB | 2026-05 | 15 | 4 | +10.44% |
| C2-IB | 2026-06 | 15 | 3 | +6.80% |
| C2-IB | 2026-07 | 5 | 2 | +4.16% |
| C2-IB | 2026-08 | 15 | 3 | -13.95% |
| C2-IB | 2026-09 | 1 | 1 | +20.43% |


## Funnel: suppressed names by first failing filter (all weeks)

| variant | reason | n |
|---|---|---|
| C1 | F10 | 42 |
| C2 | C2_sector | 32 |
| C2 | F10 | 17 |
| all | F1 | 66536 |
| all | F2 | 27324 |
| all | F3 | 26633 |
| all | F4 | 19814 |
| all | F5 | 3024 |
| all | F6 | 3264 |
| all | F7 | 6562 |
| all | F8 | 8759 |
| all | F9 | 265 |


## Go / no-go (DESIGN/90 §6; forward t >= 2.0; criterion 4 on the null benchmark)

| pair | variant | structure | forward_weeks | required | status | scale_required | verdict | note |
|---|---|---|---|---|---|---|---|---|
| C1-SS | C1 | SS | 0 | 40 | NOT DUE | 80 | NOT DUE | 0 of 40 graded forward entry-weeks |
| C1-IB | C1 | IB | 0 | 40 | NOT DUE | 80 | NOT DUE | 0 of 40 graded forward entry-weeks |
| C2-SS | C2 | SS | 0 | 40 | NOT DUE | 80 | NOT DUE | 0 of 40 graded forward entry-weeks |
| C2-IB | C2 | IB | 0 | 40 | NOT DUE | 80 | NOT DUE | 0 of 40 graded forward entry-weeks |
