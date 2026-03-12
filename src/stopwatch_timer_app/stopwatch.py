import time

class Stopwatch:

    def __init__(self):
        self.start_time = None
        self.elapsed = 0  # cumulative elapsed time while running
        self.running = False
        self._laps = []
        self._last_lap_elapsed = 0  # cumulative elapsed at last lap

    def start(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True

    def pause(self):
        if self.running:
            self.elapsed += time.time() - self.start_time
            self.running = False
            self.start_time = None

    def reset(self):
        self.start_time = None
        self.elapsed = 0
        self.running = False
        self._laps = []
        self._last_lap_elapsed = 0

    def get_time(self):
        """Return total elapsed time in seconds."""
        if self.running:
            return self.elapsed + (time.time() - self.start_time)
        return self.elapsed

    # ---------- LAP FUNCTIONALITY ----------
    def lap(self):
        """Record a lap and return its duration."""
        current_elapsed = self.get_time()
        lap_time = current_elapsed - self._last_lap_elapsed
        self._laps.append(lap_time)
        self._last_lap_elapsed = current_elapsed
        return lap_time

    def get_laps(self):
        """Return a copy of all recorded laps."""
        return self._laps.copy()
