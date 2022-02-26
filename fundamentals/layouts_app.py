import streamlit as st


def main():
    st.title("Result")

    # Former Layout
    st.subheader("Former Layout")
    st.success("Full Length Wide Layout")

    # Layout/Gridlike Columns
    st.subheader("Former Layout/Gridlie Columns")
    col1, col2 = st.columns(2)
    # Method 1
    col1.success("Col1")
    col2.warning("Col2")

    # Method 2: Context Manager with
    with col1:
        st.info("From Col1")
        fname = st.text_input("Firstname")

    with col2:
        st.success("From col2")

    # 3 Columns
    st.subheader("3 Columns")
    c1, c2, c3 = st.columns(3)

    with c1:
        st.success("From C1")

    with c2:
        st.success("From C2")

    with c3:
        st.info("From C3")

    # Unequal width
    st.subheader("Unequal width")
    c1, c2 = st.columns([3, 1])
    with c1:
        st.success("From C1 3x larger")

    with c2:
        st.info("From C2: less")

    code = """import streamlit as st
    
st.title("Result")

# Former Layout
st.subheader("Former Layout")
st.success("Full Length Wide Layout")

# Layout/Gridlike Columns
st.subheader("Former Layout/Gridlie Columns")
col1, col2 = st.columns(2)
# Method 1
col1.success("Col1")
col2.warning("Col2")

# Method 2: Context Manager with
with col1:
    st.info("From Col1")
    fname = st.text_input("Firstname")

with col2:
    st.success("From col2")

# 3 Columns
st.subheader("3 Columns")
c1, c2, c3 = st.columns(3)

with c1:
    st.success("From C1")

with c2:
    st.success("From C2")

with c3:
    st.info("From C3")

# Unequal width
st.subheader("Unequal width")
c1, c2 = st.columns([3, 1])
with c1:
    st.success("From C1 3x larger")

with c2:
    st.info("From C2: less")
        """
    st.title("Code")
    st.code(code)


if __name__ == "__main__":
    main()
