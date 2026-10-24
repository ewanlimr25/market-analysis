# S-C backtest report (generated)


## Inputs

- entries: ['2026-03-13', '2026-03-20', '2026-03-27', '2026-05-01', '2026-05-08', '2026-05-15', '2026-05-22', '2026-05-29', '2026-06-05', '2026-06-12', '2026-06-18', '2026-06-26', '2026-07-02', '2026-07-10', '2026-07-17', '2026-07-24', '2026-07-31', '2026-08-07', '2026-08-14', '2026-08-21', '2026-08-28', '2026-09-04', '2026-09-11', '2026-09-18', '2026-09-25', '2026-10-02', '2026-10-09', '2026-10-16', '2026-10-23']
- n_weeks: 29
- prices_through: 2026-10-23
- sb_open: data/backtest/sb_marked.parquet (42 positions)
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
| C1-SS | M | 87 | 20 | +4.85% | +4.95% | +65.00% | 1.37 | 0.1877 | 9,362 | +0.85% |
| C1-IB | M | 87 | 20 | +5.78% | +5.36% | +60.00% | 1.02 | 0.3194 | 6,137 | +2.09% |
| C2-SS | M | 81 | 19 | +3.73% | +5.36% | +68.42% | 0.9580 | 0.3507 | 7,514 | +0.91% |
| C2-IB | M | 81 | 19 | +3.19% | +5.17% | +63.16% | 0.4814 | 0.6361 | 4,149 | +2.14% |
| C1-SS | pooled | 87 | 20 | +4.85% | +4.95% | +65.00% | 1.37 | 0.1877 | 9,362 | +0.85% |
| C1-IB | pooled | 87 | 20 | +5.78% | +5.36% | +60.00% | 1.02 | 0.3194 | 6,137 | +2.09% |
| C2-SS | pooled | 81 | 19 | +3.73% | +5.36% | +68.42% | 0.9580 | 0.3507 | 7,514 | +0.91% |
| C2-IB | pooled | 81 | 19 | +3.19% | +5.17% | +63.16% | 0.4814 | 0.6361 | 4,149 | +2.14% |


## BH(0.10) across the four pairs (pooled; descriptive before the read)

| pair | weeks | mean_ror | nw_t | nw_p | bh_pass |
|---|---|---|---|---|---|
| C1-SS | 20 | +4.85% | 1.37 | 0.1877 | no |
| C1-IB | 20 | +5.78% | 1.02 | 0.3194 | no |
| C2-SS | 19 | +3.73% | 0.9580 | 0.3507 | no |
| C2-IB | 19 | +3.19% | 0.4814 | 0.6361 | no |


## Deflated Sharpe (6 trials, weekly series, pooled)

| pair | n | sr | sr_star | deflated_sr | dsr_prob | sr_star_null | deflated_sr_null | dsr_prob_null | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|
| C1-SS | 20 | 0.3110 | 0.1097 | 0.2012 | 0.7681 | 0.2983 | 0.0127 | 0.5185 | -1.05 | 5.39 |
| C1-IB | 20 | 0.2273 | 0.1097 | 0.1176 | 0.6721 | 0.2983 | -0.0709 | 0.3940 | -1.13 | 6.05 |
| C2-SS | 19 | 0.2090 | 0.1097 | 0.0993 | 0.6308 | 0.2983 | -0.0893 | 0.3820 | -2.30 | 11.01 |
| C2-IB | 19 | 0.1055 | 0.1097 | -0.0042 | 0.4936 | 0.2983 | -0.1928 | 0.2340 | -2.30 | 10.98 |


## PBO (CSCV over entry-week blocks; descriptive)

- pbo: 0.6142857142857143
- mean_logit: 0.04744072571980911
- n_combinations: 70
- n_configs: 4
- n_blocks: 8
- n_weeks: 20


## Month rule (net $ by expiry month at the frozen sizing, pooled)

| pair | n_months | median_month_usd | worst_month | worst_month_usd | worst_over_median | months_negative | month_rule_pass |
|---|---|---|---|---|---|---|---|
| C1-SS | 7 | 861.02 | 2026-08 | -499.67 | 0.5803 | 2 | yes |
| C1-IB | 7 | 743.03 | 2026-10 | -654.56 | 0.8809 | 3 | yes |
| C2-SS | 7 | 861.02 | 2026-09 | -2,976 | 3.46 | 2 | no |
| C2-IB | 7 | 743.03 | 2026-09 | -3,629 | 4.88 | 3 | no |


