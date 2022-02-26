import pandas as pd
import streamlit as st 

def main():
	col1, col2 = st.columns(2)
	with col1:
		st.title("Display Table")
		df = pd.read_csv("data/iris.csv")

		# Method 1
		st.dataframe(df)

		# Adding A color style from pandas
		st.dataframe(df.style.highlight_max(axis=0))

		# Method 2: Static Table
		st.table(df.head())

		# Method 3: Using superfxn st.write
		st.write(df)

		# Display Json
		st.json({'data':'name'})

		# Display Code
		mycode = """
		def sayhello():
		print("Hello Streamlit Lovers)

		"""
		st.code(mycode,language='python')

	with col2:
		code = """import pandas as pd
import streamlit as st

st.title("Display Table")
df = pd.read_csv("data/iris.csv")

# Method 1
st.dataframe(df)

# Adding A color style from pandas
st.dataframe(df.style.highlight_max(axis=0))

# Method 2: Static Table
st.table(df.head())

# Method 3: Using superfxn st.write
st.write(df)

# Display Json
st.json({'data':'name'})

# Display Code
mycode = \"\"\"
def sayhello():
print("Hello Streamlit Lovers)
\"\"\"
st.code(mycode,language='python')
"""
		st.title("Code")
		st.code(code)


if __name__ == "__main__":
	main()


















