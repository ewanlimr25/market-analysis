# S-C backtest report (generated)


## Inputs

- entries: ['2026-03-13', '2026-03-20', '2026-03-27', '2026-05-01', '2026-05-08', '2026-05-15', '2026-05-22', '2026-05-29', '2026-06-05', '2026-06-12', '2026-06-18', '2026-06-26', '2026-07-02', '2026-07-10', '2026-07-17', '2026-07-24', '2026-07-31', '2026-08-07', '2026-08-14', '2026-08-21', '2026-08-28', '2026-09-04', '2026-09-11', '2026-09-18', '2026-09-25', '2026-10-02', '2026-10-09', '2026-10-16']
- n_weeks: 28
- prices_through: 2026-10-16
- sb_open: data/backtest/sb_marked.parquet (39 positions)
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
| C1-SS | M | 85 | 20 | +6.66% | +4.95% | +65.00% | 2.37 | 0.0285 | 10,902 | +0.85% |
| C1-IB | M | 85 | 20 | +8.90% | +5.36% | +60.00% | 2.12 | 0.0476 | 7,604 | +2.10% |
| C2-SS | M | 79 | 18 | +7.17% | +5.39% | +72.22% | 3.32 | 0.0041 | 9,055 | +0.92% |
| C2-IB | M | 79 | 18 | +8.99% | +5.59% | +66.67% | 2.42 | 0.0268 | 5,616 | +2.16% |
| C1-SS | pooled | 85 | 20 | +6.66% | +4.95% | +65.00% | 2.37 | 0.0285 | 10,902 | +0.85% |
| C1-IB | pooled | 85 | 20 | +8.90% | +5.36% | +60.00% | 2.12 | 0.0476 | 7,604 | +2.10% |
| C2-SS | pooled | 79 | 18 | +7.17% | +5.39% | +72.22% | 3.32 | 0.0041 | 9,055 | +0.92% |
| C2-IB | pooled | 79 | 18 | +8.99% | +5.59% | +66.67% | 2.42 | 0.0268 | 5,616 | +2.16% |


## BH(0.10) across the four pairs (pooled; descriptive before the read)

| pair | weeks | mean_ror | nw_t | nw_p | bh_pass |
|---|---|---|---|---|---|
| C1-SS | 20 | +6.66% | 2.37 | 0.0285 | yes |
| C1-IB | 20 | +8.90% | 2.12 | 0.0476 | yes |
| C2-SS | 18 | +7.17% | 3.32 | 0.0041 | yes |
| C2-IB | 18 | +8.99% | 2.42 | 0.0268 | yes |


## Deflated Sharpe (6 trials, weekly series, pooled)

| pair | n | sr | sr_star | deflated_sr | dsr_prob | sr_star_null | deflated_sr_null | dsr_prob_null | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|
| C1-SS | 20 | 0.5675 | 0.1308 | 0.4367 | 0.9740 | 0.3064 | 0.2610 | 0.8773 | 0.2423 | 2.20 |
| C1-IB | 20 | 0.4810 | 0.1308 | 0.3502 | 0.9544 | 0.3064 | 0.1746 | 0.8000 | 0.4929 | 1.94 |
| C2-SS | 18 | 0.7143 | 0.1308 | 0.5836 | 0.9942 | 0.3064 | 0.4079 | 0.9610 | 0.4148 | 2.62 |
| C2-IB | 18 | 0.5296 | 0.1308 | 0.3988 | 0.9607 | 0.3064 | 0.2232 | 0.8375 | 0.4277 | 2.44 |


## PBO (CSCV over entry-week blocks; descriptive)

- pbo: 0.5285714285714286
- mean_logit: 0.14497272291011515
- n_combinations: 70
- n_configs: 4
- n_blocks: 8
- n_weeks: 20


## Month rule (net $ by expiry month at the frozen sizing, pooled)

| pair | n_months | median_month_usd | worst_month | worst_month_usd | worst_over_median | months_negative | month_rule_pass |
|---|---|---|---|---|---|---|---|
| C1-SS | 7 | 1,371 | 2026-08 | -499.67 | 0.3646 | 1 | yes |
| C1-IB | 7 | 812.56 | 2026-08 | -521.42 | 0.6417 | 2 | yes |
| C2-SS | 7 | 1,320 | 2026-09 | -2,976 | 2.25 | 1 | yes |
| C2-IB | 7 | 823.75 | 2026-09 | -3,629 | 4.41 | 2 | no |


## Tail (pooled)

