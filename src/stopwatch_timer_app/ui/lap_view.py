import customtkinter as ctk


class LapView(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.laps = []

        self.label = ctk.CTkLabel(self, text="Laps")
        self.label.pack()

        self.box = ctk.CTkTextbox(self, height=100)
        self.box.pack(fill="both", expand=True)

    def add_lap(self, lap_time):

        self.laps.append(lap_time)

        self.box.insert("end", f"Lap {len(self.laps)}   {lap_time}\n")
        self.box.see("end")
