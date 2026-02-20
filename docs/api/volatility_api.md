# Volatility API

This document provides the technical reference for volatility‑estimation functions in the framework. These tools compute rolling, exponentially weighted, and realized volatility measures for financial time‑series analysis.

---

## `rolling_volatility`

Rolling standard‑deviation estimator.

### Signature

```python
rolling_volatility(series, window)
```

### Parameters

| Name     | Type            | Description |
|----------|-----------------|-------------|
| `series` | `pandas.Series` | Time‑ordered numeric return series |
| `window` | `int`           | Number of observations in the rolling window |

### Returns

| Type            | Description |
|-----------------|-------------|
| `pandas.Series` | Rolling volatility series aligned with the input index |

### Errors

- `TypeError` if inputs are not of the correct type  
- `ValueError` if `window` is less than 1  

### Example

```python
from src.volatility.estimators import rolling_volatility
import pandas as pd

s = pd.Series([0.01, 0.02, -0.01, 0.03, 0.00])
vol = rolling_volatility(s, window=3)

print(vol.tail())
```

---

## `ewma_volatility`

Exponentially Weighted Moving Average (EWMA) volatility.

### Signature

```python
ewma_volatility(series, lambda_=0.94)
```

### Parameters

| Name       | Type            | Description |
|------------|-----------------|-------------|
| `series`   | `pandas.Series` | Time‑ordered numeric return series |
| `lambda_`  | `float`         | Decay factor (0 < λ < 1) controlling weight on past observations |

### Returns

| Type            | Description |
|-----------------|-------------|
| `pandas.Series` | EWMA volatility series |

### Errors

- `TypeError` if `series` is not a `pandas.Series`  
- `ValueError` if `lambda_` is not in the interval (0, 1)  

### Example

```python
from src.volatility.estimators import ewma_volatility
import pandas as pd

s = pd.Series([0.01, 0.02, -0.01, 0.03])
vol = ewma_volatility(s, lambda_=0.94)

print(vol.tail())
```

---

## `realized_volatility`

Realized volatility computed from squared returns.

### Signature

```python
realized_volatility(series, window)
```

### Parameters

| Name     | Type            | Description |
|----------|-----------------|-------------|
| `series` | `pandas.Series` | Time‑ordered numeric return series |
| `window` | `int`           | Number of observations used in the realized‑volatility window |

### Returns

| Type            | Description |
|-----------------|-------------|
| `pandas.Series` | Realized volatility series |

### Errors

- `TypeError` if `series` is not a `pandas.Series`  
- `ValueError` if `window` is less than 1  

### Example

```python
from src.volatility.estimators import realized_volatility
import pandas as pd

s = pd.Series([0.01, 0.02, -0.01, 0.03])
rv = realized_volatility(s, window=2)

print(rv.tail())
```

---

## `volatility_summary`

Unified wrapper returning all volatility estimators.

### Signature

```python
volatility_summary(series, window, lambda_=0.94)
```

### Parameters

| Name       | Type            | Description |
|------------|-----------------|-------------|
| `series`   | `pandas.Series` | Return series |
| `window`   | `int`           | Window length for rolling and realized volatility |
| `lambda_`  | `float`         | Decay factor for EWMA |

### Returns

Dictionary containing all volatility measures:

| Key                  | Type            | Meaning |
|----------------------|-----------------|---------|
| `"rolling"`          | `pandas.Series` | Rolling volatility |
| `"ewma"`             | `pandas.Series` | EWMA volatility |
| `"realized"`         | `pandas.Series` | Realized volatility |

### Errors

- `TypeError` for incorrect input types  
- `ValueError` for invalid window or decay parameters  

### Example

```python
from src.volatility.estimators import volatility_summary
import pandas as pd

s = pd.Series([0.01, 0.02, -0.01, 0.03])
summary = volatility_summary(s, window=3, lambda_=0.94)

print(summary["ewma"].tail())
```
```

---

If you want, I can now generate:

### **`arima_api.md`**  
in the same polished, consistent style.Here is a **fully polished, production‑grade** `volatility_api.md` written in the same style as your `stationarity_api.md`.  
Everything is clean, consistent, and ready to drop into your docs folder.

---

```markdown
# Volatility API

