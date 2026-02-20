# Data Directory

This directory contains all datasets used for examples, documentation, and testing within the framework.  
The structure follows a clean **raw → processed** pipeline to ensure reproducibility and clarity.

---

## Structure

```
data/
│
├── raw/
├── processed/
├── data_gen_processed.py
├── data_gen_raw.py
└── README.md
```

---

## `raw/`

The `raw/` folder contains unmodified input data.  
These files serve as the source of truth for all examples and tests.

Typical contents include:

- Synthetic return series  
- Synthetic covariance matrices  
- Regime‑shift example series  
- Small multi‑asset samples  
- Macro‑economic sample series  

All files in `raw/` are:

- small  
- deterministic  
- free of licensing restrictions  
- suitable for unit tests and documentation examples  

---

## `processed/`

The `processed/` folder contains cleaned and transformed datasets derived from `raw/`.

Examples include:

- log‑returns  
- normalized return series  
- cleaned macro series  
- covariance matrices computed from returns  
- feature‑engineered datasets for examples  

All files in `processed/` must be reproducible from `raw/` via preprocessing scripts.

---

## Scripts

The following scripts support the raw → processed data pipeline:

- **`data_gen_raw.py`** — Generates all synthetic datasets and saves them into `data/raw/`.
- **`data_gen_processed.py`** — Cleans and transforms raw datasets, producing ready‑to‑use files in `data/processed/`.

These scripts ensure that all datasets in the repository are fully reproducible and deterministic.

---

## Guidelines

- Do **not** store large datasets (>1–2 MB).  
- Do **not** store proprietary or licensed market data.  
- Do **not** store temporary or intermediate files.  
- Keep all datasets deterministic for reproducibility.  
- Use synthetic data whenever possible for examples and tests.

---

## Purpose

This directory supports:

- documentation examples  
- API demonstrations  
- unit and integration tests  
- reproducible research workflows  

It ensures that all examples in the framework run consistently without external data dependencies.