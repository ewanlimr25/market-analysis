# S-C backtest report (generated)


## Inputs

- entries: ['2026-03-13', '2026-03-20', '2026-03-27', '2026-05-01', '2026-05-08', '2026-05-15', '2026-05-22', '2026-05-29', '2026-06-05', '2026-06-12', '2026-06-18', '2026-06-26', '2026-07-02', '2026-07-10', '2026-07-17', '2026-07-24', '2026-07-31', '2026-08-07', '2026-08-14', '2026-08-21', '2026-08-28', '2026-09-04', '2026-09-11', '2026-09-18', '2026-09-25', '2026-10-02', '2026-10-09']
- n_weeks: 27
- prices_through: 2026-10-09
- sb_open: data/backtest/sb_marked.parquet (36 positions)
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
| C1-SS | M | 73 | 18 | +7.74% | +7.16% | +72.22% | 2.46 | 0.0251 | 10,600 | +0.86% |
| C1-IB | M | 73 | 18 | +10.79% | +9.12% | +66.67% | 2.30 | 0.0346 | 7,724 | +2.12% |
| C2-SS | M | 68 | 17 | +7.63% | +5.41% | +76.47% | 3.34 | 0.0042 | 8,614 | +0.92% |
| C2-IB | M | 68 | 17 | +9.85% | +6.02% | +70.59% | 2.51 | 0.0231 | 5,549 | +2.16% |
| C1-SS | pooled | 73 | 18 | +7.74% | +7.16% | +72.22% | 2.46 | 0.0251 | 10,600 | +0.86% |
| C1-IB | pooled | 73 | 18 | +10.79% | +9.12% | +66.67% | 2.30 | 0.0346 | 7,724 | +2.12% |
| C2-SS | pooled | 68 | 17 | +7.63% | +5.41% | +76.47% | 3.34 | 0.0042 | 8,614 | +0.92% |
| C2-IB | pooled | 68 | 17 | +9.85% | +6.02% | +70.59% | 2.51 | 0.0231 | 5,549 | +2.16% |


## BH(0.10) across the four pairs (pooled; descriptive before the read)

| pair | weeks | mean_ror | nw_t | nw_p | bh_pass |
|---|---|---|---|---|---|
| C1-SS | 18 | +7.74% | 2.46 | 0.0251 | yes |
| C1-IB | 18 | +10.79% | 2.30 | 0.0346 | yes |
| C2-SS | 17 | +7.63% | 3.34 | 0.0042 | yes |
| C2-IB | 17 | +9.85% | 2.51 | 0.0231 | yes |


## Deflated Sharpe (6 trials, weekly series, pooled)

| pair | n | sr | sr_star | deflated_sr | dsr_prob | sr_star_null | deflated_sr_null | dsr_prob_null | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|
| C1-SS | 18 | 0.6474 | 0.1074 | 0.5401 | 0.9828 | 0.3153 | 0.3321 | 0.9033 | 0.0249 | 2.19 |
| C1-IB | 18 | 0.5756 | 0.1074 | 0.4683 | 0.9792 | 0.3153 | 0.2603 | 0.8713 | 0.2929 | 1.81 |
| C2-SS | 17 | 0.7476 | 0.1074 | 0.6402 | 0.9950 | 0.3153 | 0.4322 | 0.9590 | 0.3000 | 2.52 |
| C2-IB | 17 | 0.5709 | 0.1074 | 0.4636 | 0.9727 | 0.3153 | 0.2556 | 0.8553 | 0.3117 | 2.34 |


## PBO (CSCV over entry-week blocks; descriptive)

- pbo: 0.6714285714285714
- mean_logit: -0.19506399438061212
- n_combinations: 70
- n_configs: 4
- n_blocks: 8
- n_weeks: 18


## Month rule (net $ by expiry month at the frozen sizing, pooled)

| pair | n_months | median_month_usd | worst_month | worst_month_usd | worst_over_median | months_negative | month_rule_pass |
|---|---|---|---|---|---|---|---|
| C1-SS | 7 | 1,069 | 2026-08 | -499.67 | 0.4675 | 1 | yes |
| C1-IB | 7 | 932.48 | 2026-08 | -521.42 | 0.5592 | 2 | yes |
| C2-SS | 7 | 879.60 | 2026-09 | -2,976 | 3.38 | 1 | no |
| C2-IB | 7 | 757.16 | 2026-09 | -3,629 | 4.79 | 2 | no |


## Tail (pooled)

