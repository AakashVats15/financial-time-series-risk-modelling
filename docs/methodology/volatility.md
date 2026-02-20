# **Volatility**

Volatility measures the magnitude of fluctuations in a financial time series. It is central to risk management, derivatives pricing, portfolio construction, and scenario analysis. This section outlines the core volatility estimators implemented in the framework and the intuition behind each method.

---

## **Conceptual Background**

Volatility captures the dispersion of returns over time. In quantitative finance, it is typically expressed as the standard deviation of returns, either over a fixed window or using a weighting scheme that emphasizes recent observations.

Volatility is used to:

- assess risk exposure  
- scale position sizes  
- compute Value‑at‑Risk  
- calibrate simulation models  
- detect regime shifts  

Different estimators serve different purposes depending on the time horizon and sensitivity to recent market conditions.

---

## **Rolling Standard Deviation**

The rolling standard deviation provides a simple, non‑parametric estimate of volatility over a fixed window.  
For a window of length `n`, the estimator is:

```
σₜ = √( (1 / (n − 1)) × Σᵢ (rₜ₋ᵢ − μₜ)² )
```

where:

- `rₜ₋ᵢ` are past returns  
- `μₜ` is the mean of the window  

This method is easy to interpret but responds slowly to sudden changes in market conditions.

---

## **EWMA Volatility**

Exponentially Weighted Moving Average (EWMA) volatility assigns greater weight to recent observations.  
The recursive formula is:

```
σₜ² = λσₜ₋₁² + (1 − λ) rₜ²
```

where:

- `λ` is the decay factor (commonly 0.94 for daily data)  
- `rₜ` is the most recent return  

Properties:

- reacts quickly to volatility spikes  
- smooths out noise  
- widely used in risk management frameworks  

EWMA is particularly effective for short‑horizon risk metrics.

---

## **Realized Volatility**

Realized volatility measures the accumulated squared returns over a window.  
For a window of length `n`:

```
RVₜ = √( Σᵢ rₜ₋ᵢ² )
```

This estimator is grounded in the idea that volatility is the integral of instantaneous variance.  
It is commonly used in:

- high‑frequency analysis  
- intraday risk estimation  
- volatility forecasting models  

Realized volatility is more sensitive to large moves than rolling standard deviation.

---

## **Comparing the Estimators**

Each estimator captures different aspects of market behaviour:

| Method | Strengths | Weaknesses |
|--------|-----------|------------|
| Rolling Std | Simple, interpretable | Slow to react |
| EWMA | Fast response, smooth | Requires decay parameter |
| Realized Vol | Captures jump risk | Sensitive to outliers |

Choosing the right estimator depends on the modelling objective and the time horizon.

---

## **Implementation Characteristics**

The volatility module in this framework is designed to be:

- deterministic  
- type‑safe  
- free of hidden state  
- consistent across estimators  

All methods return aligned time series with clear handling of warm‑up periods.