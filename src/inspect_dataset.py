import pandas as pd

from src.config import RAW_TRAIN_PATH, RAW_TEST_PATH, TARGET_COL

train = pd.read_csv(RAW_TRAIN_PATH)
test = pd.read_csv(RAW_TEST_PATH)

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
print(train[TARGET_COL].value_counts())

print("\ntarget distribution:")
print(train[TARGET_COL].value_counts(normalize=True))

print("\ndescribe for numeric columns:")
print(train.describe())