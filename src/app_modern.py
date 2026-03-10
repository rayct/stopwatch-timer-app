# src/app_modern.py

import customtkinter as ctk
from stopwatch import Stopwatch
from timer import Timer
from datetime import timedelta

ctk.set_appearance_mode("dark")  # "dark" or "light"
ctk.set_default_color_theme("blue")  # or "green", "dark-blue"

class ModernStopwatchTimerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Stopwatch & Timer")
        self.geometry("400x300")

        self.stopwatch = Stopwatch()
        self.timer = Timer()
        self.mode = "stopwatch"

        self._build_ui()
        self._update_display()

    def _build_ui(self):
        # Display
        self.display = ctk.CTkLabel(self, text="00:00:00", font=ctk.CTkFont(size=40, weight="bold"))
        self.display.pack(pady=20)

        # Timer input
        self.timer_entry = ctk.CTkEntry(self, width=120, justify="center", font=ctk.CTkFont(size=16))
        self.timer_entry.insert(0, "60")  # default 60 seconds
        self.timer_entry.pack(pady=5)

        # Mode buttons
        mode_frame = ctk.CTkFrame(self, fg_color="transparent")
        mode_frame.pack(pady=10)
        ctk.CTkButton(mode_frame, text="Stopwatch", width=120, command=self._set_stopwatch).grid(row=0, column=0, padx=5)
        ctk.CTkButton(mode_frame, text="Timer", width=120, command=self._set_timer).grid(row=0, column=1, padx=5)

        # Controls
        control_frame = ctk.CTkFrame(self, fg_color="transparent")
        control_frame.pack(pady=10)
        ctk.CTkButton(control_frame, text="Start", width=80, command=self.start).grid(row=0, column=0, padx=5)
        ctk.CTkButton(control_frame, text="Pause", width=80, command=self.pause).grid(row=0, column=1, padx=5)
        ctk.CTkButton(control_frame, text="Reset", width=80, command=self.reset).grid(row=0, column=2, padx=5)

    # Mode Switch
    def _set_stopwatch(self):
        self.mode = "stopwatch"
        self.timer_entry.configure(state="disabled")

    def _set_timer(self):
        self.mode = "timer"
        self.timer_entry.configure(state="normal")

    # Control Actions
    def start(self):
        if self.mode == "stopwatch":
            self.stopwatch.start()
        else:
            seconds = int(self.timer_entry.get())
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

    # Display Update
    def _update_display(self):
        if self.mode == "stopwatch":
            t = int(self.stopwatch.get_time())
        else:
            t = int(self.timer.remaining())
        hrs = t // 3600
        mins = (t % 3600) // 60
        secs = t % 60
        self.display.configure(text=f"{hrs:02}:{mins:02}:{secs:02}")
        self.after(200, self._update_display)

if __name__ == "__main__":
    app = ModernStopwatchTimerApp()
    app.mainloop()
