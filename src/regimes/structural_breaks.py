import pandas as pd
import numpy as np
import ruptures as rpt

def mean_shift_breaks(series, model="l2", penalty=3):
    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series")
    s = series.dropna().astype(float).values
    algo = rpt.Pelt(model=model).fit(s)
    bk = algo.predict(pen=penalty)
    return bk

def volatility_breaks(series, window=20, model="l2", penalty=3):
    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series")
    s = series.dropna().astype(float)
    vol = s.rolling(window).std().dropna().values
    algo = rpt.Pelt(model=model).fit(vol)
    bk = algo.predict(pen=penalty)
    return bk