| pair | n | mean_ror | worst_ror | best_ror | worst_decile_share_of_loss | realized_stress | mean_without_worst_1pct | skew |
|---|---|---|---|---|---|---|---|---|
| C1-SS | 85 | +4.00% | -81.91% | +35.76% | +57.08% | 0 | +5.03% | -1.01 |
| C1-IB | 85 | +3.91% | -102.63% | +60.59% | +49.23% | 0 | +5.18% | -0.5976 |
| C2-SS | 79 | +3.95% | -51.61% | +34.49% | +49.79% | 0 | +4.67% | -0.6288 |
| C2-IB | 79 | +3.17% | -102.04% | +56.93% | +44.15% | 0 | +4.52% | -0.5139 |

Worst 10 positions, C1-SS:

| ticker | entry | expiry | ror | net_usd |
|---|---|---|---|---|
| PATH | 2026-07-24 | 2026-08-21 | -81.91% | -766.11 |
| U | 2026-03-20 | 2026-04-17 | -52.04% | -488.31 |
| FOXA | 2026-06-26 | 2026-07-17 | -51.61% | -434.26 |
| ARWR | 2026-08-28 | 2026-09-18 | -50.88% | -1,073 |
| GIS | 2026-07-31 | 2026-08-21 | -39.98% | -274.06 |
| RGTI | 2026-09-18 | 2026-10-16 | -27.30% | -187.25 |
| FLR | 2026-05-15 | 2026-06-18 | -26.79% | -373.69 |
| HL | 2026-09-18 | 2026-10-16 | -20.16% | -132.40 |
| IREN | 2026-08-28 | 2026-09-25 | -19.09% | -329.80 |
| IONQ | 2026-09-18 | 2026-10-16 | -17.05% | -286.91 |

Worst 10 positions, C1-IB:

| ticker | entry | expiry | ror | net_usd |
|---|---|---|---|---|
| PATH | 2026-07-24 | 2026-08-21 | -102.63% | -509.05 |
| U | 2026-03-20 | 2026-04-17 | -100.15% | -514.88 |
| ARWR | 2026-08-28 | 2026-09-18 | -90.21% | -1,100 |
| FOXA | 2026-06-26 | 2026-07-17 | -66.44% | -447.50 |
| RGTI | 2026-09-18 | 2026-10-16 | -54.63% | -207.82 |
| GIS | 2026-07-31 | 2026-08-21 | -54.48% | -291.92 |
| FLR | 2026-05-15 | 2026-06-18 | -52.21% | -400.60 |
| HL | 2026-09-18 | 2026-10-16 | -40.25% | -148.20 |
| IREN | 2026-08-28 | 2026-09-25 | -36.46% | -377.32 |
| IONQ | 2026-09-18 | 2026-10-16 | -34.95% | -325.60 |

Worst 10 positions, C2-SS:

| ticker | entry | expiry | ror | net_usd |
|---|---|---|---|---|
| FOXA | 2026-06-26 | 2026-07-17 | -51.61% | -434.26 |
| ARWR | 2026-08-28 | 2026-09-18 | -50.88% | -1,073 |
| BROS | 2026-08-21 | 2026-09-18 | -50.52% | -584.48 |
| GIS | 2026-07-31 | 2026-08-21 | -39.98% | -274.06 |
| ALB | 2026-08-21 | 2026-09-18 | -30.94% | -1,409 |
| FLR | 2026-05-15 | 2026-06-18 | -26.79% | -373.69 |
| GME | 2026-09-18 | 2026-10-16 | -23.69% | -152.77 |
| MP | 2026-06-18 | 2026-07-17 | -21.34% | -573.21 |
| HL | 2026-09-18 | 2026-10-16 | -20.16% | -132.40 |
| IREN | 2026-08-28 | 2026-09-25 | -19.09% | -329.80 |

Worst 10 positions, C2-IB:

| ticker | entry | expiry | ror | net_usd |
|---|---|---|---|---|
| BROS | 2026-08-21 | 2026-09-18 | -102.04% | -614.23 |
| ARWR | 2026-08-28 | 2026-09-18 | -90.21% | -1,100 |
| FOXA | 2026-06-26 | 2026-07-17 | -66.44% | -447.50 |
| ALB | 2026-08-21 | 2026-09-18 | -59.76% | -1,544 |
| GIS | 2026-07-31 | 2026-08-21 | -54.48% | -291.92 |
| FLR | 2026-05-15 | 2026-06-18 | -52.21% | -400.60 |
| GME | 2026-09-18 | 2026-10-16 | -47.93% | -191.81 |
| HL | 2026-09-18 | 2026-10-16 | -40.25% | -148.20 |
| MP | 2026-06-18 | 2026-07-17 | -38.47% | -622.17 |
| IREN | 2026-08-28 | 2026-09-25 | -36.46% | -377.32 |


