import streamlit as st


def main():
    col1, col2 = st.columns(2)

    with col1:
        st.title("Result")
        # Working with and Displaying Text
        st.text("Hello World this is a text")
        name = "Johnny"
        st.text(f"This is so {name}")

        # Header
        st.header("This is a header")

        # Subheader
        st.subheader("This is a subheader")

        # Title
        st.title("This is a title")

        # Markdown
        st.markdown("## This is markdown")

        # Displaying Colored Text/Bootstraps Alert
        st.success("Successful")
        st.warning("This is danger")
        st.info("This is information")
        st.error("This is an error")
        st.exception("This is an exception")

        # Superfunction
        st.write("Normal Text")
        st.write("## This is a markdown text")
        st.write(1 + 2)

        st.write(dir(st))

        # Help Info
        st.help(range)
    with col2:
        code = """import streamlit as st

st.title("Result")
# Working with and Displaying Text 
st.text("Hello World this is a text")
name = "Johnny"
st.text(f"This is so {name}")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Title
st.title("This is a title")

# Markdown
st.markdown("## This is markdown")

# Displaying Colored Text/Bootstraps Alert
st.success("Successful")
st.warning("This is danger")
st.info("This is information")
st.error("This is an error")
st.exception("This is an exception")

# Superfunction
st.write("Normal Text")
st.write("## This is a markdown text")
st.write(1+2)

st.write(dir(st))

# Help Info
st.help(range)
        """
        st.title("Code")
        st.code(code)


if __name__ == "__main__":
    main()
