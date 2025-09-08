import tkinter as tk
from tkinter import ttk
from tool import *

import button

class Toolbar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="lightgray")
        self.app = parent  
        self.pack(side=tk.TOP, fill=tk.X)

        # Tool buttons
        button.PencilButton(self, "Pencil", lambda: self.app.set_tool(Pencil(self.app.canvas)))
        button.EraserButton(self, "Eraser", lambda: self.app.set_tool(Eraser(self.app.canvas)))

        self.size_slider = tk.Scale(self, from_=1, to=50, orient=tk.HORIZONTAL, command=self.change_size)
        self.size_slider.set(2)
        self.size_slider.pack(side=tk.LEFT)
                
        # Shapes
        self.shape_var = tk.StringVar(value="Rectangle")
        shape_dropdown = ttk.Combobox(self, textvariable=self.shape_var, values=["Rectangle", "Circle", "Polygon"], state="readonly", width=10)
        shape_dropdown.pack(side=tk.LEFT, padx=5)
        shape_dropdown.bind("<<ComboboxSelected>>", self.select_shape_tool)

        self.fill = tk.BooleanVar(value=False)
        fill_checkbox = tk.Checkbutton(self, text="Fill", variable=self.fill)
        fill_checkbox.pack(side=tk.LEFT, padx=(2, 2))



        # Color picker and clear
        button.ColorPicker(self)
        button.ClearButton(self, "Clear", self.app.clear_canvas)

        # Undo/Redo
        tk.Button(self, text="Undo", command=self.app.canvas.undo).pack(side=tk.LEFT, padx=0)
        tk.Button(self, text="Redo", command=self.app.canvas.redo).pack(side=tk.LEFT, padx=0)

    def select_shape_tool(self, event=None):
        shape = self.shape_var.get().lower()
        self.app.set_tool(ShapeTool(self.app.canvas, shape))

    def change_size(self, val):
        self.app.set_pencil_size(int(val))

