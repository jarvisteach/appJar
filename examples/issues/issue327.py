import sys
sys.path.append("../../")
import random
from appJar import gui

dicecolors = ["blue", "red", "white", "yellow", "green"]

def dice():
    canvas.itemconfig(rect, fill=random.choice(dicecolors))

with gui() as app:
    dicecolor = random.choice(dicecolors)
    canvas = app.addCanvas("dice")
    rect = app.addCanvasRectangle("dice", x=40, y=80, w=100, h=100, fill=dicecolor, tag="dice")
    app.button("Launch", dice)
