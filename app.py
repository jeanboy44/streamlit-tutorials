# Import libraries
import streamlit as st

# Import modules for other streamlit apps
from home_app import main as home
from fundamentals.home_app import main as fundamentals_home
from applications.home_app import main as applications_home
from plots.home_app import main as plots_home


def main():
    st.sidebar.markdown("# Navigator")
    menu = ["Home", "Fundamentals", "Plots", "Applications"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        home()

    elif choice == "Fundamentals":
        fundamentals_home()

    elif choice == "Plots":
        plots_home()

    elif choice == "Applications":
        applications_home()

    else:
        st.subheader("About")


if __name__ == "__main__":
    main()
