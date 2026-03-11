import tkinter as tk


class Roller(tk.Frame):

    def __init__(self, parent, min_val=0, max_val=59, width=70, height=150):
        super().__init__(parent)

        self.min_val = min_val
        self.max_val = max_val
        self.values = list(range(min_val, max_val + 1))

        self.value = tk.IntVar(value=0)

        self.canvas = tk.Canvas(self, width=width, height=height, highlightthickness=0)
        self.canvas.pack()

        self.item_height = 30
        self.center = height // 2

        self.items = []

        for i, v in enumerate(self.values):

            y = i * self.item_height

            item = self.canvas.create_text(
                width // 2,
                y,
                text=f"{v:02}",
                font=("Segoe UI", 18)
            )

            self.items.append(item)

        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        self._draw_highlight(width, height)

        self.canvas.bind("<MouseWheel>", self._scroll)
        self.canvas.bind("<ButtonRelease-1>", self._snap)

    def _draw_highlight(self, width, height):

        self.canvas.create_rectangle(
            0,
            self.center - 15,
            width,
            self.center + 15,
            outline="#4da6ff",
            width=2
        )

    def _scroll(self, event):

        delta = -1 if event.delta > 0 else 1
        self.canvas.yview_scroll(delta, "units")

        self._update_visuals()

    def _snap(self, event=None):

        pos = self.canvas.canvasy(self.center)
        index = round(pos / self.item_height)

        index = max(0, min(index, len(self.values) - 1))

        target = index * self.item_height - self.center
        self.canvas.yview_moveto(target / self.canvas.bbox("all")[3])

        self.value.set(self.values[index])

        self._update_visuals()

    def _update_visuals(self):

        for item in self.items:

            y = self.canvas.coords(item)[1]
            dist = abs(y - self.canvas.canvasy(self.center))

            if dist < 10:
                size = 20
                color = "white"
            elif dist < 40:
                size = 16
                color = "#cccccc"
            else:
                size = 12
                color = "#777777"

            self.canvas.itemconfig(item, font=("Segoe UI", size), fill=color)

    def get(self):
        return self.value.get()
