# S-C backtest report (generated)


## Inputs

- entries: ['2026-03-13', '2026-03-20', '2026-03-27', '2026-05-01', '2026-05-08', '2026-05-15', '2026-05-22', '2026-05-29', '2026-06-05', '2026-06-12', '2026-06-18', '2026-06-26', '2026-07-02', '2026-07-10', '2026-07-17', '2026-07-24', '2026-07-31', '2026-08-07', '2026-08-14', '2026-08-21', '2026-08-28', '2026-09-04', '2026-09-11', '2026-09-18', '2026-09-25', '2026-10-02', '2026-10-09', '2026-10-16', '2026-10-23', '2026-10-30', '2026-11-06']
- n_weeks: 31
- prices_through: 2026-11-06
- sb_open: data/backtest/sb_marked.parquet (46 positions)
- params: {'price_min': 10.0, 'mcap_min': 1000000000.0, 'mcap_max': 20000000000.0, 'adv_min': 50000000.0, 'iv30d_min': 0.3, 'iv30d_max': 0.8, 'dte_cal_min': 20, 'dte_cal_max': 40, 'target_dte_cal': 28, 'atm_band': 0.025, 'leg_size_min': 5, 'spread_max': 0.08, 'select_n': 10, 'c2_excluded_sectors': ['Technology'], 'wing_sigma': 2.0, 'stress_sigma': 3.0}


## Count trigger (read at 40 graded forward entry-weeks per pair)

| pair | forward_weeks | required | status | scale_required |
|---|---|---|---|---|
| C1-SS | 2 | 40 | NOT DUE | 80 |
| C1-IB | 2 | 40 | NOT DUE | 80 |
| C2-SS | 2 | 40 | NOT DUE | 80 |
| C2-IB | 2 | 40 | NOT DUE | 80 |


## Mean net return on risk, entry-week series; NW(lag 4) t

| pair | window | n | weeks | mean_ror | median_ror | hit | nw_t | nw_p | net_usd_total | mean_cost_ror |
|---|---|---|---|---|---|---|---|---|---|---|
| C1-SS | M | 93 | 22 | +1.58% | +3.56% | +63.64% | 0.2964 | 0.7698 | 8,326 | +0.83% |
| C1-IB | M | 93 | 22 | +0.11% | +2.87% | +54.55% | 0.0123 | 0.9903 | 4,936 | +2.04% |
| C2-SS | M | 86 | 21 | +0.52% | +4.17% | +66.67% | 0.0905 | 0.9288 | 6,234 | +0.89% |
| C2-IB | M | 86 | 21 | -2.34% | +4.98% | +57.14% | -0.2373 | 0.8148 | 2,726 | +2.12% |
| C1-SS | F-2026Q4 | 6 | 2 | — | — | — | — | — | -1,362 | +0.65% |
| C1-IB | F-2026Q4 | 6 | 2 | — | — | — | — | — | -1,519 | +1.46% |
| C2-SS | F-2026Q4 | 5 | 2 | — | — | — | — | — | -1,091 | +0.64% |
| C2-IB | F-2026Q4 | 5 | 2 | — | — | — | — | — | -1,236 | +1.43% |
| C1-SS | F | 6 | 2 | — | — | — | — | — | -1,362 | +0.65% |
| C1-IB | F | 6 | 2 | — | — | — | — | — | -1,519 | +1.46% |
| C2-SS | F | 5 | 2 | — | — | — | — | — | -1,091 | +0.64% |
| C2-IB | F | 5 | 2 | — | — | — | — | — | -1,236 | +1.43% |
| C1-SS | pooled | 99 | 22 | +1.58% | +3.56% | +63.64% | 0.2962 | 0.7700 | 6,963 | +0.82% |
| C1-IB | pooled | 99 | 22 | +0.11% | +2.87% | +54.55% | 0.0122 | 0.9904 | 3,417 | +2.01% |
| C2-SS | pooled | 91 | 21 | +0.52% | +4.17% | +66.67% | 0.0904 | 0.9289 | 5,143 | +0.88% |
| C2-IB | pooled | 91 | 21 | -2.34% | +4.98% | +57.14% | -0.2375 | 0.8147 | 1,490 | +2.08% |


## BH(0.10) across the four pairs (pooled; descriptive before the read)

