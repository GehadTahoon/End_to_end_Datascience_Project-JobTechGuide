# constants
API_URL = 'http://127.0.0.1:5000/'
PREDICTION_ENDPOINT = 'predict_jobs_probs'

import streamlit as st
import requests
import altair as alt
import pandas as pd
import json

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
    <h6 style="text-align: left;  color: #454955; font-family: 'Constantia';">
        {skills_str}
    </h6>
    """,
    unsafe_allow_html=True
)
st.divider()
st.markdown(
    """
    <h4 style="text-align: left; padding-top: 50px; color: black; font-family: 'Constantia'; ">
        Top Jobs Match for You
    </h4>
    """,
    unsafe_allow_html=True
)

# Make API request for job prediction
response = requests.post(API_URL + PREDICTION_ENDPOINT,
                            data=json.dumps(selected_skills),
                            headers={'content-type':'application/json'})

predictions = pd.Series(response.json()).sort_values(ascending=False)


if response.status_code == 200:
    print('Success')
else:
    st.error("Failed to fetch job predictions.")

#***********************************

# Convert to DataFrame and sort by Probability
predictions = pd.Series(predictions)
df = predictions.reset_index()
df.columns = ['Job', 'Probability']
df = df.sort_values(by='Probability', ascending=False)

#Altair horizontal bar chart with sorted color scheme
chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('Probability:Q', scale=alt.Scale(domain=[0, 1])),
    y=alt.Y('Job:N', sort='-x'),
    color=alt.Color('Probability:Q', scale=alt.Scale(domain=[0, 1], scheme='blues'))  # Use a sequential color scheme
).properties(
    title='Job Probabilities'
)

st.altair_chart(chart, use_container_width=True)

st.divider()
#**********************************
if st.button(' Home ',use_container_width=True):
    st.switch_page("app.py")