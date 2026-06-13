import streamlit as st

st.title("🇳🇵 Nepali AI")

name = st.text_input("Enter your name")

if name:
    st.success(f"Namaste, {name}!")

st.write("My first Streamlit app is working!")