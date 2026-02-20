from src.utils.data_loader import load_returns
from src.stationarity.adf_test import adf
from src.stationarity.kpss_test import kpss_test

r = load_returns("data/processed/asset.csv")
a = adf(r)
k = kpss_test(r)

print(a)
print(k)