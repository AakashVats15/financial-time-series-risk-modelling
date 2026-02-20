import pandas as pd
import numpy as np

def portfolio_variance(cov, weights):
    if not isinstance(cov, pd.DataFrame):
        raise TypeError("cov must be a pandas DataFrame")
    w = np.asarray(weights, dtype=float).reshape(-1, 1)
    if w.shape[0] != cov.shape[0]:
        raise ValueError("weights length must match cov dimension")
    c = cov.values
    return float(w.T @ c @ w)

def portfolio_volatility(cov, weights):
    v = portfolio_variance(cov, weights)
    return float(np.sqrt(v))

def scenario_variance(cov_scenarios, weights):
    if not isinstance(cov_scenarios, dict):
        raise TypeError("cov_scenarios must be a dict of DataFrames")
    out = {}
    for name, cov in cov_scenarios.items():
        out[name] = portfolio_variance(cov, weights)
    return out

def scenario_volatility(cov_scenarios, weights):
    v = scenario_variance(cov_scenarios, weights)
    return {k: float(np.sqrt(val)) for k, val in v.items()}