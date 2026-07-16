import plotly.express as px
import pandas as pd


def bar_chart(df, x_column, y_column):
    """
    Generate a bar chart.
    """
    fig = px.bar(
        df,
        x=x_column,
        y=y_column,
        title=f"{y_column} by {x_column}"
    )
    return fig


def line_chart(df, x_column, y_column):
    """
    Generate a line chart.
    """
    fig = px.line(
        df,
        x=x_column,
        y=y_column,
        title=f"{y_column} by {x_column}"
    )
    return fig


def scatter_chart(df, x_column, y_column):
    """
    Generate a scatter chart.
    """
    fig = px.scatter(
        df,
        x=x_column,
        y=y_column,
        title=f"{y_column} vs {x_column}"
    )
    return fig


def histogram(df, column):
    """
    Generate a histogram.
    """
    fig = px.histogram(
        df,
        x=column,
        title=f"Distribution of {column}"
    )
    return fig


def pie_chart(df, column):
    """
    Generate a pie chart.
    """
    counts = df[column].value_counts().reset_index()
    counts.columns = [column, "Count"]

    fig = px.pie(
        counts,
        names=column,
        values="Count",
        title=f"{column} Distribution"
    )
    return fig