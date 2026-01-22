import streamlit as st 
st.title("Hello!!!!!!!!!!!!")
name = st.text_input("Enter Your Name with surename:")
if name:
	st.success(f"Hello {name}, Good Morning!!!")

