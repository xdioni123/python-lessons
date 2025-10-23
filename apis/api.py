import streamlit as st
import request
import pandas as pd

st.title("Project Managment App")

st.header("Add developer")
dev_name = st.text_input("Developer name")
dev_experience = st.number_imput("Experience (Years)", min_value=0 , max_value=50 value=0)

if st.button ("Create Developer"):
    dev_data = {"name" : dev_name, "experience" : dev_experience}
    response = request.post("http://localhost:8000/developers", json = dev_data)
    st.json(response.json())