# Covariance API

This document provides the technical reference for covariance, correlation, and shrinkage‑estimation functions in the framework. These tools support portfolio construction, risk modelling, and simulation workflows.

---

## `empirical_covariance`

Computes the sample covariance matrix.

### Signature

```python
empirical_covariance(returns)
```

### Parameters

| Name      | Type              | Description |
|-----------|-------------------|-------------|
| `returns` | `pandas.DataFrame`| Time‑indexed matrix of asset returns |

### Returns

| Type              | Description |
|-------------------|-------------|
| `pandas.DataFrame`| Empirical covariance matrix |

### Errors

- `TypeError` if input is not a `DataFrame`  
- `ValueError` if fewer than 2 observations are provided  

### Example

```python
from src.covariance.estimators import empirical_covariance
import pandas as pd

df = pd.DataFrame({"A":[0.01,0.02], "B":[0.00,0.03]})
cov = empirical_covariance(df)

print(cov)
```

---

## `empirical_correlation`

Computes the sample correlation matrix.

### Signature

```python
empirical_correlation(returns)
```

### Parameters

| Name      | Type              | Description |
|-----------|-------------------|-------------|
| `returns` | `pandas.DataFrame`| Matrix of asset returns |

### Returns

| Type              | Description |
|-------------------|-------------|
| `pandas.DataFrame`| Correlation matrix |

### Errors

- `TypeError` for incorrect input types  

### Example

```python
from src.covariance.estimators import empirical_correlation
import pandas as pd

df = pd.DataFrame({"A":[0.01,0.02], "B":[0.00,0.03]})
corr = empirical_correlation(df)

print(corr)
```

---

## `annualize_covariance`

Scales a daily covariance matrix to an annual horizon.

### Signature

```python
annualize_covariance(cov, periods=252)
```

### Parameters

| Name       | Type              | Description |
|------------|-------------------|-------------|
| `cov`      | `pandas.DataFrame`| Covariance matrix |
| `periods`  | `int`             | Number of periods per year (default 252) |

### Returns

| Type              | Description |
|-------------------|-------------|
| `pandas.DataFrame`| Annualized covariance matrix |

### Errors

- `TypeError` if `cov` is not a `DataFrame`  
- `ValueError` if `periods < 1`  

### Example

```python
from src.covariance.estimators import annualize_covariance
import pandas as pd

cov = pd.DataFrame([[0.01,0.002],[0.002,0.03]])
annual = annualize_covariance(cov)

print(annual)
```

---

## `ledoit_wolf`

Ledoit–Wolf shrinkage estimator.

### Signature

```python
ledoit_wolf(returns)
```

### Parameters

| Name      | Type              | Description |
|-----------|-------------------|-------------|
| `returns` | `pandas.DataFrame`| Matrix of asset returns |

### Returns

Dictionary containing:

| Key        | Type              | Meaning |
|------------|-------------------|---------|
| `"cov"`    | `DataFrame`       | Shrinkage covariance matrix |
| `"alpha"`  | `float`           | Shrinkage intensity |
| `"target"` | `DataFrame`       | Shrinkage target matrix |

### Errors

- `TypeError` for incorrect input types  
- `ValueError` if insufficient observations  

### Example

```python
from src.covariance.shrinkage import ledoit_wolf
import pandas as pd

df = pd.DataFrame({"A":[0.01,0.02], "B":[0.00,0.03]})
res = ledoit_wolf(df)

print(res["cov"])
```

---

## `oas`

Oracle Approximating Shrinkage estimator.

### Signature

```python
oas(returns)
```

### Parameters

| Name      | Type              | Description |
|-----------|-------------------|-------------|
| `returns` | `pandas.DataFrame`| Matrix of asset returns |

### Returns

Dictionary containing:

| Key        | Type              | Meaning |
|------------|-------------------|---------|
| `"cov"`    | `DataFrame`       | Shrinkage covariance matrix |
| `"alpha"`  | `float`           | Shrinkage intensity |
| `"target"` | `DataFrame`       | Shrinkage target matrix |

### Errors

- `TypeError` for incorrect input types  

### Example

```python
from src.covariance.shrinkage import oas
import pandas as pd

df = pd.DataFrame({"A":[0.01,0.02], "B":[0.00,0.03]})
res = oas(df)

print(res["alpha"])
```

---

## `diagonal_shrinkage`

Shrinks covariance toward its diagonal.

### Signature

```python
diagonal_shrinkage(cov, alpha)
```

### Parameters

| Name     | Type              | Description |
|----------|-------------------|-------------|
| `cov`    | `pandas.DataFrame`| Empirical covariance matrix |
| `alpha`  | `float`           | Shrinkage intensity (0 ≤ α ≤ 1) |

### Returns

| Type              | Description |
|-------------------|-------------|
| `pandas.DataFrame`| Shrinkage covariance matrix |

### Errors

- `TypeError` for incorrect input types  
- `ValueError` if `alpha` is outside `[0, 1]`  

### Example

```python
from src.covariance.shrinkage import diagonal_shrinkage
import pandas as pd

cov = pd.DataFrame([[0.01,0.002],[0.002,0.03]])
shrunk = diagonal_shrinkage(cov, alpha=0.5)

print(shrunk)
```

---

## `covariance_summary`

Unified wrapper returning all covariance estimators.

### Signature

```python
covariance_summary(returns)
```

### Parameters

| Name      | Type              | Description |
|-----------|-------------------|-------------|
| `returns` | `pandas.DataFrame`| Matrix of asset returns |

### Returns

Dictionary containing:

| Key              | Type              | Meaning |
|------------------|-------------------|---------|
| `"empirical"`    | `DataFrame`       | Empirical covariance |
| `"correlation"`  | `DataFrame`       | Empirical correlation |
| `"ledoit_wolf"`  | `dict`            | Ledoit–Wolf shrinkage outputs |
| `"oas"`          | `dict`            | OAS shrinkage outputs |

### Errors

- `TypeError` for incorrect input types  

### Example

```python
from src.covariance.summary import covariance_summary
import pandas as pd

df = pd.DataFrame({"A":[0.01,0.02], "B":[0.00,0.03]})
summary = covariance_summary(df)

print(summary["empirical"])