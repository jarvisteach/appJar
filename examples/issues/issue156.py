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

    def config(self, cnf=None, **kw):
        self.configure(cnf, **kw)

    def configure(self, cnf=None, **kw):
        self.label.config(cnf, **kw)

def press(btn):
    print(btn)

app = gui()
#app.setLogLevel("DEBUG")
app.startLabelFrame("My Widg")
fr = MyCustomFrame("name", app.getContainer())
app.addWidget("gen", fr, 2, 1)
app.setWidgetTooltip("gen", "tooltip here")
app.setWidgetBg("gen", "green")
app.setWidgetCursor("gen", "hand")
app.setWidgetRightClickMenu("gen", press)
app.addLabel("l1", "labels here")
app.setLabelBg("l1", "yellow")
app.stopLabelFrame()
app.go()
