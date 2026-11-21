# S-C backtest report (generated)


## Inputs

- entries: ['2026-03-13', '2026-03-20', '2026-03-27', '2026-05-01', '2026-05-08', '2026-05-15', '2026-05-22', '2026-05-29', '2026-06-05', '2026-06-12', '2026-06-18', '2026-06-26', '2026-07-02', '2026-07-10', '2026-07-17', '2026-07-24', '2026-07-31', '2026-08-07', '2026-08-14', '2026-08-21', '2026-08-28', '2026-09-04', '2026-09-11', '2026-09-18', '2026-09-25', '2026-10-02', '2026-10-09', '2026-10-16', '2026-10-23', '2026-10-30', '2026-11-06', '2026-11-13', '2026-11-20']
- n_weeks: 33
- prices_through: 2026-11-20
- sb_open: data/backtest/sb_marked.parquet (48 positions)
- params: {'price_min': 10.0, 'mcap_min': 1000000000.0, 'mcap_max': 20000000000.0, 'adv_min': 50000000.0, 'iv30d_min': 0.3, 'iv30d_max': 0.8, 'dte_cal_min': 20, 'dte_cal_max': 40, 'target_dte_cal': 28, 'atm_band': 0.025, 'leg_size_min': 5, 'spread_max': 0.08, 'select_n': 10, 'c2_excluded_sectors': ['Technology'], 'wing_sigma': 2.0, 'stress_sigma': 3.0}


## Count trigger (read at 40 graded forward entry-weeks per pair)

| pair | forward_weeks | required | status | scale_required |
|---|---|---|---|---|
| C1-SS | 4 | 40 | NOT DUE | 80 |
| C1-IB | 4 | 40 | NOT DUE | 80 |
| C2-SS | 4 | 40 | NOT DUE | 80 |
| C2-IB | 4 | 40 | NOT DUE | 80 |


## Mean net return on risk, entry-week series; NW(lag 4) t

| pair | window | n | weeks | mean_ror | median_ror | hit | nw_t | nw_p | net_usd_total | mean_cost_ror |
|---|---|---|---|---|---|---|---|---|---|---|
| C1-SS | M | 96 | 24 | +1.59% | +3.56% | +62.50% | 0.3381 | 0.7383 | 6,856 | +0.83% |
| C1-IB | M | 96 | 24 | +0.20% | +2.87% | +54.17% | 0.0249 | 0.9804 | 3,373 | +2.06% |
| C2-SS | M | 89 | 23 | +0.62% | +4.17% | +65.22% | 0.1246 | 0.9019 | 4,765 | +0.89% |
| C2-IB | M | 89 | 23 | -2.04% | +4.98% | +56.52% | -0.2402 | 0.8124 | 1,164 | +2.13% |
| C1-SS | F-2026Q4 | 9 | 4 | -15.22% | -28.17% | +25.00% | -2.49 | 0.0882 | -2,831 | +0.71% |
| C1-IB | F-2026Q4 | 9 | 4 | -29.08% | -52.93% | +25.00% | -2.64 | 0.0774 | -3,082 | +1.82% |
| C2-SS | F-2026Q4 | 8 | 4 | -14.26% | -26.26% | +25.00% | -2.46 | 0.0905 | -2,560 | +0.72% |
| C2-IB | F-2026Q4 | 8 | 4 | -27.55% | -49.87% | +25.00% | -2.62 | 0.0789 | -2,799 | +1.85% |
| C1-SS | F | 9 | 4 | -15.22% | -28.17% | +25.00% | -2.49 | 0.0882 | -2,831 | +0.71% |
| C1-IB | F | 9 | 4 | -29.08% | -52.93% | +25.00% | -2.64 | 0.0774 | -3,082 | +1.82% |
| C2-SS | F | 8 | 4 | -14.26% | -26.26% | +25.00% | -2.46 | 0.0905 | -2,560 | +0.72% |
| C2-IB | F | 8 | 4 | -27.55% | -49.87% | +25.00% | -2.62 | 0.0789 | -2,799 | +1.85% |
| C1-SS | pooled | 105 | 24 | +1.59% | +3.56% | +62.50% | 0.3379 | 0.7385 | 4,025 | +0.82% |
| C1-IB | pooled | 105 | 24 | +0.19% | +2.87% | +54.17% | 0.0247 | 0.9805 | 291.97 | +2.04% |
| C2-SS | pooled | 97 | 23 | +0.62% | +4.17% | +65.22% | 0.1245 | 0.9021 | 2,205 | +0.87% |
| C2-IB | pooled | 97 | 23 | -2.04% | +4.98% | +56.52% | -0.2404 | 0.8123 | -1,635 | +2.11% |


