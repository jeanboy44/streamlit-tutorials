import streamlit as st

PRFX = "plots_home"
from .altair_app import main as altair
from .plotly_app import main as plotly
from .stpyplot_app import main as stpyplot


def main():
    menu = ["Home", "Altair", "Plotly", "StPyPlot"]
    choice = st.sidebar.selectbox("SubMenu", menu, key=f"{PRFX}_cases")

    if choice == "Home":
        st.title("Plots") 
    elif choice == "Altair":
        st.title(f"Plots - {choice}") 
        altair()
    elif choice == "Plotly":
        st.title(f"Plots - {choice}") 
        plotly()
    elif choice == "StPyPlot":
        st.title(f"Plots - {choice}") 
        stpyplot()
    else:
        pass


if __name__ == "__main__":
    main()