| pair | weeks | mean_ror | nw_t | nw_p | bh_pass |
|---|---|---|---|---|---|
| C1-SS | 22 | +1.58% | 0.2962 | 0.7700 | no |
| C1-IB | 22 | +0.11% | 0.0122 | 0.9904 | no |
| C2-SS | 21 | +0.52% | 0.0904 | 0.9289 | no |
| C2-IB | 21 | -2.34% | -0.2375 | 0.8147 | no |


## Deflated Sharpe (6 trials, weekly series, pooled)

| pair | n | sr | sr_star | deflated_sr | dsr_prob | sr_star_null | deflated_sr_null | dsr_prob_null | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|
| C1-SS | 22 | 0.0856 | 0.0830 | 0.0027 | 0.5047 | 0.2837 | -0.1981 | 0.1912 | -0.8849 | 3.52 |
| C1-IB | 22 | 0.0035 | 0.0830 | -0.0794 | 0.3582 | 0.2837 | -0.2802 | 0.1000 | -1.00 | 3.89 |
| C2-SS | 21 | 0.0261 | 0.0830 | -0.0569 | 0.4016 | 0.2837 | -0.2576 | 0.1295 | -1.57 | 6.04 |
| C2-IB | 21 | -0.0688 | 0.0830 | -0.1517 | 0.2370 | 0.2837 | -0.3525 | 0.0481 | -1.57 | 5.93 |


## PBO (CSCV over entry-week blocks; descriptive)

- pbo: 0.5857142857142857
- mean_logit: 0.09863385341203922
- n_combinations: 70
- n_configs: 4
- n_blocks: 8
- n_weeks: 22


## Month rule (net $ by expiry month at the frozen sizing, pooled)

| pair | n_months | median_month_usd | worst_month | worst_month_usd | worst_over_median | months_negative | month_rule_pass |
|---|---|---|---|---|---|---|---|
| C1-SS | 8 | 478.18 | 2026-10 | -1,449 | 3.03 | 3 | no |
| C1-IB | 8 | 130.95 | 2026-10 | -2,195 | 16.76 | 4 | no |
| C2-SS | 8 | 563.73 | 2026-09 | -2,976 | 5.28 | 3 | no |
| C2-IB | 8 | 365.33 | 2026-09 | -3,629 | 9.93 | 4 | no |


## Tail (pooled)

| pair | n | mean_ror | worst_ror | best_ror | worst_decile_share_of_loss | realized_stress | mean_without_worst_1pct | skew |
|---|---|---|---|---|---|---|---|---|
| C1-SS | 99 | -0.92% | -81.91% | +35.76% | +45.48% | 0 | -0.09% | -0.7186 |
| C1-IB | 99 | -4.41% | -102.63% | +60.59% | +41.46% | 0 | -3.40% | -0.5044 |
| C2-SS | 91 | -0.59% | -60.39% | +34.49% | +47.58% | 0 | +0.08% | -0.5940 |
| C2-IB | 91 | -4.40% | -102.04% | +58.20% | +44.31% | 0 | -3.32% | -0.5131 |

Worst 10 positions, C1-SS:

| ticker | entry | expiry | ror | net_usd |
|---|---|---|---|---|
| PATH | 2026-07-24 | 2026-08-21 | -81.91% | -766.11 |
| IREN | 2026-09-25 | 2026-10-23 | -60.39% | -1,204 |
| MARA | 2026-09-25 | 2026-10-23 | -55.73% | -336.80 |
| U | 2026-03-20 | 2026-04-17 | -52.04% | -488.31 |
| FOXA | 2026-06-26 | 2026-07-17 | -51.61% | -434.26 |
| ARWR | 2026-08-28 | 2026-09-18 | -50.88% | -1,073 |
| MARA | 2026-10-02 | 2026-10-30 | -50.61% | -282.66 |
| MARA | 2026-10-02 | 2026-10-30 | -50.53% | -282.16 |
| QBTS | 2026-10-02 | 2026-10-30 | -41.33% | -271.04 |
| QBTS | 2026-10-02 | 2026-10-30 | -41.26% | -270.54 |

Worst 10 positions, C1-IB:

