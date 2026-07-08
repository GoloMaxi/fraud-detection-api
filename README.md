# Fraud Detection API

Production-like machine learning project for detecting fraudulent credit card transactions.

## Project Goal

The goal of this project is to predict the probability that a credit card transaction is fraudulent and expose the model through a FastAPI service.

## Dataset

This project uses the Kaggle Credit Card Transactions Fraud Detection Dataset.

The dataset contains simulated credit card transactions with customer, merchant, amount, time, location and fraud label information.

Target column: `is_fraud`.

Raw data is stored locally in `data/raw/` and is not committed to Git.

## Planned Stack

- Python
- pandas
- scikit-learn
- CatBoost
- FastAPI
- PostgreSQL
- Docker Compose
- pytest
- GitHub Actions
