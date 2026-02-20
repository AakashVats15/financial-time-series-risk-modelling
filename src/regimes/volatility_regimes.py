import pandas as pd
import numpy as np
from statsmodels.tsa.regime_switching.markov_regression import MarkovRegression

def zscore_regimes(series, window):
    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series")
    s = series.dropna().astype(float)
    vol = s.rolling(window).std().dropna()
    z = (vol - vol.mean()) / vol.std()
    reg = pd.Series(np.where(z > 1, 1, np.where(z < -1, -1, 0)), index=z.index)
    return reg

def markov_vol_regimes(series, k=2):
    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series")
    s = series.dropna().astype(float)
    model = MarkovRegression(s, k_regimes=k, trend="c", switching_variance=True)
    res = model.fit()
    return res.smoothed_marginal_probabilities