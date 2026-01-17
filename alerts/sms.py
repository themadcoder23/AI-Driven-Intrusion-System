from twilio.rest import Client
import os

def send_sms_alert(event):
    client = Client(os.getenv("TWILIO_ACCOUNT_SID"),
                    os.getenv("TWILIO_AUTH_TOKEN"))
    client.messages.create(
        body=f"INTRUSION {event.camera_id} {event.confidence}",
        from_=os.getenv("TWILIO_SMS_FROM"),
        to=os.getenv("TWILIO_SMS_TO")#type:ignore
    )