| pair | n | mean_ror | worst_ror | best_ror | worst_decile_share_of_loss | realized_stress | mean_without_worst_1pct | skew |
|---|---|---|---|---|---|---|---|---|
| C1-SS | 73 | +4.77% | -81.91% | +35.76% | +61.70% | 0 | +5.97% | -1.14 |
| C1-IB | 73 | +5.36% | -102.63% | +60.59% | +52.55% | 0 | +6.86% | -0.7166 |
| C2-SS | 68 | +4.41% | -51.61% | +33.01% | +52.85% | 0 | +5.25% | -0.7366 |
| C2-IB | 68 | +4.01% | -102.04% | +55.49% | +46.35% | 0 | +5.59% | -0.6122 |

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
| C1-SS | T1 | 23 | 14 | +6.73% |
| C1-SS | T2 | 25 | 14 | +2.48% |
| C1-SS | T3 | 25 | 11 | +5.26% |
| C1-IB | T1 | 23 | 14 | +9.09% |
| C1-IB | T2 | 25 | 14 | +1.39% |
| C1-IB | T3 | 25 | 11 | +5.91% |
| C2-SS | T1 | 24 | 13 | +6.14% |
| C2-SS | T2 | 22 | 11 | +5.69% |
| C2-SS | T3 | 22 | 10 | +1.24% |
| C2-IB | T1 | 24 | 13 | +5.89% |
| C2-IB | T2 | 22 | 11 | +7.31% |
| C2-IB | T3 | 22 | 10 | -1.35% |


## Stratum: iv_tercile (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | T1 | 23 | 11 | +6.60% |
| C1-SS | T2 | 22 | 13 | +4.26% |
| C1-SS | T3 | 28 | 9 | +3.67% |
| C1-IB | T1 | 23 | 11 | +9.44% |
| C1-IB | T2 | 22 | 13 | +3.20% |
| C1-IB | T3 | 28 | 9 | +3.72% |
| C2-SS | T1 | 24 | 12 | +7.09% |
| C2-SS | T2 | 25 | 13 | +2.30% |
| C2-SS | T3 | 19 | 7 | +3.80% |
| C2-IB | T1 | 24 | 12 | +9.61% |
| C2-IB | T2 | 25 | 13 | -0.36% |
| C2-IB | T3 | 19 | 7 | +2.68% |


## Stratum: sector (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | Basic Materials | 10 | 9 | +2.94% |
| C1-SS | Communication Services | 3 | 3 | -12.50% |
| C1-SS | Consumer Cyclical | 15 | 11 | +8.20% |
| C1-SS | Consumer Defensive | 5 | 5 | +1.08% |
| C1-SS | Energy | 3 | 3 | +1.96% |
| C1-SS | Financial Services | 5 | 3 | +4.07% |
| C1-SS | Healthcare | 2 | 2 | -12.95% |
| C1-SS | Industrials | 10 | 7 | +11.46% |
| C1-SS | Real Estate | 1 | 1 | +17.43% |
| C1-SS | Technology | 17 | 9 | +2.75% |
| C1-SS | Utilities | 2 | 2 | +24.41% |
| C1-IB | Basic Materials | 10 | 9 | +0.94% |
| C1-IB | Communication Services | 3 | 3 | -18.48% |
| C1-IB | Consumer Cyclical | 15 | 11 | +9.38% |
| C1-IB | Consumer Defensive | 5 | 5 | +3.53% |
| C1-IB | Energy | 3 | 3 | -1.40% |
| C1-IB | Financial Services | 5 | 3 | +3.93% |
| C1-IB | Healthcare | 2 | 2 | -26.34% |
| C1-IB | Industrials | 10 | 7 | +15.88% |
| C1-IB | Real Estate | 1 | 1 | +19.86% |
| C1-IB | Technology | 17 | 9 | +3.53% |
| C1-IB | Utilities | 2 | 2 | +38.95% |
| C2-SS | Basic Materials | 16 | 11 | +2.51% |
| C2-SS | Communication Services | 3 | 3 | -12.50% |
| C2-SS | Consumer Cyclical | 17 | 11 | +5.67% |
| C2-SS | Consumer Defensive | 5 | 5 | +1.08% |
| C2-SS | Energy | 4 | 3 | +4.97% |
| C2-SS | Financial Services | 6 | 4 | +1.89% |
| C2-SS | Healthcare | 3 | 3 | -0.54% |
| C2-SS | Industrials | 11 | 7 | +9.05% |
| C2-SS | Real Estate | 1 | 1 | +17.43% |
| C2-SS | Utilities | 2 | 2 | +24.41% |
| C2-IB | Basic Materials | 16 | 11 | +0.36% |
| C2-IB | Communication Services | 3 | 3 | -18.48% |
| C2-IB | Consumer Cyclical | 17 | 11 | +4.46% |
| C2-IB | Consumer Defensive | 5 | 5 | +3.53% |
| C2-IB | Energy | 4 | 3 | +4.18% |
| C2-IB | Financial Services | 6 | 4 | -0.25% |
| C2-IB | Healthcare | 3 | 3 | -4.81% |
| C2-IB | Industrials | 11 | 7 | +11.83% |
| C2-IB | Real Estate | 1 | 1 | +19.86% |
| C2-IB | Utilities | 2 | 2 | +38.95% |


