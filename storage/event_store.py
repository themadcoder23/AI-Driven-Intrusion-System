from google.cloud.firestore_v1 import SERVER_TIMESTAMP
from core.event_schema import IntrusionEvent
from storage.firestore_client import get_firestore_client

db = get_firestore_client()

def save_event(event: IntrusionEvent):
    data = event.__dict__.copy()

    # ✅ Proper Firestore server timestamp
    data["created_at"] = SERVER_TIMESTAMP

    db.collection("events").document(event.event_id).set(data)
