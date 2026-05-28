import pandas as pd
from IPython.display import display
from pathlib import Path
import re
# import nltk
# from nltk.corpus import stopwords

def check_missing_values(df):

    missing_values = df.isnull().sum()

    missing_percentage = (
        missing_values / len(df)
    ) * 100

    missing_summary = pd.DataFrame({
        'Missing Values': missing_values,
        'Percentage (%)': missing_percentage
    })

    missing_summary = missing_summary[
        missing_summary['Missing Values'] > 0
    ].sort_values(
        by='Percentage (%)',
        ascending=False
    )

    return missing_summary

# HANDLE MISSING VALUES
def handle_missing_values(df, numerical_cols, categorical_cols):

    # Numerical columns
    for col in numerical_cols:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(" ", "")
            .str.replace(",", ".", regex=False)
        )

        df[col] = pd.to_numeric(df[col], errors="coerce")
        if col in df.columns:

            df[col] = df[col].fillna(
                df[col].median()
            )

    # Categorical columns
    for col in categorical_cols:

        if col in df.columns:

            df[col] = df[col].fillna(
                df[col].mode()[0]
            )


    return df