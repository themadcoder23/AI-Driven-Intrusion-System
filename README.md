# 🔐 AI Intrusion Detection System

A **real-time AI-powered intrusion detection system** that monitors a camera feed, detects unauthorized human entry into a user-defined region, logs events to Firebase with proper timestamps, captures forensic snapshot evidence, and sends **WhatsApp, SMS, and Email alerts asynchronously** — without blocking video processing.

This project is built with a **system-first mindset** and follows production-style design principles.

---

## ✨ Features

### 🎥 Computer Vision
- Real-time **person detection** using YOLO
- Interactive **ROI (Region of Interest)** selection using mouse clicks
- **Multi-frame persistence tracking** to reduce false positives

### ⚙️ Event-Driven Architecture
- Central `IntrusionEvent` schema
- Event deduplication with cooldowns
- Detection fully decoupled from alerts and storage

### 🚀 Non-Blocking (Low Latency)
All heavy tasks run in **independent background threads**:
- Firebase logging
- Snapshot saving
- WhatsApp / SMS / Email alerts

The video feed remains smooth during alerts.

### 📸 Forensic Evidence
- Snapshot captured **only when intrusion is confirmed**
- Bounding boxes + confidence overlay
- Timestamp rendered on the image
- Snapshot path stored in Firebase

### ☁️ Cloud Logging (Firebase)
- Events stored in **Firestore**
- Uses **server-side timestamps**
- Clean, query-ready event documents

### 📲 Alerts with Fallback
Alert priority:
1. WhatsApp (Twilio)
2. SMS (Twilio)
3. Email (Gmail SMTP)

Includes **per-channel cooldowns** to prevent alert spam.

---

## 🧱 High-Level Architecture
```text
Camera Feed
│
▼
YOLO Person Detection
│
▼
ROI Filtering
│
▼
Persistence Tracker
│
▼
Intrusion Event
├── Thread: Snapshot Save
├── Thread: Firestore Write
└── Thread: Alerts (WhatsApp → SMS → Email)
```
---

## 📁 Project Structure
```text
intrusion-detection/
├── .env
├── requirements.txt
├── firebase_key.json
├── snapshots/
│ └── intrusion_<event_id>.jpg
├── core/
│ ├── constants.py
│ ├── event_schema.py
│ └── event_guard.py
├── storage/
│ ├── firestore_client.py
│ └── event_store.py
├── detection/
│ ├── detector.py
│ ├── tracker.py
│ ├── roi.py
│ ├── snapshot.py
│ └── run.py
├── alerts/
│ ├── dispatcher.py
│ ├── cooldown.py
│ ├── whatsapp.py
│ ├── sms.py
│ └── email.py
```
---

## 🛠️ Requirements

- Python **3.9+**
- Webcam / Camera
- Firebase account
- Twilio account (trial is sufficient)

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/themadcoder23/AI-Driven-Intrusion-System.git
cd intrusion-detection
```

### 2️⃣ Create virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Firebase Setup

- Go to Firebase Console

- Create a new project

- Enable Firestore Database

- Generate a Service Account Key

- Download the JSON file

- Place it in the project root as:
```bash
firebase_key.json
```
### 📲 Twilio Setup (WhatsApp + SMS)

- Create a Twilio account

- Enable WhatsApp Sandbox

- Join the sandbox by sending:
```bash
join <sandbox-name>
```

to:
```bash
+1 415 523 8886
```

- Copy the following from Twilio Console:

- Account SID

- Auth Token

- Sandbox WhatsApp number

- Your phone number

- ⚠️ Sandbox membership lasts 72 hours (re-join anytime)

### 📧 Email Setup (Gmail)

- Enable 2-Step Verification on your Google account

- Generate a Gmail App Password

- Use that password (not your real Gmail password)

### 🔑 Environment Variables (.env)

Create a .env file in the project root:
```bash
# Email
ALERT_EMAIL=your_email@gmail.com
ALERT_EMAIL_PASSWORD=your_gmail_app_password
ALERT_EMAIL_RECEIVER=your_email@gmail.com

# Firebase
FIREBASE_KEY_PATH=firebase_key.json

# Twilio
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxx
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886
TWILIO_WHATSAPP_TO=whatsapp:+91XXXXXXXXXX
TWILIO_SMS_FROM=+1XXXXXXXXXX
TWILIO_SMS_TO=+91XXXXXXXXXX
```

- ⚠️ Add .env to .gitignore.

### ▶️ Running the System

- Always run from project root:
```bash
python -m detection.run
```

- ❌ Do NOT run python detection/run.py
- ❌ Do NOT change imports to “make it work”

### 🖱️ How to Use

- Camera feed opens

- Select ROI by clicking 3 or more points

- Press ENTER to confirm ROI

- System starts monitoring

- When a person enters ROI:

- Intrusion confirmed after persistence frames

- Snapshot saved with bounding boxes

- Event logged to Firebase

- Alerts sent asynchronously

## 📊 Firebase Event Example
```bash
{
  "event_id": "uuid",
  "camera_id": "CAM_01",
  "roi_id": "ZONE_A",
  "confidence": 0.91,
  "snapshot_path": "snapshots/intrusion_uuid.jpg",
  "status": "confirmed",
  "created_at": "<Firestore Timestamp>"
}
```
## 🚧 Common Issues
### Import errors

- ✔ Run using:
```bash
python -m detection.run
```
### WhatsApp not sending

- ✔ Ensure sandbox joined
- ✔ Check .env values
- ✔ Disable VPN / restricted networks

- Slight lag on first alert

- ✔ Normal one-time cost (TLS + DNS)
- ✔ All heavy operations are async

## 🧠 Design Decisions

- YOLO runs synchronously (CPU/GPU bound)

- All I/O runs asynchronously

- Firebase uses server timestamps

- Clean separation of concerns

- This mirrors real production CV systems.



