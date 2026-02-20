# **Regime Detection**

Regime detection identifies periods in which the statistical properties of a time series shift. Financial markets frequently transition between environments such as low‑volatility expansion, high‑volatility stress, liquidity shocks, or structural breaks. Recognizing these shifts is essential for risk management, portfolio construction, and scenario analysis.  
This section outlines the regime‑detection methods implemented in the framework.

---

## **Conceptual Background**

A regime refers to a segment of time during which the behaviour of a series is relatively stable. Regimes may differ in:

- volatility  
- mean level  
- autocorrelation structure  
- shock persistence  
- correlation with other assets  

Regime detection helps answer questions such as:

- When did volatility spike?  
- When did the mean return shift?  
- When did the market transition from calm to stressed?  

Different techniques capture different types of structural change.

---

## **Z‑Score Volatility Regimes**

A simple and effective approach to identifying volatility regimes is based on standardized deviations from a rolling mean.  
For a rolling window of length `n`, compute:

```
μₜ = mean(rₜ₋ₙ₊₁ … rₜ)
σₜ = std(rₜ₋ₙ₊₁ … rₜ)
zₜ = (rₜ − μₜ) / σₜ
```

A regime indicator is then defined as:

```
regimeₜ = 1 if |zₜ| > threshold
regimeₜ = 0 otherwise
```

This method highlights periods of unusually large movements relative to recent history.

---

## **Markov‑Switching Volatility Regimes**

Markov‑switching models assume that the series transitions between hidden states, each with its own volatility level.  
A two‑state model typically assumes:

```
State 0: low volatility
State 1: high volatility
```

The return process is modelled as:

```
rₜ = εₜ,     εₜ ∼ N(0, σₛₜ²)
```

where `sₜ` is the latent state at time `t`.  
State transitions follow a Markov chain:

```
P(sₜ = i | sₜ₋₁ = j) = pᵢⱼ
```

This approach captures persistent volatility regimes and is widely used in macro‑finance and risk modelling.

---

## **Mean‑Shift Break Detection**

Mean‑shift detection identifies abrupt changes in the average level of a series.  
A simple formulation compares rolling means before and after a candidate break point:

```
μ₁ = mean(y₁ … yₖ)
μ₂ = mean(yₖ₊₁ … yₙ)
```

A break is flagged when the difference `|μ₂ − μ₁|` exceeds a threshold.  
This method is useful for identifying structural changes in returns, spreads, or macroeconomic indicators.

---

## **Volatility‑Shift Break Detection**

Volatility‑shift detection focuses on abrupt changes in variance.  
For a window of length `n`, compute:

```
σ₁² = variance(y₁ … yₖ)
σ₂² = variance(yₖ₊₁ … yₙ)
```

A break is detected when:

```
|σ₂² − σ₁²| > threshold
```

This technique is effective for identifying transitions into and out of stressed market environments.

---

## **Comparing Regime Methods**

Each method captures different aspects of structural change:

| Method | Detects | Strengths | Limitations |
|--------|---------|-----------|-------------|
| Z‑Score | Local volatility spikes | Simple, fast | Sensitive to window choice |
| Markov‑Switching | Persistent hidden states | Captures regime persistence | Requires model estimation |
| Mean‑Shift | Level changes | Good for structural breaks | Not volatility‑aware |
| Volatility‑Shift | Variance changes | Highlights stress transitions | Ignores mean behaviour |

A robust analysis often combines multiple methods.

---

## **Implementation Characteristics**

The regime‑detection module in this framework is designed to be:

- deterministic  
- type‑safe  
- free of hidden randomness (except where explicitly seeded)  
- consistent in output format  
- compatible with volatility and covariance modules  

These tools provide a reliable foundation for stress testing, scenario generation, and risk‑aware portfolio construction.