import pandas as pd
from slaw_config import DATA_PATH

def load_data():
    """Load business ideas and regulatory data from CSV."""
    try:
        df = pd.read_csv(DATA_PATH)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"Data not found at {DATA_PATH}")