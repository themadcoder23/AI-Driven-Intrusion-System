import cv2
import numpy as np

roi_points = []

def draw_roi(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        roi_points.append((x, y))

def select_roi(frame):
    roi_points.clear()
    cv2.namedWindow("ROI")
    cv2.setMouseCallback("ROI", draw_roi)

    while True:
        temp = frame.copy()
        for p in roi_points:
            cv2.circle(temp, p, 5, (0,255,0), -1)
        if len(roi_points) >= 2:
            cv2.polylines(temp, [np.array(roi_points)], False, (0,255,0), 2)
        cv2.imshow("ROI", temp)
        if cv2.waitKey(1) & 0xFF == 13:
            break

    cv2.destroyAllWindows()
    if len(roi_points) < 3:
        return None
    return np.array(roi_points, dtype=np.int32)

def is_inside_roi(bbox, roi):
    contour = roi.reshape((-1,1,2))
    x1,y1,x2,y2 = bbox
    cx, cy = (x1+x2)//2, (y1+y2)//2
    return cv2.pointPolygonTest(contour, (cx,cy), False) >= 0
