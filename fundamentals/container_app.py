# Core Pkgs
import streamlit as st


def main():
    col1, col2 = st.columns(2)

    with col1:
        st.title("Result")
        st.text("Multiple elements out of order ")

        # Method 1
        container = st.container()
        container.success("Inside Container 1")

        st.success("Outside Container 1")

        # Method 2: Context Manager
        with container:
            st.warning("Inside Container 2")

        st.warning("Outside Container 2")
        st.info("Outside Container 3")

        container.info("Inside Container 3")  # Method 1
        container.write("Inside Container 4")  # Method 1

        st.write("Outside Container 4")

    with col2:
        code = """import streamlit as st 
		
st.title("Result")
st.text("Multiple elements out of order ")

# Method 1
container = st.container()
container.success("Inside Container 1")

st.success("Outside Container 1")

# Method 2: Context Manager
with container:
	st.warning("Inside Container 2")

st.warning("Outside Container 2")
st.info("Outside Container 3")

container.info("Inside Container 3") # Method 1
container.write("Inside Container 4") # Method 1

st.write("Outside Container 4")
		"""
        st.title("Code")
        st.code(code)


if __name__ == "__main__":
    main()
