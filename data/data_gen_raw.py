import numpy as np
import pandas as pd
import os

OUTPUT_DIR = r"E:\Personal\GitHub\Python Code Repo\financial-time-series-risk-modelling\data\raw"

np.random.seed(42)

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

dates_small = pd.date_range("2020-01-01", periods=10, freq="D")
returns_small = pd.DataFrame(
    {
        "A": np.round(np.random.normal(0.005, 0.005, 10), 4),
        "B": np.round(np.random.normal(0.003, 0.004, 10), 4),
        "C": np.round(np.random.normal(0.001, 0.003, 10), 4),
    },
    index=dates_small,
)
returns_small.index.name = "date"
returns_small.to_csv(os.path.join(OUTPUT_DIR, "returns_small.csv"))

dates_medium = pd.date_range("2020-01-01", periods=50, freq="D")
returns_medium = pd.DataFrame(
    {
        "A": np.round(np.random.normal(0.005, 0.01, 50), 4),
        "B": np.round(np.random.normal(0.004, 0.009, 50), 4),
        "C": np.round(np.random.normal(0.003, 0.008, 50), 4),
        "D": np.round(np.random.normal(0.006, 0.012, 50), 4),
        "E": np.round(np.random.normal(0.002, 0.007, 50), 4),
    },
    index=dates_medium,
)
returns_medium.index.name = "date"
returns_medium.to_csv(os.path.join(OUTPUT_DIR, "returns_medium.csv"))

cov_matrix = pd.DataFrame(
    [
        [0.0100, 0.0020, 0.0010],
        [0.0020, 0.0080, 0.0015],
        [0.0010, 0.0015, 0.0060],
    ],
    columns=["A", "B", "C"],
    index=["A", "B", "C"],
)
cov_matrix.to_csv(os.path.join(OUTPUT_DIR, "covariance_example.csv"))

dates_regimes = pd.date_range("2020-01-01", periods=60, freq="D")
regime1 = np.random.normal(0.003, 0.002, 20)
regime2 = np.random.normal(0.003, 0.015, 20)
regime3 = np.random.normal(0.003, 0.008, 20)
regimes_series = np.concatenate([regime1, regime2, regime3])
regimes_df = pd.DataFrame({"return": np.round(regimes_series, 4)}, index=dates_regimes)
regimes_df.index.name = "date"
regimes_df.to_csv(os.path.join(OUTPUT_DIR, "regimes_example.csv"))

sim_cov = np.array([
    [0.010, 0.002, 0.001],
    [0.002, 0.008, 0.0015],
    [0.001, 0.0015, 0.006],
])

L = np.linalg.cholesky(sim_cov)
simulated = np.random.normal(size=(100, 3)) @ L.T

sim_df = pd.DataFrame(
    np.round(simulated, 4),
    columns=["A", "B", "C"],
    index=pd.date_range("2020-01-01", periods=100, freq="D")
)
sim_df.index.name = "date"
sim_df.to_csv(os.path.join(OUTPUT_DIR, "simulation_example.csv"))

print("Synthetic datasets successfully generated in:", OUTPUT_DIR)