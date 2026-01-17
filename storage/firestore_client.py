import firebase_admin
from firebase_admin import credentials, firestore
import os

def get_firestore_client():
    if not firebase_admin._apps:
        cred = credentials.Certificate(
            os.getenv("FIREBASE_KEY_PATH", "firebase_key.json")
        )
        firebase_admin.initialize_app(cred)
    return firestore.client()
