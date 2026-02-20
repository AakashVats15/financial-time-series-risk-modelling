import pandas as pd
import numpy as np
import pytest
from src.portfolio.portfolio_variance import portfolio_variance, portfolio_volatility, scenario_variance, scenario_volatility

def test_portfolio_variance_scalar():
    cov = pd.DataFrame([[0.04, 0.01], [0.01, 0.09]])
    w = [0.5, 0.5]
    v = portfolio_variance(cov, w)
    assert isinstance(v, float)
    assert v >= 0

def test_portfolio_volatility_relation():
    cov = pd.DataFrame([[0.04, 0.01], [0.01, 0.09]])
    w = [0.5, 0.5]
    v = portfolio_variance(cov, w)
    s = portfolio_volatility(cov, w)
    assert np.isclose(s, np.sqrt(v))

def test_scenario_variance_structure():
    cov = pd.DataFrame([[0.04, 0.01], [0.01, 0.09]])
    scenarios = {
        "base": cov,
        "stress_up": cov * 1.5,
        "stress_down": cov * 0.7
    }
    w = [0.5, 0.5]
    out = scenario_variance(scenarios, w)
    assert isinstance(out, dict)
    assert set(out.keys()) == {"base", "stress_up", "stress_down"}

def test_scenario_volatility_structure():
    cov = pd.DataFrame([[0.04, 0.01], [0.01, 0.09]])
    scenarios = {
        "base": cov,
        "stress_up": cov * 1.5,
        "stress_down": cov * 0.7
    }
    w = [0.5, 0.5]
    out = scenario_volatility(scenarios, w)
    assert isinstance(out, dict)
    assert set(out.keys()) == {"base", "stress_up", "stress_down"}

def test_type_errors():
    with pytest.raises(TypeError):
        portfolio_variance([1, 2, 3], [0.5, 0.5])
    with pytest.raises(TypeError):
        portfolio_volatility([1, 2, 3], [0.5, 0.5])
    with pytest.raises(TypeError):
        scenario_variance("not a dict", [0.5, 0.5])
    with pytest.raises(TypeError):
        scenario_volatility("not a dict", [0.5, 0.5])