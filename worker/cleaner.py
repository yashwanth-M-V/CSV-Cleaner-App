import pandas as pd

def clean_csv(df: pd.DataFrame):
    # SIMPLE PLACEHOLDER — replace with your advanced logic later
    df = df.drop_duplicates()
    df = df.fillna("")

    return df