| ticker | entry | expiry | ror | net_usd |
|---|---|---|---|---|
| PATH | 2026-07-24 | 2026-08-21 | -102.63% | -509.05 |
| IREN | 2026-09-25 | 2026-10-23 | -101.67% | -1,119 |
| MARA | 2026-09-25 | 2026-10-23 | -100.85% | -348.36 |
| U | 2026-03-20 | 2026-04-17 | -100.15% | -514.88 |
| MARA | 2026-10-02 | 2026-10-30 | -93.14% | -295.57 |
| MARA | 2026-10-02 | 2026-10-30 | -92.98% | -295.07 |
| ARWR | 2026-08-28 | 2026-09-18 | -90.21% | -1,100 |
| QBTS | 2026-10-02 | 2026-10-30 | -72.35% | -283.01 |
| QBTS | 2026-10-02 | 2026-10-30 | -72.22% | -282.51 |
| OKLO | 2026-10-09 | 2026-11-06 | -70.69% | -590.04 |

Worst 10 positions, C2-SS:

| ticker | entry | expiry | ror | net_usd |
|---|---|---|---|---|
| IREN | 2026-09-25 | 2026-10-23 | -60.39% | -1,204 |
| MARA | 2026-09-25 | 2026-10-23 | -55.73% | -336.80 |
| FOXA | 2026-06-26 | 2026-07-17 | -51.61% | -434.26 |
| ARWR | 2026-08-28 | 2026-09-18 | -50.88% | -1,073 |
| MARA | 2026-10-02 | 2026-10-30 | -50.61% | -282.66 |
| MARA | 2026-10-02 | 2026-10-30 | -50.53% | -282.16 |
| BROS | 2026-08-21 | 2026-09-18 | -50.52% | -584.48 |
| GIS | 2026-07-31 | 2026-08-21 | -39.98% | -274.06 |
| OKLO | 2026-10-09 | 2026-11-06 | -38.24% | -559.79 |
| OKLO | 2026-10-09 | 2026-11-06 | -38.24% | -559.79 |

Worst 10 positions, C2-IB:

| ticker | entry | expiry | ror | net_usd |
|---|---|---|---|---|
| BROS | 2026-08-21 | 2026-09-18 | -102.04% | -614.23 |
| IREN | 2026-09-25 | 2026-10-23 | -101.67% | -1,119 |
| MARA | 2026-09-25 | 2026-10-23 | -100.85% | -348.36 |
| MARA | 2026-10-02 | 2026-10-30 | -93.14% | -295.57 |
| MARA | 2026-10-02 | 2026-10-30 | -92.98% | -295.07 |
| ARWR | 2026-08-28 | 2026-09-18 | -90.21% | -1,100 |
| OKLO | 2026-10-09 | 2026-11-06 | -70.69% | -590.04 |
| OKLO | 2026-10-09 | 2026-11-06 | -70.69% | -590.04 |
| FOXA | 2026-06-26 | 2026-07-17 | -66.44% | -447.50 |
| ALB | 2026-08-21 | 2026-09-18 | -59.76% | -1,544 |


## Stratum: cap_tercile (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | T1 | 32 | 16 | -8.48% |
| C1-SS | T2 | 32 | 15 | +3.82% |
| C1-SS | T3 | 35 | 14 | +1.66% |
| C1-IB | T1 | 33 | 16 | -15.48% |
| C1-IB | T2 | 31 | 15 | +2.57% |
| C1-IB | T3 | 35 | 14 | -0.15% |
| C2-SS | T1 | 31 | 15 | -5.80% |
| C2-SS | T2 | 31 | 15 | +5.39% |
| C2-SS | T3 | 29 | 13 | -1.40% |
| C2-IB | T1 | 31 | 15 | -14.10% |
| C2-IB | T2 | 32 | 15 | +3.43% |
| C2-IB | T3 | 28 | 13 | -2.61% |


## Stratum: iv_tercile (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | T1 | 30 | 14 | +3.08% |
| C1-SS | T2 | 32 | 13 | -0.22% |
| C1-SS | T3 | 37 | 12 | -4.78% |
| C1-IB | T1 | 30 | 14 | +3.20% |
| C1-IB | T2 | 33 | 14 | -2.27% |
| C1-IB | T3 | 36 | 11 | -12.69% |
| C2-SS | T1 | 33 | 14 | +1.98% |
| C2-SS | T2 | 31 | 14 | +1.66% |
| C2-SS | T3 | 27 | 10 | -6.30% |
| C2-IB | T1 | 34 | 14 | +0.22% |
| C2-IB | T2 | 30 | 14 | -0.27% |
| C2-IB | T3 | 27 | 10 | -14.82% |


