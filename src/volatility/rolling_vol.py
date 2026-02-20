import pandas as pd
import numpy as np

def rolling_std(series, window):
    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series")
    s = series.dropna().astype(float)
    return s.rolling(window).std().dropna()

def ewma_vol(series, span):
    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series")
    s = series.dropna().astype(float)
    return s.ewm(span=span, adjust=False).std().dropna()

def realized_vol(series, window):
    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series")
    s = series.dropna().astype(float)
    r2 = s.pow(2)
    return r2.rolling(window).sum().pow(0.5).dropna()