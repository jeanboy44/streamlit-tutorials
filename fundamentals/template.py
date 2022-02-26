import streamlit as st

def main():
	col1, col2 = st.columns(2)
	with col1:
		name = "Example"
		st.write(name)
	with col2:
		code = """
name = "Example"
st.write(name)
		"""
		st.code(code)

if __name__ == "__main__":
	main()

































