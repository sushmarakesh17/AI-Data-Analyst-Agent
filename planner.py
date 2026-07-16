from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

from config import GROQ_API_KEY


class PlannerAgent:
    def __init__(self):
        self.llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name="llama-3.3-70b-versatile",
            temperature=0
        )

    def create_plan(self, user_request, dataframe_summary):
        prompt = f"""
You are an AI Data Analysis Planner.

Based on the user's request and the dataset summary,
create a step-by-step analysis plan.

User Request:
{user_request}

Dataset Summary:
{dataframe_summary}

Return only the analysis plan as numbered steps.
"""

        response = self.llm.invoke(
            [HumanMessage(content=prompt)]
        )

        return response.content