## BH(0.10) across the four pairs (pooled; descriptive before the read)

| pair | weeks | mean_ror | nw_t | nw_p | bh_pass |
|---|---|---|---|---|---|
| C1-SS | 24 | +1.59% | 0.3379 | 0.7385 | no |
| C1-IB | 24 | +0.19% | 0.0247 | 0.9805 | no |
| C2-SS | 23 | +0.62% | 0.1245 | 0.9021 | no |
| C2-IB | 23 | -2.04% | -0.2404 | 0.8123 | no |


## Deflated Sharpe (6 trials, weekly series, pooled)

| pair | n | sr | sr_star | deflated_sr | dsr_prob | sr_star_null | deflated_sr_null | dsr_prob_null | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|
| C1-SS | 24 | 0.0795 | 0.0726 | 0.0069 | 0.5128 | 0.2711 | -0.1916 | 0.1852 | -0.6269 | 2.89 |
| C1-IB | 24 | 0.0057 | 0.0726 | -0.0669 | 0.3743 | 0.2711 | -0.2654 | 0.1019 | -0.6496 | 3.14 |
| C2-SS | 23 | 0.0292 | 0.0726 | -0.0434 | 0.4207 | 0.2711 | -0.2419 | 0.1322 | -1.13 | 4.61 |
| C2-IB | 23 | -0.0551 | 0.0726 | -0.1277 | 0.2689 | 0.2711 | -0.3262 | 0.0577 | -1.05 | 4.44 |


## PBO (CSCV over entry-week blocks; descriptive)

- pbo: 0.5428571428571428
- mean_logit: 0.1473998520071923
- n_combinations: 70
- n_configs: 4
- n_blocks: 8
- n_weeks: 24


## Month rule (net $ by expiry month at the frozen sizing, pooled)

| pair | n_months | median_month_usd | worst_month | worst_month_usd | worst_over_median | months_negative | month_rule_pass |
|---|---|---|---|---|---|---|---|
| C1-SS | 8 | 478.18 | 2026-11 | -4,058 | 8.49 | 3 | no |
| C1-IB | 8 | 130.95 | 2026-11 | -4,305 | 32.87 | 4 | no |
| C2-SS | 8 | 563.73 | 2026-11 | -4,058 | 7.20 | 3 | no |
| C2-IB | 8 | 365.33 | 2026-11 | -4,305 | 11.78 | 4 | no |


## Tail (pooled)

