import pandas as pd

file_path = "Data/customers-10000.csv"

def extract_data(file_path):
    try:
        print(f"Extracting data from {file_path}......")
        df = pd.read_csv(file_path)
        print(f"Loaded {len(df)} rows and {len(df.columns)} columns.")
        return df

    except FileNotFoundError:
        print("File not found.")
        return None

    except Exception as e:
        print(f"Unexpected error: {e}")
