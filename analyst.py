from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

from config import GROQ_API_KEY


class DataAnalystAgent:

    def __init__(self):
        self.llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name="llama-3.3-70b-versatile",
            temperature=0
        )


    def analyze(self, dataframe_summary):

        prompt = f"""
You are a Senior Business Data Analyst.

You have been provided with a dataset summary generated from a real dataset.

Analyze ONLY the information provided below.
Do NOT make assumptions or invent facts.
If information is unavailable, clearly mention that.

=========================
DATASET INFORMATION
=========================

{dataframe_summary}

=========================
YOUR TASK
=========================

Generate a professional business report with the following sections.

## Executive Summary
Provide a concise overview of the dataset.

## Key Insights
Identify the most important findings supported by the data.

## KPI Highlights
If applicable, include:
- Total Sales
- Total Profit
- Average Sales
- Average Profit
- Maximum Sale
- Minimum Sale
- Average Discount
- Total Quantity Sold

If a KPI cannot be calculated from the provided information, mention that it is unavailable.

## Trends
Discuss trends related to:
- Sales
- Profit
- Quantity
- Region
- Category
- Time (if dates are available)

## Data Quality Assessment
Comment on:
- Missing values
- Duplicate records
- Data types
- Outliers (if identifiable)
- Data consistency

## Business Recommendations
Provide 5 actionable recommendations based ONLY on the dataset.

## Interesting Observations
Mention any notable patterns or anomalies.

## Conclusion
Summarize the overall findings in 2–3 sentences.

Important Rules:
- Base every statement only on the provided dataset information.
- Do not hallucinate or fabricate numbers.
- Keep the report professional and business-focused.
- Use bullet points where appropriate.
"""


        response = self.llm.invoke(
            [
                HumanMessage(content=prompt)
            ]
        )


        return response.content
