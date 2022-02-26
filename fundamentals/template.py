# Core Pkgs
import streamlit as st

# Additional Pkgs

# Import File/Data

# More Fxn

# Config Page
PAGE_CONFIG = {
    "page_title": "StreamlitTutorial",
    "page_icon": "😃",
    "layout": "centered",
}
st.set_page_config(**PAGE_CONFIG)


def main():
    st.title("Streamlit is Awesome")
    menu = ["Home", "About", "Applications"]
    choice = st.sidebar.selectbox("Menu", menu)


if __name__ == "__main__":
    main()