## Tail (pooled)

| pair | n | mean_ror | worst_ror | best_ror | worst_decile_share_of_loss | realized_stress | mean_without_worst_1pct | skew |
|---|---|---|---|---|---|---|---|---|
| C1-SS | 87 | +2.58% | -81.91% | +35.76% | +57.47% | 0 | +3.56% | -1.02 |
| C1-IB | 87 | +1.49% | -102.63% | +60.59% | +50.00% | 0 | +2.70% | -0.7085 |
| C2-SS | 81 | +2.42% | -60.39% | +34.49% | +54.98% | 0 | +3.21% | -0.7718 |
| C2-IB | 81 | +0.59% | -102.04% | +56.93% | +49.26% | 0 | +1.87% | -0.6712 |

Worst 10 positions, C1-SS:

| ticker | entry | expiry | ror | net_usd |
|---|---|---|---|---|
| PATH | 2026-07-24 | 2026-08-21 | -81.91% | -766.11 |
| IREN | 2026-09-25 | 2026-10-23 | -60.39% | -1,204 |
| MARA | 2026-09-25 | 2026-10-23 | -55.73% | -336.80 |
| U | 2026-03-20 | 2026-04-17 | -52.04% | -488.31 |
| FOXA | 2026-06-26 | 2026-07-17 | -51.61% | -434.26 |
| ARWR | 2026-08-28 | 2026-09-18 | -50.88% | -1,073 |
| GIS | 2026-07-31 | 2026-08-21 | -39.98% | -274.06 |
| RGTI | 2026-09-18 | 2026-10-16 | -27.30% | -187.25 |
| FLR | 2026-05-15 | 2026-06-18 | -26.79% | -373.69 |
| HL | 2026-09-18 | 2026-10-16 | -20.16% | -132.40 |

Worst 10 positions, C1-IB:

| ticker | entry | expiry | ror | net_usd |
|---|---|---|---|---|
| PATH | 2026-07-24 | 2026-08-21 | -102.63% | -509.05 |
| IREN | 2026-09-25 | 2026-10-23 | -101.67% | -1,119 |
| MARA | 2026-09-25 | 2026-10-23 | -100.85% | -348.36 |
| U | 2026-03-20 | 2026-04-17 | -100.15% | -514.88 |
| ARWR | 2026-08-28 | 2026-09-18 | -90.21% | -1,100 |
| FOXA | 2026-06-26 | 2026-07-17 | -66.44% | -447.50 |
| RGTI | 2026-09-18 | 2026-10-16 | -54.63% | -207.82 |
| GIS | 2026-07-31 | 2026-08-21 | -54.48% | -291.92 |
| FLR | 2026-05-15 | 2026-06-18 | -52.21% | -400.60 |
| HL | 2026-09-18 | 2026-10-16 | -40.25% | -148.20 |

Worst 10 positions, C2-SS:

| ticker | entry | expiry | ror | net_usd |
|---|---|---|---|---|
| IREN | 2026-09-25 | 2026-10-23 | -60.39% | -1,204 |
| MARA | 2026-09-25 | 2026-10-23 | -55.73% | -336.80 |
| FOXA | 2026-06-26 | 2026-07-17 | -51.61% | -434.26 |
| ARWR | 2026-08-28 | 2026-09-18 | -50.88% | -1,073 |
| BROS | 2026-08-21 | 2026-09-18 | -50.52% | -584.48 |
| GIS | 2026-07-31 | 2026-08-21 | -39.98% | -274.06 |
| ALB | 2026-08-21 | 2026-09-18 | -30.94% | -1,409 |
| FLR | 2026-05-15 | 2026-06-18 | -26.79% | -373.69 |
| GME | 2026-09-18 | 2026-10-16 | -23.69% | -152.77 |
| MP | 2026-06-18 | 2026-07-17 | -21.34% | -573.21 |

Worst 10 positions, C2-IB:

| ticker | entry | expiry | ror | net_usd |
|---|---|---|---|---|
| BROS | 2026-08-21 | 2026-09-18 | -102.04% | -614.23 |
| IREN | 2026-09-25 | 2026-10-23 | -101.67% | -1,119 |
| MARA | 2026-09-25 | 2026-10-23 | -100.85% | -348.36 |
| ARWR | 2026-08-28 | 2026-09-18 | -90.21% | -1,100 |
| FOXA | 2026-06-26 | 2026-07-17 | -66.44% | -447.50 |
| ALB | 2026-08-21 | 2026-09-18 | -59.76% | -1,544 |
| GIS | 2026-07-31 | 2026-08-21 | -54.48% | -291.92 |
| FLR | 2026-05-15 | 2026-06-18 | -52.21% | -400.60 |
| GME | 2026-09-18 | 2026-10-16 | -47.93% | -191.81 |
| HL | 2026-09-18 | 2026-10-16 | -40.25% | -148.20 |


## Stratum: cap_tercile (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | T1 | 28 | 16 | +2.00% |
| C1-SS | T2 | 28 | 15 | +5.16% |
| C1-SS | T3 | 31 | 13 | +0.77% |
| C1-IB | T1 | 28 | 16 | +0.29% |
| C1-IB | T2 | 28 | 15 | +6.26% |
| C1-IB | T3 | 31 | 13 | -1.74% |
| C2-SS | T1 | 28 | 15 | +4.18% |
| C2-SS | T2 | 28 | 13 | +2.51% |
| C2-SS | T3 | 25 | 12 | +0.36% |
| C2-IB | T1 | 28 | 15 | +2.68% |
| C2-IB | T2 | 28 | 13 | +1.30% |
| C2-IB | T3 | 25 | 12 | -2.54% |


## Stratum: iv_tercile (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | T1 | 27 | 12 | +4.03% |
| C1-SS | T2 | 27 | 14 | +5.86% |
| C1-SS | T3 | 33 | 11 | -1.29% |
| C1-IB | T1 | 27 | 12 | +4.82% |
| C1-IB | T2 | 27 | 14 | +6.16% |
| C1-IB | T3 | 33 | 11 | -5.05% |
| C2-SS | T1 | 29 | 13 | +3.89% |
| C2-SS | T2 | 29 | 14 | +4.12% |
| C2-SS | T3 | 23 | 9 | -1.57% |
| C2-IB | T1 | 29 | 13 | +3.74% |
| C2-IB | T2 | 29 | 14 | +2.97% |
| C2-IB | T3 | 23 | 9 | -6.39% |


## Stratum: sector (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | Basic Materials | 12 | 10 | -0.06% |
| C1-SS | Communication Services | 4 | 4 | -12.83% |
| C1-SS | Consumer Cyclical | 15 | 11 | +8.20% |
| C1-SS | Consumer Defensive | 6 | 6 | +6.65% |
| C1-SS | Energy | 3 | 3 | +1.96% |
| C1-SS | Financial Services | 8 | 5 | -10.10% |
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
| C1-IB | Financial Services | 8 | 5 | -20.21% |
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
| C2-SS | Financial Services | 10 | 6 | -9.68% |
| C2-SS | Healthcare | 3 | 3 | -0.54% |
| C2-SS | Industrials | 13 | 8 | +7.90% |
| C2-SS | Real Estate | 2 | 2 | +15.04% |
| C2-SS | Utilities | 2 | 2 | +24.41% |
| C2-IB | Basic Materials | 18 | 12 | -2.99% |
| C2-IB | Communication Services | 4 | 4 | -19.90% |
| C2-IB | Consumer Cyclical | 19 | 12 | +3.11% |
| C2-IB | Consumer Defensive | 6 | 6 | +12.43% |
| C2-IB | Energy | 4 | 3 | +4.18% |
| C2-IB | Financial Services | 10 | 6 | -19.93% |
| C2-IB | Healthcare | 3 | 3 | -4.81% |
| C2-IB | Industrials | 13 | 8 | +9.87% |
| C2-IB | Real Estate | 2 | 2 | +19.17% |
| C2-IB | Utilities | 2 | 2 | +38.95% |


## Stratum: regime (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | CHOP | 62 | 12 | +3.45% |
| C1-SS | PULLBACK | 19 | 5 | -1.30% |
| C1-SS | UPTREND | 6 | 3 | +5.83% |
| C1-IB | CHOP | 62 | 12 | +2.91% |
| C1-IB | PULLBACK | 19 | 5 | -4.50% |
| C1-IB | UPTREND | 6 | 3 | +5.80% |
| C2-SS | CHOP | 59 | 11 | +0.34% |
| C2-SS | PULLBACK | 17 | 5 | +9.63% |
| C2-SS | UPTREND | 5 | 3 | +2.45% |
| C2-IB | CHOP | 59 | 11 | -2.71% |
| C2-IB | PULLBACK | 17 | 5 | +12.35% |
| C2-IB | UPTREND | 5 | 3 | -0.50% |