## Stratum: cap_tercile (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | T1 | 28 | 15 | +3.84% |
| C1-SS | T2 | 27 | 15 | +5.50% |
| C1-SS | T3 | 30 | 13 | +2.80% |
| C1-IB | T1 | 28 | 15 | +3.52% |
| C1-IB | T2 | 27 | 15 | +6.88% |
| C1-IB | T3 | 30 | 13 | +1.60% |
| C2-SS | T1 | 27 | 14 | +6.40% |
| C2-SS | T2 | 27 | 13 | +3.35% |
| C2-SS | T3 | 25 | 11 | +1.97% |
| C2-IB | T1 | 27 | 14 | +6.51% |
| C2-IB | T2 | 28 | 13 | +1.30% |
| C2-IB | T3 | 24 | 11 | +1.59% |


## Stratum: iv_tercile (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | T1 | 26 | 12 | +3.70% |
| C1-SS | T2 | 26 | 15 | +5.06% |
| C1-SS | T3 | 33 | 12 | +3.41% |
| C1-IB | T1 | 26 | 12 | +4.29% |
| C1-IB | T2 | 27 | 15 | +5.92% |
| C1-IB | T3 | 32 | 11 | +1.90% |
| C2-SS | T1 | 29 | 13 | +3.89% |
| C2-SS | T2 | 28 | 14 | +3.68% |
| C2-SS | T3 | 22 | 9 | +4.39% |
| C2-IB | T1 | 29 | 13 | +3.74% |
| C2-IB | T2 | 28 | 14 | +2.19% |
| C2-IB | T3 | 22 | 9 | +3.66% |


## Stratum: sector (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | Basic Materials | 12 | 10 | -0.06% |
| C1-SS | Communication Services | 4 | 4 | -12.83% |
| C1-SS | Consumer Cyclical | 15 | 11 | +8.20% |
| C1-SS | Consumer Defensive | 6 | 6 | +6.65% |
| C1-SS | Energy | 3 | 3 | +1.96% |
| C1-SS | Financial Services | 6 | 4 | +5.88% |
| C1-SS | Healthcare | 2 | 2 | -12.95% |
| C1-SS | Industrials | 11 | 8 | +10.89% |
| C1-SS | Real Estate | 2 | 2 | +15.04% |
| C1-SS | Technology | 22 | 11 | +0.70% |
| C1-SS | Utilities | 2 | 2 | +24.41% |
| C1-IB | Basic Materials | 12 | 10 | -4.19% |
| C1-IB | Communication Services | 4 | 4 | -19.90% |
| C1-IB | Consumer Cyclical | 15 | 11 | +9.38% |
| C1-IB | Consumer Defensive | 6 | 6 | +12.43% |
| C1-IB | Energy | 3 | 3 | -1.40% |
| C1-IB | Financial Services | 6 | 4 | +6.81% |
| C1-IB | Healthcare | 2 | 2 | -26.34% |
| C1-IB | Industrials | 11 | 8 | +14.82% |
| C1-IB | Real Estate | 2 | 2 | +19.17% |
| C1-IB | Technology | 22 | 11 | -0.74% |
| C1-IB | Utilities | 2 | 2 | +38.95% |
| C2-SS | Basic Materials | 18 | 12 | +0.56% |
| C2-SS | Communication Services | 4 | 4 | -12.83% |
| C2-SS | Consumer Cyclical | 19 | 12 | +4.98% |
| C2-SS | Consumer Defensive | 6 | 6 | +6.65% |
| C2-SS | Energy | 4 | 3 | +4.97% |
| C2-SS | Financial Services | 8 | 5 | +2.41% |
| C2-SS | Healthcare | 3 | 3 | -0.54% |
| C2-SS | Industrials | 13 | 8 | +7.90% |
| C2-SS | Real Estate | 2 | 2 | +15.04% |
| C2-SS | Utilities | 2 | 2 | +24.41% |
| C2-IB | Basic Materials | 18 | 12 | -2.99% |
| C2-IB | Communication Services | 4 | 4 | -19.90% |
| C2-IB | Consumer Cyclical | 19 | 12 | +3.11% |
| C2-IB | Consumer Defensive | 6 | 6 | +12.43% |
| C2-IB | Energy | 4 | 3 | +4.18% |
| C2-IB | Financial Services | 8 | 5 | +0.41% |
| C2-IB | Healthcare | 3 | 3 | -4.81% |
| C2-IB | Industrials | 13 | 8 | +9.87% |
| C2-IB | Real Estate | 2 | 2 | +19.17% |
| C2-IB | Utilities | 2 | 2 | +38.95% |


