import streamlit as st

from .buttons_app import main as buttons
from .components_app import main as components
from .container_app import main as container
from .display_table_app import main as display_table
from .display_text_app import main as display_text
from .layouts_app import main as layouts
from .text_inputs_app import main as text_input

PRFX = "fundamentals_home"


def main():
    menu = [
        "Home",
        "Buttons",
        "Components",
        "Container",
        "DiaplayTable",
        "DisplayText",
        "Layouts",
        "TextInputs",
    ]
    choice = st.sidebar.selectbox("SubMenu", menu, key=f"{PRFX}_submenu")

    if choice == "Home":
        st.subheader("Home")
    elif choice == "Buttons":
        st.title(f"Fundamentals - {choice}")
        buttons()
    elif choice == "Components":
        st.title(f"Fundamentals - {choice}")
        components()
    elif choice == "Container":
        st.title(f"Fundamentals - {choice}")
        container()
    elif choice == "DiaplayTable":
        st.title(f"Fundamentals - {choice}")
        display_table()
    elif choice == "DisplayText":
        st.title(f"Fundamentals - {choice}")
        display_text()
    elif choice == "Layouts":
        st.title(f"Fundamentals - {choice}")
        layouts()
    elif choice == "TextInputs":
        st.title(f"Fundamentals - {choice}")
        text_input()
    elif choice == "ML":
        pass
    else:
        st.subheader("About")


if __name__ == "__main__":
    main()
