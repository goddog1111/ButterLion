import os
import pandas as pd
from pathlib import Path

def find_csv_file():
    """Find the first CSV file in the current directory."""
    current_dir = Path('.')
    csv_files = list(current_dir.glob('*.csv'))
    if not csv_files:
        raise FileNotFoundError("No CSV files found in the current directory")
    return str(csv_files[0])

def load_data():
    """Load the CSV file and return a pandas DataFrame."""
    csv_path = find_csv_file()
    print(f"Loading data from: {csv_path}")
    
    # Try different encodings
    encodings = ['utf-8', 'big5', 'cp950']
    for encoding in encodings:
        try:
            df = pd.read_csv(csv_path, encoding=encoding)
            print(f"Successfully loaded with {encoding} encoding")
            return df
        except UnicodeDecodeError:
            continue
    
    raise ValueError("Could not decode the CSV file with any of the attempted encodings")

if __name__ == "__main__":
    df = load_data()
    print("\nData Preview:")
    print(df.head())
    print("\nData Info:")
    print(df.info()) 