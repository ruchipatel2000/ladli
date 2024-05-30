import streamlit as st
import numpy as np
st.title("welcome to web application")
st.subheader("maximum")
x=st.number_input("Enter a 1number",value=0,format="%d")
y=st.number_input("Enter a 2number",value=0,format="%d")
z=st.number_input("Enter a 3number",value=0,format="%d")
if st.button("press"):
    result=max([x,y,z])
    st.write(f"maximum is {result}")
