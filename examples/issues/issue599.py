import sys
sys.path.append("../../")

from appJar import gui

def changeColour():
    col = app.colourBox()
    if col is not None:
        app.bg = col

with gui("Colour Changer", "500x500") as app:
    app.labelFont = {'size':34, 'weight':'bold'}
    app.label("Press the button...")
    app.button("Change the Colour", changeColour)
