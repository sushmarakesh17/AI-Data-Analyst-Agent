import duckdb
import pandas as pd


class SQLAgent:
    def __init__(self, dataframe):
        self.df = dataframe
        self.connection = duckdb.connect(database=":memory:")
        self.connection.register("dataset", self.df)

    def execute_query(self, query):
        """
        Execute SQL query on the uploaded dataset.
        """
        try:
            result = self.connection.execute(query).fetchdf()
            return result

        except Exception as e:
            return f"Error: {e}"