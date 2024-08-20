import streamlit as st

st.markdown(
    """
    <h2 style="text-align: center; color: #462255; font-family: 'Andalus'; ">
        Skills simulation
    </h2>
    """,
    unsafe_allow_html=True
)

if st.button('👈',use_container_width=True):
    st.switch_page("app.py")