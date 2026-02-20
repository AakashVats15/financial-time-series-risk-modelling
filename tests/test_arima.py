import pandas as pd
import pytest
from src.arima.arima_model import fit_arima, forecast, arima_diagnostics

def test_fit_arima_model():
    s = pd.Series([0.01, 0.02, -0.01, 0.03, 0.00, 0.01])
    m = fit_arima(s, order=(1, 0, 1))
    assert m is not None

def test_arima_forecast_shapes():
    s = pd.Series([0.01, 0.02, -0.01, 0.03, 0.00, 0.01])
    m = fit_arima(s, order=(1, 0, 1))
    mean, conf = forecast(m, steps=3)
    assert len(mean) == 3
    assert conf.shape == (3, 2)

def test_arima_diagnostics_structure():
    s = pd.Series([0.01, 0.02, -0.01, 0.03, 0.00, 0.01])
    m = fit_arima(s, order=(1, 0, 1))
    d = arima_diagnostics(m)
    assert isinstance(d, dict)
    assert "aic" in d
    assert "bic" in d
    assert "hqic" in d

def test_arima_type_error():
    with pytest.raises(TypeError):
        fit_arima([1, 2, 3], order=(1, 0, 1))