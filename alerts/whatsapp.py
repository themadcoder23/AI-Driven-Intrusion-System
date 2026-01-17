from twilio.rest import Client
import os

def send_whatsapp_alert(event):
    client = Client(os.getenv("TWILIO_ACCOUNT_SID"),
                    os.getenv("TWILIO_AUTH_TOKEN"))
    client.messages.create(
        body=f"🚨 Intrusion\nCam:{event.camera_id}\nZone:{event.roi_id}\nConf:{event.confidence}",
        from_=os.getenv("TWILIO_WHATSAPP_FROM"),
        to=os.getenv("TWILIO_WHATSAPP_TO")#type:ignore
    )
