import pandas as pd
import numpy as np
import pytest
from src.volatility.rolling_vol import rolling_std, ewma_vol, realized_vol

def test_rolling_std_basic():
    s = pd.Series([0.01, 0.02, -0.01, 0.03, 0.00])
    out = rolling_std(s, window=2)
    assert isinstance(out, pd.Series)
    assert len(out) == len(s)
    assert out.iloc[2] >= 0

def test_ewma_vol_basic():
    s = pd.Series([0.01, 0.02, -0.01, 0.03, 0.00])
    out = ewma_vol(s, span=3)
    assert isinstance(out, pd.Series)
    assert len(out) == len(s)
    assert np.all(out.dropna() >= 0)

def test_realized_vol_basic():
    s = pd.Series([0.01, 0.02, -0.01, 0.03, 0.00])
    out = realized_vol(s, window=2)
    assert isinstance(out, pd.Series)
    assert len(out) == len(s)
    assert out.iloc[2] >= 0

def test_type_errors():
    with pytest.raises(TypeError):
        rolling_std([1, 2, 3], window=2)
    with pytest.raises(TypeError):
        ewma_vol([1, 2, 3], span=3)
    with pytest.raises(TypeError):
        realized_vol([1, 2, 3], window=2)