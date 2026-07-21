"""
SmartHire Configuration File
----------------------------
Stores all project paths and constants.
"""

from pathlib import Path

# Root project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data folders
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
INTERIM_DATA_DIR = BASE_DIR / "data" / "interim"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

# Model folder
MODEL_DIR = BASE_DIR / "models"

# Report folder
REPORT_DIR = BASE_DIR / "reports"

# Random seed
RANDOM_STATE = 42

# TF-IDF configuration
MAX_FEATURES = 5000
NGRAM_RANGE = (1, 2)

# Number of recommended jobs
TOP_K_RECOMMENDATIONS = 10