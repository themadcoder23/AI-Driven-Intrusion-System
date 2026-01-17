class IntrusionTracker:
    def __init__(self, required_frames=15):
        self.required_frames = required_frames
        self.counter = 0
        self.conf_sum = 0.0

    def update(self, inside):
        if inside:
            self.counter += 1
            self.conf_sum += max(d["confidence"] for d in inside)
        else:
            self.reset()

        if self.counter >= self.required_frames:
            avg = self.conf_sum / max(1, self.counter)
            self.reset()
            return True, avg

        return False, None

    def reset(self):
        self.counter = 0
        self.conf_sum = 0.0
