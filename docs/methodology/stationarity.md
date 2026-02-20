# **Stationarity**

Stationarity describes whether a time series maintains stable statistical properties over time. Many econometric and quantitative models rely on this assumption to ensure that estimated relationships remain meaningful and forecasts remain reliable. This section outlines the conceptual foundations of stationarity and the diagnostic tools implemented in the framework.

---

## **Core Idea**

A time series is considered stationary when:

- its mean is constant  
- its variance is constant  
- its autocovariance depends only on the lag, not on time  

Financial returns often satisfy these conditions, while price levels typically do not.

Stationarity determines whether a series can be modelled directly or must be transformed (for example, differenced or detrended).

---

## **Forms of Non‑Stationarity**

### **1. Unit‑Root Processes**
A unit‑root process exhibits persistent shocks. Deviations do not revert quickly, and the series behaves like a random walk.

General form:

```
yₜ = yₜ₋₁ + εₜ
```

If the coefficient on `yₜ₋₁` equals 1, the process contains a unit root.

---

### **2. Structural Breaks**
Sudden changes in mean or variance can create the appearance of non‑stationarity even when the process is stable within segments.

Example:

```
yₜ = μ₁ + εₜ   for t ≤ τ
yₜ = μ₂ + εₜ   for t > τ
```

---

### **3. Deterministic Trends**
A deterministic trend introduces predictable drift:

```
yₜ = α + βt + εₜ
```

Even if `εₜ` is stationary, the overall process is not.

---

## **Augmented Dickey–Fuller (ADF) Test**

The ADF test evaluates whether a series contains a unit root.  
It estimates the regression:

```
Δyₜ = α + βt + γyₜ₋₁ + δ₁Δyₜ₋₁ + δ₂Δyₜ₋₂ + … + δₚΔyₜ₋ₚ + εₜ
```

Interpretation:

- If γ = 0 → unit root → non‑stationary  
- If γ < 0 → mean‑reverting → stationary  

The test returns:

- test statistic  
- p‑value  
- number of lags  
- number of observations  

A small p‑value indicates rejection of the unit‑root hypothesis.

---

## **KPSS Test**

The KPSS test evaluates the opposite hypothesis: that the series is stationary around a mean or trend.

It decomposes the series as:

```
yₜ = rₜ + εₜ
```

where:

- `rₜ` is a random walk  
- `εₜ` is a stationary error  

If the random‑walk component is large, the series is non‑stationary.

The KPSS statistic measures the cumulative deviation from the estimated trend.

A large statistic leads to rejection of stationarity.

---

## **Joint Interpretation**

Using ADF and KPSS together provides a more complete diagnostic picture:

| ADF Result | KPSS Result | Interpretation |
|-----------|-------------|----------------|
| Reject unit root | Fail to reject stationarity | Stationary |
| Fail to reject unit root | Reject stationarity | Non‑stationary |
| Reject both | Likely structural breaks |
| Fail to reject both | Inconclusive; further analysis needed |

This dual‑test approach is standard in quantitative research.

---

## **Implementation Characteristics**

The stationarity tools in this framework are designed to be:

- deterministic  
- type‑safe  
- consistent in output structure  
- easy to integrate with ARIMA, volatility modelling, and regime analysis  

They serve as the first step in any modelling pipeline.