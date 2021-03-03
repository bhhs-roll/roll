"""
Base web app for this project, this is the front of the website

Usage:
for local hosting: `streamlit run streamlit_app.py`

global hosting: `push to github, streamlit will do the rest`

"""

import streamlit as st
import tools
import time

st.title('henos Roll Taking system')
markdown = st.empty()
markdown.markdown(tools.viewBeforeLogin)
id = st.empty()
passw = st.empty()
button = st.empty()
loggedin = False
while not loggedin:
    user_id = id.text_input('User ID')
    user_pass = passw.text_input('Password')
    login = button.button('Login')
    if login:
        with st.spinner('Logging in ...'):
            time.sleep(0.5)
            tf, reason = tools.auth(user_id, user_pass)
        if tf is False and reason == 'id':
            incor = st.error('I could not find a user with that id')
            try_again = button.button('Try again')
            if try_again:
                incor.empty()
                continue
        elif tf is False and reason == 'pass':
            incor = st.error('Incorrect Password')
            try_again = button.button('Try again')
            if try_again:
                incor.empty()
                continue
        else:
            id.empty()
            passw.empty()
            button.empty()
            markdown.empty()
            loggedin = True

success = st.empty()
success.success('Logged in successfully')
time.sleep(2)
button = st.empty()

