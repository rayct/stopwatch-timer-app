import time


class Timer:

    def __init__(self):
        self.duration = 0
        self.end_time = None
        self.running = False

    def start(self, seconds):
        self.duration = seconds
        self.end_time = time.time() + seconds
        self.running = True

    def pause(self):
        if self.running:
            self.duration = max(0, self.end_time - time.time())
            self.running = False

    def reset(self):
        self.duration = 0
        self.end_time = None
        self.running = False

    def remaining(self):
        if not self.running:
            return self.duration
        return max(0, self.end_time - time.time())
