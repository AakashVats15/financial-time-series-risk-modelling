import pandas as pd
from statsmodels.tsa.stattools import adfuller

def adf(series, autolag="AIC"):
    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series")
    s = series.dropna().astype(float)
    stat, p, lags, nobs, crit, _ = adfuller(s, autolag=autolag)
    return {
        "statistic": stat,
        "pvalue": p,
        "lags": lags,
        "nobs": nobs,
        "critical_values": crit
    }