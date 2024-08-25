# constants
DATA_PATH = 'file:///C:/Users/DELL/End2End_DS_Projects/JobTechGuide/data/processed/2_cleaned_data.pkl'


# import packages
import streamlit as st 
import pandas as pd

# read data
data = pd.read_pickle(DATA_PATH)

languages = data['LanguageHaveWorkedWith'].columns.tolist()
databases = data['DatabaseHaveWorkedWith'].columns.tolist()
frameworks = data['WebframeHaveWorkedWith'].columns.tolist()
othertech = data['MiscTechHaveWorkedWith'].columns.tolist()
tools = data['ToolsTechHaveWorkedWith'].columns.tolist()

jobs = data['DevType'].columns.tolist()
st.session_state.available_jobs = jobs

# for the heading
st.markdown(
    """
    <h1 style="text-align: center; color: darkred; font-family: 'Andalus'; ">
        Job Tech Guide
    </h1>
    """,
    unsafe_allow_html=True
)
st.divider()
# for header to select skills
st.markdown(
    """
    <h4 style="text-align: left; padding-top: 50px; color: black; font-family: 'Constantia'; ">
        Select your current skills ⭐
    </h4>
    """,
    unsafe_allow_html=True
)
# for language skills
st.markdown(
    """
    <h5 style="text-align: left; color: #335c67; font-family: 'Constantia'; ">
        Languages
    </h5>
    """,
    unsafe_allow_html=True
)
selected_languages = st.multiselect('Languages', languages,label_visibility = 'collapsed')

# for database skills
st.markdown(
    """
    <h5 style="text-align: left; color: #335c67; font-family: 'Constantia'; ">
        Databases
    </h5>
    """,
    unsafe_allow_html=True
)
selected_databases = st.multiselect('Databases', databases, label_visibility = 'collapsed')

# for Web Frameworks skills
st.markdown(
    """
    <h5 style="text-align: left; color: #335c67; font-family: 'Constantia'; ">
        Web Frameworks
    </h5>
    """,
    unsafe_allow_html=True
)
selected_frameworks = st.multiselect('Web Frameworks', frameworks, label_visibility = 'collapsed')

# for Other Tech skills
st.markdown(
    """
    <h5 style="text-align: left; color: #335c67; font-family: 'Constantia'; ">
        Other Tech
    </h5>
    """,
    unsafe_allow_html=True
)
selected_othertech = st.multiselect('Other Tech', othertech, label_visibility = 'collapsed')


# for Tools skills
st.markdown(
    """
    <h5 style="text-align: left; color: #335c67; font-family: 'Constantia'; ">
        Tools
    </h5>
    """,
    unsafe_allow_html=True
)
selected_tools = st.multiselect('Tools', tools, label_visibility = 'collapsed')
skills = [] + selected_languages + selected_databases + selected_frameworks \
        + selected_othertech + selected_tools

st.session_state.selected_skills = skills

st.divider()

st.markdown(
    """
    <h4 style="text-align: left; padding-top: 50px; color: black; font-family: 'Constantia'; ">
        Get the most suitable jobs for your current skills 
    </h4>
    """,
    unsafe_allow_html=True
)


if st.button('Hit here 😃',use_container_width=True):
    # Store selected values in session state
    

    if len(skills) == 0:
        st.warning('Select your current skills')       
    else :
        st.switch_page("pages/predict_jobs.py")


st.markdown(
    """
    <h4 style="text-align: left; padding-top: 50px; color: black; font-family: 'Constantia'; ">
        Get the additional skills you need for a specific job 
    </h4>
    """,
    unsafe_allow_html=True
)

if st.button('Hit here 😀',use_container_width=True):
    # Store selected values in session state
    
    if len(skills) == 0:
        st.warning('Select your current skills')       
    else :
        st.switch_page("pages/simulate_skills.py")
    



#*******************************************

