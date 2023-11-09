import streamlit as st

st.title("Streamlit Program")

firstTextInput = st.text_input("First textbox",key= 1)
secondTextInput = st.text_input("Second textbox",key=2 )

button = st.button("Save text")
if button:
    firstDisplay = st.write(firstTextInput)
    secondDisplay = st.write(secondTextInput)

    