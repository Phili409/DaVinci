import tkinter
class TextTools:
    def __init__(self, canvasWidget):
        self.canvas = canvasWidget
    
    def PlaceBox(self, x, y):
        textBox = tkinter.Text(self.canvas, wrap=tkinter.WORD, width=20, height=1)
        textBox.place(x=x, y=y)
        textBox.focus()
        return textBox
    
    def PlaceText(self, box, Font, color):
        text = box.get("1.0", "end-1c")  
        x, y = box.winfo_x(), box.winfo_y()
        
        yOff = box.winfo_height()
        newY = y + yOff
        newX = x
        
        box.destroy()
        self.canvas.create_text(x, y, text=text, font=Font, fill=color)
        self.canvas.unbind("<Button-1>")
        return newY, newX

    