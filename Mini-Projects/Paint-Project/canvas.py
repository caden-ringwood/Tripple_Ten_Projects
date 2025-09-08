import tkinter as tk

class Canvas(tk.Canvas):
    def __init__(self, parent, app):
        super().__init__(parent, bg="white")
        self.after(0, self.bind_events)
        self.app = app

        self.undo_list = []
        self.redo_list = []

    def bind_events(self):
        self.bind("<ButtonPress-1>", self.app.on_press)
        self.bind("<B1-Motion>", self.app.on_drag)
        self.bind("<ButtonRelease-1>", self.app.on_release)

    def clear(self):
        self.delete("all")

    def add_draw_action(self, action):
        self.undo_list.append(action)
        self.redo_list.clear()

    def undo(self):
        if self.undo_list:
            self.clear()
            drawing = self.undo_list.pop()
            self.redo_list.append(drawing)
            for action in self.undo_list:
                self.draw_action(action)

    def redo(self):
        if self.redo_list:
            drawing = self.redo_list.pop()
            self.undo_list.append(drawing)
            self.draw_action(drawing)

    def draw_action(self, drawing):
        shape_type = drawing["type"]
        coords = drawing["coords"]
        options = drawing["options"]

        if shape_type == "line":
            self.create_line(*coords, **options)
        elif shape_type == "rectangle":
            self.create_rectangle(*coords, **options)
        elif shape_type == "oval":
            self.create_oval(*coords, **options)
        elif shape_type == "arc":
            self.create_arc(*coords, **options)
        elif shape_type == "polygon":
            self.create_polygon(*coords, **options)