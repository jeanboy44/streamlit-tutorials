import streamlit as st

PRFX = "applications_home"
from .altair_app import main as altair
from .plotly_app import main as plotly
from .stpyplot_app import main as stpyplot


def main():
    menu = ["Home", "Altair", "Plotly", "StPyPlot"]
    choice = st.sidebar.selectbox("Examples", menu, key=f"{PRFX}_cases")

    if choice == "Home":
        st.title("Plots")
    elif choice == "Altair":
        altair()
    elif choice == "Plotly":
        plotly()
    elif choice == "StPyPlot":
        stpyplot()
    else:
        pass


if __name__ == "__main__":
    main()