## Stratum: regime (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | CHOP | 48 | 10 | +7.04% |
| C1-SS | PULLBACK | 19 | 5 | -1.30% |
| C1-SS | UPTREND | 6 | 3 | +5.83% |
| C1-IB | CHOP | 48 | 10 | +9.21% |
| C1-IB | PULLBACK | 19 | 5 | -4.50% |
| C1-IB | UPTREND | 6 | 3 | +5.80% |
| C2-SS | CHOP | 46 | 9 | +2.69% |
| C2-SS | PULLBACK | 17 | 5 | +9.63% |
| C2-SS | UPTREND | 5 | 3 | +2.45% |
| C2-IB | CHOP | 46 | 9 | +1.41% |
| C2-IB | PULLBACK | 17 | 5 | +12.35% |
| C2-IB | UPTREND | 5 | 3 | -0.50% |


## Stratum: sb_gate (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | OFF:G1 | 5 | 2 | +6.19% |
| C1-SS | OFF:G2 | 24 | 8 | +8.69% |
| C1-SS | ON | 44 | 8 | +2.47% |
| C1-IB | OFF:G1 | 5 | 2 | +7.59% |
| C1-IB | OFF:G2 | 24 | 8 | +11.28% |
| C1-IB | ON | 44 | 8 | +1.88% |
| C2-SS | OFF:G1 | 4 | 2 | +10.69% |
| C2-SS | OFF:G2 | 21 | 7 | +5.79% |
| C2-SS | ON | 43 | 8 | +3.15% |
| C2-IB | OFF:G1 | 4 | 2 | +14.50% |
| C2-IB | OFF:G2 | 21 | 7 | +6.39% |
| C2-IB | ON | 43 | 8 | +1.87% |


## Stratum: month (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | 2026-03 | 15 | 3 | -0.64% |
| C1-SS | 2026-05 | 16 | 4 | +9.43% |
| C1-SS | 2026-06 | 16 | 4 | +6.10% |
| C1-SS | 2026-07 | 6 | 2 | -11.72% |
| C1-SS | 2026-08 | 15 | 3 | +5.72% |
| C1-SS | 2026-09 | 5 | 2 | +18.80% |
| C1-IB | 2026-03 | 15 | 3 | -5.67% |
| C1-IB | 2026-05 | 16 | 4 | +12.80% |
| C1-IB | 2026-06 | 16 | 4 | +7.96% |
| C1-IB | 2026-07 | 6 | 2 | -13.64% |
| C1-IB | 2026-08 | 15 | 3 | +5.37% |
| C1-IB | 2026-09 | 5 | 2 | +29.15% |
| C2-SS | 2026-03 | 14 | 3 | +6.92% |
| C2-SS | 2026-05 | 15 | 4 | +8.06% |
| C2-SS | 2026-06 | 15 | 3 | +5.26% |
| C2-SS | 2026-07 | 5 | 2 | +2.32% |
| C2-SS | 2026-08 | 15 | 3 | -4.62% |
| C2-SS | 2026-09 | 4 | 2 | +15.21% |
| C2-IB | 2026-03 | 14 | 3 | +7.70% |
| C2-IB | 2026-05 | 15 | 4 | +10.44% |
| C2-IB | 2026-06 | 15 | 3 | +6.80% |
| C2-IB | 2026-07 | 5 | 2 | +4.16% |
| C2-IB | 2026-08 | 15 | 3 | -13.95% |
| C2-IB | 2026-09 | 4 | 2 | +23.63% |


## Funnel: suppressed names by first failing filter (all weeks)

| variant | reason | n |
|---|---|---|
| C1 | F10 | 43 |
| C2 | C2_sector | 33 |
| C2 | F10 | 17 |
| all | F1 | 69183 |
| all | F2 | 28393 |
| all | F3 | 27629 |
| all | F4 | 20545 |
| all | F5 | 3129 |
| all | F6 | 3270 |
| all | F7 | 7253 |
| all | F8 | 8812 |
| all | F9 | 269 |


## Go / no-go (DESIGN/90 §6; forward t >= 2.0; criterion 4 on the null benchmark)

| pair | variant | structure | forward_weeks | required | status | scale_required | verdict | note |
|---|---|---|---|---|---|---|---|---|
| C1-SS | C1 | SS | 0 | 40 | NOT DUE | 80 | NOT DUE | 0 of 40 graded forward entry-weeks |
| C1-IB | C1 | IB | 0 | 40 | NOT DUE | 80 | NOT DUE | 0 of 40 graded forward entry-weeks |
| C2-SS | C2 | SS | 0 | 40 | NOT DUE | 80 | NOT DUE | 0 of 40 graded forward entry-weeks |
| C2-IB | C2 | IB | 0 | 40 | NOT DUE | 80 | NOT DUE | 0 of 40 graded forward entry-weeks |
