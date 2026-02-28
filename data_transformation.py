import pandas as pd

def column_cleaning(df):
    clean_df = df.copy()

    clean_df.columns = (
        clean_df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
    )
    return clean_df

def duplicate_handling(df):
    clean_df = df.copy()
    duplicate_count = clean_df.duplicated().sum()
    print(f"Duplicate found: {duplicate_count}")

    clean_df = clean_df.drop_duplicates()
    return clean_df

def handle_missing_values(df):
    df = df.copy()

    missing_values = df.isnull().sum()
    print(f"Missing values:\n {missing_values}")

    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df[col] = df[col].fillna(
            df[col].mode()[0] if not df[col].mode().empty else ""
        )

    return df

def type_conversion(df):
    df = df.copy()

    df['subscription_date'] = pd.to_datetime(df['subscription_date'], errors='coerce')
    return df
