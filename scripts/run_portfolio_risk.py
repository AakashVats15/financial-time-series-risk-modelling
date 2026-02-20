from src.utils.data_loader import load_returns
from src.covariance.empirical_cov import empirical_cov
from src.portfolio.portfolio_variance import portfolio_variance, portfolio_volatility, scenario_variance, scenario_volatility

r = load_returns("data/processed/asset_matrix.csv")

cov = empirical_cov(r)

w = [0.25, 0.25, 0.25, 0.25]

v = portfolio_variance(cov, w)
s = portfolio_volatility(cov, w)

scenarios = {
    "base": cov,
    "stress_up": cov * 1.5,
    "stress_down": cov * 0.7
}

vs = scenario_variance(scenarios, w)
ss = scenario_volatility(scenarios, w)

print(v)
print(s)
print(vs)
print(ss)