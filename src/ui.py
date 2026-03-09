import tkinter as tk
from tkinter import ttk
from stopwatch import Stopwatch
from timer import Timer

class StopwatchTimerUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Stopwatch & Timer")
        self.root.geometry("360x300")
        self.root.configure(bg="#1e1e1e")

        self.stopwatch = Stopwatch()
        self.timer = Timer()

        self.mode = "stopwatch"

        self._build_ui()
        self._update_display()

    def _build_ui(self):

        style = ttk.Style()
        style.theme_use("clam")

        self.display = tk.Label(
            self.root,
            text="00:00:00",
            font=("Segoe UI", 36),
            fg="white",
            bg="#1e1e1e"
        )
        self.display.pack(pady=20)

        self.time_input = ttk.Entry(self.root, justify="center")
        self.time_input.insert(0, "60")
        self.time_input.pack()

        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=20)

        ttk.Button(btn_frame, text="Start", command=self.start).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="Pause", command=self.pause).grid(row=0, column=1, padx=5)
        ttk.Button(btn_frame, text="Reset", command=self.reset).grid(row=0, column=2, padx=5)

        mode_frame = ttk.Frame(self.root)
        mode_frame.pack()

        ttk.Button(mode_frame, text="Stopwatch", command=self._set_stopwatch).grid(row=0, column=0, padx=5)
        ttk.Button(mode_frame, text="Timer", command=self._set_timer).grid(row=0, column=1, padx=5)

    def _set_stopwatch(self):
        self.mode = "stopwatch"

    def _set_timer(self):
        self.mode = "timer"

    def start(self):
        if self.mode == "stopwatch":
            self.stopwatch.start()
        else:
            seconds = int(self.time_input.get())
            self.timer.start(seconds)

    def pause(self):
        if self.mode == "stopwatch":
            self.stopwatch.pause()
        else:
            self.timer.pause()

    def reset(self):
        if self.mode == "stopwatch":
            self.stopwatch.reset()
        else:
            self.timer.reset()

    def _update_display(self):

        if self.mode == "stopwatch":
            seconds = int(self.stopwatch.get_time())
        else:
            seconds = int(self.timer.remaining())

        hrs = seconds // 3600
        mins = (seconds % 3600) // 60
        secs = seconds % 60

        self.display.config(text=f"{hrs:02}:{mins:02}:{secs:02}")

        self.root.after(200, self._update_display)

    def run(self):
        self.root.mainloop()
