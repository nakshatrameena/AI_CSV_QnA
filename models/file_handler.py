import pandas as pd

def load_csv(file_path):
    """Load and validate CSV file."""
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        return f"Error loading CSV: {e}"
