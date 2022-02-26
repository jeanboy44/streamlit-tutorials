import streamlit as st


def main():
    col1, col2 = st.columns(2)
    with col1:
        st.title("Result")
        name = "Jingeol Ryu"

        if st.button("Submit"):
            st.write(f"Name: {name.upper()}")

        if st.button("Submit", key="new02"):
            st.write(f"First Name: {name.lower()}")

        # Working with RadioButtons
        status = st.radio("What is your status", ("Active", "Inactive"))
        if status == "Active":
            st.success("You are active")
        elif status == "Inactive":
            st.warning("Inactive")

        # Working with Checkbox
        if st.checkbox("Show/Hide"):
            st.text("Showing something")

        # Working with Beta Expander
        if st.expander("Python"):
            st.success("Hello Python")

        with st.expander("Julia"):
            st.text("hello Julia")
    with col2:
        code = """import streamlit as st
        
st.title("Result")
name = "Jingeol Ryu"

if st.button("Submit"):
    st.write(f"Name: {name.upper()}")

if st.button("Submit", key="new02"):
    st.write(f"First Name: {name.lower()}")

# Working with RadioButtons
status = st.radio("What is your status", ("Active", "Inactive"))
if status == "Active":
    st.success("You are active")
elif status == "Inactive":
    st.warning("Inactive")

# Working with Checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing something")

# Working with Beta Expander
if st.expander("Python"):
    st.success("Hello Python")

with st.expander("Julia"):
    st.text("hello Julia")
        """
        st.title("Code")
        st.code(code)


if __name__ == "__main__":
    main()
