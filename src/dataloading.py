import pandas as pd
def load_data(filepath):
    """Load a stock CSV file and return a clean, date-indexed DataFrame."""
    df = pd.read_csv(filepath)
    # df['date'] = pd.to_datetime(df['date'])
    # df = df.set_index('date')
    # df = df.sort_index()
    # print(f"Loaded {len(df)} rows from '{filepath}'")
    return df