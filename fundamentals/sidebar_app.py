# Core Pkgs
import streamlit as st


def main():
    # Adding Section to Sidebar
    st.sidebar.write("-------")

    # Adding Widgets to Sidebar
    st.sidebar.success("Hello World")
    st.sidebar.button("Hello")

    menu = st.sidebar.selectbox("Menu", ["Home", "About"])

    code = """import streamlit as st

# Adding Section to Sidebar
st.sidebar.write("-------")

# Adding Widgets to Sidebar
st.sidebar.success("Hello World")
st.sidebar.button("Hello")

menu = st.sidebar.selectbox("Menu", ["Home", "About"])"""
    st.title("Code")
    st.code(code)


if __name__ == "__main__":
    main()
