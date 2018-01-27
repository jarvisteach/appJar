import sys
sys.path.append("../")

import random
from appJar import gui

def press(event):
    widg = event.widget.find_closest(event.x, event.y)
    c.itemconfig(widg, fill="blue")

flakes = []

def snow():
    newX = random.randrange(c.winfo_width())
    flakes.append(app.addCanvasCircle("c", newX, 0, 20, fill="white", tag="flake"))
    for f in flakes:
        newY = random.randint(-5, 5)
        c.move(f, newY, 5)

    app.after(100, snow)

with gui("SNOW", "800x800") as app:
    app.addMenuEdit()
    app.entry("e1")
    app.setFont(size=40)
    with app.tabbedFrame("tf") as tf:
        with app.tab("Tab 1"):
            c = app.canvas("c", bg="yellow")
            app.label("l1", "Hello from the label")
            app.message("m1", "sdfsdfsdf sdf s df sdf sdf  sdf")
            app.setCanvasEvent("c", "flake", "<ButtonPress-1>", press)
            app.addCanvasRectangle("c", 50,50,200,100, fill="green")
            app.addCanvasOval("c", 100,200,200,100, fill="blue")
            app.addCanvasLine("c", 400,300,200,300, width=5, fill="blue")
            app.addCanvasText("c", 700,700, "hello", fill="blue")
            app.after(0, snow)
        with app.tab("Tab 2"):
            pass
        with app.tab("Tab 3"):
            pass
        with app.tab("Tab 4"):
            pass