## Stratum: regime (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | CHOP | 60 | 12 | +5.50% |
| C1-SS | PULLBACK | 19 | 5 | -1.30% |
| C1-SS | UPTREND | 6 | 3 | +5.83% |
| C1-IB | CHOP | 60 | 12 | +6.38% |
| C1-IB | PULLBACK | 19 | 5 | -4.50% |
| C1-IB | UPTREND | 6 | 3 | +5.80% |
| C2-SS | CHOP | 57 | 10 | +2.39% |
| C2-SS | PULLBACK | 17 | 5 | +9.63% |
| C2-SS | UPTREND | 5 | 3 | +2.45% |
| C2-IB | CHOP | 57 | 10 | +0.75% |
| C2-IB | PULLBACK | 17 | 5 | +12.35% |
| C2-IB | UPTREND | 5 | 3 | -0.50% |


## Stratum: sb_gate (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | OFF:G1 | 5 | 2 | +6.19% |
| C1-SS | OFF:G2 | 34 | 9 | +5.64% |
| C1-SS | ON | 46 | 9 | +2.56% |
| C1-IB | OFF:G1 | 5 | 2 | +7.59% |
| C1-IB | OFF:G2 | 34 | 9 | +5.89% |
| C1-IB | ON | 46 | 9 | +2.04% |
| C2-SS | OFF:G1 | 4 | 2 | +10.69% |
| C2-SS | OFF:G2 | 31 | 8 | +3.92% |
| C2-SS | ON | 44 | 8 | +3.37% |
| C2-IB | OFF:G1 | 4 | 2 | +14.50% |
| C2-IB | OFF:G2 | 31 | 8 | +3.02% |
| C2-IB | ON | 44 | 8 | +2.25% |


## Stratum: month (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | 2026-03 | 15 | 3 | -0.64% |
| C1-SS | 2026-05 | 16 | 4 | +9.43% |
| C1-SS | 2026-06 | 16 | 4 | +6.10% |
| C1-SS | 2026-07 | 6 | 2 | -11.72% |
| C1-SS | 2026-08 | 15 | 3 | +5.72% |
| C1-SS | 2026-09 | 17 | 4 | +5.06% |
| C1-IB | 2026-03 | 15 | 3 | -5.67% |
| C1-IB | 2026-05 | 16 | 4 | +12.80% |
| C1-IB | 2026-06 | 16 | 4 | +7.96% |
| C1-IB | 2026-07 | 6 | 2 | -13.64% |
| C1-IB | 2026-08 | 15 | 3 | +5.37% |
| C1-IB | 2026-09 | 17 | 4 | +5.08% |
| C2-SS | 2026-03 | 14 | 3 | +6.92% |
| C2-SS | 2026-05 | 15 | 4 | +8.06% |
| C2-SS | 2026-06 | 15 | 3 | +5.26% |
| C2-SS | 2026-07 | 5 | 2 | +2.32% |
| C2-SS | 2026-08 | 15 | 3 | -4.62% |
| C2-SS | 2026-09 | 15 | 3 | +4.90% |
| C2-IB | 2026-03 | 14 | 3 | +7.70% |
| C2-IB | 2026-05 | 15 | 4 | +10.44% |
| C2-IB | 2026-06 | 15 | 3 | +6.80% |
| C2-IB | 2026-07 | 5 | 2 | +4.16% |
| C2-IB | 2026-08 | 15 | 3 | -13.95% |
| C2-IB | 2026-09 | 15 | 3 | +4.82% |


## Funnel: suppressed names by first failing filter (all weeks)

| variant | reason | n |
|---|---|---|
| C1 | F10 | 43 |
| C2 | C2_sector | 33 |
| C2 | F10 | 17 |
| all | F1 | 71455 |
| all | F2 | 29518 |
| all | F3 | 28634 |
| all | F4 | 21337 |
| all | F5 | 3801 |
| all | F6 | 3284 |
| all | F7 | 7297 |
| all | F8 | 8886 |
| all | F9 | 270 |


## Go / no-go (DESIGN/90 §6; forward t >= 2.0; criterion 4 on the null benchmark)

| pair | variant | structure | forward_weeks | required | status | scale_required | verdict | note |
|---|---|---|---|---|---|---|---|---|
| C1-SS | C1 | SS | 0 | 40 | NOT DUE | 80 | NOT DUE | 0 of 40 graded forward entry-weeks |
| C1-IB | C1 | IB | 0 | 40 | NOT DUE | 80 | NOT DUE | 0 of 40 graded forward entry-weeks |
| C2-SS | C2 | SS | 0 | 40 | NOT DUE | 80 | NOT DUE | 0 of 40 graded forward entry-weeks |
| C2-IB | C2 | IB | 0 | 40 | NOT DUE | 80 | NOT DUE | 0 of 40 graded forward entry-weeks |
