from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import uuid

from core.constants import EVENT_TYPE_INTRUSION, EVENT_STATUS_CONFIRMED

@dataclass
class IntrusionEvent:
    event_id: str
    event_type: str
    camera_id: str
    roi_id: str
    confidence: float
    timestamp: str
    snapshot_path: Optional[str]
    status: str

    @staticmethod
    def create(camera_id, roi_id, confidence):
        return IntrusionEvent(
            event_id=str(uuid.uuid4()),
            event_type=EVENT_TYPE_INTRUSION,
            camera_id=camera_id,
            roi_id=roi_id,
            confidence=round(confidence, 3),
            timestamp=datetime.utcnow().isoformat(),
            snapshot_path=None,
            status=EVENT_STATUS_CONFIRMED
        )
