# Regime Detection API

This document provides the technical reference for regime‑detection functions in the framework. These tools identify structural changes in volatility, mean levels, and hidden states within financial time series.

---

## `zscore_regimes`

Detects volatility regimes using rolling z‑scores.

### Signature

```python
zscore_regimes(series, window, threshold)
```

### Parameters

| Name        | Type            | Description |
|-------------|-----------------|-------------|
| `series`    | `pandas.Series` | Time‑ordered numeric return series |
| `window`    | `int`           | Rolling window length for mean and standard deviation |
| `threshold` | `float`         | Absolute z‑score above which a regime is flagged |

### Returns

| Type            | Description |
|-----------------|-------------|
| `pandas.Series` | Binary regime indicator (1 = regime, 0 = normal) |

### Errors

- `TypeError` for incorrect input types  
- `ValueError` if `window < 1` or `threshold ≤ 0`  

### Example

```python
from src.regimes.zscore import zscore_regimes
import pandas as pd

s = pd.Series([0.01, 0.03, -0.02, 0.10, -0.05])
reg = zscore_regimes(s, window=3, threshold=2.0)

print(reg.tail())
```

---

## `markov_switching_regimes`

Fits a Markov‑switching volatility model and extracts state probabilities.

### Signature

```python
markov_switching_regimes(series, k_regimes=2)
```

### Parameters

| Name         | Type            | Description |
|--------------|-----------------|-------------|
| `series`     | `pandas.Series` | Return series |
| `k_regimes`  | `int`           | Number of hidden states (typically 2) |

### Returns

Dictionary containing:

| Key               | Type                | Meaning |
|-------------------|---------------------|---------|
| `"model"`         | fitted model object | Markov‑switching model |
| `"smoothed_probs"`| `pandas.DataFrame`  | Smoothed state probabilities |
| `"regimes"`       | `pandas.Series`     | Most likely regime at each time |

### Errors

- `TypeError` if `series` is not a `pandas.Series`  
- `ValueError` if `k_regimes < 2`  

### Example

```python
from src.regimes.markov import markov_switching_regimes
import pandas as pd

s = pd.Series([0.01, 0.02, -0.03, 0.05, -0.02])
res = markov_switching_regimes(s, k_regimes=2)

print(res["regimes"].tail())
```

---

## `mean_shift_breaks`

Detects structural breaks in the mean level of a time series.

### Signature

```python
mean_shift_breaks(series, window, threshold)
```

### Parameters

| Name        | Type            | Description |
|-------------|-----------------|-------------|
| `series`    | `pandas.Series` | Input time series |
| `window`    | `int`           | Window size for comparing pre‑ and post‑means |
| `threshold` | `float`         | Minimum absolute mean difference to flag a break |

### Returns

| Type            | Description |
|-----------------|-------------|
| `pandas.Series` | Binary indicator for mean‑shift breaks |

### Errors

- `TypeError` for incorrect input types  
- `ValueError` if `window < 1` or `threshold ≤ 0`  

### Example

```python
from src.regimes.breaks import mean_shift_breaks
import pandas as pd

s = pd.Series([1.0, 1.1, 1.2, 2.0, 2.1])
breaks = mean_shift_breaks(s, window=2, threshold=0.5)

print(breaks)
```

---

## `volatility_shift_breaks`

Detects structural breaks in variance.

### Signature

```python
volatility_shift_breaks(series, window, threshold)
```

### Parameters

| Name        | Type            | Description |
|-------------|-----------------|-------------|
| `series`    | `pandas.Series` | Input time series |
| `window`    | `int`           | Window size for variance comparison |
| `threshold` | `float`         | Minimum variance difference to flag a break |

### Returns

| Type            | Description |
|-----------------|-------------|
| `pandas.Series` | Binary indicator for volatility‑shift breaks |

### Errors

- `TypeError` for incorrect input types  
- `ValueError` if `window < 1` or `threshold ≤ 0`  

### Example

```python
from src.regimes.breaks import volatility_shift_breaks
import pandas as pd

s = pd.Series([0.01, 0.02, 0.50, 0.60, 0.55])
breaks = volatility_shift_breaks(s, window=2, threshold=0.1)

print(breaks)
```

---

## `regime_summary`

Unified wrapper returning all regime‑detection outputs.

### Signature

```python
regime_summary(series, window, threshold, k_regimes=2)
```

### Parameters

| Name         | Type            | Description |
|--------------|-----------------|-------------|
| `series`     | `pandas.Series` | Input time series |
| `window`     | `int`           | Window size for z‑score and break detection |
| `threshold`  | `float`         | Threshold for z‑score and break detection |
| `k_regimes`  | `int`           | Number of Markov‑switching states |

### Returns

Dictionary containing:

| Key                     | Type                | Meaning |
|-------------------------|---------------------|---------|
| `"zscore"`              | `pandas.Series`     | Z‑score regimes |
| `"mean_shift"`          | `pandas.Series`     | Mean‑shift breaks |
| `"volatility_shift"`    | `pandas.Series`     | Variance‑shift breaks |
| `"markov"`              | `dict`              | Markov‑switching outputs |

### Errors

- `TypeError` for incorrect input types  
- `ValueError` for invalid window, threshold, or regime count  

### Example

```python
from src.regimes.summary import regime_summary
import pandas as pd

s = pd.Series([0.01, 0.02, -0.03, 0.10, -0.05])
summary = regime_summary(s, window=3, threshold=2.0, k_regimes=2)

print(summary["zscore"].tail())