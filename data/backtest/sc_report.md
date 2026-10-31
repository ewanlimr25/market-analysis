# S-C backtest report (generated)


## Inputs

- entries: ['2026-03-13', '2026-03-20', '2026-03-27', '2026-05-01', '2026-05-08', '2026-05-15', '2026-05-22', '2026-05-29', '2026-06-05', '2026-06-12', '2026-06-18', '2026-06-26', '2026-07-02', '2026-07-10', '2026-07-17', '2026-07-24', '2026-07-31', '2026-08-07', '2026-08-14', '2026-08-21', '2026-08-28', '2026-09-04', '2026-09-11', '2026-09-18', '2026-09-25', '2026-10-02', '2026-10-09', '2026-10-16', '2026-10-23', '2026-10-30']
- n_weeks: 30
- prices_through: 2026-10-30
- sb_open: data/backtest/sb_marked.parquet (46 positions)
- params: {'price_min': 10.0, 'mcap_min': 1000000000.0, 'mcap_max': 20000000000.0, 'adv_min': 50000000.0, 'iv30d_min': 0.3, 'iv30d_max': 0.8, 'dte_cal_min': 20, 'dte_cal_max': 40, 'target_dte_cal': 28, 'atm_band': 0.025, 'leg_size_min': 5, 'spread_max': 0.08, 'select_n': 10, 'c2_excluded_sectors': ['Technology'], 'wing_sigma': 2.0, 'stress_sigma': 3.0}


## Count trigger (read at 40 graded forward entry-weeks per pair)

| pair | forward_weeks | required | status | scale_required |
|---|---|---|---|---|
| C1-SS | 1 | 40 | NOT DUE | 80 |
| C1-IB | 1 | 40 | NOT DUE | 80 |
| C2-SS | 1 | 40 | NOT DUE | 80 |
| C2-IB | 1 | 40 | NOT DUE | 80 |


## Mean net return on risk, entry-week series; NW(lag 4) t

| pair | window | n | weeks | mean_ror | median_ror | hit | nw_t | nw_p | net_usd_total | mean_cost_ror |
|---|---|---|---|---|---|---|---|---|---|---|
| C1-SS | M | 92 | 21 | +3.38% | +4.85% | +61.90% | 0.7901 | 0.4387 | 8,562 | +0.84% |
| C1-IB | M | 92 | 21 | +3.23% | +4.83% | +57.14% | 0.4575 | 0.6522 | 5,210 | +2.06% |
| C2-SS | M | 85 | 20 | +2.44% | +4.76% | +65.00% | 0.5266 | 0.6045 | 6,985 | +0.90% |
| C2-IB | M | 85 | 20 | +0.94% | +5.07% | +60.00% | 0.1192 | 0.9064 | 3,505 | +2.11% |
| C1-SS | F-2026Q4 | 5 | 1 | — | — | — | — | — | -802.36 | +0.67% |
| C1-IB | F-2026Q4 | 5 | 1 | — | — | — | — | — | -929.16 | +1.51% |
| C2-SS | F-2026Q4 | 4 | 1 | — | — | — | — | — | -531.32 | +0.66% |
| C2-IB | F-2026Q4 | 4 | 1 | — | — | — | — | — | -646.15 | +1.48% |
| C1-SS | F | 5 | 1 | — | — | — | — | — | -802.36 | +0.67% |
| C1-IB | F | 5 | 1 | — | — | — | — | — | -929.16 | +1.51% |
| C2-SS | F | 4 | 1 | — | — | — | — | — | -531.32 | +0.66% |
| C2-IB | F | 4 | 1 | — | — | — | — | — | -646.15 | +1.48% |
| C1-SS | pooled | 97 | 21 | +3.38% | +4.85% | +61.90% | 0.7898 | 0.4389 | 7,760 | +0.83% |
| C1-IB | pooled | 97 | 21 | +3.22% | +4.83% | +57.14% | 0.4572 | 0.6525 | 4,281 | +2.03% |
| C2-SS | pooled | 89 | 20 | +2.44% | +4.76% | +65.00% | 0.5264 | 0.6047 | 6,454 | +0.89% |
| C2-IB | pooled | 89 | 20 | +0.94% | +5.07% | +60.00% | 0.1190 | 0.9065 | 2,859 | +2.08% |


## BH(0.10) across the four pairs (pooled; descriptive before the read)

| pair | weeks | mean_ror | nw_t | nw_p | bh_pass |
|---|---|---|---|---|---|
| C1-SS | 21 | +3.38% | 0.7898 | 0.4389 | no |
| C1-IB | 21 | +3.22% | 0.4572 | 0.6525 | no |
| C2-SS | 20 | +2.44% | 0.5264 | 0.6047 | no |
| C2-IB | 20 | +0.94% | 0.1190 | 0.9065 | no |


