import pandas as pd
from statsmodels.tsa.stattools import kpss

def kpss_test(series, regression="c", nlags="auto"):
    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series")
    s = series.dropna().astype(float)
    stat, p, lags, crit = kpss(s, regression=regression, nlags=nlags)
    return {
        "statistic": stat,
        "pvalue": p,
        "lags": lags,
        "critical_values": crit
    }