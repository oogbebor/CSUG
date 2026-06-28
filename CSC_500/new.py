import numpy as np
import pandas as pd
from scipy import stats

np.random.seed(20260425)
n = 80

# Simulate baseline RUM and browser-error metrics.
clicks_before = np.random.poisson(4.5, n) + 4
frustration_before = np.random.poisson(1.2, n)
errors_before = np.random.poisson(0.75, n)
load_before = np.random.normal(2350, 420, n).round().astype(int)

sat_before = (88 - 1.8*clicks_before - 4.2*frustration_before
              - 5.0*errors_before - 0.001*(load_before - 2000)
              + np.random.normal(0, 5, n))
sat_before = np.clip(sat_before, 45, 98)

# Simulate after-update values for the same users.
click_reduction = np.random.poisson(1.3, n)
clicks_after = np.maximum(2, clicks_before - click_reduction + np.random.binomial(1, 0.15, n))
frustration_after = np.maximum(0, frustration_before
                               - np.random.binomial(frustration_before, 0.45)
                               + np.random.binomial(1, 0.25, n))
errors_after = np.maximum(0, errors_before
                          - np.random.binomial(errors_before, 0.50)
                          + np.random.binomial(1, 0.20, n))
load_after = np.random.normal(2220, 380, n).round().astype(int)

sat_after = (90 - 1.7*clicks_after - 4.3*frustration_after
             - 5.3*errors_after - 0.001*(load_after - 2000)
             + np.random.normal(0, 5, n))
sat_after = np.clip(sat_after, 45, 100)

# Build paired dataset.
df = pd.DataFrame({
    'user_id': [f'SC-{i:03d}' for i in range(1, n+1)],
    'region': 'South Central',
    'clicks_before': clicks_before,
    'clicks_after': clicks_after,
    'frustration_events_before': frustration_before,
    'frustration_events_after': frustration_after,
    'browser_errors_before': errors_before,
    'browser_errors_after': errors_after,
    'page_load_ms_before': load_before,
    'page_load_ms_after': load_after,
    'satisfaction_before': np.round(sat_before, 1),
    'satisfaction_after': np.round(sat_after, 1)
})
df['satisfaction_change'] = df['satisfaction_after'] - df['satisfaction_before']

# Estimation and paired t-test.
diff = df['satisfaction_change']
mean_diff = diff.mean()
sd_diff = diff.std(ddof=1)
se_diff = sd_diff / np.sqrt(n)
t_crit = stats.t.ppf(0.975, n-1)
ci = (mean_diff - t_crit*se_diff, mean_diff + t_crit*se_diff)
t_stat, p_value = stats.ttest_rel(df['satisfaction_after'], df['satisfaction_before'])

print('Mean difference:', round(mean_diff, 2))
print('95% CI:', [round(ci[0], 2), round(ci[1], 2)])
print('t statistic:', round(t_stat, 2))
print('p value:', p_value)
print(df)