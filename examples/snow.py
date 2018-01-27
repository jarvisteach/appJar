import sys
sys.path.append("../")

import random
from appJar import gui

def press(event):
    print("Clicked at: ", event.x, event.y)
    widg = event.widget.find_closest(event.x, event.y)
    c.itemconfig(widg, fill="blue")

flakes = []

def snow():
    newX = random.randrange(c.winfo_width())
    flakes.append(app.addCanvasCircle("c", newX, 0, 20, fill="white", tag="flake"))
    for f in flakes:
        c.move(f, 0, 5)

    app.after(100, snow)

with gui("SNOW", "800x800") as app:
    c = app.canvas("c", bg="yellow")
#    c.bind("<Button-1>", press)
    app.setCanvasEvent("c", "flake", "<ButtonPress-1>", press)
    app.addCanvasRectangle("c", 50,50,200,100, fill="green")
    app.addCanvasOval("c", 100,200,200,100, fill="blue")
    app.addCanvasLine("c", 400,300,200,300, width=5, fill="blue")
    app.addCanvasText("c", 700,700, "hello", fill="blue")
    app.after(0, snow)
