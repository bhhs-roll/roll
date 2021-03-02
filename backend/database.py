from google.cloud import firestore

_db = firestore.Client('tools/')
def get_all_users() -> list:
