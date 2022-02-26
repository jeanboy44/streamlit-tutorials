import streamlit as st


def main():
    col1, col2 = st.columns(2)
    with col1:
        st.title("Text Inputs")
        # Text Input
        fname = st.text_input("Enter Firstname")
        # Text Input Hide Password
        password = st.text_input("Enter Password", type="password")
        st.title(fname)

        # Text Area
        message = st.text_area("Enter Message", height=100)
        st.write(message)

        # Numbers
        number = st.number_input("Enter Number", 1.0, 25.0)

        # Date Input
        myappointment = st.date_input("Appointment")

        # Time Input
        mytime = st.time_input("My Time")

        # Color Picker
        color = st.color_picker("Select Color")
    with col2:
        st.title("Code")
        code = """# Text Input
fname = st.text_input("Enter Firstname")
# Text Input Hide Password
password = st.text_input("Enter Password", type="password")
st.title(fname)

# Text Area
message = st.text_area("Enter Message", height=100)
st.write(message)

# Numbers
number = st.number_input("Enter Number", 1.0, 25.0)

# Date Input
myappointment = st.date_input("Appointment")

# Time Input
mytime = st.time_input("My Time")

# Color Picker
color = st.color_picker("Select Color")
        """
        st.code(code)


if __name__ == "__main__":
    main()
