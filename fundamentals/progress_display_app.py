import time
import streamlit as st


def main():
    col1, col2 = st.columns(2)

    with col1:
        st.title("Result")
        st.subheader("Progress Bar and Spinner & Balloons")
        if st.button("Show Progress Bar"):
            bar = st.progress(0)
            for pc in range(100):
                time.sleep(pc / 500)
                bar.progress(pc + 1)
            st.success("finished")

        if st.button("Show Spinner"):
            with st.spinner("Processing"):
                # Code Computation
                time.sleep(3)
            st.success("finished")

        if st.button("Show Balloons"):
            st.balloons()
    with col2:
        code = """import time
import streamlit as st
st.title("Result")
st.subheader("Progress Bar and Spinner & Balloons")
if st.button("Show Progress Bar"):
    bar = st.progress(0)
    for pc in range(100):
        time.sleep(pc / 500)
        bar.progress(pc + 1)
    st.success("finished")

if st.button("Show Spinner"):
    with st.spinner("Processing"):
        # Code Computation
        time.sleep(3)
    st.success("finished")

if st.button("Show Balloons"):
    st.balloons()
        """
        st.title("Code")
        st.code(code)


if __name__ == "__main__":
    main()
