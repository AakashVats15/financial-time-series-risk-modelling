# financial-time-series-risk-modelling

A modular Python framework for analysing, modelling, and simulating financial time series.  
The project provides clean, well‑structured implementations of core quantitative finance tools, including stationarity testing, ARIMA modelling, volatility estimation, regime detection, covariance modelling, Monte Carlo simulation, and portfolio risk analysis.

The repository is organised to support research workflows, reproducibility, and extensibility.

---

## Features

- **Stationarity Testing**  
  Augmented Dickey–Fuller, KPSS, and combined diagnostics.

- **ARIMA Modelling**  
  Model fitting, forecasting, and information‑criterion diagnostics.

- **Volatility Estimation**  
  Rolling volatility, EWMA, and realized volatility.

- **Regime Detection**  
  Z‑score regimes, structural breaks, and Markov‑switching models.

- **Covariance Modelling**  
  Empirical covariance, correlation, and shrinkage estimators (Ledoit–Wolf, OAS).

- **Monte Carlo Simulation**  
  Cholesky‑based and PCA‑based correlated return generation.

- **Portfolio Risk**  
  Portfolio variance, volatility, and scenario‑based risk metrics.

---

## Repository Structure

```
financial-time-series-risk-modelling/
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── data_gen_raw.py
│   ├── data_gen_processed.py
│   └── README.md
│
├── src/
│   ├── arima/
│   ├── stationarity/
│   ├── volatility/
│   ├── regimes/
│   ├── covariance/
│   ├── simulation/
│   ├── portfolio/
│   └── utils/
│
├── scripts/
│   ├── run_arima.py
│   ├── run_stationarity_tests.py
│   ├── run_rolling_volatility.py
│   ├── run_regime_analysis.py
│   ├── run_covariance_estimation.py
│   ├── run_mc_simulation.py
│   └── run_portfolio_risk.py
│
├── tests/
│   ├── test_arima.py
│   ├── test_stationarity.py
│   ├── test_volatility.py
│   ├── test_regimes.py
│   ├── test_covariance.py
│   ├── test_simulation.py
│   └── test_portfolio.py
│
├── docs/
│   ├── overview.md
│   ├── methodology/
│   └── api/
│
├── requirements.txt
└── README.md
```

---

## Getting Started

Install dependencies:

```
pip install -r requirements.txt
```

Generate synthetic datasets:

```
python data/data_gen_raw.py
python data/data_gen_processed.py
```

Run any analysis script:

```
python scripts/run_arima.py
```

---

## Documentation

Full documentation is available in:

```
docs/
├── overview.md
├── methodology/
└── api/
```

These pages describe the mathematical background, implementation details, and API usage for each module.

---

## Testing

Run the full test suite:

```
pytest tests/
```
