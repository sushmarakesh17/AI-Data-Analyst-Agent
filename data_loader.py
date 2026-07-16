import pandas as pd


def load_data(uploaded_file):
    """
    Load CSV or Excel file into a Pandas DataFrame.
    """

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    elif file_name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)

    else:
        raise ValueError("Unsupported file format.")

    return df
