import smtplib, os
from email.message import EmailMessage

def send_email_alert(event):
    msg = EmailMessage()
    msg["Subject"] = "🚨 Intrusion Detected"
    msg["From"] = os.getenv("ALERT_EMAIL")
    msg["To"] = os.getenv("ALERT_EMAIL_RECEIVER")
    msg.set_content(str(event.__dict__))

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as s:
        s.login(os.getenv("ALERT_EMAIL"),os.getenv("ALERT_EMAIL_PASSWORD"))#type:ignore
        s.send_message(msg)