## Deflated Sharpe (6 trials, weekly series, pooled)

| pair | n | sr | sr_star | deflated_sr | dsr_prob | sr_star_null | deflated_sr_null | dsr_prob_null | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|
| C1-SS | 21 | 0.2033 | 0.0924 | 0.1109 | 0.6738 | 0.2907 | -0.0874 | 0.3612 | -0.8819 | 4.14 |
| C1-IB | 21 | 0.1177 | 0.0924 | 0.0252 | 0.5424 | 0.2907 | -0.1730 | 0.2328 | -0.9588 | 4.54 |
| C2-SS | 20 | 0.1330 | 0.0924 | 0.0406 | 0.5619 | 0.2907 | -0.1577 | 0.2727 | -1.94 | 8.76 |
| C2-IB | 20 | 0.0303 | 0.0924 | -0.0622 | 0.3962 | 0.2907 | -0.2605 | 0.1351 | -1.92 | 8.65 |


## PBO (CSCV over entry-week blocks; descriptive)

- pbo: 0.5571428571428572
- mean_logit: 0.12180328816107718
- n_combinations: 70
- n_configs: 4
- n_blocks: 8
- n_weeks: 21


## Month rule (net $ by expiry month at the frozen sizing, pooled)

| pair | n_months | median_month_usd | worst_month | worst_month_usd | worst_over_median | months_negative | month_rule_pass |
|---|---|---|---|---|---|---|---|
| C1-SS | 7 | 861.02 | 2026-10 | -1,772 | 2.06 | 2 | yes |
| C1-IB | 7 | 743.03 | 2026-10 | -2,510 | 3.38 | 3 | no |
| C2-SS | 7 | 861.02 | 2026-09 | -2,976 | 3.46 | 2 | no |
| C2-IB | 7 | 743.03 | 2026-09 | -3,629 | 4.88 | 3 | no |


## Tail (pooled)

| pair | n | mean_ror | worst_ror | best_ror | worst_decile_share_of_loss | realized_stress | mean_without_worst_1pct | skew |
|---|---|---|---|---|---|---|---|---|
| C1-SS | 97 | -0.37% | -81.91% | +35.76% | +48.92% | 0 | +0.48% | -0.7848 |
| C1-IB | 97 | -3.60% | -102.63% | +60.59% | +44.63% | 0 | -2.56% | -0.5667 |
| C2-SS | 89 | +0.21% | -60.39% | +34.49% | +47.36% | 0 | +0.90% | -0.6615 |
| C2-IB | 89 | -3.21% | -102.04% | +56.93% | +43.15% | 0 | -2.09% | -0.5925 |

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
| FOXA | 2026-06-26 | 2026-07-17 | -66.44% | -447.50 |

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
| OKLO | 2026-10-02 | 2026-10-30 | -32.46% | -485.12 |
| OKLO | 2026-10-02 | 2026-10-30 | -32.46% | -485.12 |

Worst 10 positions, C2-IB:

| ticker | entry | expiry | ror | net_usd |
|---|---|---|---|---|
| BROS | 2026-08-21 | 2026-09-18 | -102.04% | -614.23 |
| IREN | 2026-09-25 | 2026-10-23 | -101.67% | -1,119 |
| MARA | 2026-09-25 | 2026-10-23 | -100.85% | -348.36 |
| MARA | 2026-10-02 | 2026-10-30 | -93.14% | -295.57 |
| MARA | 2026-10-02 | 2026-10-30 | -92.98% | -295.07 |
| ARWR | 2026-08-28 | 2026-09-18 | -90.21% | -1,100 |
| FOXA | 2026-06-26 | 2026-07-17 | -66.44% | -447.50 |
| ALB | 2026-08-21 | 2026-09-18 | -59.76% | -1,544 |
| OKLO | 2026-10-02 | 2026-10-30 | -55.76% | -511.52 |
| OKLO | 2026-10-02 | 2026-10-30 | -55.76% | -511.52 |


## Stratum: cap_tercile (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | T1 | 32 | 15 | -7.18% |
| C1-SS | T2 | 31 | 15 | +5.45% |
| C1-SS | T3 | 34 | 14 | +0.74% |
| C1-IB | T1 | 32 | 15 | -15.45% |
| C1-IB | T2 | 31 | 15 | +6.74% |
| C1-IB | T3 | 34 | 14 | -1.86% |
| C2-SS | T1 | 30 | 14 | -4.05% |
| C2-SS | T2 | 31 | 15 | +4.20% |
| C2-SS | T3 | 28 | 13 | +0.37% |
| C2-IB | T1 | 30 | 14 | -11.66% |
| C2-IB | T2 | 31 | 15 | +4.41% |
| C2-IB | T3 | 28 | 13 | -2.61% |


