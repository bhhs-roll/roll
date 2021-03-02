from google.cloud import firestore

db = firestore.Client('tools/firestore.json')
def get_all_users() -> list:
    return list(db.collection('users').stream())