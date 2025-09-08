import tkinter as tk

class Tool:
    def __init__(self, canvas):
        self.canvas = canvas

    def on_press(self, event):
        pass

    def on_drag(self, event):
        pass

    def on_release(self, event):
        pass

class Pencil:
    def __init__(self, canvas):
        self.canvas = canvas
        self.size = self.canvas.app.pencil_size
        self.points = []

    def on_press(self, event):
        self.points = [(event.x, event.y)]
        if not self.canvas.app.check_size(self.size):
            self.size = self.canvas.app.pencil_size

    def on_drag(self, event):
        self.points.append((event.x, event.y))
        if len(self.points) >= 2:
            x1 = self.points[-2]
            y1 = self.points[-2]
            x2 = self.points[-1]
            y2 = self.points[-1]
            self.canvas.create_line(x1, y1, x2, y2,
                                    fill=self.canvas.app.selected_color,
                                    width=self.size,
                                    capstyle=tk.ROUND,
                                    smooth=True)

    def on_release(self, event):
        if len(self.points) >= 2:
            line_points = []
            for point in self.points:
                for coord in point:
                    line_points.append(coord)
            options = {"fill": self.canvas.app.selected_color,
                       "width": self.size,
                       "capstyle": tk.ROUND,
                       "smooth": True}
            self.canvas.create_line(*line_points, **options)
            action = {"type": "line",
                      "coords": line_points,
                      "options": options}
            self.canvas.add_draw_action(action)
            self.points = []


class Eraser(Pencil):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.canvas = canvas
        self.size = self.canvas.app.pencil_size

    def on_press(self, event):
        self.points = [(event.x, event.y)]
        if not self.canvas.app.check_size(self.size):
            self.size = self.canvas.app.pencil_size

    def on_drag(self, event):
        self.points.append((event.x, event.y))
        if len(self.points) >= 2:
            x1 = self.points[-2]
            y1 = self.points[-2]
            x2 = self.points[-1]
            y2 = self.points[-1]
            self.canvas.create_line(x1, y1, x2, y2,
                                    fill="white",
                                    width=self.size,
                                    capstyle=tk.ROUND,
                                    smooth=True)

    def on_release(self, event):
        if len(self.points) >= 2:
            line_points = []
            for point in self.points:
                for coord in point:
                    line_points.append(coord)
            options = {"fill": "white", "width": self.size, "capstyle": tk.ROUND, "smooth": True}
            self.canvas.create_line(*line_points, **options)
            action = {"type": "line", "coords": line_points, "options": options}
            self.canvas.add_draw_action(action)
        self.points = []

class ShapeTool(Tool):
    def __init__(self, canvas, shape):
        super().__init__(canvas)
        self.canvas = canvas
        self.shape = shape
        if self.shape == "circle":
            self.shape = "oval"
        self.points = []
        self.markers = []
        self.marker_size = 5

    def on_press(self, event):
        self.points.append((event.x, event.y))
        self.markers.append(self.canvas.create_oval(
            event.x - self.marker_size, event.y - self.marker_size,
            event.x + self.marker_size, event.y + self.marker_size,
            outline="black"))
        fill_enabled = self.canvas.app.toolbar.fill.get()
        color = self.canvas.app.selected_color
        if self.shape in ("rectangle", "oval") and len(self.points) == 2:
            x1, y1 = self.points[0]
            x2, y2 = self.points[1]
            coords = (x1, y1, x2, y2)
            options = {"width": 2, "fill": "white", "outline": "black"}

            if fill_enabled:
                options["fill"] = color
                options["outline"] = color
            else:
                options["outline"] = color
                options["fill"] = None
                options["width"] = 2

            if self.shape == "rectangle":
                self.canvas.create_rectangle(*coords, **options)
                shape_type = "rectangle"
            elif self.shape == "oval":
                self.canvas.create_oval(*coords, **options)
                shape_type = "oval"

            action = {
                "type": shape_type,
                "coords": coords,
                "options": options
            }
            self.canvas.add_draw_action(action)
            self.reset()

        elif self.shape == "polygon" and self.closed_shape():
            flattened = [val for point in self.points for val in point]
            options = {"fill": "white", "outline": "black"}

            if fill_enabled:
                options["fill"] = color
                options["outline"] = color
            else:
                options["outline"] = color
                options["width"] = 2

            self.canvas.create_polygon(*flattened, **options)
            action = {
                "type": "polygon",
                "coords": flattened,
                "options": options
            }
            self.canvas.add_draw_action(action)
            self.reset()

    def reset(self):
        self.points = []
        for marker in self.markers:
            self.canvas.delete(marker)
        self.markers = []

    def closed_shape(self):
        if len(self.points) <= 2:
            return False
        return (abs(self.points[0][0] - self.points[-1][0]) < self.marker_size and
                abs(self.points[0][1] - self.points[-1][1]) < self.marker_size)