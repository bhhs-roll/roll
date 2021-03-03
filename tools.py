import streamlit as st
from google.cloud import firestore
from backend import database as db

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

# class IncorrectPassword(Exception):
#     pass

# class IncorrectUserID(Exception):
#     pass

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