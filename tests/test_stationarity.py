import pandas as pd
import pytest
from src.stationarity.adf_test import adf
from src.stationarity.kpss_test import kpss_test

def test_adf_output_structure():
    s = pd.Series([0.01, 0.02, -0.01, 0.03, 0.00])
    out = adf(s)
    assert isinstance(out, dict)
    assert "statistic" in out
    assert "pvalue" in out
    assert "lags" in out
    assert "nobs" in out

def test_kpss_output_structure():
    s = pd.Series([0.01, 0.02, -0.01, 0.03, 0.00])
    out = kpss_test(s)
    assert isinstance(out, dict)
    assert "statistic" in out
    assert "pvalue" in out
    assert "lags" in out
    assert "nobs" in out

def test_adf_type_error():
    with pytest.raises(TypeError):
        adf([1, 2, 3])

def test_kpss_type_error():
    with pytest.raises(TypeError):
        kpss_test([1, 2, 3])