| pair | n | mean_ror | worst_ror | best_ror | worst_decile_share_of_loss | realized_stress | mean_without_worst_1pct | skew |
|---|---|---|---|---|---|---|---|---|
| C1-SS | 105 | -1.38% | -81.91% | +35.76% | +45.02% | 0 | -0.61% | -0.6390 |
| C1-IB | 105 | -5.22% | -102.63% | +60.59% | +41.90% | 0 | -4.28% | -0.4540 |
| C2-SS | 97 | -1.10% | -60.39% | +34.49% | +43.35% | 0 | -0.49% | -0.5208 |
| C2-IB | 97 | -5.28% | -102.04% | +60.23% | +41.24% | 0 | -4.27% | -0.4575 |

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
| DINO | 2026-10-30 | 2026-11-20 | -45.47% | -1,545 |
| DINO | 2026-10-30 | 2026-11-20 | -45.47% | -1,545 |

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
| DINO | 2026-10-30 | 2026-11-20 | -89.07% | -1,606 |
| DINO | 2026-10-30 | 2026-11-20 | -89.07% | -1,606 |
| QBTS | 2026-10-02 | 2026-10-30 | -72.35% | -283.01 |

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
| DINO | 2026-10-30 | 2026-11-20 | -45.47% | -1,545 |
| DINO | 2026-10-30 | 2026-11-20 | -45.47% | -1,545 |
| GIS | 2026-07-31 | 2026-08-21 | -39.98% | -274.06 |

Worst 10 positions, C2-IB:

| ticker | entry | expiry | ror | net_usd |
|---|---|---|---|---|
| BROS | 2026-08-21 | 2026-09-18 | -102.04% | -614.23 |
| IREN | 2026-09-25 | 2026-10-23 | -101.67% | -1,119 |
| MARA | 2026-09-25 | 2026-10-23 | -100.85% | -348.36 |
| MARA | 2026-10-02 | 2026-10-30 | -93.14% | -295.57 |
| MARA | 2026-10-02 | 2026-10-30 | -92.98% | -295.07 |
| ARWR | 2026-08-28 | 2026-09-18 | -90.21% | -1,100 |
| DINO | 2026-10-30 | 2026-11-20 | -89.07% | -1,606 |
| DINO | 2026-10-30 | 2026-11-20 | -89.07% | -1,606 |
| OKLO | 2026-10-09 | 2026-11-06 | -70.69% | -590.04 |
| OKLO | 2026-10-09 | 2026-11-06 | -70.69% | -590.04 |


## Stratum: cap_tercile (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | T1 | 34 | 17 | -8.88% |
| C1-SS | T2 | 34 | 16 | +5.58% |
| C1-SS | T3 | 37 | 15 | -0.89% |
| C1-IB | T1 | 35 | 17 | -16.13% |
| C1-IB | T2 | 33 | 16 | +6.07% |
| C1-IB | T3 | 37 | 15 | -4.96% |
| C2-SS | T1 | 33 | 16 | -6.37% |
| C2-SS | T2 | 33 | 16 | +7.10% |
| C2-SS | T3 | 31 | 14 | -4.24% |
| C2-IB | T1 | 33 | 16 | -14.88% |
| C2-IB | T2 | 34 | 16 | +6.77% |
| C2-IB | T3 | 30 | 14 | -8.37% |


## Stratum: iv_tercile (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | T1 | 32 | 15 | +5.00% |
| C1-SS | T2 | 34 | 14 | -4.93% |
| C1-SS | T3 | 39 | 14 | -3.53% |
| C1-IB | T1 | 32 | 15 | +6.76% |
| C1-IB | T2 | 34 | 14 | -11.95% |
| C1-IB | T3 | 39 | 14 | -9.17% |
| C2-SS | T1 | 35 | 15 | +3.79% |
| C2-SS | T2 | 33 | 15 | -1.45% |
| C2-SS | T3 | 29 | 12 | -6.62% |
| C2-IB | T1 | 36 | 15 | +3.55% |
| C2-IB | T2 | 33 | 15 | -8.02% |
| C2-IB | T3 | 28 | 11 | -13.40% |


