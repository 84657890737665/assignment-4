# Python website using streamlit

# Import
import streamlit as st

# Titgle & Header
st.title("WebWhizPy")
st.header("Get Ready to Be Amazed — Explore What’s Inside")

# About
st.write("This is a simple streamlit app...")

# Button
if st.button("Click Me!"):
    st.write("Thank You for clicking me! 😊")

# user input
name = st.text_input("What's your nice name? ")    
if st.button("streamlit"):
    st.write(f"Hey! {name} Welcome here! ")

