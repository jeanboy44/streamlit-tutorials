import streamlit as st
from PIL import Image


# Set config
logo_img = Image.open("resources/streamlit-mark-color.png")
PAGE_CONFIG = {
    "page_title": "Streamlit Tutorials",
    "page_icon": "✨",
    "layout": "wide",
}
st.set_page_config(**PAGE_CONFIG)


def main():
    st.title("Main App")
    st.subheader("Home")


if __name__ == "__main__":
    main()