## Stratum: iv_tercile (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | T1 | 30 | 14 | +3.72% |
| C1-SS | T2 | 32 | 14 | +2.32% |
| C1-SS | T3 | 35 | 11 | -6.34% |
| C1-IB | T1 | 30 | 14 | +4.14% |
| C1-IB | T2 | 32 | 14 | +0.60% |
| C1-IB | T3 | 35 | 11 | -14.06% |
| C2-SS | T1 | 32 | 13 | +2.56% |
| C2-SS | T2 | 30 | 14 | +3.56% |
| C2-SS | T3 | 27 | 10 | -6.30% |
| C2-IB | T1 | 32 | 13 | +1.25% |
| C2-IB | T2 | 30 | 14 | +2.46% |
| C2-IB | T3 | 27 | 10 | -14.82% |


## Stratum: sector (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | Basic Materials | 12 | 10 | -0.06% |
| C1-SS | Communication Services | 4 | 4 | -12.83% |
| C1-SS | Consumer Cyclical | 15 | 11 | +8.20% |
| C1-SS | Consumer Defensive | 6 | 6 | +6.65% |
| C1-SS | Energy | 3 | 3 | +1.96% |
| C1-SS | Financial Services | 14 | 6 | -13.81% |
| C1-SS | Healthcare | 2 | 2 | -12.95% |
| C1-SS | Industrials | 11 | 8 | +10.89% |
| C1-SS | Real Estate | 2 | 2 | +15.04% |
| C1-SS | Technology | 24 | 12 | -2.80% |
| C1-SS | Utilities | 4 | 3 | -4.03% |
| C1-IB | Basic Materials | 12 | 10 | -4.19% |
| C1-IB | Communication Services | 4 | 4 | -19.90% |
| C1-IB | Consumer Cyclical | 15 | 11 | +9.38% |
| C1-IB | Consumer Defensive | 6 | 6 | +12.43% |
| C1-IB | Energy | 3 | 3 | -1.40% |
| C1-IB | Financial Services | 14 | 6 | -27.43% |
| C1-IB | Healthcare | 2 | 2 | -26.34% |
| C1-IB | Industrials | 11 | 8 | +14.82% |
| C1-IB | Real Estate | 2 | 2 | +19.17% |
| C1-IB | Technology | 24 | 12 | -6.71% |
| C1-IB | Utilities | 4 | 3 | -8.40% |
| C2-SS | Basic Materials | 18 | 12 | +0.56% |
| C2-SS | Communication Services | 4 | 4 | -12.83% |
| C2-SS | Consumer Cyclical | 19 | 12 | +4.98% |
| C2-SS | Consumer Defensive | 6 | 6 | +6.65% |
| C2-SS | Energy | 4 | 3 | +4.97% |
| C2-SS | Financial Services | 16 | 7 | -13.08% |
| C2-SS | Healthcare | 3 | 3 | -0.54% |
| C2-SS | Industrials | 13 | 8 | +7.90% |
| C2-SS | Real Estate | 2 | 2 | +15.04% |
| C2-SS | Utilities | 4 | 3 | -4.03% |
| C2-IB | Basic Materials | 18 | 12 | -2.99% |
| C2-IB | Communication Services | 4 | 4 | -19.90% |
| C2-IB | Consumer Cyclical | 19 | 12 | +3.11% |
| C2-IB | Consumer Defensive | 6 | 6 | +12.43% |
| C2-IB | Energy | 4 | 3 | +4.18% |
| C2-IB | Financial Services | 16 | 7 | -26.35% |
| C2-IB | Healthcare | 3 | 3 | -4.81% |
| C2-IB | Industrials | 13 | 8 | +9.87% |
| C2-IB | Real Estate | 2 | 2 | +19.17% |
| C2-IB | Utilities | 4 | 3 | -8.40% |


## Stratum: regime (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | CHOP | 72 | 13 | -0.64% |
| C1-SS | PULLBACK | 19 | 5 | -1.30% |
| C1-SS | UPTREND | 6 | 3 | +5.83% |
| C1-IB | CHOP | 72 | 13 | -4.14% |
| C1-IB | PULLBACK | 19 | 5 | -4.50% |
| C1-IB | UPTREND | 6 | 3 | +5.80% |
| C2-SS | CHOP | 67 | 12 | -2.34% |
| C2-SS | PULLBACK | 17 | 5 | +9.63% |
| C2-SS | UPTREND | 5 | 3 | +2.45% |
| C2-IB | CHOP | 67 | 12 | -7.37% |
| C2-IB | PULLBACK | 17 | 5 | +12.35% |
| C2-IB | UPTREND | 5 | 3 | -0.50% |


