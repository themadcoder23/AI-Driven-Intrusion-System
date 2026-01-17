from ultralytics import YOLO#type:ignore

class PersonDetector:
    def __init__(self, model_path="yolov8n.pt", conf_thresh=0.5):
        self.model = YOLO(model_path)
        self.conf_thresh = conf_thresh

    def detect(self, frame):
        results = self.model(frame, verbose=False)[0]
        detections = []

        for box in results.boxes:
            if int(box.cls[0]) == 0:
                conf = float(box.conf[0])
                if conf >= self.conf_thresh:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    detections.append({
                        "bbox": (x1, y1, x2, y2),
                        "confidence": conf
                    })
        return detections
