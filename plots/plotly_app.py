# Core Pkgs
import streamlit as st

# Load EDA Pkg
import pandas as pd
import numpy as np

# Load Data Vis Pkg
import plotly.express as px


def main():
    col1, col2 = st.columns([5, 5])
    with col1:
        st.title("Plotting In Streamlit with Plotly")
        df = pd.read_csv("data/prog_languages_data.csv")
        st.dataframe(df)

        fig = px.pie(df, values="Sum", names="lang", title="Pie Chart of Languages")
        st.plotly_chart(fig)

        fig2 = px.bar(df, x="lang", y="Sum")
        st.plotly_chart(fig2)
    with col2:
        st.title("Code")
        code = """st.title("Plotting In Streamlit with Plotly")
df = pd.read_csv("data/prog_languages_data.csv")
st.dataframe(df)

fig = px.pie(df, values="Sum", names="lang", title="Pie Chart of Languages")
st.plotly_chart(fig)

fig2 = px.bar(df, x="lang", y="Sum")
st.plotly_chart(fig2)"""
        st.code(code)


if __name__ == "__main__":
    main()
