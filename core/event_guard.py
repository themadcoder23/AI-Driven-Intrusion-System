import time
from core.constants import DEFAULT_EVENT_COOLDOWN

_last_event = {}

def can_emit_event(camera_id, roi_id, cooldown=DEFAULT_EVENT_COOLDOWN):
    key = f"{camera_id}:{roi_id}"
    now = time.time()
    last = _last_event.get(key)

    if last is None or now - last >= cooldown:
        _last_event[key] = now
        return True
    return False
