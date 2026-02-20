from src.utils.data_loader import load_returns
from src.volatility.rolling_vol import rolling_std, ewma_vol, realized_vol

r = load_returns("data/processed/asset.csv")

roll = rolling_std(r, window=20)
ewma = ewma_vol(r, span=20)
realized = realized_vol(r, window=20)

print(roll.tail())
print(ewma.tail())
print(realized.tail())