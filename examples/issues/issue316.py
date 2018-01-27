import sys
sys.path.append("../../")
from appJar import gui

def press(btn):
    print(btn)

app = gui()

app.addButton("PRESS", press)
app.addButton("IMG", press)
app.setButtonImage("IMG", "img2.gif", "right")
app.addIconButton("OPEN", press, "OPEN", align="top")
app.addImageButton("About", press, "bStar.png", align="left")
app.addImageButton("Apply", press, "bTick.png", align="right")

app.go()
