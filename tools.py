import streamlit as st
from google.cloud import firestore
from backend import database as db
import typing

viewBeforeLogin = """
    ## Please Login to access henos Roll Taking system
"""

viewAfterLogin = """
    ## How to Use  
    ### > Mark Roll
    When you select `mark roll`, the system will boot-up and then take a photo of the class.  
    The ai will then scan the picture and mark who is here and who is not into the internal databases.  
    After that, you will get a readout of the picture as well as list of the students and whether thay are here or not.  
      
    ### > Control Panel
    When you select control panel, you will have to enter your admin password again and then you will be able to add new students and stuff like that :)  
      

    P.S. To make a teacher account you need a user with at least `user.Admin` permission level to make it for you :/
"""

viewControlPanel = """
    # Control Panel
    This is the control panel, this is where you can manage your classes and edit your user details
"""

class Admin(User):
    def add_teacher(self, id, name):
        db.db.collection('users').add(id, {
            'name': name,
            'pasword': 'rollTeacher'+id,
            'permlvl': 'teacher.Normal',
            'classes': []
        })

class User:
    def __init__(self, user_id, user_pass):
        self._id = user_id
        self._pass = user_pass
    
    @property
    def id(self):
        return self._id
    
    @property
    def password(self):
        return self._pass
    
    @property
    def name(self):
        return self.data['Name']

def auth(user_id, user_pass) -> bool:
    'authenticates the user'
    user_ids = db.get_all_users()
    if user_id in user_ids:
        if user_pass == db.get_user_pass(user_id):
            return True, None
        else:
            return False, 'pass'
    else:
        return False, 'id'

def mark_roll(user, markdown):
    pass

def control_panel(user, markdown):
    markdown.markdown(viewControlPanel)
    if isinstance(user, Admin):
        column = st.beta_columns(3)
        with column[0]:
            st.header('Details')
            new_id = st.text_input('UserID', value=user.id)
            new_name = st.text_input('Name', value=user.name)
    else:
        column = st.beta_columns(2)