# **Financial Time‑Series & Risk Modelling Framework — Overview**

This framework provides a modular, extensible toolkit for **time‑series analysis**, **volatility modelling**, **regime detection**, **covariance estimation**, **Monte Carlo simulation**, and **portfolio risk analytics**.  
It is designed for quantitative researchers, risk analysts, and data scientists who require **clean abstractions**, **deterministic behaviour**, and **production‑grade structure**.

The project follows a clear separation of concerns:

- **`src/`** contains all modelling logic  
- **`tests/`** ensures correctness and robustness  
- **`docs/`** provides methodology and API reference  
- **`scripts/`** offers reproducible entry‑points for each module  

The result is a framework that is both **educational** and **industry‑aligned**, suitable for research, prototyping, and interview‑ready demonstrations.

---

## **Core Capabilities**

The framework implements the full pipeline of quantitative time‑series modelling:

### **1. Stationarity Testing**
Tools for diagnosing mean‑reversion and structural stability:

- Augmented Dickey–Fuller (ADF)  
- KPSS stationarity test  

These form the foundation for ARIMA modelling and regime analysis.

---

### **2. Volatility Modelling**
Deterministic volatility estimators:

- Rolling standard deviation  
- EWMA volatility  
- Realized volatility  

These methods support both standalone analysis and downstream risk modelling.

---

### **3. ARIMA Modelling**
A clean wrapper around ARIMA estimation:

- Model fitting  
- Multi‑step forecasting  
- Diagnostics (AIC, BIC, HQIC)  

Designed for clarity and reproducibility.

---

### **4. Regime Detection**
Multiple approaches to identifying structural changes:

- Z‑score volatility regimes  
- Markov‑switching volatility states  
- Mean‑shift and volatility‑shift break detection  

Useful for risk management, macro analysis, and scenario construction.

---

### **5. Covariance Estimation**
Robust covariance and correlation estimators:

- Empirical covariance and correlation  
- Annualized covariance and volatilities  
- Shrinkage estimators (Ledoit–Wolf, OAS, diagonal shrinkage)  

These methods support portfolio construction and simulation.

---

### **6. Monte Carlo Simulation**
Correlated return generation using:

- Cholesky decomposition  
- PCA‑based dimensionality reduction  

Designed for scenario analysis, VaR estimation, and stress testing.

---

### **7. Portfolio Risk Analytics**
Tools for evaluating portfolio‑level risk:

- Portfolio variance and volatility  
- Scenario‑based risk evaluation  
- Stress testing via covariance perturbations  

These methods integrate directly with covariance and simulation modules.

---

## **Project Structure**

```
financial-time-series-risk-modelling/
│
├── src/                # Core modelling logic
├── tests/              # Pytest suite (deterministic, synthetic)
├── scripts/            # Reproducible entry-point scripts
└── docs/               # Methodology + API documentation
```

Each module is self‑contained, with strict type checking and deterministic behaviour.

---

## **Documentation Layout**

The documentation is split into two layers:

### **1. Methodology (`docs/methodology/`)**
Explains the **math**, **intuition**, and **use‑cases** behind each module:

- stationarity  
- volatility  
- ARIMA  
- regimes  
- covariance  
- simulation  
- portfolio risk  

These pages are written for researchers and analysts.

---

### **2. API Reference (`docs/api/`)**
Provides **function signatures**, **parameters**, **return types**, and **usage examples** for every module.

These pages are written for developers integrating the framework into workflows.

---

## **Testing Philosophy**

The test suite is designed to ensure:

- deterministic outputs  
- strict type validation  
- no reliance on external data  
- seeded randomness where required  
- minimal, focused test cases  

This mirrors the testing standards used in quantitative research teams.

---

## **Usage Workflow**

A typical workflow using this framework:

1. Load or preprocess returns  
2. Test for stationarity  
3. Model volatility or ARIMA dynamics  
4. Detect regimes or structural breaks  
5. Estimate covariance matrices  
6. Run Monte Carlo simulations  
7. Evaluate portfolio‑level risk  

Each step is modular and can be used independently or as part of a pipeline.

---

## **Design Principles**

The framework is built around five principles:

- **Modularity** — each component is independent and reusable  
- **Determinism** — no hidden randomness, no side effects  
- **Transparency** — clear, readable implementations  
- **Extensibility** — easy to add new models or estimators  
- **Reproducibility** — scripts and tests ensure consistent behaviour  

This makes the project suitable for both research and production‑grade prototyping.

---

## **Next Steps**

You can now explore:

- **Methodology pages** for conceptual understanding  
- **API pages** for implementation details  
- **Scripts** for practical examples  
- **Tests** for validation and reference behaviour  

This overview serves as the anchor for the entire documentation set.