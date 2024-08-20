API_URL = "http://127.0.0.1:5000/predict_jobs_probs"

import streamlit as st
import requests
import altair as alt
import pandas as pd

st.markdown(
    """
    <h2 style="text-align: center; color: #462255; font-family: 'Andalus'; ">
        Jobs prediction
    </h2>
    """,
    unsafe_allow_html=True
)

selected_skills = st.session_state.selected_skills
st.markdown(
    """
    <h4 style="text-align: left; padding-top: 100px; color: black; font-family: 'Constantia'; ">
        Your current skills are
    </h4>
    """,
    unsafe_allow_html=True
)

skills_str = ", ".join(selected_skills)
st.markdown(
    f"""
    <h6 style="text-align: left; color: #454955; font-family: 'Constantia';">
        {skills_str}
    </h6>
    """,
    unsafe_allow_html=True
)

#**********************************
# Make API request for job prediction
response = requests.post(API_URL, json={"available_skills": selected_skills})

if response.status_code == 200:
    st.write('Success')
else:
    st.error("Failed to fetch job predictions.")

#***********************************
if st.button('👈',use_container_width=True):
    st.switch_page("app.py")