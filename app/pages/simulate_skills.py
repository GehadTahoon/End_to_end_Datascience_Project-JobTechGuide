import streamlit as st

st.markdown(
    """
    <h2 style="text-align: center; color: #462255; font-family: 'Andalus'; ">
        Skills simulation
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
if st.button('👈',use_container_width=True):
    st.switch_page("app.py")