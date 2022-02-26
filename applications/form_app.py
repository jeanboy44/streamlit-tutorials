# Core Pkgs
from re import L
import streamlit as st
import pandas as pd


def main():
    st.title("Streamlit Forms & Salary Calculator")
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Forms Tutorial")

        # Salary Calculator
        # Combine forms + columns
        with st.form(key="salaryform", clear_on_submit=True):
            col1, col2, col3 = st.columns([3, 2, 1])

            with col1:
                amount = st.number_input("Hourly Rate in $")
            with col2:
                hour_per_week = st.number_input("Hours Per Week", 1, 168)
            with col3:
                st.text("Salary ")
                submit_salary = st.form_submit_button(label="Calculate")

        if submit_salary:
            with st.expander("Results"):
                daily = [amount * 8]
                weekly = [amount * hour_per_week]
                df = pd.DataFrame({"hourly": amount, "daily": daily, "weekly": weekly})
                df = df.T
                df.columns = ["Amount"]
                st.write(f"Hourly Rate in $: {amount}")
                st.write(f"Hours Per Week: {hour_per_week}")
                st.dataframe(df)

        # Method 1: Context Manage Approach (with)
        with st.form(key="form1"):
            first_name = st.text_input("Firstname")
            last_name = st.text_input("Lastname")
            dob = st.date_input("Date of Birth")

            # Important
            submit_button = st.form_submit_button(label="SignUp")

        # Results Can be either for or outside
        if submit_button:
            st.success(f"Hello {first_name} you have created an account")

        # Method 2:
        form2 = st.form(key="form2")
        user_name = form2.text_input("Username")
        job_type = form2.selectbox("Job", ["Dev", "Data Scientist", "Doctor"])
        submit_button2 = form2.form_submit_button(label="Login")

        if submit_button2:
            st.write(user_name.upper())


if __name__ == "__main__":
    main()
