import tkinter
from tkinter import font
from canvas import Canvas
from textTools import TextTools

class GUI:
    def __init__(self, root):
        ### Initializing the Widget
        self.root = root
        self.root.title("DaVinci Drawing App")
        self.canvasWidget = tkinter.Canvas(self.root, width=800, height=600, bg="white")
        self.canvasWidget.pack()
        
        
        # Initiate Canvas & Text Tool Objects
        self.Canvas = Canvas(self.canvasWidget)
        self.TextTools = TextTools(self.canvasWidget)
        
        # Board cordinates
        self.lastX = None
        self.lastY = None
        # Current Mode
        self.Mode = None
        
        # Custum Variables
        self.Color = "black"
        self.PixelSize = 4
        self.FontFamily = "Arial"
        self.FontSize = 12
        self.Bold = False
        self.FontColor = "black"
        self.Font = font.Font(family=self.FontFamily, size=self.FontSize, weight="bold" if self.Bold else "normal", )
        
        
        ### Buttons
        self.buttonStates = {
            "Draw" : tkinter.RAISED,
            "Erase" : tkinter.RAISED,
            "Text" : tkinter.RAISED,
        }
        #Function Buttons
        self.drawButton = tkinter.Button(self.root, text="Draw")
        self.eraseButton = tkinter.Button(self.root, text="Erase")
        self.clearButton = tkinter.Button(self.root, text="Clear", command=self.clearCanvas)
        self.textButton = tkinter.Button(self.root, text="Text")
        
        # Function Button Clicked
        self.drawButton.bind("<ButtonPress-1>", lambda event: self.toggleDrawingMode("Draw"))
        self.eraseButton.bind("<ButtonPress-1>", lambda event: self.toggleDrawingMode("Erase"))
        self.textButton.bind("<ButtonPress-1>", lambda event: self.toggleDrawingMode("Text"))
        
        
        ### Custumize Buttons
        # Color
        self.colorButton = tkinter.Menubutton(root, text=f"Colors\n{self.Color}", fg=self.Color, direction="below")
        self.colorMenu = tkinter.Menu(self.colorButton, tearoff=0)
        self.colorChoices = ["Red", "Green", "Yellow", "Blue", "Black", "White", "lightgray"]
        for color in self.colorChoices:
            self.colorMenu.add_command(label=color, command=lambda C=color: self.colorChange(color=C)) 
        self.colorButton.config(menu=self.colorMenu)
        
        # Font
        self.fontButton = tkinter.Menubutton(self.root, text=f"Font\n{self.FontFamily}",font=self.FontFamily, direction="below")
        self.fontMenu = tkinter.Menu(self.fontButton, tearoff=0)
        self.fontChoices = ["Centaur","Verdana","Symbol","Broadway","Algerian","Tahoma","@NSimSun","Bauhaus 93","@SimSun","System","Terminal","Modern","Script","Marlett","Arial","Consolas","Cambria","Calibri","Gabriola","Corbel","Modern"]
        for fontChoice in self.fontChoices:
            self.fontMenu.add_command(label=fontChoice, command=lambda font=fontChoice: self.fontChange(font))
        self.fontButton.config(menu=self.fontMenu)
        
        # Font Color
        self.fontColorButton = tkinter.Menubutton(root, text="Font Color", font=self.FontFamily, fg=self.FontColor, direction="below")
        self.fontColorMenu = tkinter.Menu(self.fontColorButton, tearoff=0)
        self.fontColors = ["Red", "Green", "Yellow", "Blue", "Black", "White", "lightgray"]
        for fontcolor in self.fontColors:
            self.fontColorMenu.add_command(label=fontcolor, command=lambda fontcolor=fontcolor: self.fontColorChange(font_color=fontcolor))
        self.fontColorButton.config(menu=self.fontColorMenu)


        ### Sizing Buttons
        # Font Size
        self.fontSizeButton = tkinter.Menubutton(self.root, text=f"Font Size\n{self.FontSize}", direction="below")
        self.fontSizeMenu = tkinter.Menu(self.fontSizeButton, tearoff=0)
        self.fontSizes = [10, 12, 14, 18, 22, 28]
        for fontsize in self.fontSizes:
            self.fontSizeMenu.add_command(label=fontsize, command= lambda fontsize=fontsize: self.fontSizeChange(size=fontsize))
        self.fontSizeButton.config(menu=self.fontSizeMenu)
        
        # Drawing/Erasing Pixel Size
        self.pixelSizeButton = tkinter.Menubutton(root, text=f"Pixel Size\n{self.PixelSize}", direction="below")
        self.pixelSizeMenu = tkinter.Menu(self.pixelSizeButton, tearoff=0)
        self.PixelSizes = [1, 2, 3, 4]
        for size in self.PixelSizes:
            self.pixelSizeMenu.add_command(label=size, command=lambda S=size: self.pixelSizeChange(size=S))
        self.pixelSizeButton.config(menu=self.pixelSizeMenu)
        
        # Bold Button
        self.boldButton = tkinter.Button(self.root, text="Bold", command=self.boldChange)
        
        
        ### Sliding Buttons left across the tool bar
        # Left Buttons, will contain the function buttons
        self.drawButton.pack(side="left"), self.eraseButton.pack(side="left"), self.clearButton.pack(side="left"), self.textButton.pack(side="left")
        
        # Right Buttons, will contain the custumizable buttons
        self.colorButton.pack(side="right"), self.fontColorButton.pack(side="right"), self.fontButton.pack(side="right"), self.fontSizeButton.pack(side="right"), self.pixelSizeButton.pack(side="right"), self.boldButton.pack(side="right")
        
    ### Updating Linked Canvas Nodes
    #def saveCanvas(self):
        #snapshot = self.canvasWidget.postscript(colormode="color")
        #t = self.linkedCanvas.prev
        #self.linkedCanvas.prev = linkedCanvas(snapshot)
        #self.linkedCanvas.prev.prev = t
        
        
    #def Undo(self, event):
        #if self.linkedCanvas.prev:
            #temp = self.linkedCanvas.current
            #self.linkedCanvas.current = self.linkedCanvas.prev
            #self.linkedCanvas.next = linkedCanvas(temp)
            
    #def Redu(self, event):
        #if self.linkedCanvas.next:
            #temp = self.linkedCanvas.current
            #tempPrev = self.linkedCanvas.prev 
            #self.linkedCanvas.current = self.linkedCanvas.next.current
            #self.linkedCanvas.prev = linkedCanvas(temp).prev = tempPrev
            
    def loadCanvas(self):
        pass
      
    ### Drawing Mode Toggle
    def toggleDrawingMode(self, Mode):
        self.Mode = Mode
        print(self.Mode)
        self.drawButton.configure(background="lightgray" if self.Mode == "Draw" else "white")
        self.eraseButton.configure(background="lightgray" if self.Mode == "Erase" else "white")
        self.textButton.configure(background="lightgray" if self.Mode == "Text" else "white")
        
        # Unbind all events and then bind appropriate events based on the mode
        self.canvasWidget.unbind("<Button-1>")
        self.canvasWidget.unbind("<B1-Motion>")
        self.canvasWidget.unbind("<ButtonRelease-1>")
        
        match self.Mode:
            case ("Draw"):
                self.bindDraw()
            case ("Erase"):
                self.bindErase()
            case ("Text"):
                self.bindText()
        
            
    ### Update Mutable Variables 
    # Font
    def updateFont(self):
        self.Font = font.Font(family=self.FontFamily, size=self.FontSize, weight="bold" if self.Bold else "normal")
    def fontChange(self, font):
        self.FontFamily = font
        print(font)
        self.updateFont()
        self.fontButton.config(text=f"Font\n{self.FontFamily}", font=self.FontFamily)
        
    # Color
    def colorChange(self, color):
        self.Color = color
        print(color)
        self.colorButton.config(text=f"Color\n{self.Color}", fg=self.Color)
    def boldChange(self):
        self.Bold = False if self.Bold else True
        print(self.Bold)
        self.boldButton.configure(background="lightgray" if self.Bold else "white")
        self.updateFont()
    def fontColorChange(self, font_color):
        self.FontColor = font_color
        print(font_color)
        self.fontColorButton.config(font=self.FontFamily, fg=font_color)
        
    # Size
    def fontSizeChange(self, size):
        self.FontSize = size
        print(size)
        self.updateFont()
        self.fontSizeButton.config(text=f"Font Size\n{self.FontSize}")
    def pixelSizeChange(self, size):
        self.PixelSize = 4 * size
        print(size)
        self.updateFont()
        self.pixelSizeButton.config(text=f"Pixel Size\n{self.PixelSize}")
    
    
    ### Binding Functions for updating to canvas
    def bindDraw(self):
        self.canvasWidget.bind("<Button-1>", self.startDrawing)
        self.canvasWidget.bind("<B1-Motion>", self.Draw)
        self.canvasWidget.bind("<ButtonRelease-1>", self.stopDrawing)
        
    def bindErase(self):
        self.canvasWidget.bind("<Button-1>", self.startErasing)
        self.canvasWidget.bind("<B1-Motion>", self.Erase)
        self.canvasWidget.bind("<ButtonRelease-1>", self.stopErasing)
            
    def bindText(self):
        self.canvasWidget.bind("<Button-1>", self.Write)
        
        
    ### Drawing Functions
    def startDrawing(self, event=None):
        print("Drawing")
        if event:
            self.lastX, self.lastY = event.x, event.y
            self.Canvas.Draw(lastX= self.lastX-1, lastY=self.lastY-1, x=self.lastX+1, y=self.lastY+1, fill=self.Color, width=self.PixelSize)

    def Draw(self, event):
        x , y = event.x , event.y
        self.Canvas.Draw(lastX= self.lastX, lastY=self.lastY, x=x, y=y, fill=self.Color, width=self.PixelSize)
        self.lastX, self.lastY = x, y
            
    def stopDrawing(self, event):
        self.lastX = None
        self.lastY = None
       
            
    ### Erasing Functions
    def startErasing(self, event=None):
        print("Erasing")
        if event:
            self.Canvas.Erase(x=event.x, y=event.y , radius=self.PixelSize)
            self.lastX, self.lastY = event.x, event.y
            
    def Erase(self, event):
        x, y = event.x, event.y
        self.Canvas.Erase(x=event.x, y=event.y , radius=self.PixelSize)
        self.lastX, self.lastY = x, y
        
    def stopErasing(self, event):
        self.lastX, self.lastY = None, None
        
    def clearCanvas(self):
        self.Canvas.ClearBoard()
        
        
    ### Text Functions
    def PlaceText(self, box):
        newY, newX = self.TextTools.PlaceText(box=box, Font=self.Font, color=self.FontColor)
        self.Write(event=None, initialY=newY, initialX=newX)

    def Write(self, event, initialY=None, initialX=None):
        x = event.x if event else initialX
        y =  event.y if event else initialY
        txtBox = self.TextTools.PlaceBox(x=x, y=y)
        txtBox.bind("<Return>", lambda event, box=txtBox: self.PlaceText(box))
        self.canvasWidget.bind("<Button-1>", lambda event, box=txtBox: self.TextTools.PlaceText(box, Font=self.Font, color=self.FontColor))
        self.Mode = None
        
        
        

        
    