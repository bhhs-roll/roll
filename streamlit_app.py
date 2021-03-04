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
count = 0
while not loggedin:
    count += 1
    user_id = id.text_input('User ID', key=count)
    user_pass = passw.text_input('Password', type='password', key=count+1)
    login = button.button('Login', key=count+2)
    if login:
        with st.spinner('Logging in ...'):
            time.sleep(0.5)
            tf, reason = tools.auth(user_id, user_pass)
        if tf is False and reason == 'id':
            incor = st.error('I could not find a user with that id')
            try_again = button.button('Try again', key=count+3)
            if try_again:
                incor.empty()
                continue
        elif tf is False and reason == 'pass':
            incor = st.error('Incorrect Password')
            try_again = button.button('Try again', key=count+4)
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
success.empty()

markdown.markdown(tools.viewAfterLogin)

mark = st.empty()
ctrl = st.empty()
markb = mark.button('Mark Roll', key=count+5)
ctrlb = ctrl.button('Control Panel', key=count+6)
if markb:
    tools.mark_roll(user_id)
if ctrlb:
    tools.control_panel(user_id)