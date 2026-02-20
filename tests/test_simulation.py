import pandas as pd
import numpy as np
import pytest
from src.simulation.correlated_mc import cholesky_simulation, pca_simulation

def test_cholesky_simulation_shape():
    np.random.seed(0)
    cov = pd.DataFrame([[0.04, 0.01], [0.01, 0.09]])
    out = cholesky_simulation(cov, n_samples=1000)
    assert isinstance(out, pd.DataFrame)
    assert out.shape == (1000, 2)
    assert not out.isna().any().any()

def test_pca_simulation_shape():
    np.random.seed(0)
    cov = pd.DataFrame([[0.04, 0.01], [0.01, 0.09]])
    out = pca_simulation(cov, n_samples=1000, variance_cutoff=0.95)
    assert isinstance(out, pd.DataFrame)
    assert out.shape == (1000, 2)
    assert not out.isna().any().any()

def test_type_errors():
    with pytest.raises(TypeError):
        cholesky_simulation([1, 2, 3], n_samples=100)
    with pytest.raises(TypeError):
        pca_simulation([1, 2, 3], n_samples=100, variance_cutoff=0.95)