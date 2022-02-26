import streamlit as st

from .text_inputs_app import main as text_input

PRFX = "fundamentals_home"


def main():
    st.title("Fundamentals")

    menu = ["Home", "TextInputs"]
    choice = st.sidebar.selectbox("SubMenu", menu, key=f"{PRFX}_cases")

    if choice == "Home":
        st.subheader("Home")

    elif choice == "TextInputs":
        text_input()
    elif choice == "ML":
        pass
    else:
        st.subheader("About")


if __name__ == "__main__":
    main()
