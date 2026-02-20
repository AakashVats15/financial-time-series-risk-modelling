import pandas as pd
import numpy as np

def empirical_cov(returns):
    if not isinstance(returns, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    r = returns.dropna().astype(float)
    return r.cov()

def empirical_corr(returns):
    if not isinstance(returns, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    r = returns.dropna().astype(float)
    return r.corr()

def annualized_cov(returns, periods=252):
    if not isinstance(returns, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    r = returns.dropna().astype(float)
    return r.cov() * periods

def annualized_vol(returns, periods=252):
    if not isinstance(returns, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    r = returns.dropna().astype(float)
    return r.std() * np.sqrt(periods)