# S-G backtest report (generated, DESIGN/91)


## Filter funnel by entry offset

3260 events x 2 entry offsets evaluated.

**offset −3**: LS traded 56, LG traded 24 (LG dropped 32: {'illiquid_strangle_leg': 32})

| filter | first_fail_count |
|---|---|
| F1 | 0 |
| F2 | 169 |
| F3 | 731 |
| F4 | 420 |
| F5 | 1817 |
| F6 | 57 |
| F7 | 7 |
| F8 | 3 |

**offset −5**: LS traded 32, LG traded 12 (LG dropped 20: {'illiquid_strangle_leg': 20})

| filter | first_fail_count |
|---|---|
| F1 | 0 |
| F2 | 169 |
| F3 | 731 |
| F4 | 420 |
| F5 | 1887 |
| F6 | 16 |
| F7 | 3 |
| F8 | 2 |


## Marks and tiers by (offset, structure)

| variant | structure | n | entry_tier1 | entry_model | exit_tier1 | exit_tier2 | exit_model | mean_atm_spread_entry | median_dte |
|---|---|---|---|---|---|---|---|---|---|
| G3_3 | LG | 24 | 24 | 0 | 24 | 0 | 0 | 0.0415 | 5.00 |
| G3_3 | LS | 56 | 56 | 0 | 51 | 5 | 0 | 0.0498 | 6.00 |
| G3_5 | LG | 12 | 12 | 0 | 10 | 1 | 1 | 0.0443 | 8.00 |
| G3_5 | LS | 32 | 32 | 0 | 25 | 5 | 2 | 0.0490 | 9.00 |


## Primary table: mean net P&L in % of spot, t clustered by entry day

| variant | structure | season | n | dates | mean_net_pct | median_net_pct | hit | t | p | mean_gross_pct | mean_cost_pct |
|---|---|---|---|---|---|---|---|---|---|---|---|
| G3_3 | LS | S1 | 26 | 11 | -0.57% | -1.02% | 0.2692 | -1.45 | 0.1772 | +0.32% | +0.89% |
| G3_3 | LG | S1 | 9 | 6 | -1.03% | -1.19% | 0.2222 | -2.65 | 0.0456 | -0.51% | +0.52% |
| G3_5 | LS | S1 | 13 | 6 | -0.70% | -0.64% | 0.4615 | -0.6899 | 0.5210 | +0.41% | +1.11% |
| G3_5 | LG | S1 | 4 | 3 | +1.10% | +0.69% | 0.7500 | 0.5823 | 0.6193 | +2.05% | +0.95% |
| G3_3 | LS | S2 | 24 | 13 | -1.41% | -1.38% | 0.0833 | -5.31 | 0.0002 | -0.62% | +0.79% |
| G3_3 | LG | S2 | 10 | 8 | -1.23% | -1.24% | 0.2000 | -3.39 | 0.0115 | -0.35% | +0.89% |
| G3_5 | LS | S2 | 16 | 11 | -1.32% | -1.39% | 0.3125 | -1.89 | 0.0880 | -0.44% | +0.88% |
| G3_5 | LG | S2 | 8 | 7 | -2.14% | -2.37% | 0.1250 | -2.14 | 0.0758 | -1.42% | +0.72% |
| G3_3 | LS | pooled | 56 | 30 | -0.96% | -1.02% | 0.1786 | -3.98 | 0.0004 | -0.13% | +0.83% |
| G3_3 | LG | pooled | 24 | 19 | -1.13% | -1.15% | 0.2083 | -5.05 | 0.0001 | -0.43% | +0.70% |
| G3_5 | LS | pooled | 32 | 20 | -1.05% | -1.03% | 0.3438 | -1.91 | 0.0710 | -0.11% | +0.93% |
| G3_5 | LG | pooled | 12 | 10 | -1.06% | -1.81% | 0.3333 | -0.9502 | 0.3668 | -0.26% | +0.80% |


## BH(0.1) across the four primary tests — S1

| variant | structure | n | mean_net_pct | t | p | bh_pass |
|---|---|---|---|---|---|---|
| G3_3 | LS | 26 | -0.57% | -1.45 | 0.1772 | no |
| G3_3 | LG | 9 | -1.03% | -2.65 | 0.0456 | no |
| G3_5 | LS | 13 | -0.70% | -0.6899 | 0.5210 | no |
| G3_5 | LG | 4 | +1.10% | 0.5823 | 0.6193 | no |


## BH(0.1) across the four primary tests — S2

| variant | structure | n | mean_net_pct | t | p | bh_pass |
|---|---|---|---|---|---|---|
| G3_3 | LS | 24 | -1.41% | -5.31 | 0.0002 | yes |
| G3_3 | LG | 10 | -1.23% | -3.39 | 0.0115 | yes |
| G3_5 | LS | 16 | -1.32% | -1.89 | 0.0880 | yes |
| G3_5 | LG | 8 | -2.14% | -2.14 | 0.0758 | yes |


