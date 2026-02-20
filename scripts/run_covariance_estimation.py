from src.utils.data_loader import load_returns
from src.covariance.empirical_cov import empirical_cov, empirical_corr, annualized_cov, annualized_vol
from src.covariance.shrinkage_methods import ledoit_wolf, oas_shrinkage, diagonal_shrinkage

r = load_returns("data/processed/asset_matrix.csv")

cov_emp = empirical_cov(r)
corr_emp = empirical_corr(r)
cov_ann = annualized_cov(r)
vol_ann = annualized_vol(r)

cov_lw = ledoit_wolf(r)
cov_oas = oas_shrinkage(r)
cov_diag = diagonal_shrinkage(r, alpha=0.5)

print(cov_emp)
print(corr_emp)
print(cov_ann)
print(vol_ann)
print(cov_lw)
print(cov_oas)
print(cov_diag)