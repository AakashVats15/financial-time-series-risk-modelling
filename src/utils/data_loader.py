import pandas as pd
import numpy as np
from pathlib import Path

def load_csv(path, parse_dates=True, index_col=None):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return pd.read_csv(p, parse_dates=parse_dates, index_col=index_col)

def load_returns(path, price_col="Close"):
    df = load_csv(path, parse_dates=True, index_col=0)
    if price_col not in df.columns:
        raise ValueError(f"{price_col} not in columns")
    s = df[price_col].astype(float)
    r = np.log(s / s.shift(1)).dropna()
    return r

def load_multi_asset_returns(paths, price_col="Close"):
    data = {}
    for name, path in paths.items():
        r = load_returns(path, price_col=price_col)
        data[name] = r
    df = pd.DataFrame(data).dropna()
    return df

def ensure_datetime_index(df):
    if not isinstance(df.index, pd.DatetimeIndex):
        df.index = pd.to_datetime(df.index)
    return df

def align_series(series_list):
    df = pd.concat(series_list, axis=1).dropna()
    return df