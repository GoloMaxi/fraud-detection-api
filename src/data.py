import pandas as pd
from sklearn.model_selection import train_test_split

from src.config import RAW_TRAIN_PATH, RAW_TEST_PATH, TARGET_COL, TEST_SIZE, RANDOM_STATE


def load_raw_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    train = pd.read_csv(RAW_TRAIN_PATH)
    test = pd.read_csv(RAW_TEST_PATH)
    return train, test


def validate_target(df: pd.DataFrame, target_col: str=TARGET_COL) -> None:
    if len(df) == 0:
        raise ValueError("This df is empty")
    if target_col not in df.columns:
        raise ValueError("There are not target in df")
    if df[target_col].isna().any():
        raise ValueError("There are some Nans")
    if df[target_col].nunique() < 2:
        raise ValueError("There are fewer than 2 classes here")
    
    unique_values = set(df[target_col].unique())
    if not unique_values.issubset({0, 1}):
        raise ValueError("Target should contain only 0 and 1")
    

def split_train_valid(df: pd.DataFrame):
    validate_target(df)

    X = df.drop(TARGET_COL, axis=1)
    y = df[TARGET_COL]

    X_train, X_valid, y_train, y_valid = train_test_split(
        X,
        y,
        random_state=RANDOM_STATE,
        test_size=TEST_SIZE,
        stratify=y
    )

    return X_train, X_valid, y_train, y_valid


if __name__ == "__main__":
    train, test = load_raw_data()
    print(f"Train shape: {train.shape}")
    print(f"Test shape: {test.shape}")

    X_train, X_valid, y_train, y_valid = split_train_valid(train)
    print(X_train.shape)
    print(X_valid.shape)
    print(y_train.shape)
    print(y_valid.shape)

    print(f"y_train fraud rate: {y_train.value_counts(normalize=True)}")
    print(f"y_valid fraud rate: {y_valid.value_counts(normalize=True)}")
