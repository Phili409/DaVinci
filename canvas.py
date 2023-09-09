

class Canvas:
    def __init__(self, canvasWidget):
        self.canvas = canvasWidget
        
    def Draw(self, lastX, lastY, x, y, fill, width):
        self.canvas.create_line(lastX, lastY, x, y, fill=fill, width=width)
        
    def Erase(self, x, y, radius):
        radius = radius * 1.25
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="white", outline="white")
        
    def ClearBoard(self):
        self.canvas.delete("all")
    
    def getCanvas(self):
        return self.canvas