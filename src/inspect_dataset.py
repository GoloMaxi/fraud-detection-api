import pandas as pd
from pathlib import Path


RAW_DIR = Path("data/raw")

train = pd.read_csv(RAW_DIR / "fraudTrain.csv")
test = pd.read_csv(RAW_DIR / "fraudTest.csv")

print(f"train shape: {train.shape}")
print(f"test shape: {test.shape}")

print("\ntrain columns:")
print(train.columns.tolist())

print("\ntest columns:")
print(test.columns.tolist())

print("\ntrain head:")
print(train.head())

print("\ntest head:")
print(test.head())

print("\ntrain info:")
train.info()

print("\ntrain missing values:")
print(train.isna().sum().sort_values(ascending=False))

print("\ntarget counts:")
print(train["is_fraud"].value_counts())

print("\ntarget distribution:")
print(train["is_fraud"].value_counts(normalize=True))

print("\ndescribe for numeric columns:")
print(train.describe())