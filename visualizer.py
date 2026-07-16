from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

from config import GROQ_API_KEY


class VisualizerAgent:
    def __init__(self):
        self.llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name="llama-3.3-70b-versatile",
            temperature=0
        )

    def recommend_charts(self, dataframe_summary):
        prompt = f"""
You are an expert Data Visualization Analyst.

Based on the dataset summary below, recommend the best visualizations.

Dataset Summary:
{dataframe_summary}

For each recommendation provide:
1. Chart Type
2. X-axis
3. Y-axis
4. Why this chart is useful

Keep the response concise.
"""

        response = self.llm.invoke(
            [HumanMessage(content=prompt)]
        )

        return response.content