# **Portfolio Risk**

Portfolio risk analysis quantifies how individual asset risks combine to produce overall portfolio volatility. It is a central component of asset allocation, risk budgeting, stress testing, and scenario construction.  
This section outlines the methodology behind portfolio variance, volatility, and scenario‑based risk evaluation as implemented in the framework.

---

## **Conceptual Background**

A portfolio with weight vector `w` and covariance matrix `Σ` has variance:

```
σₚ² = wᵀ Σ w
```

This expression captures how asset volatilities and correlations interact.  
Even if individual assets are volatile, diversification can reduce overall risk when correlations are low.

Portfolio volatility is the square root of variance:

```
σₚ = √(σₚ²)
```

These quantities form the basis for:

- risk budgeting  
- optimization  
- stress testing  
- capital allocation  

---

## **Portfolio Variance**

Given a covariance matrix `Σ` and weights `w`, the portfolio variance is computed as:

```
σₚ² = Σᵢ Σⱼ wᵢ Σᵢⱼ wⱼ
```

This expands to:

- weighted sum of individual variances  
- plus weighted sum of pairwise covariances  

The covariance terms dominate when assets are highly correlated, making diversification less effective.

---

## **Portfolio Volatility**

Portfolio volatility is simply:

```
σₚ = √(wᵀ Σ w)
```

Volatility is easier to interpret than variance because it is expressed in the same units as returns.  
It is widely used in:

- risk reporting  
- volatility targeting  
- position sizing  
- scenario analysis  

---

## **Scenario‑Based Risk Evaluation**

Scenario analysis evaluates how portfolio risk changes under alternative covariance structures.  
A scenario is defined by a modified covariance matrix `Σ*`, such as:

- stressed correlations  
- increased volatilities  
- regime‑specific covariance estimates  
- shrinkage‑adjusted matrices  

For each scenario:

```
σₚ²(Σ*) = wᵀ Σ* w
σₚ(Σ*)  = √(wᵀ Σ* w)
```

This allows analysts to quantify:

- sensitivity to volatility shocks  
- correlation breakdowns  
- regime transitions  
- macroeconomic stress events  

Scenario‑based risk is essential for robust portfolio construction.

---

## **Stress Testing via Covariance Perturbation**

Stress testing modifies the covariance matrix to reflect extreme but plausible conditions.  
Examples include:

- scaling the entire matrix  
  ```
  Σ* = k Σ
  ```
- amplifying correlations  
- increasing specific asset volatilities  
- imposing regime‑specific structures  

These perturbations reveal how the portfolio behaves under adverse environments.

---

## **Interpretation and Use Cases**

Portfolio risk analytics support a wide range of quantitative workflows:

- **Risk budgeting**  
  Decompose total risk into contributions from each asset.

- **Volatility targeting**  
  Adjust exposure to maintain a desired risk level.

- **Scenario construction**  
  Evaluate outcomes under alternative covariance regimes.

- **Stress testing**  
  Assess resilience to volatility spikes or correlation breakdowns.

- **Allocation decisions**  
  Compare risk profiles across candidate portfolios.

---

## **Implementation Characteristics**

The portfolio‑risk module in this framework is designed to be:

- deterministic  
- type‑safe  
- numerically stable  
- compatible with covariance and simulation modules  
- suitable for both research and production‑grade workflows  

It provides a clean, reliable foundation for evaluating portfolio‑level risk under both historical and hypothetical conditions.