import tkinter as tk
from tkinter import colorchooser

import tool

class ButtonBase(tk.Button):
    def __init__(self, parent, text, command):
        super().__init__(parent, text=text, command=command, width=10)
        self.pack(side=tk.LEFT)

class PencilButton(ButtonBase): pass
class EraserButton(ButtonBase): pass
class ShapeButton(ButtonBase): pass

class ColorPicker(tk.Button):
    def __init__(self, parent):
        super().__init__(parent, text="Color", command=self.pick_color, width=10)
        self.app = parent.app
        self.pack(side=tk.LEFT)

    def pick_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.app.set_color(color)
            self.config(bg=color)

class ClearButton(ButtonBase): pass