import sys
sys.path.append("../../")
import tkinter as tk


from appJar import gui

class MyCustomFrame(tk.Frame):
    def __init__(self, title, parent):
        tk.Frame.__init__(self, parent)
        # .... stuff within the frame ....
        self.label = tk.Label(self, text='Hello')
        self.label.grid(row=0, column=0) 

app = gui()
fr = MyCustomFrame("name", app._gui__getContainer())
app._gui__positionWidget(fr, 2, 1)
app.go()
