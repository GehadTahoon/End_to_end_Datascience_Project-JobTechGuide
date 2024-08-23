# constants
API_URL = 'http://127.0.0.1:5000/'
SIMULATION_ENDPOINT = 'recommend_new_skills'

import streamlit as st
import pandas as pd
import altair as alt
import requests
import json

st.markdown(
    """
    <h2 style="text-align: center; color: #462255; font-family: 'Andalus'; ">
        Skills simulation
    </h2>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <h4 style="text-align: left; padding-top: 100px; color: black; font-family: 'Constantia'; ">
        Your current skills are
    </h4>
    """,
    unsafe_allow_html=True
)
selected_skills = st.session_state.selected_skills
skills_str = ", ".join(selected_skills)
st.markdown(
    f"""
    <h6 style="text-align: left; color: #454955; font-family: 'Constantia';">
        {skills_str}
    </h6>
    """,
    unsafe_allow_html=True
)
st.divider()
st.markdown(
    """
    <h4 style="text-align: left; padding-top: 50px; color: black; font-family: 'Constantia'; ">
        Select the job you are looking forward to
    </h4>
    """,
    unsafe_allow_html=True
)

jobs = st.session_state.available_jobs
selected_job = st.selectbox(options=jobs,label="Select a job",label_visibility='collapsed', index=None, placeholder="Select a job")

if selected_job == None:
    st.warning('Select a job to get the additional skills you need')       
else :
    st.divider()
    st.markdown(
        """
        <h4 style="text-align: left; padding-top: 70px; padding-bottom: 50px; color: black; font-family: 'Constantia'; ">
            Top skills Match for You
        </h4>
        """,
        unsafe_allow_html=True
    )

    

    # Make API request for skills prediction

    response = requests.post(API_URL + SIMULATION_ENDPOINT,
                                data=json.dumps({
                                    'available_skills': selected_skills,
                                    'target_job': selected_job
                                }),
                                headers={'content-type':'application/json'})
    simulation = pd.Series(response.json()).sort_values(ascending=False)

    if response.status_code == 200:
        print('Success')
    else:
        st.error("Failed to fetch skills predictions.")


    #*************************************

    skills_df = pd.Series(simulation).reset_index()
    skills_df.columns = ['Skill', 'Probability']
    skills_df = skills_df.sort_values(by='Probability', ascending=False)


    skills_chart = alt.Chart(skills_df).mark_bar().encode(
            x=alt.X('Probability:Q', scale=alt.Scale(domain=[0, 1])),
            y=alt.Y('Skill:N', sort='-x'),
            color=alt.Color('Probability:Q', scale=alt.Scale(domain=[0, 1], scheme='plasma'))
        ).properties(
            title='Top Skills'
        )
    st.altair_chart(skills_chart, use_container_width=True)

#***************************************
st.divider()
if st.button('👈 Home 👈',use_container_width=True):
    st.switch_page("app.py")