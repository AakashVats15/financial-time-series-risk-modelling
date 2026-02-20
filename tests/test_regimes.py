import pandas as pd
import numpy as np
import pytest
from src.regimes.volatility_regimes import zscore_regimes, markov_vol_regimes
from src.regimes.structural_breaks import mean_shift_breaks, volatility_breaks

def test_zscore_regimes_basic():
    s = pd.Series([0.01, 0.02, -0.01, 0.03, 0.00])
    out = zscore_regimes(s, window=2)
    assert isinstance(out, pd.Series)
    assert len(out) == len(s)
    assert out.dropna().isin([0, 1]).all()

def test_markov_vol_regimes_basic():
    np.random.seed(0)
    s = pd.Series([0.01, 0.02, -0.01, 0.03, 0.00, 0.02, -0.02])
    out = markov_vol_regimes(s, k=2)
    assert isinstance(out, pd.Series)
    assert len(out) == len(s)
    assert out.dropna().isin([0, 1]).all()

def test_mean_shift_breaks_output():
    s = pd.Series([0.01, 0.01, 0.01, 0.10, 0.10, 0.10])
    out = mean_shift_breaks(s)
    assert isinstance(out, list)

def test_volatility_breaks_output():
    s = pd.Series([0.01, 0.02, -0.01, 0.20, -0.15, 0.18])
    out = volatility_breaks(s, window=2)
    assert isinstance(out, list)

def test_type_errors():
    with pytest.raises(TypeError):
        zscore_regimes([1, 2, 3], window=2)
    with pytest.raises(TypeError):
        markov_vol_regimes([1, 2, 3], k=2)
    with pytest.raises(TypeError):
        mean_shift_breaks([1, 2, 3])
    with pytest.raises(TypeError):
        volatility_breaks([1, 2, 3], window=2)