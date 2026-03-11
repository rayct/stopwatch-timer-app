import customtkinter as ctk
from stopwatch_timer_app.stopwatch import Stopwatch
from stopwatch_timer_app.timer import Timer
from stopwatch_timer_app.sound import play_alarm
from stopwatch_timer_app.ui.roller import Roller
from stopwatch_timer_app.ui.lap_view import LapView


class StopwatchTimerUI(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Stopwatch & Timer")
        self.geometry("420x520")

        self.stopwatch = Stopwatch()
        self.timer = Timer()

        self.mode = "stopwatch"

        self._build_ui()
        self._update_display()

    def _build_ui(self):

        self.display = ctk.CTkLabel(
            self,
            text="00:00:00",
            font=ctk.CTkFont(size=44, weight="bold")
        )
        self.display.pack(pady=20)

        roller_frame = ctk.CTkFrame(self)
        roller_frame.pack()

        self.hours = Roller(roller_frame, 0, 23)
        self.hours.grid(row=0, column=0, padx=10)

        self.minutes = Roller(roller_frame, 0, 59)
        self.minutes.grid(row=0, column=1, padx=10)

        self.seconds = Roller(roller_frame, 0, 59)
        self.seconds.grid(row=0, column=2, padx=10)

        mode_frame = ctk.CTkFrame(self)
        mode_frame.pack(pady=10)

        ctk.CTkButton(mode_frame, text="Stopwatch",
                      command=lambda: self._set_mode("stopwatch")).grid(row=0, column=0, padx=10)

        ctk.CTkButton(mode_frame, text="Timer",
                      command=lambda: self._set_mode("timer")).grid(row=0, column=1, padx=10)

        control_frame = ctk.CTkFrame(self)
        control_frame.pack(pady=10)

        ctk.CTkButton(control_frame, text="Start", command=self.start).grid(row=0, column=0, padx=10)
        ctk.CTkButton(control_frame, text="Pause", command=self.pause).grid(row=0, column=1, padx=10)
        ctk.CTkButton(control_frame, text="Reset", command=self.reset).grid(row=0, column=2, padx=10)
        ctk.CTkButton(control_frame, text="Lap", command=self.lap).grid(row=0, column=3, padx=10)

        self.lap_view = LapView(self)
        self.lap_view.pack(fill="both", expand=True, padx=10, pady=10)

        theme_button = ctk.CTkButton(self, text="Toggle Theme", command=self._toggle_theme)
        theme_button.pack(pady=5)

    def _toggle_theme(self):

        mode = ctk.get_appearance_mode()

        if mode == "Dark":
            ctk.set_appearance_mode("light")
        else:
            ctk.set_appearance_mode("dark")

    def _set_mode(self, mode):
        self.mode = mode

    def start(self):

        if self.mode == "stopwatch":

            self.stopwatch.start()

        else:

            seconds = (
                self.hours.get() * 3600 +
                self.minutes.get() * 60 +
                self.seconds.get()
            )

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

    def lap(self):

        if self.mode == "stopwatch":

            t = int(self.stopwatch.get_time())

            hrs = t // 3600
            mins = (t % 3600) // 60
            secs = t % 60

            self.lap_view.add_lap(f"{hrs:02}:{mins:02}:{secs:02}")

    def _update_display(self):

        if self.mode == "stopwatch":
            t = int(self.stopwatch.get_time())
        else:
            t = int(self.timer.remaining())

            if t == 0 and self.timer.running:
                play_alarm()

        hrs = t // 3600
        mins = (t % 3600) // 60
        secs = t % 60

        self.display.configure(text=f"{hrs:02}:{mins:02}:{secs:02}")

        self.after(200, self._update_display)