## Stratum: sector (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | Basic Materials | 13 | 10 | +1.97% |
| C1-SS | Communication Services | 4 | 4 | -12.83% |
| C1-SS | Consumer Cyclical | 17 | 12 | +5.45% |
| C1-SS | Consumer Defensive | 6 | 6 | +6.65% |
| C1-SS | Energy | 5 | 4 | -17.01% |
| C1-SS | Financial Services | 14 | 6 | -13.81% |
| C1-SS | Healthcare | 2 | 2 | -12.95% |
| C1-SS | Industrials | 12 | 8 | +15.17% |
| C1-SS | Real Estate | 2 | 2 | +15.04% |
| C1-SS | Technology | 24 | 12 | -2.80% |
| C1-SS | Utilities | 6 | 4 | -15.43% |
| C1-IB | Basic Materials | 13 | 10 | +0.61% |
| C1-IB | Communication Services | 4 | 4 | -19.90% |
| C1-IB | Consumer Cyclical | 17 | 12 | +5.11% |
| C1-IB | Consumer Defensive | 6 | 6 | +12.43% |
| C1-IB | Energy | 5 | 4 | -36.47% |
| C1-IB | Financial Services | 14 | 6 | -27.43% |
| C1-IB | Healthcare | 2 | 2 | -26.34% |
| C1-IB | Industrials | 12 | 8 | +23.27% |
| C1-IB | Real Estate | 2 | 2 | +19.17% |
| C1-IB | Technology | 24 | 12 | -6.71% |
| C1-IB | Utilities | 6 | 4 | -29.16% |
| C2-SS | Basic Materials | 19 | 12 | +1.91% |
| C2-SS | Communication Services | 4 | 4 | -12.83% |
| C2-SS | Consumer Cyclical | 20 | 13 | +2.11% |
| C2-SS | Consumer Defensive | 6 | 6 | +6.65% |
| C2-SS | Energy | 6 | 4 | -11.84% |
| C2-SS | Financial Services | 16 | 7 | -13.08% |
| C2-SS | Healthcare | 3 | 3 | -0.54% |
| C2-SS | Industrials | 15 | 9 | +11.34% |
| C2-SS | Real Estate | 2 | 2 | +15.04% |
| C2-SS | Utilities | 6 | 4 | -15.43% |
| C2-IB | Basic Materials | 19 | 12 | +0.23% |
| C2-IB | Communication Services | 4 | 4 | -19.90% |
| C2-IB | Consumer Cyclical | 20 | 13 | -1.29% |
| C2-IB | Consumer Defensive | 6 | 6 | +12.43% |
| C2-IB | Energy | 6 | 4 | -26.91% |
| C2-IB | Financial Services | 16 | 7 | -26.35% |
| C2-IB | Healthcare | 3 | 3 | -4.81% |
| C2-IB | Industrials | 15 | 9 | +16.58% |
| C2-IB | Real Estate | 2 | 2 | +19.17% |
| C2-IB | Utilities | 6 | 4 | -29.16% |


## Stratum: regime (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | CHOP | 78 | 15 | -2.86% |
| C1-SS | PULLBACK | 21 | 6 | +2.04% |
| C1-SS | UPTREND | 6 | 3 | +5.83% |
| C1-IB | CHOP | 78 | 15 | -7.92% |
| C1-IB | PULLBACK | 21 | 6 | +1.67% |
| C1-IB | UPTREND | 6 | 3 | +5.80% |
| C2-SS | CHOP | 73 | 14 | -4.80% |
| C2-SS | PULLBACK | 19 | 6 | +12.17% |
| C2-SS | UPTREND | 5 | 3 | +2.45% |
| C2-IB | CHOP | 73 | 14 | -11.51% |
| C2-IB | PULLBACK | 19 | 6 | +17.39% |
| C2-IB | UPTREND | 5 | 3 | -0.50% |


