import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Agg")  # TkAgg
import seaborn as sns


def main():
    col1, col2 = st.columns([5, 5])
    with col1:
        st.title("Result")
        df = pd.read_csv("data/iris.csv")
        st.dataframe(df.head())

        # Previous Method
        # df["species"].value_counts().plot(kind="bar")
        # st.pyplot()
        # plt.scatter(*np.random.random(size=(2, 100)))
        # st.pyplot()

        # Recommended Method
        st.markdown("### 01. Recommended Method")
        fig, ax = plt.subplots()
        ax.scatter(*np.random.random(size=(2, 100)))
        st.pyplot(fig)

        # Method 3: Simple Method
        st.markdown("### 02. Simple Method 1")
        fig = plt.figure()
        df["species"].value_counts().plot(kind="bar")
        st.pyplot(fig)

        # Method 3
        st.markdown("### 03. Simple Method 2")
        fig, ax = plt.subplots()
        df["species"].value_counts().plot(kind="bar")
        st.pyplot(fig)

        # Alternative For Matplotlib
        st.markdown("### 04. Alternative For Matplotlib")
        fig = plt.figure()
        sns.countplot(df["species"])
        st.pyplot(fig)
    with col2:
        st.title("Code")
        code = """import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")  # TkAgg
import seaborn as sns

        
st.title("Result")
df = pd.read_csv("data/iris.csv")
st.dataframe(df.head())

# Previous Method
st.markdown("### 01. Previous Method")
df["species"].value_counts().plot(kind="bar")
st.pyplot()
plt.scatter(*np.random.random(size=(2, 100)))
st.pyplot()

# Recommended Method
st.markdown("### 02. Recommended Method")
fig, ax = plt.subplots()
ax.scatter(*np.random.random(size=(2, 100)))
st.pyplot(fig)

# Method 3: Simple Method
st.markdown("### 03. Simple Method 1")
fig = plt.figure()
df["species"].value_counts().plot(kind="bar")
st.pyplot(fig)

# Method 3
st.markdown("### 04. Simple Method 2")
fig, ax = plt.subplots()
df["species"].value_counts().plot(kind="bar")
st.pyplot(fig)

# Alternative For Matplotlib
st.markdown("### 05. Alternative For Matplotlib")
fig = plt.figure()
sns.countplot(df["species"])
st.pyplot(fig)"""
        st.code(code)


if __name__ == "__main__":
    main()
