# constants
API_URL = 'http://127.0.0.1:5000/'
PREDICTION_ENDPOINT = 'predict_jobs_probs'
SIMULATION_ENDPOINT = 'recommend_new_skills'


import streamlit as st
import requests
import altair as alt
import pandas as pd
import json
import time

st.markdown(
    """
    <h2 style="text-align: center; color: #462255; font-family: 'Andalus'; ">
        Jobs prediction
    </h2>
    """,
    unsafe_allow_html=True
)

if 'selected_skills' not in st.session_state:
    st.warning('Please go back to home page and select your current skills')
else:
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
        color=alt.Color('Probability:Q', scale=alt.Scale(domain=[0, 1], scheme='viridis'))  # Use a sequential color scheme
    ).properties(
        title='Jobs Probabilities'
    )

    st.altair_chart(chart, use_container_width=True)


    st.markdown(
        """
        <h4 style="text-align: left; padding-top: 50px; color: black; font-family: 'Constantia'; ">
            The top recommended Job for You is
        </h4>
        """,
        unsafe_allow_html=True
    )
    recommended_job = df['Job'][0]
    st.markdown(
        f"""
        <h4 style="
            text-align: center; 
            padding: 20px 10px; 
            color: #333333; 
            font-family: 'Arial'; 
            font-size: 22px; 
            font-weight: bold; 
            background-color: #dee2ff; 
            letter-spacing: 1px; 
            text-shadow: 2px 2px 5px #feeafa; 
            ">
            {recommended_job}
        </h4>    
            

        """,
        unsafe_allow_html=True
        
    )
    st.divider()
    
    st.markdown(
        f"""
        <h4 style="text-align: left; padding-top: 50px; color: black; font-family: 'Constantia'; ">
            Get the additional skills you need to be a/an 
        </h4>
        <h4 style="text-align: left;  color: #5e548e; font-family: 'Constantia';font-weight: bold; text-shadow: 2px 2px 5px #feeafa;  ">
            {recommended_job} 
        </h4>
        """,
        unsafe_allow_html=True
    )

    if st.button('Hit here 😀',use_container_width=True):

        with st.spinner(text='Predicting skills...'):
            # Simulate a delay for testing purposes (you can remove this in actual use)
            time.sleep(0)

            try:
                # Make API request for skills prediction
                response = requests.post(
                    API_URL + SIMULATION_ENDPOINT,
                    data=json.dumps({
                        'available_skills': selected_skills,
                        'target_job': recommended_job
                    }),
                    headers={'content-type': 'application/json'}
                )

                # Check if the request was successful
                if response.status_code == 200:
                    simulation = pd.Series(response.json()).sort_values(ascending=False)
                    print('Success')
                else:
                    st.error("Failed to fetch skills predictions.")

            except Exception as e:
                st.error(f"An error occurred: {e}")
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

        st.markdown(
            f"""
            <p style="
                text-align: center; 
                padding: 20px 10px; 
                color: #333333; 
                font-family: 'Cascadia Mono SemiBold'; 
                font-size: 20px; 
                background-color: #f9dcc4; 
                letter-spacing: 1px; 
                text-shadow: 2px 2px 5px #feeafa; 
                ">
                {",   ".join(skills_df['Skill'])}
            </p>    
            """,
        unsafe_allow_html=True        
        )

    st.divider()

#**********************************
if st.button('👈  Home  👈',use_container_width=True):
    st.switch_page("app.py")