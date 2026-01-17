import threading
from alerts.cooldown import can_send
from alerts.whatsapp import send_whatsapp_alert
from alerts.sms import send_sms_alert
from alerts.email import send_email_alert

def _send_alerts(event):
    key = f"{event.camera_id}:{event.roi_id}"

    if can_send("whatsapp", key):
        try:
            send_whatsapp_alert(event); return
        except: pass

    if can_send("sms", key):
        try:
            send_sms_alert(event); return
        except: pass

    if can_send("email", key):
        send_email_alert(event)

def dispatch_alert(event):
    threading.Thread(target=_send_alerts, args=(event,), daemon=True).start()