This document provides the technical reference for volatility‑estimation functions in the framework. These tools compute rolling, exponentially weighted, and realized volatility measures for financial time‑series analysis.

---

## `rolling_volatility`

Rolling standard‑deviation estimator.

### Signature

```python
rolling_volatility(series, window)
```

### Parameters

| Name     | Type            | Description |
|----------|-----------------|-------------|
| `series` | `pandas.Series` | Time‑ordered numeric return series |
| `window` | `int`           | Number of observations in the rolling window |

### Returns

| Type            | Description |
|-----------------|-------------|
| `pandas.Series` | Rolling volatility series aligned with the input index |

### Errors

- `TypeError` if inputs are not of the correct type  
- `ValueError` if `window` is less than 1  

### Example

```python
from src.volatility.estimators import rolling_volatility
import pandas as pd

s = pd.Series([0.01, 0.02, -0.01, 0.03, 0.00])
vol = rolling_volatility(s, window=3)

print(vol.tail())
```

---

## `ewma_volatility`

Exponentially Weighted Moving Average (EWMA) volatility.

### Signature

```python
ewma_volatility(series, lambda_=0.94)
```

### Parameters

| Name       | Type            | Description |
|------------|-----------------|-------------|
| `series`   | `pandas.Series` | Time‑ordered numeric return series |
| `lambda_`  | `float`         | Decay factor (0 < λ < 1) controlling weight on past observations |

### Returns

| Type            | Description |
|-----------------|-------------|
| `pandas.Series` | EWMA volatility series |

### Errors

- `TypeError` if `series` is not a `pandas.Series`  
- `ValueError` if `lambda_` is not in the interval (0, 1)  

### Example

```python
from src.volatility.estimators import ewma_volatility
import pandas as pd

s = pd.Series([0.01, 0.02, -0.01, 0.03])
vol = ewma_volatility(s, lambda_=0.94)

print(vol.tail())
```

---

## `realized_volatility`

Realized volatility computed from squared returns.

### Signature

```python
realized_volatility(series, window)
```

### Parameters

| Name     | Type            | Description |
|----------|-----------------|-------------|
| `series` | `pandas.Series` | Time‑ordered numeric return series |
| `window` | `int`           | Number of observations used in the realized‑volatility window |

### Returns

| Type            | Description |
|-----------------|-------------|
| `pandas.Series` | Realized volatility series |

### Errors

- `TypeError` if `series` is not a `pandas.Series`  
- `ValueError` if `window` is less than 1  

### Example

```python
from src.volatility.estimators import realized_volatility
import pandas as pd

s = pd.Series([0.01, 0.02, -0.01, 0.03])
rv = realized_volatility(s, window=2)

print(rv.tail())
```

---

## `volatility_summary`

Unified wrapper returning all volatility estimators.

### Signature

```python
volatility_summary(series, window, lambda_=0.94)
```

### Parameters

| Name       | Type            | Description |
|------------|-----------------|-------------|
| `series`   | `pandas.Series` | Return series |
| `window`   | `int`           | Window length for rolling and realized volatility |
| `lambda_`  | `float`         | Decay factor for EWMA |

### Returns

Dictionary containing all volatility measures:

| Key                  | Type            | Meaning |
|----------------------|-----------------|---------|
| `"rolling"`          | `pandas.Series` | Rolling volatility |
| `"ewma"`             | `pandas.Series` | EWMA volatility |
| `"realized"`         | `pandas.Series` | Realized volatility |

### Errors

- `TypeError` for incorrect input types  
- `ValueError` for invalid window or decay parameters  

### Example

```python
from src.volatility.estimators import volatility_summary
import pandas as pd

s = pd.Series([0.01, 0.02, -0.01, 0.03])
summary = volatility_summary(s, window=3, lambda_=0.94)

print(summary["ewma"].tail())
