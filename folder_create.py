import os

base_path = r"E:\Personal\GitHub\Python Code Repo\financial-time-series-risk-modelling"

folders = [
    "data/raw",
    "data/processed",
    "src/arima",
    "src/stationarity",
    "src/volatility",
    "src/regimes",
    "src/covariance",
    "src/simulation",
    "src/portfolio",
    "src/utils",
    "scripts",
    "tests",
    "docs/methodology",
    "docs/api"
]

files = [
    "data/README.md",
    "src/arima/arima_model.py",
    "src/arima/__init__.py",
    "src/stationarity/adf_test.py",
    "src/stationarity/kpss_test.py",
    "src/stationarity/__init__.py",
    "src/volatility/rolling_vol.py",
    "src/volatility/__init__.py",
    "src/regimes/volatility_regimes.py",
    "src/regimes/structural_breaks.py",
    "src/regimes/__init__.py",
    "src/covariance/empirical_cov.py",
    "src/covariance/shrinkage_methods.py",
    "src/covariance/__init__.py",
    "src/simulation/correlated_mc.py",
    "src/simulation/__init__.py",
    "src/portfolio/portfolio_variance.py",
    "src/portfolio/__init__.py",
    "src/utils/data_loader.py",
    "src/utils/plotting.py",
    "src/utils/__init__.py",
    "scripts/run_arima.py",
    "scripts/run_stationarity_tests.py",
    "scripts/run_rolling_volatility.py",
    "scripts/run_regime_analysis.py",
    "scripts/run_covariance_estimation.py",
    "scripts/run_mc_simulation.py",
    "scripts/run_portfolio_risk.py",
    "tests/test_arima.py",
    "tests/test_stationarity.py",
    "tests/test_volatility.py",
    "tests/test_regimes.py",
    "tests/test_covariance.py",
    "tests/test_simulation.py",
    "tests/test_portfolio.py",
    "docs/overview.md",
    "docs/methodology/arima.md",
    "docs/methodology/stationarity.md",
    "docs/methodology/volatility.md",
    "docs/methodology/regimes.md",
    "docs/methodology/covariance.md",
    "docs/methodology/simulation.md",
    "docs/methodology/portfolio.md",
    "docs/api/arima_api.md",
    "docs/api/stationarity_api.md",
    "docs/api/volatility_api.md",
    "docs/api/regimes_api.md",
    "docs/api/covariance_api.md",
    "docs/api/simulation_api.md",
    "docs/api/portfolio_api.md",
    "requirements.txt",
    "pyproject.toml",
    "README.md",
    "LICENSE"
]

# Create folders
for folder in folders:
    path = os.path.join(base_path, folder)
    os.makedirs(path, exist_ok=True)

# Create files
for file in files:
    path = os.path.join(base_path, file)
    # Ensure parent folder exists
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # Create empty file if not exists
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write("")

print("Project structure created successfully.")
