# Core Pkgs
import streamlit as st


def main():
    col1, col2 = st.columns(2)

    with col1:
        st.title("Result")
        # Select/Multiple select
        my_lang = ["Python", "Julia", "Go", "Rust"]

        choice = st.selectbox("Language", my_lang)
        st.write(f"You selected {choice}")

        # Multiple Selection
        spoken_lang = ("English", "French", "Spanish", "Twi")
        my_spoken_lang = st.multiselect("Spoken Lang", spoken_lang, default="English")

        # Slider
        # Numbers (Int/Float/Dates)
        age = st.slider("Age", 1, 100)

        # Any Datatype
        # Select Slider
        color = st.select_slider(
            "Choose Color",
            options=["yellow", "red", "blue", "black", "white"],
            value=("yellow", "red"),
        )

    with col2:
        code = """import streamlit as st

st.title("Result")
# Select/Multiple select
my_lang = ["Python", "Julia", "Go", "Rust"]

choice = st.selectbox("Language", my_lang)
st.write(f"You selected {choice}")

# Multiple Selection
spoken_lang = ("English", "French", "Spanish", "Twi")
my_spoken_lang = st.multiselect("Spoken Lang", spoken_lang, default="English")

# Slider
# Numbers (Int/Float/Dates)
age = st.slider("Age", 1, 100)

# Any Datatype
# Select Slider
color = st.select_slider(
    "Choose Color",
    options=["yellow", "red", "blue", "black", "white"],
    value=("yellow", "red"),
)
        """
        st.title("Code")
        st.code(code)


if __name__ == "__main__":
    main()
