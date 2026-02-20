# Portfolio Risk API

This document provides the technical reference for portfolio‑risk functions in the framework. These tools compute portfolio variance, volatility, and scenario‑based risk metrics using covariance matrices and asset‑weight vectors.

---

## `portfolio_variance`

Computes portfolio variance using the covariance matrix and weight vector.

### Signature

```python
portfolio_variance(weights, cov)
```

### Parameters

| Name      | Type                | Description |
|-----------|---------------------|-------------|
| `weights` | `numpy.ndarray`     | Vector of portfolio weights |
| `cov`     | `pandas.DataFrame`  | Covariance matrix |

### Returns

| Type  | Description |
|-------|-------------|
| `float` | Portfolio variance |

### Errors

- `TypeError` if inputs are not numeric arrays/matrices  
- `ValueError` if dimensions do not align  

### Example

```python
from src.portfolio.risk import portfolio_variance
import numpy as np
import pandas as pd

w = np.array([0.6, 0.4])
cov = pd.DataFrame([[0.01, 0.002], [0.002, 0.03]])

var = portfolio_variance(w, cov)
print(var)
```

---

## `portfolio_volatility`

Computes portfolio volatility as the square root of variance.

### Signature

```python
portfolio_volatility(weights, cov)
```

### Parameters

| Name      | Type                | Description |
|-----------|---------------------|-------------|
| `weights` | `numpy.ndarray`     | Portfolio weights |
| `cov`     | `pandas.DataFrame`  | Covariance matrix |

### Returns

| Type  | Description |
|-------|-------------|
| `float` | Portfolio volatility |

### Errors

- `TypeError` for incorrect input types  
- `ValueError` for dimension mismatch  

### Example

```python
from src.portfolio.risk import portfolio_volatility
import numpy as np
import pandas as pd

w = np.array([0.6, 0.4])
cov = pd.DataFrame([[0.01, 0.002], [0.002, 0.03]])

vol = portfolio_volatility(w, cov)
print(vol)
```

---

## `scenario_variance`

Computes portfolio variance under an alternative covariance matrix (scenario).

### Signature

```python
scenario_variance(weights, cov_scenario)
```

### Parameters

| Name           | Type                | Description |
|----------------|---------------------|-------------|
| `weights`      | `numpy.ndarray`     | Portfolio weights |
| `cov_scenario` | `pandas.DataFrame`  | Scenario covariance matrix |

### Returns

| Type  | Description |
|-------|-------------|
| `float` | Portfolio variance under the scenario |

### Errors

- `TypeError` for incorrect input types  
- `ValueError` if shapes do not match |

### Example

```python
from src.portfolio.risk import scenario_variance
import numpy as np
import pandas as pd

w = np.array([0.5, 0.5])
cov_s = pd.DataFrame([[0.02, 0.005], [0.005, 0.04]])

var_s = scenario_variance(w, cov_s)
print(var_s)
```

---

## `scenario_volatility`

Computes portfolio volatility under a scenario covariance matrix.

### Signature

```python
scenario_volatility(weights, cov_scenario)
```

### Parameters

| Name           | Type                | Description |
|----------------|---------------------|-------------|
| `weights`      | `numpy.ndarray`     | Portfolio weights |
| `cov_scenario` | `pandas.DataFrame`  | Scenario covariance matrix |

### Returns

| Type  | Description |
|-------|-------------|
| `float` | Portfolio volatility under the scenario |

### Errors

- `TypeError` for incorrect input types  
- `ValueError` for dimension mismatch  

### Example

```python
from src.portfolio.risk import scenario_volatility
import numpy as np
import pandas as pd

w = np.array([0.5, 0.5])
cov_s = pd.DataFrame([[0.02, 0.005], [0.005, 0.04]])

vol_s = scenario_volatility(w, cov_s)
print(vol_s)
```

---

## `portfolio_summary`

Unified wrapper returning variance, volatility, and scenario‑based metrics.

### Signature

```python
portfolio_summary(weights, cov, cov_scenario=None)
```

### Parameters

| Name           | Type                | Description |
|----------------|---------------------|-------------|
| `weights`      | `numpy.ndarray`     | Portfolio weights |
| `cov`          | `pandas.DataFrame`  | Base covariance matrix |
| `cov_scenario` | `pandas.DataFrame` or `None` | Optional scenario covariance matrix |

### Returns

Dictionary containing:

| Key                 | Type     | Meaning |
|---------------------|----------|---------|
| `"variance"`        | `float`  | Base portfolio variance |
| `"volatility"`      | `float`  | Base portfolio volatility |
| `"scenario_variance"` | `float` or `None` | Scenario variance |
| `"scenario_volatility"` | `float` or `None` | Scenario volatility |

### Errors

- `TypeError` for incorrect input types  
- `ValueError` for dimension mismatch  

### Example

```python
from src.portfolio.risk import portfolio_summary
import numpy as np
import pandas as pd

w = np.array([0.6, 0.4])
cov = pd.DataFrame([[0.01, 0.002], [0.002, 0.03]])
cov_s = pd.DataFrame([[0.02, 0.005], [0.005, 0.04]])

summary = portfolio_summary(w, cov, cov_scenario=cov_s)

print(summary["volatility"])