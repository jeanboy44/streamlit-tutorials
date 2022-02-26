import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


def main():
    col1, col2 = st.columns([5, 5])
    with col1:
        st.title("Result")

        # Load Dataset
        df = pd.read_csv("data/lang_data.csv")
        st.dataframe(df.head())

        # Bar Chart

        # Line Chart
        lang_list = df.columns.tolist()
        lang_choices = st.multiselect("Choose Language", lang_list, default="Python")
        new_df = df[lang_choices]
        st.line_chart(new_df)

        # Area Chart
        st.area_chart(new_df, use_container_width=True)

        # Altair
        df = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
        c = (
            alt.Chart(df)
            .mark_circle()
            .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
        )
        st.dataframe(df.head())

        # Method 1 Using Write
        st.write(c)

        # Method 2 Using st.altair_chart
        st.altair_chart(c, use_container_width=True)

    with col2:
        st.title("Code")
        code = """import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("Result")

# Load Dataset
# df = pd.read_csv("data/iris.csv")
df2 = pd.read_csv("data/lang_data.csv")
st.dataframe(df2.head())

# Bar Chart
# Using St.bar_chart
# st.bar_chart(df[['sepal_length','petal_length']])

# Line Chart
lang_list = df2.columns.tolist()
lang_choices = st.multiselect("Choose Language", lang_list, default="Python")
new_df = df2[lang_choices]
st.line_chart(new_df)

# Area Chart
st.area_chart(new_df, use_container_width=True)

# Altair
df = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
c = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)
st.dataframe(df.head())

# Method 1 Using Write
st.write(c)

# Method 2 Using st.altair_chart
st.altair_chart(c, use_container_width=True)
"""
        st.code(code)


if __name__ == "__main__":
    main()
