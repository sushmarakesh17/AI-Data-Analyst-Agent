import pandas as pd


def get_basic_statistics(df):
    """
    Returns dataset statistics.
    """

    stats = {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": int(df.isnull().sum().sum()),
        "Duplicate Rows": int(df.duplicated().sum()),
        "Numeric Columns": list(df.select_dtypes(include="number").columns),
        "Categorical Columns": list(df.select_dtypes(exclude="number").columns),
    }

    return stats


def numerical_summary(df):
    """
    Summary statistics for numeric columns.
    """

    return df.describe().transpose()


def categorical_summary(df):
    """
    Summary statistics for categorical columns.
    """

    return df.describe(include="object").transpose()