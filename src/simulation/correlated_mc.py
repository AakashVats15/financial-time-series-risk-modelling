import pandas as pd
import numpy as np

def cholesky_simulation(cov, n_samples):
    if not isinstance(cov, pd.DataFrame):
        raise TypeError("cov must be a pandas DataFrame")
    c = cov.values
    L = np.linalg.cholesky(c)
    z = np.random.randn(n_samples, c.shape[0])
    r = z @ L.T
    return pd.DataFrame(r, columns=cov.columns)

def pca_simulation(cov, n_samples, variance_cutoff=0.99):
    if not isinstance(cov, pd.DataFrame):
        raise TypeError("cov must be a pandas DataFrame")
    c = cov.values
    vals, vecs = np.linalg.eigh(c)
    idx = vals.argsort()[::-1]
    vals = vals[idx]
    vecs = vecs[:, idx]
    cum = np.cumsum(vals) / np.sum(vals)
    k = np.searchsorted(cum, variance_cutoff) + 1
    L = vecs[:, :k] @ np.diag(np.sqrt(vals[:k]))
    z = np.random.randn(n_samples, k)
    r = z @ L.T
    return pd.DataFrame(r, columns=cov.columns)