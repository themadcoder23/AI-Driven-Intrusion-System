from dotenv import load_dotenv
load_dotenv()

import cv2, threading

from detection.detector import PersonDetector
from detection.tracker import IntrusionTracker
from detection.roi import select_roi, is_inside_roi
from detection.snapshot import save_snapshot

from core.event_schema import IntrusionEvent
from core.event_guard import can_emit_event
from storage.event_store import save_event
from alerts.dispatcher import dispatch_alert

CAMERA_ID = "CAM_01"
ROI_ID = "ZONE_A"

def main():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if not ret:
        return

    roi = select_roi(frame)
    if roi is None:
        return

    detector = PersonDetector()
    tracker = IntrusionTracker()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detections = detector.detect(frame)
        inside = [d for d in detections if is_inside_roi(d["bbox"], roi)]

        confirmed, conf = tracker.update(inside)

        if confirmed and can_emit_event(CAMERA_ID, ROI_ID):
            event = IntrusionEvent.create(CAMERA_ID, ROI_ID, conf)

            threading.Thread(
                target=lambda: setattr(
                    event, "snapshot_path",
                    save_snapshot(frame, inside, event.event_id)
                ),
                daemon=True
            ).start()

            threading.Thread(target=save_event, args=(event,), daemon=True).start()
            dispatch_alert(event)

        cv2.imshow("feed", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
