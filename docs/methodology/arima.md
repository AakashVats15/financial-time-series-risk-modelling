# **ARIMA Modelling**

ARIMA models capture linear dependencies in time‑series data by combining autoregressive structure, differencing, and moving‑average components. They are widely used for forecasting returns, macroeconomic indicators, and other financial signals where past values contain predictive information. This section outlines the conceptual foundations of ARIMA modelling and the structure implemented in the framework.

---

## **Model Structure**

An ARIMA model is defined by three integers:

- `p` — autoregressive order  
- `d` — differencing order  
- `q` — moving‑average order  

The general ARIMA(p, d, q) process can be expressed as:

```
ϕ₁ yₜ₋₁ + ϕ₂ yₜ₋₂ + … + ϕₚ yₜ₋ₚ
−
θ₁ εₜ₋₁ − θ₂ εₜ₋₂ − … − θ_q εₜ₋ₛ
=
Δᵈ yₜ
```

where:

- `ϕᵢ` are autoregressive coefficients  
- `θᵢ` are moving‑average coefficients  
- `εₜ` is white noise  
- `Δᵈ` denotes differencing applied `d` times  

Differencing removes trends and transforms non‑stationary series into stationary ones suitable for modelling.

---

## **Autoregressive Component (AR)**

The autoregressive part models the relationship between the current value and its past values:

```
yₜ = ϕ₁ yₜ₋₁ + ϕ₂ yₜ₋₂ + … + ϕₚ yₜ₋ₚ + εₜ
```

This captures persistence and mean‑reversion patterns.  
In financial data, AR terms often reflect short‑term autocorrelation or microstructure effects.

---

## **Moving‑Average Component (MA)**

The moving‑average part models the effect of past shocks:

```
yₜ = εₜ + θ₁ εₜ₋₁ + θ₂ εₜ₋₂ + … + θ_q εₜ₋ₛ
```

MA terms help absorb noise and correct for serial correlation in residuals.

---

## **Differencing (I)**

Differencing transforms the series to remove non‑stationarity:

```
Δyₜ = yₜ − yₜ₋₁
Δ²yₜ = Δyₜ − Δyₜ₋₁
```

A series that becomes stationary after differencing `d` times is said to be integrated of order `d`.

---

## **Model Estimation**

ARIMA estimation involves:

1. applying differencing  
2. fitting AR and MA components  
3. optimizing parameters using maximum likelihood  
4. validating residuals for whiteness  

The framework provides a clean wrapper around this process, ensuring:

- deterministic behaviour  
- consistent return structure  
- strict type checking  
- separation of model, forecast, and diagnostics  

---

## **Forecasting**

Once fitted, the model generates forecasts using the estimated structure:

```
ŷₜ₊₁ = f(yₜ, yₜ₋₁, …, εₜ, εₜ₋₁, …)
```

Forecasts include:

- predicted mean values  
- confidence intervals derived from forecast error variance  

These outputs are essential for scenario analysis, risk estimation, and signal generation.

---

## **Diagnostics**

Model adequacy is assessed using:

- Akaike Information Criterion (AIC)  
- Bayesian Information Criterion (BIC)  
- Hannan–Quinn Criterion (HQIC)  
- residual autocorrelation checks  

Lower information‑criterion values indicate a better balance between fit and complexity.

---

## **Practical Considerations**

ARIMA models are most effective when:

- the series is stationary or can be differenced to stationarity  
- linear dependencies dominate  
- volatility clustering is not the primary feature  

For financial returns, ARIMA often captures short‑term structure, while volatility dynamics are handled separately by other models.

---

## **Implementation Characteristics**

The ARIMA module in this framework is designed to be:

- transparent in structure  
- deterministic in output  
- aligned with standard econometric practice  
- easy to integrate with stationarity tests and volatility models  

It provides a reliable baseline for forecasting and residual analysis.