## Stratum: sb_gate (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | OFF:G1 | 5 | 2 | +6.19% |
| C1-SS | OFF:G2 | 34 | 9 | +5.64% |
| C1-SS | ON | 48 | 9 | +0.03% |
| C1-IB | OFF:G1 | 5 | 2 | +7.59% |
| C1-IB | OFF:G2 | 34 | 9 | +5.89% |
| C1-IB | ON | 48 | 9 | -2.26% |
| C2-SS | OFF:G1 | 4 | 2 | +10.69% |
| C2-SS | OFF:G2 | 31 | 8 | +3.92% |
| C2-SS | ON | 46 | 9 | +0.70% |
| C2-IB | OFF:G1 | 4 | 2 | +14.50% |
| C2-IB | OFF:G2 | 31 | 8 | +3.02% |
| C2-IB | ON | 46 | 9 | -2.25% |


## Stratum: month (descriptive; cannot promote)

| pair | stratum | n | weeks | mean_ror |
|---|---|---|---|---|
| C1-SS | 2026-03 | 15 | 3 | -0.64% |
| C1-SS | 2026-05 | 16 | 4 | +9.43% |
| C1-SS | 2026-06 | 16 | 4 | +6.10% |
| C1-SS | 2026-07 | 6 | 2 | -11.72% |
| C1-SS | 2026-08 | 15 | 3 | +5.72% |
| C1-SS | 2026-09 | 19 | 4 | -1.58% |
| C1-IB | 2026-03 | 15 | 3 | -5.67% |
| C1-IB | 2026-05 | 16 | 4 | +12.80% |
| C1-IB | 2026-06 | 16 | 4 | +7.96% |
| C1-IB | 2026-07 | 6 | 2 | -13.64% |
| C1-IB | 2026-08 | 15 | 3 | +5.37% |
| C1-IB | 2026-09 | 19 | 4 | -6.11% |
| C2-SS | 2026-03 | 14 | 3 | +6.92% |
| C2-SS | 2026-05 | 15 | 4 | +8.06% |
| C2-SS | 2026-06 | 15 | 3 | +5.26% |
| C2-SS | 2026-07 | 5 | 2 | +2.32% |
| C2-SS | 2026-08 | 15 | 3 | -4.62% |
| C2-SS | 2026-09 | 17 | 4 | -2.51% |
| C2-IB | 2026-03 | 14 | 3 | +7.70% |
| C2-IB | 2026-05 | 15 | 4 | +10.44% |
| C2-IB | 2026-06 | 15 | 3 | +6.80% |
| C2-IB | 2026-07 | 5 | 2 | +4.16% |
| C2-IB | 2026-08 | 15 | 3 | -13.95% |
| C2-IB | 2026-09 | 17 | 4 | -7.66% |


## Funnel: suppressed names by first failing filter (all weeks)

| variant | reason | n |
|---|---|---|
| C1 | F10 | 43 |
| C2 | C2_sector | 33 |
| C2 | F10 | 17 |
| all | F1 | 73714 |
| all | F2 | 30659 |
| all | F3 | 29632 |
| all | F4 | 22129 |
| all | F5 | 4382 |
| all | F6 | 3328 |
| all | F7 | 7356 |
| all | F8 | 8991 |
| all | F9 | 273 |


## Go / no-go (DESIGN/90 §6; forward t >= 2.0; criterion 4 on the null benchmark)

| pair | variant | structure | forward_weeks | required | status | scale_required | verdict | note |
|---|---|---|---|---|---|---|---|---|
| C1-SS | C1 | SS | 0 | 40 | NOT DUE | 80 | NOT DUE | 0 of 40 graded forward entry-weeks |
| C1-IB | C1 | IB | 0 | 40 | NOT DUE | 80 | NOT DUE | 0 of 40 graded forward entry-weeks |
| C2-SS | C2 | SS | 0 | 40 | NOT DUE | 80 | NOT DUE | 0 of 40 graded forward entry-weeks |
| C2-IB | C2 | IB | 0 | 40 | NOT DUE | 80 | NOT DUE | 0 of 40 graded forward entry-weeks |
