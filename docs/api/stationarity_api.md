# Stationarity API

This document provides the technical reference for the stationarity‑testing functions implemented in the framework. These tools support unit‑root diagnostics and stationarity assessment for financial time‑series workflows.

---

## `adf_test`

Augmented Dickey–Fuller unit‑root test.

### Signature

```python
adf_test(series, max_lags=None, regression="c")
```

### Parameters

| Name        | Type              | Description |
|-------------|-------------------|-------------|
| `series`    | `pandas.Series`   | Time‑ordered numeric series to be tested |
| `max_lags`  | `int` or `None`   | Maximum lag order; `None` applies an automatic rule |
| `regression`| `str`             | Deterministic terms: `"c"` (constant), `"ct"` (constant + trend), `"nc"` (none) |

### Returns

Dictionary containing ADF outputs:

| Key               | Type               | Meaning |
|-------------------|--------------------|---------|
| `"statistic"`      | `float`            | Test statistic |
| `"p_value"`        | `float`            | p‑value |
| `"lags"`           | `int`              | Number of lags used |
| `"nobs"`           | `int`              | Number of observations |
| `"critical_values"`| `dict[str, float]` | Critical values at standard significance levels |

### Errors

- `TypeError` if `series` is not a `pandas.Series`  
- `ValueError` if the series is empty or contains only missing values  

### Example

```python
from src.stationarity.tests import adf_test
import pandas as pd

s = pd.Series([1.01, 1.02, 1.00, 0.99, 1.01])
res = adf_test(s, max_lags=3, regression="c")

print(res["statistic"], res["p_value"])
```

---

## `kpss_test`

KPSS stationarity test.

### Signature

```python
kpss_test(series, regression="c", nlags="auto")
```

### Parameters

| Name        | Type              | Description |
|-------------|-------------------|-------------|
| `series`    | `pandas.Series`   | Time‑ordered numeric series |
| `regression`| `str`             | `"c"` (level stationarity) or `"ct"` (trend stationarity) |
| `nlags`     | `int` or `"auto"` | Number of lags in long‑run variance estimator |

### Returns

Dictionary containing KPSS outputs:

| Key               | Type               | Meaning |
|-------------------|--------------------|---------|
| `"statistic"`      | `float`            | Test statistic |
| `"p_value"`        | `float`            | p‑value |
| `"lags"`           | `int`              | Number of lags used |
| `"critical_values"`| `dict[str, float]` | Critical values for standard significance levels |

### Errors

- `TypeError` if `series` is not a `pandas.Series`  
- `ValueError` if the series is empty or contains only missing values  

### Example

```python
from src.stationarity.tests import kpss_test
import pandas as pd

s = pd.Series([0.01, 0.02, -0.01, 0.00, 0.01])
res = kpss_test(s, regression="c", nlags="auto")

print(res["statistic"], res["p_value"])
```

---

## `stationarity_summary`

Combined diagnostic wrapper for ADF and KPSS.

### Signature

```python
stationarity_summary(series)
```

### Parameters

| Name     | Type            | Description |
|----------|-----------------|-------------|
| `series` | `pandas.Series` | Time‑ordered numeric series |

### Returns

Dictionary summarizing both tests:

| Key           | Type  | Meaning |
|---------------|--------|---------|
| `"adf"`       | `dict` | Output from `adf_test` |
| `"kpss"`      | `dict` | Output from `kpss_test` |
| `"assessment"`| `str`  | High‑level classification such as `"stationary"`, `"non_stationary"`, `"inconclusive"` |

### Errors

- `TypeError` if `series` is not a `pandas.Series`  
- `ValueError` if the series is empty or contains only missing values  

### Example

```python
from src.stationarity.tests import stationarity_summary
import pandas as pd

s = pd.Series([0.01, 0.02, -0.01, 0.03, 0.00])
summary = stationarity_summary(s)

print(summary["assessment"])