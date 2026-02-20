import pandas as pd
import numpy as np
from sklearn.covariance import LedoitWolf, OAS

def ledoit_wolf(returns):
    if not isinstance(returns, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    r = returns.dropna().astype(float).values
    lw = LedoitWolf().fit(r)
    return pd.DataFrame(lw.covariance_, index=returns.columns, columns=returns.columns)

def oas_shrinkage(returns):
    if not isinstance(returns, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    r = returns.dropna().astype(float).values
    o = OAS().fit(r)
    return pd.DataFrame(o.covariance_, index=returns.columns, columns=returns.columns)

def diagonal_shrinkage(returns, alpha):
    if not isinstance(returns, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    if not 0 <= alpha <= 1:
        raise ValueError("alpha must be between 0 and 1")
    r = returns.dropna().astype(float)
    cov = r.cov().values
    diag = np.diag(np.diag(cov))
    shrunk = alpha * diag + (1 - alpha) * cov
    return pd.DataFrame(shrunk, index=returns.columns, columns=returns.columns)