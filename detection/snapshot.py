import cv2, os
from datetime import datetime

os.makedirs("snapshots", exist_ok=True)

def save_snapshot(frame, detections, event_id):
    img = frame.copy()
    for d in detections:
        x1,y1,x2,y2 = d["bbox"]
        cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
    ts = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    cv2.putText(img, ts, (10,img.shape[0]-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)
    path = f"snapshots/intrusion_{event_id}.jpg"
    cv2.imwrite(path, img)
    return path
