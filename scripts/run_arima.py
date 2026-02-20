from src.utils.data_loader import load_returns
from src.arima.arima_model import fit_arima, forecast, arima_diagnostics

r = load_returns("data/processed/asset.csv")

m = fit_arima(r, order=(1, 0, 1))
f_mean, f_conf = forecast(m, steps=10)
d = arima_diagnostics(m)

print(f_mean)
print(f_conf)
print(d)