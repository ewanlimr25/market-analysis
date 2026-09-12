# S-C R1 descriptive: E2's F3 / F6 under RV5 (generated)

Forward 21-session windows on `intraday_rv` quality rows (54,716 windows, 684 names, 82 entry dates, 6 months); VRP = iv30d − realized, vol points; `t_month` clusters on the month of T (DESIGN/90 §0 note, 2026-09-07). Earnings-free = no `earnings_events` print inside the window. Descriptive only: F3 and F6 stand as written.

| stratum | n | months | iv30d_med | rv5_med | c2c_med | vrp_rv5_mean | vrp_rv5_med | iv_gt_rv5 | t_month_rv5 | vrp_c2c_mean | vrp_c2c_med | iv_gt_c2c | t_month_c2c |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| all windows | 44273 | 6 | +55.95% | +40.36% | +52.14% | 7.27 | 13.64 | +96.21% | 0.7695 | 1.89 | 2.96 | +60.87% | 0.9700 |
| earnings-free | 27715 | 6 | +52.33% | +39.20% | +48.92% | -0.6688 | 11.63 | +95.79% | -0.0575 | 1.87 | 2.46 | +59.82% | 0.9288 |
| earnings-free, mcap < $1B | 917 | 6 | +112.20% | +85.00% | +105.47% | 21.54 | 21.47 | +84.08% | 3.53 | 1.41 | 6.91 | +57.91% | 0.1752 |
| earnings-free, mcap $1B to $20B (F3) | 11717 | 6 | +70.94% | +54.22% | +65.27% | -17.33 | 15.72 | +95.36% | -0.6450 | 4.00 | 5.08 | +64.55% | 1.68 |
| earnings-free, mcap > $20B | 15081 | 6 | +37.54% | +27.61% | +35.66% | 10.92 | 9.34 | +96.83% | 8.30 | 0.2318 | 1.29 | +56.26% | 0.1478 |
| earnings-free, iv30d < 30% | 4574 | 6 | +25.81% | +19.90% | +24.71% | 4.85 | 4.97 | +93.33% | 8.48 | -0.3824 | 0.3083 | +52.30% | -0.3810 |
| earnings-free, iv30d 30% to 80% (F6) | 16659 | 6 | +49.74% | +36.76% | +46.02% | 12.25 | 11.57 | +96.66% | 10.19 | 1.51 | 2.60 | +60.77% | 0.7822 |
| earnings-free, iv30d > 80% | 6482 | 6 | +99.49% | +75.95% | +94.84% | -37.77 | 25.14 | +95.26% | -0.8040 | 4.38 | 7.31 | +62.68% | 1.32 |
| earnings-free, F3 and F6 (the S-C band) | 6831 | 6 | +59.06% | +45.14% | +53.55% | 12.96 | 12.82 | +95.15% | 9.45 | 2.76 | 3.88 | +63.11% | 1.28 |