## Stratum: sector (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | Basic Materials | 13 | 10 | +1.97% |
| C1-SS | Communication Services | 4 | 4 | -12.83% |
| C1-SS | Consumer Cyclical | 15 | 11 | +8.20% |
| C1-SS | Consumer Defensive | 6 | 6 | +6.65% |
| C1-SS | Energy | 3 | 3 | +1.96% |
| C1-SS | Financial Services | 14 | 6 | -13.81% |
| C1-SS | Healthcare | 2 | 2 | -12.95% |
| C1-SS | Industrials | 10 | 7 | +11.46% |
| C1-SS | Real Estate | 2 | 2 | +15.04% |
| C1-SS | Technology | 24 | 12 | -2.80% |
| C1-SS | Utilities | 6 | 4 | -15.43% |
| C1-IB | Basic Materials | 13 | 10 | +0.61% |
| C1-IB | Communication Services | 4 | 4 | -19.90% |
| C1-IB | Consumer Cyclical | 15 | 11 | +9.38% |
| C1-IB | Consumer Defensive | 6 | 6 | +12.43% |
| C1-IB | Energy | 3 | 3 | -1.40% |
| C1-IB | Financial Services | 14 | 6 | -27.43% |
| C1-IB | Healthcare | 2 | 2 | -26.34% |
| C1-IB | Industrials | 10 | 7 | +15.88% |
| C1-IB | Real Estate | 2 | 2 | +19.17% |
| C1-IB | Technology | 24 | 12 | -6.71% |
| C1-IB | Utilities | 6 | 4 | -29.16% |
| C2-SS | Basic Materials | 19 | 12 | +1.91% |
| C2-SS | Communication Services | 4 | 4 | -12.83% |
| C2-SS | Consumer Cyclical | 18 | 12 | +4.04% |
| C2-SS | Consumer Defensive | 6 | 6 | +6.65% |
| C2-SS | Energy | 4 | 3 | +4.97% |
| C2-SS | Financial Services | 16 | 7 | -13.08% |
| C2-SS | Healthcare | 3 | 3 | -0.54% |
| C2-SS | Industrials | 13 | 8 | +7.90% |
| C2-SS | Real Estate | 2 | 2 | +15.04% |
| C2-SS | Utilities | 6 | 4 | -15.43% |
| C2-IB | Basic Materials | 19 | 12 | +0.23% |
| C2-IB | Communication Services | 4 | 4 | -19.90% |
| C2-IB | Consumer Cyclical | 18 | 12 | +1.55% |
| C2-IB | Consumer Defensive | 6 | 6 | +12.43% |
| C2-IB | Energy | 4 | 3 | +4.18% |
| C2-IB | Financial Services | 16 | 7 | -26.35% |
| C2-IB | Healthcare | 3 | 3 | -4.81% |
| C2-IB | Industrials | 13 | 8 | +9.87% |
| C2-IB | Real Estate | 2 | 2 | +19.17% |
| C2-IB | Utilities | 6 | 4 | -29.16% |


## Stratum: regime (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | CHOP | 74 | 14 | -1.37% |
| C1-SS | PULLBACK | 19 | 5 | -1.30% |
| C1-SS | UPTREND | 6 | 3 | +5.83% |
| C1-IB | CHOP | 74 | 14 | -5.21% |
| C1-IB | PULLBACK | 19 | 5 | -4.50% |
| C1-IB | UPTREND | 6 | 3 | +5.80% |
| C2-SS | CHOP | 69 | 13 | -3.32% |
| C2-SS | PULLBACK | 17 | 5 | +9.63% |
| C2-SS | UPTREND | 5 | 3 | +2.45% |
| C2-IB | CHOP | 69 | 13 | -8.81% |
| C2-IB | PULLBACK | 17 | 5 | +12.35% |
| C2-IB | UPTREND | 5 | 3 | -0.50% |


