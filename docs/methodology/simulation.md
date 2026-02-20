# **Monte Carlo Simulation**

Monte Carlo simulation generates synthetic return paths that preserve the statistical properties of historical data. It is a core tool in risk management, scenario analysis, stress testing, and portfolio construction.  
This section outlines the simulation techniques implemented in the framework, focusing on correlated return generation using Cholesky decomposition and PCA‑based dimensionality reduction.

---

## **Conceptual Background**

A multivariate return vector `rₜ` is often modelled as:

```
rₜ = μ + Lzₜ
```

where:

- `μ` is the mean vector  
- `L` is a matrix that encodes the covariance structure  
- `zₜ` is a vector of independent standard‑normal shocks  

The goal of simulation is to generate synthetic `rₜ` that match the covariance matrix of the original data.

Monte Carlo simulation is used to:

- estimate portfolio volatility and Value‑at‑Risk  
- evaluate tail behaviour  
- construct stress scenarios  
- test portfolio robustness under alternative environments  

---

## **Cholesky‑Based Simulation**

Cholesky decomposition factorizes a positive semi‑definite covariance matrix `Σ` into:

```
Σ = LLᵀ
```

where `L` is lower triangular.

To generate correlated returns:

1. draw independent shocks  
   ```
   z ∼ N(0, I)
   ```
2. apply the Cholesky factor  
   ```
   r = Lz
   ```

This ensures:

- correct covariance structure  
- exact reproduction of linear dependencies  
- deterministic behaviour given a random seed  

Cholesky simulation is fast and widely used in risk engines.

---

## **PCA‑Based Simulation**

Principal Component Analysis (PCA) decomposes the covariance matrix into eigenvalues and eigenvectors:

```
Σ = VΛVᵀ
```

where:

- `V` contains eigenvectors  
- `Λ` contains eigenvalues  

Simulation proceeds by:

1. drawing shocks in the principal‑component space  
   ```
   z ∼ N(0, Λ)
   ```
2. projecting back to the original space  
   ```
   r = Vz
   ```

PCA simulation is particularly useful when:

- the covariance matrix is noisy  
- the number of assets is large  
- only a subset of components explains most variance  

---

## **Variance Cutoff and Dimensionality Reduction**

In high‑dimensional settings, many eigenvalues are small and dominated by noise.  
A variance cutoff retains only the leading components that explain a chosen fraction of total variance.

If the eigenvalues are:

```
λ₁ ≥ λ₂ ≥ … ≥ λₙ
```

and the cumulative variance ratio is:

```
(λ₁ + … + λₖ) / (λ₁ + … + λₙ)
```

then the smallest `k` satisfying the cutoff (e.g., 95%) is selected.

This reduces:

- noise  
- dimensionality  
- computational cost  

while preserving most of the covariance structure.

---

## **Comparing Simulation Methods**

| Method | Strengths | Limitations |
|--------|-----------|-------------|
| Cholesky | Exact covariance reproduction | Sensitive to noise in Σ |
| PCA | Noise‑reduced, scalable | Approximate covariance |
| PCA with cutoff | Dimensionality reduction | Loses small‑variance structure |

Both methods are widely used in quantitative risk modelling.

---

## **Practical Considerations**

When applying Monte Carlo simulation:

- covariance estimation quality directly affects results  
- random seeds ensure reproducibility  
- PCA is preferred when the asset universe is large  
- Cholesky is preferred when exact covariance reproduction is required  

Simulated returns can be used for:

- portfolio stress testing  
- scenario generation  
- distributional analysis  
- risk budgeting  

---

## **Implementation Characteristics**

The simulation module in this framework is designed to be:

- deterministic when seeded  
- numerically stable  
- type‑safe  
- compatible with covariance and portfolio‑risk modules  
- suitable for both research and production‑grade prototyping  

It provides a robust foundation for generating realistic synthetic return paths.