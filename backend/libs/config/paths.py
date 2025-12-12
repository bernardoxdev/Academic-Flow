from pathlib import Path

LIBS_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = LIBS_DIR / 'data'
CSV_DIR = DATA_DIR / 'csv'
DB_DIR = DATA_DIR / 'db'