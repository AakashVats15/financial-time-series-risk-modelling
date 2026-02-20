from src.utils.data_loader import load_returns
from src.covariance.empirical_cov import empirical_cov
from src.simulation.correlated_mc import cholesky_simulation, pca_simulation

r = load_returns("data/processed/asset_matrix.csv")

cov = empirical_cov(r)

sim_chol = cholesky_simulation(cov, n_samples=10000)
sim_pca = pca_simulation(cov, n_samples=10000, variance_cutoff=0.99)

print(sim_chol.head())
print(sim_pca.head())