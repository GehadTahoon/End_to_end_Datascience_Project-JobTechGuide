import streamlit as st 
import pandas as pd

#def home():

# for the heading
st.markdown(
    """
    <h1 style="text-align: center; color: darkred; font-family: 'Andalus'; ">
        Job Tech Guide
    </h1>
    """,
    unsafe_allow_html=True
)
# for header to select skills
st.markdown(
    """
    <h4 style="text-align: left; padding-top: 100px; color: black; font-family: 'Constantia'; ">
        Select your current skills✨
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
st.multiselect('Languages', ['Python', 'C','C++'],label_visibility = 'collapsed')

# for database skills
st.markdown(
    """
    <h5 style="text-align: left; color: #335c67; font-family: 'Constantia'; ">
        Databases
    </h5>
    """,
    unsafe_allow_html=True
)
st.multiselect('Databases', ['SQL'],label_visibility = 'collapsed')

# for Web Frameworks skills
st.markdown(
    """
    <h5 style="text-align: left; color: #335c67; font-family: 'Constantia'; ">
        Web Frameworks
    </h5>
    """,
    unsafe_allow_html=True
)
st.multiselect('Web Frameworks', ['Flask'],label_visibility = 'collapsed')

# for Other Tech skills
st.markdown(
    """
    <h5 style="text-align: left; color: #335c67; font-family: 'Constantia'; ">
        Other Tech
    </h5>
    """,
    unsafe_allow_html=True
)
st.multiselect('Other Tech', [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],label_visibility = 'collapsed')


# for Tools skills
st.markdown(
    """
    <h5 style="text-align: left; color: #335c67; font-family: 'Constantia'; ">
        Tools
    </h5>
    """,
    unsafe_allow_html=True
)
st.multiselect('Tools', ['Git'],label_visibility = 'collapsed')


st.markdown(
    """
    <h4 style="text-align: left; padding-top: 100px; color: black; font-family: 'Constantia'; ">
        Get the most suitable jobs for your current skills 👇
    </h4>
    """,
    unsafe_allow_html=True
)
if st.button('Hit here 😃',use_container_width=True):
    st.switch_page("pages/predict_jobs.py")

st.markdown(
    """
    <h4 style="text-align: left; padding-top: 100px; color: black; font-family: 'Constantia'; ">
        Get the additional skills you need for a specific job 👇
    </h4>
    """,
    unsafe_allow_html=True
)
if st.button('Hit here 😀',use_container_width=True):
    st.switch_page("pages/simulate_skills.py")




#*******************************************