## Stratum: sb_gate (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | OFF:G1 | 5 | 2 | +6.19% |
| C1-SS | OFF:G2 | 36 | 10 | +3.78% |
| C1-SS | ON | 58 | 10 | -4.46% |
| C1-IB | OFF:G1 | 5 | 2 | +7.59% |
| C1-IB | OFF:G2 | 36 | 10 | +3.14% |
| C1-IB | ON | 58 | 10 | -10.12% |
| C2-SS | OFF:G1 | 4 | 2 | +10.69% |
| C2-SS | OFF:G2 | 33 | 9 | +1.50% |
| C2-SS | ON | 54 | 10 | -2.69% |
| C2-IB | OFF:G1 | 4 | 2 | +14.50% |
| C2-IB | OFF:G2 | 33 | 9 | -0.64% |
| C2-IB | ON | 54 | 10 | -8.10% |


## Stratum: month (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | 2026-03 | 15 | 3 | -0.64% |
| C1-SS | 2026-05 | 16 | 4 | +9.43% |
| C1-SS | 2026-06 | 16 | 4 | +6.10% |
| C1-SS | 2026-07 | 6 | 2 | -11.72% |
| C1-SS | 2026-08 | 15 | 3 | +5.72% |
| C1-SS | 2026-09 | 19 | 4 | -0.47% |
| C1-SS | 2026-10 | 12 | 2 | -28.04% |
| C1-IB | 2026-03 | 15 | 3 | -5.67% |
| C1-IB | 2026-05 | 16 | 4 | +12.80% |
| C1-IB | 2026-06 | 16 | 4 | +7.96% |
| C1-IB | 2026-07 | 6 | 2 | -13.64% |
| C1-IB | 2026-08 | 15 | 3 | +5.37% |
| C1-IB | 2026-09 | 19 | 4 | -3.27% |
| C1-IB | 2026-10 | 12 | 2 | -51.66% |
| C2-SS | 2026-03 | 14 | 3 | +6.92% |
| C2-SS | 2026-05 | 15 | 4 | +8.06% |
| C2-SS | 2026-06 | 15 | 3 | +5.26% |
| C2-SS | 2026-07 | 5 | 2 | +2.32% |
| C2-SS | 2026-08 | 15 | 3 | -4.62% |
| C2-SS | 2026-09 | 17 | 4 | -2.26% |
| C2-SS | 2026-10 | 10 | 2 | -25.39% |
| C2-IB | 2026-03 | 14 | 3 | +7.70% |
| C2-IB | 2026-05 | 15 | 4 | +10.44% |
| C2-IB | 2026-06 | 15 | 3 | +6.80% |
| C2-IB | 2026-07 | 5 | 2 | +4.16% |
| C2-IB | 2026-08 | 15 | 3 | -13.95% |
| C2-IB | 2026-09 | 17 | 4 | -6.07% |
| C2-IB | 2026-10 | 10 | 2 | -47.53% |


## Funnel: suppressed names by first failing filter (all weeks)

| variant | reason | n |
|---|---|---|
| C1 | F10 | 44 |
| C2 | C2_sector | 33 |
| C2 | F10 | 18 |
| all | F1 | 78225 |
| all | F2 | 32913 |
| all | F3 | 31622 |
| all | F4 | 23455 |
| all | F5 | 4889 |
| all | F6 | 3456 |
| all | F7 | 8216 |
| all | F8 | 9351 |
| all | F9 | 284 |


## Go / no-go (DESIGN/90 §6; forward t >= 2.0; criterion 4 on the null benchmark)

| pair | variant | structure | forward_weeks | required | status | scale_required | verdict | note |
|---|---|---|---|---|---|---|---|---|
| C1-SS | C1 | SS | 2 | 40 | NOT DUE | 80 | NOT DUE | 2 of 40 graded forward entry-weeks |
| C1-IB | C1 | IB | 2 | 40 | NOT DUE | 80 | NOT DUE | 2 of 40 graded forward entry-weeks |
| C2-SS | C2 | SS | 2 | 40 | NOT DUE | 80 | NOT DUE | 2 of 40 graded forward entry-weeks |
| C2-IB | C2 | IB | 2 | 40 | NOT DUE | 80 | NOT DUE | 2 of 40 graded forward entry-weeks |
