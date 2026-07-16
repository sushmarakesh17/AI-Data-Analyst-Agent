import pandas as pd


def dataframe_summary(df):
    """
    Generate a detailed summary of the DataFrame for the AI Analyst.
    """

    summary = f"""
=========================
DATASET OVERVIEW
=========================

Rows: {df.shape[0]}
Columns: {df.shape[1]}

Column Names:
{list(df.columns)}

Data Types:
{df.dtypes.to_string()}

Missing Values:
{df.isnull().sum().to_string()}

Duplicate Rows:
{df.duplicated().sum()}

"""

    # -----------------------------
    # Sales KPIs
    # -----------------------------
    if "Sales" in df.columns:
        summary += f"""
Total Sales: {df['Sales'].sum():,.2f}
Average Sales: {df['Sales'].mean():,.2f}
Maximum Sale: {df['Sales'].max():,.2f}
Minimum Sale: {df['Sales'].min():,.2f}
"""

    if "Profit" in df.columns:
        summary += f"""
Total Profit: {df['Profit'].sum():,.2f}
Average Profit: {df['Profit'].mean():,.2f}
Maximum Profit: {df['Profit'].max():,.2f}
Minimum Profit: {df['Profit'].min():,.2f}
"""

    if "Quantity" in df.columns:
        summary += f"""
Total Quantity Sold: {df['Quantity'].sum()}
Average Quantity: {df['Quantity'].mean():.2f}
"""

    if "Discount" in df.columns:
        summary += f"""
Average Discount: {df['Discount'].mean():.2f}
Maximum Discount: {df['Discount'].max()}
"""

    # -----------------------------
    # Grouped Insights
    # -----------------------------
    try:
        if "Region" in df.columns and "Sales" in df.columns:
            summary += f"""

Sales by Region:
{df.groupby('Region')['Sales'].sum().sort_values(ascending=False).to_string()}
"""
    except:
        pass

    try:
        if "Category" in df.columns and "Sales" in df.columns:
            summary += f"""

Sales by Category:
{df.groupby('Category')['Sales'].sum().sort_values(ascending=False).to_string()}
"""
    except:
        pass

    try:
        if "State" in df.columns and "Sales" in df.columns:
            summary += f"""

Sales by State:
{df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(10).to_string()}
"""
    except:
        pass

    try:
        if "Customer_Name" in df.columns and "Sales" in df.columns:
            summary += f"""

Top Customers:
{df.groupby('Customer_Name')['Sales'].sum().sort_values(ascending=False).head(10).to_string()}
"""
    except:
        pass

    # -----------------------------
    # Numerical Summary
    # -----------------------------
    try:
        summary += f"""

=========================
NUMERICAL SUMMARY
=========================

{df.describe().to_string()}
"""
    except:
        pass

    # -----------------------------
    # Categorical Summary
    # -----------------------------
    try:
        summary += f"""

=========================
CATEGORICAL SUMMARY
=========================

{df.describe(include='object').to_string()}
"""
    except:
        pass

    # -----------------------------
    # Correlation
    # -----------------------------
    try:
        numeric_df = df.select_dtypes(include="number")

        if len(numeric_df.columns) > 1:
            summary += f"""

=========================
CORRELATION MATRIX
=========================

{numeric_df.corr().to_string()}
"""
    except:
        pass

    # -----------------------------
    # Sample Data
    # -----------------------------
    summary += f"""

=========================
FIRST 10 ROWS
=========================

{df.head(10).to_string()}
"""

    return summary