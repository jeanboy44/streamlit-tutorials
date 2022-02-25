import streamlit as st

PRFX = "applications_home"


def main():
    st.title("Fundamentals")

    menu = ["Home", "TextInputs"]
    choice = st.sidebar.selectbox("List", menu, key=f"{PRFX}_cases")

    if choice == "Home":
        pass

    elif choice == "TextInputs":
        pass

    else:
        pass


if __name__ == "__main__":
    main()
