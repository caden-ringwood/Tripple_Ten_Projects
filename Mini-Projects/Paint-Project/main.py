import tkinter as tk
import canvas
import tool
import toolbar

class PaintApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Paint Clone")
        self.geometry("800x600")

        self.selected_color = "black"
        self.pencil_size = 2

        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = canvas.Canvas(self.canvas_frame, self) 
        self.canvas.bind_events()  
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.current_tool = tool.Pencil(self.canvas)
        self.toolbar = toolbar.Toolbar(self)

    def set_tool(self, tool_instance):
        self.current_tool = tool_instance

    def set_pencil_size(self, size):
        self.pencil_size = size
        
    def check_size(self, size):
        if size == self.pencil_size:
            return True
        return False

    def set_color(self, color):
        self.selected_color = color

    def clear_canvas(self):
        self.canvas.clear()

    def on_press(self, event):
        self.current_tool.on_press(event)

    def on_drag(self, event):
        self.current_tool.on_drag(event)

    def on_release(self, event):
        self.current_tool.on_release(event)

if __name__ == "__main__":
    app = PaintApp()
    app.mainloop()
