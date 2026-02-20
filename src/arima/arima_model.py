import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def fit_arima(series, order):
    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series")
    s = series.dropna().astype(float)
    model = ARIMA(s, order=order)
    res = model.fit()
    return res

def forecast(model_result, steps):
    f = model_result.get_forecast(steps=steps)
    mean = f.predicted_mean
    conf = f.conf_int()
    return mean, conf

def arima_diagnostics(model_result):
    return {
        "aic": model_result.aic,
        "bic": model_result.bic,
        "hqic": model_result.hqic,
        "residuals": model_result.resid
    }