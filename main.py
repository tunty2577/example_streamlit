# Import Streamlit
import streamlit as st

# Set the title of the app
st.title("กัปตัน Streamlit App")

# Input fields for user input
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1)

# Display a greeting message and calculate age in months
if st.button("Submit"):
    st.write(f"Hello, {name}! 👋")
    st.write(f"You are {age * 12} months old.")
