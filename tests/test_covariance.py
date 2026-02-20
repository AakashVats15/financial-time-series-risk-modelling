import pandas as pd
import numpy as np
import pytest
from src.covariance.empirical_cov import empirical_cov, empirical_corr, annualized_cov, annualized_vol
from src.covariance.shrinkage_methods import ledoit_wolf, oas_shrinkage, diagonal_shrinkage

def test_empirical_cov_shape():
    df = pd.DataFrame({
        "a": [0.01, 0.02, -0.01, 0.03],
        "b": [0.00, -0.01, 0.02, 0.01]
    })
    cov = empirical_cov(df)
    assert cov.shape == (2, 2)
    assert isinstance(cov, pd.DataFrame)

def test_empirical_corr_values():
    df = pd.DataFrame({
        "a": [0.01, 0.02, -0.01, 0.03],
        "b": [0.00, -0.01, 0.02, 0.01]
    })
    corr = empirical_corr(df)
    assert corr.shape == (2, 2)
    assert np.all(corr.values <= 1)
    assert np.all(corr.values >= -1)

def test_annualized_cov_and_vol():
    df = pd.DataFrame({
        "a": [0.01, 0.02, -0.01, 0.03],
        "b": [0.00, -0.01, 0.02, 0.01]
    })
    cov = annualized_cov(df)
    vol = annualized_vol(df)
    assert cov.shape == (2, 2)
    assert isinstance(vol, pd.Series)
    assert np.all(vol >= 0)

def test_shrinkage_methods_output():
    df = pd.DataFrame({
        "a": [0.01, 0.02, -0.01, 0.03],
        "b": [0.00, -0.01, 0.02, 0.01]
    })
    lw = ledoit_wolf(df)
    oas = oas_shrinkage(df)
    diag = diagonal_shrinkage(df, alpha=0.5)
    assert lw.shape == (2, 2)
    assert oas.shape == (2, 2)
    assert diag.shape == (2, 2)

def test_type_errors():
    with pytest.raises(TypeError):
        empirical_cov([1, 2, 3])
    with pytest.raises(TypeError):
        empirical_corr([1, 2, 3])
    with pytest.raises(TypeError):
        annualized_cov([1, 2, 3])
    with pytest.raises(TypeError):
        annualized_vol([1, 2, 3])
    with pytest.raises(TypeError):
        ledoit_wolf([1, 2, 3])
    with pytest.raises(TypeError):
        oas_shrinkage([1, 2, 3])
    with pytest.raises(TypeError):
        diagonal_shrinkage([1, 2, 3], alpha=0.5)