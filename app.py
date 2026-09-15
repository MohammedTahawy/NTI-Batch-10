import streamlit as st
#apply css in the button    
if st.button("test1"):
    st.write("button 1 pressed")
if st.button("test2"):
    st.write("button 2 pressed")

st.number_input("Enter a number", min_value=0, max_value=100, value=50)

st.slider("Select a number", 0, 100, 50)

name = st.text_input("enter you name")
st.write("hello", name)