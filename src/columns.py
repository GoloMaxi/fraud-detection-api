EXPECTED_RAW_COLUMNS = [
    "Unnamed: 0",
    "trans_date_trans_time",
    "cc_num",
    "merchant",
    "category",
    "amt",
    "first",
    "last",
    "gender",
    "street",
    "city",
    "state",
    "zip",
    "lat",
    "long",
    "city_pop",
    "job",
    "dob",
    "trans_num",
    "unix_time",
    "merch_lat",
    "merch_long",
    "is_fraud",
]


RAW_INDEX_COLUMNS = [
    "Unnamed: 0"
]

TRANSACTION_ID_COLUMNS = [
    "trans_num"
]

PERSONAL_COLUMNS = [
    "first",
    "last",
    "street",
]

CUSTOMER_ID_COLUMNS = [
    "cc_num"
]

DATETIME_COLUMNS = [
    "trans_date_trans_time",
    "dob",
    "unix_time"
]

LOCATION_COLUMNS = [
    "lat",
    "long",
    "merch_lat",
    "merch_long"
]

CATEGORICAL_COLUMNS = [
    "merchant",
    "category",
    "gender",
    "city",
    "state",
    "zip",
    "job"
]

NUMERIC_COLUMNS = [
    "amt",
    "city_pop"
]


BASELINE_DROP_COLUMNS = (
    RAW_INDEX_COLUMNS
    + TRANSACTION_ID_COLUMNS
    + PERSONAL_COLUMNS
    + CUSTOMER_ID_COLUMNS
)

def validate_column_groups() -> None:
    all_grouped_columns = set(
        RAW_INDEX_COLUMNS
        + TRANSACTION_ID_COLUMNS
        + PERSONAL_COLUMNS
        + CUSTOMER_ID_COLUMNS
        + DATETIME_COLUMNS
        + LOCATION_COLUMNS
        + CATEGORICAL_COLUMNS
        + NUMERIC_COLUMNS
    )

    expected_columns = set(EXPECTED_RAW_COLUMNS)

    unknown_columns = all_grouped_columns - expected_columns

    if unknown_columns:
        raise ValueError(f"Unknown columns in column groups: {unknown_columns}")


if __name__ == "__main__":
    validate_column_groups()

    print("Column groups are valid")
    print("Baseline drop columns:", BASELINE_DROP_COLUMNS)


