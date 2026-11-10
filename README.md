# 🚨 NHTSA FARS Traffic Safety & Fatality Risk Pipeline

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-orange.svg)](https://scikit-learn.org/)
[![Docker Ready](https://img.shields.io/badge/docker-containerized-2496ED.svg)](https://www.docker.com/)

A professional, modular data engineering and machine learning pipeline built to analyze traffic safety patterns and predict severe and fatal motor vehicle accident outcomes using the National Highway Traffic Safety Administration (NHTSA) Fatality Analysis Reporting System (FARS) dataset.

This project transforms a monolithic Jupyter notebook workflow into an enterprise-ready data pipeline, emphasizing modular architecture, relational data engineering, reproducibility, and production readiness.

---

## 📁 Project Architecture

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
```

---

## 📊 Key Features & Methodology

1. **Relational Data Engineering:** Programmatically merges massive multi-table relational files (`person.csv`, `vehicle.csv`, and auxiliary files) on compound keys (`STATE`, `ST_CASE`, `VEH_NO`).

2. **Modular Pipeline Design:** Separates concerns cleanly into data ingestion (`data_loader.py`), transformation (`features.py`), and orchestration (`train.py`).

3. **Predictive Modeling:** Implements a tuned `RandomForestClassifier` targeting severe/fatal accident outcomes (`INJ_SEV == 4`), evaluated using robust metrics (ROC-AUC, Precision-Recall).

4. **Production Readiness:** Includes a fully configured `Dockerfile` and automated unit testing capabilities.

---

## 🚀 Quickstart Guide

### 1. Clone & Set Up Environment

```bash
git clone https://github.com/Addison-McGhee/fars_analysis.git
cd fars_analysis

python -m venv .venv

# Activate environment (Mac/Linux)
source .venv/bin/activate

# On Windows use:
# .venv\Scripts\activate

pip install -r requirements.txt
```

### 2. Run the End-to-End Pipeline

Execute the centralized orchestration script to load data, process features, train the model, and print performance reports directly to your terminal:

```bash
python fars_pipeline_prod/src/train.py
```

### 3. Run Containerized (Docker)

Build and execute the pipeline inside a Docker container:

```bash
docker build -t fars-pipeline -f fars_pipeline_prod/Dockerfile .

docker run --rm fars-pipeline
```

---

## 🧪 Testing

Run the automated unit test suite using `pytest`:

```bash
pytest fars_pipeline_prod/tests/
```

---

## 🛠️ Technologies Used

- **Python 3.12** – Core programming language
- **Pandas / NumPy** – Data manipulation and numerical computing
- **Scikit-Learn** – Machine learning and predictive modeling
- **SQL** – Relational data engineering and staging
- **Pytest** – Automated testing
- **Docker** – Containerization and reproducibility
- **GitHub Actions** – Continuous integration and automated workflows

---

## 📈 Model Evaluation

The classification model is evaluated using metrics appropriate for an imbalanced classification problem:

- ROC-AUC
- Precision
- Recall
- Precision-Recall performance

The primary objective is to identify severe and fatal accident outcomes while evaluating the trade-off between false positives and false negatives.

---

## 📌 Future Improvements

- Expand hyperparameter optimization and cross-validation.
- Incorporate additional FARS years to evaluate temporal generalizability.
- Explore alternative classification algorithms, including gradient boosting.
- Implement model tracking and experiment management.
- Develop interactive visualizations for traffic safety trends and model predictions.

---

## 📚 Data Source

National Highway Traffic Safety Administration (NHTSA).

[Fatality Analysis Reporting System (FARS)](https://www.nhtsa.gov/research-data/fatality-analysis-reporting-system-fars)