## Stratum: sb_gate (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | OFF:G1 | 5 | 2 | +6.19% |
| C1-SS | OFF:G2 | 36 | 10 | +3.78% |
| C1-SS | ON | 64 | 12 | -4.88% |
| C1-IB | OFF:G1 | 5 | 2 | +7.59% |
| C1-IB | OFF:G2 | 36 | 10 | +3.14% |
| C1-IB | ON | 64 | 12 | -10.91% |
| C2-SS | OFF:G1 | 4 | 2 | +10.69% |
| C2-SS | OFF:G2 | 33 | 9 | +1.50% |
| C2-SS | ON | 60 | 12 | -3.32% |
| C2-IB | OFF:G1 | 4 | 2 | +14.50% |
| C2-IB | OFF:G2 | 33 | 9 | -0.64% |
| C2-IB | ON | 60 | 12 | -9.15% |


## Stratum: month (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | 2026-03 | 15 | 3 | -0.64% |
| C1-SS | 2026-05 | 16 | 4 | +9.43% |
| C1-SS | 2026-06 | 16 | 4 | +6.10% |
| C1-SS | 2026-07 | 6 | 2 | -11.72% |
| C1-SS | 2026-08 | 15 | 3 | +5.72% |
| C1-SS | 2026-09 | 19 | 4 | -0.47% |
| C1-SS | 2026-10 | 18 | 4 | -21.69% |
| C1-IB | 2026-03 | 15 | 3 | -5.67% |
| C1-IB | 2026-05 | 16 | 4 | +12.80% |
| C1-IB | 2026-06 | 16 | 4 | +7.96% |
| C1-IB | 2026-07 | 6 | 2 | -13.64% |
| C1-IB | 2026-08 | 15 | 3 | +5.37% |
| C1-IB | 2026-09 | 19 | 4 | -3.27% |
| C1-IB | 2026-10 | 18 | 4 | -40.63% |
| C2-SS | 2026-03 | 14 | 3 | +6.92% |
| C2-SS | 2026-05 | 15 | 4 | +8.06% |
| C2-SS | 2026-06 | 15 | 3 | +5.26% |
| C2-SS | 2026-07 | 5 | 2 | +2.32% |
| C2-SS | 2026-08 | 15 | 3 | -4.62% |
| C2-SS | 2026-09 | 17 | 4 | -2.26% |
| C2-SS | 2026-10 | 16 | 4 | -19.23% |
| C2-IB | 2026-03 | 14 | 3 | +7.70% |
| C2-IB | 2026-05 | 15 | 4 | +10.44% |
| C2-IB | 2026-06 | 15 | 3 | +6.80% |
| C2-IB | 2026-07 | 5 | 2 | +4.16% |
| C2-IB | 2026-08 | 15 | 3 | -13.95% |
| C2-IB | 2026-09 | 17 | 4 | -6.07% |
| C2-IB | 2026-10 | 16 | 4 | -36.67% |


## Funnel: suppressed names by first failing filter (all weeks)

| variant | reason | n |
|---|---|---|
| C1 | F10 | 44 |
| C2 | C2_sector | 37 |
| C2 | F10 | 18 |
| all | F1 | 82731 |
| all | F2 | 35286 |
| all | F3 | 33542 |
| all | F4 | 24850 |
| all | F5 | 5053 |
| all | F6 | 3816 |
| all | F7 | 8377 |
| all | F8 | 10382 |
| all | F9 | 308 |


## Go / no-go (DESIGN/90 §6; forward t >= 2.0; criterion 4 on the null benchmark)

| pair | variant | structure | forward_weeks | required | status | scale_required | verdict | note |
|---|---|---|---|---|---|---|---|---|
| C1-SS | C1 | SS | 4 | 40 | NOT DUE | 80 | NOT DUE | 4 of 40 graded forward entry-weeks |
| C1-IB | C1 | IB | 4 | 40 | NOT DUE | 80 | NOT DUE | 4 of 40 graded forward entry-weeks |
| C2-SS | C2 | SS | 4 | 40 | NOT DUE | 80 | NOT DUE | 4 of 40 graded forward entry-weeks |
| C2-IB | C2 | IB | 4 | 40 | NOT DUE | 80 | NOT DUE | 4 of 40 graded forward entry-weeks |
