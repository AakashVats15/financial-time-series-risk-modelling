import numpy as np
import pandas as pd
import os

RAW_DIR = r"E:\Personal\GitHub\Python Code Repo\financial-time-series-risk-modelling\data\raw"
PROCESSED_DIR = r"E:\Personal\GitHub\Python Code Repo\financial-time-series-risk-modelling\data\processed"

if not os.path.exists(PROCESSED_DIR):
    os.makedirs(PROCESSED_DIR)

def load_csv(name):
    path = os.path.join(RAW_DIR, name)
    return pd.read_csv(path, index_col=0, parse_dates=True)

returns_small = load_csv("returns_small.csv")
returns_medium = load_csv("returns_medium.csv")
regimes_example = load_csv("regimes_example.csv")
simulation_example = load_csv("simulation_example.csv")

returns_small_clean = returns_small.fillna(0)
returns_small_clean.to_csv(os.path.join(PROCESSED_DIR, "returns_small_clean.csv"))

returns_medium_clean = returns_medium.fillna(0)
returns_medium_clean.to_csv(os.path.join(PROCESSED_DIR, "returns_medium_clean.csv"))

log_returns_small = np.log1p(returns_small_clean)
log_returns_small.to_csv(os.path.join(PROCESSED_DIR, "log_returns_small.csv"))

log_returns_medium = np.log1p(returns_medium_clean)
log_returns_medium.to_csv(os.path.join(PROCESSED_DIR, "log_returns_medium.csv"))

cov_from_small = returns_small_clean.cov()
cov_from_small.to_csv(os.path.join(PROCESSED_DIR, "cov_from_returns_small.csv"))

cov_from_medium = returns_medium_clean.cov()
cov_from_medium.to_csv(os.path.join(PROCESSED_DIR, "cov_from_returns_medium.csv"))

regimes_clean = regimes_example.fillna(method="ffill").fillna(method="bfill")
regimes_clean.to_csv(os.path.join(PROCESSED_DIR, "regimes_example_clean.csv"))

simulation_clean = simulation_example.fillna(0)
simulation_clean.to_csv(os.path.join(PROCESSED_DIR, "simulation_example_clean.csv"))

print("Processed datasets saved to:", PROCESSED_DIR)