## BH(0.1) across the four primary tests — pooled

| variant | structure | n | mean_net_pct | t | p | bh_pass |
|---|---|---|---|---|---|---|
| G3_3 | LS | 56 | -0.96% | -3.98 | 0.0004 | yes |
| G3_3 | LG | 24 | -1.13% | -5.05 | 0.0001 | yes |
| G3_5 | LS | 32 | -1.05% | -1.91 | 0.0710 | yes |
| G3_5 | LG | 12 | -1.06% | -0.9502 | 0.3668 | no |


## Deflated Sharpe (10 trials) — S1

| variant | structure | n | sr | sr_star | deflated_sr | dsr_prob | skew | kurt |
|---|---|---|---|---|---|---|---|---|
| G3_3 | LS | 26 | -0.2349 | 0.7900 | -1.02 | 0.0000 | 1.20 | 3.79 |
| G3_3 | LG | 9 | -0.9297 | 0.7900 | -1.72 | 0.0000 | 0.0752 | 1.25 |
| G3_5 | LS | 13 | -0.1331 | 0.7900 | -0.9231 | 0.0006 | -0.1916 | 3.33 |
| G3_5 | LG | 4 | 0.2786 | 0.7900 | -0.5114 | 0.1749 | 0.6099 | 4.49 |


## Deflated Sharpe (10 trials) — S2

| variant | structure | n | sr | sr_star | deflated_sr | dsr_prob | skew | kurt |
|---|---|---|---|---|---|---|---|---|
| G3_3 | LS | 24 | -1.21 | 0.4740 | -1.69 | 0.0000 | -0.3896 | 2.92 |
| G3_3 | LG | 10 | -0.9869 | 0.4740 | -1.46 | 0.0010 | 0.4332 | 3.39 |
| G3_5 | LS | 16 | -0.5011 | 0.4740 | -0.9751 | 0.0001 | -0.1601 | 3.11 |
| G3_5 | LG | 8 | -0.8069 | 0.4740 | -1.28 | 0.0162 | 0.9546 | 5.53 |


## Deflated Sharpe (10 trials) — pooled

| variant | structure | n | sr | sr_star | deflated_sr | dsr_prob | skew | kurt |
|---|---|---|---|---|---|---|---|---|
| G3_3 | LS | 56 | -0.5188 | 0.5189 | -1.04 | 0.0000 | 1.52 | 6.29 |
| G3_3 | LG | 24 | -0.9946 | 0.5189 | -1.51 | 0.0000 | 0.0622 | 2.39 |
| G3_5 | LS | 32 | -0.2774 | 0.5189 | -0.7963 | 0.0000 | -0.0396 | 4.58 |
| G3_5 | LG | 12 | -0.3155 | 0.5189 | -0.8344 | 0.0090 | 0.9334 | 3.93 |


## PBO (CSCV over entry-day blocks, pooled)

- pbo: 0.02703962703962704
- mean_logit: 1.0379574997451817
- n_combinations: 12870
- n_configs: 4
- n_blocks: 16
- n_dates: 40


## Tail report — pooled

| variant | structure | n | mean_net_pct | worst_event_pct | best_event_pct | mean_win_pct | worst_to_mean_win | worst_decile_share_of_loss | mean_without_worst_1pct | mean_without_best_1pct | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| G3_3 | LS | 56 | -0.96% | -3.87% | +5.32% | +2.01% | 1.93 | 0.2428 | -0.91% | -1.08% | 1.52 | 3.29 |
| G3_3 | LG | 24 | -1.13% | -3.16% | +1.16% | +0.43% | 7.43 | 0.2106 | -1.05% | -1.23% | 0.0622 | -0.6122 |
| G3_5 | LS | 32 | -1.05% | -10.66% | +8.65% | +2.60% | 4.10 | 0.4123 | -0.74% | -1.36% | -0.0396 | 1.58 |
| G3_5 | LG | 12 | -1.06% | -6.00% | +6.29% | +2.73% | 2.20 | 0.2544 | -0.61% | -1.73% | 0.9334 | 0.9288 |


## Tail report — S1

| variant | structure | n | mean_net_pct | worst_event_pct | best_event_pct | mean_win_pct | worst_to_mean_win | worst_decile_share_of_loss | mean_without_worst_1pct | mean_without_best_1pct | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| G3_3 | LS | 26 | -0.57% | -3.87% | +5.32% | +2.70% | 1.43 | 0.2184 | -0.44% | -0.81% | 1.20 | 0.7933 |
| G3_3 | LG | 9 | -1.03% | -2.52% | +0.47% | +0.33% | 7.66 | 0.2533 | -0.85% | -1.22% | 0.0752 | -1.75 |
| G3_5 | LS | 13 | -0.70% | -10.66% | +8.65% | +3.42% | 3.11 | 0.3598 | +0.13% | -1.48% | -0.1916 | 0.3310 |
| G3_5 | LG | 4 | +1.10% | -3.27% | +6.29% | +2.56% | 1.28 | 1.00 | +2.56% | -0.63% | 0.6099 | 1.49 |


## Tail report — S2

| variant | structure | n | mean_net_pct | worst_event_pct | best_event_pct | mean_win_pct | worst_to_mean_win | worst_decile_share_of_loss | mean_without_worst_1pct | mean_without_best_1pct | skew | kurt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| G3_3 | LS | 24 | -1.41% | -3.71% | +0.88% | +0.55% | 6.79 | 0.2111 | -1.31% | -1.51% | -0.3896 | -0.0824 |
| G3_3 | LG | 10 | -1.23% | -3.16% | +1.16% | +0.59% | 5.35 | 0.2345 | -1.02% | -1.50% | 0.4332 | 0.3908 |
| G3_5 | LS | 16 | -1.32% | -6.53% | +3.69% | +1.62% | 4.05 | 0.2241 | -0.97% | -1.65% | -0.1601 | 0.1141 |
| G3_5 | LG | 8 | -2.14% | -6.00% | +3.24% | +3.24% | 1.85 | 0.2952 | -1.59% | -2.91% | 0.9546 | 2.53 |


## Spread halves (median atm_spread_entry on G3a-LS = 0.0501)

| half | variant | structure | n | mean_net_pct | t |
|---|---|---|---|---|---|
| low | G3_3 | LS | 28 | -0.71% | -2.39 |
| low | G3_3 | LG | 18 | -0.87% | -3.28 |
| low | G3_5 | LS | 18 | -0.19% | -0.1752 |
| low | G3_5 | LG | 10 | -0.70% | -0.5338 |
| wide | G3_3 | LS | 28 | -1.22% | -4.47 |
| wide | G3_3 | LG | 6 | -1.92% | -3.99 |
| wide | G3_5 | LS | 14 | -2.15% | -2.51 |
| wide | G3_5 | LG | 2 | -2.85% | -3.00 |


## Gross ramp decomposition (G3a-LS): by season

| season | unhedged_pnl_pct | delta_pnl_pct | delta_hedged_pnl_pct | vega_pnl_pct | residual_pnl_pct | net_pct | net_pct_prem | n |
|---|---|---|---|---|---|---|---|---|
| S1 | +0.32% | +0.20% | +0.11% | +3.60% | -3.48% | -0.0057 | -5.05% | 26 |
| S2 | -0.62% | +0.16% | -0.77% | +3.52% | -4.30% | -0.0141 | -11.59% | 24 |
| off | -0.13% | +0.09% | -0.21% | +2.97% | -3.19% | -0.0089 | -9.91% | 6 |


## Gross ramp decomposition (G3a-LS): by spread half

| spread_half | unhedged_pnl_pct | delta_pnl_pct | delta_hedged_pnl_pct | vega_pnl_pct | residual_pnl_pct | net_pct | net_pct_prem | n |
|---|---|---|---|---|---|---|---|---|
| low | -0.01% | +0.20% | -0.20% | +3.59% | -3.79% | -0.0071 | -6.41% | 28 |
| wide | -0.25% | +0.15% | -0.40% | +3.41% | -3.81% | -0.0122 | -10.33% | 28 |


## Go / no-go (DESIGN/91 §4)

| variant | structure | n_s1 | n_s2 | mean_s1 | mean_s2 | mean_pooled | t_pooled | mean_low_spread | mean_wide_spread | verdict | note |
|---|---|---|---|---|---|---|---|---|---|---|---|
| G3_3 | LS | 26 | 24 | -0.57% | -1.41% | -0.96% | -3.98 | -0.71% | -1.22% | KILLED | net <= 0 in Season 1 or Season 2 (DESIGN/91 §4 kill rule) |
| G3_3 | LG | 9 | 10 | -1.03% | -1.23% | -1.13% | -5.05 | -0.87% | -1.92% | KILLED | net <= 0 in Season 1 or Season 2 (DESIGN/91 §4 kill rule) |
| G3_5 | LS | 13 | 16 | -0.70% | -1.32% | -1.05% | -1.91 | -0.19% | -2.15% | KILLED | net <= 0 in Season 1 or Season 2 (DESIGN/91 §4 kill rule) |
| G3_5 | LG | 4 | 8 | +1.10% | -2.14% | -1.06% | -0.9502 | -0.70% | -2.85% | KILLED | net <= 0 in Season 1 or Season 2 (DESIGN/91 §4 kill rule) |
