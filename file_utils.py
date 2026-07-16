import os


def create_directories():
    """
    Create output directories if they don't exist.
    """

    folders = [
        "outputs",
        "outputs/reports",
        "outputs/charts",
        "outputs/cleaned_data"
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)


def save_dataframe(df, filename):
    """
    Save DataFrame as CSV.
    """

    path = os.path.join("outputs", "cleaned_data", filename)
    df.to_csv(path, index=False)
    return path