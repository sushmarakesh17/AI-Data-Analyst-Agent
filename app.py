import streamlit as st

from config import (
    APP_TITLE,
    PAGE_ICON,
    LAYOUT,
)

from data_loader import load_data
from data_cleaner import clean_data
from statistics import (
    get_basic_statistics,
    numerical_summary,
    categorical_summary,
)

from helpers import dataframe_summary
from analyst import DataAnalystAgent


# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
)

st.title("🤖 AI Data Analyst")
st.write("Upload a CSV or Excel file and get AI-powered insights.")


# -------------------------------------------------
# Upload
# -------------------------------------------------
uploaded_file = st.file_uploader(
    "Upload CSV or Excel",
    type=["csv", "xlsx"]
)


if uploaded_file is not None:

    df = load_data(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())


    if st.button("Run AI Analysis"):

        # Clean data
        df = clean_data(df)


        # Statistics
        stats = get_basic_statistics(df)

        st.subheader("Dataset Statistics")
        st.json(stats)


        st.subheader("Numerical Summary")
        st.dataframe(numerical_summary(df))


        try:
            st.subheader("Categorical Summary")
            st.dataframe(categorical_summary(df))

        except Exception:
            pass


        # AI Analysis
        with st.spinner("AI is analyzing your data..."):

            summary = dataframe_summary(df)

            analyst = DataAnalystAgent()

            insights = analyst.analyze(summary)


        st.subheader("AI Insights")
        st.write(insights)


else:
    st.info("Please upload a dataset to begin.")
