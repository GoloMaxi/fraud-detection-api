from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODEL_DIR = PROJECT_ROOT / "models"
REPORTS_DIR = PROJECT_ROOT / "reports"

RAW_TRAIN_PATH = RAW_DATA_DIR / "fraudTrain.csv"
RAW_TEST_PATH = RAW_DATA_DIR / "fraudTest.csv"

TARGET_COL = "is_fraud"
RANDOM_STATE = 42
TEST_SIZE = 0.2

MODEL_PATH = MODEL_DIR / "fraud_model.joblib"