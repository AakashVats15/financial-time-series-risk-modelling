# Simulation API

This document provides the technical reference for Monte Carlo simulation functions in the framework. These tools generate correlated return paths using Cholesky and PCA‑based methods, supporting scenario analysis, stress testing, and portfolio‑risk workflows.

---

## `simulate_cholesky`

Generates correlated returns using Cholesky decomposition.

### Signature

```python
simulate_cholesky(cov, n_samples, seed=None)
```

### Parameters

| Name        | Type              | Description |
|-------------|-------------------|-------------|
| `cov`       | `pandas.DataFrame`| Covariance matrix (must be positive semi‑definite) |
| `n_samples` | `int`             | Number of simulated return vectors |
| `seed`      | `int` or `None`   | Optional random seed for reproducibility |

### Returns

| Type               | Description |
|--------------------|-------------|
| `pandas.DataFrame` | Simulated returns with correct covariance structure |

### Errors

- `TypeError` if `cov` is not a `DataFrame`  
- `ValueError` if `n_samples < 1`  
- `ValueError` if covariance matrix is not positive semi‑definite  

### Example

```python
from src.simulation.cholesky import simulate_cholesky
import pandas as pd

cov = pd.DataFrame([[0.01, 0.002], [0.002, 0.03]])
sim = simulate_cholesky(cov, n_samples=5, seed=42)

print(sim)
```

---

## `simulate_pca`

Generates correlated returns using PCA decomposition.

### Signature

```python
simulate_pca(cov, n_samples, n_components=None, seed=None)
```

### Parameters

| Name           | Type              | Description |
|----------------|-------------------|-------------|
| `cov`          | `pandas.DataFrame`| Covariance matrix |
| `n_samples`    | `int`             | Number of simulated return vectors |
| `n_components` | `int` or `None`   | Number of principal components to retain; `None` uses all |
| `seed`         | `int` or `None`   | Optional random seed |

### Returns

| Type               | Description |
|--------------------|-------------|
| `pandas.DataFrame` | Simulated returns generated via PCA |

### Errors

- `TypeError` for incorrect input types  
- `ValueError` if `n_samples < 1`  
- `ValueError` if `n_components` is invalid or exceeds matrix rank  

### Example

```python
from src.simulation.pca import simulate_pca
import pandas as pd

cov = pd.DataFrame([[0.01, 0.002], [0.002, 0.03]])
sim = simulate_pca(cov, n_samples=5, n_components=2, seed=42)

print(sim)
```

---

## `variance_cutoff`

Selects the minimum number of principal components required to explain a target variance fraction.

### Signature

```python
variance_cutoff(eigenvalues, threshold)
```

### Parameters

| Name         | Type            | Description |
|--------------|-----------------|-------------|
| `eigenvalues`| `numpy.ndarray` | Sorted eigenvalues (descending) |
| `threshold`  | `float`         | Fraction of variance to retain (0 < threshold ≤ 1) |

### Returns

| Type  | Description |
|-------|-------------|
| `int` | Number of components required |

### Errors

- `TypeError` for incorrect input types  
- `ValueError` if `threshold` is outside `(0, 1]`  

### Example

```python
from src.simulation.pca import variance_cutoff
import numpy as np

vals = np.array([3.0, 1.0, 0.5])
k = variance_cutoff(vals, threshold=0.90)

print(k)
```

---

## `simulation_summary`

Unified wrapper returning both Cholesky and PCA simulations.

### Signature

```python
simulation_summary(cov, n_samples, n_components=None, seed=None)
```

### Parameters

| Name           | Type              | Description |
|----------------|-------------------|-------------|
| `cov`          | `pandas.DataFrame`| Covariance matrix |
| `n_samples`    | `int`             | Number of simulated return vectors |
| `n_components` | `int` or `None`   | PCA component count |
| `seed`         | `int` or `None`   | Random seed |

### Returns

Dictionary containing:

| Key             | Type               | Meaning |
|-----------------|--------------------|---------|
| `"cholesky"`    | `DataFrame`        | Cholesky‑based simulations |
| `"pca"`         | `DataFrame`        | PCA‑based simulations |
| `"components"`  | `int` or `None`    | Number of PCA components used |

### Errors

- `TypeError` for incorrect input types  
- `ValueError` for invalid sample size or PCA parameters  

### Example

```python
from src.simulation.summary import simulation_summary
import pandas as pd

cov = pd.DataFrame([[0.01, 0.002], [0.002, 0.03]])
summary = simulation_summary(cov, n_samples=5, n_components=2, seed=42)

print(summary["cholesky"].head())