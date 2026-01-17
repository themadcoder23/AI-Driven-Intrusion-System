import time

_last_sent = {}

def can_send(channel, key, cooldown=120):
    """
    channel: 'whatsapp' | 'sms' | 'email'
    key: camera_id:roi_id
    """
    now = time.time()
    k = f"{channel}:{key}"

    last = _last_sent.get(k)
    if last is None or (now - last) >= cooldown:
        _last_sent[k] = now
        return True

    return False
