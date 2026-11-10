# 🚗 NHTSA FARS Traffic Safety & Fatality Risk Pipeline

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Scikit-Learn](https://img.shields.io/badge/scikit_learn-ML-orange.svg)](https://scikit-learn.org/)
[![Docker Ready](https://img.shields.io/badge/docker-containerized-2496ED.svg)](https://www.docker.com/)

A professional, modular data engineering and machine learning pipeline built to analyze National Highway Traffic Safety Administration (NHTSA) Fatality Analysis Reporting System (FARS) datasets. 

This project transforms a monolithic Jupyter notebook workflow into an enterprise-ready, modular Python package designed to demonstrate robust software engineering best practices, data pipelines, and predictive modeling in public safety analytics.

---

## 📂 Project Architecture

```text
fars_analysis/
│
├── fars_pipeline_prod/
│   ├── .github/workflows/       # CI/CD pipeline integration
│   ├── data/                    # Raw dataset partitions
│   ├── models/                  # SQL schemas & staging scripts (stg_fars_data.sql)
│   ├── src/                     # Core modular logic
│   │   ├── __init__.py
│   │   ├── data_loader.py       # Ingestion & multi-file relational joins
│   │   ├── features.py          # Data cleaning & feature engineering transformers
│   │   └── train.py             # Centralized pipeline orchestrator & model trainer
│   ├── tests/                   # Unit test suite (pytest)
│   ├── Dockerfile               # Containerization definition
│   └── requirements.txt         # Pinned dependency manifest
│
├── fars_analysis.ipynb          # Exploratory sandbox & visualization notebook
└── README.md