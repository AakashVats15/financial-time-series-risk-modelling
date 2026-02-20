from src.utils.data_loader import load_returns
from src.regimes.volatility_regimes import zscore_regimes, markov_vol_regimes
from src.regimes.structural_breaks import mean_shift_breaks, volatility_breaks

r = load_returns("data/processed/asset.csv")

z = zscore_regimes(r, window=20)
m = markov_vol_regimes(r, k=2)
b1 = mean_shift_breaks(r)
b2 = volatility_breaks(r, window=20)

print(z.tail())
print(m)
print(b1)
print(b2)