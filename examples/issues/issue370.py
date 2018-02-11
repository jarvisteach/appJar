import sys
sys.path.append("../../")
from appJar import gui

x = y = rect = -1

def press(event):
    ''' start a new rectangle at mouse click '''
    global x, y, rect
    x = event.x
    y = event.y
    rect = c.create_rectangle(x, y, x, y)

def drag(event):
    ''' redraw the rectangle, to new coorindates '''
    c.coords(rect, x, y, event.x, event.y)

with gui("Drawing") as app:
    c = app.canvas("canvas")
    c.bind("<ButtonPress-1>", press)
    c.bind("<B1-Motion>", drag)