## Stratum: sb_gate (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | OFF:G1 | 5 | 2 | +6.19% |
| C1-SS | OFF:G2 | 34 | 9 | +5.64% |
| C1-SS | ON | 58 | 10 | -4.46% |
| C1-IB | OFF:G1 | 5 | 2 | +7.59% |
| C1-IB | OFF:G2 | 34 | 9 | +5.89% |
| C1-IB | ON | 58 | 10 | -10.12% |
| C2-SS | OFF:G1 | 4 | 2 | +10.69% |
| C2-SS | OFF:G2 | 31 | 8 | +3.92% |
| C2-SS | ON | 54 | 10 | -2.69% |
| C2-IB | OFF:G1 | 4 | 2 | +14.50% |
| C2-IB | OFF:G2 | 31 | 8 | +3.02% |
| C2-IB | ON | 54 | 10 | -8.10% |


## Stratum: month (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | 2026-03 | 15 | 3 | -0.64% |
| C1-SS | 2026-05 | 16 | 4 | +9.43% |
| C1-SS | 2026-06 | 16 | 4 | +6.10% |
| C1-SS | 2026-07 | 6 | 2 | -11.72% |
| C1-SS | 2026-08 | 15 | 3 | +5.72% |
| C1-SS | 2026-09 | 19 | 4 | -1.58% |
| C1-SS | 2026-10 | 10 | 1 | -26.00% |
| C1-IB | 2026-03 | 15 | 3 | -5.67% |
| C1-IB | 2026-05 | 16 | 4 | +12.80% |
| C1-IB | 2026-06 | 16 | 4 | +7.96% |
| C1-IB | 2026-07 | 6 | 2 | -13.64% |
| C1-IB | 2026-08 | 15 | 3 | +5.37% |
| C1-IB | 2026-09 | 19 | 4 | -6.11% |
| C1-IB | 2026-10 | 10 | 1 | -47.85% |
| C2-SS | 2026-03 | 14 | 3 | +6.92% |
| C2-SS | 2026-05 | 15 | 4 | +8.06% |
| C2-SS | 2026-06 | 15 | 3 | +5.26% |
| C2-SS | 2026-07 | 5 | 2 | +2.32% |
| C2-SS | 2026-08 | 15 | 3 | -4.62% |
| C2-SS | 2026-09 | 17 | 4 | -2.51% |
| C2-SS | 2026-10 | 8 | 1 | -22.17% |
| C2-IB | 2026-03 | 14 | 3 | +7.70% |
| C2-IB | 2026-05 | 15 | 4 | +10.44% |
| C2-IB | 2026-06 | 15 | 3 | +6.80% |
| C2-IB | 2026-07 | 5 | 2 | +4.16% |
| C2-IB | 2026-08 | 15 | 3 | -13.95% |
| C2-IB | 2026-09 | 17 | 4 | -7.66% |
| C2-IB | 2026-10 | 8 | 1 | -41.74% |


## Funnel: suppressed names by first failing filter (all weeks)

| variant | reason | n |
|---|---|---|
| C1 | F10 | 43 |
| C2 | C2_sector | 33 |
| C2 | F10 | 17 |
| all | F1 | 75973 |
| all | F2 | 31776 |
| all | F3 | 30636 |
| all | F4 | 22925 |
| all | F5 | 4786 |
| all | F6 | 3423 |
| all | F7 | 7417 |
| all | F8 | 9226 |
| all | F9 | 279 |


## Go / no-go (DESIGN/90 §6; forward t >= 2.0; criterion 4 on the null benchmark)

| pair | variant | structure | forward_weeks | required | status | scale_required | verdict | note |
|---|---|---|---|---|---|---|---|---|
| C1-SS | C1 | SS | 1 | 40 | NOT DUE | 80 | NOT DUE | 1 of 40 graded forward entry-weeks |
| C1-IB | C1 | IB | 1 | 40 | NOT DUE | 80 | NOT DUE | 1 of 40 graded forward entry-weeks |
| C2-SS | C2 | SS | 1 | 40 | NOT DUE | 80 | NOT DUE | 1 of 40 graded forward entry-weeks |
| C2-IB | C2 | IB | 1 | 40 | NOT DUE | 80 | NOT DUE | 1 of 40 graded forward entry-weeks |
