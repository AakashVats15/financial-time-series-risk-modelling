# ARIMA API

This document provides the technical reference for ARIMA model fitting, forecasting, and diagnostics. These tools implement autoregressive–integrated–moving‑average modelling suitable for financial time‑series forecasting and residual analysis.

---

## `fit_arima`

Fits an ARIMA(p, d, q) model to a univariate time series.

### Signature

```python
fit_arima(series, order)
```

### Parameters

| Name     | Type            | Description |
|----------|-----------------|-------------|
| `series` | `pandas.Series` | Time‑ordered numeric series to be modelled |
| `order`  | `tuple[int, int, int]` | ARIMA order `(p, d, q)` |

### Returns

| Type | Description |
|------|-------------|
| `statsmodels` ARIMAResults object | Fitted ARIMA model |

### Errors

- `TypeError` if `series` is not a `pandas.Series`  
- `ValueError` if `order` is not a 3‑tuple of integers  

### Example

```python
from src.arima.arima_model import fit_arima
import pandas as pd

s = pd.Series([0.01, 0.02, -0.01, 0.03])
model = fit_arima(s, order=(1, 0, 1))

print(model.params)
```

---

## `forecast`

Generates multi‑step forecasts from a fitted ARIMA model.

### Signature

```python
forecast(model, steps)
```

### Parameters

| Name     | Type  | Description |
|----------|--------|-------------|
| `model`  | ARIMAResults | Fitted ARIMA model returned by `fit_arima` |
| `steps`  | `int` | Number of periods to forecast |

### Returns

Tuple containing:

| Element | Type            | Meaning |
|---------|-----------------|---------|
| `mean`  | `pandas.Series` | Forecasted mean values |
| `conf`  | `pandas.DataFrame` | Confidence interval bounds (lower, upper) |

### Errors

- `TypeError` if `model` is not a fitted ARIMA object  
- `ValueError` if `steps` is less than 1  

### Example

```python
from src.arima.arima_model import fit_arima, forecast
import pandas as pd

s = pd.Series([0.01, 0.02, -0.01, 0.03])
m = fit_arima(s, order=(1, 0, 1))
mean, conf = forecast(m, steps=3)

print(mean)
print(conf)
```

---

## `arima_diagnostics`

Extracts information‑criterion diagnostics from a fitted ARIMA model.

### Signature

```python
arima_diagnostics(model)
```

### Parameters

| Name    | Type          | Description |
|---------|---------------|-------------|
| `model` | ARIMAResults  | Fitted ARIMA model |

### Returns

Dictionary containing model diagnostics:

| Key     | Type   | Meaning |
|---------|--------|---------|
| `"aic"` | `float` | Akaike Information Criterion |
| `"bic"` | `float` | Bayesian Information Criterion |
| `"hqic"`| `float` | Hannan–Quinn Information Criterion |

### Errors

- `TypeError` if `model` is not a fitted ARIMA object  

### Example

```python
from src.arima.arima_model import fit_arima, arima_diagnostics
import pandas as pd

s = pd.Series([0.01, 0.02, -0.01, 0.03])
m = fit_arima(s, order=(1, 0, 1))
d = arima_diagnostics(m)

print(d)
```

---

## `arima_summary`

Convenience wrapper returning model, forecasts, and diagnostics.

### Signature

```python
arima_summary(series, order, steps)
```

### Parameters

| Name     | Type            | Description |
|----------|-----------------|-------------|
| `series` | `pandas.Series` | Input time series |
| `order`  | `tuple[int, int, int]` | ARIMA order `(p, d, q)` |
| `steps`  | `int`           | Number of forecast periods |

### Returns

Dictionary containing:

| Key           | Type                  | Meaning |
|---------------|-----------------------|---------|
| `"model"`     | ARIMAResults          | Fitted model |
| `"forecast"`  | `pandas.Series`       | Forecasted mean values |
| `"conf_int"`  | `pandas.DataFrame`    | Confidence intervals |
| `"diagnostics"` | `dict`              | AIC, BIC, HQIC |

### Errors

- `TypeError` for incorrect input types  
- `ValueError` for invalid ARIMA order or forecast horizon  

### Example

```python
from src.arima.arima_model import arima_summary
import pandas as pd

s = pd.Series([0.01, 0.02, -0.01, 0.03])
summary = arima_summary(s, order=(1, 0, 1), steps=3)

print(summary["diagnostics"])