from google.cloud import firestore
# import os
# os.chdir('C:\\Users\\SPI0003\\OneDrive - boxhillhs.vic.edu.au\\School\\Year 8\\Coding\\Project - Face Recognition\\roll')

db = firestore.Client.from_service_account_json('backend/firebase.json')
def get_all_users() -> list:
    return [x.id for x in db.collection('users').stream()]

def get_user_pass(user) -> str:
    return db.collection('users').document(user).get().to_dict()['password']