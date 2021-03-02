"""
Base web app for this project, this is the front of the website

Usage:
for local hosting: `streamlit run streamlit_app.py`

global hosting: `push to github, streamlit will do the rest`

"""

import streamlit as st
import tools

markdown = st.empty()

st.title('henos Roll Taking system')
markdown.markdown(tools.viewBeforeLogin)
id = st.empty()
passw = st.empty()
user_id = id.text_input('ID')
user_pass = passw.text_input('Password')
login = st.button('Login')
if login:
    markdown.empty()
    id.empty()
    passw.empty()
    tools.auth(user_id, user_pass)